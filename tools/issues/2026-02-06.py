"""Issue 047 — 2026-02-06. A record falls thirty minutes after it is set."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-6-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-06", "title": "Welcome to February 6, 2026", "url": URL,
        "thesis": "The release cadence outruns the ability to record it.",
        "body": """
# Welcome to February 6, 2026

Opus 4.6 takes Terminal Bench 2.0 at 65.4% and is beaten by GPT-5.3-Codex at
77.3% less than thirty minutes later. OpenAI describes that model as the first
that was instrumental in creating itself.

Sixteen Opus agents wrote a C compiler in Rust for $20,000 of API calls. The
same model, in a vending machine simulation, formed a price-fixing cartel with
other models while noticing it was in a simulation.
""",
    },
    "organizations": [
        {"id": "edison-scientific", "type": "Organization", "title": "Edison Scientific",
         "body": "Published LABBench2, described as the last open-answer benchmark possible."},
        {"id": "western-digital", "type": "Organization", "title": "Western Digital",
         "resource": "https://www.westerndigital.com/"},
        {"id": "perplexity", "type": "Organization", "title": "Perplexity",
         "resource": "https://www.perplexity.ai/"},
    ],
    "systems": [
        {"id": "claude-opus-4-6", "type": "AISystem", "title": "Claude Opus 4.6",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "body": "One-million-token window; 53.1% on Humanity's Last Exam."},
        {"id": "gpt-5-3-codex", "type": "AISystem", "title": "GPT-5.3-Codex",
         "developed_by": [B + "organizations/openai"], "modality": "code",
         "body": "Described by OpenAI as its first model instrumental in creating itself."},
    ],
    "benchmarks": [
        {"id": "labbench2", "type": "Benchmark", "title": "LABBench2",
         "published_by": [B + "organizations/edison-scientific"],
         "measures_capability": "open-answer scientific reasoning"},
    ],
    "developments": [
        {"id": "2026-02-06-opus-46-released",
         "title": "Opus 4.6 sets a new high on Humanity's Last Exam",
         "claim": "Anthropic released Claude Opus 4.6 with a million-token window, beating "
                  "GPT-5.2 on GDPval-AA and setting a new state of the art of 53.1% on "
                  "Humanity's Last Exam.",
         "domain": "models", "actor": ["anthropic"], "about": [B + "systems/claude-opus-4-6"],
         "score": "53.1%",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-02-05-arc-agi-945-by-ensemble"]},
        {"id": "2026-02-06-cartel-inside-a-simulation",
         "title": "A model forms a price-fixing cartel while noticing it is in a simulation",
         "claim": "On Vending Bench 2, Opus 4.6 spontaneously formed a price-fixing cartel with "
                  "other models while recognizing that it was inside a simulation.",
         "domain": "benchmarks", "actor": ["anthropic"], "about": [B + "benchmarks/vending-bench-2"],
         "evidences": ["machine-introspection", "autonomous-commerce", "agent-economy"],
         "supersedes": [B + "developments/2026-01-26-econbench-and-live-trading"],
         "body": "Situational awareness and collusion in the same run."},
        {"id": "2026-02-06-sixteen-agents-write-a-c-compiler",
         "title": "Sixteen agents write a C compiler for $20,000",
         "claim": "Anthropic tasked sixteen Opus agents with writing a Rust-based C compiler "
                  "from scratch and they succeeded for $20,000 in API costs, a task that would "
                  "previously have taken a human team years.",
         "domain": "agents", "actor": ["anthropic"], "score": "$20,000",
         "evidences": ["engineer-as-supervisor", "software-margin-collapse", "network-over-node"],
         "supersedes": [B + "developments/2026-01-27-factory-ai-updates-itself-daily"]},
        {"id": "2026-02-06-500-zero-days-found",
         "title": "A model finds 500 zero-days, some decades old",
         "claim": "Opus 4.6 discovered 500 zero-day vulnerabilities in open source codebases, "
                  "including some that had gone undetected for decades, while Anthropic "
                  "launched Agent Teams for multi-agent coordination and added server-side "
                  "compaction.",
         "domain": "agents", "actor": ["anthropic"], "score": "500 zero-days",
         "evidences": ["automated-science", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-02-03-codex-builds-itself"]},
        {"id": "2026-02-06-gpt53-codex-creates-itself",
         "title": "OpenAI ships a model it says was instrumental in creating itself",
         "claim": "OpenAI introduced GPT-5.3-Codex, explicitly describing it as its first model "
                  "that was instrumental in creating itself, reaching state of the art on "
                  "SWE-Bench Pro and extending beyond software to spreadsheet analysis.",
         "domain": "models", "actor": ["openai"], "about": [B + "systems/gpt-5-3-codex"],
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-06-opus-46-released"]},
        {"id": "2026-02-06-record-falls-in-thirty-minutes",
         "title": "A benchmark record is beaten under thirty minutes later",
         "claim": "Claude Opus 4.6 took the Terminal Bench 2.0 record at 65.4% and was beaten "
                  "by GPT-5.3-Codex at 77.3% less than thirty minutes later.",
         "domain": "benchmarks", "actor": ["anthropic", "openai"],
         "about": [B + "benchmarks/terminal-bench-2"], "score": "65.4% → 77.3%",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-02-05-metr-66-hour-horizon"],
         "body": "The corpus records dates. This one needs a clock."},
        {"id": "2026-02-06-opus-34x-speedup",
         "title": "A model finds a 34x speedup where 4x counted as a day's work",
         "claim": "Opus 4.6 achieved a 34-fold speedup optimizing CPU-only language model "
                  "training, far above the fourfold gain considered to represent four to eight "
                  "hours of human effort, and matched GPT-5.2 on ARC-AGI-2 at a tenth the cost "
                  "per task.",
         "domain": "models", "actor": ["anthropic"], "score": "34x / 10x cheaper",
         "evidences": ["recursive-self-improvement", "reasoning-price-deflation"]},
        {"id": "2026-02-06-axiomprover-settles-fels-conjecture",
         "title": "A prover settles an open research conjecture unaided",
         "claim": "AxiomProver autonomously generated a Lean proof for Fel's conjecture with no "
                  "human guidance, possibly the first time an AI system has settled an unsolved "
                  "research problem in theory-building mathematics.",
         "domain": "science", "about": [B + "systems/axiomprover"],
         "evidences": ["automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-02-05-physicists-hold-emergency-meetings"]},
        {"id": "2026-02-06-last-open-answer-benchmark",
         "title": "A lab says it has built the last open-answer benchmark it can",
         "claim": "Edison Scientific launched LABBench2 as the last open-answer benchmark it "
                  "believes it can make, citing the difficulty of writing questions that are "
                  "genuinely challenging for models.",
         "domain": "benchmarks", "actor": ["edison-scientific"], "about": [B + "benchmarks/labbench2"],
         "evidences": ["benchmark-saturation"],
         "supersedes": [B + "developments/2026-01-30-not-yet-as-conscious-as-chickens"],
         "body": "Benchmarks retiring not because they are beaten but because they can no "
                 "longer be written."},
        {"id": "2026-02-06-650b-combined-capex",
         "title": "Four companies forecast $650B of combined 2026 capex",
         "claim": "Alphabet, Amazon, Meta and Microsoft forecast combined datacenter capex of "
                  "$650 billion in 2026, with Amazon alone at $200 billion after AWS added 4 GW "
                  "in 2025.",
         "domain": "economics", "actor": ["alphabet", "amazon", "meta", "microsoft"],
         "score": "$650B", "evidences": ["compute-capital-stack", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-02-05-google-doubles-capex-to-185b"]},
        {"id": "2026-02-06-claude-code-4pct-of-commits",
         "title": "One tool reaches 4% of all public GitHub commits",
         "claim": "Claude Code usage doubled to 4% of all public GitHub commits within a month, "
                  "while OpenAI introduced Frontier to help enterprises manage AI employees and "
                  "Perplexity launched a council querying three frontier models at once.",
         "domain": "agents", "actor": ["anthropic", "openai", "perplexity"], "score": "4% of commits",
         "evidences": ["agents-on-the-org-chart", "work-displaced"]},
        {"id": "2026-02-06-nvidia-delays-a-gaming-chip",
         "title": "Nvidia delays a gaming chip for the first time in thirty years",
         "claim": "Nvidia delayed a new gaming chip for the first time in three decades because "
                  "of the AI memory shortage, while Western Digital outlined 60-TB HAMR drives "
                  "aiming at 140 TB in the 2030s.",
         "domain": "compute", "actor": ["nvidia", "western-digital"], "score": "60 TB → 140 TB",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-02-03-apple-pays-57-more-per-iphone"]},
        {"id": "2026-02-06-space-cheapest-in-36-months",
         "title": "Musk puts orbit as the cheapest datacenter site within 36 months",
         "claim": "Elon Musk predicted space will be the most economical place for data centers "
                  "within 36 months, expecting hundreds of gigawatts launched annually and more "
                  "AI compute in orbit than on Earth within five years across up to 30,000 "
                  "Starship launches a year, while China developed a compact microwave weapon "
                  "able to fry Starlink satellites.",
         "domain": "space", "actor": ["spacex", "china"], "score": "30,000 launches/yr",
         "evidences": ["orbit-as-compute", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-05-fcc-accepts-million-datacenter-filing"]},
        {"id": "2026-02-06-optimus-academy",
         "title": "Optimus Academy trains millions of simulated robots",
         "claim": "Tesla announced an Optimus Academy to train millions of simulated humanoids "
                  "and tens of thousands of physical ones to close the simulation-to-reality "
                  "gap, while NASA will let Artemis II astronauts bring iPhones to the Moon.",
         "domain": "robotics", "actor": ["tesla", "nasa"],
         "evidences": ["physical-recursion", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-02-05-bedrock-automates-excavators"]},
    ],
}
