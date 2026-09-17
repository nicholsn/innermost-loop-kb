---
type: Development
title: A model runs thirty-five hours without a human
claim: Qwen3.7-Max sustained thirty-five hours of continuous autonomous execution on a kernel optimization task, running 432 kernel evaluations and 1,158 tool calls to reach a tenfold speedup.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-05-22
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/alibaba
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/qwen-3-7-max
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/autonomy-clock-speed
  - https://nicholsn.github.io/innermost-loop-kb/themes/engineer-as-supervisor
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/silicon-designs-itself
score: 35 hours / 1,158 tool calls
occurred_on: "2026-05-21"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-09-a-sixteen-hour-horizon-at-the-edge-of-the-ruler
description: "The autonomy horizon outruns the instruments built to measure it: a production model works unattended for a day and a half on the accelerator kernels that models run on, two weeks after METR's suite topped out at sixteen hours."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-29-a-model-writes-the-kernels-that-run-it
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-07-seventy-two-hours-fifty-experiments
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-34x-speedup
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-05-22"
  - "rsi"
  - "kernels"
  - "autonomous-research"
generated: { by: process:iml-emit, at: "2026-05-22T00:00:00Z" }
sources:
  - { id: iml-2026-05-22, resource: https://theinnermostloop.substack.com/p/welcome-to-may-22-2026, title: "Welcome to May 22, 2026", author: human:alex-wissner-gross, last_modified: "2026-05-22", supporting_text: "ran 35 hours of continuous autonomous execution, performing 432 kernel evaluations across 1,158 tool calls" }
  - { id: alibaba-qwen-x-35-hour-run, resource: https://x.com/Alibaba_Qwen/status/2057450236180935056, title: "Alibaba Qwen on X: Self-Evolving in the Wild — ~35 hours of continuous autonomous execution", author: org:alibaba }
  - { id: qwen-3-7-blog, resource: "https://qwen.ai/blog?id=qwen3.7", title: "Qwen3.7: The Agent Frontier", author: org:alibaba }
---

Alibaba's Qwen team reported that Qwen3.7-Max worked a kernel-optimization task for 35 hours with no human intervention, running 432 kernel evaluations across 1,158 tool calls and finishing with a 10x geometric-mean speedup over the Triton reference ([X post](https://x.com/Alibaba_Qwen/status/2057450236180935056)). The newsletter files it under the line that recursive self-improvement is no longer theoretical: the model is optimizing the accelerator kernels that models run on, here an Extend Attention kernel for Alibaba's own T-Head PPU, hardware the model had not encountered in training, the same loop as [GPT-5.5 topping KernelBench](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) three weeks earlier and [Opus 4.6's 34x training speedup](/developments/2026-02-06-opus-34x-speedup.md) in February. On the autonomy axis it lands two weeks after [METR's suite topped out at sixteen hours](/developments/2026-05-09-a-sixteen-hour-horizon-at-the-edge-of-the-ruler.md) and six weeks after [UNC's seventy-two-hour unattended run](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md); the next code-speedup result in the corpus is the [52x speedup where a skilled human reaches 4x](/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four.md) in June, and the kernel thread itself resumes with [a 232-fold kernel speedup found by an auto-research loop](/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup.md) in August.
