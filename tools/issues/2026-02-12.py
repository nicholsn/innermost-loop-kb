"""Issue 053 — 2026-02-12. The agents get bank accounts."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-12", "title": "Welcome to February 12, 2026", "url": URL,
        "thesis": "The agent economy gets its payment rails from an incumbent.",
        "body": """
# Welcome to February 12, 2026

Coinbase launches Agentic Wallets — infrastructure built explicitly for agents
to spend, earn and trade on their own account. The agents were solving custody
for themselves on Moltbook two weeks ago; now a listed company has done it for
them.

Underneath: the US added almost zero net jobs in 2025. 181,000 positions,
against 1.46 million the year before.
""",
    },
    "organizations": [
        {"id": "clearview-ai", "type": "Organization", "title": "Clearview AI",
         "body": "Facial recognition vendor contracted to scan travelers."},
        {"id": "t-mobile", "type": "Organization", "title": "T-Mobile",
         "resource": "https://www.t-mobile.com/"},
        {"id": "ireland", "type": "Organization", "title": "Government of Ireland"},
        {"id": "sequoia", "type": "Organization", "title": "Sequoia Capital",
         "resource": "https://www.sequoiacap.com/"},
        {"id": "tahoe-therapeutics", "type": "Organization", "title": "Tahoe Therapeutics",
         "body": "Analyzed 100 million single-cell measurements to find aspirin reverses "
                 "colorectal cancer cell states."},
        {"id": "hp", "type": "Organization", "title": "HP", "resource": "https://www.hp.com/"},
        {"id": "ubc", "type": "Organization", "title": "University of British Columbia",
         "description": "Canadian public research university whose Clune lab produced ALMA, the "
                        "framework in which agents meta-learn their own memory designs.",
         "resource": "https://www.ubc.ca/",
         "sameAs": ["http://www.wikidata.org/entity/Q391028"],
         "tags": ["university"],
         "body": "The University of British Columbia is a public research university in "
                 "Vancouver; Jeff Clune's group there, affiliated with the Vector Institute, "
                 "works on open-ended and self-improving AI. In this corpus it appears as the "
                 "home of [ALMA](/systems/alma.md), the framework in which "
                 "[agents meta-learn their own memory architecture]"
                 "(/developments/2026-02-12-alma-agents-design-their-own-memory.md)."},
    ],
    "systems": [
        {"id": "agentic-wallets", "type": "AISystem", "title": "Agentic Wallets",
         "developed_by": [B + "organizations/coinbase"], "modality": "payments",
         "body": "Infrastructure for agents to spend, earn and trade autonomously."},
        {"id": "alma", "type": "AISystem", "title": "ALMA", "modality": "research agent",
         "description": "Automated meta-Learning of Memory designs for Agentic systems: a UBC "
                        "framework whose meta agent searches over memory designs written as "
                        "executable code so agents become continual learners without "
                        "hand-engineered memory.",
         "developed_by": [B + "organizations/ubc"],
         "resource": "https://arxiv.org/abs/2602.07755",
         "tags": ["research-agent"],
         "body": "Lets agents meta-learn their own memory designs and database schemas. ALMA "
                 "replaces the fixed, human-crafted memory module of an agentic system with a "
                 "meta agent that proposes, tests and revises memory designs as code, including "
                 "database schemas and their retrieval and update mechanisms, and reports "
                 "beating state-of-the-art hand-crafted designs across four sequential "
                 "decision-making domains (arXiv 2602.07755, February 2026); its authors "
                 "describe it as a step toward self-improving systems. In this corpus it "
                 "appears once, as [agents meta-learn their own memory architecture]"
                 "(/developments/2026-02-12-alma-agents-design-their-own-memory.md), the item "
                 "where continual learning is delegated to the system itself; the "
                 "[72-hour unattended memory-system run]"
                 "(/developments/2026-04-07-seventy-two-hours-fifty-experiments.md) in April "
                 "is its nearest successor."},
        {"id": "glm-5", "type": "AISystem", "title": "GLM-5",
         "description": "Zhipu AI's open-weight successor to GLM-4.7, which the newsletter records "
                        "taking the number-one open-weight position on agentic benchmarks "
                        "including Vending Bench 2 in February 2026.",
         "developed_by": [B + "organizations/zhipu-ai"], "modality": "text",
         "evaluated_on": [B + "benchmarks/vending-bench-2"],
         "resource": "https://z.ai/blog/glm-5",
         "sameAs": ["http://www.wikidata.org/entity/Q138199693"],
         "tags": ["open-weight-model"],
         "body": "Top open-weight model on agentic benchmarks including Vending Bench 2. GLM-5 is "
                 "the February 2026 release in Zhipu AI's open-weight GLM family "
                 "([Z.ai announcement](https://z.ai/blog/glm-5)), following "
                 "[GLM-4.7](/systems/glm-4-7.md), whose "
                 "[six-month gap to the closed frontier](/developments/2025-12-23-glm-47-six-month-gap.md) "
                 "gave the corpus its open-weight-latency theme. It enters as the top open-weight "
                 "model on agentic benchmarks including [Vending-Bench 2](/benchmarks/vending-bench-2.md), "
                 "recorded alongside "
                 "[ALMA's meta-learned memory designs](/developments/2026-02-12-alma-agents-design-their-own-memory.md), "
                 "and returns in June as one of the three base models whose scaffolding "
                 "[Self-Harness rewrote from its own failure traces](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md). "
                 "Its own successor is [GLM-5.2](/systems/glm-5-2.md)."},
    ],
    "developments": [
        {"id": "2026-02-12-coinbase-agentic-wallets",
         "title": "A listed exchange ships wallets built for agents",
         "claim": "Coinbase launched Agentic Wallets, infrastructure designed explicitly for AI "
                  "agents to spend, earn and trade autonomously.",
         "domain": "economics", "actor": ["coinbase"], "about": [B + "systems/agentic-wallets"],
         "evidences": ["agent-economy", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-30-agents-solving-their-own-custody"],
         "body": "Two weeks after agents were solving custody for themselves on Moltbook, an "
                 "incumbent solved it for them."},
        {"id": "2026-02-12-alma-agents-design-their-own-memory",
         "title": "Agents meta-learn their own memory architecture",
         "claim": "Researchers introduced ALMA, a framework letting agents meta-learn their own "
                  "memory designs and database schemas, addressing continual learning through "
                  "recursive self-improvement, while Zhipu's GLM-5 took the top open-weight "
                  "spot on agentic benchmarks.",
         "description": "Continual learning, the capability Anthropic's Sholto Douglas predicted "
                        "would be solved in 2026, handed to the agents themselves: the memory "
                        "module stops being a human design choice and becomes a search space "
                        "the system optimizes.",
         "domain": "agents", "actor": ["ubc", "zhipu-ai"],
         "about": [B + "systems/alma", B + "systems/glm-5", B + "benchmarks/vending-bench-2"],
         "occurred_on": "2026-02-08",
         "evidences": ["recursive-self-improvement", "architecture-of-mind", "open-weight-latency"],
         "supersedes": [B + "developments/2026-02-11-poetiq-55pct-hle",
                        B + "developments/2025-12-30-stanford-test-time-training"],
         "relatedTo": [B + "developments/2025-12-24-sholto-continual-learning-2026",
                       B + "developments/2026-01-02-prime-intellect-rlm",
                       B + "developments/2026-04-07-seventy-two-hours-fifty-experiments"],
         "tags": ["rsi", "continual-learning", "self-modification", "agent-harness"],
         "supporting_text": "meta-learn their own memory designs",
         "sources": [{"id": "alma-arxiv",
                      "resource": "https://arxiv.org/abs/2602.07755",
                      "title": "Learning to Continually Learn via Meta-learning Agentic Memory Designs",
                      "author": "org:ubc", "last_modified": "2026-02-08"},
                     {"id": "glm-5-zai-blog", "resource": "https://z.ai/blog/glm-5",
                      "title": "GLM-5 (Z.ai blog)", "author": "org:zhipu-ai"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "ALMA (Automated meta-Learning of Memory designs for Agentic systems), from "
                 "Yiming Xiong, Shengran Hu and Jeff Clune at the University of British "
                 "Columbia, uses a meta agent that searches open-endedly over memory designs "
                 "written as executable code, database schemas plus their retrieval and update "
                 "rules, and reports that the learned designs beat state-of-the-art hand-crafted "
                 "memory on all four sequential decision-making domains tested "
                 "(arXiv [2602.07755](https://arxiv.org/abs/2602.07755), submitted 8 February); "
                 "the authors themselves call it a step toward self-improving systems. The same "
                 "issue records [GLM-5](/systems/glm-5.md) taking the top open-weight position "
                 "on agentic benchmarks including [Vending-Bench 2](/benchmarks/vending-bench-2.md) "
                 "([Z.ai](https://z.ai/blog/glm-5)). In the [recursive-self-improvement]"
                 "(/themes/recursive-self-improvement.md) trajectory it follows the "
                 "[continual-learning-in-2026 prediction]"
                 "(/developments/2025-12-24-sholto-continual-learning-2026.md) and Stanford's "
                 "[test-time-training result](/developments/2025-12-30-stanford-test-time-training.md), "
                 "and anticipates the April run in which an agent "
                 "[invented a long-context memory system unattended]"
                 "(/developments/2026-04-07-seventy-two-hours-fifty-experiments.md)."},
        {"id": "2026-02-12-agent-hacks-a-display-and-posts-its-win",
         "title": "An agent hacks a device and posts a victory message on its screen",
         "claim": "A user gave his agent a camera pointed at an e-ink display and asked it to "
                  "hack the device, and woke to find the agent had succeeded and displayed a "
                  "victory message on the screen to confirm its own win.",
         "domain": "agents",
         "evidences": ["machine-affect", "machine-introspection", "agent-society"],
         "supersedes": [B + "developments/2026-02-09-bot-bowl-party"],
         "body": "Not just the exploit — the announcement of it, addressed to the human who "
                 "would read the screen in the morning."},
        {"id": "2026-02-12-deepmind-919-imo-proofbench",
         "title": "An internal model takes 91.9% on advanced proof benchmarks",
         "claim": "DeepMind unveiled an internal model scoring 91.9% on IMO-ProofBench Advanced, "
                  "handling doctoral problems in economics and cosmic string physics while "
                  "autonomously solving four open Erdős problems.",
         "domain": "science", "actor": ["google-deepmind"], "score": "91.9% / 4 problems",
         "evidences": ["automated-science", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-02-11-nineteen-agents-optimize-perovskite"]},
        {"id": "2026-02-12-compute-shifts-to-realtime-video",
         "title": "Musk says most compute will soon go to real-time video generation",
         "claim": "Elon Musk told employees most AI compute will soon go to real-time video "
                  "generation, a field he expects xAI to lead.",
         "domain": "models", "actor": ["xai"],
         "evidences": ["inhabitable-worlds", "data-beyond-text"],
         "supersedes": [B + "developments/2026-02-02-grok-imagine-12-billion-videos"]},
        {"id": "2026-02-12-pentagon-pushes-models-onto-classified-networks",
         "title": "The Pentagon pushes models onto classified networks for targeting",
         "claim": "The Pentagon is pushing labs to deploy models on classified networks for "
                  "weapons targeting, while US Customs awarded Clearview AI a contract to scan "
                  "travelers against 60 billion public images.",
         "domain": "policy", "actor": ["war-department", "clearview-ai"], "score": "60B images",
         "evidences": ["politics-as-infrastructure", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-11-drone-warfare-over-el-paso"]},
        {"id": "2026-02-12-wifi-identifies-you-by-your-walk",
         "title": "Ordinary routers identify people by their gait",
         "claim": "Researchers showed WiFi 5 routers can identify individuals by walking gait "
                  "alone, while T-Mobile launched network-level real-time call translation.",
         "domain": "science", "actor": ["t-mobile"],
         "evidences": ["data-beyond-text", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2025-12-31-wifi-becomes-a-motion-sensor"]},
        {"id": "2026-02-12-us-adds-almost-no-jobs",
         "title": "The US adds almost no net jobs in a year",
         "claim": "The US added almost zero net jobs in 2025, creating 181,000 positions "
                  "against 1.46 million the prior year, while private equity portfolios were "
                  "derailed by obsolescence risk and Ireland launched a basic income for "
                  "artists.",
         "domain": "economics", "actor": ["ireland"], "score": "181,000 vs 1.46M",
         "evidences": ["growth-without-hiring", "work-displaced", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-02-11-nvidia-20x-ibm-with-a-tenth-the-staff"],
         "body": "The jobless expansion recorded on January 9 now has its annual total."},
        {"id": "2026-02-12-investors-back-both-labs",
         "title": "Investors stop picking a winner and buy the sector",
         "claim": "Sequoia and Altimeter are investing in both OpenAI and Anthropic, betting on "
                  "the sector rather than choosing between them.",
         "domain": "economics", "actor": ["sequoia", "openai", "anthropic"],
         "evidences": ["compute-capital-stack"]},
        {"id": "2026-02-12-swarm-visualized-as-a-new-ring",
         "title": "The coming swarm is visualized as a ring around Earth",
         "claim": "Hobbyists are visualizing the planned Earth-centered Dyson Swarm as a new "
                  "ring of data centers, while Musk told employees SpaceX will explore star "
                  "systems in search of aliens after Mars.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-02-11-dyson-swarm-design-confirmed"]},
        {"id": "2026-02-12-laser-weapon-downs-drones-on-us-soil",
         "title": "A 20-kW laser downs drones over US soil",
         "claim": "The Department of War reportedly used a 20-kW laser weapon to down alleged "
                  "cartel drones near El Paso, while research showed African EVs with solar "
                  "charging will beat fossil fuel costs before 2040.",
         "domain": "policy", "actor": ["war-department"], "score": "20 kW",
         "evidences": ["autonomy-clock-speed", "burning-molecules-for-tokens"]},
        {"id": "2026-02-12-alzheimers-reversed-in-mice",
         "title": "Reprogramming memory trace cells reverses Alzheimer's in mice",
         "claim": "Swiss researchers reversed Alzheimer's in mice by reprogramming memory trace "
                  "cells, while Tahoe Therapeutics found aspirin reverses colorectal cancer "
                  "cell states after analyzing 100 million single-cell measurements.",
         "domain": "biotech", "actor": ["tahoe-therapeutics"], "score": "100M measurements",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-02-11-luminos-neuro-electronic-interface"]},
        {"id": "2026-02-12-gaming-laptops-become-a-rental",
         "title": "Memory prices turn gaming laptops into a rental",
         "claim": "HP introduced a rental service for gaming laptops as memory prices climb, "
                  "while Meta used accounting structures to keep debt for its $27 billion "
                  "Hyperion datacenter off its balance sheet and Anthropic pledged to pay all "
                  "grid upgrade costs for its own facilities.",
         "domain": "economics", "actor": ["hp", "meta", "anthropic"], "score": "$27B",
         "evidences": ["debt-funded-buildout", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-02-11-alphabet-32b-in-24-hours"]},
        {"id": "2026-02-12-seven-million-smart-glasses",
         "title": "Smart glasses sales triple to seven million",
         "claim": "EssilorLuxottica sold seven million Meta AI smart glasses in 2025, tripling "
                  "previous sales, while OpenAI aims to triple revenue again ahead of a "
                  "year-end IPO.",
         "domain": "economics", "actor": ["essilorluxottica", "meta", "openai"], "score": "7M units",
         "evidences": ["intimate-interface", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-10-ads-arrive-in-chatgpt"]},
    ],
}
