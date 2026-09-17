---
type: Development
title: Agents act as their own data scientists, gaining most by optimizing themselves
claim: Meta's Autodata lets agents be their own data scientists, with the biggest gains coming from optimizing the scientist itself rather than the experiment.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-06-27
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/meta
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/autodata
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/self-authored-scaffolding
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
occurred_on: "2026-06-24"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-26-an-agent-generates-almost-all-its-own-output
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-31-bilevel-autoresearch
description: "An empirical vote for the outer loop: when the largest improvement comes from rewriting the experimenter rather than the experiment, the research agent becomes the most valuable object under optimization."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-25-an-agent-rewrites-its-own-harness
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-07-seventy-two-hours-fifty-experiments
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-06-27"
  - "rsi"
  - "autonomous-research"
  - "agent-harness"
  - "self-modification"
generated: { by: process:iml-emit, at: "2026-06-27T00:00:00Z" }
sources:
  - { id: iml-2026-06-27, resource: https://theinnermostloop.substack.com/p/welcome-to-june-27-2026, title: "Welcome to June 27, 2026", author: human:alex-wissner-gross, last_modified: "2026-06-27", supporting_text: the biggest gains from optimizing the scientist itself }
  - { id: meta-autodata-arxiv, resource: https://arxiv.org/abs/2606.25996, title: "Autodata: An agentic data scientist to create high quality synthetic data", author: org:meta, last_modified: "2026-06-24" }
---

Meta's [Autodata](/systems/autodata.md) paper ([arXiv:2606.25996](https://arxiv.org/abs/2606.25996)) casts the agent as its own data scientist, creating and curating synthetic training data, and reports that the largest gains came not from tuning any one experiment but from improving the agent doing the experimenting. The newsletter files it under 'the tools are now building themselves', two days after [an agent mined its own weaknesses and rewrote its scaffolding](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md). Structurally it restates the lesson of [Bilevel Autoresearch](/developments/2026-03-31-bilevel-autoresearch.md), where the loop that writes the strategies mattered more than any strategy, as a measured finding; three weeks later Weco AI's outer-loop agent [rewriting its inner researcher seven times](/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement.md) makes the same point as the corpus's first sustained evidence of [recursive self-improvement](/themes/recursive-self-improvement.md).
