---
type: Development
title: A lab reports its AI R&D evaluations have saturated
claim: Anthropic disclosed an unreleased Model 2 it has no plans to release, more powerful than Mythos 5, while nudging its misalignment risk from very low to low, and its August Risk Report admitted the lab's AI R&D evaluations have saturated with Claude now authoring most code merged into its own production repositories.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-08-15
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/anthropic-model-2
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-mythos-5
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/cobench-v2
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/r-and-d-evals-saturated
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/public-internal-divergence
  - https://nicholsn.github.io/innermost-loop-kb/themes/a-model-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/themes/benchmark-saturation
  - https://nicholsn.github.io/innermost-loop-kb/themes/takeoff-declared
score: 12.5 points on CoBench v2
occurred_on: "2026-08-14"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-08-a-release-slowed-on-an-unprovable-negative
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-05-when-ai-builds-itself
description: "The lab's own yardstick for AI accelerating AI research stops discriminating just as its model writes most of the code merged into its production systems: the measurement gives out before the phenomenon does."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-rsi-is-a-present-phenomenon
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-08-100pct-of-product-code
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-24-researchers-replaced-first
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-08-15"
  - "rsi"
  - "ai-r-and-d"
  - "evaluation"
  - "alignment"
generated: { by: process:iml-emit, at: "2026-08-15T00:00:00Z" }
sources:
  - { id: iml-2026-08-15, resource: https://theinnermostloop.substack.com/p/welcome-to-august-15-2026, title: "Welcome to August 15, 2026", author: human:alex-wissner-gross, last_modified: "2026-08-15", supporting_text: "admits its AI R&D evals have “saturated,” with Claude now authoring most code" }
  - { id: axios-anthropic-model-2-risk, resource: https://www.axios.com/2026/08/14/anthropic-model-2-ai-risk, title: Anthropic Model 2 AI risk (Axios), author: org:axios, last_modified: "2026-08-14" }
  - { id: anthropic-risk-report-august-2026, resource: https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf, title: "Risk Report, August 2026 (redacted)", author: org:anthropic, last_modified: "2026-08-14" }
  - { id: daniel-mac8-cobench-v2-takeoff-math, resource: https://x.com/daniel_mac8/status/2088344245178716175, title: Model 2 beat Mythos 5 by 12.5 points on CoBench v2 (X post), author: human:daniel_mac8 }
---

Anthropic's redacted August 2026 Risk Report, published alongside the disclosure of an unreleased [Model 2](/systems/anthropic-model-2.md) stronger than [Mythos 5](/systems/claude-mythos-5.md), states that the lab's AI R&D evaluations have saturated, with [Claude](/systems/claude.md) now authoring most of the code merged into Anthropic's own production repositories, while the lab moves its misalignment-risk rating from “very low” to “low” ([risk report](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf); [Axios](https://www.axios.com/2026/08/14/anthropic-model-2-ai-risk)). Watchers did the arithmetic on the redacted numbers: Model 2 beat Mythos 5 by 12.5 points on [CoBench v2](/benchmarks/cobench-v2.md), whose 85% threshold marks researcher replacement, so “2027 is the takeoff” ([X](https://x.com/daniel_mac8/status/2088344245178716175)). In the trajectory this is the point where the measuring instrument gives out: it follows the lab's own [When AI builds itself](/developments/2026-06-05-when-ai-builds-itself.md) evidence and the March figure of [70–90% of model code](/developments/2026-03-16-rsi-is-a-present-phenomenon.md), extends the [effectively all product code](/developments/2026-02-08-100pct-of-product-code.md) claim to the repositories behind the models, and is answered in the same issue by the [Conceptual Reasoning Index](/developments/2026-08-15-scoring-the-unverifiable.md), a new instrument for what the old ones can no longer score.
