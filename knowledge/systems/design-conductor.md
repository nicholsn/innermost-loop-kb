---
type: AISystem
title: Design Conductor
description: Verkor's autonomous chip-design agent, which applies frontier models to take a semiconductor from a written requirement to verified, tape-out-ready GDSII.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/verkor-ai
modality: silicon design
resource: https://arxiv.org/abs/2603.08716
tags:
  - "coding-agent"
sources:
  - { id: iml-2026-03-20, resource: https://theinnermostloop.substack.com/p/welcome-to-march-20-2026, title: "Welcome to March 20, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-20" }
---

Design Conductor (DC) chains RTL implementation, testbench writing, front-end debugging, timing-closure optimisation and back-end tool interaction into one unattended run. Its demonstration, VerCore, is a complete RISC-V CPU meeting timing at 1.48 GHz on the ASAP7 PDK with a CoreMark of 3261, built in 12 hours from a 219-word specification ([arXiv](https://arxiv.org/abs/2603.08716)). In this corpus it is the system behind [the twelve-hour CPU](/developments/2026-03-20-cpu-designed-in-twelve-hours.md).
