#!/usr/bin/env python3
"""
Obsidian graph connector for ~/forgetools vault.

What it does:
  1. Converts topic: strings → tags: YAML lists (what Obsidian actually uses for graph)
  2. Adds a content-type tag (idea / linkedin / article) per folder
  3. Fills in repurposed_from with [[wikilinks]] where LinkedIn posts / articles
     can be matched to source Ideas by keyword overlap

Run: python3 scripts/connect-graph.py
Use --dry-run to preview changes without writing files.
"""

import os
import re
import sys
from pathlib import Path

VAULT = Path(__file__).parent.parent
DRY_RUN = "--dry-run" in sys.argv

# ── Tag normalization ────────────────────────────────────────────────────────

NORMALIZE = {
    "1on1s": "1on1s",
    "1:1 methodology": "1on1s",
    "1:1 meetings": "1on1s",
    "1-on-1s": "1on1s",
    "feedback": "feedback",
    "coaching": "coaching",
    "management fundamentals": "management",
    "management": "management",
    "performance management": "performance-management",
    "performance reviews": "performance-reviews",
    "career development": "career-development",
    "career-development": "career-development",
    "delegation": "delegation",
    "trust": "trust",
    "consistency": "consistency",
    "communication": "communication",
    "difficult conversations": "difficult-conversations",
    "difficult-conversations": "difficult-conversations",
    "hiring": "hiring",
    "leadership": "leadership",
    "ai-workplace": "ai-workplace",
    "ai workplace": "ai-workplace",
    "team-culture": "team-culture",
    "team culture": "team-culture",
    "team dynamics": "team-dynamics",
    "team-dynamics": "team-dynamics",
    "presentations": "presentations",
    "job-search": "job-search",
    "job search": "job-search",
    "active-listening": "active-listening",
    "active listening": "active-listening",
    "vendor-management": "vendor-management",
    "vendor management": "vendor-management",
    "empathetic-leadership": "empathetic-leadership",
    "empathetic leadership": "empathetic-leadership",
    "continuous-learning": "continuous-learning",
    "continuous learning": "continuous-learning",
    "problem-solving": "problem-solving",
    "problem solving": "problem-solving",
    "retention": "retention",
    "managing up": "managing-up",
    "managing-up": "managing-up",
    "psychological safety": "psychological-safety",
    "psychological-safety": "psychological-safety",
    "self-coaching": "manager-development",
    "manager development": "manager-development",
    "manager-development": "manager-development",
    "self-awareness": "self-awareness",
    "talent development": "talent-development",
    "talent-development": "talent-development",
    "promotion": "promotion",
    "recognition": "recognition",
    "project-planning": "project-planning",
    "project planning": "project-planning",
    "documentation": "documentation",
    "work-travel": "work-travel",
    "work travel": "work-travel",
    "high performers": "high-performers",
    "high-performers": "high-performers",
    "retention, management": "retention",  # will split below
}

def normalize_tags(raw: str) -> list[str]:
    """Convert a raw topic string like 'feedback, coaching' into normalized tag list."""
    tags = []
    for part in raw.split(","):
        part = part.strip().lower()
        if not part:
            continue
        normalized = NORMALIZE.get(part, part.replace(" ", "-"))
        if normalized not in tags:
            tags.append(normalized)
    return tags


