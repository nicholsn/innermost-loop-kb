---
type: Development
title: A model improves by fine-tuning on its own samples
claim: Apple researchers showed language models can self-improve at coding through simple self-distillation, sampling their own outputs and fine-tuning on them with no verifier, teacher or reinforcement learning, lifting one model from 42.4% to 55.3% on LiveCodeBench with gains concentrated on the hardest problems.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-04-05
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/apple
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/qwen3-30b-instruct
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/livecodebench
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
score: 42.4% → 55.3%
occurred_on: "2026-04-01"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-31-bilevel-autoresearch
description: The self-improvement loop shrinks to its minimum, with no search, no reward, no teacher and no verifier between a model and its own better samples, which the author reads as the Singularity learning to teach itself.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-12-posttrainbench-v1
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-09-in-place-test-time-training
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-31-a-student-outgrows-every-teacher
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-04-05"
  - "distillation"
  - "rsi"
  - "model-trains-model"
generated: { by: process:iml-emit, at: "2026-04-05T00:00:00Z" }
sources:
  - { id: iml-2026-04-05, resource: https://theinnermostloop.substack.com/p/welcome-to-april-5-2026, title: "Welcome to April 5, 2026", author: human:alex-wissner-gross, last_modified: "2026-04-05", supporting_text: lifting Qwen3-30B-Instruct from 42.4% to 55.3% on LiveCodeBench }
  - { id: apple-simple-self-distillation-arxiv, resource: https://arxiv.org/abs/2604.01193, title: Embarrassingly Simple Self-Distillation Improves Code Generation, author: org:apple, last_modified: "2026-04-01" }
  - { id: apple-ml-ssd-code, resource: https://github.com/apple/ml-ssd, title: "apple/ml-ssd: code for Simple Self-Distillation", author: org:apple }
---

Simple self-distillation (SSD) samples solutions from the model at chosen temperature and truncation settings and fine-tunes on them with ordinary supervised fine-tuning; the paper ([arXiv](https://arxiv.org/abs/2604.01193), [code](https://github.com/apple/ml-ssd)) lifts [Qwen3-30B-Instruct](/systems/qwen3-30b-instruct.md) from 42.4% to 55.3% pass@1 on [LiveCodeBench](/benchmarks/livecodebench.md) v6, generalizes across Qwen and Llama models at 4B, 8B and 30B in instruct and thinking variants, and traces the gain to a precision-exploration conflict in decoding that SSD resolves by suppressing distractor tails where precision matters while keeping diversity where exploration matters. Where [Bilevel Autoresearch](/developments/2026-03-31-bilevel-autoresearch.md) five days earlier improved a model's research loop, this removes the loop's scaffolding entirely and still gets a model to improve itself, the tightest form of [recursive self-improvement](/themes/recursive-self-improvement.md) in the corpus to date. It is followed within days by ByteDance's [in-place test-time training](/developments/2026-04-09-in-place-test-time-training.md) and UNC's [72-hour autonomous run](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md), and prefigures July's finding that [a student distilled from weaker teachers keeps improving](/developments/2026-07-31-a-student-outgrows-every-teacher.md).
