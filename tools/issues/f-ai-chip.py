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
         "domain": "compute", "actor": ["architect-labs", "alibaba"],
         "evidences": ["recursive-self-improvement", "silicon-designs-itself", "the-designless-industry"],
         "supersedes": [B + "developments/2026-08-27-a-first-of-authorship-not-assistance"]},
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
