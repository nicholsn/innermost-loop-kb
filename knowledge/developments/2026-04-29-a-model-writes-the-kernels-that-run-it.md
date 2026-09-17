---
type: Development
title: A model tops the leaderboard for writing the GPU kernels it runs on
claim: GPT-5.5 topped KernelBench at 6.57% for writing GPU kernels, meaning the model is now optimizing the hardware that runs it, while OpenAI's Codex lead declared the product has achieved escape velocity and will keep improving rapidly.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-04-29
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
  - https://nicholsn.github.io/innermost-loop-kb/people/thibault-sottiaux
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-5
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/kernelbench
  - https://nicholsn.github.io/innermost-loop-kb/systems/codex
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/silicon-designs-itself
  - https://nicholsn.github.io/innermost-loop-kb/themes/takeoff-declared
score: 6.57%
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-27-openai-designs-phone-silicon
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-gpt53-codex-creates-itself
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-03-codex-builds-itself
description: The newsletter reads a kernel-writing leaderboard and a lead engineer's 'escape velocity' remark in one breath, as the self-improvement loop baked into the dev cycle and now reaching down into the hardware layer.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-34x-speedup
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-20-cpu-designed-in-twelve-hours
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-10-clark-ai-doing-ai-research
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-03-codex-builds-itself, relation_label: extends }
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-10-clark-ai-doing-ai-research, relation_label: corroborates }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-04-29"
  - "rsi"
  - "kernels"
  - "evaluation"
generated: { by: process:iml-emit, at: "2026-04-29T00:00:00Z" }
sources:
  - { id: iml-2026-04-29, resource: https://theinnermostloop.substack.com/p/welcome-to-april-29-2026, title: "Welcome to April 29, 2026", author: human:alex-wissner-gross, last_modified: "2026-04-29", supporting_text: at 6.57% for writing GPU kernels }
  - { id: brockman-gpt-5-5-kernelbench-x, resource: https://x.com/gdb/status/2048777802586149331, title: "Greg Brockman on X: GPT-5.5 xhigh tops KernelBench", author: human:greg-brockman }
  - { id: sottiaux-codex-escape-velocity-x, resource: https://x.com/thsottiaux/status/2048958572562710550, title: "Thibault Sottiaux on X: Codex has achieved escape velocity", author: human:thibault-sottiaux }
---

[GPT-5.5](/systems/gpt-5-5.md) at its xhigh reasoning setting took the top of [KernelBench](/benchmarks/kernelbench.md) at 6.57%, per [Greg Brockman](https://x.com/gdb/status/2048777802586149331), while OpenAI's Codex engineering lead [Thibault Sottiaux](/people/thibault-sottiaux.md) wrote that [Codex](/systems/codex.md) had achieved escape velocity and would keep improving rapidly ([X](https://x.com/thsottiaux/status/2048958572562710550)). The kernel result is the first kernel-writing leaderboard in the corpus, making concrete the early sign [Jack Clark named in January](/developments/2026-01-10-clark-ai-doing-ai-research.md) and following Opus 4.6's [34x training speedup](/developments/2026-02-06-opus-34x-speedup.md) and the [twelve-hour CPU](/developments/2026-03-20-cpu-designed-in-twelve-hours.md) in the [silicon-designs-itself](/themes/silicon-designs-itself.md) thread. Sottiaux's remark updates his own February line that [Codex builds itself](/developments/2026-02-03-codex-builds-itself.md). The storyline continues with agents [writing AMD kernels](/developments/2026-07-04-agents-write-the-kernels-closing-a-software-gap.md), a model [rewriting the kernels behind an 80% price cut](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) and, in August, [the loop reaching silicon](/developments/2026-08-27-the-loop-reaches-silicon.md).
