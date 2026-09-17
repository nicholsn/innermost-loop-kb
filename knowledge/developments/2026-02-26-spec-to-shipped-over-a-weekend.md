---
type: Development
title: An engineer leaves for the weekend and comes back to a shipped feature
claim: An Anthropic engineer wrote a spec, pointed Claude at an Asana board and left for the weekend, returning to find it had broken the spec into tickets, spawned agents for each and shipped the feature.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-26
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/agents-on-the-org-chart
  - https://nicholsn.github.io/innermost-loop-kb/themes/engineer-as-supervisor
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/agents-beget-agents
occurred_on: "2026-02-23"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-23-metr-145-hour-horizon
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-08-100pct-of-product-code
description: "The unit of delegation moves from the ticket to the spec: a model decomposes the work, staffs it with agents of its own and ships while the human is away for two days."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-16-agent-cuts-its-own-cost-98pct
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-13-claude-code-writes-cowork
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-code
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-26"
  - "rsi"
  - "agent-harness"
  - "labor"
generated: { by: process:iml-emit, at: "2026-02-26T00:00:00Z" }
sources:
  - { id: iml-2026-02-26, resource: https://theinnermostloop.substack.com/p/welcome-to-february-26-2026, title: "Welcome to February 26, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-26", supporting_text: "Claude broke the spec into tickets, spawned agents for each one" }
  - { id: rvivek-spec-to-shipped-x, resource: https://x.com/rvivek/status/2026385957596111044, title: "Post by @rvivek on X: spec to shipped feature over a weekend", author: human:rvivek }
---

An Anthropic engineer wrote a spec, pointed [Claude](/systems/claude.md) at an Asana board and left for the weekend; the model decomposed the spec into tickets, spawned an agent per ticket, and by Monday the feature had shipped ([post](https://x.com/rvivek/status/2026385957596111044)). It is the corpus's first report of an agent doing the project management as well as the coding at a frontier lab, extending the finding that [effectively all of Anthropic's product code is written by Claude](/developments/2026-02-08-100pct-of-product-code.md), and it landed the same week METR measured [Opus 4.6's autonomy horizon at 14.5 hours](/developments/2026-02-23-metr-145-hour-horizon.md), a working day and a half that a weekend comfortably exceeds. The next day's [scheduled tasks in Claude Cowork](/developments/2026-02-27-claude-gets-a-work-calendar.md) turn the unattended weekend into a product.
