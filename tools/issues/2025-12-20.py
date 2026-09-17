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
         "description": "TikTok's parent, whose Seed research group ships math provers, video "
                        "models and test-time-training work.",
         "resource": "https://www.bytedance.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q55606242"],
         "tags": ["big-tech", "frontier-lab"],
         "body": "ByteDance is the Beijing-based owner of TikTok and Douyin; its Seed team is the "
                 "research arm this corpus tracks. It enters with "
                 "[Seed-Prover 1.5 solving 11 of 12 Putnam problems](/developments/2025-12-20-seed-prover-putnam.md) "
                 "via agentic reinforcement learning, and returns with "
                 "[in-place test-time training](/developments/2026-04-09-in-place-test-time-training.md), "
                 "a model rewriting its own fast weights in flight, and the "
                 "[Seedance video models](/developments/2026-08-02-a-speedrun-record-falls-to-a-faster-kernel.md)."},
        {"id": "alibaba", "type": "Organization", "title": "Alibaba",
         "description": "Chinese e-commerce and cloud group that ships the Qwen model family, the "
                        "corpus's recurring open-weight frontier entrant.",
         "resource": "https://www.alibabagroup.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q1359568"],
         "tags": ["big-tech", "frontier-lab"],
         "body": "Alibaba Group runs China's largest e-commerce and cloud businesses and ships the "
                 "Qwen models. It enters this corpus with "
                 "[Qwen-Image-Layered](/developments/2025-12-20-qwen-image-layered.md), and its "
                 "later releases carry the recursive thread: "
                 "[Qwen3.7-Max ran thirty-five hours unattended](/developments/2026-05-22-thirty-five-hours-of-autonomous-execution.md) "
                 "on a kernel task, and Qwen3.8-Max, "
                 "[left alone for sixteen days](/developments/2026-08-03-sixteen-days-alone-and-265-commits.md), "
                 "shipped 265 commits and its own self-evolving harness."},
        {"id": "cerebras", "type": "Organization", "title": "Cerebras",
         "description": "Wafer-scale AI chipmaker whose low-latency inference capacity and OpenAI "
                        "deals track the corpus's hunger for inference.",
         "resource": "https://www.cerebras.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q66604886"],
         "tags": ["chipmaker", "startup"],
         "body": "Cerebras builds wafer-scale engines, single dinner-plate-sized chips aimed at "
                 "fast inference. It enters the corpus "
                 "[prepping a Q2 2026 IPO](/developments/2025-12-20-cerebras-ipo-q2-2026.md) on "
                 "inference demand, then supplies OpenAI with "
                 "[750 MW of low-latency compute](/developments/2026-01-15-openai-cerebras-750mw.md) "
                 "and [files to list above $35 billion](/developments/2026-04-17-cerebras-files-at-35b-with-warrants.md) "
                 "with warrants that scale with that customer's spend."},
        {"id": "catl", "type": "Organization", "title": "CATL",
         "description": "The world's largest battery manufacturer, whose humanoid-staffed "
                        "production lines open the corpus's physical-recursion thread.",
         "resource": "https://www.catl.com/en/",
         "sameAs": ["http://www.wikidata.org/entity/Q18653563"],
         # tags deliberately omitted: no controlled entity tag fits a battery manufacturer
         # (not big-tech / chipmaker / frontier-lab); the field is optional in check_spec.
         "body": "Contemporary Amperex Technology (CATL) is the Chinese battery maker that supplies "
                 "more EV and grid-storage cells than any other company. In this corpus it "
                 "[put humanoids to work at scale on its battery lines](/developments/2025-12-20-catl-humanoid-battery-lines.md), "
                 "machines building what powers machines, and later "
                 "[began commercial-scale sodium-ion deployment](/developments/2026-01-06-five-minute-solid-state-battery.md)."},
        {"id": "magna-petra", "type": "Organization", "title": "Magna Petra",
         "body": "Lunar Helium-3 mining venture."},
        {"id": "ispace", "type": "Organization", "title": "ispace",
         "resource": "https://ispace-inc.com/", "body": "Lunar lander operator."},
        {"id": "space-force", "type": "Organization", "title": "US Space Force",
         "resource": "https://www.spaceforce.mil/", "body": "Testing flat DiskSat satellites."},
        {"id": "cftc", "type": "Organization", "title": "CFTC",
         "resource": "https://www.cftc.gov/", "body": "US derivatives regulator."},
    ],
    "people": [
        {"id": "stephen-mcaleer", "type": "Person", "title": "Stephen McAleer",
         "name": "Stephen McAleer",
         "description": "Anthropic alignment researcher who announced a full pivot to automated "
                        "alignment research in December 2025.",
         "resource": "https://x.com/mcaleerstephen",
         "tags": ["researcher"],
         "body": "Stephen McAleer works on alignment at Anthropic. In this corpus he appears once, "
                 "[pivoting entirely to automated alignment research](/developments/2025-12-20-mcaleer-automated-alignment.md) "
                 "on the day METR reported the "
                 "[Opus 4.5 autonomy horizon](/developments/2025-12-20-metr-opus-45-autonomy.md), "
                 "arguing that human oversight is obsolete against the coming intelligence "
                 "explosion; the position he stakes out is the one Anthropic's later "
                 "[weak-to-strong supervision](/developments/2026-04-16-weak-to-strong-supervision.md) "
                 "result puts into practice."},
    ],
    "roles": [
        {"id": "stephen-mcaleer-anthropic-alignment-researcher", "type": "Role",
         "title": "Stephen McAleer, alignment researcher at Anthropic",
         "roleName": "Alignment researcher",
         "memberOf": [B + "organizations/anthropic"],
         "holder": [B + "people/stephen-mcaleer"],
         "description": "The role in which he announced a full pivot to automated alignment "
                        "research.",
         "body": "The newsletter identifies McAleer as Anthropic's and describes his work as "
                 "alignment research; it is from this position that he "
                 "[declared human oversight obsolete](/developments/2025-12-20-mcaleer-automated-alignment.md) "
                 "and turned entirely to automating the work."},
    ],
    "systems": [
        {"id": "claude-opus-4-5", "type": "AISystem", "title": "Claude Opus 4.5",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "evaluated_on": [B + "benchmarks/autonomous-time-horizon"],
         "description": "Anthropic's late-2025 frontier model whose 4h49m METR autonomy horizon "
                        "and unsupervised pull-request output mark the corpus's first "
                        "takeoff-grade coding agent.",
         "resource": "https://www.anthropic.com/news/claude-opus-4-5",
         "tags": ["coding-agent", "reasoning-model"],
         "body": "Claude Opus 4.5 is the Anthropic model released in November 2025 "
                 "([announcement](https://www.anthropic.com/news/claude-opus-4-5)). In this corpus "
                 "it is the system METR measured at a "
                 "[state-of-the-art 50% autonomy horizon of 4 hours 49 minutes](/developments/2025-12-20-metr-opus-45-autonomy.md), "
                 "a leap the newsletter reads as matching the fast-timeline AI 2027 variant. A week "
                 "later it is the model that, running inside [Claude Code](/systems/claude-code.md), "
                 "[wrote 200 pull requests](/developments/2025-12-27-cherny-200-pull-requests.md) "
                 "while its creator went a month without opening an IDE, the point at which the "
                 "corpus treats the coding loop as closed."},
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
         "description": "The first point in the corpus where automating alignment, not just "
                        "capability, is treated as the necessary response to the autonomy curve, "
                        "the immediate implication of the METR horizon result in the author's framing.",
         "domain": "agents", "actor": ["anthropic", "people/stephen-mcaleer"],
         "evidences": ["recursive-self-improvement"],
         "relatedTo": [B + "developments/2025-12-21-anthropic-activation-oracles",
                       B + "developments/2026-03-20-openai-monitors-its-own-agents",
                       B + "developments/2026-04-16-weak-to-strong-supervision"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2025-12-20-metr-opus-45-autonomy",
                        "relation_label": "responds to"}],
         "tags": ["alignment", "rsi"],
         "supporting_text": "declaring that human oversight is obsolete in the face of the coming intelligence explosion",
         "sources": [{"id": "mcaleer-automated-alignment-post",
                      "resource": "https://x.com/mcaleerstephen/status/2002205061737591128",
                      "title": "Stephen McAleer on X: pivoting entirely to automated alignment research",
                      "author": "human:stephen-mcaleer"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "[Stephen McAleer](/people/stephen-mcaleer.md), an alignment researcher at "
                 "Anthropic, announced that he was pivoting entirely to automated alignment "
                 "research on the grounds that human oversight cannot keep pace with the coming "
                 "intelligence explosion "
                 "([post](https://x.com/mcaleerstephen/status/2002205061737591128)). The "
                 "newsletter places it as the immediate implication of METR's "
                 "[4h49m autonomy horizon for Opus 4.5](/developments/2025-12-20-metr-opus-45-autonomy.md), "
                 "reported the same day: if capability compounds on the fast AI 2027 track, "
                 "alignment work has to be handed to the models too. The thread continues with "
                 "Anthropic's [Activation Oracles](/developments/2025-12-21-anthropic-activation-oracles.md) "
                 "a day later, OpenAI [monitoring its own coding agents](/developments/2026-03-20-openai-monitors-its-own-agents.md) "
                 "in March 2026, and [weak-to-strong supervision](/developments/2026-04-16-weak-to-strong-supervision.md) "
                 "closing 97% of the capability gap that April."},
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
         "description": "The author's physical recursion: the loop the corpus had tracked in code "
                        "crosses the air gap into matter, with humanoids working the lines that "
                        "make the cells that will power humanoids.",
         "domain": "robotics", "actor": ["catl"],
         "occurred_on": "2025-12-18",
         "evidences": ["physical-recursion", "recursive-self-improvement"],
         "relatedTo": [B + "developments/2026-09-15-robots-making-robots",
                       B + "systems/optimus"],
         "tags": ["robotics", "rsi"],
         "supporting_text": "CATL has operationalized the world’s first large-scale humanoid robot deployment",
         "sources": [{"id": "carnewschina-catl-humanoids",
                      "resource": "https://carnewschina.com/2025/12/18/catl-achieves-worlds-first-scale-deployment-of-embodied-ai-humanoid-robots-on-battery-production-lines/",
                      "title": "CATL achieves world's first scale deployment of embodied AI humanoid "
                               "robots on battery production lines",
                      "author": "org:carnewschina", "last_modified": "2025-12-18"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Machines building the batteries that power machines — the recursion the "
                 "corpus has been tracking in software, now in matter. "
                 "[CATL](/organizations/catl.md), the world's largest battery maker, put "
                 "embodied-AI humanoids to work at scale on its battery production lines "
                 "([CarNewsChina](https://carnewschina.com/2025/12/18/catl-achieves-worlds-first-scale-deployment-of-embodied-ai-humanoid-robots-on-battery-production-lines/)), "
                 "which the newsletter reads as the loop crossing the air gap into kinetic "
                 "reality and the first entry under "
                 "[physical recursion](/themes/physical-recursion.md). Eight days later "
                 "[Linkerbot humanoids were assembling their own hands](/developments/2025-12-26-linkerbot-self-assembly.md) "
                 "in Beijing, and by September 2026 XPENG's "
                 "[automated humanoid line](/developments/2026-09-15-robots-making-robots.md) "
                 "ships a robot that walks off unassisted."},
        {"id": "2025-12-20-cftc-energy-swaps-pilot",
         "title": "The CFTC pilots energy commodity swaps for AI",
         "claim": "The CFTC launched a pilot programme for energy commodity swaps aimed at AI "
                  "competitiveness.",
         "domain": "economics", "actor": ["cftc"],
         "evidences": ["burning-molecules-for-tokens", "compute-capital-stack"],
         "supersedes": [B + "developments/2025-12-11-ornn-first-gpu-compute-swap"]},
    ],
}
