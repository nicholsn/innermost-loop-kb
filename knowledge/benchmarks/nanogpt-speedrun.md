---
type: Benchmark
title: NanoGPT speedrun
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/people/keller-jordan
description: "Keller Jordan's modded-nanogpt speedrun: the wall-clock time to train a GPT-2-class model to a fixed validation loss on FineWeb on one 8xH100 node, whose falling record the corpus tracks as the cost of the training loop itself."
resource: https://github.com/KellerJordan/modded-nanogpt
measures_capability: wall-clock time to train a GPT-2-class model to a fixed validation loss on 8 H100s
tags:
  - "open-source"
sources:
  - { id: iml-2025-12-25, resource: https://theinnermostloop.substack.com/p/welcome-to-december-25-2025, title: "Welcome to December 25, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-25" }
---

The NanoGPT speedrun is an open leaderboard built on Andrej Karpathy's nanoGPT: competitors change the architecture, optimizer and kernels to reach a fixed validation loss on FineWeb as fast as possible on a single 8xH100 node, and every record is a public pull request. The corpus follows it from [127.7 seconds](/developments/2025-12-21-nanogpt-speedrun-127s.md) through [122.2](/developments/2025-12-25-nanogpt-122s.md), [119.3](/developments/2025-12-26-nanogpt-119s.md) and [116.4 seconds](/developments/2025-12-27-nanogpt-116s.md) in one week, then to [under 100 seconds](/developments/2026-01-24-nanogpt-99s-bigram-hash.md) in January and [75.4 seconds](/developments/2026-08-02-a-speedrun-record-falls-to-a-faster-kernel.md) in August; by May, agents given idle compute [beat the human baseline](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) on its optimizer track, which is why it belongs to the [recursive-self-improvement](/themes/recursive-self-improvement.md) strand.
