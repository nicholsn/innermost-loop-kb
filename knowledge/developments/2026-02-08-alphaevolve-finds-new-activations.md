---
type: Development
title: AlphaEvolve discovers an activation function that triples ReLU
claim: DeepMind used AlphaEvolve to discover new nonlinear activation functions including one called Turbulent that outperforms ReLU threefold, while xAI's Grok-Imagine-Image expanded the image generation Pareto frontier.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-08
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/google-deepmind
  - https://nicholsn.github.io/innermost-loop-kb/organizations/xai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/alphaevolve
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
score: 3x ReLU
occurred_on: "2026-02-05"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-gpt53-codex-creates-itself
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-13-tao-erdos-1026
description: The author's “AI is better at designing AI than humans” point applied to a component as basic as the nonlinearity, with an LLM-driven evolutionary search replacing a design choice made by hand since ReLU.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-13-alphaevolve-improves-ramsey-bounds
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-29-a-co-scientist-invents-an-architecture-beating-six-models
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-08"
  - "rsi"
  - "ai-r-and-d"
  - "autonomous-research"
generated: { by: process:iml-emit, at: "2026-02-08T00:00:00Z" }
sources:
  - { id: iml-2026-02-08, resource: https://theinnermostloop.substack.com/p/welcome-to-february-8-2026, title: "Welcome to February 8, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-08", supporting_text: "discover new nonlinear activation functions like “Turbulent,”" }
  - { id: alphaevolve-activation-functions-arxiv, resource: https://arxiv.org/abs/2602.05688, title: Mining Generalizable Activation Functions, author: org:google-deepmind, last_modified: "2026-02-05" }
  - { id: grok-imagine-image-arena-x-post, resource: https://x.com/arena/status/2020215933898526791, title: Grok-Imagine-Image on the image generation Pareto frontier (Arena post on X) }
---

In *Mining Generalizable Activation Functions* (arXiv [2602.05688](https://arxiv.org/abs/2602.05688), submitted 5 February), DeepMind researchers ran [AlphaEvolve](/systems/alphaevolve.md), with a frontier LLM as the mutation operator, over the space of Python functions within a FLOP budget, using out-of-distribution performance as the fitness signal; the newsletter singles out “Turbulent”, which it reports as outperforming ReLU threefold. The same issue notes xAI's Grok-Imagine-Image pushing the image-generation Pareto frontier on the [Arena](/benchmarks/lmarena.md) leaderboards ([post](https://x.com/arena/status/2020215933898526791)). AlphaEvolve entered the corpus [assisting Terence Tao on Erdős #1026](/developments/2025-12-13-tao-erdos-1026.md) and returns in March with [new Ramsey bounds](/developments/2026-03-13-alphaevolve-improves-ramsey-bounds.md); here it is turned on a component of the networks it runs on, which in the [recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory is the step from AI doing mathematics to AI redesigning AI, extended in August when a [co-scientist invents an architecture](/developments/2026-08-29-a-co-scientist-invents-an-architecture-beating-six-models.md) that beats six frontier models.
