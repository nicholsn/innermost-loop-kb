---
type: AISystem
title: Asari co-inventor agents
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/asari-ai
modality: research agent
description: Asari AI's self-improving agents for designing and optimizing high-performance infrastructure, which rebuilt the vLLM inference stack serving two open models on B200s.
resource: https://asari.ai/blog/inference-optimization
tags:
  - "research-agent"
sources:
  - { id: iml-2026-08-04, resource: https://theinnermostloop.substack.com/p/welcome-to-august-4-2026, title: "Welcome to August 4, 2026", author: human:alex-wissner-gross, last_modified: "2026-08-04" }
---

Asari AI calls its agents co-inventors: self-improving systems that design and optimize high-performance infrastructure through a rigorous improvement process. In this corpus they appear once, [rebuilding the inference stack](/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on.md) for [DeepSeek v4 Pro](/systems/deepseek-v4-pro.md) and [GLM 5.2](/systems/glm-5-2.md) on [NVIDIA B200s](/hardware/nvidia-b200.md) running vLLM, lifting throughput and interactivity by up to 16% while preserving model behaviour through distribution-level correctness checks ([Asari blog](https://asari.ai/blog/inference-optimization)).
