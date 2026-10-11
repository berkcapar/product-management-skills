---
name: stakeholder-update
description: Turn messy notes, ticket lists, Slack threads, metrics and meeting notes into a sharp stakeholder update tailored to the audience (CEO/founders, board/investors, exec team, engineering/design team, sales/CS, or customers). Leads with what changed and what is needed, flags risks honestly, and keeps it skimmable. Use when the user asks for a weekly update, status update, progress report, monthly update, board update, investor update, product update, release notes for internal teams, "what should I tell the CEO", "write the Friday update", or pastes raw progress notes that need to be communicated upward or across.
---

# Stakeholder Update

A stakeholder update exists to change what the reader knows, believes or does. Most updates fail because they report activity ("we worked on X") instead of change ("X moved from A to B"), bury the ask, and hide bad news in the middle. This skill turns raw input into an update the reader can absorb in under a minute and act on.

## Principles

1. **Bottom line up front.** The first three lines carry the whole message. Someone who reads only those must know the status, the most important change, and whether they need to do something.
2. **Outcomes over activity.** Report what changed in the world (metric, customer, decision, risk), not what the team was busy with.
3. **Bad news early, with a plan.** A risk surfaced early with options builds trust. A surprise at the deadline destroys it.
4. **One clear ask, with an owner and a date.** If nothing is needed, say "No action needed."
5. **Audience decides altitude.** Same facts, different update for the CEO, the board, the team and sales.
6. **Never invent.** No made-up numbers, dates, names or progress. Missing facts become `[TBD: ...]` placeholders.

## Step 0: Inputs

Check what the user provided. You need:

1. **Audience** (who reads this)
2. **Period** (this week, sprint, month, quarter)
3. **Raw material** (notes, tickets, metrics, threads)
4. **Goals or commitments** the update reports against (OKRs, roadmap, last update's "next" list)

If the audience is missing, ask, because it changes everything. For the rest, proceed with what's there and mark gaps as `[TBD]`. If a previous update is available, compare against what it promised.

## Audience playbook

| Audience | They care about | Length | Altitude | Tone |
|---|---|---|---|---|
| **CEO / founders** | Are we on track, what needs my decision, what could hurt us | 5 to 10 lines | Outcomes, risks, decisions | Direct, no padding |
| **Board / investors** | Progress on the plan, key metrics vs targets, strategic risks, help needed | 1 page | Quarter-level, numbers vs plan | Confident, candid |
| **Exec team / peers** | Dependencies, impact on their teams, trade-offs | Half page | Cross-functional | Collaborative |
| **Eng / design team** | Why it matters, what's next, what got decided, who did great work | Flexible | Context and decisions | Warm, specific credit |
| **Sales / CS** | What can I sell or promise, when, what changed for customers | Short bullets | Customer-facing capabilities and dates | Concrete, no internal jargon |
| **Customers** | What's new for me, what's coming, what's fixed | Short | Benefits, not features | Plain, friendly |

For Series A and other early-stage companies, CEO and board updates should always connect product work to the metrics that matter for the next milestone (revenue, retention, activation, burn-relevant efficiency).

## Status signal

Use one overall status, and per workstream if there are several:

- 🟢 **On track:** will hit the commitment with current plan.
- 🟡 **At risk:** might miss without a change. Say what change.
- 🔴 **Off track:** will miss. Say the new expectation and the recovery plan.

Rules: Status reflects the commitment, not effort or vibes. Green to red with no yellow in between is a flag: point it out to the user. Do not mark yellow to look humble or green to look good.

## Default structure (CEO / exec weekly)

```
[Period] update: [one-line headline that states the most important change]

Status: 🟢/🟡/🔴  [one sentence why]

TL;DR
- [Most important outcome or change, with a number if possible]
- [Biggest risk or decision needed]
- [Ask, owner, date] or "No action needed"

Progress vs commitments
- [Commitment]: [what changed] [status]
- ...

Metrics (only the ones that matter)
- [Metric]: [current] (vs [last period] / vs [target])

Risks and issues
- [Risk]: [impact] → [mitigation / options] [owner]

Decisions
- Made: [decision] because [reason]
- Needed: [decision] by [date] from [person]. Options: A / B. Recommendation: A because...

Next period
- [3 to 5 commitments, phrased as outcomes]
```

Cut any section that is empty. Never pad.

## Board / investor variant

```
[Month/Quarter] Product update

Headline: [one sentence]

Key metrics vs plan (table: metric | target | actual | trend | comment)

What went well (2 to 3 bullets, outcome-based)
What didn't (1 to 3 bullets, candid, with what we learned)
Strategic risks (1 to 2, with mitigation)
Next quarter priorities (3 max, tied to company goals)
Where we need help (intros, hires, advice; be specific)
```

## Team variant

Start with **why** this period mattered, then progress, decisions (and the reasoning), what's next, and **specific credit** ("Ayşe's migration script cut onboarding time from 3 days to 4 hours"), never generic thanks.

## Sales / CS variant

Lead with "What you can tell customers now" and "What's coming and when (confidence level)". Include a short "What not to promise" line if anything is uncertain. No internal ticket numbers or codenames.

## Writing rules

- **Activity → outcome rewrite.** Convert every "worked on / continued / made progress on" line. Ask what changed. If nothing changed, either drop it or say plainly that it is in progress and what "done" will look like.
  - Before: "Continued work on onboarding flow."
  - After: "New onboarding flow in beta with 12 accounts; first-week activation 58% vs 41% baseline (small sample)."
- **Numbers with context.** Every metric gets a comparison (last period, target or baseline). A number alone is noise.
- **Name owners.** "We need to decide" becomes "Need a decision from [name] by [date]."
- **Kill jargon** the audience doesn't share: internal codenames, ticket IDs, team acronyms.
- **Short sentences, active voice.** Bullets of one line where possible.
- **Hedge honestly.** "Small sample", "early signal", "estimate" are fine and build trust. Over-claiming is not.

## Bad news protocol

When something is late, failed, or at risk:
1. State it plainly in the TL;DR, not buried.
2. Impact: what does it mean for customers, revenue, dates.
3. Cause: one sentence, no blame.
4. Plan: options with trade-offs, recommendation, new date with confidence.
5. Ask: what you need from the reader, if anything.

## Challenge pass (before final output)

Read the draft as the recipient. Check:
- Could they stop after three lines and know what matters?
- Is anything important hidden below the fold (a risk in section 5, an ask in the last line)?
- Does any line describe effort instead of change?
- Do any numbers lack a comparison?
- Is the status color honest given the risks listed?
- Is there any number, date or name you did not get from the user's input? Remove it or mark `[TBD]`.

After the update, add a short **Notes for you** section (not part of the update) listing: placeholders to fill, any status concerns, and anything that looks like a surprise the reader shouldn't get in writing first (suggest a heads-up conversation instead).

## Modes

- **Draft** (default): raw input → finished update.
- **Tighten:** user's own draft → shorter, sharper version plus a list of what you cut and why.
- **Multi-audience:** one input → versions for several audiences. Keep facts identical across versions; only altitude and framing change.
- **Recurring:** if the user shares last period's update, carry over the "next period" list and report against it explicitly ("Last week we said X. Result: ...").
