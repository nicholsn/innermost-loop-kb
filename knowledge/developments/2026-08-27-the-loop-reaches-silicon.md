---
type: Development
title: A model running on the chip finds optimizations for its own operations
claim: The model running on Redwood was exposed as an endpoint inside the AI system that built it, and found timing and kernel optimizations for its own operations — extending to silicon the intelligence explosion I. J. Good imagined for software in 1965.
domain: compute
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/feature-ai-chip-designed-by-ai
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/architect-labs
  - https://nicholsn.github.io/innermost-loop-kb/organizations/alibaba
about:
  - https://nicholsn.github.io/innermost-loop-kb/hardware/redwood
  - https://nicholsn.github.io/innermost-loop-kb/systems/qwen3
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/silicon-designs-itself
  - https://nicholsn.github.io/innermost-loop-kb/themes/the-designless-industry
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-27-a-first-of-authorship-not-assistance
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-29-a-model-writes-the-kernels-that-run-it
description: The designer of the chip and the workload running on it become the same optimizing system, so the recursion the corpus has tracked through code, kernels and training loops closes for the first time through the hardware substrate itself.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/people/i-j-good
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-20-cpu-designed-in-twelve-hours
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-08-27"
  - "rsi"
  - "chip-design"
  - "kernels"
generated: { by: process:iml-emit, at: "2026-08-27T00:00:00Z" }
sources:
  - { id: iml-feature-ai-chip-designed-by-ai, resource: https://theinnermostloop.substack.com/p/the-first-ai-chip-designed-end-to, title: The First AI Chip Designed End-to-End by AI, author: human:alex-wissner-gross, last_modified: "2026-08-27", supporting_text: the model found timing and kernel optimizations for its own operations }
  - { id: architect-labs-site, resource: https://architectlabs.com/, title: Architect Labs, author: org:architect-labs }
---

Once [Redwood](/hardware/redwood.md) was serving [Qwen3](/systems/qwen3.md) inference on its FPGA, [Architect Labs](/organizations/architect-labs.md) exposed the model as an endpoint inside the same AI system that had generated the chip's RTL, verification and kernels, and the model returned timing and kernel optimizations for its own operations ([company site](https://architectlabs.com/)). The newsletter reads this against [I. J. Good](/people/i-j-good.md)'s 1965 intelligence explosion — a machine designing better machines — noting that Good was thinking of software and that the loop now reaches silicon. It is the hardware endpoint of a kernel storyline that runs from [a model topping KernelBench for the GPU kernels it runs on](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) through [kernels rewritten behind an 80% price cut](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) and [a 232-fold kernel speedup](/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup.md), and it follows the same issue's [first-of-authorship](/developments/2026-08-27-a-first-of-authorship-not-assistance.md) result; the daily issue two days later [records the announcement](/developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai.md). The figures are company-reported, the silicon numbers are FPGA-calibrated projections, and the author discloses that he advises the company.
