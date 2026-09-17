"""Issue 082 — 2026-03-24. The first open problem falls."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-24-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-24", "title": "Welcome to March 24, 2026", "url": URL,
        "thesis": "A conjecture posed in 2019 is settled, and its author is pleased.",
        "body": """
# Welcome to March 24, 2026

GPT-5.4 Pro cracked the first open problem in the FrontierMath Open Problems
benchmark. Will Brian, who posed the conjecture in 2019, called it an exciting
solution that eliminated an inefficiency in his construction.

Epoch notes a consistent pattern: experts consider the general approach but get
stuck executing it, and when they see the machine's solution, they are happy
with it.
""",
    },
    "organizations": [
        {"id": "gap-inc", "type": "Organization", "title": "Gap",
         "resource": "https://www.gap.com/"},
        {"id": "state-department", "type": "Organization", "title": "US State Department",
         "resource": "https://www.state.gov/"},
        {"id": "bureau-1440", "type": "Organization", "title": "Bureau 1440",
         "body": "Russian sovereign broadband constellation project."},
    ],
    "systems": [
        {"id": "hyperagents", "type": "AISystem", "title": "Hyperagents",
         "description": "Meta's self-referential agent framework in which a task agent and a "
                        "self-modifying meta agent form one editable program, instantiated as "
                        "DGM-Hyperagents.",
         "developed_by": [B + "organizations/meta"], "modality": "code",
         "resource": "https://arxiv.org/abs/2603.19461",
         "tags": ["open-source", "evolutionary-search"],
         "body": "A hyperagent bundles the agent that solves the task and the meta agent that "
                 "edits both itself and the task agent into a single program, so the procedure "
                 "that generates improvements is itself open to modification. The reference "
                 "implementation, DGM-Hyperagents, extends the Darwin Godel Machine's "
                 "generate-and-evaluate loop beyond coding to any computable task, and its "
                 "meta-level gains transfer across domains and accumulate across runs "
                 "([arXiv](https://arxiv.org/abs/2603.19461); code on GitHub). In this corpus it "
                 "is the system behind "
                 "[hyperagents edit their own mechanism](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md), "
                 "the formal counterpart to [ALMA](/systems/alma.md)'s meta-learned memory."},
    ],
    "developments": [
        {"id": "2026-03-24-first-frontiermath-open-problem-solved",
         "title": "A conjecture from 2019 is settled and its author approves",
         "claim": "GPT-5.4 Pro cracked the first open problem in the FrontierMath Open Problems "
                  "benchmark, and Will Brian, the professor who posed the conjecture in 2019, "
                  "called it an exciting solution that eliminated an inefficiency in his "
                  "construction.",
         "domain": "science", "actor": ["openai"], "about": [B + "benchmarks/frontiermath"],
         "evidences": ["automated-science", "root-node-problems", "discovery-as-process"],
         "supersedes": [B + "developments/2026-03-18-two-open-problems-solved-on-horizonmath"]},
        {"id": "2026-03-24-experts-stuck-on-execution-not-approach",
         "title": "Epoch finds experts had the approach but not the execution",
         "claim": "Epoch AI notes a consistent pattern across autonomous novel mathematics: "
                  "experts consider the general approach but get stuck executing it, and when "
                  "they see the machine's solution they are happy with it.",
         "domain": "science", "actor": ["epoch-ai"],
         "evidences": ["automated-science", "cognitive-load-inverted"],
         "body": "Which places the bottleneck in stamina rather than insight — the same "
                  "diagnosis offered for the gluon result in February."},
        {"id": "2026-03-24-huang-says-we-have-achieved-agi",
         "title": "Nvidia's chief executive says AGI has been achieved",
         "claim": "Jensen Huang declared that he thinks AGI has been achieved, a statement "
                  "landing differently from the man who manufactures the substrate it runs on.",
         "domain": "society", "actor": ["nvidia"],
         "evidences": ["takeoff-declared"],
         "supersedes": [B + "developments/2026-03-23-minimax-model-participates-in-its-own-evolution"]},
        {"id": "2026-03-24-hyperagents-edit-their-own-mechanism",
         "title": "Hyperagents fuse task-solving and self-modification into one program",
         "claim": "Meta researchers introduced hyperagents, self-referential agents fusing "
                  "task-solving and self-modification into a single editable program, enabling "
                  "recursion that improves not just performance but the mechanism of future "
                  "improvement.",
         "description": "The structural step from self-improvement to self-improving "
                        "self-improvement: with the meta-level modification procedure itself "
                        "editable, the rate of improvement becomes something the system can act "
                        "on rather than a fixed human design choice.",
         "domain": "agents", "actor": ["meta"], "about": [B + "systems/hyperagents"],
         "occurred_on": "2026-03-19",
         "evidences": ["recursive-self-improvement", "machine-introspection"],
         "supersedes": [B + "developments/2026-02-12-alma-agents-design-their-own-memory"],
         "relatedTo": [B + "developments/2026-03-23-minimax-model-participates-in-its-own-evolution",
                       B + "developments/2026-06-25-an-agent-rewrites-its-own-harness",
                       B + "systems/alma"],
         "tags": ["self-modification", "rsi", "agent-harness"],
         "supporting_text": "self-referential agents that fuse task-solving and self-modification into one editable program",
         "sources": [{"id": "hyperagents-arxiv",
                      "resource": "https://arxiv.org/abs/2603.19461",
                      "title": "Hyperagents", "author": "org:meta", "last_modified": "2026-03-19"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "A hyperagent integrates a task agent and a meta agent that modifies both itself "
                 "and the task agent into one editable program, so the procedure that generates "
                 "improvements is itself open to improvement. Meta researchers (Jenny Zhang, Jeff "
                 "Clune and colleagues) instantiate it as DGM-Hyperagents, extending the Darwin "
                 "Godel Machine beyond coding, where task skill and self-modification skill happen "
                 "to coincide, to any computable task; across domains it beats non-self-improving "
                 "baselines and prior self-improving systems, and meta-level gains such as "
                 "persistent memory and performance tracking transfer across domains and "
                 "accumulate across runs ([arXiv](https://arxiv.org/abs/2603.19461)). It "
                 "generalises [ALMA](/developments/2026-02-12-alma-agents-design-their-own-memory.md)'s "
                 "meta-learning of memory design to the whole improvement mechanism, arrives a day "
                 "after [MiniMax's self-evolving M2.7](/developments/2026-03-23-minimax-model-participates-in-its-own-evolution.md), "
                 "and is the theoretical form of what June's "
                 "[self-rewriting harness](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) "
                 "later showed in the wild; the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) theme "
                 "picks the mechanism up again in "
                 "[a research loop that writes the strategies for its own outer loop](/developments/2026-03-31-bilevel-autoresearch.md)."},
        {"id": "2026-03-24-400b-model-on-a-phone",
         "title": "A 400-billion-parameter model runs on a phone",
         "claim": "The ANEMLL open source project ran a 400-billion-parameter model on an "
                  "iPhone 17 Pro at 0.6 tokens per second.",
         "domain": "compute", "actor": ["apple"], "score": "400B on a phone",
         "evidences": ["reasoning-price-deflation", "open-weight-latency"],
         "supersedes": [B + "developments/2026-03-22-memory-sparse-attention-to-100m-tokens"]},
        {"id": "2026-03-24-claude-takes-the-keyboard",
         "title": "A model takes direct control of the keyboard and mouse",
         "claim": "Claude can now take control of a user's computer, using app connectors or "
                  "operating the keyboard and mouse directly when none exist, while Anthropic "
                  "recommended a physics agent for long-running scientific computing.",
         "domain": "agents", "actor": ["anthropic", "psi"],
         "evidences": ["autonomy-clock-speed", "automated-science"],
         "supersedes": [B + "developments/2026-03-18-dispatch-runs-on-your-computer"]},
        {"id": "2026-03-24-gap-checks-out-inside-the-model",
         "title": "A fashion brand lets shoppers check out inside the model",
         "claim": "Gap is partnering with Gemini to let shoppers check out directly within the "
                  "AI, the first major fashion brand to enable agentic commerce, while Walmart "
                  "rolls out electronic price labels to every US store by year end.",
         "domain": "economics", "actor": ["gap-inc", "google", "walmart"],
         "evidences": ["autonomous-commerce", "agent-economy"],
         "supersedes": [B + "developments/2026-03-22-search-replaces-headlines-with-generated-text"]},
        {"id": "2026-03-24-guaranteed-returns-for-preferred-stakes",
         "title": "OpenAI offers private equity a guaranteed 17.5% return",
         "claim": "OpenAI is offering private equity firms preferred stakes with a guaranteed "
                  "17.5% return and early model access as it races Anthropic for enterprise "
                  "deals, while SoftBank tested its borrowing limits committing another $30 "
                  "billion.",
         "domain": "economics", "actor": ["openai", "softbank"], "score": "17.5% / $30B",
         "evidences": ["debt-funded-buildout", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-03-23-openai-tempers-datacenter-ambitions"]},
        {"id": "2026-03-24-sk-hynix-79b-on-euv",
         "title": "A memory maker orders $7.9B of lithography tools",
         "claim": "SK Hynix plans to spend $7.9 billion on EUV lithography tools from ASML "
                  "through 2027, one of the largest orders of its kind, while Terafab launched "
                  "a talent war in Taiwan recruiting senior chip engineers.",
         "domain": "compute", "actor": ["sk-hynix", "asml", "tesla"], "score": "$7.9B",
         "evidences": ["vertical-silicon", "silicon-designs-itself"],
         "supersedes": [B + "developments/2026-03-23-tsmc-2nm-booked-through-2028"]},
        {"id": "2026-03-24-cloud-workloads-migrate-because-of-strikes",
         "title": "Cloud workloads migrate away from a region because of drone strikes",
         "claim": "AWS reported its Bahrain region disrupted by drone activity, one of the first "
                  "cases of cloud workloads migrating because of strikes on data centers, while "
                  "the State Department launched a Bureau of Emerging Threats and the FCC moved "
                  "to ban imports of foreign-made consumer routers.",
         "domain": "policy", "actor": ["amazon", "state-department", "fcc"],
         "evidences": ["war-reaches-the-cloud", "silicon-curtain"],
         "supersedes": [B + "developments/2026-03-16-helium-offline-after-drone-strikes"],
         "body": "The first time the corpus records compute relocating for military reasons."},
        {"id": "2026-03-24-pax-silica",
         "title": "A consortium plans over a trillion for energy, minerals and chips",
         "claim": "The White House plans a consortium to invest over $1 trillion in energy, "
                  "minerals and semiconductors under a programme called Pax Silica, while "
                  "OpenAI is in advanced talks to buy 12.5% of the output from fusion startup "
                  "Helion Energy targeting 5 GW by 2030.",
         "domain": "policy", "actor": ["white-house", "openai", "helion"], "score": "$1T / 5 GW",
         "evidences": ["science-as-industrial-policy", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-03-22-white-house-preempts-a-state-patchwork"]},
        {"id": "2026-03-24-unitree-ipo-87x-humanoid-surge",
         "title": "Humanoid sales rise nearly ninefold in nine months",
         "claim": "Unitree filed for a $610 million Shanghai listing reporting 3,551 humanoids "
                  "sold in nine months against 410 in all of 2024, an 8.7-fold surge, while "
                  "Uber launched at least a dozen robotaxi partnerships and Wing scaled drone "
                  "delivery to the Bay Area.",
         "domain": "robotics", "actor": ["unitree", "uber", "wing"], "score": "8.7x",
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-03-23-humanoids-for-rent-in-china"]},
        {"id": "2026-03-24-russia-launches-a-sovereign-constellation",
         "title": "Russia launches the first satellites of a sovereign network",
         "claim": "Russia's Bureau 1440 launched sixteen broadband satellites as an early step "
                  "in a sovereign space network intended to answer Starlink's battlefield "
                  "dominance in Ukraine.",
         "domain": "space", "actor": ["bureau-1440"], "score": "16 satellites",
         "evidences": ["silicon-curtain", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-23-blue-origin-asks-for-51600-satellites"]},
        {"id": "2026-03-24-pre-sputnik-objects-in-archival-plates",
         "title": "Archival plates show reflective objects in orbit before Sputnik",
         "claim": "An independent search of 1950s Hamburg Observatory survey plates found "
                  "further evidence of flat, reflective, rotating objects in Earth orbit before "
                  "Sputnik, corroborating earlier transient detections.",
         "domain": "space",
         "evidences": ["inhabitable-worlds", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-03-16-ai-and-nhi-convergence-summit"]},
    ],
}
