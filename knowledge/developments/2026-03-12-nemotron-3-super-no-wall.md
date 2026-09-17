---
type: Development
title: Nvidia sees no wall in post-training and opens a 120B model
claim: Nvidia said it sees no wall in post-training and announced Nemotron 3 Super, a 120-billion-parameter hybrid model with 12 billion active parameters, released with permissive licensing, open data and open training infrastructure.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-12
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/nvidia
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/nemotron-3-super
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/open-weight-latency
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
score: 120B / 12B active
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-08-nanogpt-86s
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-16-nvidia-opensources-nemotron-3
description: Nvidia's no-wall reading of post-training, delivered with a fully open release, is the supply-side counterpart to a benchmark measuring whether agents can run that post-training themselves.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/systems/nemotron-3
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-12-reasoning-1000x-cheaper-in-16-months
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-12-posttrainbench-v1, relation_label: corroborates }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-12"
  - "open-weights"
  - "compute-scaling"
generated: { by: process:iml-emit, at: "2026-03-12T00:00:00Z" }
sources:
  - { id: iml-2026-03-12, resource: https://theinnermostloop.substack.com/p/welcome-to-march-12-2026, title: "Welcome to March 12, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-12", supporting_text: "announced Nemotron 3 Super, a 120B-parameter hybrid SSM Latent MoE with 12B active parameters" }
  - { id: nvidia-no-wall-in-post-training-nemotron-3-super, resource: https://x.com/kuchaev/status/2031765543007736068, title: "No wall in post-training: Nemotron 3 Super announced" }
---

Nvidia's announcement framed [Nemotron 3 Super](/systems/nemotron-3-super.md) — 120B total parameters, 12B active, a hybrid SSM latent-MoE design built for Blackwell — around the claim that it sees no wall in post-training as scaling RL keeps paying off ([post](https://x.com/kuchaev/status/2031765543007736068)). The release extends the [Nemotron 3 family](/systems/nemotron-3.md) that Nvidia [open-sourced in December](/developments/2025-12-16-nvidia-opensources-nemotron-3.md) with weights, data and training infrastructure rather than weights alone. In the trajectory it is the supply-side companion to the same issue's [PostTrainBench v1.0](/developments/2026-03-12-posttrainbench-v1.md): one says post-training has room to run, the other measures whether agents can run it themselves, and Altman's [thousandfold cost drop](/developments/2026-03-12-reasoning-1000x-cheaper-in-16-months.md) in the same paragraph is the price curve underneath both.
