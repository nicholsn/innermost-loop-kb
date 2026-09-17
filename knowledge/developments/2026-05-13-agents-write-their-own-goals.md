---
type: Development
title: Users metaprompt an agent to write its own objective file
claim: Users are now metaprompting Codex to draft its own goal specification, with one calling the resulting stack the highest-leverage agent configuration available today.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-05-13
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/codex
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/scaffolding-over-weights
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/self-authored-scaffolding
occurred_on: "2026-05-11"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-11-the-harness-eats-the-model
description: "After agents writing their own skills and harnesses, the corpus records them writing the brief itself: the objective, the last human-authored layer, moves inside the loop."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-31-bilevel-autoresearch
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-03-codex-builds-itself
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-25-an-agent-rewrites-its-own-harness
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-11-the-harness-eats-the-model, relation_label: extends }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-05-13"
  - "rsi"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-05-13T00:00:00Z" }
sources:
  - { id: iml-2026-05-13, resource: https://theinnermostloop.substack.com/p/welcome-to-may-13-2026, title: "Welcome to May 13, 2026", author: human:alex-wissner-gross, last_modified: "2026-05-13", supporting_text: the highest leverage AI agent configuration available today }
  - { id: daniel-mac8-codex-goal-x, resource: https://x.com/daniel_mac8/status/2053896200005271594, title: "@daniel_mac8 on X: metaprompting Codex to draft its own /goal", author: human:daniel-mac8 }
---

The pattern the newsletter picked up is a user asking [Codex](/systems/codex.md) to draft its own “/goal”, the objective file that steers its subsequent work, rather than writing the brief by hand; the poster the issue quotes called the result “the highest leverage AI agent configuration available today” ([X](https://x.com/daniel_mac8/status/2053896200005271594)). It comes two days after [Hermes Agent took the token rankings by generating its own skills](/developments/2026-05-11-the-harness-eats-the-model.md) and six weeks after a research loop [wrote the strategies for its own outer loop](/developments/2026-03-31-bilevel-autoresearch.md): skills, harness and now the objective are being authored by the agent, the thread the [self-authored-scaffolding](/themes/self-authored-scaffolding.md) theme names in June. The next day [Recursive Superintelligence emerged from stealth with $650 million](/developments/2026-05-14-recursive-superintelligence-raises-650m.md) to have AI experiment on improving itself, and in June the [Self-Harness paradigm](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) closed the loop without a human engineer.
