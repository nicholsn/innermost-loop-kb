---
type: Development
title: A model reverse-engineers a DOS game from raw binary into Rust
claim: Karpathy's autoresearch project autonomously conducts training research on language models, while Codex 5.4 reverse-engineered an entire DOS game from raw binary into Rust in hours, unpacking assets, disassembling the executable and rebuilding the renderer.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-08
actor:
  - https://nicholsn.github.io/innermost-loop-kb/people/andrej-karpathy
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/autoresearch
  - https://nicholsn.github.io/innermost-loop-kb/systems/codex
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/engineer-as-supervisor
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-06-minecraft-clone-in-24-minutes
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-29-karpathy-claude-runs-nanochat
description: The corpus's autoresearch lineage begins here, with a researcher handing the experiment loop itself to agents, paired with a reverse-engineering feat showing coding agents finishing long, multi-stage builds end to end.
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-opus-34x-speedup
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-13-claude-code-writes-cowork
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-08"
  - "autonomous-research"
  - "ai-r-and-d"
generated: { by: process:iml-emit, at: "2026-03-08T00:00:00Z" }
sources:
  - { id: iml-2026-03-08, resource: https://theinnermostloop.substack.com/p/welcome-to-march-8-2026, title: "Welcome to March 8, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-08", supporting_text: Codex 5.4 reverse-engineered an entire DOS game }
  - { id: karpathy-autoresearch-announcement, resource: https://x.com/karpathy/status/2030371219518931079, title: Karpathy announces autoresearch, author: human:andrej-karpathy }
  - { id: ammaar-codex-dos-game-rust, resource: https://x.com/ammaar/status/2030392563534893381, title: Codex 5.4 reverse-engineers a DOS game from raw binary into Rust }
---

Karpathy's [autoresearch](/systems/autoresearch.md) repository sets AI agents loose on single-GPU nanochat training runs, proposing, running and scoring modifications without a human in the loop ([announcement](https://x.com/karpathy/status/2030371219518931079)); the next issue would record [650 experiments in two days](/developments/2026-03-09-autoresearch-650-experiments.md). Alongside it, Codex 5.4 ([Codex](/systems/codex.md)) took a DOS game from raw binary to a Rust rebuild in hours, unpacking assets, disassembling the executable and rewriting the renderer ([thread](https://x.com/ammaar/status/2030392563534893381)). The research loop formalizes the December moment when Karpathy [handed his nanochat optimization to Claude](/developments/2025-12-29-karpathy-claude-runs-nanochat.md), and it seeds the lineage the corpus follows through [Bilevel Autoresearch](/developments/2026-03-31-bilevel-autoresearch.md) and the [72-hour, 50-experiment run](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md) in April.
