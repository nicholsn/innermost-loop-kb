---
type: AISystem
title: Self-Harness
description: Shanghai AI Laboratory's paradigm in which an LLM agent improves its own operating harness through weakness mining, harness proposal and regression-tested validation, with no human engineers or stronger external agents.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/shanghai-ai-laboratory
modality: code
evaluated_on:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/terminal-bench-2
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/swe-bench-verified
resource: https://arxiv.org/abs/2606.09498
tags:
  - "coding-agent"
sources:
  - { id: iml-2026-06-25, resource: https://theinnermostloop.substack.com/p/welcome-to-june-25-2026, title: "Welcome to June 25, 2026", author: human:alex-wissner-gross, last_modified: "2026-06-25" }
---

Self-Harness runs an iterative loop of three stages: Weakness Mining, which extracts model-specific failure patterns from execution traces; Harness Proposal, which generates minimal harness edits tied to those failures; and Proposal Validation, which accepts an edit only after regression testing ([paper](https://arxiv.org/abs/2606.09498)). Instantiated from a minimal starting harness on [Terminal Bench 2.0](/benchmarks/terminal-bench-2.md), [SWE-bench Verified](/benchmarks/swe-bench-verified.md) and AppWorld with MiniMax M2.5, Qwen3.5-35B-A3B and [GLM-5](/systems/glm-5.md), every final harness improved both held-in and held-out pass rates, with relative gains of up to 132%. In this corpus it is the system behind [an agent rewriting its own harness](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md), the item that gave the [self-authored-scaffolding](/themes/self-authored-scaffolding.md) theme its name.
