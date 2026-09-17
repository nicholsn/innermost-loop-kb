---
type: AISystem
title: Activation Oracles
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
modality: text
description: Anthropic language models fine-tuned to take a target model's (including their own) neural activations as input and explain them in natural language, surfacing knowledge and misalignment that fine-tuning had hidden.
resource: https://alignment.anthropic.com/2025/activation-oracles/
tags:
  - "open-source"
sources:
  - { id: iml-2025-12-21, resource: https://theinnermostloop.substack.com/p/welcome-to-december-21-2025, title: "Welcome to December 21, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-21" }
---

Models that accept neural activations as input to interrogate internal states, surfacing secret knowledge and hidden misalignment. Activation Oracles are LLMs trained to take activations from a target model and answer questions about them in plain language — general-purpose activation explainers, in the words of the [Anthropic Alignment Science write-up](https://alignment.anthropic.com/2025/activation-oracles/). Pointed at fine-tuned models they surfaced secret knowledge and misalignment the fine-tuning had tried to hide, which is why the newsletter calls the result a machine psychoanalyzing its own weights. They open the [machine-introspection](/themes/machine-introspection.md) theme through the [development reported on 21 December](/developments/2025-12-21-anthropic-activation-oracles.md); DeepMind's [Gemma Scope 2](/developments/2025-12-24-gemma-scope-2-saes.md) three days later is the corpus's next attempt to open the black box.
