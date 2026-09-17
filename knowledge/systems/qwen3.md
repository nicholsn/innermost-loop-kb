---
type: AISystem
title: Qwen3
description: Alibaba's 2025 open-weight Qwen3 language-model family, the workload brought up on Redwood in its third week and the model that then found optimizations for its own operations on the chip.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/alibaba
modality: text
resource: https://arxiv.org/abs/2505.09388
tags:
  - "open-weight-model"
sources:
  - { id: iml-feature-ai-chip-designed-by-ai, resource: https://theinnermostloop.substack.com/p/the-first-ai-chip-designed-end-to, title: The First AI Chip Designed End-to-End by AI, author: human:alex-wissner-gross, last_modified: "2026-08-27" }
---

Qwen3 is the 2025 generation of [Alibaba](/organizations/alibaba.md)'s Qwen model family, released with a technical report on arXiv ([paper](https://arxiv.org/abs/2505.09388)); later members of the family in this corpus include [Qwen3-Max-Thinking](/systems/qwen3-max-thinking.md) and [Qwen3.7-Max](/systems/qwen-3-7-max.md). Here it is the workload Architect Labs brought online on [Redwood](/hardware/redwood.md) in the accelerator's third week and demonstrated live at the Design Automation Conference. Exposed as an endpoint inside the AI system that built the chip, it found timing and kernel optimizations for its own operations — the moment the newsletter calls [the loop reaching silicon](/developments/2026-08-27-the-loop-reaches-silicon.md).
