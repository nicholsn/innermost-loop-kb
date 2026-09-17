---
type: Development
title: Agents review their own session histories overnight
claim: Anthropic launched dreaming in its managed agents, a scheduled process that reviews session histories and curates shared memories across teams, while Chrome began quietly installing four gigabytes of a local model on every desktop with available storage.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-05-08
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
  - https://nicholsn.github.io/innermost-loop-kb/organizations/google
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-managed-agents
  - https://nicholsn.github.io/innermost-loop-kb/systems/gemini-nano
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/agent-society
  - https://nicholsn.github.io/innermost-loop-kb/themes/models-sleep
score: 4 GB
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-29-every-ticket-gets-its-own-agent
description: "The newsletter files a memory-curation job under agents training themselves overnight: offline consolidation, until now a research result about agents designing their own memory, ships as a product feature the agents run on themselves."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-12-alma-agents-design-their-own-memory
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-07-seventy-two-hours-fifty-experiments
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-23-agents-build-memories-from-screen-captures
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-05-08"
  - "rsi"
  - "continual-learning"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-05-08T00:00:00Z" }
sources:
  - { id: iml-2026-05-08, resource: https://theinnermostloop.substack.com/p/welcome-to-may-8-2026, title: "Welcome to May 8, 2026", author: human:alex-wissner-gross, last_modified: "2026-05-08", supporting_text: a scheduled process that reviews session histories and curates shared memories across teams }
  - { id: anthropic-managed-agents-dreaming-blog, resource: https://claude.com/blog/new-in-claude-managed-agents, title: "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration", author: org:anthropic }
  - { id: 9to5google-chrome-gemini-nano-4gb, resource: https://9to5google.com/2026/05/06/google-chrome-4gb-storage-ai-details/, title: "Google Chrome takes up 4GB for AI, but only if you have room", author: org:9to5google, last_modified: "2026-05-06" }
---

Anthropic's “dreaming” is a scheduled job inside [Claude Managed Agents](/systems/claude-managed-agents.md) that reads back an agent's session histories and curates the memories worth keeping, shared across a team's agents ([Anthropic blog](https://claude.com/blog/new-in-claude-managed-agents)); the newsletter files it under agents training themselves overnight. It brings offline consolidation into a shipped product, after researchers had agents [meta-learn their own memory designs](/developments/2026-02-12-alma-agents-design-their-own-memory.md) and a 72-hour unsupervised run [invented a memory system](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md), and it anticipates the [models-sleep](/themes/models-sleep.md) theme the newsletter names later in May. The same issue notes Chrome quietly installing 4 GB of [Gemini Nano](/systems/gemini-nano.md) on every desktop with room for it ([9to5Google](https://9to5google.com/2026/05/06/google-chrome-4gb-storage-ai-details/)), the local-model half of the claim. It follows the [Symphony orchestrator](/developments/2026-04-29-every-ticket-gets-its-own-agent.md) giving every ticket its own agent, and precedes the [self-rewriting harness](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) of June.
