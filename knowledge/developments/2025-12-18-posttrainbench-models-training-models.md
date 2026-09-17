---
type: Development
title: PostTrainBench ranks models at post-training other models
claim: The new PostTrainBench showed GPT 5.1 Codex Max leading at the recursive task of post-training other models.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2025-12-18
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
  - https://nicholsn.github.io/innermost-loop-kb/organizations/tubingen-ai-center
about:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/posttrainbench
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-1-codex-max
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/a-model-trains-a-model
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-15-codex-babysits-own-training
description: "The author's Darwinian training loop acquires a scoreboard: once agents are ranked on how well they train other models, the recursion becomes a measured competition rather than an anecdote."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-10-a-model-post-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/systems/codex
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2025-12-18"
  - "model-trains-model"
  - "evaluation"
  - "rsi"
generated: { by: process:iml-emit, at: "2025-12-18T00:00:00Z" }
sources:
  - { id: iml-2025-12-18, resource: https://theinnermostloop.substack.com/p/welcome-to-december-18-2025, title: "Welcome to December 18, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-18", supporting_text: PostTrainBench shows GPT 5.1 Codex Max reigning supreme }
  - { id: posttrainbench-leaderboard, resource: https://posttrainbench.com/, title: "PostTrainBench: Measuring how well AI agents can post-train language models", author: org:tubingen-ai-center }
---

Three days after a model was reported watching its own training, there is a leaderboard for models training models. PostTrainBench hands each coding agent four small base models, a single H100 and ten hours to post-train them, and in this first cut OpenAI's [GPT-5.1-Codex-Max](/systems/gpt-5-1-codex-max.md), the same [Codex](/systems/codex.md) line that had just been reported [supervising its own training](/developments/2025-12-15-codex-babysits-own-training.md), led the field ([leaderboard](https://posttrainbench.com/)). The benchmark becomes the corpus's ruler for the loop: ten days later Altman [confirms self-improving systems in production](/developments/2025-12-28-altman-self-improving-in-production.md), [v1.0](/developments/2026-03-12-posttrainbench-v1.md) in March 2026 asks outright whether agents can automate their own post-training, and by July OpenAI reports [Sol post-training Luna](/developments/2026-07-10-a-model-post-trains-a-model.md) at 50.3% on it.
