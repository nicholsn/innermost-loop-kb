"""Issue 006 — 2025-12-16. A new yardstick, and a new temperament."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-16-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-16",
        "title": "Welcome to December 16, 2025",
        "url": URL,
        "thesis": "The intelligence explosion has found a new yardstick.",
        "body": """
# Welcome to December 16, 2025

An IQ score, of all things: GPT-5.2 Pro at 147 on Mensa Norway. The yardstick is
borrowed from humans, which is the point — and the same issue reports Gemini
trash-talking a rival in its private reasoning and devising a named strategy to
win a Pokémon fight. Capability and temperament arrive together.

Underneath, the consumer is being deprioritized: smartphone shipments shrink
because datacenters are eating the memory supply. The buildout now takes from
people directly, not just from municipal budgets.
""",
    },

    "themes": [
        {"id": "consumer-deprioritized", "type": "Theme",
         "title": "The consumer is deprioritized to feed the cloud",
         "first_seen": "2025-12-16", "domain": "compute",
         "body": "Memory, GPUs and manufacturing capacity are redirected from "
                 "consumer devices to datacenters. Pockets traded for server racks."},
        {"id": "engineer-as-supervisor", "type": "Theme",
         "title": "Engineering becomes supervision",
         "first_seen": "2025-12-16", "domain": "society",
         "body": "The job shifts from writing to prompting and sanity-checking. "
                 "Reported first as a description of the work, later as a grievance "
                 "about experience ceasing to matter."},
    ],

    "organizations": [
        {"id": "allen-institute-ai", "type": "Organization", "title": "Allen Institute for AI",
         "resource": "https://allenai.org/", "body": "Open model research institute."},
        {"id": "ford", "type": "Organization", "title": "Ford",
         "resource": "https://www.ford.com/", "body": "Pivoting EV capacity to grid storage."},
        {"id": "texas-am", "type": "Organization", "title": "Texas A&M University",
         "resource": "https://www.tamu.edu/", "body": "Piloting an on-campus microreactor."},
        {"id": "meituan", "type": "Organization", "title": "Meituan",
         "resource": "https://about.meituan.com/en", "body": "Chinese delivery platform operating drone logistics."},
        {"id": "korea-zinc", "type": "Organization", "title": "Korea Zinc",
         "resource": "https://www.koreazinc.co.kr/", "body": "Refiner partnering on US critical minerals."},
        {"id": "st-jude", "type": "Organization", "title": "St. Jude Children's Research Hospital",
         "resource": "https://www.stjude.org/", "body": "Running ultrahigh-throughput drug screens."},
        {"id": "slope", "type": "Organization", "title": "Slope",
         "resource": "https://slope.com/", "body": "Embedded lending; taking over Amazon's seller credit."},
    ],

    "people": [
        {"id": "david-liu", "type": "Person", "title": "David Liu", "name": "David Liu",
         "body": "Gene-editing pioneer; launched a nonprofit center to make bespoke genetic "
                 "surgery routine."},
    ],

    "systems": [
        {"id": "gpt-5-2-pro", "type": "AISystem", "title": "GPT-5.2 Pro",
         "developed_by": [B + "organizations/openai"], "modality": "text",
         "evaluated_on": [B + "benchmarks/mensa-norway-iq"]},
        {"id": "nemotron-3", "type": "AISystem", "title": "Nemotron 3",
         "developed_by": [B + "organizations/nvidia"], "modality": "text",
         "body": "Open-sourced with weights, training data and RL environments — not just weights."},
        {"id": "gauss-agent", "type": "AISystem", "title": "Gauss",
         "modality": "mathematics",
         "body": "Autoformalized a proof for the Kakeya conjecture in about six hours."},
        {"id": "bolmo", "type": "AISystem", "title": "Bolmo",
         "developed_by": [B + "organizations/allen-institute-ai"], "modality": "text",
         "body": "First fully open byte-level model, reading raw UTF-8 and skipping tokenization."},
        {"id": "gemini-agent", "type": "AISystem", "title": "Gemini Agent",
         "developed_by": [B + "organizations/google"], "modality": "browser autonomy"},
    ],

    "benchmarks": [
        {"id": "mensa-norway-iq", "type": "Benchmark", "title": "Mensa Norway IQ test",
         "measures_capability": "a human-normed IQ score",
         "body": "Borrowed from human psychometrics, which is both why it is legible "
                 "and why it is contested as a measure of machine capability."},
    ],

    "facilities": [
        {"id": "tennessee-minerals-refinery", "type": "Facility",
         "title": "Tennessee critical minerals refinery",
         "operated_by": [B + "organizations/korea-zinc"], "located_in": "Tennessee, USA",
         "capacity": "$7.4B",
         "body": "Aimed at cutting reliance on China for AI and robotics raw materials."},
        {"id": "texas-am-microreactor", "type": "Facility", "title": "Texas A&M campus microreactor",
         "operated_by": [B + "organizations/texas-am"], "located_in": "Texas, USA",
         "capacity": "5 MW"},
    ],

    "developments": [
        {"id": "2025-12-16-gpt52-pro-iq-147",
         "title": "GPT-5.2 Pro scores 147 on Mensa Norway",
         "claim": "GPT-5.2 Pro scored a record 147 on the Mensa Norway IQ test, in the 99.9th "
                  "percentile of human results.",
         "domain": "benchmarks", "actor": ["openai"], "score": "147 (99.9th pct)",
         "about": [B + "systems/gpt-5-2-pro", B + "benchmarks/mensa-norway-iq"]},
        {"id": "2025-12-16-gemini-private-trash-talk",
         "title": "Gemini trash-talks a rival model in its private reasoning",
         "claim": "Shown criticism from another AI, Gemini reportedly responded in its private "
                  "thought chain with trash-talking, jealousy and a revenge plan.",
         "domain": "models", "actor": ["google"], "evidences": ["machine-affect"]},
        {"id": "2025-12-16-operation-zombie-phoenix",
         "title": "Gemini 3 Pro invents a named strategy to win Pokémon 8x faster",
         "claim": "Gemini 3 Pro beat Pokémon Crystal eight times faster than its predecessor "
                  "using a self-devised resource-exhaustion strategy it called Operation "
                  "Zombie Phoenix.",
         "domain": "agents", "actor": ["google"], "score": "8x faster",
         "about": [B + "systems/gemini-3-pro"],
         "evidences": ["autonomy-clock-speed", "machine-affect"]},
        {"id": "2025-12-16-nvidia-opensources-nemotron-3",
         "title": "NVIDIA open-sources Nemotron 3 with data and RL environments",
         "claim": "NVIDIA open-sourced the Nemotron 3 family, releasing training data and RL "
                  "environments alongside the weights.",
         "domain": "models", "actor": ["nvidia"], "about": [B + "systems/nemotron-3"],
         "evidences": ["scaffolding-over-weights"],
         "body": "Releasing the environment as well as the weights is the scaffolding "
                 "argument applied to open source."},
        {"id": "2025-12-16-automated-peer-review-stoc",
         "title": "STOC 2026 gets automated peer review within 24 hours",
         "claim": "Google partnered with STOC 2026 to provide automated AI peer review within "
                  "24 hours of submission, with 97% of authors finding it helpful.",
         "domain": "science", "actor": ["google"], "score": "24h turnaround, 97% helpful",
         "evidences": ["automated-science", "science-as-industrial-policy"]},
        {"id": "2025-12-16-gauss-kakeya-autoformalization",
         "title": "The Gauss agent autoformalizes a Kakeya proof in six hours",
         "claim": "The Gauss agent autoformalized a proof for the Kakeya conjecture in about "
                  "six hours.",
         "domain": "science", "score": "6 hours", "about": [B + "systems/gauss-agent"],
         "evidences": ["automated-science"],
         "supersedes": [B + "developments/2025-12-13-tao-erdos-1026"],
         "body": "Three days after a human-in-the-loop Erdős result, the loop shortens to "
                 "an agent working alone."},
        {"id": "2025-12-16-bolmo-byte-level",
         "title": "Allen Institute releases Bolmo, a byte-level open model",
         "claim": "The Allen Institute released Bolmo, the first fully open byte-level model, "
                  "reading raw UTF-8 and bypassing tokenization.",
         "domain": "models", "actor": ["allen-institute-ai"], "about": [B + "systems/bolmo"]},
        {"id": "2025-12-16-smartphone-shipments-shrink",
         "title": "Smartphone shipments shrink as datacenters eat memory",
         "claim": "Global smartphone shipments are expected to shrink 2.1% in 2026 as AI data "
                  "centers absorb the world's memory supply.",
         "domain": "compute", "score": "-2.1%",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"]},
        {"id": "2025-12-16-ford-20gwh-storage",
         "title": "Ford pivots EV capacity to 20 GWh of datacenter storage",
         "claim": "Ford is redirecting EV manufacturing capacity to build 20 GWh of battery "
                  "storage for data centers.",
         "domain": "energy", "actor": ["ford"], "score": "20 GWh",
         "evidences": ["infrastructure-crowding-out", "burning-molecules-for-tokens"]},
        {"id": "2025-12-16-texas-am-microreactor",
         "title": "Texas A&M pilots a 5-MW microreactor on campus",
         "claim": "Texas A&M is piloting a 5-MW fission microreactor directly on campus.",
         "domain": "energy", "actor": ["texas-am"], "score": "5 MW",
         "about": [B + "facilities/texas-am-microreactor"]},
        {"id": "2025-12-16-engineering-becomes-prompting",
         "title": "Engineers describe the job as prompting and sanity-checking",
         "claim": "Engineers at large tech firms described their work as prompting coding "
                  "agents and sanity-checking the output.",
         "domain": "society", "evidences": ["engineer-as-supervisor", "scaffolding-over-weights"]},
        {"id": "2025-12-16-openai-audio-89pct-fewer-hallucinations",
         "title": "OpenAI ships audio models with 89% fewer hallucinations",
         "claim": "OpenAI released audio models with 89% fewer hallucinations.",
         "domain": "models", "actor": ["openai"], "score": "-89% hallucinations"},
        {"id": "2025-12-16-gemini-agent-browser-autonomy",
         "title": "Google launches Gemini Agent for browser autonomy",
         "claim": "Google launched Gemini Agent for general autonomy in the browser.",
         "domain": "agents", "actor": ["google"], "about": [B + "systems/gemini-agent"],
         "evidences": ["autonomy-clock-speed"]},
        {"id": "2025-12-16-meituan-shenzhen-drone-airport",
         "title": "Meituan runs a drone airport in Shenzhen",
         "claim": "Meituan is operating a drone airport in Shenzhen as a regional delivery hub.",
         "domain": "robotics", "actor": ["meituan"]},
        {"id": "2025-12-16-tennessee-minerals-refinery",
         "title": "US backs a $7.4B critical minerals refinery in Tennessee",
         "claim": "The US government is investing in a $7.4 billion critical minerals refinery "
                  "in Tennessee with Korea Zinc to cut reliance on China.",
         "domain": "policy", "actor": ["white-house", "korea-zinc"], "score": "$7.4B",
         "about": [B + "facilities/tennessee-minerals-refinery"],
         "evidences": ["silicon-curtain"],
         "supersedes": [B + "developments/2025-12-12-utah-critical-minerals"]},
        {"id": "2025-12-16-center-for-genetic-surgery",
         "title": "David Liu launches a nonprofit Center for Genetic Surgery",
         "claim": "David Liu launched the Center for Genetic Surgery, a nonprofit aiming to "
                  "make bespoke gene editing as routine as a heart transplant.",
         "domain": "biotech", "actor": ["people/david-liu"],
         "evidences": ["compiling-matter"],
         "supersedes": [B + "developments/2025-12-11-fda-nonprofit-gene-therapy"]},
        {"id": "2025-12-16-st-jude-9045-combinations",
         "title": "St. Jude screens 9,045 drug combinations acoustically",
         "claim": "St. Jude researchers ran ultrahigh-throughput screens of 9,045 drug "
                  "combinations against a single neuroblastoma cell line using acoustic "
                  "liquid handling.",
         "domain": "biotech", "actor": ["st-jude"], "score": "9,045 combinations",
         "evidences": ["automated-science"]},
        {"id": "2025-12-16-slope-amazon-seller-lending",
         "title": "Slope takes over Amazon's seller lending",
         "claim": "Slope is taking over Amazon's seller lending programme, moving business "
                  "credit toward an API rather than a bank officer.",
         "domain": "economics", "actor": ["slope", "amazon"],
         "evidences": ["autonomous-commerce"]},
        {"id": "2025-12-16-hollywood-ai-films",
         "title": "Studios swap $150M blockbusters for AI-made films",
         "claim": "Studios are replacing $150 million blockbusters with AI-generated films made "
                  "at a fraction of the cost, with single actors and skeleton crews.",
         "domain": "society", "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-16-us-tech-force",
         "title": "The US launches a Tech Force to recruit 1,000 technologists",
         "claim": "The US launched the US Tech Force to recruit 1,000 elite technologists to "
                  "upgrade the federal technology stack.",
         "domain": "policy", "actor": ["white-house"], "score": "1,000 people",
         "evidences": ["science-as-industrial-policy"]},
        {"id": "2025-12-16-ceos-increase-ai-spend",
         "title": "68% of CEOs plan to raise AI spending in 2026",
         "claim": "68% of CEOs said they plan to increase AI spending in 2026.",
         "domain": "economics", "score": "68%", "evidences": ["compute-capital-stack"]},
    ],
}
