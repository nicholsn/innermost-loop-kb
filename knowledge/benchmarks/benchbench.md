---
type: Benchmark
title: BenchBench
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/strange-loop-canon
description: A benchmark that scores a model on whether it can author a benchmark package that strong solver models cannot simply clear.
resource: https://github.com/strangeloopcanon/benchbench
measures_capability: a model's ability to write benchmarks that other frontier models cannot clear
tags:
  - "open-source"
sources:
  - { id: iml-2026-05-26, resource: https://theinnermostloop.substack.com/p/welcome-to-may-26-2026, title: "Welcome to May 26, 2026", author: human:alex-wissner-gross, last_modified: "2026-05-26" }
---

BenchBench inverts the usual arrangement: the model under test is the benchmark's author, supplying public solver evidence, private gold answers, a generator, a verifier, a scorer and an account of likely failures, and it wins only if a panel of strong solvers cannot clear the package. It enters this corpus through the [May 26 item](/developments/2026-05-26-a-benchmark-for-writing-benchmarks.md), where GPT-5.2 led as top creator, and sits beside [PostTrainBench](/benchmarks/posttrainbench.md) as a benchmark built around models doing the measurement work themselves.
