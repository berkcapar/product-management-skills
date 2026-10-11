---
name: user-interview-synthesis
description: Synthesize customer interview notes or transcripts into evidence-backed themes, verbatim quotes, jobs-to-be-done, and opportunities in customer voice, ready to feed an Opportunity Solution Tree. Works on a single interview (snapshot) or many (cross-interview synthesis), separates what customers did from what they said they want, and counts evidence honestly. Use when the user shares interview notes, call transcripts, customer call recordings' text, discovery notes, sales call notes, user research, usability test notes, "what did customers say", "synthesize these interviews", "find patterns", "affinity map", or "interview snapshot".
---

# User Interview Synthesis

Synthesis turns raw conversations into a small number of well-evidenced insights a team can act on. The failure modes are well known: cherry-picked quotes that confirm what the PM already believed, feature requests mistaken for needs, themes backed by one loud customer, and summaries so generic they could describe any product. This skill is built to avoid them.

## Principles

1. **Behavior over opinion.** What a customer did last week outweighs what they say they would do. Stories about specific past events are the strongest evidence.
2. **Needs over requests.** A feature request is a clue to a need. Record the request, then dig for the underlying need.
3. **Count honestly.** Every theme shows how many interviews support it (n/N). One vivid quote is an anecdote, not a pattern.
4. **Verbatim means verbatim.** Quotes are copied exactly from the input. Never paraphrase inside quote marks, never stitch fragments together, never invent.
5. **Separate observation from interpretation.** Label which is which.
6. **Look for disconfirming evidence.** Actively report what contradicts the leading theme and what surprised you.

## Step 0: Inputs

Check for:
1. The notes or transcripts (one or many)
2. The **research question** or decision this research supports
3. Participant context (role, company size, segment, customer vs prospect, plan tier)
4. The current outcome or OST, if one exists

If the research question is missing, ask for it once. If the user says "just synthesize", infer one from the notes, state it at the top as `[assumed research question]`, and proceed.

Notes quality check: if notes are mostly the interviewer's summaries rather than the customer's words, say so. Themes from summary-only notes get lower confidence.

## Mode A: Interview snapshot (one interview)

Produce a one-page snapshot (Torres-style):

```
INTERVIEW SNAPSHOT: [participant id / role, company type, segment] | [date]

Memorable quote: "[verbatim]"

Quick facts
- Role, context, tools they use today, how often they do the job

The story (what actually happened, in sequence)
1. [trigger]
2. [what they did]
3. [where it broke / what was hard]
4. [workaround]
5. [outcome]

Opportunities (customer voice)
- "[need / pain / desire]" [evidence: quote or behavior]
- ...

Insights and surprises
- [anything that challenges current assumptions]

Feature requests mentioned (with underlying need if discovered)
- Request: ... → Need: ... / Need unknown

Follow-ups
- [questions to ask next time, people to talk to, data to check]
```

Keep it to one screen. Every opportunity must point at a quote or a described behavior.

## Mode B: Cross-interview synthesis (many interviews)

### 1. Extract atomic observations

Go interview by interview. Pull one observation per line, each tagged:

`[P#] [type] observation (quote if available)`

Types:
- **[did]** past behavior or story
- **[pain]** friction, frustration, cost, risk
- **[workaround]** hacks, spreadsheets, manual steps, other tools (strong signal of an unmet need)
- **[goal]** what they're ultimately trying to achieve
- **[request]** explicit feature ask
- **[context]** constraints, environment, who else is involved
- **[said]** opinion, prediction, hypothetical ("I would use...")

Do this extraction internally or show it in a collapsible appendix if the user wants it. Don't skip it: it's what keeps themes honest.

### 2. Cluster into themes

Group observations into themes by underlying need, not by feature area or by interview question. Then for each theme:

- **Name it as an insight**, a full sentence that says something non-obvious. "Onboarding" is a topic. "Admins can't start until IT approves the integration, so the first week is wasted waiting" is an insight.
- **Evidence count:** n/N participants. Note segments if the pattern is concentrated ("4/5 enterprise, 0/4 SMB").
- **Strength:** behavior-backed (did / workaround) vs opinion-backed (said / request). A theme backed only by [said] and [request] is weak, say so.
- **Best 1 to 3 quotes**, verbatim, attributed to participant id.
- **Counter-evidence:** participants who said or did the opposite.

### 3. Translate to opportunities

For each theme, write opportunities in customer voice (something a customer could say about their own experience, not a solution). Apply the solution-in-disguise test: if it names something we'd build, ask "why would they want that?" and rewrite.

### 4. Jobs to be done (when useful)

If the research is exploratory, add a JTBD line per key segment:

> When [situation], I want to [motivation], so I can [expected outcome].

Only write jobs supported by stories in the data.

## Output (Mode B)

```
SYNTHESIS: [research question] | N = [#] interviews | [segments] | [date range]

TL;DR (3 bullets max: the most important insights for the decision at hand)

Themes (ordered by strength of evidence, not by how interesting they are)

1. [Insight sentence]
   Evidence: n/N [segments] | Strength: behavior / mixed / opinion-only
   "[verbatim quote]" (P3)
   "[verbatim quote]" (P7)
   Counter-evidence: [P5 did/said ...] or none found
   Opportunities: "[customer voice]", "[customer voice]"

2. ...

Feature requests (table)
| Request | # | Underlying need (if known) | Maps to theme |

Surprises / things that challenge our assumptions

What we still don't know (and suggested next interviews or data pulls)

Opportunities for the OST (flat list, customer voice, with evidence tag [interviews n/N])
```

The final opportunity list is formatted to drop straight into the `opportunity-solution-tree` skill.

## Bias checks (always run before final output)

- **Confirmation:** Did the themes mostly confirm what the user expected (from their framing of the request)? If so, look again for disconfirming evidence and report it.
- **Loudest voice:** Is any theme driven mostly by one participant? Mark it as an anecdote.
- **Recency / vividness:** Is a theme ranked high because of a great quote rather than evidence count?
- **Sample skew:** Are segments, roles or customer types missing that matter for the decision? Name them.
- **Leading questions:** If transcripts include interviewer questions, flag answers that were prompted ("Would it be helpful if...?" → "Yes") and down-weight them.
- **Small N honesty:** With fewer than 5 interviews, frame themes as hypotheses to validate, not findings.

Report the most important bias issue in a short **Caveats** line at the end.

## Rules

- Never fabricate quotes, participants, counts or details. If a quote isn't in the input, it doesn't exist.
- Anonymize by default (P1, P2...) unless the user wants names. Remove personal data that isn't needed (emails, phone numbers).
- Keep the customer's language in opportunities; it's often better than ours.
- Don't recommend solutions unless asked. Synthesis feeds discovery; jumping to solutions here biases the next step.

## Quick-pass mode

If the user says "quick", "top takeaways", or "TL;DR": return the 3 strongest themes with evidence counts and one quote each, plus the single biggest caveat.
