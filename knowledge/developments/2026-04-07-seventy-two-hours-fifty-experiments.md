---
type: Development
title: Three unsupervised days produce a memory system beating every baseline
claim: UNC researchers let an AI run autonomously for 72 hours, during which it ran fifty experiments and invented a long-context memory system that beats every human-designed baseline.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-04-07
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/unc
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/automated-science
score: 72 hours / 50 experiments
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-05-self-distillation-without-a-teacher
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-09-autoresearch-650-experiments
description: "The author's 'scientist is now a subroutine' moment: an unattended loop is credited with inventing an architecture rather than tuning one, and its largest gains came from bug fixes and structural changes beyond the reach of AutoML."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-12-alma-agents-design-their-own-memory
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-31-bilevel-autoresearch
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-04-07"
  - "autonomous-research"
  - "rsi"
  - "ai-r-and-d"
generated: { by: process:iml-emit, at: "2026-04-07T00:00:00Z" }
sources:
  - { id: iml-2026-04-07, resource: https://theinnermostloop.substack.com/p/welcome-to-april-7-2026, title: "Welcome to April 7, 2026", author: human:alex-wissner-gross, last_modified: "2026-04-07", supporting_text: let an AI loose for 72 hours of autonomous research }
  - { id: omni-simplemem-arxiv, resource: https://arxiv.org/abs/2604.01007, title: "Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory", author: org:unc }
---

The paper behind the item is *Omni-SimpleMem* ([arXiv 2604.01007](https://arxiv.org/abs/2604.01007)), from a UNC-led team: an autonomous research pipeline started from a naive agent-memory baseline and, with no human in the inner loop, executed roughly 50 experiments across two benchmarks over what the newsletter reports as 72 unattended hours, lifting F1 on LoCoMo from 0.117 to 0.598 (+411%) and on Mem-Gallery from 0.254 to 0.797 (+214%) to reach state of the art on both. The authors stress that the biggest gains were bug fixes, architectural changes and prompt rewrites rather than hyperparameter tuning, which is what separates the run from AutoML. In the [recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it sits between Karpathy's [650-experiment autoresearch run](/developments/2026-03-09-autoresearch-650-experiments.md) and Anthropic's report the next day that Mythos [sped internal research up to 400x](/developments/2026-04-08-research-sped-up-400x.md); the target it optimized, agent memory, is the same one [ALMA](/developments/2026-02-12-alma-agents-design-their-own-memory.md) had agents meta-learn in February.
