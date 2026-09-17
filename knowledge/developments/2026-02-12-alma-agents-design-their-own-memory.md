---
type: Development
title: Agents meta-learn their own memory architecture
claim: Researchers introduced ALMA, a framework letting agents meta-learn their own memory designs and database schemas, addressing continual learning through recursive self-improvement, while Zhipu's GLM-5 took the top open-weight spot on agentic benchmarks.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-12
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/ubc
  - https://nicholsn.github.io/innermost-loop-kb/organizations/zhipu-ai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/alma
  - https://nicholsn.github.io/innermost-loop-kb/systems/glm-5
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/vending-bench-2
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
  - https://nicholsn.github.io/innermost-loop-kb/themes/open-weight-latency
occurred_on: "2026-02-08"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-11-poetiq-55pct-hle
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-30-stanford-test-time-training
description: "Continual learning, the capability Anthropic's Sholto Douglas predicted would be solved in 2026, handed to the agents themselves: the memory module stops being a human design choice and becomes a search space the system optimizes."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-24-sholto-continual-learning-2026
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-02-prime-intellect-rlm
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-07-seventy-two-hours-fifty-experiments
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-12"
  - "rsi"
  - "continual-learning"
  - "self-modification"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-02-12T00:00:00Z" }
sources:
  - { id: iml-2026-02-12, resource: https://theinnermostloop.substack.com/p/welcome-to-february-12-2026, title: "Welcome to February 12, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-12", supporting_text: meta-learn their own memory designs }
  - { id: alma-arxiv, resource: https://arxiv.org/abs/2602.07755, title: Learning to Continually Learn via Meta-learning Agentic Memory Designs, author: org:ubc, last_modified: "2026-02-08" }
  - { id: glm-5-zai-blog, resource: https://z.ai/blog/glm-5, title: GLM-5 (Z.ai blog), author: org:zhipu-ai }
---

ALMA (Automated meta-Learning of Memory designs for Agentic systems), from Yiming Xiong, Shengran Hu and Jeff Clune at the University of British Columbia, uses a meta agent that searches open-endedly over memory designs written as executable code, database schemas plus their retrieval and update rules, and reports that the learned designs beat state-of-the-art hand-crafted memory on all four sequential decision-making domains tested (arXiv [2602.07755](https://arxiv.org/abs/2602.07755), submitted 8 February); the authors themselves call it a step toward self-improving systems. The same issue records [GLM-5](/systems/glm-5.md) taking the top open-weight position on agentic benchmarks including [Vending-Bench 2](/benchmarks/vending-bench-2.md) ([Z.ai](https://z.ai/blog/glm-5)). In the [recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it follows the [continual-learning-in-2026 prediction](/developments/2025-12-24-sholto-continual-learning-2026.md) and Stanford's [test-time-training result](/developments/2025-12-30-stanford-test-time-training.md), and anticipates the April run in which an agent [invented a long-context memory system unattended](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md).
