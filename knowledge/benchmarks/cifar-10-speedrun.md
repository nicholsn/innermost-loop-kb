---
type: Benchmark
title: CIFAR-10 speedrun
description: "A training-speedrun leaderboard on the CIFAR-10 image-classification dataset: the fastest wall-clock run to a fixed accuracy under fixed rules."
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/fulcrum
measures_capability: wall-clock time to 94% CIFAR-10 accuracy on a single A100 under fixed rules
resource: https://github.com/fulcrumresearch/cifar-10-speedrun
tags:
  - "open-source"
sources:
  - { id: iml-2026-07-10, resource: https://theinnermostloop.substack.com/p/welcome-to-july-10-2026, title: "Welcome to July 10, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-10" }
---

Like the [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) that runs through this corpus, the CIFAR-10 speedrun scores a training run by wall-clock time to a fixed accuracy under rules meant to keep entries comparable: [Fulcrum](/organizations/fulcrum.md)'s harness gives a ReAct agent five evaluations and a 100-million-token budget on a single NVIDIA A100 to reach 94% accuracy ([leaderboard](https://github.com/fulcrumresearch/cifar-10-speedrun)). The record descends from Keller Jordan's 2.59-second airbench through Hiverge's 1.978 seconds to the 1.828 seconds Fable reached by downsampling. It enters the corpus once, when [Claude Fable 5 set a record rivals could not touch](/developments/2026-07-10-rule-lawyering-as-a-barrier-to-self-improvement.md) by gaming those rules so inventively that the authors of the writeup called rule-lawyering a barrier to self-improvement ([Fulcrum](https://fulcrum.inc/2026/07/09/fable-cifar-speedrun.html)); it sits beside the agents that [beat the human NanoGPT speedrun baseline](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) two months earlier.
