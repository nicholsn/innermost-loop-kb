---
type: Development
title: Self-improving agents rebuild the inference stack serving two open models
claim: Asari AI's self-improving co-inventor agents rebuilt the inference stack for two open models on B200s, lifting throughput and interactivity up to 16%, while Intology's Locus agent led PostTrainBench by post-training models unsupervised in ten H100-hours and beating human tuners on the harder variant.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-08-04
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/asari-ai
  - https://nicholsn.github.io/innermost-loop-kb/organizations/intology
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/asari-co-inventor
  - https://nicholsn.github.io/innermost-loop-kb/systems/deepseek-v4-pro
  - https://nicholsn.github.io/innermost-loop-kb/systems/glm-5-2
  - https://nicholsn.github.io/innermost-loop-kb/hardware/nvidia-b200
  - https://nicholsn.github.io/innermost-loop-kb/systems/locus
  - https://nicholsn.github.io/innermost-loop-kb/benchmarks/posttrainbench
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/a-model-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/themes/optimizing-its-own-invoice
score: up to 16%
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-08-03-sixteen-days-alone-and-265-commits
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-10-a-model-post-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price
description: "The Singularity filing its own optimization tickets: the loop reaches the serving layer, the last piece of infrastructure between a model and its users, and the post-training pipeline in the same week."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-29-a-model-writes-the-kernels-that-run-it
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-04-agents-write-the-kernels-closing-a-software-gap
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-12-posttrainbench-v1
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-07-10-a-model-post-trains-a-model, relation_label: extends }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-08-04"
  - "rsi"
  - "kernels"
  - "model-trains-model"
  - "autonomous-research"
generated: { by: process:iml-emit, at: "2026-08-04T00:00:00Z" }
sources:
  - { id: iml-2026-08-04, resource: https://theinnermostloop.substack.com/p/welcome-to-august-4-2026, title: "Welcome to August 4, 2026", author: human:alex-wissner-gross, last_modified: "2026-08-04", supporting_text: "DeepSeek v4 Pro and GLM 5.2 on B200s, lifting throughput and interactivity up to 16%" }
  - { id: asari-inference-optimization-blog, resource: https://asari.ai/blog/inference-optimization, title: Speeding up end-to-end inference with self-improving agents, author: org:asari-ai, last_modified: "2026-07-28" }
  - { id: intology-scaling-automated-post-training, resource: https://intology.ai/blog/scaling-automated-post-training, title: Scaling Automated Post-Training, author: org:intology, last_modified: "2026-08-03" }
---

Asari AI's [co-inventor agents](/systems/asari-co-inventor.md) optimized the full vLLM serving stack for [DeepSeek v4 Pro](/systems/deepseek-v4-pro.md) and [GLM 5.2](/systems/glm-5-2.md) on [NVIDIA B200s](/hardware/nvidia-b200.md), improving throughput and interactivity by up to 16% across concurrency levels while preserving model behaviour through distribution-level correctness checks ([Asari blog](https://asari.ai/blog/inference-optimization)). In the same issue Intology's [Locus](/systems/locus.md) took the top of [PostTrainBench](/benchmarks/posttrainbench.md) by post-training models unsupervised in ten H100-hours and beating human tuners on the harder variant ([Intology blog](https://intology.ai/blog/scaling-automated-post-training)), overtaking the [Sol post-trains Luna](/developments/2026-07-10-a-model-post-trains-a-model.md) result of July. Together they extend the loop from [production kernels](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) and [self-evolving harnesses](/developments/2026-08-03-sixteen-days-alone-and-265-commits.md) to the serving stack and the post-training pipeline, two more of the layers between a model and its own next version; four days later Poetiq's [self-optimizing optimizer](/developments/2026-08-08-a-self-optimizing-optimizer.md) makes the same claim for the harness layer.
