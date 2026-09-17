---
type: Benchmark
title: CoBench v2
description: Anthropic's internal AI R&D evaluation, defined in its August 2026 Risk Report, whose 85% threshold the lab itself estimates would mark full researcher substitution and on which Model 2 beat Mythos 5 by 12.5 points.
measures_capability: AI research and development capability against a researcher-replacement threshold
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
resource: https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf
tags:
  - "research-agent"
sources:
  - { id: iml-2026-08-15, resource: https://theinnermostloop.substack.com/p/welcome-to-august-15-2026, title: "Welcome to August 15, 2026", author: human:alex-wissner-gross, last_modified: "2026-08-15" }
---

CoBench is [Anthropic](/organizations/anthropic.md)'s internal evaluation, defined in section 3.4.3 of its redacted August 2026 Risk Report: a model is placed at a historical point in Anthropic's infrastructure, given a snapshot of the codebase, logs, messaging and docs, and asked to diagnose the root causes of issues its engineers actually solved, across 449 problems drawn from February to April 2026 ([risk report](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf)). The 85% threshold is the lab's own estimate of the score a model truly capable of fully substituting for its research staff would reach; watchers applied it to the redacted gap between [Model 2](/systems/anthropic-model-2.md) and [Mythos 5](/systems/claude-mythos-5.md), 12.5 points, to conclude that “2027 is the takeoff” ([X](https://x.com/daniel_mac8/status/2088344245178716175)). It stands beside [PostTrainBench](/benchmarks/posttrainbench.md) as one of the few named instruments for AI doing AI research, introduced at the moment the lab says its task-based AI R&D evaluations have [saturated](/developments/2026-08-15-the-r-and-d-evals-have-saturated.md).
