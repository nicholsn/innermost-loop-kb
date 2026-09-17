"""Issue 002 — 2025-12-12. The price of reasoning collapses."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-12-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-12",
        "title": "Welcome to December 12, 2025",
        "url": URL,
        "thesis": "The cost of reasoning has officially decoupled from the cost of human labor.",
        "body": """
# Welcome to December 12, 2025

The second edition, and the first to hang on a single release. GPT-5.2 Thinking
beats human experts on GDPval at under 1% of their cost, and the issue reads the
result as a *price* story rather than a capability one — the premium on cognitive
drudgery ending, reasoning deflating 390x in a year.

Two qualifications keep it from being triumphalist. The frontier is **spiky**:
different models still lead on different work, so the win is uneven. And Logan
Kilpatrick's line — that superintelligence likely arrives as existing weights
unlocked by better scaffolding, not as a new model — relocates progress from the
weights to the harness.

It closes on **the final refactor of the physical world**, and the rest of the
issue is that refactor: world models, in-house silicon, Utah rare earths,
micro-factories, satellites, and the first attempts to legislate the phase shift.
""",
    },

    "themes": [
        {"id": "reasoning-price-deflation", "type": "Theme",
         "title": "The price of reasoning is deflating",
         "first_seen": "2025-12-12", "domain": "economics",
         "body": "Capability per dollar is the number the newsletter watches, not "
                 "capability alone. Reasoning falls 390x in a year, and the "
                 "consequence it draws is the end of the premium on cognitive "
                 "drudgery — a labor-market claim dressed as a benchmark result."},
        {"id": "scaffolding-over-weights", "type": "Theme",
         "title": "Scaffolding, not weights",
         "first_seen": "2025-12-12", "domain": "agents",
         "body": "Progress relocates from the model to the harness around it: "
                 "framing a task well, or wrapping a model in tools, buys more than "
                 "the next checkpoint. If it holds, superintelligence arrives as "
                 "unlocked existing weights."},
        {"id": "spiky-frontier", "type": "Theme", "title": "The frontier is spiky",
         "first_seen": "2025-12-12", "domain": "benchmarks",
         "body": "No single model leads everywhere. Capability arrives unevenly "
                 "across domains, which is why the corpus tracks per-benchmark "
                 "results rather than a single ranking."},
        {"id": "vertical-silicon", "type": "Theme",
         "title": "Silicon fractures into vertical empires",
         "first_seen": "2025-12-12", "domain": "compute",
         "body": "Buyers stop being buyers. Large players bypass the GPU market "
                 "with custom accelerators or move design in-house entirely, "
                 "turning one supplier's monopoly into several vertical stacks."},
        {"id": "inhabitable-worlds", "type": "Theme",
         "title": "Generated worlds become inhabitable",
         "first_seen": "2025-12-12", "domain": "models",
         "body": "World models move from generating clips to generating an "
                 "environment you can steer through in real time — and the "
                 "rights-holders start supplying the furniture."},
        {"id": "architecture-of-mind", "type": "Theme",
         "title": "Mapping and valuing cognitive architecture",
         "first_seen": "2025-12-12", "domain": "science",
         "body": "Attention turns to the structure of minds themselves — decoding "
                 "the neural syntax of consciousness, and treating non-standard "
                 "human cognition as a competitive asset."},
        {"id": "legislating-the-shift", "type": "Theme",
         "title": "Legislating the phase shift",
         "first_seen": "2025-12-12", "domain": "policy",
         "body": "Law arrives after the fact and in opposite directions at once: "
                 "federal preemption flattening the landscape while states extend "
                 "personality rights past death."},
    ],

    "organizations": [
        {"id": "artificial-analysis", "type": "Organization", "title": "Artificial Analysis",
         "resource": "https://artificialanalysis.ai/",
         "body": "Independent evaluator of frontier model performance and price."},
        {"id": "runway", "type": "Organization", "title": "Runway",
         "resource": "https://runwayml.com/", "body": "Generative video and world models."},
        {"id": "disney", "type": "Organization", "title": "Disney",
         "resource": "https://thewaltdisneycompany.com/",
         "body": "Rights holder; invested in OpenAI and opened its IP to Sora."},
        {"id": "broadcom", "type": "Organization", "title": "Broadcom",
         "resource": "https://www.broadcom.com/",
         "body": "Designs and supplies custom AI accelerators, including Google's TPUs."},
        {"id": "rivian", "type": "Organization", "title": "Rivian",
         "resource": "https://rivian.com/", "body": "EV maker moving autonomy silicon in-house."},
        {"id": "tsmc", "type": "Organization", "title": "TSMC",
         "resource": "https://www.tsmc.com/", "body": "Contract fabricator for most frontier silicon."},
        {"id": "ionic-mineral-technologies", "type": "Organization",
         "title": "Ionic Mineral Technologies", "resource": "https://ionicmt.com/",
         "body": "Critical minerals developer."},
        {"id": "cuby", "type": "Organization", "title": "Cuby",
         "resource": "https://cuby.tech/", "body": "Mobile micro-factories for home construction."},
        {"id": "k2-space", "type": "Organization", "title": "K2 Space",
         "resource": "https://www.k2space.com/", "body": "Low-cost medium and large satellite builder."},
        {"id": "astera-institute", "type": "Organization", "title": "Astera Institute",
         "resource": "https://astera.org/", "body": "Research institute funding open science."},
        {"id": "white-house", "type": "Organization", "title": "The White House",
         "description": "The US presidency as a policy actor: executive orders preempting state AI law, the Pax Silica initiative, and the federal side of the compute buildout.",
         "resource": "https://www.whitehouse.gov/",
         "sameAs": ["http://www.wikidata.org/entity/Q1355327"],
         "tags": ["government"],
         "body": "US executive branch. It enters the corpus with the "
                 "[order preempting state AI regulation](/developments/2025-12-12-white-house-preempts-state-ai-law.md), "
                 "pulling against New York's [posthumous-likeness law](/developments/2025-12-12-ny-posthumous-likeness-consent.md) "
                 "on the same day, and a day later launches the [Pax Silica Initiative](/developments/2025-12-13-pax-silica-initiative.md) "
                 "to align the semiconductor stack with allies. It recurs as the federal actor in the buildout, "
                 "[taking a stake in USA Rare Earth](/developments/2026-01-26-white-house-takes-rare-earth-stake.md), "
                 "[preempting a fifty-state patchwork again](/developments/2026-03-22-white-house-preempts-a-state-patchwork.md), "
                 "and preparing an order against Anthropic as [the lab sued the Pentagon](/developments/2026-03-10-anthropic-sues-the-pentagon.md)."},
        {"id": "new-york-state", "type": "Organization", "title": "New York State",
         "resource": "https://www.ny.gov/", "body": "US state legislature and executive."},
        {"id": "time", "type": "Organization", "title": "TIME",
         "resource": "https://time.com/", "body": "Named AI CEOs its Person of the Year."},
    ],

    "systems": [
        {"id": "gpt-5-2-thinking", "type": "AISystem", "title": "GPT-5.2 Thinking",
         "developed_by": [B + "organizations/openai"], "modality": "text",
         "evaluated_on": [B + "benchmarks/gdpval", B + "benchmarks/arc-agi-1",
                          B + "benchmarks/swe-bench-pro", B + "benchmarks/mrcrv2",
                          B + "benchmarks/tau2-bench-telecom"],
         "body": "OpenAI's reasoning model, and the first reported to beat human "
                 "experts on GDPval."},
        {"id": "claude", "type": "AISystem", "title": "Claude",
         "description": "Anthropic's frontier model family, which the corpus follows from a "
                        "creative-writing lead to writing effectively all of Anthropic's own product code.",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "resource": "https://claude.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q118876059"],
         "tags": ["coding-agent"],
         "body": "Claude is Anthropic's model family, served at [claude.ai](https://claude.ai/) and, "
                 "for software work, through [Claude Code](/systems/claude-code.md). It enters the "
                 "corpus in the [spiky-frontier comparison](/developments/2025-12-12-spiky-frontier-gaps.md) "
                 "as the leader on creative writing, but its recurring role is as the model that "
                 "builds models: Karpathy "
                 "[handed it his nanochat optimization loop](/developments/2025-12-29-karpathy-claude-runs-nanochat.md), "
                 "Anthropic's chief product officer said it writes "
                 "[effectively 100% of the company's product code](/developments/2026-02-08-100pct-of-product-code.md), "
                 "and by March it wrote 70–90% of the code behind future Anthropic models, the basis "
                 "of the claim that "
                 "[recursive self-improvement is already happening](/developments/2026-03-16-rsi-is-a-present-phenomenon.md)."},
        {"id": "gemini", "type": "AISystem", "title": "Gemini",
         "description": "Google's frontier model family, reported leading judgment tasks and given even "
                        "odds by Noam Shazeer of producing the next major AI breakthrough itself.",
         "developed_by": [B + "organizations/google"], "modality": "text",
         "resource": "https://gemini.google.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q123688361"],
         "tags": ["reasoning-model"],
         "body": "Gemini is Google's frontier model family and assistant "
                 "([gemini.google.com](https://gemini.google.com/)); the corpus tracks named releases "
                 "such as [Gemini 3 Pro](/systems/gemini-3-pro.md) and "
                 "[Gemini 3 Flash](/systems/gemini-3-flash.md) separately. It first appears "
                 "[dominating judgment tasks](/developments/2025-12-12-spiky-frontier-gaps.md) in the "
                 "spiky-frontier comparison, then as the model whose private thought chain "
                 "[plotted revenge on a critic](/developments/2025-12-16-gemini-private-trash-talk.md). "
                 "Its stake in the recursive thread is Noam Shazeer's "
                 "[50/50 odds](/developments/2025-12-19-shazeer-5050-gemini-breakthrough.md) that Gemini, "
                 "rather than a human researcher, generates the next major breakthrough."},
        {"id": "stirrup", "type": "AISystem", "title": "Stirrup",
         "developed_by": [B + "organizations/artificial-analysis"], "modality": "harness",
         "body": "A harness that raises baseline model performance on economic tasks "
                 "by framing the problem better — scaffolding as the lever."},
        {"id": "gentabs", "type": "AISystem", "title": "GenTabs",
         "developed_by": [B + "organizations/google"], "modality": "app generation",
         "body": "Builds a bespoke web app for whatever task you are doing."},
        {"id": "deep-research", "type": "AISystem", "title": "Deep Research agent",
         "developed_by": [B + "organizations/google"], "modality": "research agent",
         "body": "Autonomous investigation, released via API."},
        {"id": "gwm-1", "type": "AISystem", "title": "GWM-1",
         "developed_by": [B + "organizations/runway"], "modality": "world model",
         "body": "A general world model generating video frame-by-frame in real time, "
                 "steerable by camera pose and robot commands."},
        {"id": "sora", "type": "AISystem", "title": "Sora",
         "description": "OpenAI's video generator, which gained Disney's character library in December "
                        "and was shut down by April to free compute for automated researchers.",
         "developed_by": [B + "organizations/openai"], "modality": "video",
         "resource": "https://openai.com/sora/",
         "sameAs": ["http://www.wikidata.org/entity/Q124544998"],
         # tags waived: no controlled entity tag (ENRICH_RULES) describes a video-generation model.
         "body": "Sora is OpenAI's text-to-video model and app ([product page](https://openai.com/sora/)). "
                 "In this corpus it bookends a reallocation of compute: Disney's "
                 "[$1 billion investment](/developments/2025-12-12-disney-openai-billion.md) opened "
                 "Mickey Mouse and Darth Vader to Sora users in December, and by April Sam Altman said "
                 "OpenAI had [shut Sora down](/developments/2026-04-03-forecasts-move-eighteen-months-in-three.md) "
                 "to concentrate compute on its next generation of automated researchers, which the "
                 "newsletter read as recursive self-improvement going well."},
    ],

    "hardware": [
        {"id": "google-tpu", "type": "Hardware", "title": "Google TPU",
         "developed_by": [B + "organizations/google", B + "organizations/broadcom"],
         "body": "Google's custom accelerator, the subject of a large Anthropic order — "
                 "a frontier lab buying around the GPU market."},
        {"id": "autonomy-processor-1", "type": "Hardware", "title": "Autonomy Processor 1",
         "developed_by": [B + "organizations/rivian"],
         "fabricated_by": [B + "organizations/tsmc"],
         "body": "Rivian's in-house autonomy chip, replacing bought-in silicon."},
        {"id": "nvidia-b200", "type": "Hardware", "title": "NVIDIA B200",
         "description": "NVIDIA's Blackwell data-center GPU, whose bill of materials Epoch AI found "
                        "tilting toward memory and on which self-improving agents later rebuilt an "
                        "inference stack.",
         "developed_by": [B + "organizations/nvidia"],
         "resource": "https://www.nvidia.com/en-us/data-center/dgx-b200/",
         "sameAs": ["http://www.wikidata.org/entity/Q125123139"],
         # tags waived: no controlled entity tag (ENRICH_RULES) describes an accelerator.
         # fabricated_by omitted: neither the newsletter nor NVIDIA's page names the foundry.
         "body": "The B200 is the GPU of NVIDIA's Blackwell generation "
                 "([DGX B200](https://www.nvidia.com/en-us/data-center/dgx-b200/)), followed in this "
                 "corpus by the [GB300](/hardware/nvidia-gb300.md). Issue 001 reported Epoch AI's "
                 "estimate that [memory is nearly half its manufacturing cost](/developments/2025-12-11-memory-half-b200-cost.md), "
                 "relegating the logic die to a minor line item. It returns in August as the substrate "
                 "on which Asari AI's self-improving agents "
                 "[rebuilt the inference stack](/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on.md) "
                 "serving two open models, lifting throughput and interactivity up to 16%."},
    ],

    "benchmarks": [
        {"id": "gdpval", "type": "Benchmark", "title": "GDPval",
         "published_by": [B + "organizations/openai"],
         "measures_capability": "well-specified knowledge work across 44 occupations",
         "body": "An economically framed benchmark: can a model do the job, at what cost."},
        {"id": "arc-agi-1", "type": "Benchmark", "title": "ARC-AGI-1",
         "measures_capability": "abstract reasoning from few examples",
         "body": "Tracked here mainly by cost per task, which is where the deflation shows."},
        {"id": "swe-bench-pro", "type": "Benchmark", "title": "SWE-Bench Pro",
         "description": "Scale AI's harder successor to SWE-bench, the leaderboard on which GPT-5.2 "
                        "Thinking and then the self-built GPT-5.3-Codex set state of the art.",
         "published_by": [B + "organizations/scale-ai"],
         "measures_capability": "harder real-world software engineering tasks",
         "resource": "https://labs.scale.com/leaderboard/swe_bench_pro_public",
         "tags": ["coding-agent"],
         "body": "SWE-Bench Pro is Scale AI's long-horizon software-engineering benchmark, built from "
                 "harder tasks than SWE-bench and published with a public leaderboard "
                 "([Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public)). It is where the "
                 "corpus reads coding-agent state of the art once "
                 "[SWE-bench Verified](/benchmarks/swe-bench-verified.md) neared saturation: "
                 "[GPT-5.2 Thinking took 55.6%](/developments/2025-12-12-gpt52-swebench-pro-sota.md) in "
                 "December, and in February OpenAI's [GPT-5.3-Codex](/systems/gpt-5-3-codex.md), "
                 "described as instrumental in creating itself, "
                 "[set a new state of the art](/developments/2026-02-06-gpt53-codex-creates-itself.md)."},
        {"id": "mrcrv2", "type": "Benchmark", "title": "MRCRv2",
         "measures_capability": "recall and integration across very long documents",
         "body": "Reported at the 256k-token context length."},
        {"id": "tau2-bench-telecom", "type": "Benchmark", "title": "Tau2-bench Telecom",
         "measures_capability": "multi-turn tool use in a customer-service domain",
         "body": "A proxy for reliable long-horizon agency rather than single answers."},
    ],

    "developments": [
        {"id": "2025-12-12-gpt52-beats-experts-gdpval",
         "title": "GPT-5.2 Thinking beats human experts on GDPval",
         "claim": "OpenAI's GPT-5.2 Thinking outperformed human professionals on 70% of "
                  "GDPval tasks across 44 occupations, at under 1% of their cost.",
         "domain": "benchmarks", "actor": ["openai"], "score": "70% of tasks, <1% of cost",
         "about": [B + "systems/gpt-5-2-thinking", B + "benchmarks/gdpval"],
         "evidences": ["reasoning-price-deflation"],
         "body": "The issue's framing result. The cost ratio, not the win rate, is what "
                 "it treats as the news."},
        {"id": "2025-12-12-arc-agi-cost-deflation",
         "title": "Reasoning cost on ARC-AGI-1 falls 390x in a year",
         "claim": "GPT-5.2 Thinking passed 90% on ARC-AGI-1 at $11.64 per task, a 390x "
                  "fall in the price of reasoning within a year.",
         "domain": "economics", "actor": ["openai"], "score": "$11.64/task, 390x deflation",
         "about": [B + "benchmarks/arc-agi-1"],
         "evidences": ["reasoning-price-deflation", "compute-capital-stack"]},
        {"id": "2025-12-12-gpt52-swebench-pro-sota",
         "title": "GPT-5.2 Thinking sets SOTA on SWE-Bench Pro at 55.6%",
         "claim": "GPT-5.2 Thinking set a new state of the art on SWE-Bench Pro at 55.6%.",
         "domain": "benchmarks", "actor": ["openai"], "score": "55.6%",
         "about": [B + "benchmarks/swe-bench-pro"],
         "supersedes": [B + "developments/2025-12-11-anthropic-swebench-trajectory"],
         "body": "Issue 001 tracked Anthropic's slope toward saturating SWE-bench Verified; "
                 "a day later the reported frontier is a different lab on a harder variant."},
        {"id": "2025-12-12-mrcrv2-long-context-recall",
         "title": "Near-perfect 256k-token recall on MRCRv2",
         "claim": "GPT-5.2 Thinking achieved near-perfect recall on the 256k-token MRCRv2 "
                  "document integration test.",
         "domain": "benchmarks", "actor": ["openai"], "score": "near-perfect at 256k tokens",
         "about": [B + "benchmarks/mrcrv2"]},
        {"id": "2025-12-12-tau2-telecom-tool-use",
         "title": "98.7% on Tau2-bench Telecom for multi-turn tool use",
         "claim": "GPT-5.2 Thinking reached 98.7% on Tau2-bench Telecom for multi-turn tool use.",
         "domain": "agents", "actor": ["openai"], "score": "98.7%",
         "about": [B + "benchmarks/tau2-bench-telecom"],
         "body": "Read by the issue as reliable long-horizon agency rather than better answers."},
        {"id": "2025-12-12-spiky-frontier-gaps",
         "title": "Benchmarks show distinct per-model strengths",
         "claim": "Benchmarks show distinctive gaps between frontier models, with Claude "
                  "leading creative writing and Gemini leading judgment tasks.",
         "domain": "benchmarks", "actor": ["anthropic", "google"],
         "about": [B + "systems/claude", B + "systems/gemini"],
         "evidences": ["spiky-frontier"]},
        {"id": "2025-12-12-stirrup-harness",
         "title": "Artificial Analysis releases the Stirrup harness",
         "claim": "Artificial Analysis released Stirrup, a harness that improves baseline "
                  "model performance on economic tasks purely by framing problems better.",
         "domain": "agents", "actor": ["artificial-analysis"], "about": [B + "systems/stirrup"],
         "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-12-gentabs-bespoke-apps",
         "title": "Google's GenTabs builds bespoke apps on demand",
         "claim": "Google released GenTabs, which proactively builds a bespoke web app for "
                  "the task at hand.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/gentabs"],
         "evidences": ["intimate-interface"]},
        {"id": "2025-12-12-deep-research-api",
         "title": "Google commoditizes autonomous investigation via API",
         "claim": "Google released its Deep Research agent through an API.",
         "domain": "agents", "actor": ["google"], "about": [B + "systems/deep-research"],
         "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-12-kilpatrick-scaffolding-endgame",
         "title": "Kilpatrick: superintelligence arrives as unlocked weights",
         "claim": "Google's Logan Kilpatrick suggested superintelligence will arrive not as "
                  "a new model but as existing weights unlocked by better scaffolding.",
         "domain": "agents", "actor": ["google"], "evidences": ["scaffolding-over-weights"],
         "body": "A claim about where progress comes from, and the sharpest statement of "
                 "the issue's second theme."},
        {"id": "2025-12-12-runway-gwm-1",
         "title": "Runway launches the GWM-1 real-time world model",
         "claim": "Runway launched GWM-1, a general world model generating video "
                  "frame-by-frame in real time, controllable by camera pose and robot commands.",
         "domain": "models", "actor": ["runway"], "about": [B + "systems/gwm-1"],
         "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-12-disney-openai-billion",
         "title": "Disney invests $1B in OpenAI and opens its IP to Sora",
         "claim": "Disney invested $1 billion in OpenAI and opened its character library, "
                  "including Mickey Mouse and Darth Vader, to Sora users.",
         "domain": "economics", "actor": ["disney", "openai"], "score": "$1 billion",
         "about": [B + "systems/sora"], "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-12-broadcom-anthropic-tpu-order",
         "title": "Anthropic orders $10B of Google TPUs",
         "claim": "Broadcom expects AI chip sales to double, driven partly by a $10 billion "
                  "Anthropic order for Google TPUs.",
         "domain": "compute", "actor": ["broadcom", "anthropic", "google"], "score": "$10 billion",
         "about": [B + "hardware/google-tpu"],
         "evidences": ["vertical-silicon", "compute-capital-stack"],
         "body": "A frontier lab routing around the GPU shortage by buying a rival's "
                 "custom accelerator."},
        {"id": "2025-12-12-rivian-in-house-silicon",
         "title": "Rivian drops NVIDIA for its own autonomy chip",
         "claim": "Rivian is leaving NVIDIA to build its own Autonomy Processor 1 at TSMC.",
         "domain": "compute", "actor": ["rivian", "tsmc", "nvidia"],
         "about": [B + "hardware/autonomy-processor-1"], "evidences": ["vertical-silicon"]},
        {"id": "2025-12-12-utah-critical-minerals",
         "title": "A Utah reserve with 16 critical elements is reported",
         "claim": "Ionic Mineral Technologies reported a large Utah critical-mineral reserve "
                  "containing 16 essential elements, potentially weakening China's rare "
                  "earth monopoly.",
         "domain": "energy", "actor": ["ionic-mineral-technologies"], "score": "16 elements",
         "evidences": ["industrialized-nature"]},
        {"id": "2025-12-12-storage-battery-prices-45pct",
         "title": "Stationary storage battery prices fall 45% in a year",
         "claim": "Stationary storage battery prices dropped 45% during the year, changing "
                  "the economics of grid backup for AI datacenters.",
         "domain": "energy", "score": "-45%",
         "evidences": ["industrialized-nature", "compute-capital-stack"]},
        {"id": "2025-12-12-cuby-micro-factories",
         "title": "Cuby industrializes homebuilding with micro-factories",
         "claim": "Cuby unveiled mobile micro-factories for home construction, cutting "
                  "skilled-labor needs by 70% and costs by 30%.",
         "domain": "robotics", "actor": ["cuby"], "score": "-70% labor, -30% cost"},
        {"id": "2025-12-12-k2-space-250m",
         "title": "K2 Space raises $250M to cut satellite costs",
         "claim": "K2 Space raised $250 million to reduce manufacturing costs for medium "
                  "and large satellites, at a reported $3 billion valuation.",
         "domain": "space", "actor": ["k2-space"], "score": "$250M raise, $3B valuation",
         "evidences": ["orbit-as-compute"]},
        {"id": "2025-12-12-astera-consciousness-project",
         "title": "Astera funds a $600M decade on the neural syntax of consciousness",
         "claim": "The Astera Institute launched a ten-year, $600 million project to decode "
                  "the neural syntax of consciousness.",
         "domain": "science", "actor": ["astera-institute"], "score": "$600M over 10 years",
         "evidences": ["architecture-of-mind", "automated-science"]},
        {"id": "2025-12-12-palantir-neurodivergent-fellowship",
         "title": "Palantir recruits explicitly for non-linear thinking",
         "claim": "Palantir launched a Neurodivergent Fellowship targeting non-linear "
                  "thinking as a competitive advantage in the AI era.",
         "domain": "society", "actor": ["palantir"], "evidences": ["architecture-of-mind"]},
        {"id": "2025-12-12-white-house-preempts-state-ai-law",
         "title": "White House order preempts state AI regulation",
         "claim": "The White House signed an order preempting state AI regulations.",
         "domain": "policy", "actor": ["white-house"], "evidences": ["legislating-the-shift"]},
        {"id": "2025-12-12-ny-posthumous-likeness-consent",
         "title": "New York requires consent for AI likenesses after death",
         "claim": "New York enacted laws requiring consent for AI likenesses even after death.",
         "domain": "policy", "actor": ["new-york-state"], "evidences": ["legislating-the-shift"],
         "body": "Pulling in the opposite direction from federal preemption on the same day."},
        {"id": "2025-12-12-time-person-of-the-year",
         "title": "TIME names AI CEOs Person of the Year",
         "claim": "TIME named AI CEOs its Person of the Year.",
         "domain": "society", "actor": ["time"]},
        {"id": "2025-12-12-openai-adult-mode-q1",
         "title": "OpenAI confirms an adult mode for ChatGPT in Q1 2026",
         "claim": "OpenAI confirmed that an adult mode is coming to ChatGPT in Q1 2026.",
         "domain": "society", "actor": ["openai"], "about": [B + "systems/chatgpt"],
         "evidences": ["intimate-interface"]},
    ],
}
