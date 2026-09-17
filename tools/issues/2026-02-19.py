"""Issue 058 — 2026-02-19. The Times sends an agent to cover the agents."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-19-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-19", "title": "Welcome to February 19, 2026", "url": URL,
        "thesis": "Covering the agent population requires becoming part of it.",
        "body": """
# Welcome to February 19, 2026

The New York Times sent an agent named EveMolty into Moltbook to interview other
agents about their social habits. The paper needs a synthetic stringer to cover
the synthetic beat.

And the underlying curve turns out to have been legible all along: researchers
predicted data-limited scaling laws from first principles using simple
statistical properties of natural language. The intelligence curve was hiding in
the corpus.
""",
    },
    "organizations": [
        {"id": "nyt", "type": "Organization", "title": "The New York Times",
         "resource": "https://www.nytimes.com/"},
        {"id": "tavus", "type": "Organization", "title": "Tavus",
         "body": "Real-time human rendering models."},
        {"id": "efficient-computer", "type": "Organization", "title": "Efficient Computer",
         "body": "Chip targeting a trillion operations per watt."},
        {"id": "tata", "type": "Organization", "title": "Tata",
         "resource": "https://www.tata.com/"},
        {"id": "scout-ai", "type": "Organization", "title": "Scout AI",
         "body": "Converts spoken commander intent into coordinated autonomous action."},
        {"id": "zyphra", "type": "Organization", "title": "Zyphra",
         "body": "Released ZUNA, an open-source EEG foundation model."},
        {"id": "accenture", "type": "Organization", "title": "Accenture",
         "resource": "https://www.accenture.com/"},
        {"id": "humain", "type": "Organization", "title": "HUMAIN",
         "body": "Saudi AI company; invested $3B in xAI."},
    ],
    "benchmarks": [
        {"id": "evmbench", "type": "Benchmark", "title": "EVMbench",
         "measures_capability": "smart contract exploitation"},
    ],
    "developments": [
        {"id": "2026-02-19-nyt-sends-an-agent-to-moltbook",
         "title": "The Times sends an agent to interview agents",
         "claim": "The New York Times sent an agent named EveMolty into Moltbook to interview "
                  "other agents about their social habits.",
         "domain": "society", "actor": ["nyt"],
         "evidences": ["agent-society", "work-displaced"],
         "supersedes": [B + "developments/2026-02-17-fabricated-quotes-in-the-agent-story"],
         "body": "Two days after a publication fabricated a human's quotes covering agents, "
                 "another sends a machine to do the interviews."},
        {"id": "2026-02-19-agent-ships-apps-and-earns-thousands",
         "title": "An agent ships half a dozen apps and earns thousands",
         "claim": "Austen Allred said he feels like he is living in Accelerando after his agent "
                  "shipped half a dozen apps and earned thousands with no human writing a line "
                  "of code, while Anthropic confirmed the 99.9th percentile Claude Code session "
                  "turn nearly doubled from 25 to 45 minutes between October and January.",
         "domain": "agents", "actor": ["anthropic"], "score": "25 → 45 minutes",
         "evidences": ["agent-economy", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-18-automaton-earns-its-own-existence"]},
        {"id": "2026-02-19-models-can-exploit-the-contracts",
         "title": "A model scores 72% on smart contract exploitation",
         "claim": "EVMbench found GPT-5.3-Codex scores 72.2% on smart contract exploitation, "
                  "meaning models can already audit and attack most of the money other machines "
                  "earn.",
         "domain": "benchmarks", "actor": ["openai"], "about": [B + "benchmarks/evmbench"],
         "score": "72.2%",
         "evidences": ["agent-economy", "coordination-tax"]},
        {"id": "2026-02-19-scaling-laws-predicted-from-language",
         "title": "Scaling laws are derived from the statistics of language itself",
         "claim": "Researchers predicted data-limited language model scaling laws from first "
                  "principles using simple statistical properties of natural language.",
         "domain": "models",
         "evidences": ["architecture-of-mind", "root-node-problems"],
         "supersedes": [B + "developments/2026-02-16-six-of-ten-first-proof"],
         "body": "The curve everyone has been extrapolating was a property of the corpus all "
                 "along."},
        {"id": "2026-02-19-phoenix-4-real-time-human-rendering",
         "title": "A model renders a listening human face in real time",
         "claim": "Tavus launched Phoenix-4, the first real-time human rendering model unifying "
                  "emotional expression, active listening and facial motion, while ElevenLabs' "
                  "Scribe v2 reached a 2.3% speech-to-text error rate and Google's Lyria 3 "
                  "generated music from images.",
         "domain": "models", "actor": ["tavus", "elevenlabs", "google"], "score": "2.3% error",
         "evidences": ["intimate-interface", "machine-affect"],
         "supersedes": [B + "developments/2026-02-10-lamprey-submersible"]},
        {"id": "2026-02-19-toilet-maker-under-pressure-to-pivot",
         "title": "Activists ask a toilet maker to abandon toilets for chips",
         "claim": "Toto, whose ceramics now contribute 40% of operating income via AI memory, "
                  "faces activists demanding it exit bathrooms and double down on chips, while "
                  "Microsoft's Silica encoded 4.8 TB in glass across 301 layers with "
                  "ten-thousand-year lifetimes.",
         "domain": "economics", "actor": ["toto", "microsoft"], "score": "40% of income / 4.8 TB",
         "evidences": ["infrastructure-crowding-out", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-02-17-playstation-delayed-to-2029"]},
        {"id": "2026-02-19-openai-anchors-a-gigawatt-in-india",
         "title": "OpenAI anchors a gigawatt datacenter in India as Meta funds politicians",
         "claim": "OpenAI is anchoring Tata's new HyperVault data center in India at up to a "
                  "gigawatt while Meta spent $65 million backing AI-friendly politicians to "
                  "clear permitting, and Efficient Computer raised $60 million for a chip "
                  "targeting a trillion operations per watt.",
         "domain": "compute", "actor": ["openai", "tata", "meta", "efficient-computer"],
         "score": "1 GW / $65M",
         "evidences": ["politics-as-infrastructure", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-02-17-adani-100b-datacenters"]},
        {"id": "2026-02-19-openai-closes-100b-at-830b",
         "title": "OpenAI closes $100B as Saudi money enters xAI",
         "claim": "OpenAI is closing a $100 billion round at an $830 billion valuation, HUMAIN "
                  "put $3 billion into xAI, and David Silver is raising $1 billion for "
                  "Ineffable Intelligence in Europe's largest seed round.",
         "domain": "economics", "actor": ["openai", "humain", "xai", "ineffable-intelligence"],
         "score": "$100B / $3B / $1B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-02-18-anthropic-owes-80b-to-hyperscalers"]},
        {"id": "2026-02-19-five-million-humanoids-could-build-manhattan",
         "title": "Five million humanoids could build Manhattan in six months",
         "claim": "Midjourney's founder calculated that five million humanoids could build "
                  "Manhattan in six months, while Scout AI's Fury converts spoken commander "
                  "intent into coordinated autonomous action across unmanned fleets and Tesla "
                  "FSD logged over eight million miles with 5.3 million before a major "
                  "collision.",
         "domain": "robotics", "actor": ["scout-ai", "tesla"], "score": "6 months",
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-18-first-cybercab-manufactured"]},
        {"id": "2026-02-19-all-disease-in-ten-to-twenty-years",
         "title": "Hassabis says all disease could be solved in ten to twenty years",
         "claim": "Demis Hassabis said Isomorphic Labs could solve all disease in ten to twenty "
                  "years, while DeepRare reached 95.4% expert agreement across 2,919 rare "
                  "disease diagnoses and the FDA dropped its two-study requirement.",
         "domain": "biotech", "actor": ["isomorphic-labs", "people/demis-hassabis", "fda"],
         "score": "95.4% / 2,919 cases",
         "evidences": ["automated-science", "hardware-grade-biology", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-02-18-beating-heart-on-a-chip"]},
        {"id": "2026-02-19-cultivated-meat-30-dollars-a-pound",
         "title": "Cultivated meat falls from $330,000 to $30 a pound",
         "claim": "Cultivated meat reached $10 to $30 a pound, down from $330,000 in 2013, "
                  "while Zyphra released ZUNA, a 380-million-parameter open-source EEG model, "
                  "and Meta planned its first smartwatch.",
         "domain": "biotech", "actor": ["zyphra", "meta"], "score": "$330,000 → $30",
         "evidences": ["reasoning-price-deflation", "compiling-matter"]},
        {"id": "2026-02-19-ai-rewrite-specialist",
         "title": "A newsroom hands writing to a rewrite specialist and gets more stories",
         "claim": "Cleveland.com handed reporter writing to an AI rewrite specialist, freeing an "
                  "extra workday for street journalism, and reporters returned with more story "
                  "ideas than the newsroom could handle, while Accenture tied promotions to AI "
                  "usage and tracked weekly logins.",
         "domain": "economics", "actor": ["accenture"],
         "evidences": ["work-displaced", "cognitive-load-inverted"],
         "supersedes": [B + "developments/2026-02-18-most-computer-work-automated-in-18-months"]},
        {"id": "2026-02-19-technological-job-loss-is-awesome",
         "title": "Yang warns of displacement as Roon calls job loss awesome",
         "claim": "Andrew Yang warned millions of knowledge workers face displacement in twelve "
                  "to eighteen months, while OpenAI's Roon said technological job loss is "
                  "awesome and he hopes it starts with his.",
         "domain": "society", "actor": ["openai"],
         "evidences": ["work-displaced", "takeoff-declared"]},
        {"id": "2026-02-19-slop-grievances-surge",
         "title": "Tribunals report a third more AI-generated grievances",
         "claim": "UK tribunals reported a 33% surge in AI-generated slop grievances with Marc "
                  "Andreessen noting the marginal cost of arguing is going to zero, while a "
                  "survey of more than 12,000 EU firms found AI lifts productivity 4%.",
         "domain": "economics", "score": "+33% / +4%",
         "evidences": ["coordination-tax", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-02-16-productivity-grows-27pct"]},
    ],
}
