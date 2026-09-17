---
type: Development
title: Recursive models handle contexts 100x their window
claim: Recursive Language Models are decomposing problems and calling themselves to handle contexts two orders of magnitude larger than their context windows.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-01-04
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/recursive-language-model
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/scaffolding-over-weights
score: two orders of magnitude
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-02-prime-intellect-rlm
description: "Long context stops being a property of the weights: a scaffold that lets the model program over its own prompt beats both larger windows and existing agent harnesses, which the newsletter reads as what replaces programmers asking programmers for help."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-30-stanford-test-time-training
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-million-token-windows-ship
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-12-alma-agents-design-their-own-memory
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-01-04"
  - "agent-harness"
  - "capability-jump"
generated: { by: process:iml-emit, at: "2026-01-04T00:00:00Z" }
sources:
  - { id: iml-2026-01-04, resource: https://theinnermostloop.substack.com/p/welcome-to-january-4-2026, title: "Welcome to January 4, 2026", author: human:alex-wissner-gross, last_modified: "2026-01-04", supporting_text: to handle contexts two orders of magnitude larger than their windows }
  - { id: rlm-arxiv-paper, resource: https://arxiv.org/abs/2512.24601v1, title: Recursive Language Models, author: org:mit, last_modified: "2025-12-31" }
---

The paper, by Alex L. Zhang, Tim Kraska and Omar Khattab of MIT CSAIL (arXiv 2512.24601, 31 December 2025), treats a long prompt as an external environment: the model examines it from a Python REPL, decomposes it, and recursively calls itself over snippets. RLMs process inputs up to two orders of magnitude beyond the context window, working at the 10M-plus-token scale, and across four long-context tasks improve GPT-5 by a median of 26% over compaction, 130% over CodeAct with sub-calls and 13% over Claude Code at comparable cost, while a post-trained RLM-Qwen3-8B beats its base model by 28.3% ([arXiv](https://arxiv.org/abs/2512.24601)). It supplies the measured result behind [Prime Intellect's adoption of the RLM as the paradigm of 2026](/developments/2026-01-02-prime-intellect-rlm.md) two days earlier, and stands as the scaffold-side answer to long context beside Stanford's weight-side [end-to-end test-time training](/developments/2025-12-30-stanford-test-time-training.md), months before [million-token windows ship](/developments/2026-03-16-million-token-windows-ship.md) as a property of the model itself.
