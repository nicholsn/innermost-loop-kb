---
type: Benchmark
title: LiveCodeBench
description: A contamination-free benchmark of LLM coding ability that continuously collects new problems from LeetCode, AtCoder and Codeforces contests and evaluates code generation, self-repair, code execution and test-output prediction.
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/uc-berkeley
  - https://nicholsn.github.io/innermost-loop-kb/organizations/mit
measures_capability: competitive-programming code generation on post-cutoff problems
resource: https://livecodebench.github.io/
tags:
  - "open-source"
sources:
  - { id: iml-2026-04-05, resource: https://theinnermostloop.substack.com/p/welcome-to-april-5-2026, title: "Welcome to April 5, 2026", author: human:alex-wissner-gross, last_modified: "2026-04-05" }
---

LiveCodeBench (Jain et al., UC Berkeley, MIT and Cornell) collects problems from periodic LeetCode, AtCoder and Codeforces contests, annotates them with release dates so that a model can be scored only on problems published after its training cutoff, and evaluates several code scenarios beyond generation ([site](https://livecodebench.github.io/)). In this corpus it is the yardstick for Apple's [simple self-distillation](/developments/2026-04-05-self-distillation-without-a-teacher.md), which moved [Qwen3-30B-Instruct](/systems/qwen3-30b-instruct.md) from 42.4% to 55.3% pass@1 on the v6 release with no verifier, teacher or reinforcement learning.
