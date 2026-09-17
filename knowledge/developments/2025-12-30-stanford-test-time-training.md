---
type: Development
title: Test-time training gives continual learning constant latency
claim: Stanford researchers achieved continual learning via test-time training, letting models learn from next-token prediction at constant latency regardless of context length.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2025-12-30
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/stanford
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-24-sholto-continual-learning-2026
description: Long context is reframed as a continual-learning problem the model solves by compressing what it reads into its own weights, six days after an Anthropic researcher predicted continual learning would be solved in 2026.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-09-in-place-test-time-training
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-02-prime-intellect-rlm
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-million-token-windows-ship
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2025-12-30"
  - "test-time-training"
  - "continual-learning"
generated: { by: process:iml-emit, at: "2025-12-30T00:00:00Z" }
sources:
  - { id: iml-2025-12-30, resource: https://theinnermostloop.substack.com/p/welcome-to-december-30-2025, title: "Welcome to December 30, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-30", supporting_text: continual learning via test-time training }
  - { id: ttt-e2e-paper-pdf, resource: https://test-time-training.github.io/e2e.pdf, title: End-to-End Test-Time Training for Long Context, author: org:stanford }
  - { id: ttt-e2e-arxiv, resource: https://arxiv.org/abs/2512.23675v1, title: End-to-End Test-Time Training for Long Context, author: org:stanford, last_modified: "2025-12-29" }
---

The paper (Tandon, Dalal and twelve co-authors including Hashimoto, Guestrin, Choi and Yu Sun; arXiv 2512.23675, posted 29 December 2025) formulates long-context modeling as continual learning: a standard sliding-window Transformer keeps training at test time by next-token prediction on the context it is reading, compressing that context into its weights, with meta-learning at training time to initialize the learner. TTT-E2E scales with context length the way full attention does while Mamba 2 and Gated DeltaNet do not, yet keeps RNN-like constant latency, 2.7 times faster than full attention at 128K context ([arXiv](https://arxiv.org/abs/2512.23675)). In the trajectory it turns the [prediction that continual learning is solved in 2026](/developments/2025-12-24-sholto-continual-learning-2026.md) into a published mechanism within a week, opens the weight-level route to long context that [ByteDance's in-place test-time training](/developments/2026-04-09-in-place-test-time-training.md) extends in April, and sits beside the scaffold-level route of the [Recursive Language Model](/developments/2026-01-02-prime-intellect-rlm.md) three days later.
