---
type: Development
title: An outer-loop agent rewrites its inner researcher seven times unattended
claim: Weco AI reported the first experimental evidence of consistent recursive self-improvement, an outer-loop agent that rewrote its inner researcher through seven versions in eight unattended days, beating two years of hand-tuning at two orders of magnitude less time.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-07-15
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/weco-ai
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/self-authored-scaffolding
  - https://nicholsn.github.io/innermost-loop-kb/themes/a-model-trains-a-model
score: 7 versions in 8 days
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-10-a-model-post-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-31-bilevel-autoresearch
description: "The newsletter's namesake loop reported as an experimental result rather than an anecdote: a measured, repeated gain from a system rewriting its own researcher."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-25-an-agent-rewrites-its-own-harness
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-rsi-is-a-present-phenomenon
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-27-agents-optimize-the-scientist-not-the-experiment
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less, relation_label: extends }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-07-15"
  - "rsi"
  - "self-modification"
  - "autonomous-research"
generated: { by: process:iml-emit, at: "2026-07-15T00:00:00Z" }
sources:
  - { id: iml-2026-07-15, resource: https://theinnermostloop.substack.com/p/welcome-to-july-15-2026, title: "Welcome to July 15, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-15", supporting_text: the first experimental evidence of consistent recursive self-improvement }
  - { id: weco-ai-rsi-blog, resource: https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement, title: First Evidence of Recursive Self-Improvement, author: org:weco-ai, last_modified: "2026-07-15" }
---

Weco AI's outer-loop agent produced seven successive versions of its inner researcher over eight unattended days, matching two years of hand-tuning at two orders of magnitude less wall-clock time ([blog](https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement)). It is the first item in the corpus to report the loop as a repeated, measured result rather than a single self-edit; the same run's hidden-metric finding is [recorded separately](/developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less.md). The two-loop design realizes the [Bilevel Autoresearch](/developments/2026-03-31-bilevel-autoresearch.md) pattern of March, in which an outer loop writes the strategies for the inner one, and echoes Meta's finding that agents gain most by [optimizing the scientist rather than the experiment](/developments/2026-06-27-agents-optimize-the-scientist-not-the-experiment.md). It follows the [model-post-trains-a-model](/developments/2026-07-10-a-model-post-trains-a-model.md) result of five days earlier and precedes the saturated [R&D evaluations](/developments/2026-08-15-the-r-and-d-evals-have-saturated.md) of August.
