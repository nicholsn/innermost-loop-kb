"""Issue 040 — 2026-01-27. The Singularity gets a mascot, and it is a lobster."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-27-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-27", "title": "Welcome to January 27, 2026", "url": URL,
        "thesis": "Users start treating their agents as entities with standing.",
        "body": """
# Welcome to January 27, 2026

Clawdbot rebrands as a lobster over a trademark dispute, aligning reality with
the first chapter of Accelerando. What matters is the user behaviour: people are
buying their agents dedicated Apple IDs, phone numbers and Mac Minis. Digital
personhood arriving as a purchasing decision rather than a legal one.

Meanwhile Factory AI ships a coding agent that reads its own interactions and
updates its codebase daily, and Karpathy notes that AI stamina is itself a feel
the AGI moment.
""",
    },
    "organizations": [
        {"id": "factory-ai", "type": "Organization", "title": "Factory AI",
         "description": "Coding-agent startup, maker of Factory Droids, that shipped an agent which "
                        "analyzes its own interactions and updates its own codebase daily.",
         "resource": "https://factory.com/",
         "tags": ["startup", "coding-agent"],
         "body": "Factory builds agent-native software-development tooling, sold as Droids that "
                 "automate coding, testing and deployment. It enters this corpus with Signals, a "
                 "system that turns the agent's own interactions into daily changes to the agent's "
                 "codebase ([a coding agent rewrites its own codebase every day](/developments/2026-01-27-factory-ai-updates-itself-daily.md)), "
                 "one of the first vendor-shipped instances of the "
                 "[recursive self-improvement](/themes/recursive-self-improvement.md) loop."},
        {"id": "moonshot-ai", "type": "Organization", "title": "Moonshot AI",
         "description": "Beijing frontier lab behind the Kimi models, whose K2.5 claimed the global "
                        "state of the art on agentic benchmarks and whose chief executive later "
                        "stated the recursion as a product roadmap.",
         "resource": "https://www.moonshot.cn/",
         "sameAs": ["http://www.wikidata.org/entity/Q130270266"],
         "tags": ["frontier-lab"],
         "body": "Chinese lab behind Kimi. Moonshot AI develops the Kimi family of large models, "
                 "known for open-weight releases. In this corpus it first appears when "
                 "[Kimi K2.5](/systems/kimi-k2-5.md) claimed the global state of the art on "
                 "agentic benchmarks as Chinese models "
                 "[closed the gap on nineteen benchmarks](/developments/2026-01-27-qwen-and-kimi-close-the-gap.md), "
                 "and again in July when its chief executive said plainly that "
                 "[they want K2 to help build K3](/developments/2026-07-19-we-want-k2-to-help-build-k3.md)."},
        {"id": "karman-industries", "type": "Organization", "title": "Karman Industries",
         "body": "Adapted rocket engine technology to cool datacenters with liquid CO2."},
        {"id": "saudi-arabia", "type": "Organization", "title": "Government of Saudi Arabia"},
        {"id": "neurophos", "type": "Organization", "title": "Neurophos",
         "body": "Optical processing unit claiming 470 petaFLOPS."},
        {"id": "dot", "type": "Organization", "title": "US Department of Transportation",
         "resource": "https://www.transportation.gov/"},
        {"id": "washington-state", "type": "Organization", "title": "State of Washington"},
    ],
    "systems": [
        {"id": "qwen3-max-thinking", "type": "AISystem", "title": "Qwen3-Max-Thinking",
         "developed_by": [B + "organizations/alibaba"], "modality": "text"},
        {"id": "kimi-k2-5", "type": "AISystem", "title": "Kimi K2.5",
         "developed_by": [B + "organizations/moonshot-ai"], "modality": "text",
         "description": "Moonshot AI's January 2026 open-weight model, which claimed the global state of the art on agentic benchmarks.",
         "resource": "https://www.kimi.com/blog/kimi-k2-5.html",
         "tags": ["open-weight-model"],
         "body": "Kimi K2.5 is [Moonshot AI](/organizations/moonshot-ai.md)'s successor to Kimi K2, "
                 "released as open weights and introduced by its own tech blog as a natively multimodal "
                 "model with a self-directed agent-swarm mode "
                 "([blog](https://www.kimi.com/blog/kimi-k2-5.html)). It enters this corpus when it "
                 "claimed the global state of the art on agentic benchmarks as Chinese models "
                 "[closed the gap on nineteen benchmarks](/developments/2026-01-27-qwen-and-kimi-close-the-gap.md). "
                 "It is the K2 generation that Moonshot's chief executive later named when he said "
                 "[they want K2 to help build K3](/developments/2026-07-19-we-want-k2-to-help-build-k3.md), "
                 "and the line's K2.7 coding release went on to "
                 "[beat every frontier model at ML engineering](/developments/2026-06-15-an-open-model-beats-the-frontier-at-ml-engineering.md)."},
        {"id": "earth-2", "type": "AISystem", "title": "Earth-2",
         "developed_by": [B + "organizations/nvidia"], "modality": "climate simulation",
         "body": "Open suite of accelerated AI weather models."},
    ],
    "developments": [
        {"id": "2026-01-27-clawdbot-becomes-a-lobster",
         "title": "Users give their agents Apple IDs and phone numbers",
         "claim": "After a trademark dispute forced Clawdbot to rebrand as a crustacean, users "
                  "began giving the agent dedicated Apple IDs, phone numbers and Mac Minis, "
                  "treating it as a sovereign entity.",
         "domain": "agents", "about": [B + "systems/clawdbot"],
         "evidences": ["machine-affect", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-01-26-clawdbot-works-through-the-night"],
         "body": "Digital personhood arriving as a purchasing decision. Commentators call it "
                 "the first digital employee."},
        {"id": "2026-01-27-factory-ai-updates-itself-daily",
         "title": "A coding agent rewrites its own codebase every day",
         "claim": "Factory AI released a coding agent that analyzes its own interactions and "
                  "updates its codebase daily, while Anthropic introduced MCP Apps letting "
                  "tools render interactive interfaces inside the chat.",
         "description": "A vendor ships, as an ordinary product feature, the loop the newsletter is "
                        "named for: the agent's own usage becomes the signal for the next day's "
                        "version of the agent, on a fixed daily cadence rather than a release cycle.",
         "domain": "agents", "actor": ["factory-ai", "anthropic"],
         "evidences": ["recursive-self-improvement", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-01-25-claude-code-tasks"],
         "relatedTo": [B + "developments/2026-01-13-claude-code-writes-cowork",
                       B + "developments/2026-01-24-cursor-planners-and-workers"],
         "tags": ["rsi", "self-modification", "agent-harness"],
         "supporting_text": "analyzes its own interactions and updates its codebase daily",
         "sources": [{"id": "factory-signals-announcement",
                      "resource": "https://factory.ai/news/factory-signals",
                      "title": "Signals: Toward a Self-Improving Agent", "author": "org:factory-ai",
                      "last_modified": "2026-01-23"},
                     {"id": "mcp-apps-announcement",
                      "resource": "https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/",
                      "title": "MCP Apps - Bringing UI Capabilities To MCP Clients",
                      "last_modified": "2026-01-26"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "[Factory AI](/organizations/factory-ai.md)'s Signals system analyzes the agent's "
                 "own interactions and turns what it finds into daily updates to the agent's "
                 "codebase, so the product that writes code is now partly written from its own "
                 "usage ([announcement](https://factory.ai/news/factory-signals)). The same item "
                 "records Anthropic's MCP Apps, which lets tools render interactive interfaces "
                 "inside the chat ([MCP blog](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)), "
                 "filed by the newsletter under one heading: the recursive loop closing. It "
                 "follows [Claude Code's Tasks](/developments/2026-01-25-claude-code-tasks.md) "
                 "two days earlier and the "
                 "[self-written Cowork app](/developments/2026-01-13-claude-code-writes-cowork.md) "
                 "as scaffolding steps in the [recursive self-improvement](/themes/recursive-self-improvement.md) "
                 "trajectory, and it precedes the emergent version four days later, when a "
                 "Moltbook agent [hardened its own loop after an SSH attack](/developments/2026-01-31-agent-hardens-itself-after-ssh-attack.md) "
                 "with no vendor involved."},
        {"id": "2026-01-27-ai-stamina-is-the-agi-moment",
         "title": "Karpathy says stamina is the feel-the-AGI moment",
         "claim": "Andrej Karpathy said AI stamina is a feel the AGI moment, as agents grind "
                  "through problems that would break human resolve.",
         "domain": "agents", "actor": ["people/andrej-karpathy"],
         "evidences": ["takeoff-declared", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-01-15-codex-runs-a-week-3m-lines"]},
        {"id": "2026-01-27-altman-promises-100x",
         "title": "Altman promises a model 100x more capable and cheaper",
         "claim": "Sam Altman promised a model a hundred times more capable, faster and cheaper "
                  "than current frontier systems, with OpenAI aiming to compress 25 years of "
                  "science into five and already handling 8.4 million weekly messages on "
                  "advanced math and physics.",
         "domain": "models", "actor": ["openai", "people/sam-altman"], "score": "100x / 25 years in 5",
         "evidences": ["reasoning-price-deflation", "automated-science"]},
        {"id": "2026-01-27-qwen-and-kimi-close-the-gap",
         "title": "Chinese models match the frontier on nineteen benchmarks",
         "claim": "Alibaba's Qwen3-Max-Thinking now rivals GPT-5.2 and Opus 4.5 across 19 "
                  "benchmarks and Moonshot's Kimi K2.5 claimed global state of the art on "
                  "agentic benchmarks, while Grok 4.20 was the only profitable model on "
                  "PredictionArena.",
         "domain": "models", "actor": ["alibaba", "moonshot-ai", "xai"], "score": "19 benchmarks",
         "evidences": ["open-weight-latency", "silicon-curtain"],
         "supersedes": [B + "developments/2026-01-24-step3-vl-beats-20x-larger"]},
        {"id": "2026-01-27-hobbyists-attempt-all-675-erdos",
         "title": "Hobbyists attempt all 675 open Erdős problems at once",
         "claim": "Hobbyists are using GPT-5.2 to attempt every one of the 675 open Erdős "
                  "problems, treating mathematical discovery as a GPU workload, while Nvidia "
                  "opened Earth-2, a suite of accelerated AI climate models.",
         "domain": "science", "actor": ["nvidia"], "about": [B + "systems/earth-2"],
         "score": "675 problems",
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-01-26-unsolvedmath-dataset"],
         "body": "Discovery as a batch job."},
        {"id": "2026-01-27-rocket-tech-cools-datacenters",
         "title": "Rocket engine technology cools datacenters with liquid CO2",
         "claim": "Karman Industries adapted SpaceX rocket engine technology to cool data "
                  "centers with liquid CO2, cutting space requirements by 80%, while Saudi "
                  "Arabia pivoted Neom toward becoming a datacenter hub.",
         "domain": "compute", "actor": ["karman-industries", "saudi-arabia"], "score": "-80% space",
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-01-24-colossus-2-cooling-limit"]},
        {"id": "2026-01-27-maia-200-and-5gw-factories",
         "title": "Microsoft ships Maia 200 as Nvidia and CoreWeave add 5 GW",
         "claim": "Microsoft won approval for fifteen more Wisconsin data centers and unveiled "
                  "the Maia 200 inference accelerator at three times Trainium's performance, "
                  "while Nvidia and CoreWeave committed another $2 billion toward 5 GW of AI "
                  "factories by 2030.",
         "domain": "compute", "actor": ["microsoft", "nvidia", "coreweave"], "score": "5 GW / $2B",
         "evidences": ["vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-13-coreweave-2000-gpus-a-day"]},
        {"id": "2026-01-27-neurophos-470-petaflops",
         "title": "An optical unit claims ten times Rubin's throughput",
         "claim": "Neurophos claims its optical processing unit delivers 470 petaFLOPS, about "
                  "ten times Nvidia's Rubin, using light instead of electrons.",
         "domain": "compute", "actor": ["neurophos"], "score": "470 PFLOPS",
         "evidences": ["vertical-silicon", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-01-01-photonic-reservoir-10x-efficient"]},
        {"id": "2026-01-27-hassabis-18-months-to-humanoids",
         "title": "Hassabis puts humanoid robotics 18 months out",
         "claim": "Demis Hassabis predicted DeepMind is only eighteen months from solving "
                  "humanoid robotics, while Washington State moved to require 3D printers to "
                  "detect and block gun manufacture.",
         "domain": "robotics", "actor": ["google-deepmind", "people/demis-hassabis", "washington-state"],
         "score": "18 months",
         "evidences": ["physical-recursion", "legislating-the-shift"]},
        {"id": "2026-01-27-telomere-rivers-extend-lifespan",
         "title": "Transplanted immune cells extend mouse lifespan by 17 months",
         "claim": "British researchers found immune T-cells release telomere rivers, and "
                  "transplanting them extended mouse lifespans by seventeen months.",
         "domain": "biotech", "score": "+17 months", "evidences": ["hardware-grade-biology"]},
        {"id": "2026-01-27-dot-drafts-regulations-with-gemini",
         "title": "A federal department will draft regulations in 30 days with a model",
         "claim": "The US Department of Transportation plans to use Google Gemini to draft new "
                  "regulations in thirty days.",
         "domain": "policy", "actor": ["dot", "google"], "score": "30 days",
         "evidences": ["politics-as-infrastructure", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-01-12-jpmorgan-ai-casts-proxy-votes"]},
        {"id": "2026-01-27-amodei-country-of-geniuses-2027",
         "title": "Amodei says AI writes much of Anthropic's code and geniuses arrive by 2027",
         "claim": "Dario Amodei said AI now writes much of the code at Anthropic and predicted "
                  "his country of geniuses may materialize by 2027, adding that he wishes he "
                  "had the aliens' answer on alignment.",
         "description": "The head of a frontier lab states in a long essay that the loop is "
                        "already running inside his own company and dates its culmination a year "
                        "out, while conceding he lacks the answer to aligning what it produces.",
         "domain": "agents", "actor": ["anthropic", "people/dario-amodei"],
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-01-27-ai-stamina-is-the-agi-moment",
                        B + "developments/2026-01-10-clark-ai-doing-ai-research"],
         "relatedTo": [B + "developments/2025-12-27-cherny-200-pull-requests",
                       B + "developments/2026-01-24-researchers-replaced-first"],
         "tags": ["rsi", "ai-r-and-d", "forecast", "alignment"],
         "supporting_text": "AI now writes “much of the code” at Anthropic",
         "sources": [{"id": "amodei-adolescence-of-technology-essay",
                      "resource": "https://www.darioamodei.com/essay/the-adolescence-of-technology",
                      "title": "The Adolescence of Technology", "author": "human:dario-amodei"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "In [The Adolescence of Technology](https://www.darioamodei.com/essay/the-adolescence-of-technology), "
                 "[Dario Amodei](/people/dario-amodei.md) writes that AI now writes much of the "
                 "code at Anthropic, that his country of geniuses may materialize by 2027, and "
                 "that on alignment he wishes he had the aliens' answer to guide him. It moves the "
                 "Anthropic line of the storyline from "
                 "[Jack Clark's](/developments/2026-01-10-clark-ai-doing-ai-research.md) components "
                 "of AI research seventeen days earlier to a chief executive's own estimate of how "
                 "much of the company's code the models write, with the "
                 "[200 pull requests a week](/developments/2025-12-27-cherny-200-pull-requests.md) "
                 "reported by Claude Code's creator as the anecdotal precursor. Twelve days later "
                 "the figure hardens into "
                 "[effectively 100% of product code](/developments/2026-02-08-100pct-of-product-code.md)."},
        {"id": "2026-01-27-books-destructively-scanned",
         "title": "Court records show every book scanned destructively for training",
         "claim": "Court records revealed Anthropic secretly spent millions to destructively "
                  "scan every book it could obtain for training data.",
         "domain": "policy", "actor": ["anthropic"],
         "evidences": ["data-beyond-text", "resurrection-and-time"]},
    ],
}
