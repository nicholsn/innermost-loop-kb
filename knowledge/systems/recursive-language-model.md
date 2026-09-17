---
type: AISystem
title: Recursive Language Model
description: Inference paradigm from MIT CSAIL, adopted by Prime Intellect, in which a language model treats a long prompt as an external environment and works on it from a persistent Python REPL, decomposing it and recursively calling itself over snippets.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/prime-intellect
  - https://nicholsn.github.io/innermost-loop-kb/organizations/mit
modality: text
resource: https://arxiv.org/abs/2512.24601
tags:
  - "open-source"
sources:
  - { id: iml-2026-01-02, resource: https://theinnermostloop.substack.com/p/welcome-to-january-2-2026, title: "Welcome to January 2, 2026", author: human:alex-wissner-gross, last_modified: "2026-01-02" }
---

Manages its own context through a persistent Python REPL, inspecting and transforming data without human oversight. The RLM was introduced by Alex L. Zhang of MIT CSAIL as a blog post in October 2025 and formalized with Tim Kraska and Omar Khattab in the paper *Recursive Language Models* (arXiv 2512.24601, 31 December 2025), with code released at github.com/alexzhang13/rlm; Prime Intellect made it a central research focus in its 1 January 2026 post. In the corpus it is the system behind [a model taking over its own context](/developments/2026-01-02-prime-intellect-rlm.md) and [handling contexts two orders of magnitude beyond its window](/developments/2026-01-04-rlm-two-orders-of-context.md), the scaffold-level counterpart to the weight-level [end-to-end test-time training](/developments/2025-12-30-stanford-test-time-training.md) of the same week.
