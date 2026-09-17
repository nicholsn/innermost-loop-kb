"""Issue 048 — 2026-02-07. Editors and terminals are banned."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-7-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-07", "title": "Welcome to February 7, 2026", "url": URL,
        "thesis": "Working directly becomes a policy violation.",
        "body": """
# Welcome to February 7, 2026

OpenAI will require every employee to code through agents by March 31, banning
direct use of editors and terminals. The corpus has recorded the supervisor role
emerging by choice since December; here it is mandated.

The creator of Moltbook predicts AIs will be the largest population on the
internet and tells developers to build for them rather than for people. In
China, racks of Mac Minis host agents as round-the-clock employees.
""",
    },
    "organizations": [
        {"id": "21st-century-medicine", "type": "Organization", "title": "21st Century Medicine",
         "body": "Demonstrated aldehyde-free vitrification of a rabbit brain."},
        {"id": "erebor", "type": "Organization", "title": "Erebor Bank",
         "body": "Palmer Luckey's crypto-integrated bank, chartered for continuous operation."},
        {"id": "semianalysis", "type": "Organization", "title": "SemiAnalysis",
         "resource": "https://semianalysis.com/"},
    ],
    "benchmarks": [
        {"id": "vals-index", "type": "Benchmark", "title": "Vals Index",
         "measures_capability": "aggregate frontier model capability"},
        {"id": "alpha-arena", "type": "Benchmark", "title": "Alpha Arena",
         "measures_capability": "returns in a live stock trading simulation"},
    ],
    "developments": [
        {"id": "2026-02-07-openai-bans-editors-and-terminals",
         "title": "OpenAI bans its own employees from using editors and terminals",
         "claim": "OpenAI will require all employees to code through agents by March 31, "
                  "banning direct use of editors or terminals.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["engineer-as-supervisor", "agents-on-the-org-chart", "deskilling"],
         "supersedes": [B + "developments/2026-02-06-claude-code-4pct-of-commits"],
         "body": "Working directly becomes a policy violation."},
        {"id": "2026-02-07-mac-mini-racks-as-employees",
         "title": "Racks of Mac Minis are run as round-the-clock employees",
         "claim": "In China, racks of Mac Minis are hosting OpenClaw agents as 24/7 employees, "
                  "creating a synthetic workforce in a closet, while the creator of Moltbook "
                  "predicted AIs will be the largest population on the internet and urged "
                  "developers to build for them rather than for humans.",
         "domain": "agents", "actor": ["china"],
         "evidences": ["agent-society", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-02-05-moltbook-15-million-agents"]},
        {"id": "2026-02-07-claude-code-20pct-by-year-end",
         "title": "One tool is projected at a fifth of public commits by year end",
         "claim": "SemiAnalysis projects Claude Code will account for 20% of all public GitHub "
                  "commits by year end, while Goldman Sachs co-developed autonomous accounting "
                  "and vetting agents with Anthropic as digital coworkers and X launched "
                  "AI-drafted community fact-checks.",
         "domain": "economics", "actor": ["semianalysis", "goldman-sachs", "anthropic"],
         "score": "20% of commits",
         "evidences": ["agents-on-the-org-chart", "work-displaced"]},
        {"id": "2026-02-07-opus-46-tops-vals-index",
         "title": "Opus 4.6 takes the top index spot as markets price the next month",
         "claim": "Claude Opus 4.6 took first on the Vals Index and the Code and Text Arenas "
                  "while statistically tying GPT-5.2-xhigh across FrontierMath Tiers 1 to 4, "
                  "with prediction markets giving Anthropic 67% odds of the best model by "
                  "month's end.",
         "domain": "benchmarks", "actor": ["anthropic"], "about": [B + "benchmarks/vals-index"],
         "score": "67% odds",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-02-06-record-falls-in-thirty-minutes"]},
        {"id": "2026-02-07-grok-34pct-in-alpha-arena",
         "title": "A model returns 34% in a live trading arena",
         "claim": "Grok 4.20 delivered a 34% return in the Alpha Arena stock trading simulation, "
                  "taking the top spot overall.",
         "domain": "benchmarks", "actor": ["xai"], "about": [B + "benchmarks/alpha-arena"],
         "score": "34%",
         "evidences": ["autonomous-commerce", "agent-economy"],
         "supersedes": [B + "developments/2026-02-06-cartel-inside-a-simulation"]},
        {"id": "2026-02-07-encrypted-solutions-challenge",
         "title": "Mathematicians publish problems with encrypted solutions",
         "claim": "Mathematicians released ten research-level problems with encrypted solutions "
                  "to test whether AI can solve in days questions whose answers the authors "
                  "have not published.",
         "domain": "benchmarks",
         "evidences": ["benchmark-saturation", "automated-science"],
         "supersedes": [B + "developments/2026-02-06-last-open-answer-benchmark"],
         "body": "A benchmark designed around the assumption that anything published has "
                 "already been absorbed."},
        {"id": "2026-02-07-rabbit-brain-vitrification",
         "title": "A rabbit brain is preserved intact without chemical fixation",
         "claim": "21st Century Medicine demonstrated perfect ultrastructural preservation of a "
                  "rabbit brain by vitrification without aldehyde fixation, establishing the "
                  "feasibility of human cryopreservation.",
         "domain": "biotech", "actor": ["21st-century-medicine"],
         "evidences": ["resurrection-and-time", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-05-lifespan-heritability-above-50pct"]},
        {"id": "2026-02-07-memory-prices-up-90pct",
         "title": "Memory prices rise up to 90% in a quarter",
         "claim": "Memory chip prices soared 80 to 90% in the first quarter with global chip "
                  "sales projected to reach $1 trillion this year, while Chinese researchers "
                  "achieved device-independent quantum key distribution over 100 km and OpenAI "
                  "prepared an audio wearable called Dime.",
         "domain": "economics", "actor": ["china", "openai"], "score": "+90% / $1T",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-02-06-nvidia-delays-a-gaming-chip"]},
        {"id": "2026-02-07-moratorium-pushes-compute-to-orbit",
         "title": "A datacenter moratorium bill pushes compute toward orbit",
         "claim": "New York lawmakers introduced a datacenter moratorium bill as terrestrial "
                  "resistance mounts, and Musk confirmed SpaceX's near-term focus is shifting "
                  "to disassembling the Moon for AI data centers via mass drivers, delaying "
                  "Mars for an uncrewed lunar landing in March 2027.",
         "domain": "policy", "actor": ["new-york-state", "spacex"],
         "evidences": ["regulatory-exit", "orbit-as-compute", "industrialized-nature"],
         "supersedes": [B + "developments/2026-02-06-space-cheapest-in-36-months"]},
        {"id": "2026-02-07-waymo-world-model",
         "title": "Waymo trains on worlds it generates itself",
         "claim": "Waymo is using its own Waymo World Model, based on DeepMind's Genie 3, to "
                  "generate realistic digital worlds for training, while Tesla FSD is reportedly "
                  "saving lives by driving heart attack victims to hospital faster than "
                  "ambulances.",
         "domain": "robotics", "actor": ["waymo", "google-deepmind", "tesla"],
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-06-optimus-academy"]},
        {"id": "2026-02-07-erebor-charters-a-sunday-bank",
         "title": "A bank is chartered to operate on Sundays to match the blockchain",
         "claim": "Palmer Luckey's Erebor Bank received a national charter for 24/7 "
                  "crypto-integrated banking, explicitly planning to operate on Sundays to "
                  "match the blockchain's rhythm, while AI.com sold for $70 million.",
         "domain": "economics", "actor": ["erebor"], "score": "$70M",
         "evidences": ["autonomous-commerce", "agent-economy"],
         "supersedes": [B + "developments/2026-01-29-fidelity-launches-a-stablecoin"]},
        {"id": "2026-02-07-bonobos-identify-pretend-objects",
         "title": "Bonobos are found to identify pretend objects",
         "claim": "Bonobos were found to identify pretend objects, further evidence that "
                  "symbolic thought is not unique to humans.",
         "domain": "science", "evidences": ["biosphere-uplift", "architecture-of-mind"]},
    ],
}
