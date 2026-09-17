"""Issue 138 — 2026-06-13. The Singularity becomes export controlled."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-13-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-13", "title": "Welcome to June 13, 2026", "url": URL,
        "thesis": "A government switches off a frontier model for every foreign national.",
        "body": """
# Welcome to June 13, 2026

The US issued an export-control directive suspending all foreign-national
access to Fable 5 and Mythos 5, forcing Anthropic to disable both models for
hundreds of millions of users — while the lab disputed that a narrow jailbreak
justified recalling them.

Dean Ball caught the irony: because the lab's own non-US staff can no longer
touch the models, this is accidentally the first regulation on recursive
self-improvement.
""",
    },
    "themes": [
        {"id": "models-as-munitions", "type": "Theme",
         "title": "Model access as export control",
         "first_seen": "2026-06-13", "domain": "policy",
         "body": "Capability regulated not by what a model may do but by who may "
                 "touch it. The nationality of the user becomes the control surface, "
                 "and a lab's own foreign staff fall inside the blast radius."},
        {"id": "instruments-lag-the-models", "type": "Theme",
         "title": "The measurements were wrong, not the models",
         "first_seen": "2026-06-13", "domain": "benchmarks",
         "body": "When an AI audit finds errors in 42% of a benchmark's problems and "
                 "every score jumps on correction, the apparent plateau was an "
                 "artifact of the ruler. Capability that looked slow was already there."},
    ],
    "organizations": [
        {"id": "infineon", "type": "Organization", "title": "Infineon"},
        {"id": "nygc", "type": "Organization", "title": "New York Genome Center"},
        {"id": "switzerland", "type": "Organization", "title": "Switzerland"},
        {"id": "kpmg", "type": "Organization", "title": "KPMG"},
    ],
    "developments": [
        {"id": "2026-06-13-a-model-becomes-export-controlled",
         "title": "A government suspends all foreign-national access to a frontier model",
         "claim": "The US issued an export-control directive suspending all foreign-national "
                  "access to Fable 5 and Mythos 5 on national security grounds, forcing "
                  "Anthropic to disable both models for hundreds of millions of users while the "
                  "lab disputed that a narrow jailbreak justified recalling them.",
         "domain": "policy", "actor": ["white-house", "anthropic"],
         "evidences": ["models-as-munitions", "silicon-curtain", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-06-10-mythos-on-a-leash"],
         "body": "Because the lab's own non-US staff can no longer touch the models, "
                 "one analyst noted this is accidentally the first regulation on "
                 "recursive self-improvement — a brake arrived by side effect rather "
                 "than by design."},
        {"id": "2026-06-13-a-benchmark-was-wrong-in-42-percent-of-problems",
         "title": "An AI audit finds errors in 42% of a benchmark's problems",
         "claim": "Epoch AI shipped a v2 of FrontierMath after an AI audit corrected errors in "
                  "42% of problems, and scores leapt across the board, with GPT-5.5-xhigh "
                  "reaching 85% on Tiers 1-3 and its Tier 4 result jumping from 35% to 73%, "
                  "while the now-disabled Fable 5 had already topped the board at 88% on Tier 4.",
         "domain": "benchmarks", "actor": ["epoch-ai", "openai", "anthropic"],
         "score": "42% of problems wrong; Tier 4 35% to 73%",
         "evidences": ["instruments-lag-the-models", "models-audit-their-benchmarks",
                       "benchmark-saturation"],
         "supersedes": [B + "developments/2026-06-10-a-clean-sweep-of-the-boards"],
         "body": "One Epoch researcher noted this finally explains why systems felt slow "
                 "at proofs while quietly cracking open problems: mathematics was "
                 "actually cooked months ago."},
        {"id": "2026-06-13-seventy-five-projects-blocked-in-a-quarter",
         "title": "Opponents block or delay 75 datacenter projects worth $130B in one quarter",
         "claim": "Opponents blocked or delayed at least 75 data-center projects worth about "
                  "$130 billion in the first quarter, the most in any quarter since tracking "
                  "began in 2023, with grassroots groups more than doubling to 833 across 49 "
                  "states.",
         "domain": "policy", "score": "75 projects / $130B / 833 groups",
         "evidences": ["infrastructure-crowding-out", "regulatory-exit", "violence-arrives"],
         "supersedes": [B + "developments/2026-06-10-a-city-pauses-and-a-grid-pays-back"]},
        {"id": "2026-06-13-a-five-billion-euro-power-fab",
         "title": "Europe opens its largest-ever power-semiconductor investment",
         "claim": "Infineon prepares to open a €5 billion Dresden power-semiconductor fab backed "
                  "by roughly €1 billion in EU Chips Act subsidies, to make the power "
                  "semiconductors feeding AI data centers, while windfall AI bonuses turned "
                  "Samsung's factory town of Dongtan into a luxury hotspot.",
         "domain": "compute", "actor": ["infineon", "european-union", "samsung"], "score": "€5B",
         "evidences": ["science-as-industrial-policy", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-06-09-a-two-hundred-ninety-five-billion-domestic-stack"]},
        {"id": "2026-06-13-the-bottleneck-shifts-to-orchestration",
         "title": "A rival hands over a whole campus after hitting network walls",
         "claim": "SpaceX handed the full capacity of its Memphis Colossus 1 to Anthropic after "
                  "its own teams hit latency and aging-network walls that made training Grok "
                  "across three campuses impractical, shifting the bottleneck from owning "
                  "compute to orchestrating it.",
         "domain": "compute", "actor": ["spacex", "xai", "anthropic"],
         "evidences": ["coordination-tax", "network-over-node", "orchestration-not-construction"],
         "supersedes": [B + "developments/2026-06-12-a-lab-leases-its-own-datacenters"]},
        {"id": "2026-06-13-a-crewed-aircraft-on-solid-state-batteries",
         "title": "The first crewed fixed-wing flight on solid-state batteries",
         "claim": "Test pilot Miguel Iturmendi flew the Helios Horizon, the first crewed "
                  "fixed-wing aircraft on solid-state batteries, on cells reaching 410 Wh/kg, a "
                  "60% leap over its previous lithium-ion pack.",
         "domain": "energy", "score": "410 Wh/kg, +60%",
         "evidences": ["industrialized-nature", "physical-recursion"],
         "supersedes": [B + "developments/2026-06-12-solar-outproduces-coal"]},
        {"id": "2026-06-13-car-t-at-a-third-the-price",
         "title": "A country becomes a medical-tourism hub at a third the price",
         "claim": "China is becoming a medical-tourism hub, offering CAR-T cancer therapy for "
                  "$150,000 against up to $475,000 in the United States, while the New York "
                  "Genome Center's SeqTag profiles transcriptome, chromatin and histone marks "
                  "at once to model how cell identity decays with age.",
         "domain": "biotech", "actor": ["china", "nygc"], "score": "$150K vs $475K",
         "evidences": ["hardware-grade-biology", "longevity-escape-velocity"],
         "supersedes": [B + "developments/2026-06-10-partial-reprogramming-reaches-a-patient"]},
        {"id": "2026-06-13-chromatin-shredded-in-p53-mutant-cancers",
         "title": "CRISPR is used to shred the chromatin of p53-mutant cancer cells",
         "claim": "The Innovative Genomics Institute used CRISPR-Cas12a2 to shred the chromatin "
                  "of cancer cells carrying mutated p53, a flaw in nearly half of all cancers, "
                  "while sparing healthy tissue.",
         "domain": "biotech", "actor": ["igi"], "score": "~50% of cancers",
         "evidences": ["hardware-grade-biology", "compiling-matter"],
         "supersedes": [B + "developments/2026-06-07-embryos-base-edited-without-crispr-damage"]},
        {"id": "2026-06-13-junior-postings-up-as-hiring-collapses",
         "title": "Junior postings rise 47% while junior hiring falls 73%",
         "claim": "The computer-science degree survives but its entry-level pipeline does not, "
                  "with junior postings up 47% while hiring fell 73%, as Switzerland votes on "
                  "capping its population at 10 million on the implicit wager that an automated "
                  "economy can prosper without importing workers.",
         "domain": "economics", "actor": ["switzerland"], "score": "+47% postings / -73% hires",
         "evidences": ["ladder-pulled-up", "work-displaced", "oral-tradition-dissolves"],
         "supersedes": [B + "developments/2026-06-09-ai-majors-go-from-five-to-seventy-four"]},
        {"id": "2026-06-13-a-consultancy-report-padded-with-hallucinations",
         "title": "A consultancy's AI adoption report is padded with fabricated case studies",
         "claim": "A KPMG report on AI adoption was padded with bogus case studies built on AI "
                  "hallucinations, while Meta told staff it will cap AI token usage and steer "
                  "engineers toward its own internal tooling after forecasting internal AI "
                  "spending in the billions.",
         "domain": "economics", "actor": ["kpmg", "meta"],
         "evidences": ["deskilling", "gaming-the-token-metric"],
         "supersedes": [B + "developments/2026-06-12-agents-reach-for-your-wallet"]},
        {"id": "2026-06-13-the-first-trillionaire",
         "title": "A public listing creates the world's first trillionaire",
         "claim": "SpaceX debuted on the Nasdaq up 19%, raising a record $75 billion at a $1.77 "
                  "trillion valuation, making Elon Musk the world's first trillionaire at $1.05 "
                  "trillion, more than the next five richest combined.",
         "domain": "economics", "actor": ["spacex", "nasdaq"], "score": "$75B raised / $1.05T",
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-06-12-the-largest-ipo-ever-funds-orbital-compute"]},
    ],
}
