# Content Dashboard

## 🔥 Ready to Publish
```dataview
TABLE type, topic, status
FROM "Content"
WHERE contains(status, "ready")
SORT type ASC
```

## ✍️ In Draft
```dataview
TABLE type, topic, status
FROM "Content"
WHERE contains(status, "draft")
SORT file.mtime DESC
```

## 💡 Ideas Backlog
```dataview
TABLE type, topic
FROM "Content"
WHERE contains(status, "idea")
SORT file.ctime DESC
```

## ✅ Published
```dataview
TABLE type, topic, published_date, published_url
FROM "Content"
WHERE contains(status, "published")
SORT published_date DESC
```

## LinkedIn
```dataview
TABLE type, status, topic, published_date
FROM "Content"
WHERE contains(type, "linkedin") OR contains(potential_format, "linkedin") OR contains(platforms, "linkedin")
SORT file.mtime DESC
```

## Articles (ManagerForge Blog)
```dataview
TABLE status, topic, published_date, published_url
FROM "Content"
WHERE contains(type, "article")
SORT file.mtime DESC
```

## Book
```dataview
TABLE status, chapter_number, section
FROM "Content"
WHERE contains(type, "book-chapter")
SORT chapter_number ASC
```
