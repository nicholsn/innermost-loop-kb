---
type: Benchmark
title: SWE-bench Verified
description: OpenAI's human-validated 500-task subset of SWE-bench, the corpus's reference yardstick for agentic software engineering and the saturation clock the newsletter watches.
published_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/openai
measures_capability: resolving real GitHub issues in software repositories
resource: https://openai.com/index/introducing-swe-bench-verified/
tags:
  - "coding-agent"
sources:
  - { id: iml-2025-12-11, resource: https://theinnermostloop.substack.com/p/welcome-to-december-11-2025, title: "Welcome to December 11, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-11" }
---

SWE-bench Verified is the human-validated subset of SWE-bench that OpenAI released in 2024 so that scores reflect solvable, unambiguous GitHub issues ([announcement](https://openai.com/index/introducing-swe-bench-verified/)). The corpus uses it as a clock: the first issue reported Anthropic's models [improving about 2% a month](/developments/2025-12-11-anthropic-swebench-trajectory.md) toward saturation by late 2026, and Epoch AI later found [15% of the score available from prompt restructuring alone](/developments/2025-12-28-epoch-15pct-from-prompting.md). Its harder sibling is [SWE-Bench Pro](/benchmarks/swe-bench-pro.md), where [a self-play bug-repair agent](/developments/2025-12-25-meta-self-play-bug-repair.md) and later frontier models are scored.
