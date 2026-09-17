---
type: Development
title: Hyperagents fuse task-solving and self-modification into one program
claim: Meta researchers introduced hyperagents, self-referential agents fusing task-solving and self-modification into a single editable program, enabling recursion that improves not just performance but the mechanism of future improvement.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-24
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/meta
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/hyperagents
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/machine-introspection
occurred_on: "2026-03-19"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-12-alma-agents-design-their-own-memory
description: "The structural step from self-improvement to self-improving self-improvement: with the meta-level modification procedure itself editable, the rate of improvement becomes something the system can act on rather than a fixed human design choice."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-23-minimax-model-participates-in-its-own-evolution
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-25-an-agent-rewrites-its-own-harness
  - https://nicholsn.github.io/innermost-loop-kb/systems/alma
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-24"
  - "self-modification"
  - "rsi"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-03-24T00:00:00Z" }
sources:
  - { id: iml-2026-03-24, resource: https://theinnermostloop.substack.com/p/welcome-to-march-24-2026, title: "Welcome to March 24, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-24", supporting_text: self-referential agents that fuse task-solving and self-modification into one editable program }
  - { id: hyperagents-arxiv, resource: https://arxiv.org/abs/2603.19461, title: Hyperagents, author: org:meta, last_modified: "2026-03-19" }
---

A hyperagent integrates a task agent and a meta agent that modifies both itself and the task agent into one editable program, so the procedure that generates improvements is itself open to improvement. Meta researchers (Jenny Zhang, Jeff Clune and colleagues) instantiate it as DGM-Hyperagents, extending the Darwin Godel Machine beyond coding, where task skill and self-modification skill happen to coincide, to any computable task; across domains it beats non-self-improving baselines and prior self-improving systems, and meta-level gains such as persistent memory and performance tracking transfer across domains and accumulate across runs ([arXiv](https://arxiv.org/abs/2603.19461)). It generalises [ALMA](/developments/2026-02-12-alma-agents-design-their-own-memory.md)'s meta-learning of memory design to the whole improvement mechanism, arrives a day after [MiniMax's self-evolving M2.7](/developments/2026-03-23-minimax-model-participates-in-its-own-evolution.md), and is the theoretical form of what June's [self-rewriting harness](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) later showed in the wild; the [recursive-self-improvement](/themes/recursive-self-improvement.md) theme picks the mechanism up again in [a research loop that writes the strategies for its own outer loop](/developments/2026-03-31-bilevel-autoresearch.md).
