---
type: Development
title: A student distilled from weaker teachers keeps improving anyway
claim: New research shows a strong student distilled from weaker teachers via logit arithmetic keeps improving even when every supervisor is less capable than the pupil.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-07-31
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/students-outgrow-their-teachers
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/a-model-trains-a-model
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-31-a-model-rewrites-its-own-harness-for-eleven-points
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-16-weak-to-strong-supervision
description: "The theoretical floor under the loop: if supervision weaker than the pupil still lifts it, the ceiling of the available teachers stops bounding what a self-improving system can learn."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-05-self-distillation-without-a-teacher
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-10-a-model-post-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-07-31"
  - "distillation"
  - "model-trains-model"
  - "rsi"
generated: { by: process:iml-emit, at: "2026-07-31T00:00:00Z" }
sources:
  - { id: iml-2026-07-31, resource: https://theinnermostloop.substack.com/p/welcome-to-july-31-2026, title: "Welcome to July 31, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-31", supporting_text: a strong student distilled from weaker teachers }
  - { id: arxiv-weak-to-strong-on-policy-distillation, resource: https://arxiv.org/abs/2607.26246, title: Weak-to-Strong On-Policy Distillation, author: human:fangxu-yu, last_modified: "2026-07-28" }
---

Removes the last obvious reason a self-improvement loop must terminate at the quality of its supervision. The paper, *Weak-to-Strong On-Policy Distillation* ([arXiv:2607.26246](https://arxiv.org/abs/2607.26246)), distills a student from several teachers whose logits are combined arithmetically, and the student keeps improving although every teacher is individually weaker than it. It is the research-side counterpart to Anthropic's [weak-to-strong supervision](/developments/2026-04-16-weak-to-strong-supervision.md) result of April, which closed 97% of a capability gap with a weaker overseer, and to Apple's [self-distillation without a teacher](/developments/2026-04-05-self-distillation-without-a-teacher.md); in the production loop it underwrites [Sol post-training Luna](/developments/2026-07-10-a-model-post-trains-a-model.md) and Weco's [seven-version self-rewrite](/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement.md). The newsletter files it the same day as [Kimi K3 rewriting its own harness](/developments/2026-07-31-a-model-rewrites-its-own-harness-for-eleven-points.md), under the heading that the improvement loop is eating its tail.
