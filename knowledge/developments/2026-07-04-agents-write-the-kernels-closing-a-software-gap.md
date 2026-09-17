---
type: Development
title: A challenger GPU serves an open model at half the cost as agents write kernels
claim: Wafer served GLM-5.2 on AMD's MI355X at 2,626 tokens per second per node at less than half Blackwell's cost, arguing AMD's software gap is closing because AI agents now write the kernels.
domain: compute
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-07-04
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/wafer-inc
  - https://nicholsn.github.io/innermost-loop-kb/organizations/amd
  - https://nicholsn.github.io/innermost-loop-kb/organizations/nvidia
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/glm-5-2
  - https://nicholsn.github.io/innermost-loop-kb/hardware/amd-mi355x
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/intelligence-per-watt
  - https://nicholsn.github.io/innermost-loop-kb/themes/vertical-silicon
score: 2,626 tok/s/node
occurred_on: "2026-07-03"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-03-circuits-drawn-in-minutes-not-months
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-03-seventeen-leaders-in-two-years
description: "The kernel-writing loop leaves the leaderboard and lands on market structure: if agents write the kernels, the software moat that kept a challenger GPU out of frontier serving stops being a moat."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-29-a-model-writes-the-kernels-that-run-it
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-04-authoring-minds-becomes-an-artform, relation_label: extends }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-07-04"
  - "kernels"
  - "rsi"
  - "compute-scaling"
  - "open-weights"
generated: { by: process:iml-emit, at: "2026-07-04T00:00:00Z" }
sources:
  - { id: iml-2026-07-04, resource: https://theinnermostloop.substack.com/p/welcome-to-july-4-2026, title: "Welcome to July 4, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-04", supporting_text: arguing AMD’s software gap is closing because AI agents now write the kernels }
  - { id: wafer-glm52-amd-blog, resource: https://www.wafer.ai/blog/glm52-amd, title: Performance per dollar is getting faster and cheaper, author: org:wafer-inc, last_modified: "2026-07-03" }
---

Wafer's write-up ([blog](https://www.wafer.ai/blog/glm52-amd)) reports [GLM-5.2](/systems/glm-5-2.md) served on AMD's [Instinct MI355X](/hardware/amd-mi355x.md) at 2,626 tokens per second per node for less than half the cost of Nvidia's Blackwell, and credits AI agents writing the kernels for closing the software gap that has protected the incumbent. The newsletter reads it as 'the silicon is cooperating' with the [cheap post-training economics](/developments/2026-07-04-authoring-minds-becomes-an-artform.md) of the same open model. In the recursion trajectory it carries the kernel strand, [GPT-5.5 topping KernelBench](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) in April and [Fable 5's megakernel](/developments/2026-07-03-seventeen-leaders-in-two-years.md) the day before, from benchmark scores to production serving on a rival vendor's chips, a month before [self-improving agents rebuild an inference stack](/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on.md) on B200s.
