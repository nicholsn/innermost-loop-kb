---
type: Development
title: An agent architecture lifts a model from 30% to a perfect 100
claim: Nvidia's AVO agent architecture lifted Claude Opus 5 from a 30% baseline to a perfect 100 on ARC-AGI-3, sweeping all 183 levels, fresh off a week evolving GPU kernels past FlashAttention-4.
domain: benchmarks
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-08-23
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/nvidia
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/nvidia-avo
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-opus-5
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/arc-agi-3
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/harness-as-generalizer
  - https://nicholsn.github.io/innermost-loop-kb/themes/benchmark-saturation
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/scaffolding-over-weights
score: 30% to 100%
occurred_on: "2026-08-21"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-13-ninety-six-percent-with-stock-tooling-for-five-hundred-dollars
description: "The systems-side twin of the research-taste result: a general-purpose agent architecture rather than a new checkpoint closes the benchmark launched five months earlier to humble the frontier, and the same architecture had just spent a week evolving the kernels it runs on."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-27-arc-agi-3-humbles-the-frontier
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-29-a-model-writes-the-kernels-that-run-it
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-23-research-taste-trained-by-reinforcement-learning, relation_label: corroborates }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-08-23"
  - "agent-harness"
  - "capability-jump"
  - "evaluation"
  - "kernels"
generated: { by: process:iml-emit, at: "2026-08-23T00:00:00Z" }
sources:
  - { id: iml-2026-08-23, resource: https://theinnermostloop.substack.com/p/welcome-to-august-23-2026, title: "Welcome to August 23, 2026", author: human:alex-wissner-gross, last_modified: "2026-08-23", supporting_text: lifting Claude Opus 5 from a 30% baseline to a perfect 100 on ARC-AGI-3 }
  - { id: nvidia-avo-arc-agi-3-blog, resource: https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/, title: "NVIDIA AVO Reaches 100% on ARC-AGI-3, Demonstrating a Frontier-Level General-Purpose Architecture for Long-Horizon Autonomous Agents", author: org:nvidia, last_modified: "2026-08-21" }
---

Nvidia's [AVO](/systems/nvidia-avo.md) is a general-purpose architecture for long-horizon autonomous agents; wrapped around [Claude Opus 5](/systems/claude-opus-5.md) it scored 100.00 on the [ARC-AGI-3](/benchmarks/arc-agi-3.md) public set, completing all 183 levels across 25 environments where the bare model's baseline was 30% ([NVIDIA blog](https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/)). The week before, the same agent had explored more than 500 directions on DGX B200 systems and produced kernels beating cuDNN by up to 3.5% and FlashAttention-4 by up to 10.5%. The newsletter pairs it with Inherent's [research-taste result](/developments/2026-08-23-research-taste-trained-by-reinforcement-learning.md) as the systems-side proof that architecture, not model capability alone, now moves the frontier. In the trajectory it closes the benchmark that [returned frontier models to near zero](/developments/2026-03-27-arc-agi-3-humbles-the-frontier.md) in March, eight days after [stock Claude Code lifted the same model to 96.2%](/developments/2026-08-13-ninety-six-percent-with-stock-tooling-for-five-hundred-dollars.md), and joins the [232x kernel](/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup.md) and [KernelBench](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) results on the line where agents rewrite the kernels they run on.
