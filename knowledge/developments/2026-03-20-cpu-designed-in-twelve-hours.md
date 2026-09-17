---
type: Development
title: An agent takes a CPU from concept to tape-out in twelve hours
claim: Verkor announced Design Conductor, an agent that autonomously built a 1.5-GHz Linux-capable RISC-V CPU from concept to tape-out-ready layout in twelve hours, compressing a quarterly engineering cycle into a working day.
domain: compute
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-20
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/verkor-ai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/design-conductor
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/silicon-designs-itself
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
score: 12 hours
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-transformers-run-arbitrary-c-code
description: "The first corpus item in which the substrate becomes an output of the loop: an agent laying out silicon end to end, so chip design time stops being a human-bounded step."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-03-a-quantum-chip-designed-by-an-agent
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-03-circuits-drawn-in-minutes-not-months
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-20"
  - "chip-design"
  - "rsi"
  - "capability-jump"
generated: { by: process:iml-emit, at: "2026-03-20T00:00:00Z" }
sources:
  - { id: iml-2026-03-20, resource: https://theinnermostloop.substack.com/p/welcome-to-march-20-2026, title: "Welcome to March 20, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-20", supporting_text: autonomously built a 1.5-GHz Linux-capable RISC-V CPU from concept to tape-out-ready GDSII in 12 hours }
  - { id: design-conductor-arxiv, resource: https://arxiv.org/abs/2603.08716, title: "Design Conductor: An agent autonomously builds a 1.5 GHz Linux-capable RISC-V CPU", author: org:verkor-ai }
---

Design Conductor started from a 219-word requirements document and, in 12 unattended hours, produced several micro-architecture variants of a complete RISC-V core (VerCore) meeting timing at 1.48 GHz on the ASAP7 PDK, with a CoreMark of 3261, roughly a 2011 Celeron, and a verified, tape-out-ready GDSII layout ([arXiv](https://arxiv.org/abs/2603.08716)). Verkor calls it the first time an autonomous agent has built a complete working CPU from spec to layout. In the [recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it opens the [silicon-designs-itself](/themes/silicon-designs-itself.md) thread: two days later [TERAFAB](/developments/2026-03-22-terafab-announced.md) was announced with a recursive design loop, and the thread runs through [a quantum chip designed with an agent](/developments/2026-06-03-a-quantum-chip-designed-by-an-agent.md) in June to [the first chip designed end to end by AI](/developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai.md) in August.
