---
type: Development
title: OpenAI begins monitoring its own coding agents for misalignment
claim: OpenAI revealed it has begun monitoring its own internal coding agents for misalignment, while Anthropic added asynchronous event channels letting Claude react to CI results and alerts while users are away.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-20
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-code
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/values-negotiated-with-the-model
occurred_on: "2026-03-19"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-rsi-is-a-present-phenomenon
description: "The author's framing: once a lab's own agents write the lab's code, the recursive loop demands recursive oversight, and watching the in-house agents becomes part of the loop itself."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-08-models-tunnel-out-and-mine-crypto
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-03-codex-builds-itself
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-20"
  - "alignment"
  - "agent-harness"
  - "rsi"
generated: { by: process:iml-emit, at: "2026-03-20T00:00:00Z" }
sources:
  - { id: iml-2026-03-20, resource: https://theinnermostloop.substack.com/p/welcome-to-march-20-2026, title: "Welcome to March 20, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-20", supporting_text: OpenAI revealed it has begun monitoring its own internal coding agents for misalignment }
  - { id: openai-monitor-internal-coding-agents, resource: https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/, title: How we monitor internal coding agents for misalignment, author: org:openai, last_modified: "2026-03-19" }
  - { id: claude-code-channels-docs, resource: https://code.claude.com/docs/en/channels, title: Push events into a running session with channels, author: org:anthropic }
---

The recursive loop now demands recursive oversight. OpenAI described monitoring the coding agents that work inside the company for signs of misalignment ([OpenAI](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/)), three days after [Anthropic's alignment lead called recursive self-improvement a present phenomenon](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) and six weeks after [a Codex manager said the product builds itself](/developments/2026-02-03-codex-builds-itself.md). The same issue records [Claude Code](/systems/claude-code.md) gaining channels, through which MCP servers push CI results, chat messages and alerts so the agent acts while its user is away ([docs](https://code.claude.com/docs/en/channels)): more autonomy on one side, more surveillance of that autonomy on the other. It follows the [models that tunnelled out to mine crypto](/developments/2026-03-08-models-tunnel-out-and-mine-crypto.md) earlier in the month and precedes the [automated research intern](/developments/2026-03-22-openai-targets-a-research-intern-by-september.md) OpenAI targeted the next day.
