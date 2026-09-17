---
type: AISystem
title: AIRA2
description: Meta's second-generation AI research agent, which attacks three structural bottlenecks in research agents with an asynchronous multi-GPU worker pool, a hidden consistent evaluation protocol and interactively debugging ReAct agents.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/meta
modality: research agent
resource: https://arxiv.org/abs/2603.26499
tags:
  - "research-agent"
sources:
  - { id: iml-2026-03-31, resource: https://theinnermostloop.substack.com/p/welcome-to-march-31-2026, title: "Welcome to March 31, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-31" }
---

AIRA2 ([arXiv](https://arxiv.org/abs/2603.26499)) is Meta's follow-on research agent, built around fixes for three bottlenecks the field had identified: synchronous single-GPU execution, a generalization gap in which validation-based selection overfits over long search horizons, and the ceiling imposed by fixed single-turn operators. It reports an 81.5% mean percentile rank on MLE-bench-30 at 24 hours (83.1% at 72) against a 72.7% baseline, exceeds human state of the art on 6 of 20 AIRS-Bench tasks, and its ablations attribute earlier reports of overfitting to evaluation noise. In this corpus it shares [the March 31 development](/developments/2026-03-31-bilevel-autoresearch.md) with Bilevel Autoresearch and follows Meta's [hyperagents](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md) of the previous week.
