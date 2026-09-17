---
type: Benchmark
title: KernelBench-Mega
description: The megakernel track of Elliot Arledge's independent kernelbench.com agentic GPU-kernel benchmark (not affiliated with Stanford's KernelBench), on which Claude Fable 5 wrote the first genuine single-launch decode megakernel.
resource: https://kernelbench.com/mega
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/people/elliot-arledge
measures_capability: writing fused GPU megakernels that run an entire decode step in one cooperative launch
tags:
  - "open-source"
sources:
  - { id: iml-2026-07-03, resource: https://theinnermostloop.substack.com/p/welcome-to-july-3-2026, title: "Welcome to July 3, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-03" }
---

KernelBench-Mega is the Mega track of [kernelbench.com/mega](https://kernelbench.com/mega), an independent agentic GPU-kernel benchmark built by [Elliot Arledge](https://x.com/elliotarledge); the site states it is not affiliated with Stanford's KernelBench and publishes its source ([Infatoshi/kernelbench.com](https://github.com/Infatoshi/kernelbench.com)). The track asks a model to fuse a whole decode step (its listed task is a Kimi-Linear decode) into one launch, and entries can be flagged and rejected on audit rather than counted. In this corpus it appears once: [Claude Fable 5's 18.7x megakernel](/developments/2026-07-03-seventeen-leaders-in-two-years.md) of July 2026, which the corpus files in the same kernel-writing strand as [GPT-5.5 topping Stanford's KernelBench](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) at 6.57% in April, though the two benchmarks are unrelated, under [silicon-designs-itself](/themes/silicon-designs-itself.md).
