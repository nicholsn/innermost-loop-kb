---
type: Development
title: The cheap model beats the expensive one
claim: Anthropic's Sonnet 4.6 claimed the lead on GDPval-AA at 1633 Elo and 63.3% on Finance Agent v1.1, beating Opus 4.6 on both at a fraction of the cost, while Musk claimed Grok 4.2 features continuous post-training learning that will let it improve every week.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-18
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
  - https://nicholsn.github.io/innermost-loop-kb/organizations/xai
  - https://nicholsn.github.io/innermost-loop-kb/people/elon-musk
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-sonnet-4-6
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-opus-4-6
  - https://nicholsn.github.io/innermost-loop-kb/systems/grok-4-20
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/gdpval-aa
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/finance-agent
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/reasoning-price-deflation
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
score: 1633 Elo / 63.3%
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-13-intelligence-too-cheap-to-meter
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-46-released
description: "Two ways the frontier compounds in one paragraph: the price of a leaderboard-topping model collapses to the mid tier, and a rival promises a model that keeps learning after it ships."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-24-sholto-continual-learning-2026
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-10-xai-used-claude-to-build-grok
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-17-models-improve-every-few-days
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-18"
  - "capability-jump"
  - "continual-learning"
  - "evaluation"
generated: { by: process:iml-emit, at: "2026-02-18T00:00:00Z" }
sources:
  - { id: iml-2026-02-18, resource: https://theinnermostloop.substack.com/p/welcome-to-february-18-2026, title: "Welcome to February 18, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-18", supporting_text: beating even Opus 4.6 on both at a fraction of the cost }
  - { id: anthropic-sonnet-4-6-announcement, resource: https://www.anthropic.com/news/claude-sonnet-4-6, title: Introducing Sonnet 4.6, author: org:anthropic }
  - { id: artificial-analysis-gdpval-aa-leaderboard, resource: https://artificialanalysis.ai/evaluations/gdpval-aa, title: GDPval-AA leaderboard, author: org:artificial-analysis }
  - { id: vals-ai-finance-agent-leaderboard, resource: https://www.vals.ai/benchmarks/finance_agent, title: Finance Agent benchmark leaderboard, author: org:vals-ai }
  - { id: musk-grok-4-2-continuous-learning-x, resource: https://x.com/elonmusk/status/2023828048580387001, title: "Elon Musk on X: Grok 4.2 continuous post-training learning", author: human:elon-musk }
---

Anthropic's [Sonnet 4.6](/systems/claude-sonnet-4-6.md) took the top spot on Artificial Analysis' [GDPval-AA](/benchmarks/gdpval-aa.md) at 1633 Elo and led Vals AI's [Finance Agent v1.1](/benchmarks/finance-agent.md) at 63.3%, ahead of [Opus 4.6](/systems/claude-opus-4-6.md), the larger model that had [taken the GDPval-AA lead from GPT-5.2](/developments/2026-02-06-opus-46-released.md) twelve days earlier ([GDPval-AA leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), [Finance Agent leaderboard](https://www.vals.ai/benchmarks/finance_agent)); Anthropic's own [announcement](https://www.anthropic.com/news/claude-sonnet-4-6), which gives neither figure, framed the model as Opus-class performance on real-world, economically valuable office tasks at unchanged Sonnet pricing. In the same paragraph Musk said xAI's [Grok 4.2](/systems/grok-4-20.md) features continuous post-training that will let it improve every week, promising recursive intelligence growth ([post](https://x.com/elonmusk/status/2023828048580387001)). The first half extends the [dollar-an-hour agentic capability](/developments/2026-02-13-intelligence-too-cheap-to-meter.md) storyline; the second is an early vendor claim of a shipped model that keeps learning, the property [Sholto Douglas predicted for 2026](/developments/2025-12-24-sholto-continual-learning-2026.md) and later reported as [models improving every few days](/developments/2026-05-17-models-improve-every-few-days.md).
