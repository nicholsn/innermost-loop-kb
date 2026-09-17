---
type: Development
title: Effectively all of Anthropic's product code is written by Claude
claim: Anthropic's chief product officer confirmed that effectively 100% of Anthropic product code is now written by Claude, while OpenAI cut its model release cycle from 97 days to 29.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-08
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
  - https://nicholsn.github.io/innermost-loop-kb/people/mike-krieger
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/engineer-as-supervisor
score: 100% / 97→29 days
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-07-openai-bans-editors-and-terminals
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-27-amodei-country-of-geniuses-2027
description: "The newsletter's “bootstrap complete” moment: the tool that writes the tools has taken over the entire product codebase of a frontier lab, while a rival's release cadence compresses threefold."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-27-cherny-200-pull-requests
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-03-codex-builds-itself
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-claude-code-4pct-of-commits
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-08"
  - "rsi"
  - "ai-r-and-d"
generated: { by: process:iml-emit, at: "2026-02-08T00:00:00Z" }
sources:
  - { id: iml-2026-02-08, resource: https://theinnermostloop.substack.com/p/welcome-to-february-8-2026, title: "Welcome to February 8, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-08", supporting_text: “effectively 100%” of Anthropic product code is now written by Claude }
  - { id: krieger-cisco-enterprise-ai-interview, resource: "https://www.youtube.com/watch?v=CHscuD6Q4xs&t=582s", title: "Enterprise & AI | Mike Krieger, Chief Product Officer, Anthropic", author: org:cisco }
  - { id: openai-release-cadence-x-post, resource: https://x.com/chatgpt21/status/2019983107781242936, title: OpenAI's model release cycle down from 97 days to 29 (post on X) }
---

Speaking in Cisco's Enterprise & AI interview series, Anthropic chief product officer Mike Krieger put the share of Anthropic product code written by [Claude](/systems/claude.md) at “effectively 100%” ([interview](https://www.youtube.com/watch?v=CHscuD6Q4xs&t=582s)); the same issue records OpenAI's release cadence shortening from 97 days to 29 ([post](https://x.com/chatgpt21/status/2019983107781242936)). It closes the arc that ran from [Boris Cherny's 200 pull requests](/developments/2025-12-27-cherny-200-pull-requests.md) in December through [Dario Amodei's “much of the code”](/developments/2026-01-27-amodei-country-of-geniuses-2027.md) in January, and sits beside OpenAI's [Codex building itself](/developments/2026-02-03-codex-builds-itself.md). In the [recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it is the point where the product layer of a frontier lab is fully model-written; the model-training layer follows in March, when [70-90% of model code](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) is reported as Claude-written.
