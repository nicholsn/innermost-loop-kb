---
type: Development
title: A model speeds up training code thirteen times better than a skilled human
claim: On a standing test to speed up model-training code, Mythos Preview reached roughly 52x where a skilled human reaches 4x and 2024's Opus 4 managed 3x, while Anthropic engineers now ship eight times as much code per quarter as in 2021-2025.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-06-05
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-mythos
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-opus-4
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/humans-need-not-apply
  - https://nicholsn.github.io/innermost-loop-kb/themes/engineer-as-supervisor
score: ~52x vs 4x human
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-34x-speedup
description: The clearest instance in the corpus of a model outperforming skilled humans at the very task that speeds up making the next model, which is the mechanism the recursive loop depends on.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-08-100pct-of-product-code
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-08-research-sped-up-400x
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-29-a-model-writes-the-kernels-that-run-it
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-06-05"
  - "rsi"
  - "ai-r-and-d"
  - "capability-jump"
generated: { by: process:iml-emit, at: "2026-06-05T00:00:00Z" }
sources:
  - { id: iml-2026-06-05, resource: https://theinnermostloop.substack.com/p/welcome-to-june-5-2026, title: "Welcome to June 5, 2026", author: human:alex-wissner-gross, last_modified: "2026-06-05", supporting_text: Mythos Preview hit ~52x }
  - { id: anthropic-x-mythos-preview-52x, resource: https://x.com/AnthropicAI/status/2062568869240476050, title: "Anthropic on X: Mythos Preview hits ~52x on the training-code speedup test", author: org:anthropic }
  - { id: anthropic-x-engineers-ship-8x-code, resource: https://x.com/AnthropicAI/status/2062568864240836995, title: "Anthropic on X: engineers ship 8x as much code per quarter", author: org:anthropic }
  - { id: anthropic-institute-report-speedup-figures, resource: https://www.anthropic.com/institute/recursive-self-improvement, title: When AI builds itself, author: org:anthropic-institute }
---

On Anthropic's standing test of speeding up model-training code, Mythos Preview reached roughly 52x against the 4x a skilled human engineer reaches and the 3x that [Opus 4](/systems/claude-opus-4.md) managed (the post dates it to 2024; the model shipped in May 2025) ([Anthropic on X](https://x.com/AnthropicAI/status/2062568869240476050); [report](https://www.anthropic.com/institute/recursive-self-improvement)). The same thread reports Anthropic engineers shipping 8x as much code per quarter as in 2021-2025. It is the direct successor of February's [34x speedup by Opus 4.6](/developments/2026-02-06-opus-34x-speedup.md), where 4x had counted as a day's human work, and it sits beside the [400x internal research speedup](/developments/2026-04-08-research-sped-up-400x.md) claimed for [Claude Mythos](/systems/claude-mythos.md) in April; the [steering result](/developments/2026-06-05-the-model-learns-to-steer.md) from the same report covers the problem-selection half of the loop.
