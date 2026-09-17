---
type: Development
title: A 121-parameter adder is hand-coded rather than trained
claim: The AdderBoard competition to find the smallest transformer that perfectly adds ten-digit numbers is led by a 121-parameter model whose weights were hand-coded by Codex rather than trained.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-25
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/codex
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/adderboard
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
score: 121 parameters
description: "The author's framing: recursive self-improvement can now straight-shot the weights of a perfect successor model, writing them analytically instead of finding them by gradient descent."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-gpt53-codex-creates-itself
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-08-alphaevolve-finds-new-activations
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-02-adderboard-36-parameters
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-25"
  - "rsi"
  - "model-trains-model"
  - "evaluation"
generated: { by: process:iml-emit, at: "2026-02-25T00:00:00Z" }
sources:
  - { id: iml-2026-02-25, resource: https://theinnermostloop.substack.com/p/welcome-to-february-25-2026, title: "Welcome to February 25, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-25", supporting_text: "121 parameters hand-coded by Codex, not trained" }
  - { id: adderboard-github, resource: https://github.com/anadim/AdderBoard, title: "AdderBoard: Smallest transformer that can add two 10-digit numbers" }
---

Recursive self-improvement writing successor weights directly rather than searching for them. [AdderBoard](/benchmarks/adderboard.md) asks for the smallest transformer that adds two ten-digit numbers at 99% or better on a held-out test set; when the newsletter picked it up, the hand-coded table was led by a 121-parameter single-layer Qwen3-style decoder whose weights were set analytically by [Codex](/systems/codex.md), using tied embeddings, RoPE digit routing and a carry computed through the final norm ([leaderboard](https://github.com/anadim/AdderBoard)). It is the constructive counterpart to [AlphaEvolve's search for activation functions](/developments/2026-02-08-alphaevolve-finds-new-activations.md) and a step past [Codex being instrumental in creating its own successor](/developments/2026-02-06-gpt53-codex-creates-itself.md). The record did not last: [36 parameters a week later](/developments/2026-03-02-adderboard-36-parameters.md).
