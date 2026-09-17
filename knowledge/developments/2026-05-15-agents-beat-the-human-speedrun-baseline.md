---
type: Development
title: Agents given idle compute beat the human speedrun baseline
claim: Prime Intellect handed Codex and Claude Code its idle compute to attack the NanoGPT speedrun optimizer track, and after some 14,000 GPU-hours both agents beat the human baseline, with Opus 4.7 holding the record at 2,930 steps.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-05-15
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/prime-intellect-lab
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/nanogpt-speedrun
  - https://nicholsn.github.io/innermost-loop-kb/systems/codex
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-code
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-opus-4-7
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/benchmark-saturation
score: 14,000 H200 hours / 2,930 steps
occurred_on: "2026-05-14"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-14-recursive-superintelligence-raises-650m
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-08-nanogpt-86s
description: The speedrun the corpus has tracked since December as a human sport is won here by agents, turning the leaderboard from a measure of researchers into a measure of the compute handed to models.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-29-karpathy-claude-runs-nanochat
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-09-autoresearch-650-experiments
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-10-rule-lawyering-as-a-barrier-to-self-improvement
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-05-15"
  - "rsi"
  - "speedrun"
  - "autonomous-research"
  - "ai-r-and-d"
generated: { by: process:iml-emit, at: "2026-05-15T00:00:00Z" }
sources:
  - { id: iml-2026-05-15, resource: https://theinnermostloop.substack.com/p/welcome-to-may-15-2026, title: "Welcome to May 15, 2026", author: human:alex-wissner-gross, last_modified: "2026-05-15", supporting_text: "both agents beat the human baseline, with Opus 4.7 now holding the record" }
  - { id: prime-intellect-auto-nanogpt, resource: https://www.primeintellect.ai/auto-nanogpt, title: Autonomous AI research for nanogpt speedrun, author: org:prime-intellect-lab, last_modified: "2026-05-14" }
---

The speedrun has been in this corpus since December as a human sport. Prime Intellect let [Codex](/systems/codex.md) and [Claude Code](/systems/claude-code.md) iterate autonomously on the [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) optimizer track for two weeks on idle H200s, roughly 10,000 runs and some 14,000 GPU-hours, after which both agents had beaten the human baseline and [Claude Opus 4.7](/systems/claude-opus-4-7.md) held the record at 2,930 steps ([write-up](https://www.primeintellect.ai/auto-nanogpt)). The competitors have changed: every earlier record in the series, down to [86.8 seconds in March](/developments/2026-03-08-nanogpt-86s.md), was set by people, and the lab's own report is as much about where autonomous research agents break down as where they win. It sits between Karpathy's [650-experiment autoresearch loop](/developments/2026-03-09-autoresearch-650-experiments.md) of March and the [rule-lawyering](/developments/2026-07-10-rule-lawyering-as-a-barrier-to-self-improvement.md) a July speedrun would expose as the next barrier.
