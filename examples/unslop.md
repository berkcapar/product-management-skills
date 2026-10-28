# Example: unslop on an iPad calculator PRD

The input is an AI-written PRD for a native iPad calculator. It is cleaner than most: real requirements, real targets. The skill still cut a third of it, and the bigger win was in the open questions.

**What to look at**

- **Overview, User journeys, Goals:** cut. They restated the requirements table in prose.
- **Problem:** rewritten to what the source actually supports, with "no evidence" turned into Q1.
- **Q4:** the source lists percent and operator precedence as P0, then calls them "consistent" and "documented" without defining either. That is a missing decision dressed up as a requirement. The skill names it: is 50 + 10% equal to 55 or 50.1?
- **Success metrics:** every target was kept, and the skill points out that none of them measures adoption (Q2).
- **Nothing invented:** no new metric, date, owner or scope.

## After

### Native Calculator for iPad

**TL;DR:** A free, native Calculator for iPadOS with Basic and Scientific modes, keyboard support, local history and full offline use. It's for anyone who needs a quick calculation without leaving the app they're in. Calculation semantics (precision, percent, operator precedence) and supported devices are still undecided, and several launch gates depend on them.

Status: Draft · Owner: iPad Product Team (no named owner) · Launch date: not set

#### Problem
iPad users who need to calculate something today use a third-party app, a browser, or another device. The doc gives no evidence for how often this happens or how many users it affects (Q1).

#### Who it's for
Everyday users (splitting a bill, a discount), students (scientific formulas while studying), professionals (checking a number beside a document).

#### Non-goals (initial release)
- Handwriting recognition, graphing
- Symbolic algebra, step-by-step tutoring
- Spreadsheet features
- Currency conversion with live rates
- Shared sessions, cloud-synced history

#### Solution

**P0**
- Arithmetic: + − × ÷, decimals, sign change, percent, parentheses. Precedence and percent rules are undefined (Q4).
- Correction: delete last digit, clear entry, clear all. Invalid operations show an error and keep the expression.
- Expression and result shown separately. Long expressions stay inspectable.
- Scientific mode: powers, roots, logs, trig, constants, degrees/radians with the active mode clearly shown. App opens in Basic.
- Layout: portrait, landscape, every multitasking size down to a minimum width (Q5). The active expression survives rotation, resizing, mode switches, backgrounding and normal termination.
- Keyboard: digits, operators, Enter, Backspace, copy/paste shortcuts, full keyboard navigation.
- Copy results. Paste numeric expressions, with an error for unsupported input (Q6).
- History: last 100 calculations, stored locally, kept across restarts. Reload, copy, delete one, clear all.
- Works offline, no account.
- No onboarding. Touch targets at least 44×44 pt.
- VoiceOver, increased contrast, larger text, locale-aware separators and text direction, light and dark.
- No floating-point artifacts in display: 0.1 + 0.2 shows 0.3.
- Analytics never include numbers, expressions, results or clipboard contents. Clearing history deletes the stored entries.

**P1** (gated separately, must not delay P0)
- Unit conversion: length, mass, temperature, area, volume, time (Q7)
- Launch from system shortcuts and surfaces (Q8)

#### Success metrics
New app, so no baselines. All targets are proposed and get validated in beta.

| Metric | Target | Measured by |
|---|---|---|
| Unassisted basic task completion | ≥ 95% | Moderated usability test |
| Rate basic calculation easy / very easy | ≥ 90% | Post-task survey |
| Reference suite pass rate | 100% | Automated |
| Crash-free sessions | ≥ 99.9% | Diagnostics |
| Input feedback | < 100 ms p95 | Device testing |
| Usable UI after launch | < 1 s p95 on oldest supported device | Device testing |

No adoption or usage target (Q2).

#### Launch gates
- All P0 requirements accepted
- Reference suite passes 100%
- Performance and reliability targets met
- Accessibility review with no blocking issues
- No open critical or high-severity defects
- History deletion and analytics privacy verified

#### Risks & dependencies
- Narrow windows hiding controls: depends on Q5.
- Percent and rounding behavior surprising users: depends on Q3, Q4.
- History holding sensitive numbers: kept local, with prominent delete controls.
- The reference suite and performance testing can't start until Q3 and Q9 are answered.

