"""Issue 001 — 2025-12-11, the first edition of The Innermost Loop."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-11-2025"

SPEC = {
    "issue": {
        "date": "2025-12-11",
        "title": "Welcome to December 11, 2025",
        "url": URL,
        "thesis": "The Singularity is hitting a coordination tax.",
        "body": """
# Welcome to December 11, 2025

The first edition. It sets the newsletter's shape: a single day's developments,
grouped by where they bite, each one attributed and dated, ending on a line that
names the day's through-thread.

The framing claim is a *cost*, not a capability — multi-agent systems pay a
coordination tax, and the fix is hierarchy. The rest of the issue reads as
evidence that intelligence is escaping the datacenter into materials labs,
fulfillment centers, geothermal wells, orbit, and the ocean, while the capital
stack reorganizes itself around compute.

It closes on **compute is the new gold standard** — the thesis the following
232 issues elaborate.

See the [developments](/developments/2025-12-11-deepmind-coordination-tax.md)
this issue reports, and the [themes](/themes/compute-capital-stack.md) they feed.
""",
    },

    "themes": [
        {"id": "coordination-tax", "type": "Theme", "title": "The coordination tax",
         "first_seen": "2025-12-11", "domain": "agents",
         "body": "Scaling the *number* of intelligences is not free. Coordination "
                 "between agents amplifies error, and the measured remedy is "
                 "hierarchy — a boss — rather than more peers."},
        {"id": "compute-capital-stack", "type": "Theme", "title": "Compute is the capital stack",
         "first_seen": "2025-12-11", "domain": "economics",
         "body": "Compute stops behaving like an input and starts behaving like "
                 "money: backlogs, swaps, and balance sheets denominated in it. "
                 "The issue's closing line, *compute is the new gold standard*, "
                 "names this directly."},
        {"id": "orbit-as-compute", "type": "Theme", "title": "Orbit becomes a compute layer",
         "first_seen": "2025-12-11", "domain": "space",
         "body": "Satellites stop being sensors and relays and start being "
                 "datacenters — power budgets, training runs, and hosted models "
                 "above the atmosphere."},
        {"id": "automated-science", "type": "Theme", "title": "Science is automated at the hardware level",
         "first_seen": "2025-12-11", "domain": "science",
         "body": "Discovery moves from human-in-the-loop experiment design to "
                 "self-driving labs and models trained on physical data rather "
                 "than text."},
        {"id": "intimate-interface", "type": "Theme", "title": "The human interface becomes intimate",
         "first_seen": "2025-12-11", "domain": "society",
         "body": "The questions people bring to these systems shift from tasks to "
                 "bodies and health, and chat displaces the GUI as the default "
                 "surface."},
        {"id": "industrialized-nature", "type": "Theme", "title": "Industrializing geology and atmosphere",
         "first_seen": "2025-12-11", "domain": "energy",
         "body": "The physical world is re-engineered to feed compute — geothermal "
                 "drilled for datacenter power, weather modification proposed as a "
                 "service."},
        {"id": "biosphere-uplift", "type": "Theme", "title": "Uplifting the rest of the biosphere",
         "first_seen": "2025-12-11", "domain": "biotech",
         "body": "Machine intelligence is turned on non-human minds and on the "
                 "substitution of animal experiments by engineered tissue."},
    ],

    "organizations": [
        {"id": "google-deepmind", "type": "Organization", "title": "Google DeepMind",
         "description": "Google's AI research arm, source of the corpus's opening coordination-tax result and builder of the AlphaEvolve discovery loop.",
         "resource": "https://deepmind.google/",
         "sameAs": ["http://www.wikidata.org/entity/Q15733006"],
         "tags": ["frontier-lab", "research-lab"],
         "body": "Google's AI research organization. It opens the corpus with the "
                 "[coordination-tax measurement](/developments/2025-12-11-deepmind-coordination-tax.md) "
                 "that gives issue 001 its thesis. In the recursive-self-improvement strand it is the "
                 "builder of [AlphaEvolve](/systems/alphaevolve.md), the evolutionary coding agent that "
                 "[found an activation function tripling ReLU](/developments/2026-02-08-alphaevolve-finds-new-activations.md), "
                 "and the lab whose chief strategy officer said "
                 "[recursive self-improvement is what justifies the capex](/developments/2026-08-04-recursive-self-improvement-justifies-the-capex.md)."},
        {"id": "anthropic", "type": "Organization", "title": "Anthropic",
         "description": "Frontier lab behind Claude and Claude Code, the corpus's most frequent actor and the source of its most explicit first-person accounts of a model writing the lab's own code.",
         "resource": "https://www.anthropic.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q116758847"],
         "tags": ["frontier-lab"],
         "body": "Frontier model developer behind [Claude](/systems/claude.md) and Claude Code. It enters "
                 "the corpus with a [2%-per-month slope on SWE-bench Verified](/developments/2025-12-11-anthropic-swebench-trajectory.md). "
                 "In the recursive-self-improvement strand it supplies the report that Claude Code's creator "
                 "[had not opened an IDE in a month](/developments/2025-12-27-cherny-200-pull-requests.md), "
                 "the confirmation that [effectively all of its product code is written by Claude](/developments/2026-02-08-100pct-of-product-code.md), "
                 "and its alignment lead's statement that "
                 "[recursive self-improvement is a present phenomenon](/developments/2026-03-16-rsi-is-a-present-phenomenon.md)."},
        {"id": "google", "type": "Organization", "title": "Google",
         "description": "Alphabet's operating company: parent of DeepMind, developer of Gemini, Gemma and the TPU, and the actor whose researchers and co-founder the corpus reports steering toward the loop.",
         "resource": "https://about.google/",
         "sameAs": ["http://www.wikidata.org/entity/Q95"],
         "tags": ["big-tech"],
         "body": "Parent of [Google DeepMind](/organizations/google-deepmind.md); ships [Gemini](/systems/gemini.md), "
                 "the open-weight [Gemma](/systems/gemma.md) family and the [TPU](/hardware/google-tpu.md). "
                 "It enters the corpus with the [Gemini text-to-speech upgrade](/developments/2025-12-11-gemini-tts-upgrade.md). "
                 "In the recursive-self-improvement strand it appears for Noam Shazeer's "
                 "[even odds that Gemini makes the next breakthrough](/developments/2025-12-19-shazeer-5050-gemini-breakthrough.md), "
                 "the [internal-RL inner-optimizer result](/developments/2025-12-27-internal-rl-inner-optimizers.md), and the report that "
                 "[Sergey Brin is steering resources toward recursive self-improvement](/developments/2026-08-13-a-cofounder-steers-toward-recursive-self-improvement.md)."},
        {"id": "microsoft", "type": "Organization", "title": "Microsoft",
         "description": "Hyperscaler that ships Copilot, hosts OpenAI on Azure, and in this corpus designs a quantum chip with its own agent.",
         "resource": "https://www.microsoft.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q2283"],
         "tags": ["big-tech"],
         "body": "Ships [Copilot](/systems/copilot.md) and is OpenAI's principal cloud and capital partner. It enters "
                 "the corpus with the finding that [health was Copilot's dominant mobile topic](/developments/2025-12-11-copilot-health-dominant-topic.md). "
                 "In the recursive-self-improvement strand it appears for "
                 "[Majorana 2, a topological quantum chip designed with its own agentic AI](/developments/2026-06-03-a-quantum-chip-designed-by-an-agent.md), "
                 "and as the platform through which "
                 "[Meta burns trillions of tokens a week writing its own software](/developments/2026-08-21-trillions-of-tokens-a-week-to-write-its-own-software.md)."},
        {"id": "openai", "type": "Organization", "title": "OpenAI",
         "description": "Frontier lab behind ChatGPT, the GPT-5 line and Codex; the source of the corpus's first recursive-self-improvement report and of its most explicit statements that self-improving systems are in production.",
         "resource": "https://openai.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q21708200"],
         "tags": ["frontier-lab"],
         "body": "Ships [ChatGPT](/systems/chatgpt.md), the GPT-5 line and [Codex](/systems/codex.md). It enters the "
                 "corpus with [ChatGPT as the most downloaded iOS app](/developments/2025-12-11-chatgpt-most-downloaded-ios.md). "
                 "The recursive-self-improvement strand opens with its "
                 "[Codex babysitting its own training runs](/developments/2025-12-15-codex-babysits-own-training.md), "
                 "followed by [Altman confirming self-improving systems in production](/developments/2025-12-28-altman-self-improving-in-production.md) "
                 "and by [GPT-5.3-Codex](/systems/gpt-5-3-codex.md), the model it described as "
                 "[instrumental in creating itself](/developments/2026-02-06-gpt53-codex-creates-itself.md)."},
        {"id": "polymathic-ai", "type": "Organization", "title": "Polymathic AI",
         "resource": "https://polymathic-ai.org/",
         "body": "Collaboration training foundation models on scientific rather than text data."},
        {"id": "palantir", "type": "Organization", "title": "Palantir",
         "resource": "https://www.palantir.com/", "body": "Defense and industrial software; ships ShipOS."},
        {"id": "mercado-libre", "type": "Organization", "title": "Mercado Libre",
         "resource": "https://www.mercadolibre.com/", "body": "Latin American e-commerce and logistics."},
        {"id": "agility-robotics", "type": "Organization", "title": "Agility Robotics",
         "resource": "https://www.agilityrobotics.com/", "body": "Builds the Digit humanoid."},
        {"id": "oracle", "type": "Organization", "title": "Oracle",
         "resource": "https://www.oracle.com/", "body": "Cloud and datacenter capacity provider."},
        {"id": "supermicro", "type": "Organization", "title": "Supermicro",
         "resource": "https://www.supermicro.com/", "body": "Server and datacenter systems builder."},
        {"id": "xai", "type": "Organization", "title": "xAI",
         "description": "Elon Musk's frontier lab, builder of Grok and co-builder of the Memphis gigawatt datacenter; acquired by SpaceX in February 2026.",
         "resource": "https://x.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q120599684"],
         "tags": ["frontier-lab"],
         "body": "Frontier model developer; builds [Grok](/systems/grok.md) and, with Supermicro, the "
                 "[Memphis gigawatt datacenter](/facilities/memphis-gigawatt-datacenter.md). It enters the corpus with "
                 "[Tesla using Grok to design its chips](/developments/2025-12-11-tesla-grok-chip-design.md). In the "
                 "recursive-self-improvement strand it appears for the report that it "
                 "[used Claude to build Grok until cut off](/developments/2026-01-10-xai-used-claude-to-build-grok.md), for "
                 "[a co-founder's resignation warning of live loops within a year](/developments/2026-02-11-xai-cofounder-resigns-warning.md), "
                 "and for Grok 4.3 [improving every few days](/developments/2026-05-17-models-improve-every-few-days.md). "
                 "It was [acquired by SpaceX](/developments/2026-02-03-spacex-acquires-xai.md) in February 2026."},
        {"id": "epoch-ai", "type": "Organization", "title": "Epoch AI",
         "description": "Research institute that measures AI compute, cost and capability trends; the corpus's most-cited source of rates and doubling times.",
         "resource": "https://epoch.ai/",
         "tags": ["research-lab", "nonprofit"],
         "body": "Research group measuring AI compute and economics. It enters the corpus with the estimate that "
                 "[memory is nearly half the manufacturing cost of a B200](/developments/2025-12-11-memory-half-b200-cost.md), "
                 "then publishes the [autonomous time horizon](/benchmarks/autonomous-time-horizon.md) behind issue 003's "
                 "[4.9-hour state of the art](/developments/2025-12-13-autonomy-time-horizon-sota.md) and the finding that "
                 "[global AI compute doubles every seven months](/developments/2026-01-11-compute-doubles-every-7-months.md). "
                 "In the recursive-self-improvement strand it is the measurer rather than an actor: the rates against "
                 "which the loop's claims are checked."},
        {"id": "nvidia", "type": "Organization", "title": "NVIDIA",
         "description": "Dominant accelerator designer whose GPUs the buildout runs on; in this corpus its cost structure, its software moat and its post-training stack are all reported being reworked.",
         "resource": "https://www.nvidia.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q182477"],
         "tags": ["chipmaker", "big-tech"],
         "body": "Designs the accelerators the buildout runs on. Issue 001 carries Epoch AI's estimate that "
                 "[memory is nearly half the manufacturing cost of a B200](/developments/2025-12-11-memory-half-b200-cost.md). "
                 "In the recursive-self-improvement strand it "
                 "[sees no wall in post-training and opens Nemotron 3 Super](/developments/2026-03-12-nemotron-3-super-no-wall.md), "
                 "and it is the incumbent whose software advantage narrows when "
                 "[agents write the kernels for a challenger GPU](/developments/2026-07-04-agents-write-the-kernels-closing-a-software-gap.md)."},
        {"id": "tesla", "type": "Organization", "title": "Tesla",
         "description": "Elon Musk's vehicle, robotics and energy company; in this corpus a chip designer using Grok, and an early deployer of unsupervised robotaxis and Optimus.",
         "resource": "https://www.tesla.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q478214"],
         "tags": ["big-tech"],
         "body": "Uses Grok in its own silicon design. It enters the corpus with Musk confirming that "
                 "[Grok is used to design its chips](/developments/2025-12-11-tesla-grok-chip-design.md), the corpus's first "
                 "instance of a model designing the silicon that will run models. Later items include "
                 "[unsupervised robotaxis in Austin](/developments/2025-12-15-unsupervised-robotaxis-austin.md), "
                 "[Fremont converting to Optimus production](/developments/2026-01-31-fremont-converts-to-optimus.md) and the "
                 "[terafab plan](/developments/2026-01-29-tesla-terafab.md) that names chip production as its bottleneck."},
        {"id": "unsloth-ai", "type": "Organization", "title": "Unsloth AI",
         "resource": "https://unsloth.ai/", "body": "Ships training kernels for open-weight models."},
        {"id": "fervo-energy", "type": "Organization", "title": "Fervo Energy",
         "resource": "https://fervoenergy.com/", "body": "Enhanced geothermal developer."},
        {"id": "rainmaker", "type": "Organization", "title": "Rainmaker Technology",
         "resource": "https://makerain.com/", "body": "Cloud seeding and weather modification."},
        {"id": "spacex", "type": "Organization", "title": "SpaceX",
         "description": "Elon Musk's launch and satellite company, operator of Starlink; in this corpus the vehicle for orbit becoming a compute layer, and xAI's acquirer.",
         "resource": "https://www.spacex.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q193701"],
         "tags": ["big-tech"],
         "body": "Operates Starlink. It enters the corpus with Musk's plan to "
                 "[scale Starlink satellites past 100 kW for AI compute](/developments/2025-12-11-starlink-100kw-compute.md), "
                 "followed two days later by [10,000 satellites by February](/developments/2025-12-13-starlink-10000-satellites.md); "
                 "it later [files for a million satellites](/developments/2026-02-02-spacex-files-for-a-million-satellites.md) "
                 "and [acquires xAI](/developments/2026-02-03-spacex-acquires-xai.md), which is how it enters the "
                 "recursive-self-improvement strand: as parent of the lab whose Grok is reported "
                 "[improving every few days](/developments/2026-05-17-models-improve-every-few-days.md)."},
        {"id": "blue-origin", "type": "Organization", "title": "Blue Origin",
         "resource": "https://www.blueorigin.com/", "body": "Launch and orbital infrastructure."},
        {"id": "starcloud", "type": "Organization", "title": "Starcloud",
         "resource": "https://www.starcloud.com/", "body": "Orbital datacenter startup."},
        {"id": "starlab", "type": "Organization", "title": "Starlab Space",
         "resource": "https://starlab.space/", "body": "Commercial space station developer."},
        {"id": "project-ceti", "type": "Organization", "title": "Project CETI",
         "resource": "https://www.projectceti.org/", "body": "Applies machine learning to sperm whale communication."},
        {"id": "cdc", "type": "Organization", "title": "CDC",
         "resource": "https://www.cdc.gov/", "body": "US Centers for Disease Control and Prevention."},
        {"id": "fda", "type": "Organization", "title": "FDA",
         "resource": "https://www.fda.gov/", "body": "US Food and Drug Administration."},
        {"id": "amazon", "type": "Organization", "title": "Amazon",
         "resource": "https://www.amazon.com/", "body": "Cloud and AI capital deployment."},
        {"id": "polymarket", "type": "Organization", "title": "Polymarket",
         "resource": "https://polymarket.com/", "body": "Prediction market."},
        {"id": "ornn", "type": "Organization", "title": "Ornn",
         "body": "Compute-trading venue. The author discloses an indirect interest."},
        {"id": "us-congress", "type": "Organization", "title": "US Congress",
         "resource": "https://www.congress.gov/", "body": "Source of the NDAA provision."},
    ],

    "systems": [
        {"id": "gemini-tts", "type": "AISystem", "title": "Gemini Text-to-Speech",
         "developed_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/google"], "modality": "speech",
         "body": "Gemini's speech synthesis, upgraded for context-aware pacing and "
                 "consistency across multiple speakers."},
        {"id": "grok", "type": "AISystem", "title": "Grok",
         "description": "xAI's frontier model and chatbot, which the corpus tracks from chip-design "
                        "work at Tesla to Musk's claim that it could exceed human intelligence in 2026.",
         "developed_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/xai"], "modality": "text",
         "resource": "https://grok.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q123361035"],
         # tags waived: no controlled entity tag (ENRICH_RULES) describes a general-purpose chatbot.
         "body": "Grok is xAI's frontier model and the assistant served at [grok.com](https://grok.com/). "
                 "In this corpus it first appears as a tool Tesla uses to "
                 "[design its own chips](/developments/2025-12-11-tesla-grok-chip-design.md), an early "
                 "case of a model shaping the silicon models run on; a week later Musk told xAI staff it "
                 "[could exceed human intelligence in 2026](/developments/2025-12-18-musk-grok-exceeds-human-2026.md). "
                 "The recursive thread folds back on itself in January, when xAI was reported to have "
                 "[used Claude to build Grok](/developments/2026-01-10-xai-used-claude-to-build-grok.md) "
                 "until Anthropic revoked access."},
        {"id": "chatgpt", "type": "AISystem", "title": "ChatGPT",
         "description": "OpenAI's consumer assistant, the corpus's proxy for how fast chat has displaced "
                        "the GUI as the mass-market interface.",
         "developed_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/openai"], "modality": "text",
         "resource": "https://chatgpt.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q115564437"],
         # tags waived: no controlled entity tag (ENRICH_RULES) describes a general-purpose chatbot.
         "body": "ChatGPT is OpenAI's chat assistant, served at [chatgpt.com](https://chatgpt.com/). "
                 "The corpus reads it as a distribution fact more than a model: it closed 2025 as the "
                 "[most downloaded iOS app](/developments/2025-12-11-chatgpt-most-downloaded-ios.md), "
                 "its release was linked to a "
                 "[6% rise in new business formation](/developments/2025-12-14-chatgpt-business-formation.md), "
                 "and OpenAI opened it to "
                 "[developer-submitted inline apps](/developments/2025-12-18-chatgpt-inline-apps.md), "
                 "turning the chat window into the platform."},
        {"id": "copilot", "type": "AISystem", "title": "Microsoft Copilot",
         "description": "Microsoft's AI assistant, whose own 2025 usage report made health the leading "
                        "mobile topic.",
         "developed_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/microsoft"], "modality": "text",
         "resource": "https://copilot.microsoft.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q116793893"],
         # tags waived: no controlled entity tag (ENRICH_RULES) describes a general-purpose chatbot.
         "body": "Microsoft Copilot is Microsoft's consumer AI assistant "
                 "([copilot.microsoft.com](https://copilot.microsoft.com/)). Its place in this corpus "
                 "is the human-interface thread: Microsoft's usage report found that "
                 "[health questions were the dominant mobile topic in 2025](/developments/2025-12-11-copilot-health-dominant-topic.md), "
                 "which the newsletter read as a chatbot becoming primary care for the masses. It "
                 "reappears in August among the agent products "
                 "[given their own channels in Slack Code](/developments/2026-08-21-trillions-of-tokens-a-week-to-write-its-own-software.md)."},
        {"id": "wham", "type": "AISystem", "title": "WhAM",
         "developed_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/project-ceti"], "modality": "bioacoustics",
         "body": "A model that generates synthetic sperm whale codas."},
        {"id": "digit", "type": "AISystem", "title": "Digit",
         "developed_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/agility-robotics"], "modality": "robotic control",
         "body": "Agility's bipedal humanoid, deployed into fulfillment work."},
        {"id": "gemma", "type": "AISystem", "title": "Gemma",
         "developed_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/google"], "modality": "text",
         "body": "Google's open-weight model family, reported hosted on a satellite."},
        {"id": "shipos", "type": "AISystem", "title": "ShipOS",
         "developed_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/palantir"], "modality": "industrial planning",
         "body": "Palantir's naval production software."},
    ],

    "benchmarks": [
        {"id": "swe-bench-verified", "type": "Benchmark", "title": "SWE-bench Verified",
         "description": "OpenAI's human-validated 500-task subset of SWE-bench, the corpus's reference "
                        "yardstick for agentic software engineering and the saturation clock the "
                        "newsletter watches.",
         "published_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/openai"],
         "measures_capability": "resolving real GitHub issues in software repositories",
         "resource": "https://openai.com/index/introducing-swe-bench-verified/",
         "tags": ["coding-agent"],
         "body": "SWE-bench Verified is the human-validated subset of SWE-bench that OpenAI released "
                 "in 2024 so that scores reflect solvable, unambiguous GitHub issues "
                 "([announcement](https://openai.com/index/introducing-swe-bench-verified/)). "
                 "The corpus uses it as a clock: the first issue reported Anthropic's models "
                 "[improving about 2% a month](/developments/2025-12-11-anthropic-swebench-trajectory.md) "
                 "toward saturation by late 2026, and Epoch AI later found "
                 "[15% of the score available from prompt restructuring alone](/developments/2025-12-28-epoch-15pct-from-prompting.md). "
                 "Its harder sibling is [SWE-Bench Pro](/benchmarks/swe-bench-pro.md), where "
                 "[a self-play bug-repair agent](/developments/2025-12-25-meta-self-play-bug-repair.md) "
                 "and later frontier models are scored."},
        {"id": "facts-benchmark", "type": "Benchmark", "title": "FACTS Benchmark",
         "published_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/google-deepmind"],
         "measures_capability": "factual grounding and verifiability of model outputs",
         "body": "DeepMind's benchmark for checking what models actually know."},
    ],

    "facilities": [
        {"id": "memphis-gigawatt-datacenter", "type": "Facility",
         "title": "Memphis gigawatt datacenter",
         "operated_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/xai", "https://nicholsn.github.io/innermost-loop-kb/organizations/supermicro"],
         "located_in": "Memphis, Tennessee, USA", "capacity": "1 GW",
         "body": "Described as the world's first gigawatt-scale datacenter."},
        {"id": "uk-materials-discovery-lab", "type": "Facility",
         "title": "UK automated materials discovery lab",
         "operated_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/google-deepmind"],
         "located_in": "United Kingdom",
         "body": "A self-driving lab targeting superconductors, solar cells and semiconductors."},
        {"id": "robotgym-shanghai", "type": "Facility", "title": "RobotGym (Shanghai)",
         "located_in": "Shanghai, China",
         "body": "Humanoid training facility placing robots into nursing homes."},
        {"id": "starlab-habitat", "type": "Facility", "title": "Starlab commercial habitat",
         "operated_by": ["https://nicholsn.github.io/innermost-loop-kb/organizations/starlab"], "located_in": "low Earth orbit",
         "capacity": "1,600 sq ft floor area",
         "body": "A three-story cylindrical commercial station, launch targeted for 2029."},
    ],

    "developments": [
        {"id": "2025-12-11-deepmind-coordination-tax",
         "title": "DeepMind measures the multi-agent coordination tax",
         "claim": "DeepMind reports that decentralized multi-agent coordination amplifies "
                  "errors 17.2x, falling to 4.4x under centralized command.",
         "domain": "agents", "actor": ["google-deepmind"],
         "evidences": ["coordination-tax"],
         "body": "The issue's framing result, and the source of its thesis: adding agents "
                 "has diminishing returns, and the measured remedy is hierarchy rather "
                 "than more peers."},
        {"id": "2025-12-11-anthropic-swebench-trajectory",
         "title": "Anthropic models improving ~2% per month on SWE-bench Verified",
         "claim": "Anthropic's models are reported improving about 2% per month on "
                  "SWE-bench Verified, on track to saturate it by late 2026.",
         "domain": "benchmarks", "actor": ["anthropic"],
         "about": ["https://nicholsn.github.io/innermost-loop-kb/benchmarks/swe-bench-verified"],
         "body": "A rate, not a score — the newsletter's habit of tracking slopes and "
                 "projected saturation dates rather than leaderboard positions."},
        {"id": "2025-12-11-facts-benchmark-launch",
         "title": "DeepMind launches the FACTS Benchmark",
         "claim": "DeepMind released the FACTS Benchmark to evaluate what models factually know.",
         "domain": "benchmarks", "actor": ["google-deepmind"],
         "about": ["https://nicholsn.github.io/innermost-loop-kb/benchmarks/facts-benchmark"],
         "body": "Verification capacity offered as the counterweight to capability."},
        {"id": "2025-12-11-gemini-tts-upgrade",
         "title": "Gemini text-to-speech gains context-aware pacing",
         "claim": "Google upgraded Gemini's text-to-speech for context-aware pacing and "
                  "multi-speaker consistency.",
         "domain": "models", "actor": ["google"], "about": ["https://nicholsn.github.io/innermost-loop-kb/systems/gemini-tts"],
         "evidences": ["intimate-interface"]},
        {"id": "2025-12-11-deepmind-uk-materials-lab",
         "title": "DeepMind sets up an automated materials discovery lab in the UK",
         "claim": "Google DeepMind is establishing a UK lab to automate the search for "
                  "superconductors, solar cells and semiconductors.",
         "domain": "science", "actor": ["google-deepmind"],
         "about": ["https://nicholsn.github.io/innermost-loop-kb/facilities/uk-materials-discovery-lab"],
         "evidences": ["automated-science"]},
        {"id": "2025-12-11-polymathic-physics-models",
         "title": "Polymathic AI releases models trained on physics data",
         "claim": "Polymathic AI released models trained on physics datasets rather than "
                  "text, aimed at astronomy and fluid dynamics.",
         "domain": "science", "actor": ["polymathic-ai"], "evidences": ["automated-science"],
         "body": "Foundation models whose pretraining corpus is measurement rather than prose."},
        {"id": "2025-12-11-copilot-health-dominant-topic",
         "title": "Health was Copilot's dominant mobile topic in 2025",
         "claim": "Microsoft reports health questions were the leading mobile Copilot topic in 2025.",
         "domain": "society", "actor": ["microsoft"], "about": ["https://nicholsn.github.io/innermost-loop-kb/systems/copilot"],
         "evidences": ["intimate-interface"]},
        {"id": "2025-12-11-chatgpt-most-downloaded-ios",
         "title": "ChatGPT closes 2025 as the most downloaded iOS app",
         "claim": "ChatGPT ended 2025 as the most downloaded application on iOS.",
         "domain": "society", "actor": ["openai"], "about": ["https://nicholsn.github.io/innermost-loop-kb/systems/chatgpt"],
         "evidences": ["intimate-interface"],
         "body": "Offered as evidence of the shift from GUI to chat as the default surface."},
        {"id": "2025-12-11-palantir-shipos-navy",
         "title": "Palantir's ShipOS compresses a 200-hour Navy process to 12 seconds",
         "claim": "Palantir reports ShipOS reduced a 200-hour naval production process to 12 seconds.",
         "domain": "policy", "actor": ["palantir"], "about": ["https://nicholsn.github.io/innermost-loop-kb/systems/shipos"]},
        {"id": "2025-12-11-mercado-libre-digit",
         "title": "Mercado Libre deploys Agility's Digit humanoids",
         "claim": "Mercado Libre is deploying Agility Robotics' Digit humanoids in "
                  "e-commerce fulfillment centers.",
         "domain": "robotics", "actor": ["mercado-libre", "agility-robotics"],
         "about": ["https://nicholsn.github.io/innermost-loop-kb/systems/digit"]},
        {"id": "2025-12-11-robotgym-nursing-homes",
         "title": "Shanghai's RobotGym sends humanoids into nursing homes",
         "claim": "Shanghai's RobotGym is placing humanoid robots into nursing homes.",
         "domain": "robotics", "about": ["https://nicholsn.github.io/innermost-loop-kb/facilities/robotgym-shanghai"]},
        {"id": "2025-12-11-oracle-backlog",
         "title": "Oracle's backlog rises 438% to $523 billion",
         "claim": "Oracle reported its backlog grew 438% to $523 billion on datacenter demand.",
         "domain": "economics", "actor": ["oracle"], "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-11-memphis-gigawatt-datacenter",
         "title": "Supermicro and xAI build the first gigawatt datacenter",
         "claim": "Supermicro and xAI are constructing what is described as the world's first "
                  "gigawatt datacenter, in Memphis.",
         "domain": "compute", "actor": ["supermicro", "xai"],
         "about": ["https://nicholsn.github.io/innermost-loop-kb/facilities/memphis-gigawatt-datacenter"],
         "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-11-memory-half-b200-cost",
         "title": "Memory is nearly half the manufacturing cost of a B200",
         "claim": "Epoch AI estimates memory accounts for nearly half the manufacturing cost "
                  "of an NVIDIA B200 GPU, reducing the logic die to a minor line item.",
         "domain": "compute", "actor": ["epoch-ai", "nvidia"],
         "evidences": ["compute-capital-stack"],
         "body": "A cost-structure inversion: the accelerator's value migrates from logic to memory."},
        {"id": "2025-12-11-tesla-grok-chip-design",
         "title": "Tesla uses Grok to design its chips",
         "claim": "Elon Musk confirmed Tesla is using Grok in the design of its own chips.",
         "domain": "compute", "actor": ["tesla", "xai"], "about": ["https://nicholsn.github.io/innermost-loop-kb/systems/grok"],
         "body": "An early instance of models designing the silicon that will run models."},
        {"id": "2025-12-11-unsloth-faster-kernels",
         "title": "Unsloth releases kernels training open-weight models 3-5x faster",
         "claim": "Unsloth AI released kernels reported to train open-weight models 3-5x faster.",
         "domain": "compute", "actor": ["unsloth-ai"]},
        {"id": "2025-12-11-fervo-462m-geothermal",
         "title": "Fervo raises $462M to scale geothermal for AI power",
         "claim": "Fervo Energy raised $462 million to scale geothermal generation for AI power demand.",
         "domain": "energy", "actor": ["fervo-energy"],
         "evidences": ["industrialized-nature", "compute-capital-stack"]},
        {"id": "2025-12-11-rainmaker-weather-modification",
         "title": "Rainmaker promises weather modification in the American West",
         "claim": "Rainmaker Technology is promising weather modification to deliver "
                  "year-round skiing and swimmable lakes in the American West.",
         "domain": "energy", "actor": ["rainmaker"], "evidences": ["industrialized-nature"]},
        {"id": "2025-12-11-starlink-100kw-compute",
         "title": "Starlink satellites to scale beyond 100 kW for AI compute",
         "claim": "Elon Musk said Starlink satellites will scale to more than 100 kW to focus "
                  "on AI compute.",
         "domain": "space", "actor": ["spacex"], "evidences": ["orbit-as-compute"]},
        {"id": "2025-12-11-blue-origin-space-datacenters",
         "title": "Blue Origin forms a space-based datacenter team",
         "claim": "Blue Origin now has a dedicated team working on space-based datacenters.",
         "domain": "space", "actor": ["blue-origin"], "evidences": ["orbit-as-compute"]},
        {"id": "2025-12-11-starcloud-orbital-training-run",
         "title": "Starcloud runs the first LLM training run in orbit",
         "claim": "Starcloud conducted the first training run of a large language model in "
                  "orbit and hosted Google's Gemma on a satellite.",
         "domain": "space", "actor": ["starcloud"], "about": ["https://nicholsn.github.io/innermost-loop-kb/systems/gemma"],
         "evidences": ["orbit-as-compute"],
         "body": "The point at which orbit stops being a relay and becomes a compute site."},
        {"id": "2025-12-11-starlab-habitat-tour",
         "title": "Starlab details its 2029 commercial habitat",
         "claim": "Starlab detailed a three-story cylindrical commercial habitat with 1,600 "
                  "square feet of floor area, launching in 2029.",
         "domain": "space", "actor": ["starlab"], "about": ["https://nicholsn.github.io/innermost-loop-kb/facilities/starlab-habitat"],
         "evidences": ["orbit-as-compute"]},
        {"id": "2025-12-11-project-ceti-wham",
         "title": "Project CETI releases WhAM, generating synthetic whale codas",
         "claim": "Project CETI released WhAM, a model generating synthetic sperm whale codas.",
         "domain": "biotech", "actor": ["project-ceti"], "about": ["https://nicholsn.github.io/innermost-loop-kb/systems/wham"],
         "evidences": ["biosphere-uplift"],
         "body": "Generation, not just classification — the step from listening to speaking."},
        {"id": "2025-12-11-cdc-organ-chips",
         "title": "CDC ends monkey research in favor of organ chips",
         "claim": "The CDC is ending monkey research to pivot to organ-on-a-chip models.",
         "domain": "biotech", "actor": ["cdc"], "evidences": ["biosphere-uplift"]},
        {"id": "2025-12-11-fda-nonprofit-gene-therapy",
         "title": "FDA approves the first nonprofit gene therapy",
         "claim": "The FDA approved the first nonprofit gene therapy for a rare genetic disease.",
         "domain": "biotech", "actor": ["fda"],
         "body": "Decoupling a life-saving treatment from the profit motive."},
        {"id": "2025-12-11-polymarket-trillionaire-odds",
         "title": "Polymarket prices Musk at 32% to be a trillionaire by end of 2026",
         "claim": "Polymarket gave Elon Musk a 32% chance of becoming a trillionaire by the "
                  "end of 2026.",
         "domain": "economics", "actor": ["polymarket"], "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-11-amazon-india-35b",
         "title": "Amazon commits $35 billion to AI in India",
         "claim": "Amazon is investing $35 billion in AI in India.",
         "domain": "economics", "actor": ["amazon"], "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-11-ndaa-agi-panel",
         "title": "House NDAA mandates a Pentagon panel on AGI",
         "claim": "The House NDAA mandates a Pentagon panel to study the military implications "
                  "of artificial general intelligence.",
         "domain": "policy", "actor": ["us-congress"]},
        {"id": "2025-12-11-ornn-first-gpu-compute-swap",
         "title": "Ornn executes the first GPU compute swap",
         "claim": "Ornn reported executing the first GPU compute swap, making teraflops a "
                  "tradeable commodity.",
         "domain": "economics", "actor": ["ornn"], "evidences": ["compute-capital-stack"],
         "body": "Compute becomes a financial instrument rather than only an input. "
                 "The author discloses an indirect interest in Ornn."},
    ],
}
