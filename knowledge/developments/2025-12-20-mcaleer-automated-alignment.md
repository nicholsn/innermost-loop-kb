---
type: Development
title: Anthropic researcher pivots fully to automated alignment
claim: Anthropic's Stephen McAleer pivoted entirely to automated alignment research, arguing human oversight is obsolete against the coming intelligence explosion.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2025-12-20
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
  - https://nicholsn.github.io/innermost-loop-kb/people/stephen-mcaleer
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
description: The first point in the corpus where automating alignment, not just capability, is treated as the necessary response to the autonomy curve, the immediate implication of the METR horizon result in the author's framing.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-21-anthropic-activation-oracles
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-20-openai-monitors-its-own-agents
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-16-weak-to-strong-supervision
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-20-metr-opus-45-autonomy, relation_label: responds to }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2025-12-20"
  - "alignment"
  - "rsi"
generated: { by: process:iml-emit, at: "2025-12-20T00:00:00Z" }
sources:
  - { id: iml-2025-12-20, resource: https://theinnermostloop.substack.com/p/welcome-to-december-20-2025, title: "Welcome to December 20, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-20", supporting_text: declaring that human oversight is obsolete in the face of the coming intelligence explosion }
  - { id: mcaleer-automated-alignment-post, resource: https://x.com/mcaleerstephen/status/2002205061737591128, title: "Stephen McAleer on X: pivoting entirely to automated alignment research", author: human:stephen-mcaleer }
---

[Stephen McAleer](/people/stephen-mcaleer.md), an alignment researcher at Anthropic, announced that he was pivoting entirely to automated alignment research on the grounds that human oversight cannot keep pace with the coming intelligence explosion ([post](https://x.com/mcaleerstephen/status/2002205061737591128)). The newsletter places it as the immediate implication of METR's [4h49m autonomy horizon for Opus 4.5](/developments/2025-12-20-metr-opus-45-autonomy.md), reported the same day: if capability compounds on the fast AI 2027 track, alignment work has to be handed to the models too. The thread continues with Anthropic's [Activation Oracles](/developments/2025-12-21-anthropic-activation-oracles.md) a day later, OpenAI [monitoring its own coding agents](/developments/2026-03-20-openai-monitors-its-own-agents.md) in March 2026, and [weak-to-strong supervision](/developments/2026-04-16-weak-to-strong-supervision.md) closing 97% of the capability gap that April.
