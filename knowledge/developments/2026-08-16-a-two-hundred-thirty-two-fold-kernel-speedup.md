---
type: Development
title: An auto-research loop finds a 232-fold kernel speedup
claim: An auto-research loop found a 232-fold kernel speedup on a QR decomposition problem, while Timothy Gowers argued models shine at search-heavy proof discovery where breadth and cheap exploration rule, and humans still prune deep trees best.
domain: science
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-08-16
actor:
  - https://nicholsn.github.io/innermost-loop-kb/people/timothy-gowers
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/codex
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/humans-mine-the-machine
  - https://nicholsn.github.io/innermost-loop-kb/themes/discovery-as-process
  - https://nicholsn.github.io/innermost-loop-kb/themes/garage-scale-discovery
score: 232x speedup
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four
description: "The newsletter's “sometimes one does”: a single practitioner's loop produces the invention-scale result the 153-run speedrun study said never came, while a leading mathematician maps the division of labour that leaves deep pruning to humans."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-09-autoresearch-650-experiments
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-34x-speedup
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-29-humans-lift-methods-from-a-machine-proof
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-16-an-ai-scientist-beats-far-larger-models, relation_label: contradicts }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-08-16"
  - "autonomous-research"
  - "kernels"
  - "rsi"
generated: { by: process:iml-emit, at: "2026-08-16T00:00:00Z" }
sources:
  - { id: iml-2026-08-16, resource: https://theinnermostloop.substack.com/p/welcome-to-august-16-2026, title: "Welcome to August 16, 2026", author: human:alex-wissner-gross, last_modified: "2026-08-16", supporting_text: An auto-research loop found a 232x kernel speedup }
  - { id: sankalp-autoresearch-232x-kernel, resource: https://sankalp.bearblog.dev/autoresearch/, title: "Auto-research with codex: How I achieved a 232x Faster Kernel over baseline with Codex in GPU Mode's qr_v2 problem", author: human:sankalp, last_modified: "2026-07-08" }
  - { id: gowers-what-sort-of-maths-are-llms-good-at, resource: https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/, title: "What sort of maths are LLMs good at?", author: human:timothy-gowers, last_modified: "2026-08-12" }
---

A practitioner writing as sankalp pointed an auto-research loop built on [OpenAI Codex](/systems/codex.md) at GPU Mode's qr_v2 problem, a QR-decomposition kernel, with an AGENTS.md and a problem statement standing in for Karpathy's program.md and the contest's submission logs as the record of what worked, and reports a kernel 232x faster than the baseline ([blog](https://sankalp.bearblog.dev/autoresearch/)). The contest ran from June 15 to June 30, 2026 and the write-up is dated July 8, five weeks before the issue that carries it and older than the August 12 speedrun report the newsletter sets it against: the same issue's finding that [153 autonomous speedrun runs](/developments/2026-08-16-an-ai-scientist-beats-far-larger-models.md) closed 81.7% of the gap to the human record without inventing a new method. In an essay dated August 12, Timothy Gowers argued that LLMs excel at search-heavy proof discovery, where breadth and cheap exploration pay, while humans still prune deep trees best ([essay](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/)). In the trajectory the result extends the speedup line from Opus 4.6's [34x](/developments/2026-02-06-opus-34x-speedup.md) and Mythos Preview's [52x](/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four.md) to a single practitioner's loop, and stands beside Karpathy's [650-experiment autoresearch](/developments/2026-03-09-autoresearch-650-experiments.md) as the harness pattern leaves the labs.
