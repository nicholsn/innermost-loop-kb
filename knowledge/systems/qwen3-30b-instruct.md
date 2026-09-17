---
type: AISystem
title: Qwen3-30B-Instruct
description: Alibaba's 30-billion-parameter Qwen3 instruct model (reported in the Apple paper as Qwen3-30B-Instruct, the Qwen3-30B-A3B-Instruct-2507 checkpoint), the base model that simple self-distillation lifted from 42.4% to 55.3% on LiveCodeBench.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/alibaba
modality: text
evaluated_on:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/livecodebench
resource: https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507
tags:
  - "open-weight-model"
sources:
  - { id: iml-2026-04-05, resource: https://theinnermostloop.substack.com/p/welcome-to-april-5-2026, title: "Welcome to April 5, 2026", author: human:alex-wissner-gross, last_modified: "2026-04-05" }
---

An open-weight model from Alibaba's Qwen3 family with about 30 billion total parameters and, per its A3B designation, roughly 3 billion active per token ([model card](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507)). In this corpus it is the subject of Apple's [self-distillation result](/developments/2026-04-05-self-distillation-without-a-teacher.md), where fine-tuning on its own samples with no verifier, teacher or reinforcement learning raised its [LiveCodeBench](/benchmarks/livecodebench.md) v6 pass@1 from 42.4% to 55.3%, with the gains concentrated on the hardest problems.
