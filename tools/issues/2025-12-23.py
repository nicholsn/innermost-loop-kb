"""Issue 013 — 2025-12-23. The frontier monopoly becomes a latency."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-23-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-23",
        "title": "Welcome to December 23, 2025",
        "url": URL,
        "thesis": "The monopoly on frontier cognition has dissolved into a mere six-month latency.",
        "body": """
# Welcome to December 23, 2025

The gap between closed and open stops being a gap and becomes a *duration*.
Zhipu's GLM-4.7 tops GPT-5.2 on WebDev Arena and breaks 73% on SWE-bench while
trailing the closed frontier by about half a year; Epoch puts the FrontierMath
lag at roughly seven months. A monopoly measured in months is a schedule, not a
moat.

Against that, the price of *agency* is rising even as the price of reasoning
falls — the hourly cost at the METR autonomy horizon is going up.
""",
    },
    "themes": [
        {"id": "open-weight-latency", "type": "Theme",
         "title": "The frontier gap becomes a measured latency", "first_seen": "2025-12-23",
         "domain": "models",
         "body": "Open-weight models trail the closed frontier by a number of months "
                 "that can be stated and tracked. The moat is re-described as a "
                 "release schedule."},
    ],
    "organizations": [
        {"id": "zhipu-ai", "type": "Organization", "title": "Zhipu AI",
         "description": "Beijing AI startup behind the open-weight GLM model family, whose GLM-4.7 "
                        "the corpus uses to state the open-closed frontier gap as a six-month latency.",
         "resource": "https://www.zhipuai.cn/",
         "sameAs": ["http://www.wikidata.org/entity/Q129572031"],
         "tags": ["startup", "open-source"],
         "body": "Chinese lab shipping the open-weight GLM family. In this corpus Zhipu AI is "
                 "the maker of [GLM-4.7](/systems/glm-4-7.md), whose "
                 "[WebDev Arena win over GPT-5.2 and 73% on SWE-bench](/developments/2025-12-23-glm-47-six-month-gap.md) "
                 "turned the gap between open and closed models into a stated duration of about "
                 "half a year — the [open-weight-latency](/themes/open-weight-latency.md) theme — "
                 "and later of [GLM-5](/systems/glm-5.md), the top open-weight model on agentic "
                 "benchmarks."},
        {"id": "satvu", "type": "Organization", "title": "SatVu",
         "resource": "https://www.satellitevu.com/", "body": "Thermal imaging satellites."},
        {"id": "intersect-power", "type": "Organization", "title": "Intersect Power",
         "resource": "https://intersectpower.com/", "body": "Clean energy developer."},
        {"id": "byd", "type": "Organization", "title": "BYD",
         "resource": "https://www.byd.com/", "body": "EV and battery manufacturer."},
        {"id": "war-department", "type": "Organization", "title": "US War Department",
         "body": "Partnered with xAI to deploy models on GenAI.mil."},
    ],
    "systems": [
        {"id": "glm-4-7", "type": "AISystem", "title": "GLM-4.7",
         "developed_by": [B + "organizations/zhipu-ai"], "modality": "text",
         "evaluated_on": [B + "benchmarks/webdev-arena", B + "benchmarks/swe-bench-pro"],
         "body": "Open-weight, and reported topping GPT-5.2 on WebDev Arena."},
        {"id": "universal-reasoning-models", "type": "AISystem",
         "title": "Universal Reasoning Models", "modality": "text",
         "body": "Reported 40% pass@1 on ARC-AGI-1 with an eighth of the parameters of a "
                 "standard Transformer."},
        {"id": "claude-code", "type": "AISystem", "title": "Claude Code",
         "developed_by": [B + "organizations/anthropic"], "modality": "code",
         "evaluated_on": [B + "benchmarks/posttrainbench"],
         "description": "Anthropic's terminal coding agent, the harness through which the corpus "
                        "most often watches a model write, ship and post-train software "
                        "without a human in the loop.",
         "resource": "https://claude.com/product/claude-code",
         "sameAs": ["http://www.wikidata.org/entity/Q138457287"],
         "tags": ["coding-agent"],
         "body": "Claude Code is Anthropic's command-line agent that runs Claude models against a "
                 "codebase ([product page](https://claude.com/product/claude-code)). It enters the "
                 "corpus with a tooling note, "
                 "[Language Server Protocol support](/developments/2025-12-23-claude-code-lsp.md), "
                 "but within days becomes the newsletter's central instrument of recursion: its own "
                 "creator reports it [wrote 200 pull requests without him](/developments/2025-12-27-cherny-200-pull-requests.md), "
                 "and Anthropic confirms it "
                 "[wrote the whole Claude Cowork desktop app](/developments/2026-01-13-claude-code-writes-cowork.md) "
                 "in a week and a half. By March 2026 PostTrainBench v1.0 names "
                 "[Opus 4.6 running in Claude Code](/developments/2026-03-12-posttrainbench-v1.md) "
                 "the most capable agent at automating a model's own post-training."},
    ],
    "benchmarks": [
        {"id": "webdev-arena", "type": "Benchmark", "title": "WebDev Arena",
         "measures_capability": "head-to-head web development tasks"},
    ],
    "facilities": [
        {"id": "rockdale-bitcoin-mine", "type": "Facility", "title": "Rockdale mine (Texas)",
         "located_in": "Rockdale, Texas, USA", "capacity": "700 MW",
         "body": "Its waste heat was imaged from orbit — compute as a visible thermal feature."},
        {"id": "chaotan-one", "type": "Facility", "title": "Chaotan One",
         "operated_by": [B + "organizations/china"], "located_in": "China",
         "body": "First commercial generator using supercritical CO2 rather than steam."},
    ],
    "developments": [
        {"id": "2025-12-23-glm-47-six-month-gap",
         "title": "GLM-4.7 tops GPT-5.2 on WebDev Arena, trailing the frontier by six months",
         "claim": "Zhipu AI released GLM-4.7, an open-weight model that tops GPT-5.2 in WebDev "
                  "Arena and breaks 73% on SWE-bench, trailing the closed frontier by about "
                  "half a year.",
         "domain": "models", "actor": ["zhipu-ai"], "score": "73% SWE-bench; ~6 month lag",
         "about": [B + "systems/glm-4-7", B + "benchmarks/webdev-arena"],
         "evidences": ["open-weight-latency", "silicon-curtain"],
         "supersedes": [B + "developments/2025-12-12-gpt52-swebench-pro-sota"]},
        {"id": "2025-12-23-epoch-seven-month-lag",
         "title": "Epoch puts the open-weight FrontierMath lag at seven months",
         "claim": "Epoch AI found leading open-weight Chinese models trail the FrontierMath "
                  "Tiers 1-3 edge by approximately seven months.",
         "domain": "benchmarks", "actor": ["epoch-ai"], "score": "~7 months",
         "about": [B + "benchmarks/frontiermath"],
         "evidences": ["open-weight-latency"]},
        {"id": "2025-12-23-universal-reasoning-models",
         "title": "Universal Reasoning Models hit 40% on ARC-AGI with an eighth the parameters",
         "claim": "Researchers unveiled Universal Reasoning Models achieving 40% pass@1 on "
                  "ARC-AGI-1 with one-eighth the parameters of standard Transformers.",
         "domain": "models", "score": "40% pass@1, 1/8 params",
         "about": [B + "systems/universal-reasoning-models", B + "benchmarks/arc-agi-1"],
         "evidences": ["reasoning-price-deflation"]},
        {"id": "2025-12-23-agent-hourly-cost-rising",
         "title": "The hourly cost of agency is rising even as reasoning deflates",
         "claim": "Analysis suggests the hourly cost of agents at METR's 50% autonomy time "
                  "horizon is increasing, pressuring the inference stack.",
         "domain": "economics", "actor": ["metr"],
         "evidences": ["autonomy-clock-speed", "reasoning-price-deflation"],
         "body": "A counterweight the corpus should keep: reasoning gets cheaper per token "
                 "while sustained autonomy gets more expensive per hour."},
        {"id": "2025-12-23-microsoft-eliminate-c-cpp-2030",
         "title": "Microsoft sets a goal of removing all C and C++ by 2030",
         "claim": "Microsoft set a North Star goal to eliminate every line of C and C++ from "
                  "its codebase by 2030, targeting a velocity where one engineer rewrites a "
                  "million lines a month.",
         "domain": "society", "actor": ["microsoft"], "score": "1M lines/engineer/month",
         "evidences": ["engineer-as-supervisor"]},
        {"id": "2025-12-23-claude-code-lsp",
         "title": "Claude Code adds Language Server Protocol support",
         "claim": "Claude Code added Language Server Protocol support for deeper editor "
                  "integration.",
         "domain": "agents", "actor": ["anthropic"], "about": [B + "systems/claude-code"],
         "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-23-youtube-playables-builder",
         "title": "YouTube ships a no-code game builder driven by prompts",
         "claim": "YouTube launched a no-code Playables Builder letting creators generate games "
                  "from prompts.",
         "domain": "society", "actor": ["youtube"], "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-23-war-department-xai-genai-mil",
         "title": "The War Department partners with xAI on GenAI.mil",
         "claim": "The US War Department partnered with xAI to deploy advanced models on "
                  "GenAI.mil.",
         "domain": "policy", "actor": ["war-department", "xai"],
         "evidences": ["politics-as-infrastructure"]},
        {"id": "2025-12-23-satvu-images-mine-waste-heat",
         "title": "A satellite images the waste heat of a 700-MW mine from orbit",
         "claim": "A SatVu heat-seeking satellite captured waste heat from a 700-MW Bitcoin "
                  "mine in Rockdale, Texas, visible from orbit.",
         "domain": "energy", "actor": ["satvu"], "score": "700 MW",
         "about": [B + "facilities/rockdale-bitcoin-mine"],
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"],
         "body": "Compute becomes a thermal feature of the planet, observable from space."},
        {"id": "2025-12-23-alphabet-buys-intersect-power",
         "title": "Alphabet buys Intersect Power for $4.75B and a 15 GW pipeline",
         "claim": "Alphabet is buying clean energy developer Intersect Power for $4.75 billion, "
                  "securing a pipeline of more than 15 gigawatts.",
         "domain": "energy", "actor": ["google", "intersect-power"], "score": "$4.75B, 15+ GW",
         "evidences": ["capital-takes-the-plant", "burning-molecules-for-tokens"]},
        {"id": "2025-12-23-chaotan-one-supercritical-co2",
         "title": "China activates the first commercial supercritical CO2 generator",
         "claim": "China activated Chaotan One, the first commercial power generator using "
                  "supercritical carbon dioxide instead of steam.",
         "domain": "energy", "actor": ["china"], "about": [B + "facilities/chaotan-one"],
         "evidences": ["industrialized-nature"]},
        {"id": "2025-12-23-byd-400km-in-5-minutes",
         "title": "BYD chargers add 400 km of range in five minutes",
         "claim": "BYD charging stations can add 400 km of EV range in five minutes.",
         "domain": "energy", "actor": ["byd"], "score": "400 km / 5 min"},
        {"id": "2025-12-23-mosquito-proboscis-bioprinting",
         "title": "Mosquito proboscides are used as 20-micron printing nozzles",
         "claim": "Researchers used female mosquito proboscides as high-resolution printing "
                  "nozzles, achieving 20-micron line widths to print bioscaffolds.",
         "domain": "biotech", "score": "20 microns",
         "evidences": ["compiling-matter", "hardware-grade-biology"]},
        {"id": "2025-12-23-shenzhen-robots-ride-subway",
         "title": "Robots ride the Shenzhen subway alone to make deliveries",
         "claim": "In Shenzhen, robots are riding the subway unaccompanied to make deliveries.",
         "domain": "robotics", "actor": ["china"],
         "evidences": ["autonomy-clock-speed"]},
        {"id": "2025-12-23-robot-olympics-gold",
         "title": "Physical Intelligence agents win Robot Olympics golds by fine-tuning",
         "claim": "Physical Intelligence's agents won gold medals at the Robot Olympics for "
                  "tasks like spreading peanut butter and unlocking doors, simply by "
                  "fine-tuning vision-language-action models.",
         "domain": "robotics", "actor": ["physical-intelligence"],
         "evidences": ["generalism-beats-specialism"]},
        {"id": "2025-12-23-big-red-button-abandoned",
         "title": "The industry drops the big red button for probabilistic failure limits",
         "claim": "With a million robots expected, the industry is abandoning the big red "
                  "button standard for probabilistic failure limits, accepting that physically "
                  "stopping a humanoid is no longer viable.",
         "domain": "policy", "evidences": ["legislating-the-shift", "physical-recursion"],
         "body": "A safety standard retired because the assumption underneath it — that a "
                 "human can intervene in time — stopped holding."},
        {"id": "2025-12-23-neural-nets-solve-kohn-sham",
         "title": "Neural networks solve the Kohn-Sham equation directly",
         "claim": "Researchers used neural networks to directly solve the Kohn-Sham equation, "
                  "optimizing the ground state of density functional theory.",
         "domain": "science", "evidences": ["root-node-problems", "automated-science"]},
        {"id": "2025-12-23-simulating-lipid-flip-flops",
         "title": "AI simulates rare biomolecular events invisible to dynamics",
         "claim": "Researchers used AI to simulate rare biomolecular events such as lipid "
                  "flip-flops that conventional dynamics simulations could not reach.",
         "domain": "science", "evidences": ["automated-science"]},
    ],
}
