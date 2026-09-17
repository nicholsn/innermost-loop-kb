"""Issue 091 — 2026-04-05. Self-distillation without a teacher."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-5-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-05", "title": "Welcome to April 5, 2026", "url": URL,
        "thesis": "A model improves by sampling itself, with no verifier, teacher or reward.",
        "body": """
# Welcome to April 5, 2026

Apple showed models can self-improve at coding through simple self-distillation
— sampling their own outputs and fine-tuning on them with no verifier, no
teacher and no reinforcement learning — lifting one model from 42.4% to 55.3% on
LiveCodeBench, with gains concentrated on the hardest problems.

Meta translated an entire graduate mathematics textbook into Lean using 30,000
agents, turning proof into a parallelizable compute job.
""",
    },
    "organizations": [
        {"id": "gladstone", "type": "Organization", "title": "Gladstone Institutes",
         "resource": "https://gladstone.org/"},
        {"id": "irena", "type": "Organization", "title": "IRENA",
         "resource": "https://www.irena.org/"},
        {"id": "cu-boulder", "type": "Organization", "title": "University of Colorado Boulder",
         "resource": "https://www.colorado.edu/"},
        {"id": "planet-labs", "type": "Organization", "title": "Planet Labs",
         "resource": "https://www.planet.com/"},
    ],
    "developments": [
        {"id": "2026-04-05-self-distillation-without-a-teacher",
         "title": "A model improves by fine-tuning on its own samples",
         "claim": "Apple researchers showed language models can self-improve at coding through "
                  "simple self-distillation, sampling their own outputs and fine-tuning on them "
                  "with no verifier, teacher or reinforcement learning, lifting one model from "
                  "42.4% to 55.3% on LiveCodeBench with gains concentrated on the hardest "
                  "problems.",
         "domain": "models", "actor": ["apple"], "score": "42.4% → 55.3%",
         "evidences": ["recursive-self-improvement", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-03-31-bilevel-autoresearch"]},
        {"id": "2026-04-05-a-textbook-formalized-by-30000-agents",
         "title": "Thirty thousand agents formalize a graduate textbook",
         "claim": "Meta researchers translated an entire graduate mathematics textbook into "
                  "Lean using 30,000 language model agents, turning formalization into a "
                  "parallelizable compute job.",
         "domain": "science", "actor": ["meta"], "score": "30,000 agents",
         "evidences": ["automated-science", "network-over-node"],
         "supersedes": [B + "developments/2026-04-01-three-more-erdos-problems"]},
        {"id": "2026-04-05-mrna-models-for-165-dollars",
         "title": "mRNA language models across 25 species are trained for $165",
         "claim": "Open-source labs are training mRNA language models across 25 species for "
                  "$165, while Gladstone Institutes and Nvidia unveiled a temporal model trained "
                  "on nearly a trillion gene tokens that simulates cell-state trajectories "
                  "across the human lifespan.",
         "domain": "biotech", "actor": ["gladstone", "nvidia"], "score": "$165 / 1T gene tokens",
         "evidences": ["reasoning-price-deflation", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-04-03-anthropic-buys-a-drug-discovery-company"]},
        {"id": "2026-04-05-copilot-inside-copilot",
         "title": "One brand name is applied to 78 separate products",
         "claim": "Microsoft has applied the name Copilot to 78 separately marketed products, "
                  "producing Copilots inside Copilots and a physical key for summoning them, "
                  "while quietly noting the assistant is for entertainment purposes only.",
         "domain": "economics", "actor": ["microsoft"], "score": "78 products",
         "evidences": ["coordination-tax", "software-margin-collapse"]},
        {"id": "2026-04-05-a-terminal-inside-doom",
         "title": "A coding agent is embedded inside a game so players can task it mid-level",
         "claim": "OpenAI's Codex modified the DOOM engine so players can walk up to a rendered "
                  "terminal inside the game and ask it to work on their code mid-level, while "
                  "developers cut token usage roughly 75% by having the model talk like a "
                  "caveman while keeping technical accuracy.",
         "domain": "agents", "actor": ["openai"], "score": "-75% tokens",
         "evidences": ["reasoning-price-deflation", "engineer-as-supervisor"]},
        {"id": "2026-04-05-anthropic-prices-out-third-party-agents",
         "title": "A lab makes subscribers pay extra for third-party agent access",
         "claim": "Anthropic effectively banned OpenClaw from non-API Claude by making "
                  "subscribers pay extra for third-party tool access.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["agent-exclusion", "agent-economy"],
         "supersedes": [B + "developments/2026-03-22-lobsters-go-mainstream-in-china"]},
        {"id": "2026-04-05-half-of-us-datacenters-may-slip",
         "title": "Half of planned US datacenters may slip for want of transformers",
         "claim": "Almost half of US data centers planned for this year are expected to be "
                  "delayed or cancelled because of shortages of transformers, switchgear and "
                  "batteries, despite electrical gear representing under 10% of total cost, "
                  "while Microsoft committed $10 billion to Japan by 2029.",
         "domain": "compute", "actor": ["microsoft"], "score": "~50% delayed",
         "evidences": ["infrastructure-crowding-out", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-04-02-data-heat-island-effect"]},
        {"id": "2026-04-05-tesla-calls-its-research-fab-heaven",
         "title": "Tesla's research fab puts logic, memory, packaging and masks in one building",
         "claim": "Elon Musk said Tesla's new chip research fab will host logic, memory, "
                  "packaging and masks in one building for a fast development cycle, and calls "
                  "it Heaven.",
         "domain": "compute", "actor": ["tesla"],
         "evidences": ["silicon-designs-itself", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-23-terafab-one-billion-chips-a-year"]},
        {"id": "2026-04-05-renewables-856-percent-of-new-capacity",
         "title": "Renewables are 85.6% of new global capacity",
         "claim": "IRENA reported renewables accounted for 85.6% of new global capacity last "
                  "year, pushing renewables to 49.4% of total installed capacity worldwide.",
         "domain": "energy", "actor": ["irena"], "score": "85.6% of new / 49.4% of total",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-03-29-microreactors-by-independence-day"]},
        {"id": "2026-04-05-an-appetite-suppressant-from-python-blood",
         "title": "A compound in python blood suppresses appetite without nausea",
         "claim": "Colorado researchers discovered a compound in python blood that lets snakes "
                  "eat enormous meals and fast for months while staying metabolically healthy, "
                  "suppressing food intake and weight in obese mice without the nausea of GLP-1 "
                  "drugs.",
         "domain": "biotech", "actor": ["cu-boulder"],
         "evidences": ["hardware-grade-biology", "discovery-as-process"],
         "supersedes": [B + "developments/2026-03-29-a-living-pharmacy-implant"]},
        {"id": "2026-04-05-unicorn-founders-get-younger",
         "title": "The average AI unicorn founder gets eleven years younger",
         "claim": "The average age of AI unicorn founders fell from 40 in 2020 to 29 in 2024 as "
                  "dropouts overtook doctorates at the frontier, while a field experiment on "
                  "515 high-growth startups found firms given information about AI "
                  "reorganization used 44% more AI and generated 1.9 times higher revenue.",
         "domain": "economics", "score": "40 → 29 years old",
         "evidences": ["ladder-pulled-up", "one-person-company"],
         "supersedes": [B + "developments/2026-04-03-first-one-person-unicorn"]},
        {"id": "2026-04-05-eight-hundred-sanctions-for-hallucinated-briefs",
         "title": "Eight hundred court sanctions are issued for hallucinated filings",
         "claim": "Roughly 800 US court sanctions have been issued against attorneys for filing "
                  "AI-hallucinated briefs, while Colorado deployed an automated vehicle "
                  "identification system computing average speed across cameras and "
                  "auto-ticketing anyone ten miles per hour over.",
         "domain": "policy", "actor": ["colorado-state"], "score": "~800 sanctions",
         "evidences": ["coordination-tax", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-31-eyewear-banned-from-courts"],
         "body": "Automated enforcement arriving faster than automated adjudication."},
        {"id": "2026-04-05-uk-courts-a-dual-listing",
         "title": "The UK courts a blacklisted lab for a dual listing",
         "claim": "The United Kingdom is courting Anthropic for a dual US-UK listing amid the "
                  "lab's fight with the Department of War.",
         "domain": "policy", "actor": ["uk-govt", "anthropic"],
         "evidences": ["refusal-as-differentiator", "regulatory-exit"],
         "supersedes": [B + "developments/2026-03-27-anthropic-wins-an-injunction"]},
        {"id": "2026-04-05-artemis-crosses-the-halfway-point",
         "title": "Artemis II crosses halfway, shooting on modified iPhones",
         "claim": "The Artemis II crew crossed the halfway point to the Moon carrying modified "
                  "iPhones as their primary cameras in a NASA first, capturing Earth eclipsing "
                  "the Sun with twin auroras, while Planet Labs agreed to withhold satellite "
                  "imagery of Iran at US government request.",
         "domain": "space", "actor": ["nasa", "apple", "planet-labs"],
         "evidences": ["inhabitable-worlds", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-04-03-first-translunar-injection-since-apollo"]},
    ],
}
