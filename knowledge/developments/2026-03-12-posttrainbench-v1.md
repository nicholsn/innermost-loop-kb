---
type: Development
title: A benchmark measures whether agents can post-train themselves
claim: PostTrainBench v1.0 evaluated whether language model agents can automate their own post-training for recursive self-improvement, finding Claude Opus 4.6 with Claude Code the most capable such agent.
domain: benchmarks
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-12
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/posttrainbench
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-opus-4-6
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-code
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/benchmark-saturation
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-18-posttrainbench-models-training-models
description: The December leaderboard for models post-training models returns with a version number and a new leader, giving the recursion the newsletter is named for a score to track.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-10-a-model-post-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-28-altman-self-improving-in-production
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-12"
  - "evaluation"
  - "model-trains-model"
  - "rsi"
generated: { by: process:iml-emit, at: "2026-03-12T00:00:00Z" }
sources:
  - { id: iml-2026-03-12, resource: https://theinnermostloop.substack.com/p/welcome-to-march-12-2026, title: "Welcome to March 12, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-12", supporting_text: evaluated whether LLM agents can automate their own post-training for recursive self-improvement }
  - { id: posttrainbench-v1-announcement, resource: https://x.com/maksym_andr/status/2031792006884659705, title: PostTrainBench v1.0 announcement, author: human:maksym-andriushchenko }
---

[PostTrainBench](/benchmarks/posttrainbench.md) v1.0 asks whether an LLM agent can carry out the post-training of another model unaided, and in its first versioned release [Claude Opus 4.6](/systems/claude-opus-4-6.md) driving [Claude Code](/systems/claude-code.md) came out as the most capable such agent ([announcement](https://x.com/maksym_andr/status/2031792006884659705)). The leaderboard first appeared in December with [GPT 5.1 Codex Max on top](/developments/2025-12-18-posttrainbench-models-training-models.md); the version number and the change of leader are what the newsletter marks. Four days later Anthropic's alignment lead would call recursive self-improvement [a present phenomenon](/developments/2026-03-16-rsi-is-a-present-phenomenon.md), and in July a model [post-trains a model at 50.3%](/developments/2026-07-10-a-model-post-trains-a-model.md) on this benchmark.
