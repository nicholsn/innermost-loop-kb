---
type: Development
title: Google shows inner optimizers work, via internal RL
claim: Google researchers showed inner optimizers are remarkably effective, developing internal RL in which a higher-order model explores a base model's internal representations to learn from sparse rewards.
domain: models
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2025-12-27
actor:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/google
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/machine-introspection
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-24-gemma-scope-2-saes
description: "A construct AI-safety theory had treated as a hazard, an optimizer running inside the model, is reported as a working training method: the machine's internal monologue optimizing itself."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2025-12-21-anthropic-activation-oracles
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-04-09-in-place-test-time-training
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2025-12-27"
  - "rsi"
  - "interpretability"
generated: { by: process:iml-emit, at: "2025-12-27T00:00:00Z" }
sources:
  - { id: iml-2025-12-27, resource: https://theinnermostloop.substack.com/p/welcome-to-december-27-2025, title: "Welcome to December 27, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-27", supporting_text: a higher-order model explores the internal representations of a base model }
  - { id: arxiv-internal-rl-temporal-abstractions, resource: https://arxiv.org/abs/2512.20605, title: Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning, author: org:google, last_modified: "2025-12-24" }
---

The paper ([arXiv:2512.20605](https://arxiv.org/abs/2512.20605), Kobayashi, von Oswald and colleagues at Google) trains a higher-order, non-causal sequence model whose outputs steer the residual-stream activations of a base autoregressive model, compressing long activation chunks into internal controllers with learned termination conditions; reinforcing those controllers directly, which the authors call internal RL, learns from sparse rewards on grid-world and MuJoCo tasks where standard RL fine-tuning fails. The newsletter reads it as the 'inner optimizers' long theorized by safety researchers turning out to be remarkably effective. It sits in the [machine-introspection](/themes/machine-introspection.md) strand after Anthropic's [Activation Oracles](/developments/2025-12-21-anthropic-activation-oracles.md) and DeepMind's [Gemma Scope 2](/developments/2025-12-24-gemma-scope-2-saes.md): where those read a model's internals, this one acts in them, a step toward models that [rewrite their own weights in flight](/developments/2026-04-09-in-place-test-time-training.md).
