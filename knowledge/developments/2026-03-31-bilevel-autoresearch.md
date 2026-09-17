---
type: Development
title: A research loop writes the strategies for its own outer loop
claim: Bilevel Autoresearch wraps an inner research loop inside an outer one that generates new search strategies as Python code at runtime, with both loops powered by the same model and no stronger model required, while Meta's AIRA2 cracked three structural bottlenecks in research agents.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-31
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/meta
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/bilevel-autoresearch
  - https://nicholsn.github.io/innermost-loop-kb/systems/aira2
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/scaffolding-over-weights
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-29-autonomous-zero-day-on-stage
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-24-hyperagents-edit-their-own-mechanism
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-09-autoresearch-650-experiments
description: The outer loop that a human used to be, reading the inner loop's code, finding its bottleneck and writing the fix, is handed to the same model, so the recursion no longer needs a smarter supervisor.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-31-harnesses-become-editable-artifacts
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-12-alma-agents-design-their-own-memory
  - https://nicholsn.github.io/innermost-loop-kb/people/andrej-karpathy
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-31"
  - "rsi"
  - "autonomous-research"
  - "self-modification"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-03-31T00:00:00Z" }
sources:
  - { id: iml-2026-03-31, resource: https://theinnermostloop.substack.com/p/welcome-to-march-31-2026, title: "Welcome to March 31, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-31", supporting_text: generates new search strategies as Python code at runtime }
  - { id: bilevel-autoresearch-arxiv, resource: https://arxiv.org/abs/2603.23420, title: "Bilevel Autoresearch: Meta-Autoresearching Itself", author: human:yaonan-qu, last_modified: "2026-03-24" }
  - { id: aira2-arxiv, resource: https://arxiv.org/abs/2603.26499, title: "AIRA2: Overcoming Bottlenecks in AI Research Agents", author: org:meta, last_modified: "2026-03-27" }
---

The recursion stops needing a smarter supervisor. [Bilevel Autoresearch](/systems/bilevel-autoresearch.md) (Qu and Lu, [arXiv](https://arxiv.org/abs/2603.23420)) nests two loops: the inner one is the hyperparameter-search loop Karpathy popularized as autoresearch, and the outer one reads the inner loop's code and traces, identifies bottlenecks and injects new Python search mechanisms at runtime; on Karpathy's GPT pretraining benchmark the outer loop reports a 5x improvement over the inner loop alone (-0.045 vs -0.009 val_bpb), instantiating mechanisms from bandits, combinatorial optimization and design of experiments that no human specified. Both loops use the same model, which is the point: the gain comes from the architecture rather than a stronger supervisor. Meta's [AIRA2](/systems/aira2.md) ([arXiv](https://arxiv.org/abs/2603.26499)) attacks the other side of the problem, replacing synchronous single-GPU execution with an asynchronous multi-GPU worker pool, adding a hidden consistent evaluation protocol to close the generalization gap and using ReAct agents that debug interactively, and reaches an 81.5% mean percentile rank on MLE-bench-30 at 24 hours against a 72.7% baseline. The pair extend Meta's [hyperagents](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md) of the previous week and Karpathy's [650-experiment autoresearch run](/developments/2026-03-09-autoresearch-650-experiments.md), and are overtaken within days by Apple's [self-distillation result](/developments/2026-04-05-self-distillation-without-a-teacher.md), which removes the search loop entirely.
