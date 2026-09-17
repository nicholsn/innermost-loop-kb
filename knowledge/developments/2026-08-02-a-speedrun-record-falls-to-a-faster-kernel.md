---
type: Development
title: A training speedrun record falls to 75.4 seconds
claim: The NanoGPT speedrun record fell to 75.4 seconds on a faster Triton kernel, while ByteDance's Seedance 2.5 began generating 30-second audio-video in one pass with multi-minute extensions and timestamp-level edits.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-08-02
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/bytedance
  - https://nicholsn.github.io/innermost-loop-kb/organizations/recursive-superintelligence
about:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/nanogpt-speedrun
  - https://nicholsn.github.io/innermost-loop-kb/systems/seedance-2-5
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/optimizing-its-own-invoice
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
score: 75.4 seconds
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-31-a-model-rewrites-its-own-harness-for-eleven-points
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-08-nanogpt-86s
description: The corpus's steadiest gauge of algorithmic progress ticks down again, this time at the kernel layer rather than the architecture, with the newsletter filing it under the machinery tightening beneath lab strategy.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-15-agents-beat-the-human-speedrun-baseline
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-12-nanogpt-106s
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-14-recursive-superintelligence-raises-650m
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-08-02"
  - "speedrun"
  - "kernels"
  - "rsi"
generated: { by: process:iml-emit, at: "2026-08-02T00:00:00Z" }
sources:
  - { id: iml-2026-08-02, resource: https://theinnermostloop.substack.com/p/welcome-to-august-2-2026, title: "Welcome to August 2, 2026", author: human:alex-wissner-gross, last_modified: "2026-08-02", supporting_text: fell to 75.4 seconds }
  - { id: classiclarryd-nanogpt-75-4s-post, resource: https://x.com/classiclarryd/status/2083739041338630372, title: "New NanoGPT Speedrun WR at 75.4s (-0.6s) from @cong_ml and Recursive, with a faster ReLU^2 MLP Triton kernel", author: human:classiclarryd, last_modified: "2026-08-02" }
  - { id: modded-nanogpt-record-table, resource: https://github.com/KellerJordan/modded-nanogpt, title: "Modded-NanoGPT: World record history", author: human:kellerjordan0 }
  - { id: bytedance-seed-seedance-2-5-blog, resource: https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5, title: "One-take Creation, Flexible Referencing: Introducing Seedance 2.5", author: org:bytedance, last_modified: "2026-07-31" }
---

The [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) record fell to 75.4 seconds on a faster ReLU^2 MLP Triton kernel ([post on X](https://x.com/classiclarryd/status/2083739041338630372)), down from [86.8 s](/developments/2026-03-08-nanogpt-86s.md) in March and [127.7 s](/developments/2025-12-21-nanogpt-speedrun-127s.md) when the corpus began tracking it in December. The X post and the speedrun's own [record table](https://github.com/KellerJordan/modded-nanogpt) credit the record to @cong_ml and an AI system called Recursive from [Recursive Superintelligence](/organizations/recursive-superintelligence.md), the lab that [raised $650M in May](/developments/2026-05-14-recursive-superintelligence-raises-650m.md) to have AI experiment on improving itself, so the record carries an AI-system co-author. The gain comes from the kernel layer, where [compiler kernel hacking](/developments/2026-01-12-nanogpt-106s.md) had already set a record in January and where [a model rewrote the production kernels](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) behind OpenAI's price cut three days earlier, and it lands after [agents given idle compute beat the human baseline](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) on the speedrun's optimizer track. In the same item ByteDance's [Seedance 2.5](/systems/seedance-2-5.md) began generating 30-second audio-video in one pass with multi-minute extensions and timestamp-level edits ([ByteDance Seed](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)).
