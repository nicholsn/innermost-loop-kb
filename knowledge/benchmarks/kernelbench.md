---
type: Benchmark
title: KernelBench
description: A benchmark from Stanford's Scaling Intelligence Lab that asks models to write correct, faster-than-baseline GPU kernels for PyTorch reference workloads.
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/stanford
measures_capability: writing correct, faster-than-baseline GPU kernels from PyTorch reference code
resource: https://scalingintelligence.stanford.edu/KernelBenchLeaderboard/
tags:
  - "open-source"
sources:
  - { id: iml-2026-04-29, resource: https://theinnermostloop.substack.com/p/welcome-to-april-29-2026, title: "Welcome to April 29, 2026", author: human:alex-wissner-gross, last_modified: "2026-04-29" }
---

KernelBench ([arXiv 2502.10517](https://arxiv.org/abs/2502.10517)) scores a model on replacing PyTorch operators with GPU kernels that are both correct and faster than the reference, with a public leaderboard maintained by Stanford's Scaling Intelligence Lab. In this corpus it is the leaderboard that [GPT-5.5](/systems/gpt-5-5.md) xhigh [topped at 6.57%](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md), the item the newsletter reads as a model optimizing the hardware it runs on; a megakernel variant, KernelBench-Mega, appears in the [seventeen-leaders item](/developments/2026-07-03-seventeen-leaders-in-two-years.md) of July.
