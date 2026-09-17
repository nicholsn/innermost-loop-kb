---
type: AISystem
title: Hyperagents
description: Meta's self-referential agent framework in which a task agent and a self-modifying meta agent form one editable program, instantiated as DGM-Hyperagents.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/meta
modality: code
resource: https://arxiv.org/abs/2603.19461
tags:
  - "open-source"
  - "evolutionary-search"
sources:
  - { id: iml-2026-03-24, resource: https://theinnermostloop.substack.com/p/welcome-to-march-24-2026, title: "Welcome to March 24, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-24" }
---

A hyperagent bundles the agent that solves the task and the meta agent that edits both itself and the task agent into a single program, so the procedure that generates improvements is itself open to modification. The reference implementation, DGM-Hyperagents, extends the Darwin Godel Machine's generate-and-evaluate loop beyond coding to any computable task, and its meta-level gains transfer across domains and accumulate across runs ([arXiv](https://arxiv.org/abs/2603.19461); code on GitHub). In this corpus it is the system behind [hyperagents edit their own mechanism](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md), the formal counterpart to [ALMA](/systems/alma.md)'s meta-learned memory.
