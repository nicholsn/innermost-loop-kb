---
type: Benchmark
title: AdderBoard
description: Open leaderboard for the smallest transformer that adds two ten-digit numbers with at least 99% accuracy, tracking trained and hand-coded weights separately.
measures_capability: minimal parameter count for exact ten-digit addition
resource: https://github.com/anadim/AdderBoard
tags:
  - "open-source"
sources:
  - { id: iml-2026-02-25, resource: https://theinnermostloop.substack.com/p/welcome-to-february-25-2026, title: "Welcome to February 25, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-25" }
---

AdderBoard, maintained by Dimitris Papailiopoulos on GitHub, grew out of a prompt that asked Claude Code and Codex for the smallest possible addition transformer and got back 6,080 and 1,644 parameters. It admits only models that add two ten-digit numbers at 99%-plus accuracy (the launch framing was perfect addition), keeps two tables, weights learned from data and weights set analytically, and in this corpus is the leaderboard where a [121-parameter model hand-coded by Codex](/developments/2026-02-25-121-parameter-adder.md) led before [the record fell to 36 parameters a week later](/developments/2026-03-02-adderboard-36-parameters.md). The newsletter reads that drop, beside the [NanoGPT speedrun's fall to 88.1 seconds](/developments/2026-02-28-nanogpt-88s.md) two days earlier, as a gauge of how fast capability density is compressing; the two leaderboards ([NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) and AdderBoard) are the corpus's paired rulers for that compression.
