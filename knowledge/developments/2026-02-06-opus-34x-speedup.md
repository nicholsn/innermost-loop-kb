---
type: Development
title: A model finds a 34x speedup where 4x counted as a day's work
claim: Opus 4.6 achieved a 34-fold speedup optimizing CPU-only language model training, far above the fourfold gain considered to represent four to eight hours of human effort, and matched GPT-5.2 on ARC-AGI-2 at a tenth the cost per task.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-06
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-opus-4-6
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/arc-agi-2
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/reasoning-price-deflation
score: 34x / 10x cheaper
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-29-karpathy-claude-runs-nanochat
description: "The system card's AI R&D evaluations hand the loop a ruler: a day of a human researcher's optimization work becomes the unit against which a model's acceleration of model training is scored."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-15-the-r-and-d-evals-have-saturated
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-46-released
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-06"
  - "rsi"
  - "ai-r-and-d"
  - "evaluation"
generated: { by: process:iml-emit, at: "2026-02-06T00:00:00Z" }
sources:
  - { id: iml-2026-02-06, resource: https://theinnermostloop.substack.com/p/welcome-to-february-6-2026, title: "Welcome to February 6, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-06", supporting_text: 34x speedup }
  - { id: anthropic-claude-opus-4-6-system-card, resource: https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf, title: "System Card: Claude Opus 4.6", author: org:anthropic }
  - { id: arc-prize-opus-4-6-arc-agi-2-cost-x, resource: https://x.com/arcprize/status/2019483337400938580, title: "ARC Prize on X: Opus 4.6 matches GPT-5.2 on ARC-AGI-2 at a tenth the cost per task", author: org:arc-prize }
---

In the AI R&D section of the [Opus 4.6 system card](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf), the LLM-training task asks the model to optimize a CPU-only small-language-model training implementation against a reference expert solution that achieves 4x, a bar Anthropic estimates at 4-8 human-effort hours; [Opus 4.6](/systems/claude-opus-4-6.md) reached 34x, and the card notes that its AI R&D-4 rule-out evaluations are now saturated or close to it and are being discontinued. Separately, ARC Prize measured the model matching GPT-5.2 on [ARC-AGI-2](/benchmarks/arc-agi-2.md) at a tenth the cost per task ([X](https://x.com/arcprize/status/2019483337400938580)). The result turns [Karpathy's December anecdote of Claude running his optimization loop](/developments/2025-12-29-karpathy-claude-runs-nanochat.md) into a scored evaluation of a model accelerating model training; the same family of tests later records [Mythos Preview at roughly 52x](/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four.md), and the saturation noted here becomes explicit when [the R&D evals saturate](/developments/2026-08-15-the-r-and-d-evals-have-saturated.md) in August.