#### Open questions
1. What evidence shows this is a real gap (third-party calculator usage, support requests, survey data)? This decides priority and "why now".
2. Is there an adoption or usage target? Every current metric measures quality, so nothing tells us whether the launch mattered.
3. What precision, numeric range, rounding and overflow behavior do we guarantee? Blocks the reference suite and a launch gate.
4. How does percent work (is 50 + 10% equal to 55 or 50.1)? Standard order of operations or immediate execution? Both are P0 and both are undefined; the source only says "consistent" and "documented".
5. What is the minimum supported window width?
6. Which pasted formats count as "supported"?
7. Is unit conversion in the launch build?
8. Which system shortcuts and surfaces does P1 launch access cover?
9. Which iPadOS versions and devices are supported? This defines "oldest supported device" in the launch-time target.
10. What do repeated presses of equals do?
11. Who is the named owner, and what is the target launch date?
12. Who writes and approves the reference calculation suite?

---
Unslop report
- Words: 1,033 → 658 (−36%), counted with `scripts/wordcount.py`
- Decisions kept: every requirement, target, non-goal and launch gate in the source
- Open questions raised: 12 (5 from the source, 7 new)
- Invented content: none
- Dropped "User journeys": every journey restated a P0 requirement.
- Moved "default to Basic mode" from Risks into Solution, since it's a decision.
- Dropped delivery phases, kept launch gates. Dropped the "later releases" question as roadmap, not a launch blocker.

## Before

<details>
<summary>The original AI-written PRD (click to expand)</summary>

### PRD: Native Calculator for iPad

**Status:** Draft  
**Platform:** iPadOS  
**Release:** Proposed initial launch  
**Owner:** iPad Product Team

#### 1. Overview

Build a free, native Calculator app that helps iPad users perform quick arithmetic and scientific calculations without interrupting their work.

The app should feel natural on iPad: easy to use with touch or a keyboard, responsive to different window sizes, and useful alongside apps such as Notes, Safari, and Numbers.

#### 2. Problem

Users need calculations while studying, budgeting, shopping, and working. Without a built-in calculator, they must find a third-party app, use a browser, or reach for another device.

These workarounds add friction to a simple, frequent task. A native calculator should make reliable answers immediately accessible.

**Core user need:** “When I need to calculate something on my iPad, I want a fast, trustworthy answer so I can continue what I’m doing.”

#### 3. Goals and Non-goals

**Goals**

- Make everyday calculations fast and discoverable.
- Provide scientific functions for students and technical users.
- Support calculation alongside other iPad workflows.
- Deliver an accessible experience that works offline.
- Let users review, correct, and reuse calculations.

**Non-goals for the initial release**

- Handwritten equation recognition and graphing.
- Symbolic algebra or step-by-step tutoring.
- Spreadsheet functionality.
- Currency conversion requiring live exchange rates.
- Shared calculation sessions or cloud-synced history.

#### 4. Target Users

| User | Primary need | Example |
|---|---|---|
| Everyday user | Quick arithmetic | Split a bill or calculate a discount |
| Student | Scientific calculations | Evaluate a formula while reading course material |
| Professional | Calculations within a workflow | Check a cost estimate beside a document |

#### 5. Key User Journeys

**Quick calculation:** The user opens Calculator, enters `84 ÷ 4`, and sees `21`. They can copy the result or start another calculation immediately.

**Calculation alongside work:** The user opens Calculator beside a document, calculates a total, and copies the answer into the document. Resizing the calculator preserves the active expression.

**Scientific calculation:** The user switches to Scientific mode, selects degrees or radians, enters an expression, and receives a result with the angle mode clearly visible.

**Correct and reuse:** The user notices an input mistake, deletes the last digit, and completes the calculation. Later, they reopen the expression from history to modify it.

#### 6. Functional Requirements

