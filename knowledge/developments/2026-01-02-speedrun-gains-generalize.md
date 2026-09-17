---
type: Development
title: Speedrun gains transfer to the harder track and break it by 25%
claim: Six months of NanoGPT speedrun optimizations found on the 3.28 loss track were shown to generalize to the harder 2.92 track, breaking that world record by 25%.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-01-02
about:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/nanogpt-speedrun
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/generalism-beats-specialism
score: -25% on the 2.92 track
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-30-nanogpt-115s
description: "The newsletter's 'free compute in the geometry of the model': a leaderboard chase turns into evidence that its accumulated tricks were general improvements to training rather than overfitting to one target."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-21-nanogpt-speedrun-127s
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-29-karpathy-claude-runs-nanochat
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-15-agents-beat-the-human-speedrun-baseline
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-01-02"
  - "speedrun"
  - "ai-r-and-d"
generated: { by: process:iml-emit, at: "2026-01-02T00:00:00Z" }
sources:
  - { id: iml-2026-01-02, resource: https://theinnermostloop.substack.com/p/welcome-to-january-2-2026, title: "Welcome to January 2, 2026", author: human:alex-wissner-gross, last_modified: "2026-01-02", supporting_text: have now been found to generalize to the harder 2.92 loss track }
  - { id: classiclarryd-x-speedrun-2-92-track, resource: https://x.com/classiclarryd/status/2005659526960492638, title: New NanoGPT Speedrun WR at 115.1 (-1.3s), author: human:classiclarryd, last_modified: "2025-12-29" }
---

The chain stops being a leaderboard and becomes evidence that the optimizations were general. The [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md)'s main track asks for 3.28 FineWeb validation loss on 8xH100, and six months of work had pushed that under two minutes, most recently to [115.1 seconds](/developments/2025-12-30-nanogpt-115s.md); applied to the GPT-2-medium track, which targets 2.92 loss, the same advances cut that record by a quarter ([X](https://x.com/classiclarryd/status/2005659526960492638)). The newsletter links the same record-holder's post as the 115.1-second result, whose top-level text describes the 3.28-track gain; the 2.92-track transfer is the newsletter's report of it. The result reframes the whole chain from [127.7 seconds](/developments/2025-12-21-nanogpt-speedrun-127s.md) onward as accumulating transferable training knowledge, which is what later makes [handing the speedrun to agents](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) a test of automated research rather than of tuning; the main-track record falls again to [113.7 seconds](/developments/2026-01-05-nanogpt-113s.md) three days later.
