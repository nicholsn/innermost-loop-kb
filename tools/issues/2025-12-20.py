"""Issue 010 — 2025-12-20. Superexponential."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-20-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-20",
        "title": "Welcome to December 20, 2025",
        "url": URL,
        "thesis": "The exponential curve has shattered into a superexponential vertical.",
        "body": """
# Welcome to December 20, 2025

METR puts Claude Opus 4.5 at a 4h49m 50% autonomy horizon, matching the *fast*
variant of AI 2027 in which each doubling gets 15% easier. Prediction markets
missed it, which the issue treats as the finding: the forecasting community is
recalibrating for recursive self-improvement after the fact.

Underneath, recursion crosses into matter. CATL runs humanoids on the lines that
build the batteries that power them.
""",
    },
    "themes": [
        {"id": "physical-recursion", "type": "Theme",
         "title": "Machines building what powers machines", "first_seen": "2025-12-20",
         "domain": "robotics",
         "body": "The loop closes in matter, not code: humanoids on the production "
                 "lines making the batteries and datacenter hardware that will run "
                 "the next generation of them."},
    ],
    "organizations": [
        {"id": "metr", "type": "Organization", "title": "METR",
         "resource": "https://metr.org/", "body": "Evaluates autonomous capability and time horizons."},
        {"id": "bytedance", "type": "Organization", "title": "ByteDance",
         "resource": "https://www.bytedance.com/", "body": "Released the Seed-Prover math models."},
        {"id": "alibaba", "type": "Organization", "title": "Alibaba",
         "resource": "https://www.alibabagroup.com/", "body": "Ships the Qwen model family."},
        {"id": "cerebras", "type": "Organization", "title": "Cerebras",
         "resource": "https://www.cerebras.ai/", "body": "Wafer-scale inference hardware."},
        {"id": "catl", "type": "Organization", "title": "CATL",
         "resource": "https://www.catl.com/en/", "body": "The largest battery manufacturer."},
        {"id": "magna-petra", "type": "Organization", "title": "Magna Petra",
         "body": "Lunar Helium-3 mining venture."},
        {"id": "ispace", "type": "Organization", "title": "ispace",
         "resource": "https://ispace-inc.com/", "body": "Lunar lander operator."},
        {"id": "space-force", "type": "Organization", "title": "US Space Force",
         "resource": "https://www.spaceforce.mil/", "body": "Testing flat DiskSat satellites."},
        {"id": "cftc", "type": "Organization", "title": "CFTC",
         "resource": "https://www.cftc.gov/", "body": "US derivatives regulator."},
    ],
    "systems": [
        {"id": "claude-opus-4-5", "type": "AISystem", "title": "Claude Opus 4.5",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "evaluated_on": [B + "benchmarks/autonomous-time-horizon"]},
        {"id": "seed-prover-1-5", "type": "AISystem", "title": "Seed-Prover 1.5",
         "developed_by": [B + "organizations/bytedance"], "modality": "mathematics",
         "evaluated_on": [B + "benchmarks/putnam"]},
        {"id": "qwen-image-layered", "type": "AISystem", "title": "Qwen-Image-Layered",
         "developed_by": [B + "organizations/alibaba"], "modality": "image",
         "body": "First foundation model natively decomposing images into discrete layers."},
    ],
    "benchmarks": [
        {"id": "putnam", "type": "Benchmark", "title": "Putnam competition",
         "measures_capability": "undergraduate competition mathematics"},
        {"id": "frontiermath", "type": "Benchmark", "title": "FrontierMath",
         "measures_capability": "research-level mathematics"},
    ],
    "hardware": [
        {"id": "lightgen", "type": "Hardware", "title": "LightGen photonic chip",
         "body": "All-optical chip integrating millions of photonic neurons, reported two "
                 "orders of magnitude more energy efficient than electronics."},
        {"id": "disksat", "type": "Hardware", "title": "DiskSat",
         "developed_by": [B + "organizations/space-force"],
         "body": "Flat, pizza-shaped satellite maximizing surface area for power."},
    ],
    "facilities": [
        {"id": "three-body-constellation", "type": "Facility",
         "title": "Three-Body Computing Constellation",
         "operated_by": [B + "organizations/china"], "located_in": "low Earth orbit",
         "capacity": "planned 2,800 satellites",
         "body": "An orbital AI datacenter network already operating for over six months."},
    ],
    "developments": [
        {"id": "2025-12-20-metr-opus-45-autonomy",
         "title": "METR puts Opus 4.5 at a 4h49m autonomy horizon",
         "claim": "METR measured Claude Opus 4.5 at a state-of-the-art 50% autonomy time "
                  "horizon of 4 hours 49 minutes, matching a fast-timeline AI 2027 variant in "
                  "which each doubling is 15% easier.",
         "domain": "agents", "actor": ["metr", "anthropic"], "score": "4h49m",
         "about": [B + "systems/claude-opus-4-5", B + "benchmarks/autonomous-time-horizon"],
         "evidences": ["autonomy-clock-speed"],
         "supersedes": [B + "developments/2025-12-13-autonomy-time-horizon-sota"]},
        {"id": "2025-12-20-mcaleer-automated-alignment",
         "title": "Anthropic researcher pivots fully to automated alignment",
         "claim": "Anthropic's Stephen McAleer pivoted entirely to automated alignment research, "
                  "arguing human oversight is obsolete against the coming intelligence explosion.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["recursive-self-improvement"]},
        {"id": "2025-12-20-markets-missed-opus-breakout",
         "title": "Prediction markets underestimated the Opus autonomy jump",
         "claim": "Manifold prediction markets significantly underestimated the Opus 4.5 "
                  "autonomy breakout, leaving forecasters recalibrating for recursive "
                  "self-improvement.",
         "domain": "economics", "evidences": ["autonomy-clock-speed"],
         "supersedes": [B + "developments/2025-12-15-ai-2027-forecast-accuracy"],
         "body": "Five days after 91% of AI 2027 predictions were reported accurate, the "
                 "same community is caught out by a single result."},
        {"id": "2025-12-20-seed-prover-putnam",
         "title": "Seed-Prover 1.5 solves 11 of 12 Putnam problems",
         "claim": "ByteDance released Seed-Prover 1.5, trained with large-scale agentic "
                  "reinforcement learning, which solved 11 of 12 problems from the 2025 Putnam "
                  "competition and 88% of an undergraduate benchmark.",
         "domain": "science", "actor": ["bytedance"], "score": "11/12 Putnam, 88% undergrad",
         "about": [B + "systems/seed-prover-1-5", B + "benchmarks/putnam"],
         "evidences": ["automated-science", "discovery-as-process"]},
        {"id": "2025-12-20-gemini-flash-agentic-rl-frontiermath",
         "title": "Gemini 3 Flash's gains traced to agentic RL, at 36% on FrontierMath",
         "claim": "Google attributed Gemini 3 Flash's gains to agentic reinforcement learning, "
                  "scoring 36% on FrontierMath Tiers 1-3 and matching far more expensive models.",
         "domain": "benchmarks", "actor": ["google"], "score": "36%",
         "about": [B + "benchmarks/frontiermath", B + "systems/gemini-3-flash"],
         "evidences": ["reasoning-price-deflation"]},
        {"id": "2025-12-20-deepmind-collective-superintelligence",
         "title": "DeepMind argues superintelligence emerges from agent networks",
         "claim": "A DeepMind paper argued superintelligence will emerge from collective agent "
                  "networks rather than a single monolithic mind.",
         "domain": "agents", "actor": ["google-deepmind"],
         "evidences": ["network-over-node"],
         "supersedes": [B + "developments/2025-12-13-zoom-federated-swarm-hle"],
         "body": "A week after a federated swarm beat the monolith empirically, the claim "
                 "is made as theory."},
        {"id": "2025-12-20-qwen-image-layered",
         "title": "Alibaba's Qwen-Image-Layered decomposes images into layers",
         "claim": "Alibaba released Qwen-Image-Layered, the first foundation model natively "
                  "decomposing images into discrete layers.",
         "domain": "models", "actor": ["alibaba"], "about": [B + "systems/qwen-image-layered"]},
        {"id": "2025-12-20-google-rations-internal-compute",
         "title": "Google forms a council to ration internal compute",
         "claim": "Google formed a high-power executive council to ration internal compute, "
                  "with DeepMind, Cloud and Search competing for supply.",
         "domain": "compute", "actor": ["google"],
         "evidences": ["infrastructure-crowding-out"],
         "supersedes": [B + "developments/2025-12-18-openai-cannibalizes-research-compute"]},
        {"id": "2025-12-20-lightgen-optical-chip",
         "title": "LightGen runs generative tasks entirely in light",
         "claim": "Chinese researchers demonstrated LightGen, an all-optical chip integrating "
                  "millions of photonic neurons with energy efficiency two orders of magnitude "
                  "above electronic chips.",
         "domain": "compute", "actor": ["china"], "score": "~100x efficiency",
         "about": [B + "hardware/lightgen"],
         "evidences": ["vertical-silicon", "silicon-curtain"],
         "supersedes": [B + "developments/2025-12-18-photonic-2d-waveguide-inference"]},
        {"id": "2025-12-20-cerebras-ipo-q2-2026",
         "title": "Cerebras preps a Q2 2026 IPO on inference demand",
         "claim": "Cerebras is preparing a Q2 2026 IPO, capitalizing on demand for inference "
                  "capacity.",
         "domain": "economics", "actor": ["cerebras"], "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-20-three-body-constellation",
         "title": "China's orbital AI datacenter has run for six months",
         "claim": "China has been operating the Three-Body Computing Constellation, a "
                  "space-based AI data center network, for over six months, with plans to "
                  "scale to 2,800 satellites.",
         "domain": "space", "actor": ["china"], "score": "2,800 satellites planned",
         "about": [B + "facilities/three-body-constellation"],
         "evidences": ["orbit-as-compute", "silicon-curtain"],
         "supersedes": [B + "developments/2025-12-11-starcloud-orbital-training-run"],
         "body": "The orbital datacenter stops being a first and becomes an operating "
                 "national asset."},
        {"id": "2025-12-20-rocket-lab-816m-missile-defense",
         "title": "Rocket Lab wins $816M for missile-defense satellites",
         "claim": "Rocket Lab secured an $816 million contract for missile defense satellites "
                  "carrying StarLite protection sensors.",
         "domain": "space", "actor": ["rocket-lab"], "score": "$816M"},
        {"id": "2025-12-20-space-force-disksats",
         "title": "The Space Force tests flat DiskSats for power density",
         "claim": "The Space Force is testing DiskSats, flat satellites whose large surface "
                  "area favors power generation.",
         "domain": "space", "actor": ["space-force"], "about": [B + "hardware/disksat"],
         "evidences": ["orbit-as-compute"]},
        {"id": "2025-12-20-magna-petra-lunar-helium3",
         "title": "Magna Petra signs ispace to mine lunar Helium-3",
         "claim": "Magna Petra signed with ispace to mine lunar Helium-3 to feed terrestrial "
                  "fusion.",
         "domain": "space", "actor": ["magna-petra", "ispace"],
         "evidences": ["industrialized-nature", "orbit-as-compute"]},
        {"id": "2025-12-20-catl-humanoid-battery-lines",
         "title": "CATL puts humanoids on the lines that build batteries",
         "claim": "CATL operationalized the first large-scale humanoid robot deployment in its "
                  "battery production lines.",
         "domain": "robotics", "actor": ["catl"],
         "evidences": ["physical-recursion", "recursive-self-improvement"],
         "body": "Machines building the batteries that power machines — the recursion the "
                 "corpus has been tracking in software, now in matter."},
        {"id": "2025-12-20-cftc-energy-swaps-pilot",
         "title": "The CFTC pilots energy commodity swaps for AI",
         "claim": "The CFTC launched a pilot programme for energy commodity swaps aimed at AI "
                  "competitiveness.",
         "domain": "economics", "actor": ["cftc"],
         "evidences": ["burning-molecules-for-tokens", "compute-capital-stack"],
         "supersedes": [B + "developments/2025-12-11-ornn-first-gpu-compute-swap"]},
    ],
}
