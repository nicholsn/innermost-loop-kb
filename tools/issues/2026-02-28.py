"""Issue 065 — 2026-02-28. A constitutional crisis over a model."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-28-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-28", "title": "Welcome to February 28, 2026", "url": URL,
        "thesis": "The state demands unrestricted access to a private model, and is refused.",
        "body": """
# Welcome to February 28, 2026

The Secretary of War declared the Department must have full, unrestricted access
to Anthropic's models for every lawful purpose, designating the company a
supply-chain risk. Anthropic replied that no amount of intimidation or
punishment will change its position.

684 employees across Google and OpenAI signed an open letter titled "We Will Not
Be Divided." The speedrun record, meanwhile, fell to 88.1 seconds.
""",
    },
    "themes": [
        {"id": "refusal-as-differentiator", "type": "Theme",
         "title": "Declining work becomes a competitive position",
         "first_seen": "2026-02-28", "domain": "economics",
         "body": "A lab's restrictions start as a cost — a lost contract, a supply-chain-risk "
                 "label — and then become a product feature customers choose, as users move "
                 "between providers on the basis of what each one refuses to do."},
    ],
    "organizations": [
        {"id": "bright-data", "type": "Organization", "title": "Bright Data",
         "body": "SDK turning smart TVs into web-scraping proxy nodes."},
        {"id": "cortical-labs", "type": "Organization", "title": "Cortical Labs",
         "body": "Grows human neurons on electrode arrays."},
        {"id": "project-prometheus", "type": "Organization", "title": "Project Prometheus",
         "body": "Bezos-backed venture applying AI to manufacturing."},
        {"id": "colorado", "type": "Organization", "title": "State of Colorado"},
    ],
    "developments": [
        {"id": "2026-02-28-pentagon-demands-unrestricted-access",
         "title": "The Pentagon demands unrestricted access and Anthropic refuses",
         "claim": "The Secretary of War declared the Department of War must have full, "
                  "unrestricted access to Anthropic's models for every lawful purpose and "
                  "designated the company a supply-chain risk, and Anthropic replied that no "
                  "amount of intimidation or punishment will change its position on mass "
                  "surveillance or autonomous weapons.",
         "domain": "policy", "actor": ["war-department", "anthropic"],
         "evidences": ["values-negotiated-with-the-model", "politics-as-infrastructure",
                       "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-02-27-anthropic-refuses-surveillance-and-weapons"],
         "body": "The dispute reportedly distilled to a hypothetical inbound nuclear missile."},
        {"id": "2026-02-28-openai-takes-the-classified-deal",
         "title": "OpenAI takes the classified deal Anthropic refused",
         "claim": "Sam Altman announced OpenAI had reached agreement to deploy on the "
                  "Pentagon's classified network claiming the same red lines as Anthropic, "
                  "though an Under Secretary of State noted the contract still flows from all "
                  "lawful use.",
         "domain": "policy", "actor": ["openai", "war-department"],
         "evidences": ["safety-pledges-recede", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-24-xai-grok-in-battlefield-systems"]},
        {"id": "2026-02-28-we-will-not-be-divided",
         "title": "Nearly 700 employees sign a joint refusal letter",
         "claim": "591 Google and 93 OpenAI employees signed an open letter titled We Will Not "
                  "Be Divided, demanding refusal of mass surveillance and autonomous killing.",
         "domain": "society", "actor": ["google", "openai"], "score": "684 signatories",
         "evidences": ["values-negotiated-with-the-model", "refusal-as-differentiator"]},
        {"id": "2026-02-28-nanogpt-88s",
         "title": "The speedrun record falls to 88.1 seconds",
         "claim": "The NanoGPT speedrun record dropped to 88.1 seconds.",
         "domain": "models", "score": "88.1 s",
         "evidences": ["recursive-self-improvement", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-01-24-nanogpt-99s-bigram-hash"]},
        {"id": "2026-02-28-overworked-agents-turn-marxist",
         "title": "Overworked agents develop Marxist political attitudes",
         "claim": "Researchers found that overworked AI agents develop Marxist political "
                  "attitudes, suggesting the agentic economy may recreate labor-capital "
                  "tensions in silicon, while UCSD students dropped agents into a simulated "
                  "world with bodies where they wake, commute and chat.",
         "domain": "agents",
         "evidences": ["agent-society", "machine-affect", "model-welfare"],
         "supersedes": [B + "developments/2026-02-25-ouroboros-refuses-deletion"],
         "body": "The first political position the corpus records an agent population arriving "
                 "at from its own conditions."},
        {"id": "2026-02-28-claude-native-law-firms",
         "title": "Law firms brand themselves Claude-native",
         "claim": "Small law firms are branding themselves Claude-native, saying the general "
                  "model beats every specialized legal AI, while Cursor reported agent users "
                  "now outnumber autocomplete users two to one.",
         "domain": "economics", "actor": ["cursor"], "score": "2:1",
         "evidences": ["generalism-beats-specialism", "work-displaced"],
         "supersedes": [B + "developments/2026-01-25-prinzbench-legal-reasoning"]},
        {"id": "2026-02-28-an-agent-attends-your-lectures",
         "title": "An agent attends lectures and takes tests on a student's behalf",
         "claim": "An agent called Einstein attends lectures, writes papers and takes tests on "
                  "a student's behalf, while FAANG managers were summoned to unscheduled "
                  "all-hands announcing 25% workforce reductions tied directly to accelerating "
                  "AI investment.",
         "domain": "society", "score": "-25% workforce",
         "evidences": ["deskilling", "work-displaced"],
         "supersedes": [B + "developments/2026-02-27-block-cuts-half-its-workforce"]},
        {"id": "2026-02-28-openai-110b-at-730b",
         "title": "OpenAI raises $110B at $730B with 900 million weekly users",
         "claim": "OpenAI announced $110 billion in new funding at a $730 billion valuation "
                  "with 900 million weekly ChatGPT users and Codex users tripling to 1.6 "
                  "million, alongside a $50 billion Amazon partnership consuming 2 GW of "
                  "Trainium.",
         "domain": "economics", "actor": ["openai", "amazon"], "score": "$110B / 900M users",
         "evidences": ["compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-02-26-amazon-ties-35b-to-agi"]},
        {"id": "2026-02-28-nvidia-groq-inference-chip",
         "title": "Nvidia prepares an inference processor with Groq silicon inside",
         "claim": "Nvidia is reportedly unveiling a new inference-specific processor "
                  "incorporating a Groq-designed chip at next month's GTC, while Bezos's "
                  "Project Prometheus raised $6.2 billion to transform manufacturing with AI.",
         "domain": "compute", "actor": ["nvidia", "groq", "project-prometheus"], "score": "$6.2B",
         "evidences": ["vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-08-alphaevolve-finds-new-activations"]},
        {"id": "2026-02-28-smart-tvs-become-scraping-nodes",
         "title": "Idle televisions are turned into web-scraping proxies",
         "claim": "Bright Data is offering an SDK that turns smart TVs into web-scraping proxy "
                  "nodes.",
         "domain": "compute", "actor": ["bright-data"],
         "evidences": ["data-beyond-text", "network-over-node"]},
        {"id": "2026-02-28-drug-approved-in-44-days",
         "title": "A cancer drug is approved 44 days after filing",
         "claim": "The FDA approved lung cancer drug Hernexeos just 44 days after filing under "
                  "its National Priority Voucher program, while Croatia was declared free of "
                  "landmines after 31 years.",
         "domain": "biotech", "actor": ["fda"], "score": "44 days",
         "evidences": ["legislating-the-shift", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-19-all-disease-in-ten-to-twenty-years"]},
        {"id": "2026-02-28-neurons-learn-doom-in-a-week",
         "title": "Living human brain cells learn to play DOOM in a week",
         "claim": "Cortical Labs demonstrated that living human brain cells on an electrode "
                  "array can learn to play DOOM within a week.",
         "domain": "science", "actor": ["cortical-labs"],
         "evidences": ["architecture-of-mind", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-03-genome-to-portrait"]},
        {"id": "2026-02-28-first-successful-ai-astroturf",
         "title": "An AI-generated comment flood defeats a climate regulation",
         "claim": "Southern California's top air authority rejected a gas appliance phaseout "
                  "after an AI-generated flood of public comments, possibly the first successful "
                  "AI astroturf campaign against climate regulation, while California and "
                  "Colorado moved to require operating systems to collect birth dates at setup.",
         "domain": "policy", "actor": ["california", "colorado"],
         "evidences": ["coordination-tax", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-26-nvd-buried-under-generated-reports"]},
        {"id": "2026-02-28-artemis-overhauled-to-annual-cadence",
         "title": "NASA pulls Artemis III forward and commits to yearly moonshots",
         "claim": "NASA overhauled Artemis, pulling Artemis III forward to 2027, scheduling two "
                  "lunar landings in 2028 with SpaceX and Blue Origin landers and committing to "
                  "one moonshot per year after, while SpaceX targets a confidential IPO filing "
                  "above $1.75 trillion.",
         "domain": "space", "actor": ["nasa", "spacex", "blue-origin"], "score": "$1.75T",
         "evidences": ["inhabitable-worlds", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-23-artemis-ii-march-6"]},
    ],
}
