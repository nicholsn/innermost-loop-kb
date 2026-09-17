---
type: Development
title: OpenAI ships a model it says was instrumental in creating itself
claim: OpenAI introduced GPT-5.3-Codex, explicitly describing it as its first model that was instrumental in creating itself, reaching state of the art on SWE-Bench Pro and extending beyond software to spreadsheet analysis.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-06
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-3-codex
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/swe-bench-pro
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/takeoff-declared
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-03-codex-builds-itself
description: "The author's 'officially running in production' moment: a frontier lab puts the recursion into its own launch copy rather than leaving it to be inferred from anecdotes."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-record-falls-in-thirty-minutes
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-15-codex-babysits-own-training
  - https://nicholsn.github.io/innermost-loop-kb/systems/codex
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-28-altman-self-improving-in-production, relation_label: corroborates }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-06"
  - "rsi"
  - "ai-r-and-d"
  - "capability-jump"
generated: { by: process:iml-emit, at: "2026-02-06T00:00:00Z" }
sources:
  - { id: iml-2026-02-06, resource: https://theinnermostloop.substack.com/p/welcome-to-february-6-2026, title: "Welcome to February 6, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-06", supporting_text: model that was instrumental in creating itself }
  - { id: openai-introducing-gpt-5-3-codex, resource: https://openai.com/index/introducing-gpt-5-3-codex/, title: Introducing GPT-5.3-Codex, author: org:openai }
  - { id: boris-power-level-4-glimpses-x, resource: https://x.com/borismpower/status/2019445755019206800, title: "Boris Power on X: glimpses of Level 4 (Innovator-level) intelligence", author: human:boris-power }
---

OpenAI's launch post for [GPT-5.3-Codex](/systems/gpt-5-3-codex.md) calls it the company's first model that was instrumental in creating itself, reports state of the art on [SWE-Bench Pro](/benchmarks/swe-bench-pro.md), and extends the Codex line beyond software into tasks such as spreadsheet analysis ([OpenAI](https://openai.com/index/introducing-gpt-5-3-codex/)); the same model [took the Terminal Bench 2.0 record at 77.3% under thirty minutes after Opus 4.6 set it](/developments/2026-02-06-record-falls-in-thirty-minutes.md), and OpenAI's head of applied research said the lab was seeing glimpses of Level 4, innovator-level intelligence. It closes an arc that began with [Codex babysitting its own training runs](/developments/2025-12-15-codex-babysits-own-training.md) in December and ran through [a Codex manager saying the product builds itself](/developments/2026-02-03-codex-builds-itself.md) three days earlier: the claim moves from anecdote to release note. Two days later [AlphaEvolve's discovery of a new activation function](/developments/2026-02-08-alphaevolve-finds-new-activations.md) carries the [recursive self-improvement](/themes/recursive-self-improvement.md) thread forward.
