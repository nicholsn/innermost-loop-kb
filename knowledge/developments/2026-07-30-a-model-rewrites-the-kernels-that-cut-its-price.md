---
type: Development
title: A model autonomously rewrites the kernels behind an 80% price cut
claim: OpenAI cut GPT-5.6 Luna prices by 80% and trimmed Terra by 20%, crediting an efficiency campaign in which Sol autonomously rewrote production GPU kernels and its own speculative-decoding drafts, and claiming Luna beats Claude Fable 5 on one agent benchmark at 99% lower cost per task.
domain: economics
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-07-30
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-6-luna
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-6-terra
  - https://nicholsn.github.io/innermost-loop-kb/systems/gpt-5-6-sol
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-fable-5
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/agents-last-exam
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/optimizing-its-own-invoice
  - https://nicholsn.github.io/innermost-loop-kb/themes/price-implosion
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/intelligence-per-watt
score: -80% / -99% per task
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-29-the-first-open-three-trillion-class-model
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-29-a-model-writes-the-kernels-that-run-it
description: "The point where the recursive loop reaches the rate card: an efficiency gain the model engineered for itself is passed straight through as a price cut, collapsing cost and capability into a single process."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-10-a-model-post-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-04-agents-write-the-kernels-closing-a-software-gap
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-16-agent-cuts-its-own-cost-98pct
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-30-compute-could-get-ten-times-more-expensive, relation_label: contradicts }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-07-30"
  - "rsi"
  - "kernels"
  - "self-modification"
generated: { by: process:iml-emit, at: "2026-07-30T00:00:00Z" }
sources:
  - { id: iml-2026-07-30, resource: https://theinnermostloop.substack.com/p/welcome-to-july-30-2026, title: "Welcome to July 30, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-30", supporting_text: Sol autonomously rewrote production GPU kernels and its own speculative-decoding drafts }
  - { id: openai-gpt-5-6-price-performance-frontier, resource: https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/, title: Advancing the price-performance frontier with GPT-5.6, author: org:openai }
  - { id: openai-gpt-5-6-efficiency-campaign, resource: https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/, title: "GPT-5.6: frontier intelligence, efficiency", author: org:openai }
---

OpenAI cut [GPT-5.6 Luna](/systems/gpt-5-6-luna.md) prices by 80% and [Terra](/systems/gpt-5-6-terra.md) by 20%, added a Fast mode running 2.5x quicker for twice the price, and claimed Luna beats [Claude Fable 5](/systems/claude-fable-5.md) on [Agents' Last Exam](/benchmarks/agents-last-exam.md) at 99% lower cost per task ([announcement](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)). The saving is credited to an efficiency campaign in which [Sol](/systems/gpt-5-6-sol.md) autonomously rewrote production GPU kernels and its own speculative-decoding drafts ([efficiency post](https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/)); the newsletter's gloss is that the optimizer is now optimizing its own invoice. It closes the arc opened when [GPT-5.5 topped KernelBench](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) for writing the kernels it runs on, and follows [Sol post-training Luna](/developments/2026-07-10-a-model-post-trains-a-model.md) three weeks earlier. The same issue carries Dwarkesh Patel's counter-argument that [compute could get ten times more expensive](/developments/2026-07-30-compute-could-get-ten-times-more-expensive.md), and two days later OpenAI's finance chief folded the cut into an [abundant-intelligence strategy](/developments/2026-08-01-agents-write-almost-all-output-tokens.md).
