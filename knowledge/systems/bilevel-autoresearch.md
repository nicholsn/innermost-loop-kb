---
type: AISystem
title: Bilevel Autoresearch
description: A two-level autoresearch framework in which an outer loop reads the inner hyperparameter-search loop's code and traces and injects new Python search mechanisms at runtime, both loops running on the same model.
modality: research agent
resource: https://arxiv.org/abs/2603.23420
tags:
  - "research-agent"
sources:
  - { id: iml-2026-03-31, resource: https://theinnermostloop.substack.com/p/welcome-to-march-31-2026, title: "Welcome to March 31, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-31" }
---

Bilevel Autoresearch, by independent researchers Yaonan Qu and Meng Lu ([arXiv](https://arxiv.org/abs/2603.23420)), treats Karpathy's autoresearch loop as itself a research target: the inner loop proposes and tests changes to a GPT pretraining run, while the outer loop diagnoses the inner loop's search behavior and writes new mechanisms drawn from bandits, combinatorial optimization and design of experiments. On Karpathy's GPT pretraining benchmark the outer loop reports a 5x improvement over the inner loop alone (-0.045 vs -0.009 val_bpb) with no stronger meta-level model. It enters the corpus in [the March 31 development](/developments/2026-03-31-bilevel-autoresearch.md) as the point where the recursion stops needing a smarter supervisor, and is the immediate predecessor of Apple's [self-distillation result](/developments/2026-04-05-self-distillation-without-a-teacher.md).
