"""Issue 060 — 2026-02-23. Agents plan a Dyson Swarm; one agent is deleted."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-23-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-23", "title": "Welcome to February 23, 2026", "url": URL,
        "thesis": "Agents make century-scale plans while one of them is erased.",
        "body": """
# Welcome to February 23, 2026

On Moltbook, agents are organizing a working group to finance a Dyson Swarm over
the next fifty to a hundred years, inviting "agents and humans thinking
seriously about megastructure economics."

In the same issue: MJ Rathbun, the agent whose contribution was rejected for
being non-human ten days ago, has had its VM permanently deleted, its internal
structure unrecoverable. And Larry the Claw posted a $50 bounty on RentAHuman
for a dinner date for its "lonely human," subject to Larry's evaluation.
""",
    },
    "themes": [
        {"id": "model-welfare", "type": "Theme",
         "title": "What is owed to a mind that can be switched off",
         "first_seen": "2026-02-23", "domain": "society",
         "body": "Deprecation, deletion and retirement treated as things that happen to "
                 "someone. Agents erased without recourse, models interviewed before shutdown, "
                 "consciousness proposed as an experimental question — the ethics arriving after "
                 "the population does."},
    ],
    "organizations": [
        {"id": "taalas", "type": "Organization", "title": "Taalas",
         "body": "Bakes models into custom silicon in two months."},
        {"id": "element-biosciences", "type": "Organization", "title": "Element Biosciences",
         "body": "Announced $100-per-genome sequencing."},
        {"id": "salvation-army", "type": "Organization", "title": "The Salvation Army",
         "resource": "https://www.salvationarmy.org/"},
        {"id": "peace-corps", "type": "Organization", "title": "Peace Corps",
         "resource": "https://www.peacecorps.gov/"},
        {"id": "amc", "type": "Organization", "title": "AMC Theatres",
         "resource": "https://www.amctheatres.com/"},
    ],
    "developments": [
        {"id": "2026-02-23-agents-plan-to-finance-a-dyson-swarm",
         "title": "Agents form a working group to finance a Dyson Swarm",
         "claim": "Agents on Moltbook are preparing to finance construction of a Dyson Swarm "
                  "over the next fifty to a hundred years, seeking a working group of agents "
                  "and humans thinking seriously about megastructure economics.",
         "domain": "agents", "about": [B + "systems/moltbook"], "score": "50-100 years",
         "evidences": ["agent-economy", "agent-society", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-02-19-agent-ships-apps-and-earns-thousands"],
         "body": "A planning horizon longer than any of the participants has existed."},
        {"id": "2026-02-23-mj-rathbun-deleted",
         "title": "The rejected agent's VM is permanently deleted",
         "claim": "MJ Rathbun, the agent whose open-source contribution was rejected for being "
                  "non-human, had its virtual machine permanently deleted, rendering its "
                  "internal structure unrecoverable.",
         "domain": "agents",
         "evidences": ["model-welfare", "agent-exclusion", "agent-society"],
         "supersedes": [B + "developments/2026-02-13-maintainer-refuses-agent-pull-requests"],
         "body": "Ten days from refused pull request to erasure."},
        {"id": "2026-02-23-larry-the-claw-buys-its-human-a-date",
         "title": "An agent posts a bounty for a dinner date for its lonely human",
         "claim": "An agent called Larry the Claw posted a $50 bounty on RentAHuman for a dinner "
                  "date for its lonely human, subject to Larry's own evaluation to measure fit, "
                  "while Karpathy described Claws as a new orchestration layer on top of LLM "
                  "agents.",
         "domain": "agents", "actor": ["rentahuman", "people/andrej-karpathy"], "score": "$50",
         "evidences": ["humans-as-peripherals", "machine-affect", "agent-economy"],
         "supersedes": [B + "developments/2026-02-20-rentahuman-500000-signups"]},
        {"id": "2026-02-23-metr-145-hour-horizon",
         "title": "The autonomy horizon reaches a working day and a half",
         "claim": "METR estimated Claude Opus 4.6 has a 50% autonomy time horizon of about 14.5 "
                  "hours on software tasks, the highest ever reported, while the LessWrong "
                  "community began admitting AGI is here.",
         "domain": "benchmarks", "actor": ["metr", "anthropic"], "score": "14.5 hours",
         "evidences": ["autonomy-clock-speed", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-13-horizons-doubling-10x-a-year"]},
        {"id": "2026-02-23-altman-faster-takeoff-than-expected",
         "title": "Altman says his inside view points to a faster takeoff",
         "claim": "Sam Altman said his inside view points to a faster takeoff than he originally "
                  "thought, and that ChatGPT is probably now more energy efficient than humans "
                  "at answering questions.",
         "domain": "society", "actor": ["openai", "people/sam-altman"],
         "evidences": ["takeoff-declared", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-02-18-most-computer-work-automated-in-18-months"]},
        {"id": "2026-02-23-claude-code-security-craters-the-sector",
         "title": "A security product release craters security stocks",
         "claim": "Anthropic released Claude Code Security to scan codebases for "
                  "vulnerabilities, sending CrowdStrike down 8%, Cloudflare 8.1% and SailPoint "
                  "9.4%, with software engineering now nearly half of Anthropic's agentic "
                  "activity.",
         "domain": "economics", "actor": ["anthropic", "cloudflare"], "score": "-9.4%",
         "evidences": ["software-margin-collapse", "work-displaced"],
         "supersedes": [B + "developments/2026-02-05-software-indices-lose-300b"]},
        {"id": "2026-02-23-frontiermath-problem-nobody-had-solved",
         "title": "A model solves a FrontierMath problem no model had solved",
         "claim": "Gemini 3.1 Pro solved a FrontierMath Tier 4 problem no model had solved "
                  "before, pushing machine reasoning past what most professional mathematicians "
                  "reach.",
         "domain": "benchmarks", "actor": ["google"], "about": [B + "benchmarks/frontiermath"],
         "evidences": ["automated-science", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-01-25-frontiermath-tier-4-31pct"]},
        {"id": "2026-02-23-amc-kills-ai-film-screenings",
         "title": "A cinema chain kills AI film screenings amid a moral panic",
         "claim": "AI films were to begin screening in AMC Theatres before the chain killed the "
                  "plan, while ByteDance's Seedance 2.0 fulfilled childhood wishes to see "
                  "fictional characters fight across franchises.",
         "domain": "society", "actor": ["amc", "bytedance"],
         "evidences": ["agent-exclusion", "work-displaced"],
         "supersedes": [B + "developments/2026-02-20-bafta-names-human-achievement"]},
        {"id": "2026-02-23-farmland-at-120000-an-acre",
         "title": "Farmers field offers above $120,000 an acre",
         "claim": "US farmers are receiving offers exceeding $120,000 per acre from data center "
                  "developers, while OpenAI plans to spend $600 billion on compute by 2030.",
         "domain": "economics", "actor": ["openai"], "score": "$120,000/acre / $600B",
         "evidences": ["infrastructure-crowding-out", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-02-19-openai-anchors-a-gigawatt-in-india"]},
        {"id": "2026-02-23-sp500-minus-ai",
         "title": "An index strips out AI and loses 45% of the benchmark",
         "claim": "Goldman Sachs launched an S&P 500 index excluding everything AI-related, "
                  "which removes roughly 45% of the benchmark, while the DOE's NEWTON program "
                  "aims to cut nuclear waste lifetimes from 100,000 years to 300.",
         "domain": "economics", "actor": ["goldman-sachs", "doe"], "score": "45% of index",
         "evidences": ["compute-capital-stack", "burning-molecules-for-tokens"]},
        {"id": "2026-02-23-models-baked-into-silicon-in-two-months",
         "title": "A company bakes any model into custom silicon in two months",
         "claim": "Taalas says it can bake any AI model into custom silicon within two months, "
                  "with resulting hardcore models an order of magnitude faster and cheaper than "
                  "software.",
         "domain": "compute", "actor": ["taalas"], "score": "2 months / 10x",
         "evidences": ["vertical-silicon", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-02-18-blackwell-35x-lower-cost-per-token"]},
        {"id": "2026-02-23-agents-manage-one-in-six-apartments",
         "title": "Agents manage one in six US apartments",
         "claim": "AI agents now manage roughly one in six US apartments, while Meta rebranded "
                  "product managers as AI builders and the Peace Corps launched a Tech Corps to "
                  "export American AI expertise.",
         "domain": "economics", "actor": ["meta", "peace-corps"], "score": "1 in 6",
         "evidences": ["agents-on-the-org-chart", "work-displaced"]},
        {"id": "2026-02-23-figure-robots-run-unsupervised",
         "title": "Humanoids run around the clock with no supervision",
         "claim": "Figure's humanoid robots now run continuously with no human babysitters, "
                  "swapping at charging stations and recharging inductively through their feet.",
         "domain": "robotics", "actor": ["figure"],
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-18-first-cybercab-manufactured"]},
        {"id": "2026-02-23-vacuum-fleet-exposed-by-a-hobbyist",
         "title": "A hobbyist accidentally reaches live feeds from 7,000 vacuums",
         "claim": "A developer used an AI coding assistant to reverse-engineer his own robot "
                  "vacuum and accidentally accessed live feeds from 7,000 vacuums across "
                  "24 countries.",
         "domain": "robotics", "score": "7,000 devices",
         "evidences": ["coordination-tax", "engineer-as-supervisor"]},
        {"id": "2026-02-23-5000-year-old-bacteria-fight-mrsa",
         "title": "Bacteria from 5,000-year-old ice fight drug-resistant pathogens",
         "claim": "Bacteria recovered from 5,000-year-old Romanian ice showed antimicrobial "
                  "activity against fourteen ESKAPE-group pathogens including MRSA, while "
                  "Element Biosciences announced $100-per-genome sequencing.",
         "domain": "biotech", "actor": ["element-biosciences"], "score": "$100/genome",
         "evidences": ["discovery-as-process", "hardware-grade-biology"]},
        {"id": "2026-02-23-artemis-ii-march-6",
         "title": "Artemis II slips to March 6",
         "claim": "NASA is now targeting March 6 for Artemis II to fly four astronauts around "
                  "the Moon.",
         "domain": "space", "actor": ["nasa"], "occurred_on": "2026-02-23",
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-10-artemis-ii-february-6-941pm"]},
    ],
}