# ── Frontmatter parsing ──────────────────────────────────────────────────────

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def parse_fm(text: str) -> tuple[dict, str]:
    """Returns (frontmatter_dict, body). Very lightweight — not a full YAML parser."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    body = text[m.end():]
    fm: dict = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm, body

def render_fm(fm: dict) -> str:
    lines = ["---"]
    for k, v in fm.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n"


# ── Cross-link matching ──────────────────────────────────────────────────────

def keywords_from_path(p: Path) -> set[str]:
    """Extract meaningful words from a filename for fuzzy matching."""
    name = p.stem.lower()
    # strip prefixes
    for prefix in ("post-", "article-"):
        if name.startswith(prefix):
            name = name[len(prefix):]
    stopwords = {"a", "an", "the", "to", "for", "of", "and", "or", "in", "on",
                 "is", "it", "its", "how", "what", "why", "when", "who", "your",
                 "you", "i", "my", "be", "not", "dont", "with", "that", "this",
                 "from", "at", "by", "up", "do", "so", "but", "can", "vs"}
    words = set(re.split(r"[-_\s]+", name)) - stopwords
    return {w for w in words if len(w) > 2}

def build_idea_index(ideas_dir: Path) -> list[tuple[Path, set[str]]]:
    index = []
    for p in ideas_dir.glob("*.md"):
        index.append((p, keywords_from_path(p)))
    return index

def find_best_idea(source: Path, idea_index: list[tuple[Path, set[str]]]) -> Path | None:
    source_kw = keywords_from_path(source)
    if not source_kw:
        return None
    best_path, best_score = None, 0
    for idea_path, idea_kw in idea_index:
        score = len(source_kw & idea_kw)
        if score > best_score and score >= 2:  # require at least 2 shared keywords
            best_score, best_path = score, idea_path
    return best_path


# ── File processing ──────────────────────────────────────────────────────────

def content_type_for(path: Path) -> str:
    parts = path.parts
    if "LinkedIn" in parts:
        return "linkedin"
    if "Articles" in parts:
        return "article"
    if "Ideas" in parts:
        return "idea"
    return ""

def process_file(path: Path, idea_index: list[tuple[Path, set[str]]]) -> bool:
    """Returns True if the file was (or would be) modified."""
    text = path.read_text(encoding="utf-8")
    fm, body = parse_fm(text)

    if not fm:
        # No frontmatter — skip (we don't want to invent metadata for files we don't understand)
        return False

    changed = False

    # 1. Convert topic → tags
    raw_topic = fm.get("topic", "").strip()
    existing_tags_raw = fm.get("tags", "").strip()

    if raw_topic and not existing_tags_raw:
        tags = normalize_tags(raw_topic)
        ctype = content_type_for(path)
        if ctype and ctype not in tags:
            tags.insert(0, ctype)
        # Format as YAML inline list: [tag1, tag2]
        fm["tags"] = "[" + ", ".join(tags) + "]"
        changed = True
    elif not existing_tags_raw:
        ctype = content_type_for(path)
        if ctype:
            fm["tags"] = f"[{ctype}]"
            changed = True

    # 2. Fill repurposed_from for LinkedIn / Article notes
    rp = fm.get("repurposed_from", "").strip()
    ctype = content_type_for(path)
    if not rp and ctype in ("linkedin", "article"):
        best = find_best_idea(path, idea_index)
        if best:
            link = f"[[{best.stem}]]"
            fm["repurposed_from"] = link
            changed = True

    if not changed:
        return False

    new_text = render_fm(fm) + body
    if DRY_RUN:
        print(f"  [DRY RUN] {path.relative_to(VAULT)}")
        if fm.get("tags"):
            print(f"    tags: {fm['tags']}")
        if fm.get("repurposed_from"):
            print(f"    repurposed_from: {fm['repurposed_from']}")
    else:
        path.write_text(new_text, encoding="utf-8")

    return True


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    idea_index = build_idea_index(VAULT / "Content" / "Ideas")

    dirs = [
        VAULT / "Content" / "Ideas",
        VAULT / "Content" / "LinkedIn",
        VAULT / "Content" / "LinkedIn" / "Published",
        VAULT / "Content" / "Articles",
        VAULT / "Content" / "Articles" / "Published",
    ]

    total, modified = 0, 0
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            total += 1
            if process_file(path, idea_index):
                modified += 1

    verb = "Would modify" if DRY_RUN else "Modified"
    print(f"\n{verb} {modified} of {total} files.")
    if DRY_RUN:
        print("Run without --dry-run to apply changes.")

if __name__ == "__main__":
    main()
