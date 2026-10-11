# Example: Opportunity Solution Tree

> **Illustrative example.** A classic product sense question, worked through with the `opportunity-solution-tree` skill. All observations, numbers and evidence below are invented for demonstration. Nothing here is based on internal Spotify data.

![OST example](ost-example.png)

## The prompt

> You're the PM for podcasts at Spotify. Leadership wants more music-first listeners to become regular podcast listeners. Here's what we've heard from users and the team. Build the OST, pick where to focus, and tell me what to test first. Just go, make assumptions where needed.
>
> 1. People say they don't know what to listen to
> 2. Episodes are too long
> 3. Can't find the episode I was in the middle of
> 4. Home feed is all music
> 5. Tried a podcast, first 10 minutes were boring, quit
> 6. Need a podcast recommendations tab
> 7. Only listen during my commute
> 8. When I open Spotify I'm in music mode
> 9. Want shorter clips
> 10. I only start shows my friends recommend
> 11. Need a "continue listening" button
> 12. Ad revenue team wants more weekly podcast listeners
>
> Data: 18% of music-first MAU listen 10+ min of podcasts in 3 of 4 weeks. 22% of first plays of a new show are followed by a 2nd episode within 14 days.

---

## Output

### Root: outcome and KPI

| Field | Value |
|---|---|
| Metric | **Weekly podcast habit** |
| Definition | % of music-first monthly active users who play ≥10 min of podcasts in ≥3 of 4 weeks |
| Baseline | 18% (last full quarter) |
| Benchmark | Comparable discovery bets moved similar habit metrics by 4 to 8 points in two quarters `[assumed]` |
| Target | **25% within 2 quarters** (stretch but inside the benchmark range) |
| Source | Listening events |
| Owner | Podcast PM |
| Business link (hypothesis) | More habitual listeners → more podcast ad impressions and higher subscriber retention `[assumed]` |

Why not "podcast plays"? One-off plays don't build the habit the business case depends on. The root measures repeat behavior.

### Rewrites: solutions in disguise

| Original | Rewritten (customer voice) | Why |
|---|---|---|
| Need a podcast recommendations tab | "I don't know which show is worth my time" | A tab is a solution |
| Need a "continue listening" button | "I lose track of what I was in the middle of" | A button is a solution |
| Want shorter clips | "I don't have time for a full episode right now" | Clips are one possible answer |
| Ad revenue team wants more weekly listeners | Moved to the root's business link | The company's need, not the customer's |

### The tree

```
OUTCOME: Weekly podcast habit | KPI: 18% → 25% in 2 quarters
  ↳ drives: podcast ad revenue, subscriber retention (hypothesis)

├── O1 "I don't know which podcast is worth my time" [anecdote]   ★ TARGET
│   │   leading indicator: % of first plays of a new show followed by a 2nd episode within 14 days (22% → 30%)
│   ├── O1.1 "Trying a new show feels like a big commitment" [anecdote]   ★
│   └── O1.2 "Recommendations don't match my taste" [assumed]
│
├── O2 "Podcasts don't fit the moments I use Spotify" [anecdote]
│   │   leading indicator: % of commute-time sessions that include a podcast (9%)
│   ├── O2.1 "My commute is shorter than an episode" [anecdote]
│   └── O2.2 "When I open the app I'm in music mode" [anecdote]
│
├── O3 "I lose track of what I was listening to" [anecdote]
│       leading indicator: % of unfinished episodes resumed within 7 days (41%)
│
└── O4 "I only trust shows people I know recommend" [anecdote]
        leading indicator: % of show starts from shares (3%)
```

### Choose: target opportunity

| | Sizing | Market | Company | Customer | Confidence |
|---|---|---|---|---|---|
| **O1 Discovery** | **5** | 3 | **5** | **5** | M |
| O2 Moments | 4 | 3 | 4 | 3 | L |
| O3 Continuity | 3 | 2 (table stakes) | 3 | 4 | M |
| O4 Social proof | 3 | 4 (differentiator) | 3 | 4 | L |

- **Target:** O1, then O1.1 inside it
- **Runner-up:** O4 (strong differentiator, weak evidence)
- **What would change this call:** if data shows most music-first users never *start* a show, the problem is earlier (O2, being in music mode), not discovery.

### Solutions for O1.1

- **S1 Episode previews:** a 60-second preview of a show's best moment, playable inline in the home feed (suggested) ★
- **S2 Start-here picks:** each show recommends the one episode new listeners should start with (suggested)
- **S3 Clips feed:** a vertical feed of short podcast clips (ambitious, suggested)
- **S4 Editorial starter lists:** hand-picked "start here" lists for 3 genres (cheap, suggested)

### Assumptions (S1)

| # | Assumption | Type | Importance | Evidence | Riskiest? |
|---|---|---|---|---|---|
| A1 | ≥5% of music-first users who see a preview will tap it | Desirability | H | L | ⚠ |
| A2 | Previews in the feed don't reduce music listening time | Viability | H | L | ⚠ |
| A3 | ≥20% of preview listeners start the full episode | Desirability | H | M | |
| A4 | We can pick a "best 60 seconds" automatically at scale | Feasibility | M | M | |
| A5 | Show creators are fine with us choosing their preview | Viability | M | L | |

### Test cards

**T1 (A1): 1% feed test, 2 weeks**
- Preview card shown to 1% of music-first users, hand-picked previews for 50 shows
- Success: ≥5% tap rate **and** ≥20% of tappers start the episode
- Pass → invest in automated preview selection. Fail → try S2.

**T2 (A2): Holdout guardrail, same test**
- Compare music minutes per user, test vs holdout
- Success: no drop beyond 1%
- Fail → previews only in podcast-related surfaces

### RICE (illustrative)

| | Reach / qtr | Impact | Confidence | Effort (pw) | RICE |
|---|---|---|---|---|---|
| **S1 Previews** | 2M | 2 | 50% | 8 | **250K** |
| S2 Start-here picks | 1.5M | 1 | 50% | 4 | 187.5K |
| S4 Editorial lists | 500K | 1 | 50% | 2 | 125K |
| S3 Clips feed | 3M | 3 | 20% | 30 | 60K |

Sensitivity: if S1 effort grows to 11 person-weeks, S2 wins.

### Pushback

1. **The target leans on an assumed benchmark.** Check the 4 to 8 point range against your own past discovery launches before committing to 25% in public.
2. **O1 was picked on anecdotes.** Run 5 interviews with music-first users about the last time they tried a new show before committing.
3. **S1 competes with music for the same feed slot.** The guardrail test isn't optional.

### Next step this week

Pull the funnel for music-first users: saw a podcast → started one → reached episode 2. The biggest drop decides between O1, O2 and O3.
