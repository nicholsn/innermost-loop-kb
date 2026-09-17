---
type: AISystem
title: Claude Code
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/anthropic
modality: code
evaluated_on:
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/posttrainbench
description: Anthropic's terminal coding agent, the harness through which the corpus most often watches a model write, ship and post-train software without a human in the loop.
resource: https://claude.com/product/claude-code
sameAs:
  - http://www.wikidata.org/entity/Q138457287
tags:
  - "coding-agent"
sources:
  - { id: iml-2025-12-23, resource: https://theinnermostloop.substack.com/p/welcome-to-december-23-2025, title: "Welcome to December 23, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-23" }
---

Claude Code is Anthropic's command-line agent that runs Claude models against a codebase ([product page](https://claude.com/product/claude-code)). It enters the corpus with a tooling note, [Language Server Protocol support](/developments/2025-12-23-claude-code-lsp.md), but within days becomes the newsletter's central instrument of recursion: its own creator reports it [wrote 200 pull requests without him](/developments/2025-12-27-cherny-200-pull-requests.md), and Anthropic confirms it [wrote the whole Claude Cowork desktop app](/developments/2026-01-13-claude-code-writes-cowork.md) in a week and a half. By March 2026 PostTrainBench v1.0 names [Opus 4.6 running in Claude Code](/developments/2026-03-12-posttrainbench-v1.md) the most capable agent at automating a model's own post-training.
