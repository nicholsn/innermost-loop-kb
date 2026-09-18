# Temporal analytics: persona walkthroughs and design decisions

September 18, 2026. This is a second **simulated** research round, using the owner's previously selected method. No participants were interviewed. The owner relayed feedback about timelines, but no transcript was available; no further feedback is attributed to real people.

## Evidence and analytical boundaries

At baseline commit 4d301b6 the corpus contains 2,961 developments, 2,893 with `evidences` theme links, 2,548 with `actor` links, and only 50 with `occurred_on`. Existing timelines show records chronologically but do not aggregate theme trajectories or compare coverage. The rich relationship structure supports aggregation without drawing a network. Counts reflect editorial selection and extraction, not independent corroboration, confidence, event frequency, or real-world importance. A development can link to several themes; per-theme shares can sum above 100%. Repeated source reporting is not independent evidence.

## Provisional analytical personas

These are task-based hypotheses, not participant quotes or market segments established by research.

| Persona | Task / simulated feedback | Risk to address | Implemented response |
| --- | --- | --- | --- |
| Research synthesis analyst | Compare how evidence accumulates for three explanations; identify an inflection and read the contributing claims | A cumulative line always rises and can disguise inactivity | Theme growth chart with cumulative/new-record/share modes; common scale; point-to-record drilldown |
| Editorial coverage analyst | Separate a topic's increased prominence from an increase in newsletter output | Counts alone conflate editorial volume and topic attention | Monthly coverage pulse, count/share toggle, monthly denominator shown; empty months distinguished from zero theme matches |
| Policy horizon scanner | Identify bursts and quieter periods without inferring that nothing happened in the world | Partial months and missing coverage look like real-world changes | Explicit reporting-date range, partial-month labels, zero-coverage gaps, no extrapolation |
| Competitive intelligence researcher | See which organizations or people occur in the same theme evidence during a selected period | Co-mention is mistaken for influence or a business relationship | Ranked actor footprint linked through developments; unique record counts; drilldown into actor/theme evidence |
| Evidence auditor | Reconcile a chart value to identifiable records and source links | Duplicate edges and multiple theme assignments inflate totals | Deduplicate developments per theme and actors per development; linked detail pages and CSV export; explicit metric definitions |

Cross-cutting needs: readable narrow-screen views, keyboard access, equivalent data tables, saved URL state, and visible empty/error states. Keep charts useful without relying on color or hovering.

## Walkthrough synthesis and alternatives

The synthesis analyst follows theme selection → cumulative trajectory → a monthly increment → claim/source detail. The editorial analyst switches the same data to a share of all recorded developments to check whether a burst simply follows a larger issue. The horizon scanner uses the pulse's blank/zero distinction and partial-month note before interpreting a lull. The intelligence researcher selects a month, ranks its actors, then opens the actor's matching records. The auditor uses the numeric tables to reproduce the same counts. These paths are analytical evaluations of the design, not measured user success rates.

Three complementary views are selected: a theme-growth line chart, a monthly pulse heatmap, and ranked actor bars for the current period. Cumulative counts describe stock; monthly additions describe flow. This follows the distinction in [ONS chart-selection guidance](https://service-manual.ons.gov.uk/data-visualisation/chart-types/choosing-a-chart-type); [ONS line-chart guidance](https://service-manual.ons.gov.uk/data-visualisation/chart-types/line-chart) supports comparisons over time. Textual descriptions and equivalent data tables follow [W3C complex-image guidance](https://www.w3.org/WAI/tutorials/images/complex/).

Deferred: confidence scores (no independent-verification model); Sankey diagrams (theme links are not flows); causal diagrams (co-occurrence is not causation); event forecasts (reporting history does not supply an event-generating model); source-diversity-as-corroboration scores (shared newsletter citations and syndicated reporting are dependent). A calendar heatmap adds detail without helping the monthly comparison task yet.

## Review questions and real-user follow-up

Ask reviewers to compare two themes, explain the cumulative versus monthly view, reconcile one peak to records, identify who appears in that period, and explain why a high count is not strong verification. Recruit 5–8 real analysts/readers across these tasks, including keyboard/screen-reader users. Record comprehension mistakes and task detours; do not manufacture completion percentages. Revisit the three-theme default, monthly granularity, actor ranking, and whether share-of-coverage is understandable after that round.

## Implementation contract

Use unique Development IDs and typed `evidences` / `actor` relations, resolving references through the bundle. Use reporting dates (linked issue dates where available; dated record IDs as fallback), never ingestion timestamps. Unknown dates are counted and excluded from temporal aggregates. Only present themes/actors are resolved. Date ranges are inclusive; cumulative totals start at the selected range's beginning. Monthly share divides the theme's unique developments by all dated developments in the same month and date range. Empty denominators yield no data, not 0%. Actor counts deduplicate records across selected themes. All aggregates link back to source records. No production merge/deployment is requested in this review round.

## Prototype walkthrough findings

The implemented corpus projection resolves 2,961 dated developments, 68 without theme links, and no undated records. The default compute trajectory reconciles to 271 developments. Its September pulse is 10 / 117 = 8.5%; keyboard activation reveals exactly ten records, and choosing Crusoe reveals one. That actor/month/theme selection survives reload. A September 16-only range has zero coverage and recovers through Reset. The 320px viewport contains chart/table scrolling without horizontal page overflow. No browser console errors were reported in these checks. Axis review caught fractional tick labels on record counts; ticks were changed to integer intervals.

Validation: 16 automated tests pass, including duplicate-edge handling, multi-theme deduplication, missing-month denominators, inclusive date boundaries, cumulative rebasing, actor filtering, date validation, and CSV formatting. The production build generates 4,839 pages. These are implementation checks, not measured participant outcomes.
