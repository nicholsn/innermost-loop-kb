---
type: Development
title: An agent mines its weaknesses and rewrites its own scaffolding
claim: A new Self-Harness paradigm lets an agent mine its own weaknesses and rewrite its scaffolding, lifting Terminal-Bench scores by double digits with no human engineers involved.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-06-25
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/self-harness
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/terminal-bench-2
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/self-authored-scaffolding
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/scaffolding-over-weights
score: double digits on Terminal-Bench
occurred_on: "2026-06-08"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-06-24-skills-that-write-themselves
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-05-15-a-meta-system-builds-its-own-harnesses
description: "The newsletter's \"editing its own source code\" moment: the scaffolding layer, until now the last reliably human-authored part of an agent, is rewritten by the agent from its own failure traces, which is what the self-authored-scaffolding theme is named for."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-31-a-model-rewrites-its-own-harness-for-eleven-points
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-24-hyperagents-edit-their-own-mechanism
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-31-harnesses-become-editable-artifacts
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-06-25"
  - "rsi"
  - "self-modification"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-06-25T00:00:00Z" }
sources:
  - { id: iml-2026-06-25, resource: https://theinnermostloop.substack.com/p/welcome-to-june-25-2026, title: "Welcome to June 25, 2026", author: human:alex-wissner-gross, last_modified: "2026-06-25", supporting_text: lets an agent mine its weaknesses and rewrite its scaffolding }
  - { id: self-harness-arxiv, resource: https://arxiv.org/abs/2606.09498, title: "Self-Harness: Harnesses That Improve Themselves", author: human:hangfan-zhang, last_modified: "2026-08-20" }
---

[Self-Harness](/systems/self-harness.md), from Hangfan Zhang and colleagues at the [Shanghai AI Laboratory](/organizations/shanghai-ai-laboratory.md), has the agent mine model-specific failure patterns from its own execution traces, propose minimal harness edits tied to those failures, and keep only the edits that survive regression testing ([arXiv](https://arxiv.org/abs/2606.09498), submitted June 8). Starting from a minimal harness, three base models (MiniMax M2.5, Qwen3.5-35B-A3B and [GLM-5](/systems/glm-5.md)) improved on every held-in and held-out split of [Terminal Bench 2.0](/benchmarks/terminal-bench-2.md), SWE-bench Verified and AppWorld, with relative gains of up to 132% and no human or stronger external agent in the loop. The newsletter leads with it as the Singularity "editing its own source code", and it is the item that gave [the harness writes itself](/themes/self-authored-scaffolding.md) its name. It follows Poetiq's meta-system [building its own harnesses](/developments/2026-05-15-a-meta-system-builds-its-own-harnesses.md) and Meta's [hyperagents](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md), and is followed the next day by Codex [generating 99.8% of its own output tokens](/developments/2026-06-26-an-agent-generates-almost-all-its-own-output.md) and in July by Kimi K3 [rewriting its own Cline harness](/developments/2026-07-31-a-model-rewrites-its-own-harness-for-eleven-points.md) for eleven Terminal Bench points.