| Priority | Requirement | Acceptance criteria |
|---|---|---|
| P0 | Basic arithmetic | Supports addition, subtraction, multiplication, division, decimals, sign changes, percentages, and parentheses. |
| P0 | Clear calculation rules | Uses documented operator precedence. Percentage behavior is consistent and covered by examples in QA. |
| P0 | Input correction | Users can delete the last digit, clear the current entry, and clear the full expression. |
| P0 | Visible expression and result | Users can distinguish the entered expression from the answer. Long expressions remain inspectable. |
| P0 | Scientific mode | Supports powers, roots, logarithms, trigonometric functions, constants, and degrees/radians. |
| P0 | Adaptive layout | Works in portrait, landscape, and supported multitasking window sizes without hiding essential controls. |
| P0 | Keyboard support | Supports numeric entry, arithmetic operators, Enter to evaluate, Backspace to delete, and standard copy/paste shortcuts. |
| P0 | Copy and paste | Users can copy a result and paste supported numeric expressions. Unsupported input produces a clear message. |
| P0 | Local history | Stores the latest 100 completed calculations across app restarts. Users can reload, copy, delete individual entries, or clear all history. |
| P0 | Offline operation | All initial-release calculations work without connectivity or an account. |
| P0 | Error handling | Invalid operations show understandable errors and preserve the expression for correction. |
| P1 | Unit conversion | Supports common length, mass, temperature, area, volume, and time conversions. |
| P1 | Additional launch access | Provides convenient access through supported system shortcuts and surfaces. |

#### 7. Experience Requirements

- Open directly into a usable calculator without onboarding.
- Use large, clearly labeled touch targets of at least 44 × 44 points.
- Keep Basic and Scientific modes easy to find.
- Preserve the active expression when switching modes, rotating, resizing, or briefly leaving the app.
- Make the active angle mode and selected operators visually clear.
- Support VoiceOver, increased contrast, larger text where applicable, and full keyboard navigation.
- Respect locale conventions for decimal separators, digit grouping, and text direction.
- Include light and dark appearances.

#### 8. Accuracy, Performance, and Privacy

**Accuracy:** Define supported precision, rounding, numeric range, and overflow behavior before implementation. Avoid displaying floating-point artifacts in ordinary calculations; for example, `0.1 + 0.2` should display `0.3`.

**Performance:** Proposed launch targets are a usable interface within one second at the 95th percentile on the oldest supported device, and visible input feedback within 100 milliseconds.

**Reliability:** Recover the current expression and saved history after normal app termination.

**Privacy:** Store expressions and history locally. Product analytics must exclude entered numbers, expressions, results, and clipboard contents. Clearing history must remove the corresponding stored entries.

#### 9. Success Metrics

These are proposed targets to validate during beta.

| Metric | Target | Measurement |
|---|---|---|
| Basic task completion | At least 95% without assistance | Moderated usability testing |
| Ease of use | At least 90% rate basic calculation easy or very easy | Post-task survey |
| Calculation correctness | 100% pass rate for the approved reference suite | Automated verification |
| Crash-free sessions | At least 99.9% | Privacy-preserving diagnostics |
| Input responsiveness | Under 100 ms at the 95th percentile | Device performance testing |

Usage frequency is a secondary signal; success primarily means users get accurate answers quickly.

#### 10. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Scientific controls overwhelm casual users | Default to Basic mode and provide an explicit mode switch. |
| Narrow windows become difficult to use | Define a minimum supported width and validate all essential controls at that size. |
| Percentage or rounding behavior surprises users | Specify behavior explicitly and test common real-world examples. |
| History exposes sensitive information | Keep it local and provide prominent deletion controls. |
| Advanced features delay core quality | Ship the core calculation experience first; gate P1 features separately. |

#### 11. Delivery Plan and Launch Criteria

**Definition:** Approve calculation semantics, supported devices, precision rules, and accessibility requirements.

**Prototype:** Test basic arithmetic, scientific mode discovery, correction, and multitasking with representative users.

**Implementation and beta:** Build the calculation engine, adaptive interface, history, and accessibility support. Validate across supported devices and locales.

**Launch gates**

- All P0 requirements accepted.
- Reference calculation suite passes completely.
- Performance and reliability targets met.
- Accessibility review completed with no blocking issues.
- No unresolved critical or high-severity defects.
- History deletion and analytics privacy behavior verified.

#### 12. Open Decisions

- Which iPadOS versions and devices will be supported?
- What precision and maximum numeric range should the app guarantee?
- Should unit conversion be included at launch?
- What should repeated presses of equals do?
- Should later releases add Apple Pencil input, graphing, or synchronized history?

</details>
