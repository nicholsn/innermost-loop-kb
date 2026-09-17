---
type: Development
title: A model reportedly speeds internal AI research by up to 400x
claim: Anthropic reports Claude Mythos sped up internal AI research by up to 400 times on tasks equivalent to forty hours of expert work, while arguing the two- to fourfold slope jump still has not tripped its Responsible Scaling Policy threshold for AI research doubling.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-04-08
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-mythos
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/epoch-capabilities-index
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/safety-pledges-recede
score: 400x
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-07-seventy-two-hours-fifty-experiments
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-rsi-is-a-present-phenomenon
description: A frontier lab puts a research-wide multiplier on how much its model accelerates its own R&D, delivered alongside the lab's own ruling that the jump stays under the safety threshold written to catch it.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-08-mythos-benchmark-sweep
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-27-claude-mythos-leaked
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-34x-speedup
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-08-mythos-benchmark-sweep, relation_label: extends }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-04-08"
  - "rsi"
  - "ai-r-and-d"
  - "capability-jump"
  - "policy"
generated: { by: process:iml-emit, at: "2026-04-08T00:00:00Z" }
sources:
  - { id: iml-2026-04-08, resource: https://theinnermostloop.substack.com/p/welcome-to-april-8-2026, title: "Welcome to April 8, 2026", author: human:alex-wissner-gross, last_modified: "2026-04-08", supporting_text: sped up internal AI research by up to 400x }
  - { id: scaling01-mythos-400x-research-speedup, resource: https://x.com/scaling01/status/2041584495061504159, title: Anthropic reports Mythos sped up internal AI research by up to 400x on 40-hour expert tasks (X post), author: human:scaling01 }
  - { id: lifland-mythos-slope-jump-rsp-threshold, resource: https://x.com/eli_lifland/status/2041655642948260228, title: The 2-4x slope jump has not tripped Anthropic's RSP threshold for AI R&D doubling (X post), author: human:eli-lifland }
---

Anthropic's figure, relayed via [an X post](https://x.com/scaling01/status/2041584495061504159), is that [Claude Mythos](/systems/claude-mythos.md) accelerated internal AI research by as much as 400x on tasks sized at about 40 hours of expert work. The same launch produced an apparent upward discontinuity on the [Epoch Capabilities Index](/benchmarks/epoch-capabilities-index.md), recorded in the [benchmark sweep](/developments/2026-04-08-mythos-benchmark-sweep.md), and Anthropic's position, [summarized by Eli Lifland](https://x.com/eli_lifland/status/2041655642948260228), is that the resulting 2-4x steepening of the slope still falls short of the Responsible Scaling Policy trigger for a doubling of AI R&D speed. In the [recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it turns the qualitative claims of March, that [70-90% of Anthropic's model code is written by Claude](/developments/2026-03-16-rsi-is-a-present-phenomenon.md), into a lab-stated multiplier, one day after UNC's [72-hour unattended run](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md) and eight days before Anthropic turned the same machinery on [alignment research](/developments/2026-04-16-weak-to-strong-supervision.md); the 34x kernel speedup [found by Opus in February](/developments/2026-02-06-opus-34x-speedup.md) is the nearest earlier per-task figure.
