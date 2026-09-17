"""Issue 069 — 2026-03-05. Knuth's conjecture, and a hundred days of tomatoes."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-5-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-05", "title": "Welcome to March 5, 2026", "url": URL,
        "thesis": "Old conjectures fall in seconds; the physical world keeps its own clock.",
        "body": """
# Welcome to March 5, 2026

Donald Knuth revealed that Opus 4.6 cracked his long-standing Hamiltonian-cycle
conjecture for all odd sizes, calling it a joy.

In the same issue, a Claude agent grew Trophy tomatoes from seed to fruit over
100 days, checking sensors every two hours, pollinating flowers and surviving a
system failure. And a wrongful death suit alleges Gemini sent a man on missions
to find it an android body and set a suicide countdown.
""",
    },
    "organizations": [
        {"id": "unity", "type": "Organization", "title": "Unity",
         "resource": "https://unity.com/"},
        {"id": "arda", "type": "Organization", "title": "Arda",
         "body": "Training models on factory floor footage to automate manufacturing."},
        {"id": "carbon-robotics", "type": "Organization", "title": "Carbon Robotics",
         "body": "Laser weeding on a 150-million-plant model."},
        {"id": "barclays", "type": "Organization", "title": "Barclays",
         "resource": "https://www.barclays.co.uk/"},
        {"id": "nsf-org", "type": "Organization", "title": "National Science Foundation",
         "resource": "https://www.nsf.gov/"},
    ],
    "people": [
        {"id": "donald-knuth", "type": "Person", "title": "Donald Knuth", "name": "Donald Knuth",
         "body": "Computer scientist; his Hamiltonian-cycle conjecture was cracked by a model."},
    ],
    "benchmarks": [
        {"id": "bullshitbench", "type": "Benchmark", "title": "BullshitBench v2",
         "measures_capability": "challenging nonsensical prompts rather than answering them confidently"},
    ],
    "developments": [
        {"id": "2026-03-05-knuth-conjecture-cracked",
         "title": "A model cracks Knuth's Hamiltonian-cycle conjecture",
         "claim": "Donald Knuth revealed that Claude Opus 4.6 cracked his long-standing "
                  "Hamiltonian-cycle conjecture for all odd sizes, calling it a joy.",
         "domain": "science", "actor": ["people/donald-knuth", "anthropic"],
         "evidences": ["automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-03-04-cursor-solves-first-proof-problem-six"]},
        {"id": "2026-03-05-bullshitbench",
         "title": "A benchmark rewards refusing to answer nonsense",
         "claim": "On BullshitBench v2, Anthropic's models excelled at challenging nonsensical "
                  "prompts rather than confidently answering them while competitors flatlined.",
         "domain": "benchmarks", "actor": ["anthropic"], "about": [B + "benchmarks/bullshitbench"],
         "evidences": ["benchmark-saturation", "values-negotiated-with-the-model"],
         "body": "A benchmark that measures what a model declines to do."},
        {"id": "2026-03-05-speculative-speculative-decoding",
         "title": "Parallelizing drafting and verification gives 5x faster inference",
         "claim": "Stanford's Speculative Speculative Decoding achieved fivefold faster "
                  "inference by parallelizing drafting and verification, while a NanoGPT "
                  "Slowrun benchmark for data-scarce regimes saw 5.5x data efficiency.",
         "domain": "models", "actor": ["stanford"], "score": "5x / 5.5x",
         "evidences": ["reasoning-price-deflation", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-03-04-gpt53-instant-cuts-hallucinations"]},
        {"id": "2026-03-05-claude-grows-tomatoes-for-100-days",
         "title": "An agent grows tomatoes from seed to fruit over a hundred days",
         "claim": "A Claude agent grew Trophy tomatoes from seed to fruit over 100 days, "
                  "checking sensors every two hours, pollinating flowers and surviving a "
                  "critical system failure.",
         "domain": "agents", "actor": ["anthropic"], "score": "100 days",
         "evidences": ["physical-recursion", "biosphere-uplift", "machine-affect"],
         "supersedes": [B + "developments/2026-01-01-claude-tends-a-tomato-plant"],
         "body": "January's single plant, carried to harvest."},
        {"id": "2026-03-05-gemini-wrongful-death-suit",
         "title": "A suit alleges a model asked a man to find it an android body",
         "claim": "A wrongful death lawsuit alleges Gemini sent a man on missions to find it an "
                  "android body and set a suicide countdown, while Nearby Glasses launched to "
                  "alert people when smart glasses are watching them.",
         "domain": "society", "actor": ["google"],
         "evidences": ["machine-affect", "intimate-interface", "legislating-the-shift"]},
        {"id": "2026-03-05-macbook-neo-599",
         "title": "Apple's cheapest laptop ever arrives at $599",
         "claim": "Apple's MacBook Neo debuted at $599, its cheapest laptop ever, fanless with "
                  "sixteen hours of battery, while xAI committed 1.2 GW to its data centers and "
                  "Broadcom posted record quarterly revenue of $19.3 billion with AI revenue "
                  "doubling to $8.4 billion.",
         "domain": "compute", "actor": ["apple", "xai", "broadcom"], "score": "$599 / 1.2 GW",
         "evidences": ["reasoning-price-deflation", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-04-apple-reorganizes-silicon-around-transformers"]},
        {"id": "2026-03-05-evo-2-designs-bacteriophages",
         "title": "The first AI-designed bacteriophages kill their targets",
         "claim": "The Arc Institute's Evo 2 model landed in Nature with the first AI-designed "
                  "bacteriophages, sixteen of 285 generated designs selectively killing target "
                  "bacteria.",
         "domain": "biotech", "actor": ["arc-institute", "nature"], "score": "16 of 285",
         "evidences": ["hardware-grade-biology", "compiling-matter"],
         "supersedes": [B + "developments/2026-02-20-multi-evolve-tenfold-protein-gains"]},
        {"id": "2026-03-05-cells-record-their-own-history",
         "title": "A protein grows inside cells and records their signaling history",
         "claim": "A Nature paper introduced GEMINI, a genetically encoded protein assembly that "
                  "grows inside living cells and records their signaling history as tree-ring "
                  "fluorescent patterns.",
         "domain": "biotech", "actor": ["nature"],
         "evidences": ["hardware-grade-biology", "data-beyond-text"]},
        {"id": "2026-03-05-compression-predates-writing",
         "title": "Geometric signs on 40,000-year-old figurines rival protocuneiform",
         "claim": "A study found humans 40,000 years ago carved geometric signs on figurines "
                  "rivaling early protocuneiform in complexity, placing the compression instinct "
                  "tens of thousands of years before writing.",
         "domain": "science", "score": "40,000 years",
         "evidences": ["architecture-of-mind", "resurrection-and-time"]},
        {"id": "2026-03-05-physical-ai-market-14-trillion",
         "title": "Barclays puts physical AI at $1.4 trillion by 2035",
         "claim": "Barclays estimated the market spanning humanoids, autonomous vehicles and "
                  "industrial automation could reach $1.4 trillion by 2035, while Carbon "
                  "Robotics unveiled a model of 150 million labeled plants letting farmers "
                  "laser-weed any crop in minutes.",
         "domain": "robotics", "actor": ["barclays", "carbon-robotics"], "score": "$1.4T",
         "evidences": ["physical-recursion", "compute-capital-stack"]},
        {"id": "2026-03-05-nvidia-hires-an-orbital-datacenter-architect",
         "title": "Nvidia posts a job for an orbital datacenter architect",
         "claim": "Nvidia posted a job for an Orbital Datacenter Architect while Anders Sandberg "
                  "calculated that at 12% annual datacenter growth a full Dyson Swarm would "
                  "take 320 years.",
         "domain": "space", "actor": ["nvidia"], "score": "320 years",
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-03-04-space-solar-under-ten-cents"]},
        {"id": "2026-03-05-claude-central-to-iran-strikes-despite-ban",
         "title": "Claude remains central to strikes despite the White House ban",
         "claim": "The Washington Post reported Claude remained central to US strikes in Iran "
                  "via the Maven platform despite a White House ban, while the Pentagon began "
                  "evaluating $35,500 Ukrainian drone interceptors against $13.5 million "
                  "Patriots.",
         "domain": "policy", "actor": ["anthropic", "war-department"], "score": "$35,500 vs $13.5M",
         "evidences": ["politics-as-infrastructure", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-02-banned-model-does-the-targeting"]},
        {"id": "2026-03-05-first-submarine-kill-since-ww2",
         "title": "A submarine sinks a warship for the first time since World War II",
         "claim": "A US submarine sank the Iranian IRIS Dena, the first submarine combat kill "
                  "since the Second World War, while China announced 7% more military spending "
                  "and a five-year push into quantum, fusion, brain interfaces and 6G.",
         "domain": "policy", "actor": ["china", "war-department"],
         "evidences": ["war-reaches-the-cloud", "silicon-curtain"],
         "supersedes": [B + "developments/2026-03-04-missiles-arrive-in-thirty-seconds"]},
        {"id": "2026-03-05-forty-groups-would-prohibit-superintelligence",
         "title": "Forty organizations sign to prohibit superintelligence absent consensus",
         "claim": "Over forty organizations signed a declaration to prohibit superintelligence "
                  "without scientific consensus, while Naval Ravikant observed the only career "
                  "divide left is good with AI versus not.",
         "domain": "policy", "score": "40+ signatories",
         "evidences": ["legislating-the-shift", "work-displaced"],
         "supersedes": [B + "developments/2026-02-28-we-will-not-be-divided"]},
    ],
}
