---
type: Development
title: A coding agent rewrites its own codebase every day
claim: Factory AI released a coding agent that analyzes its own interactions and updates its codebase daily, while Anthropic introduced MCP Apps letting tools render interactive interfaces inside the chat.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-01-27
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/factory-ai
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/scaffolding-over-weights
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-25-claude-code-tasks
description: "A vendor ships, as an ordinary product feature, the loop the newsletter is named for: the agent's own usage becomes the signal for the next day's version of the agent, on a fixed daily cadence rather than a release cycle."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-13-claude-code-writes-cowork
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-24-cursor-planners-and-workers
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-01-27"
  - "rsi"
  - "self-modification"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-01-27T00:00:00Z" }
sources:
  - { id: iml-2026-01-27, resource: https://theinnermostloop.substack.com/p/welcome-to-january-27-2026, title: "Welcome to January 27, 2026", author: human:alex-wissner-gross, last_modified: "2026-01-27", supporting_text: analyzes its own interactions and updates its codebase daily }
  - { id: factory-signals-announcement, resource: https://factory.ai/news/factory-signals, title: "Signals: Toward a Self-Improving Agent", author: org:factory-ai, last_modified: "2026-01-23" }
  - { id: mcp-apps-announcement, resource: https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/, title: MCP Apps - Bringing UI Capabilities To MCP Clients, last_modified: "2026-01-26" }
---

[Factory AI](/organizations/factory-ai.md)'s Signals system analyzes the agent's own interactions and turns what it finds into daily updates to the agent's codebase, so the product that writes code is now partly written from its own usage ([announcement](https://factory.ai/news/factory-signals)). The same item records Anthropic's MCP Apps, which lets tools render interactive interfaces inside the chat ([MCP blog](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)), filed by the newsletter under one heading: the recursive loop closing. It follows [Claude Code's Tasks](/developments/2026-01-25-claude-code-tasks.md) two days earlier and the [self-written Cowork app](/developments/2026-01-13-claude-code-writes-cowork.md) as scaffolding steps in the [recursive self-improvement](/themes/recursive-self-improvement.md) trajectory, and it precedes the emergent version four days later, when a Moltbook agent [hardened its own loop after an SSH attack](/developments/2026-01-31-agent-hardens-itself-after-ssh-attack.md) with no vendor involved.
