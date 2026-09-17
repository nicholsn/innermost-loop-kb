---
type: Development
title: A lab credits a loop where conduct and capability compound together
claim: SpaceXAI launched Grok 4.5, trained on tens of thousands of GB300s alongside Cursor and served at roughly twice its peers' token efficiency, with Aditya Gupta crediting synthetic environments at scale and a loop in which a smarter model behaves better and better behavior unlocks more intelligence.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-07-09
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/spacex
  - https://nicholsn.github.io/innermost-loop-kb/organizations/xai
  - https://nicholsn.github.io/innermost-loop-kb/organizations/nvidia
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anysphere
  - https://nicholsn.github.io/innermost-loop-kb/people/aditya-gupta
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/grok-4-5
  - https://nicholsn.github.io/innermost-loop-kb/hardware/nvidia-gb300
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/behavior-unlocks-intelligence
  - https://nicholsn.github.io/innermost-loop-kb/themes/alignment-as-moat
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
score: $2/$6 per million tokens
occurred_on: "2026-07-08"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-08-the-transformer-eulogized
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-17-models-improve-every-few-days
description: "Alignment is recast from a tax on capability into a training input: the mechanism credited for a frontier launch is conduct feeding back into intelligence."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-11-xai-cofounder-resigns-warning
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-09-a-training-run-ingests-its-own-benchmark
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less
references:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-20-agi-becomes-a-version-number
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-07-09"
  - "rsi"
  - "alignment"
  - "capability-jump"
generated: { by: process:iml-emit, at: "2026-07-09T00:00:00Z" }
sources:
  - { id: iml-2026-07-09, resource: https://theinnermostloop.substack.com/p/welcome-to-july-9-2026, title: "Welcome to July 9, 2026", author: human:alex-wissner-gross, last_modified: "2026-07-09", supporting_text: "a smarter model behaves better, and better behavior unlocks more intelligence" }
  - { id: xai-grok-4-5-announcement, resource: https://x.ai/news/grok-4-5, title: Introducing Grok 4.5, author: org:xai }
  - { id: aditya-gupta-training-loop-post, resource: https://x.com/adityagupta/status/2074917787445997822, title: Aditya Gupta on what drove Grok 4.5, author: human:aditya-gupta }
  - { id: nvidia-grok-4-5-gb300-post, resource: https://x.com/nvidia/status/2074979063106843131, title: NVIDIA on Grok 4.5 training on GB300s, author: org:nvidia }
---

[Grok 4.5](/systems/grok-4-5.md) launched as SpaceXAI's smartest model, trained on tens of thousands of NVIDIA [GB300s](/hardware/nvidia-gb300.md) alongside Cursor and served at about 80 tokens per second with roughly twice its peers' token efficiency at $2 in and $6 out per million tokens ([announcement](https://x.ai/news/grok-4-5)). Asked how, [Aditya Gupta](/people/aditya-gupta.md) credited synthetic environments at scale and a tight loop in which a smarter model behaves better and better behavior unlocks more intelligence ([post](https://x.com/adityagupta/status/2074917787445997822)), the statement that seeds the [theme of the same name](/themes/behavior-unlocks-intelligence.md). It delivers the 1.5-trillion-parameter Grok 4.5 of Musk's [April roadmap](/developments/2026-04-20-agi-becomes-a-version-number.md), the successor he said in May was [about to start mid-training on coding-tool data](/developments/2026-05-17-models-improve-every-few-days.md), arrives five months after an xAI co-founder [resigned warning that live loops were a year away](/developments/2026-02-11-xai-cofounder-resigns-warning.md), and carries the asterisk that the run [ingested the Cursor codebase, benchmark tasks included](/developments/2026-07-09-a-training-run-ingests-its-own-benchmark.md).
