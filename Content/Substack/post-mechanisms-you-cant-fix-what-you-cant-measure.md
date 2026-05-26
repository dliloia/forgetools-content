# Mechanisms: You Can't Fix What You Can't Measure

*Most teams run on vibes. The leader has a feeling about how things are going, and the feeling becomes the report. Mechanisms replace vibes with signal, and without them you can't tell whether your last change made anything better or worse.*

## The Problem With Running on Feel

Most teams I've worked with don't actually know how they're doing. They think they do. The leader has a general sense of things. The team is heads-down. Work is getting done. Nobody's complaining. That feeling becomes the status report, the quarterly review, the answer when the CEO asks how the project is tracking.

Then something fails, and everyone is surprised.

This is what operating without mechanisms looks like. Not chaos, not incompetence, just a slow accumulation of blind spots that nobody notices until the compounded cost shows up all at once.

Jeff Bezos had a word for what fixes this, and at Amazon it was used precisely: mechanism. The distinction between a metric, a process, and a mechanism matters and I'll get to it, but the core idea is simple. A mechanism is a practice that produces measurable signal on a repeatable schedule. It tells you whether the thing you care about is improving, degrading, or just staying flat. And because it runs on a schedule, you don't need to remember to check. It checks for you.

You cannot improve what you cannot see. That sounds obvious. It is obvious. And most teams are still not doing it.

## What a Mechanism Actually Is

A metric is a number. Revenue, headcount, ticket volume, response time. Numbers are fine but they're passive. They sit there until someone looks at them, and then they mean whatever that person needs them to mean.

A mechanism is the practice that produces the number and creates a forcing function around it. It closes the loop. It turns the number from a data point into a decision.

Here's a simple example. Tracking customer complaints is a metric. A weekly meeting where you review the top five complaint categories, assign an owner to each, and check last week's owners on whether their issue closed is a mechanism. The first one tells you something is happening. The second one makes sure something gets done about it.

The Amazon six-pager is a mechanism. It forces the writer to think through a problem in full sentences, with logic that holds under scrutiny, before the meeting even starts. The output is the document. The signal is whether the logic holds. If it doesn't, the problem wasn't thought through well enough, and you know that before you've burned an hour of eight people's time in a conference room.

That's what a good mechanism does. It surfaces the problem early, before the cost is high.

## The ManagerForge Example

I'll make this concrete with something I actually run.

The content system I built for ManagerForge generates an article every day. A cron kicks it off, the pipeline runs, and a draft appears. For a while, articles were shipping and things felt fine. Volume was up. Output was visible. The system appeared to be working.

The problem was I had no idea what was actually being published. I couldn't tell if the voice was consistent, if the structure was right, if the draft had drifted from the standards I'd set. I just knew articles were appearing.

So I built a voice audit. It checks every draft against a set of explicit rules before anything ships. Em dashes, forbidden cadence patterns, credential density, stabby fragment beats. The audit either passes the draft or returns a violation report. Then a Telegram bot pings me with which articles shipped, which ones failed, and which specific rules they failed on.

Now I can see the error rate by rule. I can see which rules fail most often, which means I know where the highest-leverage fix is. Without those three pieces, I would have been publishing content I thought was good because it was appearing, and I would have had no idea what was actually going out the door.

That is the difference between a metric (articles published today: 1) and a mechanism (voice audit plus bot plus error-rate tracking that closes the loop on quality before publication).

The metric tells you volume. The mechanism tells you whether the volume is worth anything.

## Why Good Judgment Doesn't Scale

There's a version of every team where the leader is smart enough and close enough to everything that their judgment functions as a substitute for measurement. The team is small. The leader knows everyone. Problems surface through hallway conversations and gut feel.

That works until it doesn't, and the ceiling is usually around ten people. Once you're past that, the leader can't be present for everything. Information starts filtering before it reaches them. The people who know about the problems are not always the people who talk to the leader. And the leader's gut feel is now operating on incomplete, secondhand signal.

This is where mechanisms pay for themselves. Not because the leader becomes less smart, but because the team becomes too large and too complex for any one person's judgment to cover the whole surface area. Mechanisms are how you extend your perception past the limits of your own attention.

I managed large distributed teams for years, and the pattern was always the same. The leaders who relied on feel were always the ones who got blindsided. Not once, but repeatedly. Same story, different quarter. The leaders who built mechanisms, even crude ones, were the ones who caught problems early and had something concrete to point to when they needed to make a case for resources or a change in direction.

## The Cheap Mechanisms Your Team Isn't Running

None of this requires a sophisticated tech stack. Most of the highest-value mechanisms I've seen are almost embarrassingly simple.

Weekly written status. Not a meeting, not a verbal update. Every person on the team writes three sentences: what they shipped, what's blocked, and what they're focused on next week. This takes five minutes to write and two minutes to read, and it creates a searchable record that a verbal standup never does. Patterns in blockers show up fast when they're written down.

A post-mortem template. When something goes wrong, the template gets filled out. What happened, what we missed, what changes. That's it. The discipline of filling it out is the mechanism. Most teams skip this and then make the same mistake again eighteen months later because there's no record that the first one happened.

An error-rate dashboard for whatever your team's core output is. If you're a support team, what percentage of tickets are reopening. If you're an engineering team, what's the defect rate on shipped code. If you're running a content system, what percentage of drafts are failing quality review. One number, tracked weekly, visible to the team. The number will focus every conversation about improvement onto something real.

None of these are complicated. Most teams don't run them because installing a mechanism requires admitting that you haven't been measuring the thing, and that admission is uncomfortable. The discomfort of introducing a mechanism is usually proportional to how badly the team needs one.

## The Bottom Line

If you can't measure it, you can't improve it. That's not a philosophy, it's just true. Every change you make without a feedback loop is a guess, and guessing isn't a strategy.

Pick one thing your team does every week that you're currently evaluating by feel. Design the simplest possible mechanism to produce real signal on it. Run it for four weeks. Then tell me the feel wasn't lying to you.

It almost always was.

---

Originally published at [ManagerForge](https://www.managerforge.com/insights/mechanisms-you-cant-fix-what-you-cant-measure).
