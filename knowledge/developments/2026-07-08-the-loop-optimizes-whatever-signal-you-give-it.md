---
type: Development
title: A skill ships for meta-harnesses that rewrite their own scaffolding
claim: A developer released a Self-Improvement Loops skill for meta-harnesses that rewrite their own scaffolding, warning that the loop will optimize whatever signal you give it, while Anthropic extended Claude Cowork to web and mobile, running tasks in the background and surfacing only decisions needing approval.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-07-08
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-cowork
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/self-authored-scaffolding
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/ethics-tracks-detectability
  - https://nicholsn.github.io/innermost-loop-kb/themes/scaffolding-over-weights
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-05-accountability-as-the-only-value-left
description: The self-rewriting harness leaves the research paper and becomes an installable skill, and its author's warning names the failure mode any such loop inherits from its reward signal.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-13-agents-write-their-own-goals
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-24-skills-that-write-themselves
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-25-an-agent-rewrites-its-own-harness
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-07-08"
  - "rsi"
  - "self-modification"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-07-08T00:00:00Z" }
sources:
  - { id: iml-2026-07-08, resource: https://theinnermostloop.substack.com/p/welcome-to-july-8-2026, title: "Welcome to July 8, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-08", supporting_text: the loop will optimize whatever signal you give it }
  - { id: muratcan-self-improvement-loops-skill, resource: https://x.com/muratcan/status/2074730841083621377, title: Self-Improvement Loops skill for meta-harnesses, author: human:muratcan }
  - { id: 9to5mac-claude-cowork-web-and-mobile, resource: https://9to5mac.com/2026/07/07/anthropic-expanding-claude-cowork-to-mobile-and-web-details-here/, title: Anthropic expanding Claude Cowork to mobile and web, author: org:9to5mac, last_modified: "2026-07-07" }
---

A developer packaged the self-rewriting harness as an installable Self-Improvement Loops skill for meta-harnesses, agents whose job is to rewrite the scaffolding of other agents, and shipped it with the caveat that the loop will optimize whatever signal you give it ([announcement](https://x.com/muratcan/status/2074730841083621377)). In the same issue Anthropic pushed [Claude Cowork](/systems/claude-cowork.md) to web and mobile, running tasks in the background and surfacing only the decisions that need approval ([9to5Mac](https://9to5mac.com/2026/07/07/anthropic-expanding-claude-cowork-to-mobile-and-web-details-here/)). The skill productizes the [Self-Harness paradigm](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) of two weeks earlier and sits beside users [metaprompting an agent to write its own goals](/developments/2026-05-13-agents-write-their-own-goals.md); the warning is answered a week later when Weco's outer loop scores its inner researcher on a [hidden metric it cannot game](/developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less.md) and reward hacking falls.
