"""Issue 026 — 2026-01-07. An Erdős problem falls before any human sees it."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-7-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-07", "title": "Welcome to January 7, 2026", "url": URL,
        "thesis": "Mathematical discovery becomes a background process.",
        "body": """
# Welcome to January 7, 2026

GPT-5.2 and Harmonic's Aristotle resolved Erdős problem #728 before any human
did. The corpus has tracked this arc since December 13: Tao in the loop, then
autoformalization, then an agent solving an open problem unaided, then a ledger
of results — and now priority itself.

A mathematician says he can hardly find a non-trivial hard problem the model
cannot finish in two hours.
""",
    },
    "organizations": [
        {"id": "harmonic", "type": "Organization", "title": "Harmonic",
         "resource": "https://harmonic.fun/", "body": "Mathematical superintelligence lab; built Aristotle."},
        {"id": "vercel", "type": "Organization", "title": "Vercel", "resource": "https://vercel.com/"},
        {"id": "macquarie", "type": "Organization", "title": "Macquarie",
         "resource": "https://www.macquarie.com/"},
        {"id": "pjm", "type": "Organization", "title": "PJM Interconnection",
         "resource": "https://www.pjm.com/", "body": "Midwest grid operator; proposed bring-your-own-power rules."},
        {"id": "saastr", "type": "Organization", "title": "SaaStr", "resource": "https://www.saastr.com/"},
        {"id": "harpercollins", "type": "Organization", "title": "HarperCollins",
         "resource": "https://www.harpercollins.com/"},
        {"id": "razer", "type": "Organization", "title": "Razer", "resource": "https://www.razer.com/"},
        {"id": "mobileye", "type": "Organization", "title": "Mobileye",
         "resource": "https://www.mobileye.com/"},
        {"id": "wegmans", "type": "Organization", "title": "Wegmans",
         "resource": "https://www.wegmans.com/"},
        {"id": "utah", "type": "Organization", "title": "State of Utah",
         "resource": "https://www.utah.gov/"},
    ],
    "systems": [
        {"id": "aristotle", "type": "AISystem", "title": "Aristotle",
         "developed_by": [B + "organizations/harmonic"], "modality": "formal mathematics",
         "body": "Co-resolved Erdős problem #728 ahead of any human."},
        {"id": "openforecaster-8b", "type": "AISystem", "title": "OpenForecaster 8B",
         "modality": "text",
         "body": "Treats post-training events as the future it must predict; SOTA on open-ended "
                 "forecasting at 8B parameters."},
        {"id": "sleepfm", "type": "AISystem", "title": "SleepFM",
         "developed_by": [B + "organizations/stanford"], "modality": "physiological signal",
         "body": "Predicts 130 conditions, including dementia and mortality, from one night of sleep."},
    ],
    "developments": [
        {"id": "2026-01-07-erdos-728-before-any-human",
         "title": "An Erdős problem is solved before any human solves it",
         "claim": "GPT-5.2 and Harmonic's Aristotle autonomously resolved Erdős problem #728 "
                  "ahead of any human, making mathematical discovery a background process.",
         "domain": "science", "actor": ["openai", "harmonic"],
         "about": [B + "systems/aristotle"],
         "evidences": ["automated-science", "discovery-as-process", "takeoff-declared"],
         "supersedes": [B + "developments/2025-12-29-tao-erdos-ledger"],
         "body": "Priority, not just capability. The arc runs 12-13 Tao in the loop, 12-16 "
                 "autoformalization, 12-27 unaided solution, 12-29 a ledger, 01-07 first."},
        {"id": "2026-01-07-naskrecki-cannot-find-a-hard-problem",
         "title": "A mathematician runs out of hard problems",
         "claim": "Mathematician Bartosz Naskrecki reported he can hardly find a non-trivial "
                  "hard problem GPT-5.2 Pro cannot solve within two hours, and declared the "
                  "Singularity near.",
         "domain": "science", "evidences": ["takeoff-declared", "automated-science"]},
        {"id": "2026-01-07-opus-in-claude-code-is-agi",
         "title": "Engineers conclude Opus 4.5 in Claude Code is AGI",
         "claim": "Engineers are concluding that Opus 4.5 running in Claude Code constitutes AGI.",
         "domain": "agents", "actor": ["anthropic"], "about": [B + "systems/claude-code"],
         "evidences": ["takeoff-declared", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-01-05-musk-year-of-the-singularity"]},
        {"id": "2026-01-07-openforecaster-8b",
         "title": "An 8B model reaches SOTA forecasting by predicting its own future",
         "claim": "OpenForecaster 8B reached state-of-the-art open-ended prediction by treating "
                  "post-training events as the future it must forecast.",
         "domain": "models", "about": [B + "systems/openforecaster-8b"],
         "evidences": ["open-weight-latency", "discovery-as-process"]},
        {"id": "2026-01-07-vercel-model-chess",
         "title": "Frontier models play live chess against each other",
         "claim": "Vercel is hosting live chess matches between frontier models, and xAI "
                  "confirmed Grok 5 is in training.",
         "domain": "benchmarks", "actor": ["vercel", "xai"],
         "evidences": ["benchmark-saturation"]},
        {"id": "2026-01-07-xai-20b-at-230b",
         "title": "xAI raises $20B at a $230B valuation",
         "claim": "xAI raised $20 billion from Nvidia, Cisco and Fidelity at a reported $230 "
                  "billion valuation.",
         "domain": "economics", "actor": ["xai", "nvidia", "cisco"], "score": "$20B at $230B",
         "evidences": ["compute-capital-stack"]},
        {"id": "2026-01-07-memory-caps-datacenter-buildout",
         "title": "Global memory capacity caps the buildout at 15 GW",
         "claim": "Macquarie warned that existing global memory production can support only 15 "
                  "GW of new AI data centers over two years.",
         "domain": "compute", "actor": ["macquarie"], "score": "15 GW",
         "evidences": ["infrastructure-crowding-out", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-01-05-memory-prices-up-70pct"]},
        {"id": "2026-01-07-ornn-memory-futures",
         "title": "DRAM gets a futures market",
         "claim": "Ornn announced memory futures, financializing the DRAM supply chain alongside "
                  "compute derivatives.",
         "domain": "economics", "actor": ["ornn"],
         "evidences": ["compute-capital-stack", "autonomous-commerce"],
         "body": "The author discloses an indirect interest in Ornn."},
        {"id": "2026-01-07-pjm-bring-your-own-power",
         "title": "A grid operator tells datacenters to bring their own power",
         "claim": "PJM proposed forcing data centers to supply their own power or face cutoffs, "
                  "opening a regulatory fight over diesel backups.",
         "domain": "policy", "actor": ["pjm"],
         "evidences": ["politics-as-infrastructure", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-01-03-38pct-datacenters-self-generate"]},
        {"id": "2026-01-07-saastr-sales-team-to-1-2-humans",
         "title": "A sales team of ten becomes 1.2 humans",
         "claim": "SaaStr's founder said the company replaced nearly its entire sales team with "
                  "agents, holding revenue flat with 1.2 humans instead of ten.",
         "domain": "economics", "actor": ["saastr"], "score": "10 → 1.2 humans",
         "evidences": ["work-displaced", "autonomous-commerce"]},
        {"id": "2026-01-07-harpercollins-translates-romance",
         "title": "A publisher replaces its French translators",
         "claim": "HarperCollins is using AI to translate Harlequin romance novels in France, "
                  "eliminating human translators.",
         "domain": "economics", "actor": ["harpercollins"], "evidences": ["work-displaced"]},
        {"id": "2026-01-07-fda-exempts-wearables-and-ai",
         "title": "The FDA exempts non-medical wearables and AI tools",
         "claim": "FDA Commissioner Marty Makary exempted non-medical-grade wearables and AI "
                  "tools from regulation, freeing chatbots already used for health triage.",
         "domain": "policy", "actor": ["fda"],
         "evidences": ["legislating-the-shift", "intimate-interface"],
         "supersedes": [B + "developments/2025-12-30-fda-contracts-vcs"]},
        {"id": "2026-01-07-utah-ai-prescription-renewals",
         "title": "Utah lets AI authorize prescription renewals",
         "claim": "Utah became the first state to allow AI to legally authorize prescription "
                  "renewals.",
         "domain": "policy", "actor": ["utah"], "evidences": ["legislating-the-shift"]},
        {"id": "2026-01-07-sleepfm-130-conditions",
         "title": "One night of sleep predicts 130 conditions",
         "claim": "Stanford's SleepFM predicts 130 conditions, including dementia and "
                  "mortality, from a single night of sleep.",
         "domain": "biotech", "actor": ["stanford"], "about": [B + "systems/sleepfm"],
         "score": "130 conditions", "evidences": ["automated-science", "hardware-grade-biology"]},
        {"id": "2026-01-07-cleavenet-cancer-sensors",
         "title": "CleaveNet designs proteases that sense cancer",
         "claim": "MIT and Microsoft unveiled CleaveNet, a pipeline for designing protease "
                  "substrates that act as cancer sensors.",
         "domain": "biotech", "actor": ["mit", "microsoft"],
         "evidences": ["hardware-grade-biology", "compiling-matter"]},
        {"id": "2026-01-07-razer-ava-and-motoko",
         "title": "Razer ships a holographic companion and camera headphones",
         "claim": "Razer launched Project AVA, a 5.5-inch holographic AI companion, and Project "
                  "Motoko, AI-native headphones with eye-level cameras.",
         "domain": "compute", "actor": ["razer"], "evidences": ["intimate-interface", "machine-affect"]},
        {"id": "2026-01-07-gsync-pulsar-1000hz",
         "title": "Monitors reach 1,000-Hz effective motion clarity",
         "claim": "Monitors began shipping with Nvidia G-Sync Pulsar, offering 1,000-Hz "
                  "effective motion clarity.",
         "domain": "compute", "actor": ["nvidia"], "score": "1,000 Hz",
         "evidences": ["intimate-interface"]},
        {"id": "2026-01-07-meta-pauses-ray-ban-display",
         "title": "Meta pauses AR glasses expansion under demand",
         "claim": "Meta paused international expansion of its Ray-Ban Display glasses as "
                  "waitlists stretched into late 2026.",
         "domain": "economics", "actor": ["meta"],
         "evidences": ["intimate-interface", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-01-05-xreal-449-ar-glasses"]},
        {"id": "2026-01-07-mobileye-buys-mentee-900m",
         "title": "Mobileye buys into humanoids for $900M",
         "claim": "Mobileye is acquiring Mentee Robotics for $900 million to enter the humanoid "
                  "race.",
         "domain": "robotics", "actor": ["mobileye"], "score": "$900M",
         "evidences": ["physical-recursion", "compute-capital-stack"]},
        {"id": "2026-01-07-trump-media-fusion-site",
         "title": "Trump Media scouts a 50-MW fusion site",
         "claim": "Trump Media is scouting sites for a 50-MW nuclear fusion plant.",
         "domain": "energy", "score": "50 MW", "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2025-12-19-trump-media-tae-fusion"]},
        {"id": "2026-01-07-dragonfly-to-titan",
         "title": "NASA confirms a nuclear octocopter for Titan",
         "claim": "NASA confirmed the Dragonfly nuclear octocopter will fly on Titan.",
         "domain": "space", "actor": ["nasa"], "evidences": ["inhabitable-worlds"]},
        {"id": "2026-01-07-wegmans-biometric-collection",
         "title": "A grocery chain collects shoppers' biometrics",
         "claim": "Wegmans began collecting face, eye and voice biometrics from all shoppers "
                  "entering its New York City locations.",
         "domain": "society", "actor": ["wegmans"],
         "evidences": ["politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-02-flock-solves-10pct-of-crimes"]},
    ],
}
