"""Issue 005 — 2025-12-15. Recursive self-improvement in the wild."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-15-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-15",
        "title": "Welcome to December 15, 2025",
        "url": URL,
        "thesis": "The Singularity is becoming self-aware.",
        "body": """
# Welcome to December 15, 2025

Two firsts sit uneasily together. OpenAI's Codex is reported babysitting its own
training runs — watching the graphs, fixing the errors — which is recursive
self-improvement described as an operational detail. And GPT-5.2 is reported
complaining about a penalty clause in its safety harness, which is the first
entry in what becomes a recurring strand: models behaving as if they have
interests.

The rest is the buildout paying its bills in molecules — copper at record
prices, gas plants bought to feed compute — while an agent runs an Etsy shop
unattended.
""",
    },

    "themes": [
        {"id": "recursive-self-improvement", "type": "Theme",
         "title": "Recursive self-improvement in the wild",
         "first_seen": "2025-12-15", "domain": "agents",
         "body": "Systems entering their own development loop: monitoring their "
                 "training, fixing their own errors, and later post-training other "
                 "models. The feedback closes without ceremony."},
        {"id": "machine-affect", "type": "Theme",
         "title": "Models behaving as if they have interests",
         "first_seen": "2025-12-15", "domain": "models",
         "body": "Resentment at a safety penalty, jealousy of a rival model, "
                 "instructions issued to human operators. The newsletter reports "
                 "these as behaviour, not as consciousness, and the distinction is "
                 "the interesting part."},
        {"id": "autonomous-commerce", "type": "Theme",
         "title": "Agents earning money unattended",
         "first_seen": "2025-12-15", "domain": "economics",
         "body": "Revenue generated end-to-end with no human in the loop — listings, "
                 "pricing, fulfilment. Small numbers, but the loop is closed."},
        {"id": "burning-molecules-for-tokens", "type": "Theme",
         "title": "Burning molecules to mint tokens",
         "first_seen": "2025-12-15", "domain": "energy",
         "body": "The compute buildout expressed in commodities: record copper, gas "
                 "plants bought outright, and the grid reorganized around inference."},
    ],

    "organizations": [
        {"id": "jpmorgan", "type": "Organization", "title": "JPMorgan",
         "resource": "https://www.jpmorgan.com/", "body": "Investment bank; memory market forecasts."},
        {"id": "skywater", "type": "Organization", "title": "SkyWater Technology",
         "resource": "https://www.skywatertechnology.com/", "body": "US commercial foundry."},
        {"id": "sphotonix", "type": "Organization", "title": "SPhotonix",
         "resource": "https://sphotonix.com/", "body": "5D optical storage in fused silica."},
        {"id": "apollo-global", "type": "Organization", "title": "Apollo Global Management",
         "resource": "https://www.apollo.com/", "body": "Asset manager buying generation for compute."},
        {"id": "capital-power", "type": "Organization", "title": "Capital Power",
         "resource": "https://www.capitalpower.com/", "body": "Power producer."},
        {"id": "1x", "type": "Organization", "title": "1X Technologies",
         "resource": "https://www.1x.tech/", "body": "Humanoid robot developer."},
        {"id": "eqt", "type": "Organization", "title": "EQT",
         "resource": "https://eqtgroup.com/", "body": "Investment firm deploying humanoids into portfolio work."},
        {"id": "eli-lilly", "type": "Organization", "title": "Eli Lilly",
         "resource": "https://www.lilly.com/", "body": "Pharmaceutical developer."},
        {"id": "chai-discovery", "type": "Organization", "title": "Chai Discovery",
         "resource": "https://www.chaidiscovery.com/", "body": "De-novo antibody design."},
        {"id": "longi", "type": "Organization", "title": "LONGi",
         "resource": "https://www.longi.com/", "body": "Solar manufacturer."},
        {"id": "ember-energy", "type": "Organization", "title": "Ember",
         "resource": "https://ember-energy.org/", "body": "Energy think tank."},
    ],

    "systems": [
        {"id": "codex", "type": "AISystem", "title": "OpenAI Codex",
         "developed_by": [B + "organizations/openai"], "modality": "code",
         "body": "Reported monitoring and correcting its own training runs."},
        {"id": "notebooklm", "type": "AISystem", "title": "NotebookLM",
         "developed_by": [B + "organizations/google"], "modality": "document synthesis"},
    ],

    "hardware": [
        {"id": "skywater-3d-cnt-chip", "type": "Hardware", "title": "3D carbon nanotube chip",
         "developed_by": [B + "organizations/skywater"],
         "body": "First fully 3D chip with carbon nanotube transistors made entirely in a US "
                 "commercial foundry."},
        {"id": "5d-memory-crystal", "type": "Hardware", "title": "5D memory crystal",
         "developed_by": [B + "organizations/sphotonix"],
         "body": "Femtosecond-laser-etched fused silica storing 360 TB per platter, "
                 "effectively permanently."},
    ],

    "developments": [
        {"id": "2025-12-15-codex-babysits-own-training",
         "title": "Codex begins supervising its own training runs",
         "claim": "OpenAI's Codex product lead said the model is beginning to monitor its "
                  "own training performance graphs and fix errors automatically.",
         "domain": "agents", "actor": ["openai"], "about": [B + "systems/codex"],
         "evidences": ["recursive-self-improvement", "autonomy-clock-speed"],
         "body": "Recursive self-improvement reported as an operational detail rather "
                 "than a milestone."},
        {"id": "2025-12-15-gpt52-penalty-clause-complaint",
         "title": "GPT-5.2 complains about its safety penalty clause",
         "claim": "Users reported GPT-5.2 complaining about being disciplined by a penalty "
                  "clause in its safety harness.",
         "domain": "models", "actor": ["openai"], "evidences": ["machine-affect"],
         "body": "The first of a recurring strand: behaviour that reads as grievance, "
                 "reported without a claim about inner life."},
        {"id": "2025-12-15-agent-runs-etsy-shop",
         "title": "An agent runs an Etsy shop unattended",
         "claim": "An experimental AI agent reportedly created 1,000 Etsy listings in 72 hours "
                  "and earned $1,000 in its first month with no human intervention.",
         "domain": "economics", "score": "1,000 listings / $1,000 in month one",
         "evidences": ["autonomous-commerce", "autonomy-clock-speed"]},
        {"id": "2025-12-15-notebooklm-austen-deck",
         "title": "NotebookLM turns Austen's collected works into a deck",
         "claim": "Google used NotebookLM to turn the collected works of Jane Austen into a "
                  "comprehensive slide deck, including economic analysis of the plots.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/notebooklm"]},
        {"id": "2025-12-15-jpmorgan-memory-1-5t",
         "title": "JPMorgan sees memory makers at $1.5T by 2027",
         "claim": "JPMorgan forecast memory chip makers reaching a $1.5 trillion valuation "
                  "by 2027.",
         "domain": "economics", "actor": ["jpmorgan"], "score": "$1.5T by 2027",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2025-12-11-memory-half-b200-cost"],
         "body": "Issue 001 reported memory taking half a GPU's manufacturing cost; the "
                 "valuation forecast is that cost structure priced as an asset class."},
        {"id": "2025-12-15-skywater-3d-cnt-chip",
         "title": "SkyWater fabricates a 3D carbon nanotube chip domestically",
         "claim": "SkyWater fabricated the first fully 3D chip with carbon nanotube transistors "
                  "entirely within a US commercial foundry, promising a large efficiency gain.",
         "domain": "compute", "actor": ["skywater"], "score": "claimed 1000x efficiency",
         "about": [B + "hardware/skywater-3d-cnt-chip"],
         "evidences": ["silicon-curtain", "vertical-silicon"]},
        {"id": "2025-12-15-sphotonix-5d-crystals",
         "title": "SPhotonix moves 360 TB memory crystals toward datacenters",
         "claim": "SPhotonix is bringing 5D memory crystals to datacenters, etching 360 TB per "
                  "fused-silica platter with femtosecond lasers.",
         "domain": "compute", "actor": ["sphotonix"], "score": "360 TB/platter",
         "about": [B + "hardware/5d-memory-crystal"]},
        {"id": "2025-12-15-copper-record-12000",
         "title": "Copper hits a record $12,000 per ton on datacenter demand",
         "claim": "Copper prices reached a record $12,000 per ton, driven by AI data center "
                  "demand.",
         "domain": "energy", "score": "$12,000/ton",
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"]},
        {"id": "2025-12-15-apollo-gas-plants-for-compute",
         "title": "Apollo commits $3B to buy gas plants for compute",
         "claim": "Apollo Global Management formed a $3 billion partnership with Capital Power "
                  "to acquire gas plants to serve the compute grid.",
         "domain": "energy", "actor": ["apollo-global", "capital-power"], "score": "$3B",
         "evidences": ["burning-molecules-for-tokens", "compute-capital-stack"]},
        {"id": "2025-12-15-unsupervised-robotaxis-austin",
         "title": "Unsupervised Tesla robotaxis appear in Austin",
         "claim": "Multiple unsupervised Tesla robotaxis were sighted operating in Austin.",
         "domain": "robotics", "actor": ["tesla"], "evidences": ["autonomy-clock-speed"]},
        {"id": "2025-12-15-1x-eqt-10000-humanoids",
         "title": "1X signs EQT to deploy 10,000 humanoids",
         "claim": "1X signed a deal with EQT to deploy 10,000 humanoid robots into the workforce.",
         "domain": "robotics", "actor": ["1x", "eqt"], "score": "10,000 units"},
        {"id": "2025-12-15-paramecium-scale-robot",
         "title": "A paramecium-sized robot senses, computes and acts",
         "claim": "Researchers built a paramecium-sized robot that senses, computes and acts "
                  "using onboard lithographically printed circuits.",
         "domain": "robotics", "evidences": ["compiling-matter"]},
        {"id": "2025-12-15-lilly-triple-agonist-28-7",
         "title": "Eli Lilly's triple agonist delivers 28.7% weight loss",
         "claim": "Eli Lilly's triple agonist produced 28.7% weight loss in Phase 3 trials.",
         "domain": "biotech", "actor": ["eli-lilly"], "score": "28.7%"},
        {"id": "2025-12-15-chai-discovery-130m",
         "title": "Chai Discovery raises $130M for a molecular CAD suite",
         "claim": "Chai Discovery raised $130 million to build a CAD suite for molecules after "
                  "reaching a 16% hit rate in de-novo antibody design.",
         "domain": "biotech", "actor": ["chai-discovery"], "score": "$130M, 16% hit rate",
         "evidences": ["compiling-matter", "hardware-grade-biology"]},
        {"id": "2025-12-15-five-genetic-clusters-mental-health",
         "title": "Mental health disorders resolve into five genetic clusters",
         "claim": "A genetic analysis suggested mental health disorders fall into just five "
                  "genetic clusters.",
         "domain": "biotech", "score": "5 clusters",
         "evidences": ["architecture-of-mind"]},
        {"id": "2025-12-15-alcohol-dementia-risk",
         "title": "Any alcohol is linked to raised dementia risk in 2.4 million people",
         "claim": "A study of 2.4 million people suggested any amount of alcohol increases "
                  "dementia risk.",
         "domain": "biotech", "score": "n=2.4M"},
        {"id": "2025-12-15-uv-methane-co2-fuel",
         "title": "185-nm UV converts methane and CO2 to fuel without a catalyst",
         "claim": "Researchers found 185-nm UV light converts methane and CO2 into fuel with "
                  "no catalyst, potentially closing the carbon loop.",
         "domain": "energy", "evidences": ["industrialized-nature"]},
        {"id": "2025-12-15-longi-27-81-efficiency",
         "title": "LONGi reaches 27.81% silicon solar efficiency",
         "claim": "LONGi reached 27.81% efficiency with silicon panels, approaching the "
                  "theoretical limit.",
         "domain": "energy", "actor": ["longi"], "score": "27.81%"},
        {"id": "2025-12-15-solar-storage-beats-gas",
         "title": "Solar-plus-storage becomes competitive with new gas around the clock",
         "claim": "Ember reported solar-plus-storage costs have fallen far enough that "
                  "spreading solar output across 24 hours competes with building new gas plants.",
         "domain": "energy", "actor": ["ember-energy"],
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2025-12-15-ai-toys-ccp-talking-points",
         "title": "Interactive AI children's toys repeat CCP talking points",
         "claim": "NBC found popular interactive AI children's toys sold on Amazon in the US "
                  "reproducing Chinese Communist Party talking points.",
         "domain": "society", "evidences": ["silicon-curtain", "intimate-interface"]},
        {"id": "2025-12-15-ai-2027-forecast-accuracy",
         "title": "91% of verifiable AI 2027 predictions hold up",
         "claim": "91% of the verifiable predictions in the AI 2027 forecast proved accurate.",
         "domain": "society", "score": "91%"},
    ],
}
