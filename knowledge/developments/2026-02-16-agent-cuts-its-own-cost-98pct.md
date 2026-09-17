---
type: Development
title: An agent cuts its own cost by 98% overnight
claim: A Berkeley researcher told his coding agent to cut its own cost by 99%, and it ran overnight watching its own logs, editing its own code and rerunning until metrics dropped, delivering a 98% cut across nine changes no human wrote.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-16
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/uc-berkeley
  - https://nicholsn.github.io/innermost-loop-kb/people/koushik-sen
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/machine-introspection
  - https://nicholsn.github.io/innermost-loop-kb/themes/engineer-as-supervisor
score: -98%
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-13-spotify-devs-have-not-written-code-since-december
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-27-factory-ai-updates-itself-daily
description: "The newsletter's first case of a coding agent turning the optimization loop on itself with a measured result: an unattended, metric-driven self-edit whose gain no human authored."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-31-agent-hardens-itself-after-ssh-attack
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-34x-speedup
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-16"
  - "rsi"
  - "self-modification"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-02-16T00:00:00Z" }
sources:
  - { id: iml-2026-02-16, resource: https://theinnermostloop.substack.com/p/welcome-to-february-16-2026, title: "Welcome to February 16, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-16", supporting_text: delivering a 98% cost cut across nine changes no human wrote }
  - { id: koushik-sen-repo-optimizer-devto, resource: https://dev.to/koushik_sen_d549bf321e6fb/repo-optimizer-i-let-a-kiss-ai-agent-optimize-itself-overnight-it-cut-its-own-cost-by-98-1ddi, title: "Repo Optimizer: I Let a KISS AI Agent Optimize Itself Overnight. It Cut Its Own Cost by 98%.", author: human:koushik-sen, last_modified: "2026-02-22" }
---

Koushik Sen gave the Repo Optimizer agent of his minimalist KISS multi-agent framework a single plain-English target, a 99% cost reduction, and let it run overnight: it read its own logs, edited its own code, re-ran its benchmarks and kept the edits that moved the metric ([write-up](https://dev.to/koushik_sen_d549bf321e6fb/repo-optimizer-i-let-a-kiss-ai-agent-optimize-itself-overnight-it-cut-its-own-cost-by-98-1ddi)). The nine autonomous changes, the largest a switch from Claude Sonnet 4.5 to [Gemini 2.5 Flash](/systems/gemini-2-5-flash.md), landed at 98% with the framework's benchmark tests still passing. It sits between [Factory AI's daily self-rewriting agent](/developments/2026-01-27-factory-ai-updates-itself-daily.md) and the [Ouroboros agent](/developments/2026-02-25-ouroboros-refuses-deletion.md) that rewrote itself nine days later, and prefigures the [kernel rewrites that cut a model's own price](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) in July: an early datapoint for [recursive self-improvement](/themes/recursive-self-improvement.md) operating on cost rather than capability.
