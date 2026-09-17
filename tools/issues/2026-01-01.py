"""Issue — 2026-01-01. A model keeps a tomato plant alive."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-01", "title": "Welcome to 2026", "url": URL,
        "thesis": "Agency crosses from text into the care of a living thing.",
        "body": """
# Welcome to 2026

Claude monitored and managed the growing conditions of a tomato plant. Small,
and the first item in the corpus where a model's agency extends to keeping
something alive rather than producing something.

The year opens with xAI at 450,000 GPUs heading to 900,000, Goldman financing
5 GW of private power campuses to skip the grid queue, and Morgan Stanley
warning of a 44-GW US shortfall by 2028.
""",
    },
    "organizations": [
        {"id": "iquest", "type": "Organization", "title": "iQuest",
         "body": "Chinese lab; 40B looped recurrent Coder-V1."},
        {"id": "goldman-sachs", "type": "Organization", "title": "Goldman Sachs",
         "resource": "https://www.goldmansachs.com/"},
        {"id": "brookfield", "type": "Organization", "title": "Brookfield",
         "resource": "https://www.brookfield.com/"},
        {"id": "atlas-data-storage", "type": "Organization", "title": "Atlas Data Storage",
         "body": "DNA storage at a thousand times tape density."},
        {"id": "space-forge", "type": "Organization", "title": "Space Forge",
         "body": "British orbital semiconductor crystal foundry."},
        {"id": "neuralink", "type": "Organization", "title": "Neuralink",
         "resource": "https://neuralink.com/"},
        {"id": "israel", "type": "Organization", "title": "Government of Israel"},
    ],
    "systems": [
        {"id": "coder-v1", "type": "AISystem", "title": "Coder-V1",
         "developed_by": [B + "organizations/iquest"], "modality": "code",
         "body": "40B looped recurrent transformer claiming 81.4% on SWE-bench Verified."},
    ],
    "developments": [
        {"id": "2026-01-01-claude-tends-a-tomato-plant",
         "title": "A model keeps a tomato plant alive",
         "claim": "Claude monitored and managed the environmental conditions of a growing "
                  "tomato plant, extending its agency from text to the care of a living thing.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["physical-recursion", "biosphere-uplift", "machine-affect"],
         "body": "The first item in the corpus where a model's task is to keep something alive."},
        {"id": "2026-01-01-coder-v1-looped-transformer",
         "title": "A 40B looped transformer claims 81.4% on SWE-bench Verified",
         "claim": "iQuest claims its 40-billion-parameter Coder-V1 reaches 81.4% on SWE-bench "
                  "Verified using a looped recurrent transformer, algorithmic novelty beating "
                  "raw scale.",
         "domain": "models", "actor": ["iquest"], "about": [B + "systems/coder-v1"],
         "score": "81.4%", "evidences": ["architecture-of-mind", "open-weight-latency"],
         "supersedes": [B + "developments/2025-12-23-glm-47-six-month-gap"]},
        {"id": "2026-01-01-concepts-from-raw-experience",
         "title": "Adobe formalizes discovering concepts from raw experience",
         "claim": "Adobe researchers formalized an information-theoretic approach for models to "
                  "discover concepts from raw experience, treating definitions like planet as "
                  "fluid structures rather than fixed entries.",
         "domain": "models", "actor": ["adobe"],
         "evidences": ["architecture-of-mind", "discovery-as-process"],
         "supersedes": [B + "developments/2025-12-27-adobe-causal-models-from-llms"]},
        {"id": "2026-01-01-xai-450000-gpus",
         "title": "xAI runs 450,000 GPUs heading to 900,000",
         "claim": "xAI has 450,000 GPUs online with construction underway to reach 900,000 by "
                  "the second quarter.",
         "domain": "compute", "actor": ["xai"], "score": "450,000 → 900,000",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2025-12-31-xai-third-site-tennessee"]},
        {"id": "2026-01-01-goldman-5gw-private-campuses",
         "title": "Goldman finances 5 GW of private power campuses",
         "claim": "Goldman Sachs is financing 5 GW of private Texas power campuses using "
                  "modular gas turbines to bypass the grid queue, while Morgan Stanley warned "
                  "of a 44-GW US shortfall by 2028 and Brookfield launched a $10 billion "
                  "chip-leasing cloud.",
         "domain": "energy", "actor": ["goldman-sachs", "morgan-stanley", "brookfield"],
         "score": "5 GW / -44 GW",
         "evidences": ["regulatory-exit", "burning-molecules-for-tokens"]},
        {"id": "2026-01-01-photonic-reservoir-10x-efficient",
         "title": "A photonic reservoir device is ten times more efficient per operation",
         "claim": "Researchers built a tunable photonic reservoir computing device roughly ten "
                  "times more energy efficient per operation than the best current GPUs, while "
                  "Atlas Data Storage announced DNA storage at a thousand times tape density.",
         "domain": "compute", "actor": ["atlas-data-storage"], "score": "10x / 1000x",
         "evidences": ["vertical-silicon", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2025-12-20-lightgen-optical-chip"]},
        {"id": "2026-01-01-tsmc-expedites-14nm-fab",
         "title": "TSMC pulls in its 1.4-nm fab on better yields",
         "claim": "TSMC is expediting its 1.4-nm fabrication plant on better-than-expected "
                  "yields as Nvidia scrambles to meet Chinese demand for two million H200 chips.",
         "domain": "compute", "actor": ["tsmc", "nvidia"], "score": "2M H200s",
         "evidences": ["vertical-silicon", "silicon-curtain"]},
        {"id": "2026-01-01-coast-to-coast-zero-disengagements",
         "title": "A car drives coast to coast with zero disengagements",
         "claim": "The first US coast-to-coast autonomous drive was completed with zero "
                  "disengagements.",
         "domain": "robotics", "score": "0 disengagements",
         "evidences": ["autonomy-clock-speed"],
         "supersedes": [B + "developments/2025-12-25-waymo-hardens-for-outages"]},
        {"id": "2026-01-01-e-skin-feels-pain",
         "title": "Robotic skin learns to feel pain",
         "claim": "Chinese researchers developed a neuromorphic robotic e-skin that detects "
                  "pain and injury, while Israel deployed the first operational 100-kW Iron "
                  "Beam laser against drones.",
         "domain": "robotics", "actor": ["china", "israel"], "score": "100 kW",
         "evidences": ["machine-affect", "autonomy-clock-speed"]},
        {"id": "2026-01-01-space-forge-orbital-furnace",
         "title": "An orbital furnace reaches 1,000°C to grow crystals",
         "claim": "Space Forge switched on the furnace of a microwave-sized orbital factory at "
                  "1,000°C, capable of growing semiconductor crystals four thousand times purer "
                  "than terrestrial ones.",
         "domain": "space", "actor": ["space-forge"], "score": "4,000x purity",
         "evidences": ["orbit-as-compute", "compiling-matter"]},
        {"id": "2026-01-01-starlink-41-million-passengers",
         "title": "Starlink serves 41 million travellers in a year",
         "claim": "Starlink served 20 million cruise passengers and 21 million airline "
                  "passengers in 2025, becoming a utility layer.",
         "domain": "space", "actor": ["spacex"], "score": "41M passengers",
         "evidences": ["network-over-node"]},
        {"id": "2026-01-01-three-blockbuster-ipos-planned",
         "title": "OpenAI, SpaceX and Anthropic all plan 2026 IPOs",
         "claim": "OpenAI, SpaceX and Anthropic are all reportedly planning blockbuster IPOs "
                  "for 2026, as Yale economists derived scaling laws for economic impact "
                  "suggesting a 20% US productivity gain over a decade.",
         "domain": "economics", "actor": ["openai", "spacex", "anthropic", "yale"],
         "score": "+20% productivity",
         "evidences": ["compute-capital-stack", "growth-without-hiring"]},
        {"id": "2026-01-01-openai-sbc-15m-per-employee",
         "title": "OpenAI's stock compensation reaches $1.5M per employee",
         "claim": "OpenAI's stock-based compensation hit $1.5 million per employee while Scale "
                  "AI's remnant reported its biggest quarter ever.",
         "domain": "economics", "actor": ["openai", "scale-ai"], "score": "$1.5M/employee",
         "evidences": ["compute-capital-stack", "work-displaced"]},
        {"id": "2026-01-01-neuralink-high-volume-2026",
         "title": "Neuralink moves to volume production and automated surgery",
         "claim": "Elon Musk said Neuralink will begin high-volume production and automated "
                  "surgery in 2026, streamlining thread installation through the dura.",
         "domain": "biotech", "actor": ["neuralink"],
         "evidences": ["intimate-interface", "hardware-grade-biology"]},
        {"id": "2026-01-01-aschenbrenner-growth-minimizes-risk",
         "title": "Aschenbrenner argues growth minimizes existential risk",
         "claim": "Leopold Aschenbrenner argued that faster technological growth minimizes "
                  "existential risk.",
         "domain": "society", "evidences": ["takeoff-declared"]},
    ],
}
