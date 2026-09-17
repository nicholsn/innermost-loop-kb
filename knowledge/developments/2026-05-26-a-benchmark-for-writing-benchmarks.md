---
type: Development
title: A benchmark scores models on writing benchmarks
claim: BenchBench asks whether a model can write a benchmark that other strong models cannot simply clear, with GPT-5.2 currently leading as the top benchmark creator.
domain: benchmarks
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-05-26
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
about:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/benchbench
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-2
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/models-audit-their-benchmarks
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/benchmark-saturation
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-12-the-model-grades-the-graders
description: "Measurement itself joins the recursion: two weeks after models began grading the graders, a benchmark asks them to author the tests, closing the loop between the measured and the measurement."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-12-posttrainbench-v1
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-13-a-model-scores-136-on-an-iq-meta-eval
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-05-26"
  - "evaluation"
  - "rsi"
generated: { by: process:iml-emit, at: "2026-05-26T00:00:00Z" }
sources:
  - { id: iml-2026-05-26, resource: https://theinnermostloop.substack.com/p/welcome-to-may-26-2026, title: "Welcome to May 26, 2026", author: human:alex-wissner-gross, last_modified: "2026-05-26", supporting_text: asks whether a model can write a benchmark that other strong models cannot simply clear }
  - { id: benchbench-github, resource: https://github.com/strangeloopcanon/benchbench, title: BenchBench (GitHub repository) }
---

BenchBench, published on GitHub under the strangeloopcanon account, makes the model the benchmark's author: a creator must supply public solver evidence, private gold, a generator, a verifier, a scorer and an explanation of where solvers will fail, and it wins only if strong solver models cannot clear the package ([repository](https://github.com/strangeloopcanon/benchbench)). At the time of the issue GPT-5.2 led as top benchmark creator; by September 2026 the repository's canonical record listed no validated incumbent, later candidates having been solved nearly outright (25/30 or better), invalidated, or left incomplete. The newsletter files it with [Language Models Need Sleep](/developments/2026-05-26-language-models-need-sleep.md) and [SkillOpt](/developments/2026-05-26-a-skill-document-as-trainable-state.md) as waking hours doing recursive work: sleep, self-test, study, repeat. It follows [GPT-5.5 flagging fatal errors in a third of FrontierMath](/developments/2026-05-12-the-model-grades-the-graders.md) two weeks earlier and sits beside [PostTrainBench v1](/developments/2026-03-12-posttrainbench-v1.md), which measures whether agents can post-train themselves.
