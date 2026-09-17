---
type: Benchmark
title: PostTrainBench
description: Benchmark that gives coding agents four small base models, one GPU and ten hours to post-train them, ranking how well models train other models.
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/tubingen-ai-center
measures_capability: a model's skill at post-training other models
resource: https://posttrainbench.com/
tags:
  - "open-source"
sources:
  - { id: iml-2025-12-18, resource: https://theinnermostloop.substack.com/p/welcome-to-december-18-2025, title: "Welcome to December 18, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-18" }
---

PostTrainBench asks whether LLM agents can post-train LLMs: each agent gets four small base models (Qwen 3 1.7B and 4B, SmolLM3-3B, Gemma 3 4B), a single H100 and ten hours, and is scored on downstream benchmarks (five at the December 2025 launch, seven weighted from v1.0 in March 2026) ([site](https://posttrainbench.com/), [paper](https://arxiv.org/abs/2603.08640)). In this corpus it is the ruler for the model-trains-model loop: [GPT-5.1-Codex-Max led the first cut](/developments/2025-12-18-posttrainbench-models-training-models.md) in December 2025, [v1.0](/developments/2026-03-12-posttrainbench-v1.md) reframed the task as recursive self-improvement in March 2026, and OpenAI's [Sol scored 50.3%](/developments/2026-07-10-a-model-post-trains-a-model.md) on it after post-training Luna in July.
