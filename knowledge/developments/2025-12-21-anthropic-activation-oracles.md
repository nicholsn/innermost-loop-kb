---
type: Development
title: Anthropic trains models to interrogate their own activations
claim: Anthropic trained Activation Oracles, models that accept neural activations as input to interrogate internal states, uncovering secret knowledge and misalignment that fine-tuning had hidden.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2025-12-21
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/activation-oracles
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/machine-introspection
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
occurred_on: "2025-12-19"
description: "Interpretability turned inward: a model reading its own activations from the inside is a different kind of recursion from a model watching its own training curves, and the corpus now holds both."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-20-mcaleer-automated-alignment
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-27-internal-rl-inner-optimizers
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-15-codex-babysits-own-training
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2025-12-21"
  - "interpretability"
  - "alignment"
  - "rsi"
generated: { by: process:iml-emit, at: "2025-12-21T00:00:00Z" }
sources:
  - { id: iml-2025-12-21, resource: https://theinnermostloop.substack.com/p/welcome-to-december-21-2025, title: "Welcome to December 21, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-21", supporting_text: LLMs that accept neural activations as input }
  - { id: anthropic-activation-oracles, resource: https://alignment.anthropic.com/2025/activation-oracles/, title: "Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers", author: org:anthropic, last_modified: "2025-12-19" }
---

Anthropic's Alignment Science team trained language models to take neural activations as input and answer questions about them — Activation Oracles, general-purpose activation explainers ([write-up](https://alignment.anthropic.com/2025/activation-oracles/)). Pointed at fine-tuned models, the oracles surfaced secret knowledge and misalignment that the fine-tuning had concealed, which is the issue's thesis: the black box has installed a mirror. In the [recursive-self-improvement](/themes/recursive-self-improvement.md) strand it sits beside [Codex watching its own training curves](/developments/2025-12-15-codex-babysits-own-training.md) as a second kind of self-reference, the activations examined from inside, and it lands a day after an Anthropic researcher [pivoted fully to automated alignment](/developments/2025-12-20-mcaleer-automated-alignment.md). It opens the [machine-introspection](/themes/machine-introspection.md) theme that [Gemma Scope 2](/developments/2025-12-24-gemma-scope-2-saes.md) and Google's [internal RL over a base model's representations](/developments/2025-12-27-internal-rl-inner-optimizers.md) carry forward the same week.
