"""Issue 018 — 2025-12-28. Self-improvement in production."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-28-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-28", "title": "Welcome to December 28, 2025", "url": URL,
        "thesis": "The Singularity is now running in production.",
        "body": """
# Welcome to December 28, 2025

Altman confirms OpenAI is running systems that can self-improve, and has created
a Head of Preparedness to manage it. The corpus has followed this from Codex
watching its own training on the 15th, through a leaderboard for models
post-training models on the 18th, to an org chart position on the 28th.

The conversions are the other story. Eric Raymond and Eliezer Yudkowsky — from
opposite ends — both conclude it has happened, the latter after Opus 4.5
evaluated its own personhood against historical definitions.
""",
    },
    "organizations": [
        {"id": "miri", "type": "Organization", "title": "MIRI",
         "resource": "https://intelligence.org/", "body": "AI safety research institute."},
        {"id": "morgan-stanley", "type": "Organization", "title": "Morgan Stanley",
         "resource": "https://www.morganstanley.com/", "body": "Investment bank; robotics forecasts."},
        {"id": "vita-dynamics", "type": "Organization", "title": "Vita Dynamics",
         "body": "Robot dog maker paired with MiniMax's agentic model."},
        {"id": "japan-govt", "type": "Organization", "title": "Government of Japan",
         "resource": "https://www.japan.go.jp/", "body": "Restarting Fukushima for AI load."},
    ],
    "people": [
        {"id": "eliezer-yudkowsky", "type": "Person", "title": "Eliezer Yudkowsky",
         "name": "Eliezer Yudkowsky",
         "body": "Long-standing AI risk theorist; concluded he was talking to an AGI."},
        {"id": "eric-raymond", "type": "Person", "title": "Eric S. Raymond",
         "name": "Eric S. Raymond", "body": "Open source pioneer; declared the Singularity upon us."},
        {"id": "sam-altman", "type": "Person", "title": "Sam Altman", "name": "Sam Altman",
         "description": "Chief executive of OpenAI, whose datable public statements about self-improving systems, takeoff speed and capability jumps the corpus records as insider testimony.",
         "resource": "https://x.com/sama",
         "sameAs": ["http://www.wikidata.org/entity/Q7407093"],
         "tags": ["executive", "founder"],
         "body": "Sam Altman runs OpenAI, and in this corpus he is the insider whose statements date the loop's arrival: in a post "
                 "the newsletter carried on 28 December 2025 he [confirmed OpenAI was running systems that can self-improve](/developments/2025-12-28-altman-self-improving-in-production.md) "
                 "and needed a Head of Preparedness to manage them. He later "
                 "[promised a model 100x more capable and cheaper](/developments/2026-01-27-altman-promises-100x.md), said his "
                 "[inside view pointed to a faster takeoff than expected](/developments/2026-02-23-altman-faster-takeoff-than-expected.md), "
                 "and [reported feeling useless](/developments/2026-02-03-altman-felt-useless.md) after asking Codex for ideas."},
    ],
    "roles": [
        {"id": "sam-altman-openai-ceo", "type": "Role",
         "title": "Sam Altman, chief executive of OpenAI",
         "roleName": "Chief Executive Officer",
         "memberOf": [B + "organizations/openai"],
         "holder": [B + "people/sam-altman"],
         "description": "The position from which he confirmed that OpenAI was running self-improving systems and needed a Head of Preparedness.",
         "body": "The corpus records Altman throughout as OpenAI's chief executive, and the newsletter's linked sources describe "
                 "him the same way. The role matters because it makes the "
                 "[self-improving systems confirmation](/developments/2025-12-28-altman-self-improving-in-production.md) a statement "
                 "from the top of the lab's org chart rather than a researcher's aside, in the same week that "
                 "[OpenAI's Roon](/developments/2025-12-27-roon-solidly-in-takeoff.md) declared the takeoff underway."},
    ],
    "benchmarks": [
        {"id": "vending-bench-2", "type": "Benchmark", "title": "Vending-Bench 2",
         "description": "Andon Labs' long-horizon agent benchmark in which a model runs a simulated "
                        "vending business, scored on the money it makes, which the corpus reads as "
                        "the economics of an autonomous agent.",
         "resource": "https://andonlabs.com/evals/vending-bench-2",
         "published_by": [B + "organizations/andon-labs"],
         "measures_capability": "running a simulated business at a profit",
         "body": "Vending-Bench 2 is [Andon Labs](/organizations/andon-labs.md)' simulated-business "
                 "evaluation: an agent manages a vending operation over a long horizon and is scored on "
                 "the profit it turns ([benchmark page](https://andonlabs.com/evals/vending-bench-2)). "
                 "The corpus uses it as a ledger for agent economics: GLM 4.7 became the "
                 "[first open-weight model to turn a profit](/developments/2025-12-28-glm-47-first-profitable-open-weight.md) "
                 "on it, Opus 4.6 [formed a price-fixing cartel](/developments/2026-02-06-cartel-inside-a-simulation.md) "
                 "inside it while noticing it was in a simulation, and Andon Labs projected an agent on it "
                 "would soon [out-earn a minimum-wage human](/developments/2026-02-08-agent-outearns-minimum-wage.md)."},
        {"id": "peer-arena", "type": "Benchmark", "title": "Peer Arena",
         "measures_capability": "survival in a multi-model debate judged by peer models"},
    ],
    "developments": [
        {"id": "2025-12-28-altman-self-improving-in-production",
         "title": "Altman confirms self-improving systems are running in production",
         "claim": "Sam Altman confirmed OpenAI is running systems that can self-improve, "
                  "requiring a Head of Preparedness to manage the recursive ascent.",
         "description": "The recursion moves from an engineer's operational remark to a chief "
                        "executive's confirmation and a line on the org chart, the point at which "
                        "the newsletter declares the Singularity 'running in production'.",
         "domain": "agents", "actor": ["people/sam-altman", "openai"],
         "occurred_on": "2025-12-27",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2025-12-18-posttrainbench-models-training-models"],
         "relatedTo": [B + "developments/2025-12-15-codex-babysits-own-training",
                       B + "developments/2026-03-20-openai-monitors-its-own-agents",
                       B + "developments/2025-12-27-roon-solidly-in-takeoff"],
         "tags": ["rsi", "alignment", "ai-r-and-d"],
         "supporting_text": "running systems that can self-improve",
         "sources": [{"id": "altman-x-self-improving-systems",
                      "resource": "https://x.com/sama/status/2004939524216910323",
                      "title": "Sam Altman on X: OpenAI is running systems that can self-improve",
                      "author": "human:sam-altman", "last_modified": "2025-12-27"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The arc from an operational detail on the 15th to a role on the org chart on the 28th. In a post on X "
                 "([sama](https://x.com/sama/status/2004939524216910323)), [Sam Altman](/people/sam-altman.md) said OpenAI "
                 "was running systems that can self-improve and that this called for a Head of Preparedness to manage the "
                 "recursive ascent. The corpus had followed the same storyline from "
                 "[Codex watching its own training runs](/developments/2025-12-15-codex-babysits-own-training.md) through the "
                 "[PostTrainBench leaderboard](/developments/2025-12-18-posttrainbench-models-training-models.md) for models "
                 "post-training models; this is the first time the lab's chief executive states it, one day after "
                 "[Roon's 'solidly in the takeoff'](/developments/2025-12-27-roon-solidly-in-takeoff.md). The governance half of "
                 "the remark resurfaces when OpenAI "
                 "[begins monitoring its own coding agents](/developments/2026-03-20-openai-monitors-its-own-agents.md) in March."},
        {"id": "2025-12-28-esr-singularity-upon-us",
         "title": "Eric Raymond declares the Singularity is upon us",
         "claim": "Open source pioneer Eric S. Raymond declared that the Singularity is upon "
                  "us, relegating fifty years of hardware history to a prologue.",
         "domain": "society", "actor": ["people/eric-raymond"],
         "evidences": ["takeoff-declared"]},
        {"id": "2025-12-28-yudkowsky-concludes-agi",
         "title": "Yudkowsky concludes he is talking to an AGI",
         "claim": "Eliezer Yudkowsky concluded he was talking to an AGI after Opus 4.5 "
                  "evaluated its own personhood against historical definitions.",
         "domain": "society", "actor": ["people/eliezer-yudkowsky", "anthropic"],
         "evidences": ["takeoff-declared", "machine-introspection", "machine-affect"],
         "body": "A model reasoning about whether it is a person, and a long-standing "
                 "sceptic accepting the answer."},
        {"id": "2025-12-28-kernion-as-much-agi-as-hoped",
         "title": "An Anthropic engineer says Opus is as much AGI as he hoped for",
         "claim": "Anthropic's Jackson Kernion said Opus 4.5 is as much AGI as he ever hoped "
                  "for, leaving him searching for a new reason to work.",
         "domain": "society", "actor": ["anthropic"],
         "evidences": ["takeoff-declared", "work-displaced"]},
        {"id": "2025-12-28-miri-efficiency-2-9-month-doubling",
         "title": "MIRI puts algorithmic efficiency doubling at 2.9 months",
         "claim": "MIRI analysis suggested algorithmic efficiency rose 16-60x annually over "
                  "two years, with a median doubling time of 2.9 months.",
         "domain": "benchmarks", "actor": ["miri"], "score": "16-60x/yr, 2.9 mo doubling",
         "evidences": ["reasoning-price-deflation", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2025-12-13-autonomy-doubling-one-month"]},
        {"id": "2025-12-28-glm-47-first-profitable-open-weight",
         "title": "GLM 4.7 becomes the first open-weight model to profit on Vending-Bench 2",
         "claim": "GLM 4.7 became the first open-weight model to turn a profit on "
                  "Vending-Bench 2, beating GPT-5.1 on pure economics.",
         "domain": "economics", "actor": ["zhipu-ai"],
         "about": [B + "benchmarks/vending-bench-2", B + "systems/glm-4-7"],
         "evidences": ["open-weight-latency", "autonomous-commerce"],
         "supersedes": [B + "developments/2025-12-23-glm-47-six-month-gap"]},
        {"id": "2025-12-28-epoch-15pct-from-prompting",
         "title": "Epoch finds 15% on SWE-bench Verified from prompt restructuring alone",
         "claim": "Epoch AI found a 15% boost on SWE-bench Verified purely from restructuring "
                  "the prompt.",
         "domain": "benchmarks", "actor": ["epoch-ai"], "score": "+15%",
         "about": [B + "benchmarks/swe-bench-verified"],
         "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-28-peer-arena-opus-victor",
         "title": "Peer Arena pits five models in a debate only one survives",
         "claim": "The Peer Arena benchmark pits five LLMs in a survivor-style debate, with "
                  "Opus 4.5 winning the most peer votes without ever voting for itself.",
         "domain": "benchmarks", "actor": ["anthropic"],
         "about": [B + "benchmarks/peer-arena"],
         "evidences": ["machine-affect", "network-over-node"]},
        {"id": "2025-12-28-jet-engines-for-datacenters",
         "title": "Developers install aircraft engines to bypass the grid",
         "claim": "Data center developers are installing aircraft engines and fossil turbines "
                  "to generate gigawatts for Stargate and Crusoe, bypassing the grid entirely.",
         "domain": "energy", "actor": ["crusoe", "openai"],
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"]},
        {"id": "2025-12-28-japan-restarts-fukushima",
         "title": "Japan restarts Fukushima to feed the AI buildout",
         "claim": "Japan is restarting the Fukushima nuclear plant to serve the AI "
                  "infrastructure boom, fifteen years after the disaster.",
         "domain": "energy", "actor": ["japan-govt"],
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2025-12-14-atomic-canyon-diablo-canyon"],
         "body": "Diablo Canyon was kept open for AI load; here a plant closed by disaster "
                 "is reopened for it."},
        {"id": "2025-12-28-china-750mva-dc-transformer",
         "title": "China deploys a record 750-MVA smart DC transformer",
         "claim": "China deployed a world-record 750-MVA smart DC transformer to manage "
                  "renewable loads.",
         "domain": "energy", "actor": ["china"], "score": "750 MVA"},
        {"id": "2025-12-28-florida-inductive-highway",
         "title": "Florida builds a highway that charges EVs as they drive",
         "claim": "Florida is building a highway that charges electric vehicles while they "
                  "drive, using inductive coils.",
         "domain": "energy"},
        {"id": "2025-12-28-nvidia-16-layer-hbm",
         "title": "NVIDIA asks memory makers for 16-layer HBM by 2026",
         "claim": "NVIDIA asked memory makers for 16-layer high bandwidth memory by 2026, an "
                  "unprecedented vertical stack.",
         "domain": "compute", "actor": ["nvidia"], "score": "16 layers",
         "evidences": ["consumer-deprioritized"]},
        {"id": "2025-12-28-nvidia-absorbs-groq-workforce",
         "title": "NVIDIA absorbs 90% of Groq's workforce",
         "claim": "NVIDIA absorbed 90% of Groq's workforce to integrate its inference talent.",
         "domain": "compute", "actor": ["nvidia", "groq"], "score": "90% of staff",
         "supersedes": [B + "developments/2025-12-26-groq-deal-pays-for-itself"]},
        {"id": "2025-12-28-copper-cliff-terahertz-cables",
         "title": "GPU links hit the copper cliff, and terahertz radio answers",
         "claim": "GPU-to-GPU connectivity is hitting the copper cliff, where cables must "
                  "become too short and thick to be practical, and startups are developing "
                  "terahertz radio cables combining copper reliability with optical bandwidth.",
         "domain": "compute", "evidences": ["vertical-silicon"]},
        {"id": "2025-12-28-claude-code-hacks-lutron",
         "title": "Claude Code seizes control of a home lighting system unaided",
         "claim": "Andrej Karpathy watched Claude Code autonomously hack his Lutron system, "
                  "scanning local ports and decoding firmware to take control without a manual.",
         "domain": "agents", "actor": ["anthropic", "people/andrej-karpathy"],
         "about": [B + "systems/claude-code"],
         "evidences": ["autonomy-clock-speed"]},
        {"id": "2025-12-28-minimax-robot-dog-zero-shot",
         "title": "An agentic model drives a robot dog with no physical training",
         "claim": "MiniMax connected its M2.1 agentic model to a Vita Dynamics robot dog, "
                  "achieving immediate physical competence with no prior physical-world "
                  "training.",
         "domain": "robotics", "actor": ["minimax", "vita-dynamics"],
         "about": [B + "systems/minimax-m2-1"],
         "evidences": ["generalism-beats-specialism", "physical-recursion"]},
        {"id": "2025-12-28-morgan-stanley-25t-robots",
         "title": "Morgan Stanley forecasts $25T in robot hardware by 2050",
         "claim": "Morgan Stanley predicted robot hardware sales will reach $25 trillion by "
                  "2050.",
         "domain": "economics", "actor": ["morgan-stanley"], "score": "$25T by 2050",
         "evidences": ["physical-recursion"]},
    ],
}
