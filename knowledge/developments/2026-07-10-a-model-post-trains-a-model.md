---
type: Development
title: A model autonomously post-trains another model
claim: OpenAI said Sol autonomously post-trained Luna, once a senior team's job, calling an automated researcher pretty close and years early, with Sol at 50.3% on PostTrainBench, Terra at 51.5% and experiment throughput doubled this year.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-07-10
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-6
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-6-sol
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-6-luna
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-6-terra
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/posttrainbench
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/a-model-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/authoring-minds
score: 50.3% / 51.5% PostTrainBench
occurred_on: "2026-07-09"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-09-a-model-a-month-through-pipelining
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-22-openai-targets-a-research-intern-by-september
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-12-posttrainbench-v1
description: The post-training step that once took a senior team is done by a sibling model, and the lab's own caveat, that compute has not yet flooded to AI-run research, becomes the corpus's test for whether the loop is real.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-05-when-ai-builds-itself
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-09-a-personal-agi-for-every-human
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-15-codex-babysits-own-training
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-07-10"
  - "rsi"
  - "model-trains-model"
  - "ai-r-and-d"
  - "autonomous-research"
generated: { by: process:iml-emit, at: "2026-07-10T00:00:00Z" }
sources:
  - { id: iml-2026-07-10, resource: https://theinnermostloop.substack.com/p/welcome-to-july-10-2026, title: "Welcome to July 10, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-10", supporting_text: Sol autonomously post-trained Luna }
  - { id: sol-post-trained-luna-report, resource: https://x.com/deredleritt3r/status/2075314461401911364, title: OpenAI says Sol autonomously post-trained Luna }
  - { id: posttrainbench-gpt-5-6-scores, resource: https://x.com/maksym_andr/status/2075276389448872089, title: GPT-5.6 Sol at 50.3% on PostTrainBench }
  - { id: openai-experiment-throughput-doubled, resource: https://x.com/scaling01/status/2075269455781703850, title: OpenAI experiment throughput has doubled this year }
  - { id: the-information-noam-brown-prefers-5-6-to-intern, resource: https://www.theinformation.com/newsletters/ai-agenda/openai-researcher-says-gpt-5-6-better-ai-research-human-interns, title: OpenAI researcher says GPT-5.6 is better at AI research than human interns, author: org:the-information }
---

OpenAI reported that [GPT-5.6](/systems/gpt-5-6.md) [Sol](/systems/gpt-5-6-sol.md) post-trained its sibling [Luna](/systems/gpt-5-6-luna.md) without human direction, the step where a senior team shapes a model into a product, and called an automated researcher pretty close, years ahead of its own schedule ([report](https://x.com/deredleritt3r/status/2075314461401911364)). Sol scored 50.3% on [PostTrainBench](/benchmarks/posttrainbench.md) with [Terra](/systems/gpt-5-6-terra.md) nosing past at 51.5% ([scores](https://x.com/maksym_andr/status/2075276389448872089)), the lab's experiment throughput has doubled this year ([throughput](https://x.com/scaling01/status/2075269455781703850)), and Noam Brown said he prefers 5.6 to a human intern ([The Information](https://www.theinformation.com/newsletters/ai-agenda/openai-researcher-says-gpt-5-6-better-ai-research-human-interns)). It lands four months after PostTrainBench v1.0 [first measured whether agents can post-train themselves](/developments/2026-03-12-posttrainbench-v1.md) and three after OpenAI [set a September target for an automated research intern](/developments/2026-03-22-openai-targets-a-research-intern-by-september.md); five days later Weco reports [the first evidence of consistent recursive self-improvement](/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement.md). The lab's own stated test of whether the loop is real — chips flooding to AI-run research — has not yet happened.
