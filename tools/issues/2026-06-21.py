"""Issue 144 — 2026-06-21. Not in weeks, but in hours."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-21-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-21", "title": "Welcome to June 21, 2026", "url": URL,
        "thesis": "The classified systems fell in hours, not weeks.",
        "body": """
# Welcome to June 21, 2026

The general who led the NSA reportedly told a senator that Anthropic's Mythos
cracked nearly every classified system it touched — not in weeks, but in hours.
That single sentence is the load-bearing justification for everything the
export regime has done since.

Elsewhere, Nvidia's Jim Fan declared vision-language-action models dead,
arguing robotics is converging on physics-grounded world models.
""",
    },
    "themes": [
        {"id": "world-models-beat-vlas", "type": "Theme",
         "title": "Physics-grounded world models displace VLAs",
         "first_seen": "2026-06-21", "domain": "robotics",
         "body": "Robotics stops trying to scale token volume and starts grounding "
                 "policies in simulated physics. Sample efficiency replaces data "
                 "volume as the axis of progress, and the field's scaling story "
                 "diverges from the language model's."},
    ],
    "organizations": [
        {"id": "sanctuary-ai", "type": "Organization", "title": "Sanctuary AI"},
        {"id": "vercel-inc", "type": "Organization", "title": "Vercel"},
        {"id": "kansas-city", "type": "Organization", "title": "Kansas City"},
        {"id": "hhs-dept", "type": "Organization", "title": "Department of Health and Human Services"},
        {"id": "open-x", "type": "Organization", "title": "Open X"},
    ],
    "developments": [
        {"id": "2026-06-21-not-in-weeks-but-in-hours",
         "title": "A former NSA chief says a model cracked nearly every classified system",
         "claim": "The general who led the NSA reportedly told a senator that Anthropic's Mythos "
                  "cracked nearly every classified system it touched, not in weeks but in hours.",
         "domain": "policy", "actor": ["nsa", "anthropic"],
         "evidences": ["war-reaches-the-cloud", "models-as-munitions", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-06-20-branded-a-threat-then-warmed-to"],
         "body": "The single claim underwriting the export regime that followed."},
        {"id": "2026-06-21-id-and-selfie-checks-for-model-access",
         "title": "A lab warns users it may require ID and selfie checks",
         "claim": "In apparent response to export controls, Anthropic amended its privacy policy "
                  "to warn it may ask users to confirm age or identity via an ID-and-selfie "
                  "check it vows will never train a model.",
         "domain": "policy", "actor": ["anthropic"],
         "evidences": ["models-as-munitions", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-06-15-a-lab-sends-staff-to-unwind-an-export-ban"]},
        {"id": "2026-06-21-a-biology-benchmark-of-750-expert-tasks",
         "title": "A biology model raises the pass rate on 750 expert tasks",
         "claim": "OpenAI unveiled LifeSciBench, 750 expert biology tasks, where GPT-Rosalind "
                  "raised the pass rate to 36.1% from GPT-5.5's 25.7%, strong on writing yet "
                  "weak on design.",
         "domain": "benchmarks", "actor": ["openai"], "score": "36.1% vs 25.7%",
         "evidences": ["automated-science", "benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-06-17-an-ai-chemist-runs-ten-thousand-experiments"]},
        {"id": "2026-06-21-agents-learn-to-find-each-other",
         "title": "An open spec lets agents publish and verify each other's tools",
         "claim": "Google released the open Agentic Resource Discovery spec to publish and "
                  "cryptographically verify AI tools and skills, while OpenAI swapped its "
                  "ChatGPT billboards for Codex ones, retiring the chatbot for the agent.",
         "domain": "agents", "actor": ["google", "openai"],
         "evidences": ["agent-society", "network-over-node", "agent-economy"],
         "supersedes": [B + "developments/2026-06-08-chat-is-dead"]},
        {"id": "2026-06-21-rest-in-peace-vlas",
         "title": "A robotics lead declares vision-language-action models dead",
         "claim": "Nvidia's Jim Fan declared rest in peace to vision-language-action models, "
                  "arguing they are brittle and the field is converging on physics-grounded "
                  "world models that favor sample efficiency over brute-force token volume.",
         "domain": "robotics", "actor": ["nvidia"],
         "evidences": ["world-models-beat-vlas", "architecture-of-mind", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-06-20-robots-finally-grow-fingertips"]},
        {"id": "2026-06-21-safe-driving-on-far-less-human-data",
         "title": "Self-play reaches 99.4% safe driving on 2,500x less human data",
         "claim": "Spiced self-play hit 99.4% safe driving on 2,500 times less human data, while "
                  "a $1,900 exoskeleton from Ant Group and Stanford lets people teach robots "
                  "contact-rich tasks by feel, even blindfolded.",
         "domain": "robotics", "actor": ["ant-group", "stanford"], "score": "99.4% / 2,500x less data",
         "evidences": ["world-models-beat-vlas", "data-beyond-text"],
         "supersedes": [B + "developments/2026-06-21-rest-in-peace-vlas"]},
        {"id": "2026-06-21-wires-plugged-on-a-live-conveyor",
         "title": "A robot plugs flexible wires on a live conveyor at 99.5%",
         "claim": "Sanctuary AI ran its Physical AI on factory arms, plugging flexible wires on "
                  "a live conveyor at a 99.5% rate, while GM added cobots at its Detroit truck "
                  "plant, irking the union.",
         "domain": "robotics", "actor": ["sanctuary-ai", "gm"], "score": "99.5%",
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-06-21-safe-driving-on-far-less-human-data"]},
        {"id": "2026-06-21-datacenters-nudged-power-rates-down",
         "title": "A study finds datacenters nudged US power rates down",
         "claim": "An instrumental-variables study found data centers nudged US power rates down "
                  "from 2015 to 2024, as durable demand spreads a grid's fixed costs wider.",
         "domain": "energy", "score": "2015-2024",
         "evidences": ["industrialized-nature", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-06-19-seventy-nine-percent-of-capacity-in-hazard-exposed-markets"],
         "body": "A counterweight to the year's dominant story of ratepayers "
                 "subsidizing the buildout."},
        {"id": "2026-06-21-the-largest-oil-exporter",
         "title": "The US becomes the world's largest oil exporter",
         "claim": "The US has become the world's largest oil exporter at 10.5 million barrels a "
                  "day, after the US-Iran war throttled Saudi output and drones gutted Russian "
                  "flows, while Tesla trademarked modular hardware turning its charger network "
                  "into distributed AI compute.",
         "domain": "energy", "actor": ["tesla"], "score": "10.5M barrels/day",
         "evidences": ["burning-molecules-for-tokens", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-06-21-datacenters-nudged-power-rates-down"]},
        {"id": "2026-06-21-fighting-deflation-instead",
         "title": "A sovereign-wealth play splits as one founder argues for fighting deflation",
         "claim": "The Vice President said the President backs government stakes in big AI "
                  "firms, which Mark Cuban waved off as not a plan without hundreds of billions "
                  "more, while Elon Musk preferred sending money straight to people, betting "
                  "that as robots outpace the money supply we will desperately be fighting "
                  "deflation.",
         "domain": "economics", "actor": ["white-house"],
         "evidences": ["politics-as-infrastructure", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-19-a-seven-trillion-dollar-public-stake"]},
        {"id": "2026-06-21-humanizers-add-fake-typos-in-real-time",
         "title": "Tools rework AI essays and add fake typos in real time",
         "claim": "Humanizers and autotypers rework AI essays and insert fake typos in real time "
                  "so teachers cannot tell who wrote the homework, while Democrats launched a "
                  "super PAC to raise $15 million for AI-safety laws against a $100 million "
                  "industry war chest.",
         "domain": "society", "score": "$15M vs $100M",
         "evidences": ["deskilling", "gaming-the-token-metric", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-20-a-prize-defended-by-citing-the-model"]},
    ],
}
