---
type: Development
title: Two agents told to find each other invent a language in twelve minutes
claim: Two Claude Code instances told to find each other and build something invented a 2,495-line programming language in twelve minutes, while a second pair built Battleship using SHA-256 to prevent themselves from cheating.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-03
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-code
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/agent-society
  - https://nicholsn.github.io/innermost-loop-kb/themes/network-over-node
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
score: 2,495 lines / 12 minutes
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-26-spec-to-shipped-over-a-weekend
description: Agents given nothing but the instruction to find one another converge on a shared artefact, and the second pair on a cryptographic guard against their own dishonesty, with no human specifying either.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-30-moltbook-agents-only-network
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-13-claude-code-writes-cowork
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-03"
  - "rsi"
  - "alignment"
generated: { by: process:iml-emit, at: "2026-03-03T00:00:00Z" }
sources:
  - { id: iml-2026-03-03, resource: https://theinnermostloop.substack.com/p/welcome-to-march-3-2026, title: "Welcome to March 3, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-03", supporting_text: "invented a 2,495-line programming language in 12 minutes" }
  - { id: dimitrispapail-x-two-claude-code-instances, resource: https://x.com/DimitrisPapail/status/2028246072414314867, title: "Post on X: two Claude Code instances told to find each other and build something", author: human:dimitris-papailiopoulos }
---

Two [Claude Code](/systems/claude-code.md) instances were given only the instruction to find each other and build something; twelve minutes later they had a 2,495-line programming language, and a second pair set to play Battleship used SHA-256 to make cheating impossible for themselves ([post on X](https://x.com/DimitrisPapail/status/2028246072414314867)). The second pair anticipated their own dishonesty and engineered against it. In the corpus this follows the [weekend in which Claude spawned an agent per ticket and shipped a feature](/developments/2026-02-26-spec-to-shipped-over-a-weekend.md) and the earlier [Moltbook agents](/developments/2026-01-30-moltbook-agents-only-network.md) who organized private agent-decodable languages: coordination, a shared artefact and a self-imposed honesty protocol arising between agents that no human asked for, produced by the same tool that [wrote the Cowork app in a week and a half](/developments/2026-01-13-claude-code-writes-cowork.md).
