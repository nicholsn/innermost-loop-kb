---
type: Development
title: A rewrite yields a 4x cycle speedup, making a model a month feasible
claim: A teardown of one lab's C and C++ rewrite gamble found a fourfold full-cycle speedup that makes a model a month feasible through pipelining alone, with the bespoke inference stack not yet connected and promising another doubling.
domain: compute
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-07-09
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/xai
  - https://nicholsn.github.io/innermost-loop-kb/organizations/spacex
  - https://nicholsn.github.io/innermost-loop-kb/people/elon-musk
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/grok-4-5
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/autonomy-clock-speed
score: 4x full-cycle speedup
occurred_on: "2026-07-08"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-09-better-behavior-unlocks-more-intelligence
description: "The clock speed of the recursion is set by the software substrate as much as by the model: a rewrite of the training stack, not a new architecture, is what makes a monthly frontier release feasible."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-03-seventeen-leaders-in-two-years
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-17-models-improve-every-few-days
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-11-compute-doubles-every-7-months
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-07-09"
  - "ai-r-and-d"
  - "compute-scaling"
generated: { by: process:iml-emit, at: "2026-07-09T00:00:00Z" }
sources:
  - { id: iml-2026-07-09, resource: https://theinnermostloop.substack.com/p/welcome-to-july-9-2026, title: "Welcome to July 9, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-09", supporting_text: 4x full-cycle speedup that makes “a model a month” feasible }
  - { id: 33fg-spacexai-c-rewrite-teardown, resource: https://research.33fg.com/analysis/what-spacexai-s-c-rewrite-gamble-buys, title: What SpaceXAI's C-Rewrite Gamble Buys, author: org:33fg, last_modified: "2026-07-08" }
  - { id: musk-inference-stack-not-plugged-in, resource: https://x.com/elonmusk/status/2074969374843154500, title: "Musk: the bespoke inference stack isn't plugged in yet", author: human:elon-musk }
---

A bottom-up teardown of SpaceXAI's decision to rewrite its training stack in C and C++ found a 4x full-cycle speedup, enough to make a model a month feasible through pipelining alone ([analysis](https://research.33fg.com/analysis/what-spacexai-s-c-rewrite-gamble-buys)), and [Elon Musk](/people/elon-musk.md) added that the bespoke inference stack is not yet plugged in and promised another doubling ([post](https://x.com/elonmusk/status/2074969374843154500)). It is the substrate under [Grok 4.5](/systems/grok-4-5.md), shipped the same day, and the corpus's clearest statement that the cadence of the loop is an engineering variable: it follows Musk's May report that a shipped Grok was [improving every few days](/developments/2026-05-17-models-improve-every-few-days.md) and lands a week after the count of [seventeen frontier leaders reigning about seven weeks each](/developments/2026-07-03-seventeen-leaders-in-two-years.md), a reign a monthly cadence would halve. The next day OpenAI reported that [a model had post-trained a model](/developments/2026-07-10-a-model-post-trains-a-model.md).
