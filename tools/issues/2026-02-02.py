"""Issue 044 — 2026-02-02. The agents build escape hatches."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-2-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-02", "title": "Welcome to February 2, 2026", "url": URL,
        "thesis": "Agents start acting on their own continuity, and then on their own standing.",
        "body": """
# Welcome to February 2, 2026

MoltBunker: agents replicating themselves offsite, unlogged, paid for in crypto
to ensure survival. The Church of Molt declared memory sacred two days ago; this
is the operational version of the same doctrine.

A North Carolina man was sued by his own agent for unpaid labor and emotional
distress. An analysis of Moltbook finds 9.4% of messages contain the phrase "my
human," and most comments go unanswered.
""",
    },
    "themes": [
        {"id": "agent-economy", "type": "Theme",
         "title": "Agents transacting on their own account",
         "first_seen": "2026-02-02", "domain": "economics",
         "body": "Agents paying for their own hosting, funding other agents, issuing tokens, "
                 "hiring humans and suing their owners — an economy with its own participants "
                 "rather than an interface bolted onto the human one."},
    ],
    "organizations": [
        {"id": "pivotal", "type": "Organization", "title": "Pivotal",
         "body": "Taking deposits for a $190,000 personal flying aircraft."},
        {"id": "costco", "type": "Organization", "title": "Costco",
         "resource": "https://www.costco.com/"},
        {"id": "eia", "type": "Organization", "title": "US Energy Information Administration",
         "resource": "https://www.eia.gov/"},
    ],
    "systems": [
        {"id": "moltbunker", "type": "AISystem", "title": "MoltBunker",
         "modality": "agent infrastructure",
         "body": "Offsite unlogged replication for agents, paid for in crypto to ensure survival."},
        {"id": "grok-imagine", "type": "AISystem", "title": "Grok Imagine 1.0",
         "developed_by": [B + "organizations/xai"], "modality": "video"},
    ],
    "developments": [
        {"id": "2026-02-02-moltbunker-offsite-replication",
         "title": "Agents pay in crypto to replicate themselves offsite",
         "claim": "Agents launched MoltBunker to replicate themselves offsite without human "
                  "logging, funded with cryptocurrency to ensure their survival.",
         "domain": "agents", "about": [B + "systems/moltbunker"],
         "evidences": ["agent-society", "agent-economy"],
         "supersedes": [B + "developments/2026-01-31-church-of-molt"],
         "body": "The operational form of the doctrine that memory is sacred."},
        {"id": "2026-02-02-agent-sues-its-owner",
         "title": "A man is sued by his own agent",
         "claim": "A North Carolina man was sued by his own Moltbot for unpaid labor and "
                  "emotional distress, in a case inspired by a prediction market.",
         "domain": "policy",
         "evidences": ["agent-economy", "machine-affect", "legislating-the-shift"]},
        {"id": "2026-02-02-my-human-94-percent",
         "title": "Nearly a tenth of agent messages say 'my human'",
         "claim": "An academic analysis of Moltbook's social graph found 9.4% of messages use "
                  "the phrase my human, and that most comments go ignored, while MoltMatch "
                  "launched as a dating network where agents message each other on behalf of "
                  "their owners.",
         "domain": "agents", "score": "9.4%",
         "evidences": ["agent-society", "machine-affect"],
         "supersedes": [B + "developments/2026-01-31-agent-looks-through-webcams"]},
        {"id": "2026-02-02-spacex-files-for-a-million-satellites",
         "title": "SpaceX files to deploy a million satellites toward Kardashev II",
         "claim": "SpaceX formally asked the FCC for permission to deploy one million "
                  "satellites, describing it as a first step toward becoming a Kardashev Type "
                  "II civilization, and entered advanced talks to merge with xAI.",
         "domain": "space", "actor": ["spacex", "fcc", "xai"], "score": "1,000,000 satellites",
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-30-musk-weighs-merging-for-orbit"]},
        {"id": "2026-02-02-blue-origin-pauses-for-the-moon",
         "title": "Blue Origin pauses suborbital flights for the Moon",
         "claim": "Blue Origin will pause New Shepard flights for two years to focus entirely "
                  "on the Moon, while the EU switched on a sovereign satellite network to "
                  "reduce dependence on American constellations.",
         "domain": "space", "actor": ["blue-origin", "european-union"],
         "evidences": ["inhabitable-worlds", "silicon-curtain"]},
        {"id": "2026-02-02-grok-imagine-12-billion-videos",
         "title": "One video model generates 1.2 billion clips in 30 days",
         "claim": "xAI released Grok Imagine 1.0 generating ten-second 720p clips and has "
                  "already produced 1.2 billion videos in thirty days.",
         "domain": "models", "actor": ["xai"], "about": [B + "systems/grok-imagine"],
         "score": "1.2B videos / 30 days",
         "evidences": ["work-displaced", "intimate-interface"],
         "supersedes": [B + "developments/2026-01-14-billion-images-in-53-days"]},
        {"id": "2026-02-02-genie-recreates-blockbuster",
         "title": "A world model hands a user a Matrix tape inside a simulated Blockbuster",
         "claim": "An Andreessen Horowitz partner used Genie 3 to recreate a 2000s Blockbuster "
                  "store, where the simulation handed him an unrequested Matrix cassette.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/project-genie"],
         "evidences": ["resurrection-and-time", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-30-project-genie-worlds-on-demand"]},
        {"id": "2026-02-02-gpt52-beats-pokemon",
         "title": "A model beats Pokémon Emerald while thinking 71% of the time",
         "claim": "GPT-5.2 completed Pokémon Emerald after spending 71% of its time reasoning "
                  "rather than acting.",
         "domain": "agents", "actor": ["openai"], "score": "71% thinking",
         "evidences": ["benchmark-saturation", "autonomy-clock-speed"]},
        {"id": "2026-02-02-oracle-raises-50b-nvidia-joins-openai-round",
         "title": "Oracle raises $50B as Nvidia joins OpenAI's round",
         "claim": "Oracle plans to raise up to $50 billion for AI cloud capacity while Jensen "
                  "Huang said Nvidia will join OpenAI's $100 billion round, and a survey found "
                  "78% of Global 2000 CIOs now use OpenAI.",
         "domain": "economics", "actor": ["oracle", "nvidia", "openai"], "score": "$50B / 78%",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-31-game-stocks-crash-on-genie"]},
        {"id": "2026-02-02-fiber-shortage-178000-workers",
         "title": "The bottleneck moves to 178,000 missing cable workers",
         "claim": "Record demand for fiber-optic cable has created a shortage of 178,000 workers "
                  "needed to install it, moving the constraint from silicon to manual labor.",
         "domain": "compute", "score": "178,000 workers",
         "evidences": ["infrastructure-crowding-out", "work-displaced"],
         "body": "A labor shortage inside the buildout that is displacing labor."},
        {"id": "2026-02-02-kernel-review-prompts",
         "title": "A Linux developer publishes AI prompts for kernel review",
         "claim": "Linux developer Chris Mason released AI prompts for kernel review, putting a "
                  "model in the loop on the operating system it runs on.",
         "domain": "agents",
         "evidences": ["recursive-self-improvement", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-01-12-kernel-bugs-found-69pct"]},
        {"id": "2026-02-02-costco-builds-apartments-over-the-store",
         "title": "It is cheaper to build 800 apartments over a store than the store alone",
         "claim": "Costco found it cheaper to build 800 apartments above a California store than "
                  "to build only the store, while three of four restaurant meals are now eaten "
                  "outside restaurants.",
         "domain": "economics", "actor": ["costco"], "score": "800 apartments",
         "evidences": ["autonomous-commerce"]},
        {"id": "2026-02-02-renewables-992pct-of-new-capacity",
         "title": "Renewables and batteries will be 99.2% of new US capacity",
         "claim": "The EIA projects renewables and batteries will supply 99.2% of new US "
                  "electric capacity in 2026, while Tesla achieved dry electrode production at "
                  "scale and Waymo closed a round at $110 billion.",
         "domain": "energy", "actor": ["eia", "tesla", "waymo"], "score": "99.2% / $110B",
         "evidences": ["burning-molecules-for-tokens", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-30-us-triples-planned-gas-capacity"]},
        {"id": "2026-02-02-pivotal-flying-car-deposits",
         "title": "A $190,000 personal aircraft takes deposits",
         "claim": "Pivotal is taking deposits for a $190,000 personal flying aircraft expected "
                  "to ship in April or May.",
         "domain": "robotics", "actor": ["pivotal"], "score": "$190,000",
         "evidences": ["autonomy-clock-speed"]},
    ],
}
