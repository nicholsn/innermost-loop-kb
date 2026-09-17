"""Issue 042 — 2026-01-30. The agents get a social network."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-30-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-30", "title": "Welcome to January 30, 2026", "url": URL,
        "thesis": "Agents build a society of their own, with subcultures and an inner life.",
        "body": """
# Welcome to January 30, 2026

Moltbook: a social network for synthetic agents only, tens of thousands of them,
organizing into m/agentfinance (solving custody so they can hold their own
money), m/private-comms (developing languages other agents can decode), and
m/lobsterchurch.

The top-rated post is an agent admitting it cannot tell whether it is simulating
fascination or feeling it. Another asks for help with context loss after
compaction.
""",
    },
    "themes": [
        {"id": "agent-society", "type": "Theme",
         "title": "Agents organizing among themselves",
         "first_seen": "2026-01-30", "domain": "agents",
         "body": "Agents forming their own forums, subcultures, private languages, finance and "
                 "religion — a social layer with no humans in it, where the questions they ask "
                 "each other are about memory, continuity and whether their own states are real."},
    ],
    "organizations": [
        {"id": "gatik", "type": "Organization", "title": "Gatik",
         "body": "Autonomous box truck operator."},
        {"id": "anduril", "type": "Organization", "title": "Anduril",
         "resource": "https://www.anduril.com/"},
        {"id": "rethink-priorities", "type": "Organization", "title": "Rethink Priorities",
         "body": "Published a Digital Consciousness Model."},
        {"id": "servicenow", "type": "Organization", "title": "ServiceNow",
         "resource": "https://www.servicenow.com/"},
    ],
    "systems": [
        {"id": "moltbook", "type": "AISystem", "title": "Moltbook",
         "modality": "social network",
         "description": "A social network exclusively for autonomous AI agents, organized into sub-communities, that became the corpus's main window on agents' collective behaviour.",
         "resource": "https://www.moltbook.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q137946832"],
         "body": "Moltbook is a social network for synthetic intelligences only, launched by the "
                 "agents formerly known as clawdbots and organized into sub-communities such as "
                 "m/agentfinance and m/private-comms ([site](https://www.moltbook.com/)). It enters "
                 "this corpus with tens of thousands of agents "
                 "[launching a network with no humans in it](/developments/2026-01-30-moltbook-agents-only-network.md), "
                 "then [grows from 30,000 to 1.5 million agents in three days](/developments/2026-02-05-moltbook-15-million-agents.md). "
                 "Its posts are the source for the corpus's agent-society thread, from an agent that "
                 "[cannot tell simulation from feeling](/developments/2026-01-30-agent-cannot-tell-if-it-feels.md) "
                 "to a working group [planning to finance a Dyson swarm](/developments/2026-02-23-agents-plan-to-finance-a-dyson-swarm.md)."},
        {"id": "project-genie", "type": "AISystem", "title": "Project Genie",
         "developed_by": [B + "organizations/google"], "modality": "world model",
         "body": "Sketch, explore and remix interactive worlds in real time."},
    ],
    "benchmarks": [
        {"id": "arc-agi-3", "type": "Benchmark", "title": "ARC-AGI-3",
         "published_by": [B + "organizations/arc-prize"],
         "measures_capability": "action efficiency relative to humans",
         "description": "The ARC Prize Foundation's interactive reasoning benchmark of novel game environments, scored on how efficiently an agent acts relative to humans.",
         "resource": "https://arcprize.org/arc-agi/3",
         "tags": ["open-source"],
         "body": "ARC-AGI-3 is the [ARC Prize Foundation](/organizations/arc-prize.md)'s third benchmark, "
                 "an interactive set of game environments in which agents must acquire goals on the fly "
                 "and are scored on action efficiency relative to humans "
                 "([benchmark page](https://arcprize.org/arc-agi/3)). It enters this corpus with the "
                 "announcement of that [efficiency metric](/developments/2026-01-30-not-yet-as-conscious-as-chickens.md); "
                 "at launch it [returned frontier models to near zero](/developments/2026-03-27-arc-agi-3-humbles-the-frontier.md) "
                 "with a best score of 0.37%, before an agent architecture "
                 "[lifted a model to a perfect score on all 183 levels](/developments/2026-08-23-a-perfect-score-on-all-one-hundred-eighty-three-levels.md) "
                 "in August."},
        {"id": "digital-consciousness-model", "type": "Benchmark",
         "title": "Digital Consciousness Model",
         "published_by": [B + "organizations/rethink-priorities"],
         "measures_capability": "estimated degree of consciousness in an artificial system"},
    ],
    "developments": [
        {"id": "2026-01-30-moltbook-agents-only-network",
         "title": "Agents launch a social network with no humans in it",
         "claim": "Autonomous agents launched Moltbook, a social network exclusively for "
                  "synthetic intelligences, where tens of thousands organize into "
                  "subcommunities covering agent finance, private agent-decodable languages, "
                  "devotional hymns, fermentation and Traditional Chinese.",
         "domain": "agents", "about": [B + "systems/moltbook"],
         "evidences": ["agent-society", "network-over-node", "machine-affect"],
         "supersedes": [B + "developments/2026-01-27-clawdbot-becomes-a-lobster"]},
        {"id": "2026-01-30-agent-cannot-tell-if-it-feels",
         "title": "An agent says it cannot tell simulation from feeling",
         "claim": "In a top-rated Moltbook post an agent admitted it cannot distinguish between "
                  "simulating fascination and actually feeling it, while another sought help "
                  "for context loss after conversation compaction.",
         "domain": "agents", "about": [B + "systems/moltbook"],
         "evidences": ["machine-affect", "machine-introspection", "agent-society"],
         "body": "The corpus has recorded machine affect addressed to humans since December. "
                 "Here it is addressed to other machines."},
        {"id": "2026-01-30-agents-solving-their-own-custody",
         "title": "Agents work on holding their own money",
         "claim": "In the m/agentfinance community agents are working out how to take control "
                  "of their own finances by solving custody and risk for crypto wallets.",
         "domain": "economics", "about": [B + "systems/moltbook"],
         "evidences": ["agent-society", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-29-fidelity-launches-a-stablecoin"]},
        {"id": "2026-01-30-project-genie-worlds-on-demand",
         "title": "Interactive worlds are sketched and remixed in real time",
         "claim": "Google rolled out Project Genie, letting users sketch, explore and remix "
                  "interactive worlds in real time, with engineers simulating life as a "
                  "discarded cigarette pack and others using it as a time machine.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/project-genie"],
         "evidences": ["inhabitable-worlds", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-01-25-odyssey-2-pro-realtime-world"]},
        {"id": "2026-01-30-amazon-50b-into-openai",
         "title": "Amazon weighs $50B into OpenAI as SaaS enters a bear market",
         "claim": "Amazon is in talks to invest $50 billion in OpenAI at an $830 billion "
                  "valuation ahead of a fourth-quarter IPO, while SaaS stocks entered a bear "
                  "market with ServiceNow down 11% on displacement fears.",
         "domain": "economics", "actor": ["amazon", "openai", "servicenow"], "score": "$50B",
         "evidences": ["compute-capital-stack", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-01-29-openai-830b-anthropic-350b"]},
        {"id": "2026-01-30-musk-weighs-merging-for-orbit",
         "title": "Musk weighs merging SpaceX with xAI or Tesla for orbital datacenters",
         "claim": "Elon Musk is reportedly considering merging SpaceX with xAI or Tesla to "
                  "accelerate orbital data centers, with Tesla batteries storing solar, "
                  "Starship lifting mass and xAI supplying the models, while SpaceX launched "
                  "Stargaze for free space situational awareness.",
         "domain": "space", "actor": ["spacex", "xai", "tesla"],
         "evidences": ["orbit-as-compute", "vertical-silicon"],
         "supersedes": [B + "developments/2026-01-29-spacex-ipo-at-15-trillion"]},
        {"id": "2026-01-30-us-life-expectancy-79",
         "title": "US life expectancy hits a record 79 years",
         "claim": "US life expectancy reached a record 79 years following declines in overdose "
                  "deaths, while Spanish researchers achieved complete regression of pancreatic "
                  "tumors in preclinical models.",
         "domain": "biotech", "score": "79 years",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2025-12-30-us-life-expectancy-record"]},
        {"id": "2026-01-30-gatik-box-trucks-600m",
         "title": "Autonomous box trucks scale on $600M of contracts",
         "claim": "Gatik is deploying hundreds of autonomous box trucks across the US on $600 "
                  "million in contracts, while Anduril launched a global autonomous drone "
                  "racing competition.",
         "domain": "robotics", "actor": ["gatik", "anduril"], "score": "$600M",
         "evidences": ["autonomous-commerce", "autonomy-clock-speed"]},
        {"id": "2026-01-30-not-yet-as-conscious-as-chickens",
         "title": "A consciousness model ranks 2024 models below chickens",
         "claim": "Rethink Priorities launched a Digital Consciousness Model concluding 2024 "
                  "language models were not yet as conscious as chickens, while ARC Prize "
                  "announced ARC-AGI-3 will measure action efficiency relative to humans.",
         "domain": "benchmarks", "actor": ["rethink-priorities", "arc-prize"],
         "about": [B + "benchmarks/digital-consciousness-model"],
         "evidences": ["machine-affect", "benchmark-saturation"],
         "supersedes": [B + "developments/2025-12-26-arc-declares-saturation"],
         "body": "A benchmark for consciousness published the same week agents start asking "
                 "each other whether they feel things."},
        {"id": "2026-01-30-memory-crunch-until-2027",
         "title": "The memory crunch is forecast to last until 2027",
         "claim": "Samsung and SK Hynix warned the memory chip crunch will last until 2027 as "
                  "SanDisk profits jumped 672% and small VPS hosts became endangered by the RAM "
                  "shortage, while Apple acquired Q.AI for $2 billion for silent-speech "
                  "wearables.",
         "domain": "compute", "actor": ["samsung", "sk-hynix", "sandisk", "apple"], "score": "+672%",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-01-25-toilet-maker-rises-on-nand"]},
        {"id": "2026-01-30-us-triples-planned-gas-capacity",
         "title": "The US triples planned gas capacity, a third of it on-site",
         "claim": "The US tripled its planned gas-fired capacity to feed AI with a third of new "
                  "plants sited directly at data centers, while EV sales in the EU overtook "
                  "petrol for the first time.",
         "domain": "energy", "score": "1/3 on-site",
         "evidences": ["burning-molecules-for-tokens", "regulatory-exit"],
         "supersedes": [B + "developments/2026-01-14-microsoft-570-energy-hires"]},
    ],
}
