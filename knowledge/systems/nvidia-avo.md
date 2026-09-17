---
type: AISystem
title: NVIDIA AVO
description: Nvidia's general-purpose agent architecture for long-horizon autonomy, which lifted Claude Opus 5 to a perfect score on ARC-AGI-3 and evolved GPU kernels past FlashAttention-4.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/nvidia
modality: research agent
evaluated_on:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/arc-agi-3
resource: https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/
tags:
  - "research-agent"
sources:
  - { id: iml-2026-08-23, resource: https://theinnermostloop.substack.com/p/welcome-to-august-23-2026, title: "Welcome to August 23, 2026", author: human:alex-wissner-gross, last_modified: "2026-08-23" }
---

AVO is Nvidia's agent architecture for long-horizon autonomy, presented as a research project rather than a product. Its first reported week went to evolving GPU kernels on DGX B200 systems, exploring more than 500 directions to beat cuDNN by up to 3.5% and FlashAttention-4 by up to 10.5%; transferred unchanged to ARC-AGI-3 with [Claude Opus 5](/systems/claude-opus-5.md) inside, it [swept all 183 levels](/developments/2026-08-23-a-perfect-score-on-all-one-hundred-eighty-three-levels.md) from a 30% model baseline. In this corpus it is the clearest case of the [harness generalizing](/themes/harness-as-generalizer.md) while the weights stay fixed.
