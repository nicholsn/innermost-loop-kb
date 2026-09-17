"""Issue 036 — 2026-01-25. Apply only if you can beat it with infinite time."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-25-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-25", "title": "Welcome to January 25, 2026", "url": URL,
        "thesis": "Hiring criteria are rewritten around what the model already beats.",
        "body": """
# Welcome to January 25, 2026

Anthropic open-sourced its performance engineering exam because Opus 4.5 beats
the best humans under time pressure, and now invites applications only from
people who can beat the model given infinite time. The bar is no longer a score;
it is a relation to the model.

A Nature study says scientists using AI publish 3x more and are cited 5x more,
splitting the academy in two. Graduate job postings fall from 180,000 to 55,000.
""",
    },
    "organizations": [
        {"id": "odyssey", "type": "Organization", "title": "Odyssey",
         "body": "Real-time world model company."},
        {"id": "toto", "type": "Organization", "title": "Toto",
         "body": "Japanese toilet maker whose electrostatic chucks matter to NAND fabrication."},
        {"id": "sandisk", "type": "Organization", "title": "SanDisk",
         "resource": "https://www.sandisk.com/"},
        {"id": "tepco", "type": "Organization", "title": "TEPCO",
         "resource": "https://www.tepco.co.jp/"},
        {"id": "ebay", "type": "Organization", "title": "eBay", "resource": "https://www.ebay.com/"},
        {"id": "netflix-studios", "type": "Organization", "title": "Netflix Studios",
         "body": "Instructing filmmakers to repeat plot points for second-screen audiences."},
        {"id": "sphere-entertainment", "type": "Organization", "title": "Sphere Entertainment",
         "resource": "https://sphereentertainmentco.com/"},
    ],
    "benchmarks": [
        {"id": "prinzbench", "type": "Benchmark", "title": "prinzbench",
         "measures_capability": "legal reasoning and retrieval of obscure authority"},
    ],
    "systems": [
        {"id": "odyssey-2-pro", "type": "AISystem", "title": "Odyssey-2 Pro",
         "developed_by": [B + "organizations/odyssey"], "modality": "world model",
         "body": "Streams 720p at 22 FPS for minutes at a time, aiming at years of continuous "
                 "simulation."},
    ],
    "developments": [
        {"id": "2026-01-25-frontiermath-tier-4-31pct",
         "title": "FrontierMath Tier 4 jumps from 19% to 31%",
         "claim": "GPT-5.2 Pro scored a state-of-the-art 31% on FrontierMath Tier 4, up from "
                  "19%, with mathematicians now studying the cases where it failed unexpectedly.",
         "domain": "benchmarks", "actor": ["openai"], "about": [B + "benchmarks/frontiermath"],
         "score": "31%", "evidences": ["automated-science", "benchmark-saturation"],
         "supersedes": [B + "developments/2025-12-31-frontiermath-tier-4-29pct"],
         "body": "The interesting work moves to the failures."},
        {"id": "2026-01-25-apply-only-if-you-beat-it",
         "title": "Anthropic opens its exam and asks for humans who can beat the model",
         "claim": "Anthropic open-sourced its performance engineering exam because Opus 4.5 "
                  "beats the best humans under time constraints, and now invites applications "
                  "only from people who can beat the model given infinite time.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["work-displaced", "ladder-pulled-up", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-01-24-researchers-replaced-first"]},
        {"id": "2026-01-25-claude-code-tasks",
         "title": "Claude Code gets a project management cortex",
         "claim": "Anthropic introduced Tasks for Claude Code, letting it track dependencies "
                  "and collaborate across sessions.",
         "domain": "agents", "actor": ["anthropic"], "about": [B + "systems/claude-code"],
         "evidences": ["agents-on-the-org-chart", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-01-24-mcp-tool-search"]},
        {"id": "2026-01-25-ai-scientists-publish-3x",
         "title": "Scientists using AI publish three times more and are cited five times more",
         "claim": "A Nature study found scientists using AI publish 3.02 times more papers and "
                  "receive 4.84 times more citations, splitting the academy into augmented and "
                  "obsolete factions.",
         "domain": "science", "score": "3.02x papers / 4.84x citations",
         "evidences": ["automated-science", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-01-13-ecologists-lose-touch-with-nature"]},
        {"id": "2026-01-25-odyssey-2-pro-realtime-world",
         "title": "A world model streams 720p for minutes at a time",
         "claim": "Odyssey released Odyssey-2 Pro, a real-time world model running for minutes "
                  "and streaming 720p at 22 FPS, aiming at years of continuous simulation.",
         "domain": "models", "actor": ["odyssey"], "about": [B + "systems/odyssey-2-pro"],
         "evidences": ["data-beyond-text", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-13-1xwm-world-model"]},
        {"id": "2026-01-25-prinzbench-legal-reasoning",
         "title": "A model tops a new legal reasoning benchmark at 52%",
         "claim": "GPT-5.2 Thinking scored a state-of-the-art 52% on the new prinzbench legal "
                  "reasoning benchmark, locating obscure authority that well-paid associates "
                  "often miss.",
         "domain": "benchmarks", "actor": ["openai"], "about": [B + "benchmarks/prinzbench"],
         "score": "52%", "evidences": ["work-displaced", "benchmark-saturation"]},
        {"id": "2026-01-25-toilet-maker-rises-on-nand",
         "title": "A toilet maker rises 11% on NAND demand",
         "claim": "Shares in Japanese toilet maker Toto rose 11% because its electrostatic "
                  "chucks are critical to NAND fabrication, while SanDisk is up around 1,000% "
                  "in five months and Intel admitted it was caught off guard by server CPU "
                  "demand.",
         "domain": "economics", "actor": ["toto", "sandisk", "intel"], "score": "+11% / +1,000%",
         "evidences": ["infrastructure-crowding-out", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-01-15-glass-cloth-shortage"]},
        {"id": "2026-01-25-glp1s-save-airlines-579m",
         "title": "Weight-loss drugs save airlines $579 million in fuel",
         "claim": "Jefferies forecast US airlines will save $579 million in fuel this year "
                  "because weight-loss drugs have made passengers lighter.",
         "domain": "economics", "score": "$579M",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-01-13-glp1-cuts-grocery-spending"]},
        {"id": "2026-01-25-he-jiankui-raises-capital",
         "title": "The CRISPR-baby scientist raises capital to edit embryos again",
         "claim": "He Jiankui, released from Chinese prison for creating CRISPR babies, is "
                  "raising capital to gene-edit embryos for Alzheimer's resistance in South "
                  "Africa, while the Apple Watch proved four times better than standard "
                  "protocols at detecting heart rhythm disorders.",
         "domain": "biotech", "actor": ["apple"], "score": "4x",
         "evidences": ["hardware-grade-biology", "regulatory-exit"],
         "supersedes": [B + "developments/2026-01-11-apoe-92pct-of-alzheimers-risk"]},
        {"id": "2026-01-25-china-consumes-double-us-power",
         "title": "China consumes twice US electricity as datacenter load jumps 17%",
         "claim": "China consumed 10.4 trillion kWh in 2025, double the US total, driven by a "
                  "17% jump in datacenter load, while TEPCO restarted a Kashiwazaki-Kariwa "
                  "reactor for the first time since Fukushima and EU wind and solar overtook "
                  "fossil fuels.",
         "domain": "energy", "actor": ["china", "tepco", "european-union"], "score": "10.4T kWh",
         "evidences": ["burning-molecules-for-tokens", "silicon-curtain"],
         "supersedes": [B + "developments/2026-01-15-china-india-coal-falls"]},
        {"id": "2026-01-25-waymo-reaches-miami",
         "title": "Waymo opens its sixth commercial market",
         "claim": "Waymo expanded its autonomous service to Miami, its sixth commercial market, "
                  "while researchers achieved near-real-time seismic tracking of space debris "
                  "re-entry shockwaves and Rice unveiled PFAS filtration absorbing a hundred "
                  "times faster.",
         "domain": "robotics", "actor": ["waymo", "rice-university"], "score": "6 markets / 100x",
         "evidences": ["autonomous-commerce", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-01-06-lucid-nuro-uber-fleet"]},
        {"id": "2026-01-25-netflix-repeats-plot-points",
         "title": "Netflix tells filmmakers to repeat plot points for the second screen",
         "claim": "Netflix is reportedly instructing filmmakers to repeat plot points three or "
                  "four times because audiences are on their phones, while Sphere Entertainment "
                  "plans a second immersive venue near Washington.",
         "domain": "society", "actor": ["netflix-studios", "sphere-entertainment"],
         "evidences": ["cognitive-load-inverted", "intimate-interface"]},
        {"id": "2026-01-25-ebay-bans-agent-purchases",
         "title": "eBay moves to ban unsupervised agent purchases",
         "claim": "eBay is attempting to ban AI agents from making purchases without direct "
                  "human supervision.",
         "domain": "economics", "actor": ["ebay"],
         "evidences": ["autonomous-commerce", "coordination-tax"],
         "supersedes": [B + "developments/2026-01-12-universal-commerce-protocol"],
         "body": "Two weeks after a protocol is built for agents to transact, a marketplace "
                 "tries to shut them out."},
        {"id": "2026-01-25-graduate-postings-collapse",
         "title": "Graduate job postings fall from 180,000 to 55,000",
         "claim": "Recruiter Reed reported new graduate job postings collapsing from 180,000 to "
                  "55,000 even as 40% of executives report saving more than eight hours a week "
                  "using AI.",
         "domain": "economics", "score": "180,000 → 55,000",
         "evidences": ["ladder-pulled-up", "work-displaced", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-01-15-job-singularity-predicted"]},
        {"id": "2026-01-25-china-population-falls-again",
         "title": "China's population falls by another 3.39 million",
         "claim": "China's population contracted by 3.39 million in 2025 at the lowest birth "
                  "rate since records began in 1949, accelerating the push to replace people "
                  "with automation.",
         "domain": "society", "actor": ["china"], "score": "-3.39M",
         "evidences": ["work-displaced", "physical-recursion"]},
        {"id": "2026-01-25-states-build-bitcoin-reserves",
         "title": "US states build their own Bitcoin reserves",
         "claim": "Texas and New Hampshire are creating state-level Bitcoin strategic reserves "
                  "as a hedge against macro volatility, while Elon Musk predicted the first "
                  "$100 trillion company within a decade.",
         "domain": "economics", "score": "$100T",
         "evidences": ["autonomous-commerce", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-09-stablecoin-volume-33t"]},
    ],
}
