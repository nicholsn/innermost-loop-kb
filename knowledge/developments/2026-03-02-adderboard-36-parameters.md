---
type: Development
title: The smallest adder falls from 121 parameters to 36 in a week
claim: The AdderBoard competition for the smallest transformer exceeding 99% accuracy on ten-digit addition reached 36 parameters, down from 121 a week earlier.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-02
about:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/adderboard
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/reasoning-price-deflation
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
score: 121 → 36 parameters
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-25-121-parameter-adder
description: "The author's gauge of capability density: a minimum found a week earlier is already bloat, the parameter floor for a competence falling as fast as the training-time floor beside it."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-28-nanogpt-88s
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-25-qwen-35b-beats-its-own-235b
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-02"
  - "rsi"
  - "evaluation"
generated: { by: process:iml-emit, at: "2026-03-02T00:00:00Z" }
sources:
  - { id: iml-2026-03-02, resource: https://theinnermostloop.substack.com/p/welcome-to-march-2-2026, title: "Welcome to March 2, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-02", supporting_text: "hit 36 parameters, down from 121 a week ago" }
  - { id: adderboard-github, resource: https://github.com/anadim/AdderBoard, title: "AdderBoard: Smallest transformer that can add two 10-digit numbers", author: human:dimitris-papailiopoulos }
---

Last week's breakthrough is this week's bloat. The [AdderBoard](/benchmarks/adderboard.md) leaderboard ranks the smallest transformer that adds two ten-digit numbers at 99%-plus accuracy, and its minimum fell from the [121-parameter entry hand-coded by Codex](/developments/2026-02-25-121-parameter-adder.md) a week earlier to 36 parameters ([repository](https://github.com/anadim/AdderBoard)). The newsletter reads the drop as capability density compressing and files it beside the [NanoGPT speedrun's fall to 88.1 seconds](/developments/2026-02-28-nanogpt-88s.md) two days earlier as evidence that raw intelligence keeps getting cheaper. In the recursive-self-improvement storyline it extends the February result in which a model straight-shot the weights of a successor rather than training them, and the next day's [4B-parameter models matching last generation's 80B](/developments/2026-03-03-qwen-4b-matches-80b.md) carries the same compression story to frontier scale.
