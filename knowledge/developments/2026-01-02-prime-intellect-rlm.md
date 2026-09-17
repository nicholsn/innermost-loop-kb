---
type: Development
title: A model takes over its own context via a Python REPL
claim: Prime Intellect unveiled a Recursive Language Model that manages its own context through a persistent Python REPL, inspecting and transforming data end-to-end without human oversight.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-01-02
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/prime-intellect
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/recursive-language-model
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/scaffolding-over-weights
  - https://nicholsn.github.io/innermost-loop-kb/themes/architecture-of-mind
description: "The human leaves the context window: a lab names as its paradigm for 2026 a scheme in which the model, not the operator, decides what enters its own working memory."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-30-stanford-test-time-training
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-12-alma-agents-design-their-own-memory
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-16-million-token-windows-ship
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-01-02"
  - "agent-harness"
  - "rsi"
generated: { by: process:iml-emit, at: "2026-01-02T00:00:00Z" }
sources:
  - { id: iml-2026-01-02, resource: https://theinnermostloop.substack.com/p/welcome-to-january-2-2026, title: "Welcome to January 2, 2026", author: human:alex-wissner-gross, last_modified: "2026-01-02", supporting_text: manages its own context via a persistent Python REPL }
  - { id: prime-intellect-rlm-blog, resource: https://www.primeintellect.ai/blog/rlm, title: "Recursive Language Models: the paradigm of 2026", author: org:prime-intellect, last_modified: "2026-01-01" }
---

Prime Intellect's research post of 1 January 2026, *Recursive Language Models: the paradigm of 2026*, calls the RLM the simplest and most flexible form of context folding: instead of ingesting its input, the model uses a persistent Python REPL to inspect and transform the data and to call sub-models from inside the REPL, so PDFs, datasets or videos never have to be loaded into the context at all ([blog](https://www.primeintellect.ai/blog/rlm)). The post credits the idea to Alex Zhang's October 2025 blog post and the MIT paper published the day before, and says the RLM is now a major focus of the lab's research; the corpus records the paper's own result, [contexts two orders of magnitude beyond the window](/developments/2026-01-04-rlm-two-orders-of-context.md), two days later. In the [recursive-self-improvement trajectory](/themes/recursive-self-improvement.md) it is the first entry in which a model administers its own working memory, the scaffold-side twin of Stanford's [end-to-end test-time training](/developments/2025-12-30-stanford-test-time-training.md) and a precursor of agents that [meta-learn their own memory architecture](/developments/2026-02-12-alma-agents-design-their-own-memory.md).
