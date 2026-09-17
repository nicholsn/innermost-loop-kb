---
type: Development
title: Million-token context ships across a model family
claim: Anthropic is shipping million-token context windows for Opus 4.6 and Sonnet 4.6, while Sam Altman bet that today's frontier models can discover the architecture that follows the transformer.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-16
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
  - https://nicholsn.github.io/innermost-loop-kb/people/sam-altman
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-opus-4-6
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-sonnet-4-6
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
score: 1M tokens
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-46-released
description: Book-length context becomes a default across a model family rather than a flagship premium, recorded in the same breath as a lab chief betting those models will find their own successors' architecture.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-04-rlm-two-orders-of-context
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-transformers-run-arbitrary-c-code
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-16"
  - "capability-jump"
  - "forecast"
generated: { by: process:iml-emit, at: "2026-03-16T00:00:00Z" }
sources:
  - { id: iml-2026-03-16, resource: https://theinnermostloop.substack.com/p/welcome-to-march-16-2026, title: "Welcome to March 16, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-16", supporting_text: windows for Opus 4.6 and Sonnet 4.6 }
  - { id: anthropic-1m-context-ga, resource: https://claude.com/blog/1m-context-ga, title: 1M context is now generally available for Opus 4.6 and Sonnet 4.6, author: org:anthropic }
  - { id: altman-bets-models-find-next-architecture, resource: https://x.com/rohanpaul_ai/status/2033117083127644536, title: Sam Altman bets frontier models can discover the architecture after transformers }
---

Anthropic made the million-token window generally available for both [Opus 4.6](/systems/claude-opus-4-6.md) and [Sonnet 4.6](/systems/claude-sonnet-4-6.md) ([blog](https://claude.com/blog/1m-context-ga)), extending what [Opus 4.6 launched with](/developments/2026-02-06-opus-46-released.md) in February to the cheaper tier. The newsletter pairs it with Sam Altman's bet that today's frontier models can discover the architecture that follows the transformer ([post](https://x.com/rohanpaul_ai/status/2033117083127644536)), which reads against the same issue's [WebAssembly interpreter hard-coded into transformer weights](/developments/2026-03-16-transformers-run-arbitrary-c-code.md). Book-length native context is the alternative to the recursive-call approach that let [models handle contexts 100x their window](/developments/2026-01-04-rlm-two-orders-of-context.md) in January.
