---
name: unslop
description: Cuts long, AI-generated PRDs and product docs down to the decisions, numbers and open questions. Use when asked to unslop, tighten, shorten or de-AI a PRD, spec, brief or product doc.
---

# Unslop

Turn a bloated product doc into the shortest version that keeps every decision, number and constraint. Make missing decisions visible instead of papering over them.

AI-generated PRDs have two problems. The obvious one is style: long sentences, filler words, rhetorical tricks. The deeper one is substance: the prose hides decisions nobody made. Fixing only the style gives you a shorter doc that is still empty. This skill fixes both.

## Core rules

1. **Never invent.** No new metrics, targets, dates, owners, segments or scope. If the source doesn't say it, it becomes an open question.
2. **Decisions over prose.** Every sentence that survives is a decision, a verifiable claim, or context the reader needs to make a decision.
3. **Length follows decisions, not the original.** A doc with three decisions does not need four pages. Never pad a section to make it look complete.
4. **Keep the source language.** Write the output in the language of the input. Keep product and technical terms as the team uses them.
5. **Your own output must pass the slop check.** Run the pattern list below on the rewrite before returning it.

## Process

### 1. Extract before writing
Read the whole doc and list, for yourself:
- decisions (what we will and won't do)
- numbers (baselines, targets, sizes, dates)
- constraints and dependencies
- user segments
- explicit non-goals

Everything not on this list is a candidate for deletion.

### 2. Sentence test
For each sentence in the source ask: is it a decision, a verifiable claim, or context the reader needs? If none, cut it. If it is a vague claim ("improve engagement", "better experience"), turn it into an open question: which metric, from what, to what?

### 3. Gap check
Compare what you extracted against the template sections. Each missing piece becomes an open question. Typical gaps:
- no success metric, or a metric with no baseline or target
- no non-goals
- "users" with no segment
- solution described, problem never evidenced
- no owner or timeline when the doc implies one

### 4. Rewrite into the template
Use the template below. Reorder freely; do not keep the source's structure if the structure itself was padding.

### 5. Slop pass
Apply the pattern list to your rewrite. Then reread only the TL;DR: someone who reads nothing else must know what is being built, for whom, and what is still undecided.

### 6. Report
Append the short report described below.

## Output template

```
# [Feature / project name]

**TL;DR:** max 3 sentences. What, for whom, why now.

## Problem
What is broken and the evidence from the source. No evidence → open question.

## Who it's for
The specific segment.

## Non-goals
What we are explicitly not doing.

## Solution
What we are building. Scope, not aspirations.

## Success metrics
| Metric | Baseline | Target |
Missing values → open question, never a guess.

## Risks & dependencies

## Open questions
1. The question. Why it matters / what it blocks.
```

If a section has nothing in the source, write one line pointing to the open question (e.g. "Not specified, see Q2"). Do not delete the section silently; an empty section is information.

Rough length target: under ~1 page (~500 words) for a typical PRD, usually 20–35% of the original. Docs with many real decisions can be longer. Docs with few decisions should be shorter.

## Patterns to remove

### Filler vocabulary
leverage, seamless, robust, empower, unlock, holistic, delve, streamline, cutting-edge, game-changer, best-in-class, world-class, synergy, ecosystem (when not literal), "in today's fast-paced world", "it's important to note", "it is crucial that", "at the end of the day".

Replace with the concrete thing, or delete.

### Sentence level
- **One idea per sentence.** Split or cut anything over ~25 words.
- **No restating.** Drop section intros that announce what's coming and section endings that summarize what was just said.
- **No hedging.** "Potentially", "may be worth considering", "in some cases", "could possibly". Either claim it or move it to open questions.
- **Actor + verb + object.** "Improvements to the user experience are targeted" → "We're cutting checkout from 5 steps to 3."
- **Question every triplet.** AI lists things in threes ("fast, reliable, and scalable"). Keep only items the source actually supports.
- **No synonym stacking.** "Clear, concise, and actionable" → usually one word, often none.

### Rhetorical tics
These create the feeling of content without content. Rule: **if a sentence gets its effect from rhythm and contains no number, name or decision, make it concrete or delete it.**

- **False contrast:** "This isn't just a feature, it's a new way of working." Nobody claimed X; state Y directly. Keep the contrast only if someone actually argued X.
- **Staccato fragments:** "No meetings. No friction. Just results." Turn into one concrete sentence or delete.
- **Fake suspense:** "The result? 40% faster." / "Here's the thing:" State the answer.
- **Colon reveal:** "The answer: simplicity."
- **Aphorism closers:** "Because in the end, great products are built by great teams." Delete.
- **Reader instructions:** "Let that sink in." / "Read that again."
- **"Whether you're X or Y…"** openers.
- **Em-dash habit:** a dash aside in every other sentence. Use commas, parentheses or a new sentence.

### Formatting
- One-sentence paragraphs stacked LinkedIn-style (outside of lists).
- Bold sprinkled on random phrases. Bold only what a skimmer must not miss, if anything.
- Bullets that are each a full paragraph; nesting deeper than two levels.
- Emoji in headers.

## Example

Before:
> In today's rapidly evolving landscape, it is crucial that we leverage our existing capabilities to deliver a seamless and intuitive onboarding experience that empowers users to realize value quickly. This isn't just about reducing friction, it's about building lasting relationships.

After (source mentioned 60% day-one drop-off and a 7-screen flow):
> 60% of new users leave on day one. We're cutting onboarding from 7 screens to 3.

After (source mentioned neither):
> We want to simplify onboarding.
> Open questions: What is the current day-one drop-off? What's the target? Which screens go?

The second "after" is the important case. Do not invent the 60%.

## Report

After the rewritten doc, add a short block:

```
---
Unslop report
- Words: 2,840 → 610 (−79%)
- Decisions kept: 6
- Open questions raised: 5
- Invented content: none
```

If you had to make any interpretation call (e.g. merging two contradictory scope statements), list it in one line each under the report. Nothing else: no summary of the doc, no list of every cut.

## Non-PRD inputs
For updates, memos, strategy docs or long messages, apply the same rules (extract, sentence test, gap check, slop pass, report) but skip the PRD template. Keep the doc's purpose and put the conclusion or ask in the first two sentences.

## Don'ts
- Don't add content, examples or metrics the source doesn't contain.
- Don't soften open questions to be polite. A missing success metric is a real problem; say so plainly.
- Don't preserve the source's section structure out of respect for it.
- Don't end with a summary of what you did beyond the report.
