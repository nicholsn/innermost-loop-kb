---
type: Hardware
title: Redwood
description: Architect Labs' AI inference accelerator, the first designed, verified and deployed end-to-end by an AI system from a two-person specification, running today on an AMD Versal FPGA.
developed_by:
  - https://nicholsn.github.io/innermost-loop-kb/organizations/architect-labs
resource: https://architectlabs.com/
sources:
  - { id: iml-feature-ai-chip-designed-by-ai, resource: https://theinnermostloop.substack.com/p/the-first-ai-chip-designed-end-to, title: The First AI Chip Designed End-to-End by AI, author: human:alex-wissner-gross, last_modified: "2026-08-27" }
---

Redwood is the accelerator [Architect Labs](/organizations/architect-labs.md) unveiled on 2026-08-27: from a high-level specification written by two human architects, an AI system generated its performance model, RTL, UVM verification environments, formal proofs, firmware, drivers and compute kernels, closed every block at 95% code and functional coverage in under two weeks, and took its first RTL drop to an AMD Versal FPGA with zero bugs ([company site](https://architectlabs.com/)). It lives today on the FPGA; the silicon figures — a projected Redwood Nano on Samsung 8 nm serving Qwen3 at 49 tokens per second against a Jetson Orin Nano's measured 28, at 1.3 W against 2.6 W — are projections calibrated from FPGA measurements. In this corpus it is the product of the [first-of-authorship](/developments/2026-08-27-a-first-of-authorship-not-assistance.md) result and the substrate on which [the loop reaches silicon](/developments/2026-08-27-the-loop-reaches-silicon.md): [Qwen3](/systems/qwen3.md) running on it found optimizations for its own operations.
