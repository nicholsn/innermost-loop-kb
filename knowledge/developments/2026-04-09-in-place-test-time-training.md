---
type: Development
title: A 4B model dominates long context by rewriting its own weights in flight
claim: ByteDance introduced in-place test-time training, repurposing projection matrices as fast weights so a four-billion-parameter model can dominate at 128,000 tokens of context.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-04-09
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/bytedance
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
score: 4B at 128k context
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-05-self-distillation-without-a-teacher
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-30-stanford-test-time-training
description: "Self-improvement moves from the scaffold into the weights: a deployed model updates part of itself on each input stream, making adaptation a property of inference rather than of a retraining cycle."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-04-rlm-two-orders-of-context
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-million-token-windows-ship
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-04-09"
  - "test-time-training"
  - "continual-learning"
  - "self-modification"
  - "rsi"
generated: { by: process:iml-emit, at: "2026-04-09T00:00:00Z" }
sources:
  - { id: iml-2026-04-09, resource: https://theinnermostloop.substack.com/p/welcome-to-april-9-2026, title: "Welcome to April 9, 2026", author: human:alex-wissner-gross, last_modified: "2026-04-09", supporting_text: repurposing MLP projection matrices as fast weights so a 4B model can dominate at 128k }
  - { id: in-place-ttt-arxiv, resource: https://arxiv.org/abs/2604.06169, title: In-Place Test-Time Training, author: org:bytedance }
---

The paper ([arXiv 2604.06169](https://arxiv.org/abs/2604.06169)) makes the final projection matrix of every MLP block the model's fast weights, swaps test-time training's usual reconstruction loss for an objective tied to next-token prediction, and updates in chunks so the method runs under context parallelism; applied in place to an existing 4B-parameter model it gives superior results on tasks with contexts up to 128k tokens, and the same recipe also works when pretrained from scratch. The newsletter's framing is that ByteDance is 'making old models smarter mid-flight', a drop-in answer to the long-context problem that Anthropic had addressed weeks earlier with [million-token windows](/developments/2026-03-16-million-token-windows-ship.md) and Prime Intellect with [recursive self-calls](/developments/2026-01-04-rlm-two-orders-of-context.md). In the [recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it extends Stanford's [constant-latency test-time training](/developments/2025-12-30-stanford-test-time-training.md) from December and Apple's [teacherless self-distillation](/developments/2026-04-05-self-distillation-without-a-teacher.md) of four days earlier: the model modifies its own weights during use rather than between training runs.
