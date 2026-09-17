"""Feature — 2026-08-27. The first AI chip designed end-to-end by AI."""
URL = "https://theinnermostloop.substack.com/p/the-first-ai-chip-designed-end-to"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-27", "slug": "feature-ai-chip-designed-by-ai",
        "title": "The First AI Chip Designed End-to-End by AI", "url": URL,
        "thesis": "Two humans wrote a specification; a machine produced the entire chip.",
        "body": """
# The First AI Chip Designed End-to-End by AI

Two human architects wrote a high-level specification. From it, an AI system
generated the performance model, RTL, verification environments, formal proofs,
firmware, drivers and compute kernels — with no human intervention below the
specification and no pre-existing IP. The first drop to hardware had zero bugs.

Earlier systems were firsts of *assistance*. This is a first of *authorship*.
And the model running on the finished chip found optimizations for its own
operations.
""",
    },
    "themes": [
        {"id": "the-designless-industry", "type": "Theme",
         "title": "The design team becomes a specification",
         "first_seen": "2026-08-27", "domain": "compute",
         "body": "Fabless separated design from manufacturing. Designless separates "
                 "intent from design: a customer brings a workload and the chip is "
                 "derived from it, the way a fabless company brings a design and "
                 "wafers come back."},
    ],
    "hardware": [
        {"id": "redwood", "type": "Hardware", "title": "Redwood",
         "description": "Architect Labs' AI inference accelerator, the first designed, verified and "
                        "deployed end-to-end by an AI system from a two-person specification, running "
                        "today on an AMD Versal FPGA.",
         "developed_by": [B + "organizations/architect-labs"],
         "resource": "https://architectlabs.com/",
         "body": "Redwood is the accelerator [Architect Labs](/organizations/architect-labs.md) unveiled "
                 "on 2026-08-27: from a high-level specification written by two human architects, an AI "
                 "system generated its performance model, RTL, UVM verification environments, formal "
                 "proofs, firmware, drivers and compute kernels, closed every block at 95% code and "
                 "functional coverage in under two weeks, and took its first RTL drop to an AMD Versal "
                 "FPGA with zero bugs ([company site](https://architectlabs.com/)). It lives today on "
                 "the FPGA; the silicon figures — a projected Redwood Nano on Samsung 8 nm serving Qwen3 "
                 "at 49 tokens per second against a Jetson Orin Nano's measured 28, at 1.3 W against "
                 "2.6 W — are projections calibrated from FPGA measurements. In this corpus it is the "
                 "product of the [first-of-authorship](/developments/2026-08-27-a-first-of-authorship-not-assistance.md) "
                 "result and the substrate on which [the loop reaches silicon](/developments/2026-08-27-the-loop-reaches-silicon.md): "
                 "[Qwen3](/systems/qwen3.md) running on it found optimizations for its own operations."},
    ],
    "systems": [
        {"id": "qwen3", "type": "AISystem", "title": "Qwen3",
         "description": "Alibaba's 2025 open-weight Qwen3 language-model family, the workload brought "
                        "up on Redwood in its third week and the model that then found optimizations "
                        "for its own operations on the chip.",
         "developed_by": [B + "organizations/alibaba"],
         "modality": "text",
         "resource": "https://arxiv.org/abs/2505.09388",
         "tags": ["open-weight-model"],
         "body": "Qwen3 is the 2025 generation of [Alibaba](/organizations/alibaba.md)'s Qwen model "
                 "family, released with a technical report on arXiv ([paper](https://arxiv.org/abs/2505.09388)); "
                 "later members of the family in this corpus include "
                 "[Qwen3-Max-Thinking](/systems/qwen3-max-thinking.md) and [Qwen3.7-Max](/systems/qwen-3-7-max.md). "
                 "Here it is the workload Architect Labs brought online on [Redwood](/hardware/redwood.md) "
                 "in the accelerator's third week and demonstrated live at the Design Automation "
                 "Conference. Exposed as an endpoint inside the AI system that built the chip, it found "
                 "timing and kernel optimizations for its own operations — the moment the newsletter "
                 "calls [the loop reaching silicon](/developments/2026-08-27-the-loop-reaches-silicon.md)."},
    ],
    "people": [
        {"id": "i-j-good", "type": "Person", "title": "I. J. Good", "name": "I. J. Good",
         "description": "British statistician and Bletchley Park cryptographer who in 1965 imagined a "
                        "machine designing better machines and named the result an intelligence "
                        "explosion.",
         "resource": "https://en.wikipedia.org/wiki/I._J._Good",
         "sameAs": ["http://www.wikidata.org/entity/Q224372"],
         "tags": ["researcher"],
         "body": "Irving John Good (1916–2009) was a British statistician who worked alongside Alan "
                 "Turing at Bletchley Park and, in a 1965 essay on the first ultraintelligent machine, "
                 "described a machine able to design ever better machines, calling the resulting "
                 "runaway an intelligence explosion ([Wikipedia](https://en.wikipedia.org/wiki/I._J._Good)). "
                 "The corpus's [recursive-self-improvement](/themes/recursive-self-improvement.md) theme "
                 "tracks that idea in the wild; the newsletter invokes him by name when "
                 "[the loop reaches silicon](/developments/2026-08-27-the-loop-reaches-silicon.md), "
                 "noting that Good was thinking of software and that a model has now found "
                 "optimizations for its own operations on a chip an AI designed."},
    ],
    "developments": [
        {"id": "2026-08-27-a-first-of-authorship-not-assistance",
         "title": "A specification alone produces a complete, verified accelerator",
         "claim": "Architect Labs unveiled Redwood, an AI accelerator designed, verified and "
                  "deployed end-to-end by an AI system from a high-level specification written by "
                  "two human architects, with no human intervention below the specification and "
                  "no pre-existing or open-source intellectual property, closing every block at "
                  "95% coverage in under two weeks and taking its first hardware drop with zero "
                  "bugs.",
         "domain": "compute", "actor": ["architect-labs"], "score": "2 weeks / zero bugs",
         "evidences": ["silicon-designs-itself", "the-designless-industry", "source-code-becomes-assembly"],
         "body": "Earlier milestones were firsts of assistance — a placement model "
                 "inside a human flow, a processor designed by conversing with a "
                 "chatbot. This is a first of authorship."},
        {"id": "2026-08-27-the-loop-reaches-silicon",
         "title": "A model running on the chip finds optimizations for its own operations",
         "claim": "The model running on Redwood was exposed as an endpoint inside the AI system "
                  "that built it, and found timing and kernel optimizations for its own "
                  "operations — extending to silicon the intelligence explosion I. J. Good "
                  "imagined for software in 1965.",
         "description": "The designer of the chip and the workload running on it become the same "
                        "optimizing system, so the recursion the corpus has tracked through code, "
                        "kernels and training loops closes for the first time through the "
                        "hardware substrate itself.",
         "domain": "compute", "actor": ["architect-labs", "alibaba"],
         "about": [B + "hardware/redwood", B + "systems/qwen3"],
         "evidences": ["recursive-self-improvement", "silicon-designs-itself", "the-designless-industry"],
         "supersedes": [B + "developments/2026-08-27-a-first-of-authorship-not-assistance",
                        B + "developments/2026-04-29-a-model-writes-the-kernels-that-run-it"],
         "relatedTo": [B + "people/i-j-good",
                       B + "developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai",
                       B + "developments/2026-03-20-cpu-designed-in-twelve-hours"],
         "tags": ["rsi", "chip-design", "kernels"],
         "supporting_text": "the model found timing and kernel optimizations for its own operations",
         "sources": [{"id": "architect-labs-site", "resource": "https://architectlabs.com/",
                      "title": "Architect Labs", "author": "org:architect-labs"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Once [Redwood](/hardware/redwood.md) was serving [Qwen3](/systems/qwen3.md) inference "
                 "on its FPGA, [Architect Labs](/organizations/architect-labs.md) exposed the model as "
                 "an endpoint inside the same AI system that had generated the chip's RTL, verification "
                 "and kernels, and the model returned timing and kernel optimizations for its own "
                 "operations ([company site](https://architectlabs.com/)). The newsletter reads this "
                 "against [I. J. Good](/people/i-j-good.md)'s 1965 intelligence explosion — a machine "
                 "designing better machines — noting that Good was thinking of software and that the "
                 "loop now reaches silicon. It is the hardware endpoint of a kernel storyline that runs "
                 "from [a model topping KernelBench for the GPU kernels it runs on](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) "
                 "through [kernels rewritten behind an 80% price cut](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) "
                 "and [a 232-fold kernel speedup](/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup.md), "
                 "and it follows the same issue's [first-of-authorship](/developments/2026-08-27-a-first-of-authorship-not-assistance.md) "
                 "result; the daily issue two days later [records the announcement](/developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai.md). "
                 "The figures are company-reported, the silicon numbers are FPGA-calibrated projections, "
                 "and the author discloses that he advises the company."},
        {"id": "2026-08-27-the-architecture-never-froze",
         "title": "A design absorbs 115 merged changes in a single day",
         "claim": "Any change to the specification is regenerated, reverified and redeployed to "
                  "hardware in under 48 hours, so where a traditional chip program freezes its "
                  "architecture early and defers later ideas to the next generation, this design "
                  "never froze — absorbing 115 merged changes in a single day at its peak.",
         "domain": "compute", "actor": ["architect-labs"], "score": "115 changes in a day",
         "evidences": ["the-designless-industry", "autonomy-clock-speed", "moation"],
         "supersedes": [B + "developments/2026-08-27-the-loop-reaches-silicon"],
         "body": "The mismatch it resolves is one of clocks: an architecture freezes "
                 "years before volume silicon, while the workloads it serves change "
                 "in months."},
        {"id": "2026-08-27-a-chip-for-every-workload-that-matters",
         "title": "Custom silicon falls from $725 million to two people and a machine",
         "claim": "With a 2-nanometer chip's design cost put at roughly $725 million, only 14% of "
                  "chip projects reaching first-silicon success and three-quarters running late, "
                  "Redwood was specified by two people and designed by a machine — and projected "
                  "onto an older process runs the same model at 49 tokens per second against a "
                  "comparable part's 28, at half the power.",
         "domain": "compute", "actor": ["architect-labs", "nvidia"], "score": "$725M vs two people",
         "evidences": ["the-designless-industry", "price-implosion", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-08-27-the-architecture-never-froze"],
         "body": "Silicon figures are company-reported projections calibrated from "
                 "FPGA measurements, not measured silicon."},
    ],
}
