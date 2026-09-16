"""Issue 012 — 2025-12-22. The jagged frontier smooths out."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-22-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-22",
        "title": "Welcome to December 22, 2025",
        "url": URL,
        "thesis": "The models are learning to learn in real-time.",
        "body": """
# Welcome to December 22, 2025

The quiet reversal: analysis of METR data finds autonomy horizons now correlate
strongly with ARC-AGI and FrontierMath, suggesting the era of jagged capabilities
is ending and intelligence is becoming a smooth, predictable surface. Issue 002
argued the opposite — that the frontier was spiky and no model led everywhere.
Ten days.

The other shift is ownership. Blackstone and TPG plan 40 GW, and Big Tech's
share of global compute is forecast to fall to 18% by 2032.
""",
    },
    "themes": [
        {"id": "capital-takes-the-plant", "type": "Theme",
         "title": "Finance takes over the physical plant", "first_seen": "2025-12-22",
         "domain": "economics",
         "body": "Datacenters stop being built by the companies that use them. Asset "
                 "managers become the landlords of compute, and Big Tech becomes a "
                 "tenant."},
    ],
    "organizations": [
        {"id": "blackstone", "type": "Organization", "title": "Blackstone",
         "resource": "https://www.blackstone.com/", "body": "Asset manager building datacenter capacity."},
        {"id": "tpg", "type": "Organization", "title": "TPG",
         "resource": "https://www.tpg.com/", "body": "Asset manager building datacenter capacity."},
        {"id": "reve", "type": "Organization", "title": "Reve",
         "body": "Generative image and video editor."},
        {"id": "tars", "type": "Organization", "title": "TARS",
         "body": "Built the first autonomous embroidery robot."},
        {"id": "gitai", "type": "Organization", "title": "GITAI",
         "resource": "https://gitai.tech/", "body": "Space robotics."},
        {"id": "blueprint", "type": "Organization", "title": "Blueprint (Bryan Johnson)",
         "resource": "https://blueprint.bryanjohnson.com/", "body": "Longevity venture."},
    ],
    "developments": [
        {"id": "2025-12-22-meta-rl-without-gradients",
         "title": "A Meta-RL framework lets agents learn from feedback without gradient updates",
         "claim": "Swiss researchers unveiled a Meta-RL framework letting agents reflect on "
                  "feedback without gradient updates, giving double-digit gains by turning "
                  "test-time compute into active exploration.",
         "domain": "agents", "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-22-jagged-capabilities-ending",
         "title": "Autonomy horizons now correlate with reasoning benchmarks",
         "claim": "Third-party analysis of METR data found autonomy time horizons correlate "
                  "strongly with ARC-AGI and FrontierMath, suggesting the era of jagged "
                  "capabilities is concluding and intelligence is becoming a smooth surface.",
         "domain": "benchmarks", "actor": ["metr"],
         "about": [B + "benchmarks/autonomous-time-horizon", B + "benchmarks/frontiermath"],
         "evidences": ["autonomy-clock-speed"],
         "supersedes": [B + "developments/2025-12-12-spiky-frontier-gaps"],
         "body": "The direct reversal of issue 002's spiky-frontier claim, ten days later."},
        {"id": "2025-12-22-gemini-flash-distillation",
         "title": "Gemini 3 Flash is confirmed as a distillation product",
         "claim": "A Google engineer confirmed Gemini 3 Flash is a product of pretraining "
                  "distillation.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/gemini-3-flash"],
         "evidences": ["reasoning-price-deflation"]},
        {"id": "2025-12-22-query-projection-beats-thinking-tokens",
         "title": "Updating query projections beats generating thinking tokens on long contexts",
         "claim": "Harvard and Meta researchers showed updating query projection matrices is "
                  "more efficient than generating thinking tokens for long contexts.",
         "domain": "models", "actor": ["meta"], "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-22-reve-five-minute-video",
         "title": "Reve forecasts five-minute generative video in 2026",
         "claim": "AI image editor Reve forecast five-minute generative videos by 2026, with "
                  "hour-long coherent streams soon after.",
         "domain": "models", "actor": ["reve"], "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-22-llm-preprint-volume-50pct",
         "title": "Researchers using LLMs post up to 50% more preprints",
         "claim": "Researchers using LLMs are posting up to 50% more papers on preprint servers.",
         "domain": "science", "score": "+50%",
         "evidences": ["discovery-as-process", "automated-science"]},
        {"id": "2025-12-22-diffusion-designed-catalysts",
         "title": "Diffusion models design catalysts for low-carbon ammonia decomposition",
         "claim": "Diffusion models designed bimetallic alloy catalysts for low-carbon ammonia "
                  "decomposition, solving bottlenecks that had stumped human chemists.",
         "domain": "science", "evidences": ["compiling-matter", "automated-science"]},
        {"id": "2025-12-22-blackstone-tpg-40gw",
         "title": "Blackstone and TPG plan 40 GW as Big Tech's compute share falls to 18%",
         "claim": "Blackstone and TPG are planning 40 gigawatts of capacity, with Big Tech's "
                  "share of global compute forecast to shrink to 18% by 2032.",
         "domain": "economics", "actor": ["blackstone", "tpg"], "score": "40 GW; 18% by 2032",
         "evidences": ["capital-takes-the-plant", "compute-capital-stack"]},
        {"id": "2025-12-22-openai-compute-margins-70pct",
         "title": "OpenAI's compute margins double to 70%",
         "claim": "OpenAI's compute margins rose from 35% to 70% in under two years.",
         "domain": "economics", "actor": ["openai"], "score": "35% to 70%",
         "evidences": ["reasoning-price-deflation", "compute-capital-stack"]},
        {"id": "2025-12-22-tibetan-solar-park",
         "title": "China builds the largest solar park on the Tibetan Plateau",
         "claim": "China is building the world's largest solar park on the Tibetan Plateau, "
                  "covering an area ten times the size of Manhattan, to power its AI ambitions.",
         "domain": "energy", "actor": ["china"], "score": "10x Manhattan",
         "evidences": ["industrialized-nature", "burning-molecules-for-tokens"]},
        {"id": "2025-12-22-kilpatrick-2026-embodied",
         "title": "Kilpatrick calls 2026 the year of embodied AI",
         "claim": "Google's Logan Kilpatrick said 2026 will be the year of embodied AI.",
         "domain": "robotics", "actor": ["google"], "evidences": ["physical-recursion"]},
        {"id": "2025-12-22-unitree-police-patrols",
         "title": "China deploys Unitree humanoids in bulletproof vests on patrol",
         "claim": "China is deploying Unitree humanoid robots in bulletproof vests for police "
                  "patrols.",
         "domain": "robotics", "actor": ["china", "unitree"],
         "supersedes": [B + "developments/2025-12-13-unitree-humanoid-app-store"]},
        {"id": "2025-12-22-tars-embroidery-robot",
         "title": "TARS unveils the first autonomous embroidery robot",
         "claim": "TARS unveiled the world's first autonomous embroidery robot.",
         "domain": "robotics", "actor": ["tars"]},
        {"id": "2025-12-22-disneyland-olaf-rl",
         "title": "Disneyland Paris animates a walking, talking Olaf with deep RL",
         "claim": "Disneyland Paris is using deep reinforcement learning to animate a robotic "
                  "Olaf that walks and talks with non-physical fluidity.",
         "domain": "robotics", "actor": ["disney"]},
        {"id": "2025-12-22-tesla-fsd-power-outage",
         "title": "Tesla FSD drives San Francisco through a power outage",
         "claim": "Tesla FSD navigated San Francisco during power outages, driving in the dark "
                  "without human intervention.",
         "domain": "robotics", "actor": ["tesla"],
         "supersedes": [B + "developments/2025-12-21-tesla-fsd-autonomous-parking"]},
        {"id": "2025-12-22-gitai-desert-welding",
         "title": "GITAI robots weld solar panels in the desert to rehearse for Mars",
         "claim": "GITAI robots are welding solar panels in the desert as practice for Mars.",
         "domain": "space", "actor": ["gitai"], "evidences": ["physical-recursion"]},
        {"id": "2025-12-22-rocket-lab-21-electron-launches",
         "title": "Rocket Lab closes the year with 21 Electron launches",
         "claim": "Rocket Lab ended the year with a record 21 Electron launches.",
         "domain": "space", "actor": ["rocket-lab"], "score": "21 launches"},
        {"id": "2025-12-22-first-wheelchair-user-karman-line",
         "title": "The first wheelchair user crosses the Kármán Line",
         "claim": "Michaela Benthaus became the first wheelchair user to cross the Kármán Line, "
                  "on a Blue Origin flight.",
         "domain": "space", "actor": ["blue-origin"]},
        {"id": "2025-12-22-bryan-johnson-immortality-2039",
         "title": "Bryan Johnson targets immortality by 2039",
         "claim": "Bryan Johnson updated his company's mission to helping humanity achieve "
                  "immortality by 2039.",
         "domain": "biotech", "actor": ["blueprint"], "score": "by 2039",
         "evidences": ["resurrection-and-time"],
         "supersedes": [B + "developments/2025-12-14-musk-aging-reversal-mrna"]},
        {"id": "2025-12-22-deep-learning-mpox-antigens",
         "title": "Deep learning identifies protective Mpox antigens",
         "claim": "Deep learning models identified protective antigens for Mpox.",
         "domain": "biotech", "evidences": ["automated-science"]},
    ],
}
