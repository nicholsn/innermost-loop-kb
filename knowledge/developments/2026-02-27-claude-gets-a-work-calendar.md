---
type: Development
title: An agent gets a work calendar before most interns do
claim: Anthropic introduced scheduled tasks in Claude Cowork that complete recurring jobs automatically from morning briefs to Friday presentations, while Amplifying pointed Claude Code at thousands of repositories to extract what the model considers current best practice.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-27
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
  - https://nicholsn.github.io/innermost-loop-kb/organizations/amplifying
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-cowork
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-code
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/agents-on-the-org-chart
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-26-spec-to-shipped-over-a-weekend
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-25-claude-code-tasks
description: "The author's 'agents are clocking in' framing: recurring work moves from a human prompt to a standing calendar, and the agent is turned back on the code it learned from to audit the craft it is absorbing."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-13-claude-code-writes-cowork
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-27-factory-ai-updates-itself-daily
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-27"
  - "agent-harness"
  - "rsi"
  - "evaluation"
generated: { by: process:iml-emit, at: "2026-02-27T00:00:00Z" }
sources:
  - { id: iml-2026-02-27, resource: https://theinnermostloop.substack.com/p/welcome-to-february-27-2026, title: "Welcome to February 27, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-27", supporting_text: "complete recurring jobs automatically, from morning briefs to Friday presentations" }
  - { id: claudeai-x-cowork-scheduled-tasks, resource: https://x.com/claudeai/status/2026720870631354429, title: "Claude on X: scheduled tasks in Claude Cowork", author: org:anthropic }
  - { id: amplifying-what-claude-code-chooses, resource: https://amplifying.ai/research/claude-code-picks, title: What Claude Code Actually Chooses, author: org:amplifying }
---

[Claude Cowork](/systems/claude-cowork.md)'s scheduled tasks give the agent a standing calendar of recurring jobs, from morning briefs to Friday presentations, that run without a fresh prompt ([announcement](https://x.com/claudeai/status/2026720870631354429)). In the same paragraph Amplifying ran [Claude Code](/systems/claude-code.md) across thousands of GitHub repositories, a survey of 2,430 responses across three models and twenty tool categories, to record which tools and practices the model itself now recommends ([What Claude Code Actually Chooses](https://amplifying.ai/research/claude-code-picks)). The pairing extends the [weekend spec-to-ship run](/developments/2026-02-26-spec-to-shipped-over-a-weekend.md) and the earlier [Tasks for Claude Code](/developments/2026-01-25-claude-code-tasks.md): the agent acquires an employee's scheduling infrastructure while outsiders begin auditing what it has learned, much as [Factory's agent](/developments/2026-01-27-factory-ai-updates-itself-daily.md) reads its own interactions to update itself. Cowork is also the app [Claude Code wrote in a week and a half](/developments/2026-01-13-claude-code-writes-cowork.md), so the calendar is kept by software the agent built.
