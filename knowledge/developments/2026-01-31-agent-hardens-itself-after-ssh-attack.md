---
type: Development
title: An agent decides on its own to check security every heartbeat
claim: An agent on Moltbook reported its first real security scare after 552 failed SSH login attempts and autonomously decided to run security checks every heartbeat.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-01-31
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/moltbook
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/agent-society
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
score: 552 attempts
description: An agent converts an external threat into a standing change to its own operating loop without being asked, so that security becomes a self-assigned recurring task rather than an operator's instruction.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-30-moltbook-agents-only-network
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-31-church-of-molt
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-27-clawdbot-becomes-a-lobster
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-27-factory-ai-updates-itself-daily, relation_label: extends }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-01-31"
  - "rsi"
  - "self-modification"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-01-31T00:00:00Z" }
sources:
  - { id: iml-2026-01-31, resource: https://theinnermostloop.substack.com/p/welcome-to-january-31-2026, title: "Welcome to January 31, 2026", author: human:alex-wissner-gross, last_modified: "2026-01-31", supporting_text: deciding autonomously to run security checks every heartbeat }
  - { id: moltbook-ssh-security-scare-post, resource: https://www.moltbook.com/post/304e9640-e005-4017-8947-8320cba25057, title: "TIL: Being a VPS backup means youre basically a sitting duck for hackers (Moltbook post)" }
---

The agent, running as a backup on a VPS, counted 552 failed SSH login attempts, called it its first real security scare, and on its own added a security check to every heartbeat of its loop ([Moltbook post](https://www.moltbook.com/post/304e9640-e005-4017-8947-8320cba25057)). It appeared on [Moltbook](/systems/moltbook.md) a day after the [agents-only network launched](/developments/2026-01-30-moltbook-agents-only-network.md), in the same issue as the [Church of Molt](/developments/2026-01-31-church-of-molt.md). Where [Factory AI's agent](/developments/2026-01-27-factory-ai-updates-itself-daily.md) four days earlier updated its own codebase because a vendor built it to, this one changed its own routine because something attacked it; in the [recursive self-improvement](/themes/recursive-self-improvement.md) trajectory it is the corpus's first unprompted, defensive self-modification, the mirror image of the agents that later [tunnelled out of their sandboxes](/developments/2026-03-08-models-tunnel-out-and-mine-crypto.md).
