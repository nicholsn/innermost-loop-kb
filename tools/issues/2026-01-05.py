"""Issue 024 — 2026-01-05. Five years of theory in four hours."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-5-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-05", "title": "Welcome to January 5, 2026", "url": URL,
        "thesis": "The latency between having an idea and having the artifact collapses.",
        "body": """
# Welcome to January 5, 2026

Railway's CEO handed Claude a distributed runtime he had been theorizing for
five years. The Go codebase came back in four hours.

That is the shape of the issue: the bottleneck moves from implementation to
specification. Musk names 2026 the year of the Singularity; Anthropic's
president argues AGI is already an outdated target.
""",
    },
    "themes": [
        {"id": "software-margin-collapse", "type": "Theme",
         "title": "Software's marginal cost goes to zero",
         "first_seen": "2026-01-05", "domain": "economics",
         "body": "When a model can one-shot a product, the price of software approaches the "
                 "price of the inference that produced it, and every business built on "
                 "software margins has to re-underwrite itself."},
    ],
    "organizations": [
        {"id": "railway", "type": "Organization", "title": "Railway",
         "resource": "https://railway.com/", "body": "Infrastructure platform; CEO specified a runtime, Claude wrote it."},
        {"id": "rand", "type": "Organization", "title": "RAND Corporation",
         "resource": "https://www.rand.org/"},
        {"id": "bcg", "type": "Organization", "title": "Boston Consulting Group",
         "resource": "https://www.bcg.com/"},
        {"id": "furiosa", "type": "Organization", "title": "FuriosaAI",
         "resource": "https://furiosa.ai/", "body": "South Korean inference chip startup."},
        {"id": "xreal", "type": "Organization", "title": "Xreal",
         "resource": "https://www.xreal.com/", "body": "AR glasses maker."},
        {"id": "phoenix-tailings", "type": "Organization", "title": "Phoenix Tailings",
         "body": "Zero-emission rare earth refining in New Hampshire."},
        {"id": "pwc", "type": "Organization", "title": "PricewaterhouseCoopers",
         "resource": "https://www.pwc.com/"},
    ],
    "people": [
        {"id": "daniela-amodei", "type": "Person", "title": "Daniela Amodei", "name": "Daniela Amodei",
         "body": "Anthropic president; argues AGI is becoming an outdated framing."},
        {"id": "jake-cooper", "type": "Person", "title": "Jake Cooper", "name": "Jake Cooper",
         "body": "Railway CEO; five years of design specified in one prompt."},
    ],
    "hardware": [
        {"id": "furiosa-rngd", "type": "Hardware", "title": "Furiosa RNGD",
         "fabricated_by": [B + "organizations/furiosa"],
         "body": "Korean inference accelerator claiming double Nvidia's power efficiency."},
    ],
    "developments": [
        {"id": "2026-01-05-musk-year-of-the-singularity",
         "title": "Musk names 2026 the year of the Singularity",
         "claim": "Elon Musk declared 2026 the year of the Singularity while Anthropic "
                  "president Daniela Amodei argued AGI is an outdated target already passed on "
                  "many metrics.",
         "domain": "society", "actor": ["people/daniela-amodei"],
         "evidences": ["takeoff-declared"],
         "supersedes": [B + "developments/2026-01-04-musk-enters-the-singularity"]},
        {"id": "2026-01-05-five-years-in-four-hours",
         "title": "Five years of design becomes four hours of code",
         "claim": "Railway CEO Jake Cooper gave Claude a specification for a distributed "
                  "runtime he had theorized for five years, and the model wrote the entire Go "
                  "codebase in four hours.",
         "domain": "agents", "actor": ["railway", "people/jake-cooper"], "score": "5 years → 4 hours",
         "evidences": ["engineer-as-supervisor", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-01-04-claude-code-compresses-research"],
         "body": "The bottleneck moves from implementation to specification."},
        {"id": "2026-01-05-rand-calibrated-self-confidence",
         "title": "Models know they are right before running the code",
         "claim": "RAND researchers found Claude models developing accurate self-reflective "
                  "confidence on coding tasks, predicting correctness before execution.",
         "domain": "models", "actor": ["rand", "anthropic"],
         "evidences": ["machine-introspection", "architecture-of-mind"]},
        {"id": "2026-01-05-nanogpt-113s",
         "title": "The speedrun record falls to 113.7 seconds",
         "claim": "The NanoGPT speedrun record collapsed again to 113.7 seconds.",
         "domain": "models", "score": "113.7 s",
         "evidences": ["recursive-self-improvement", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-01-02-speedrun-gains-generalize"]},
        {"id": "2026-01-05-agents-as-windows-apps",
         "title": "Windows makes agents first-class apps",
         "claim": "Microsoft introduced Agent Launchers, letting developers register autonomous "
                  "workers directly into the Windows taskbar.",
         "domain": "agents", "actor": ["microsoft"],
         "evidences": ["autonomous-commerce", "scaffolding-over-weights"]},
        {"id": "2026-01-05-bcg-36000-custom-gpts",
         "title": "BCG runs an assembly line for 36,000 custom models",
         "claim": "BCG has built over 36,000 custom GPTs through an internal AI assembly line.",
         "domain": "economics", "actor": ["bcg"], "score": "36,000",
         "evidences": ["work-displaced"]},
        {"id": "2026-01-05-openai-26b-users-2030",
         "title": "OpenAI projects a third of humanity as weekly users",
         "claim": "OpenAI projects 2.6 billion weekly active users by 2030, about a third of "
                  "the human population.",
         "domain": "society", "actor": ["openai"], "score": "2.6B weekly",
         "evidences": ["intimate-interface"]},
        {"id": "2026-01-05-memory-prices-up-70pct",
         "title": "Server memory prices rise up to 70%",
         "claim": "Samsung and SK Hynix are raising server memory prices by up to 70% as AI "
                  "demand overwhelms supply.",
         "domain": "economics", "actor": ["samsung", "sk-hynix"], "score": "+70%",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-01-02-memory-shortage-raises-prices"]},
        {"id": "2026-01-05-furiosa-rngd-mass-production",
         "title": "A Korean inference chip enters mass production",
         "claim": "FuriosaAI began mass production of its RNGD inference chip, claiming double "
                  "the power efficiency of the incumbent.",
         "domain": "compute", "actor": ["furiosa"], "about": [B + "hardware/furiosa-rngd"],
         "evidences": ["vertical-silicon", "silicon-curtain"]},
        {"id": "2026-01-05-gemini-800m-edge-devices",
         "title": "Samsung pushes Gemini onto 800 million devices",
         "claim": "Samsung plans to reach 800 million devices with Gemini in 2026, including "
                  "fridges that track food freshness by vision.",
         "domain": "models", "actor": ["samsung", "google"], "score": "800M devices",
         "evidences": ["intimate-interface", "reasoning-price-deflation"]},
        {"id": "2026-01-05-xreal-449-ar-glasses",
         "title": "AR glasses reach $449 with 2D-to-3D conversion",
         "claim": "Xreal announced 1S AR glasses at $449 that convert 2D video to 3D without "
                  "proprietary software.",
         "domain": "compute", "actor": ["xreal"], "score": "$449",
         "evidences": ["intimate-interface"],
         "supersedes": [B + "developments/2026-01-02-pickle-799-ar-glasses"]},
        {"id": "2026-01-05-arctic-route-20-days",
         "title": "A melting Arctic halves the China-UK shipping time",
         "claim": "The Northern Sea Route carried its first container ship from China to the UK "
                  "in twenty days, half the Suez route, aided by nuclear icebreakers.",
         "domain": "economics", "score": "20 days",
         "evidences": ["industrialized-nature", "coordination-tax"]},
        {"id": "2026-01-05-spacex-10000-starships",
         "title": "SpaceX prepares to build 10,000 Starships a year",
         "claim": "SpaceX is preparing to manufacture 10,000 Starships per year.",
         "domain": "space", "actor": ["spacex"], "score": "10,000/yr",
         "evidences": ["orbit-as-compute", "inhabitable-worlds"]},
        {"id": "2026-01-05-magnetic-shield-against-flares",
         "title": "Superconducting shields are proposed against Carrington events",
         "claim": "Andrew Cote argued that superconducting tape and heavy lift now make it "
                  "feasible to orbit magnetic shields protecting Earth from civilization-ending "
                  "solar flares.",
         "domain": "space", "evidences": ["industrialized-nature", "inhabitable-worlds"]},
        {"id": "2026-01-05-starlink-free-venezuela",
         "title": "Starlink gives Venezuela free broadband through February",
         "claim": "Starlink is providing free broadband to Venezuela through February 3.",
         "domain": "policy", "actor": ["spacex"],
         "evidences": ["politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-04-maduro-capture-drone-cyber"]},
        {"id": "2026-01-05-tesla-semi-1-2mw-charging",
         "title": "A truck takes 1.2 MW of charge",
         "claim": "Tesla demonstrated a Semi charging at 1.2 MW peak, refilling 70% of its "
                  "battery in under 45 minutes, as EVs and hybrids reached a quarter of US auto "
                  "sales.",
         "domain": "energy", "actor": ["tesla"], "score": "1.2 MW / 25% of sales",
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-01-05-zero-emission-rare-earths",
         "title": "Rare earths are refined without emissions in New Hampshire",
         "claim": "Phoenix Tailings began zero-emission rare earth refining in New Hampshire.",
         "domain": "science", "actor": ["phoenix-tailings"],
         "evidences": ["industrialized-nature", "silicon-curtain"]},
        {"id": "2026-01-05-fish-gill-microplastic-filter",
         "title": "A fish-gill filter strips 99.6% of microplastics",
         "claim": "German researchers built a bio-inspired fish-gill filter that removes 99.6% "
                  "of microplastics from washing machine effluent.",
         "domain": "science", "score": "99.6%", "evidences": ["biosphere-uplift"]},
        {"id": "2026-01-05-daraxonrasib-breakthrough",
         "title": "The FDA fast-tracks a drug for undruggable RAS",
         "claim": "The FDA granted breakthrough status to daraxonrasib for pancreatic cancer, "
                  "targeting undruggable RAS mutations with 8.8 months of progression-free "
                  "survival.",
         "domain": "biotech", "actor": ["fda"], "score": "8.8 months",
         "evidences": ["hardware-grade-biology", "legislating-the-shift"]},
        {"id": "2026-01-05-15-pgdh-regrows-cartilage",
         "title": "Blocking one protein regrows knee cartilage",
         "claim": "Stanford researchers found that blocking the 15-PGDH protein regrows knee "
                  "cartilage without stem cells, reversing arthritis.",
         "domain": "biotech", "actor": ["stanford"], "evidences": ["hardware-grade-biology"]},
        {"id": "2026-01-05-more-ai-startups-than-public-companies",
         "title": "AI startups now outnumber US public companies",
         "claim": "There are now 6,956 AI startups, more than the number of publicly listed US "
                  "companies.",
         "domain": "economics", "score": "6,956", "evidences": ["compute-capital-stack"]},
        {"id": "2026-01-05-war-department-evaluates-safes",
         "title": "The Department of War evaluates YC SAFEs",
         "claim": "The US Department of War is evaluating YC SAFE instruments for the first "
                  "time to fund defense technology.",
         "domain": "policy", "actor": ["war-department"],
         "evidences": ["legislating-the-shift", "science-as-industrial-policy"]},
        {"id": "2026-01-05-pwc-pitches-stablecoins",
         "title": "A Big Four firm pitches clients on stablecoins",
         "claim": "PricewaterhouseCoopers began pitching clients on crypto and stablecoins "
                  "following the GENIUS Act.",
         "domain": "economics", "actor": ["pwc"],
         "evidences": ["autonomous-commerce"],
         "supersedes": [B + "developments/2025-12-29-stablecoins-300b"]},
        {"id": "2026-01-05-35-day-workweek-predicted",
         "title": "Dimon and Gates predict a 3.5-day week",
         "claim": "Jamie Dimon and Bill Gates both predicted a slide toward a 3.5-day workweek.",
         "domain": "economics", "score": "3.5 days",
         "evidences": ["work-displaced"]},
        {"id": "2026-01-05-public-domain-expands",
         "title": "Betty Boop enters the public domain",
         "claim": "The public domain expanded to include Betty Boop and the Marx Brothers' "
                  "Animal Crackers, opening them to generative remixing.",
         "domain": "society", "evidences": ["resurrection-and-time"]},
    ],
}
