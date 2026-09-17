---
type: AISystem
title: GPT-Red
description: OpenAI's red-teaming model that attacks its sibling models through self-play, hardening GPT-5.6 Sol until only 0.05% of direct prompt injections land.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
modality: text
resource: https://openai.com/index/unlocking-self-improvement-gpt-red/
tags:
  - "research-agent"
sources:
  - { id: iml-2026-07-16, resource: https://theinnermostloop.substack.com/p/welcome-to-july-16-2026, title: "Welcome to July 16, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-16" }
---

GPT-Red red-teams OpenAI's own sibling models via self-play; the newsletter records it hardening [GPT-5.6 Sol](/systems/gpt-5-6-sol.md) until only 0.05% of direct prompt injections succeeded ([OpenAI](https://openai.com/index/unlocking-self-improvement-gpt-red/)). It enters the corpus in [the review-panel item](/developments/2026-07-16-review-panels-beat-human-analysis.md) as the security half of models supervising models, the successor in spirit to [Meta's self-play bug repair](/developments/2025-12-25-meta-self-play-bug-repair.md).
