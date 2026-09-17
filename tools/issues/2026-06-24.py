"""Issue 146 — 2026-06-24. Patch the planet."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-24-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-24", "title": "Welcome to June 24, 2026", "url": URL,
        "thesis": "The mission shifts from finding vulnerabilities to patching them.",
        "body": """
# Welcome to June 24, 2026

GPT-5.5-Cyber hit a state-of-the-art 85.6% on CyberGym, edging out Mythos 5,
and the mission shifted from finding vulnerabilities to autonomously patching
them through a Patch the Planet effort with Trail of Bits.

Alphabet had its worst day in over a year, losing $250 billion after Noam
Shazeer and Nobel laureate John Jumper defected to rivals. Talent, not compute,
priced at a quarter-trillion dollars.
""",
    },
    "themes": [
        {"id": "the-persistent-colleague", "type": "Theme",
         "title": "The model joins the team",
         "first_seen": "2026-06-24", "domain": "agents",
         "body": "The third redesign of how people use models: not a chat window and "
                 "not a delegated task, but a persistent asynchronous entity addressed "
                 "the way a colleague is — tagged, assigned, and expected to come back "
                 "with something."},
    ],
    "organizations": [
        {"id": "trail-of-bits", "type": "Organization", "title": "Trail of Bits"},
        {"id": "cline", "type": "Organization", "title": "Cline"},
        {"id": "reflection-inc", "type": "Organization", "title": "Reflection"},
        {"id": "nabla-bio", "type": "Organization", "title": "Nabla Bio"},
        {"id": "lineshine", "type": "Organization", "title": "LineShine"},
        {"id": "chicago", "type": "Organization", "title": "Chicago"},
    ],
    "developments": [
        {"id": "2026-06-24-from-finding-flaws-to-patching-the-planet",
         "title": "A cyber model shifts the mission from finding flaws to patching them",
         "claim": "OpenAI expanded Daybreak with a Codex Security plugin and the full "
                  "GPT-5.5-Cyber, which hit a state-of-the-art 85.6% on CyberGym, edging out "
                  "Mythos 5, and shifted the mission from finding vulnerabilities to "
                  "autonomously patching them through a Patch the Planet effort with Trail of "
                  "Bits.",
         "domain": "compute", "actor": ["openai", "trail-of-bits", "anthropic"], "score": "85.6%",
         "evidences": ["risk-becomes-uninsurable", "war-reaches-the-cloud", "agent-economy"],
         "supersedes": [B + "developments/2026-06-17-two-thousand-flaws-patched-pre-disclosure"]},
        {"id": "2026-06-24-an-open-model-tidier-than-the-frontier",
         "title": "An open model fixes a real bug at half the cost and more tidily",
         "claim": "Skeptical of benchmarks, Cline pitted GLM-5.2 against Opus 4.8 on a real "
                  "repository bug and found GLM half the cost and tidier, while Opus finished "
                  "faster but left build-breaking type errors.",
         "domain": "models", "actor": ["cline", "zai", "anthropic"],
         "evidences": ["open-weight-latency", "instruments-lag-the-models"],
         "supersedes": [B + "developments/2026-06-20-open-chinese-models-take-the-majority"]},
        {"id": "2026-06-24-a-quarter-trillion-lost-to-two-departures",
         "title": "Two researcher departures cost a company $250 billion",
         "claim": "Alphabet had its worst day in over a year, losing $250 billion after Noam "
                  "Shazeer and Nobel laureate John Jumper defected to OpenAI and Anthropic, "
                  "while the White House pressed Meta, the last holdout, to submit models for "
                  "federal safety review.",
         "domain": "economics", "actor": ["alphabet", "openai", "anthropic", "meta", "white-house"],
         "score": "-$250B",
         "evidences": ["growth-without-hiring", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-20-a-nobel-laureate-changes-labs"]},
        {"id": "2026-06-24-a-model-joins-the-team-in-slack",
         "title": "A model becomes a persistent asynchronous colleague",
         "claim": "Anthropic's Claude Tag lets teams delegate by tagging Claude in Slack, where "
                  "it works asynchronously, which Andrej Karpathy called the third redesign of "
                  "LLM user experience — a persistent, asynchronous entity that joins the team "
                  "like a colleague.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["the-persistent-colleague", "agents-on-the-org-chart", "agent-economy"],
         "supersedes": [B + "developments/2026-06-21-agents-learn-to-find-each-other"]},
        {"id": "2026-06-24-skills-that-write-themselves",
         "title": "A command turns any document into a reusable skill",
         "claim": "Nous Research shipped a learn command that turns any document or workflow "
                  "into a reusable skill, as OpenAI debuted at Cannes Lions pitching ChatGPT ads "
                  "and Codex to marketers.",
         "domain": "agents", "actor": ["nous-research", "openai"],
         "evidences": ["scaffolding-over-weights", "agents-beget-agents"],
         "supersedes": [B + "developments/2026-06-19-record-and-replay-turns-a-chore-into-a-skill"]},
        {"id": "2026-06-24-banned-chips-double-on-the-black-market",
         "title": "Banned chips more than double in price on a black market",
         "claim": "Nvidia's banned chips more than doubled in price on China's black market, "
                  "with DGX B300 servers topping $1.1 million, while Cerebras posted 92% growth "
                  "in its first results since listing.",
         "domain": "compute", "actor": ["nvidia", "cerebras"], "score": "$1.1M per server",
         "evidences": ["silicon-curtain", "regulatory-exit"],
         "supersedes": [B + "developments/2026-06-22-location-beacons-on-top-silicon"]},
        {"id": "2026-06-24-a-supercomputer-on-cpus-alone",
         "title": "A CPU-only machine becomes the world's most powerful supercomputer",
         "claim": "China's LineShine became the world's most powerful supercomputer at 2.198 "
                  "exaflops on CPUs alone, as SpaceX inked a $6.3 billion deal to rent GB300s "
                  "to the startup Reflection and one analysis argued the real bottleneck is "
                  "grid hookups rather than electricity.",
         "domain": "compute", "actor": ["lineshine", "spacex", "reflection-inc"],
         "score": "2.198 exaflops",
         "evidences": ["silicon-curtain", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-06-17-capex-tops-cash-flow"]},
        {"id": "2026-06-24-two-quantum-executive-orders",
         "title": "Two executive orders target a useful quantum computer by 2028",
         "claim": "The President signed two quantum executive orders targeting a useful machine "
                  "by 2028 and Chicago bet $500 million on a quantum park, while Canada declared "
                  "a civilian nuclear renaissance of up to ten reactors, mirrored by a US $17.5 "
                  "billion loan for ten AP1000s.",
         "domain": "policy", "actor": ["white-house", "chicago", "canada"],
         "score": "2028 target / $17.5B loan",
         "evidences": ["science-as-industrial-policy", "industrialized-nature"],
         "supersedes": [B + "developments/2026-06-19-small-reactors-and-a-lifted-nuclear-ban"]},
        {"id": "2026-06-24-fifty-robots-while-workers-await-recall",
         "title": "Fifty robots are installed while 1,300 laid-off staff await recall",
         "claim": "GM installed 50 robots at its flagship Detroit plant while 1,300 laid-off "
                  "staff still awaited recall, as Oracle cut 21,000 jobs blaming AI.",
         "domain": "economics", "actor": ["gm", "oracle"], "score": "21,000 jobs cut",
         "evidences": ["work-displaced", "physical-recursion"],
         "supersedes": [B + "developments/2026-06-22-seven-hundred-thousand-couriers-to-be-replaced"]},
        {"id": "2026-06-24-directed-energy-downs-drones-autonomously",
         "title": "A missile-defense test autonomously downs drones with directed energy",
         "claim": "The Secretary of War declared the first Golden Dome test a full mission "
                  "success, with directed energy autonomously downing drones and cruise "
                  "missiles, as Musk trademarked a name for SpaceX's Dyson Swarm.",
         "domain": "space", "actor": ["war-department", "spacex"],
         "evidences": ["violence-arrives", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-06-19-drones-licensed-and-dispatched"]},
        {"id": "2026-06-24-antibodies-designed-and-tested-in-six-weeks",
         "title": "Zero-shot design produces multifunctional antibodies in six weeks",
         "claim": "Nabla Bio's JAM-2 pushed zero-shot drug design beyond binding into "
                  "multifunctional antibodies, including KRAS-targeting multispecifics built and "
                  "tested in roughly six weeks, while Eli Lilly built an app store for "
                  "scientists on its own Blackwell cluster.",
         "domain": "biotech", "actor": ["nabla-bio", "eli-lilly"], "score": "~6 weeks",
         "evidences": ["hardware-grade-biology", "compiling-matter", "automated-science"],
         "supersedes": [B + "developments/2026-06-22-cervical-cancer-death-cut-to-effectively-zero"]},
        {"id": "2026-06-24-money-becomes-programmable",
         "title": "Europe backs a digital euro to escape US payment rails",
         "claim": "Europe backed a digital euro by 2029 to escape US payment rails and Meta "
                  "began building a prediction-markets app, as Alphabet replaced Verizon in the "
                  "Dow and Meta paused a keystroke-harvesting program after the data leaked "
                  "internally.",
         "domain": "economics", "actor": ["european-union", "meta", "alphabet"],
         "evidences": ["regulatory-exit", "autonomous-commerce", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-12-agents-reach-for-your-wallet"]},
    ],
}
