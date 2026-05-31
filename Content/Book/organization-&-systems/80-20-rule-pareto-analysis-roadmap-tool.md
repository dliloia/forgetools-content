---
title: "The 80/20 Rule Is Actually a Roadmap Tool"
book_chapter: "organization-&-systems"
word_count: 1047
source_idea: the-80-20-rule-is-a-roadmap-tool.md
---

## The Analysis Nobody Actually Does

Early in my career I thought the goal of a roadmap meeting was to leave with a list everyone agreed on. It took me years to understand that consensus and correctness are not the same thing. A list that everyone agrees on might be a beautifully negotiated artifact with no relationship to what customers actually need. And in most organizations, that's exactly what it is.

The 80/20 rule gets cited constantly in roadmap conversations. It's used as a rhetorical device, a way of gesturing at prioritization without actually doing any. "We need to focus on the twenty percent that matters." Okay. Which twenty percent? Based on what? That's where the conversation usually stalls and someone with a louder voice or a more senior title fills the silence.

What Vilfredo Pareto actually observed, and what quality engineers like Joseph Juran built into a practical tool, was that distributions in complex systems are almost never uniform. A small number of causes account for a disproportionate share of the outcomes. That's not a motivational poster. It's a mathematical reality that shows up whether you're looking at manufacturing defects, customer support tickets, software bugs, or sales pipeline problems. The shape of the distribution is nearly always the same. A few things at the top are doing most of the damage.

The discipline is in doing the actual analysis instead of just nodding at the concept.

I remember sitting in a planning session at a previous company where the team spent three hours debating the roadmap for the next quarter. Every leader in the room had a clear view of what mattered most, and every view was different. The product team wanted to build a new feature that a key customer had requested. The ops team wanted to fix a workflow that was creating manual rework every week. The support team was exhausted from fielding a particular category of complaint that had been growing for months. Three smart groups of people, three different definitions of the problem.

Nobody had pulled the data.

When we finally did, the picture was unambiguous. That category of support complaint the support team was exhausted by? It was responsible for nearly forty percent of our total ticket volume and had a measurable correlation with customer churn in the sixty to ninety day window. The workflow the ops team wanted to fix was real but modest in scale. The new feature the product team wanted to build had been requested by one customer, a customer who, it turned out, was already planning to leave.

The Pareto didn't make the decision for us. But it ended the debate. When you can show that one problem is generating four times the customer pain of the next thing on the list, the conversation changes. You're no longer negotiating between preferences. You're looking at evidence.

The process itself is not complicated, and that's part of why it doesn't get done. There's a bias in organizations toward sophisticated-looking work. A three-day offsite with a strategy consultant feels like serious prioritization. A spreadsheet with two columns feels too simple to be meaningful. But the spreadsheet is usually more honest than the offsite, because the offsite is still susceptible to whoever speaks most confidently in the room.

What you actually need is a categorized list of your problems, a count of how often each category occurs, and an estimate of what each occurrence costs in some meaningful unit. Dollars, hours, customer satisfaction, revenue at risk, whatever is most relevant to your situation. Multiply frequency by per-occurrence impact to get total impact. Sort by that column. Look at where the curve breaks.

The categorization step is where most of the real work lives. It requires judgment. Five support tickets about the same root cause are one problem, not five. Calling them five separate problems is a way of hiding a pattern in noise. The person doing the categorization needs enough context to see the underlying causes, not just the surface symptoms.

One thing I've learned the hard way: run the frequency sort and the impact sort separately before combining them. They tell different stories. The frequency sort shows you where customers are experiencing friction most often. The impact sort shows you where the damage is most severe. Where both agree, your decision is easy. Where they diverge, you need to make a judgment call about what you're optimizing for and who your most important customers are. That judgment call is worth a real conversation, because different answers produce genuinely different roadmaps.

The failure mode I've watched play out more than once is what I'd call Pareto as excuse. A team does one analysis, identifies the top three problems, fixes them, and then uses "we're focused on the twenty percent that matters" as a permanent pass on everything else. The long tail doesn't disappear because you stopped looking at it. Small problems compound. A friction point that affects three percent of your users this quarter might become the thing that breaks your retention numbers two years from now, especially if that three percent turns out to be your highest-value segment.

The analysis is a starting point, not a destination. The top of the list is where your energy goes. The rest of the list still needs someone paying attention to it, even if that attention is lighter.

The habit that actually produces results is running the analysis regularly, not once. The first time you do it, you find the obvious things, the problems that have been sitting in plain sight because nobody organized the data. The third and fourth time, you start seeing patterns that aren't visible in a single snapshot. You see which categories keep reappearing in the top tier despite being "fixed" before, which tells you the fix addressed the symptom but not the cause. You see categories that are slowly climbing the rankings, giving you early warning before they become emergencies.

That cadence, monthly or quarterly depending on how fast your environment moves, is what turns a one-time exercise into genuine organizational intelligence.

The principle is old and widely quoted. The practice is rare. The gap between those two things is where most teams leave real leverage on the table, and it doesn't take much to close it.
