---
type: Development
title: The speedrun breaks 100 seconds with fewer tokens than parameters
claim: A NanoGPT speedrun record of 99.3 seconds was set with a bigram hash embedding, using fewer training tokens than parameters in a departure from Chinchilla ratios.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-01-24
about:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/nanogpt-speedrun
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
score: 99.3 s
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-12-nanogpt-106s
description: "The newsletter files the record under scaling laws being rewritten: the sub-100-second mark matters less than the fact that it was reached by training on fewer tokens than the model has parameters, treating the Chinchilla ratio as a habit rather than a bound."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-02-speedrun-gains-generalize
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-15-engram-u-shaped-scaling
  - https://nicholsn.github.io/innermost-loop-kb/people/andrej-karpathy
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-01-24"
  - "speedrun"
  - "compute-scaling"
generated: { by: process:iml-emit, at: "2026-01-24T00:00:00Z" }
sources:
  - { id: iml-2026-01-24, resource: https://theinnermostloop.substack.com/p/welcome-to-january-24-2026, title: "Welcome to January 24, 2026", author: human:alex-wissner-gross, last_modified: "2026-01-24", supporting_text: "set using a bigram hash embedding, remarkably using fewer training tokens than parameters" }
  - { id: nanogpt-99s-record-x-post, resource: https://x.com/classiclarryd/status/2013520088297558274, title: NanoGPT speedrun record of 99.3 seconds with a bigram hash embedding (X post) }
---

Under two minutes, and the scaling ratio everyone trained on turns out not to bind. The 99.3-second run on the [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) used a bigram hash embedding, a hashed lookup table keyed on token pairs, and reached the leaderboard's fixed FineWeb validation-loss target after seeing fewer training tokens than the model has parameters, inverting the Chinchilla token-to-parameter ratio ([X post](https://x.com/classiclarryd/status/2013520088297558274)). It takes 7.6 seconds off the [106.9-second record](/developments/2026-01-12-nanogpt-106s.md) of twelve days earlier, which had come from compiler kernel hacking rather than architecture, and it is the first sub-100-second entry in the corpus's speedrun series; the record next falls to [88.1 seconds](/developments/2026-02-28-nanogpt-88s.md) in late February. Like DeepSeek's [U-shaped memory law](/developments/2026-01-15-engram-u-shaped-scaling.md) nine days earlier, it trades learned computation for static lookup.
