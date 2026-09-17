---
type: Development
title: A Linux developer publishes AI prompts for kernel review
claim: Linux developer Chris Mason released AI prompts for kernel review, putting a model in the loop on the operating system it runs on.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-02-02
actor:
  - https://nicholsn.github.io/innermost-loop-kb/people/chris-mason
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/engineer-as-supervisor
occurred_on: "2026-01-30"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-12-kernel-bugs-found-69pct
description: "The loop reaches below the model into its substrate: a kernel maintainer's own review workflow now includes the model, which the author calls a critical step in recursive self-improvement."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-01-12-torvalds-vibe-codes
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-02-06-500-zero-days-found
  - https://nicholsn.github.io/innermost-loop-kb/people/linus-torvalds
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-02-02"
  - "rsi"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-02-02T00:00:00Z" }
sources:
  - { id: iml-2026-02-02, resource: https://theinnermostloop.substack.com/p/welcome-to-february-2-2026, title: "Welcome to February 2, 2026", author: human:alex-wissner-gross, last_modified: "2026-02-02", supporting_text: AI prompts for kernel review }
  - { id: phoronix-ai-code-review-prompts-linux, resource: https://www.phoronix.com/news/AI-Code-Review-Prompts-Linux, title: AI Code Review Prompts Initiative Making Progress For The Linux Kernel, author: human:michael-larabel, last_modified: "2026-01-30" }
---

Chris Mason, the Btrfs creator, maintains a public repository of prompts ([masoncl/review-prompts](https://github.com/masoncl/review-prompts)) for LLM-assisted review of Linux kernel patches; the update covered by Phoronix on January 30 broke the review into per-chunk tasks with dedicated passes for `Fixes:` tags, past lore threads and syzkaller fixes, which he reported uses fewer tokens and catches more bugs ([Phoronix](https://www.phoronix.com/news/AI-Code-Review-Prompts-Linux)). The newsletter reads it as the [recursive self-improvement](/themes/recursive-self-improvement.md) loop reaching below the model into the operating system it runs on. It follows the finding that [AI fuzzing now surfaces 69% of kernel bugs within a year](/developments/2026-01-12-kernel-bugs-found-69pct.md) and [Torvalds vibe-coding](/developments/2026-01-12-torvalds-vibe-codes.md), and precedes Opus 4.6 finding [500 zero-days in open source](/developments/2026-02-06-500-zero-days-found.md) four days later.
