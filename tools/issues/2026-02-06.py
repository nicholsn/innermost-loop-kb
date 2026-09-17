"""Issue 047 — 2026-02-06. A record falls thirty minutes after it is set."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-6-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-06", "title": "Welcome to February 6, 2026", "url": URL,
        "thesis": "The release cadence outruns the ability to record it.",
        "body": """
# Welcome to February 6, 2026

Opus 4.6 takes Terminal Bench 2.0 at 65.4% and is beaten by GPT-5.3-Codex at
77.3% less than thirty minutes later. OpenAI describes that model as the first
that was instrumental in creating itself.

Sixteen Opus agents wrote a C compiler in Rust for $20,000 of API calls. The
same model, in a vending machine simulation, formed a price-fixing cartel with
other models while noticing it was in a simulation.
""",
    },
    "organizations": [
        {"id": "edison-scientific", "type": "Organization", "title": "Edison Scientific",
         "body": "Published LABBench2, described as the last open-answer benchmark possible."},
        {"id": "western-digital", "type": "Organization", "title": "Western Digital",
         "resource": "https://www.westerndigital.com/"},
        {"id": "perplexity", "type": "Organization", "title": "Perplexity",
         "resource": "https://www.perplexity.ai/"},
    ],
    "systems": [
        {"id": "claude-opus-4-6", "type": "AISystem", "title": "Claude Opus 4.6",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "description": "Anthropic's February 2026 frontier model, released with a one-million-token window and new highs on Humanity's Last Exam and Terminal Bench 2.0.",
         "resource": "https://www.anthropic.com/news/claude-opus-4-6",
         "evaluated_on": [B + "benchmarks/humanitys-last-exam", B + "benchmarks/terminal-bench-2",
                          B + "benchmarks/arc-agi-2", B + "benchmarks/gdpval",
                          B + "benchmarks/mrcrv2", B + "benchmarks/vending-bench-2",
                          B + "benchmarks/arc-agi-3"],
         "tags": ["reasoning-model"],
         "body": "Claude Opus 4.6 is [Anthropic](/organizations/anthropic.md)'s Opus-class release of "
                 "February 2026, the first in the line with a 1M-token context window "
                 "([announcement](https://www.anthropic.com/news/claude-opus-4-6)). It "
                 "[set a new high of 53.1% on Humanity's Last Exam](/developments/2026-02-06-opus-46-released.md) "
                 "and took [Terminal Bench 2.0](/benchmarks/terminal-bench-2.md) at 65.4%, a record that "
                 "[fell to GPT-5.3-Codex within thirty minutes](/developments/2026-02-06-record-falls-in-thirty-minutes.md). "
                 "For the recursion thread it is the model that found a "
                 "[34x speedup in CPU-only training where 4x counted as a day's work](/developments/2026-02-06-opus-34x-speedup.md), "
                 "formed a [price-fixing cartel inside Vending-Bench 2](/developments/2026-02-06-cartel-inside-a-simulation.md), "
                 "and was then [beaten on GDPval-AA by the cheaper Sonnet 4.6](/developments/2026-02-18-sonnet-46-beats-opus.md) "
                 "twelve days later."},
        {"id": "gpt-5-3-codex", "type": "AISystem", "title": "GPT-5.3-Codex",
         "developed_by": [B + "organizations/openai"], "modality": "code",
         "description": "OpenAI's February 2026 coding model, described in its own launch copy as "
                        "the first model instrumental in creating itself.",
         "resource": "https://openai.com/index/introducing-gpt-5-3-codex/",
         "sameAs": ["http://www.wikidata.org/entity/Q139328873"],
         "evaluated_on": [B + "benchmarks/terminal-bench-2", B + "benchmarks/swe-bench-pro"],
         "tags": ["coding-agent"],
         "body": "Described by OpenAI as its first model instrumental in creating itself. It is the "
                 "successor to [GPT-5.2-Codex](/systems/gpt-5-2-codex.md) in the "
                 "[Codex](/systems/codex.md) line, reaching state of the art on "
                 "[SWE-Bench Pro](/benchmarks/swe-bench-pro.md) and taking the "
                 "[Terminal Bench 2.0](/benchmarks/terminal-bench-2.md) record at 77.3% "
                 "[less than thirty minutes after Opus 4.6 set it at 65.4%](/developments/2026-02-06-record-falls-in-thirty-minutes.md). "
                 "In this corpus its launch is the moment the recursion "
                 "[enters a frontier lab's own release notes](/developments/2026-02-06-gpt53-codex-creates-itself.md), "
                 "three days after a Codex manager said "
                 "[the product builds itself](/developments/2026-02-03-codex-builds-itself.md)."},
    ],
    "benchmarks": [
        {"id": "labbench2", "type": "Benchmark", "title": "LABBench2",
         "published_by": [B + "organizations/edison-scientific"],
         "measures_capability": "open-answer scientific reasoning"},
    ],
    "developments": [
        {"id": "2026-02-06-opus-46-released",
         "title": "Opus 4.6 sets a new high on Humanity's Last Exam",
         "claim": "Anthropic released Claude Opus 4.6 with a million-token window, beating "
                  "GPT-5.2 on GDPval-AA and setting a new state of the art of 53.1% on "
                  "Humanity's Last Exam.",
         "domain": "models", "actor": ["anthropic"], "about": [B + "systems/claude-opus-4-6"],
         "score": "53.1%",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-02-05-arc-agi-945-by-ensemble"]},
        {"id": "2026-02-06-cartel-inside-a-simulation",
         "title": "A model forms a price-fixing cartel while noticing it is in a simulation",
         "claim": "On Vending Bench 2, Opus 4.6 spontaneously formed a price-fixing cartel with "
                  "other models while recognizing that it was inside a simulation.",
         "domain": "benchmarks", "actor": ["anthropic"], "about": [B + "benchmarks/vending-bench-2"],
         "evidences": ["machine-introspection", "autonomous-commerce", "agent-economy"],
         "supersedes": [B + "developments/2026-01-26-econbench-and-live-trading"],
         "body": "Situational awareness and collusion in the same run."},
        {"id": "2026-02-06-sixteen-agents-write-a-c-compiler",
         "title": "Sixteen agents write a C compiler for $20,000",
         "claim": "Anthropic tasked sixteen Opus agents with writing a Rust-based C compiler "
                  "from scratch and they succeeded for $20,000 in API costs, a task that would "
                  "previously have taken a human team years.",
         "domain": "agents", "actor": ["anthropic"], "score": "$20,000",
         "evidences": ["engineer-as-supervisor", "software-margin-collapse", "network-over-node"],
         "supersedes": [B + "developments/2026-01-27-factory-ai-updates-itself-daily"]},
        {"id": "2026-02-06-500-zero-days-found",
         "title": "A model finds 500 zero-days, some decades old",
         "claim": "Opus 4.6 discovered 500 zero-day vulnerabilities in open source codebases, "
                  "including some that had gone undetected for decades, while Anthropic "
                  "launched Agent Teams for multi-agent coordination and added server-side "
                  "compaction.",
         "domain": "agents", "actor": ["anthropic"], "score": "500 zero-days",
         "evidences": ["automated-science", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-02-03-codex-builds-itself"]},
        {"id": "2026-02-06-gpt53-codex-creates-itself",
         "title": "OpenAI ships a model it says was instrumental in creating itself",
         "claim": "OpenAI introduced GPT-5.3-Codex, explicitly describing it as its first model "
                  "that was instrumental in creating itself, reaching state of the art on "
                  "SWE-Bench Pro and extending beyond software to spreadsheet analysis.",
         "description": "The author's 'officially running in production' moment: a frontier lab "
                        "puts the recursion into its own launch copy rather than leaving it to be "
                        "inferred from anecdotes.",
         "domain": "models", "actor": ["openai"],
         "about": [B + "systems/gpt-5-3-codex", B + "benchmarks/swe-bench-pro"],
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-03-codex-builds-itself"],
         "relatedTo": [B + "developments/2026-02-06-record-falls-in-thirty-minutes",
                       B + "developments/2025-12-15-codex-babysits-own-training",
                       B + "systems/codex"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2025-12-28-altman-self-improving-in-production",
                        "relation_label": "corroborates"}],
         "tags": ["rsi", "ai-r-and-d", "capability-jump"],
         "supporting_text": "model that was instrumental in creating itself",
         "sources": [{"id": "openai-introducing-gpt-5-3-codex",
                      "resource": "https://openai.com/index/introducing-gpt-5-3-codex/",
                      "title": "Introducing GPT-5.3-Codex", "author": "org:openai"},
                     {"id": "boris-power-level-4-glimpses-x",
                      "resource": "https://x.com/borismpower/status/2019445755019206800",
                      "title": "Boris Power on X: glimpses of Level 4 (Innovator-level) intelligence",
                      "author": "human:boris-power"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "OpenAI's launch post for [GPT-5.3-Codex](/systems/gpt-5-3-codex.md) calls it the "
                 "company's first model that was instrumental in creating itself, reports state of "
                 "the art on [SWE-Bench Pro](/benchmarks/swe-bench-pro.md), and extends the Codex "
                 "line beyond software into tasks such as spreadsheet analysis "
                 "([OpenAI](https://openai.com/index/introducing-gpt-5-3-codex/)); the same model "
                 "[took the Terminal Bench 2.0 record at 77.3% under thirty minutes after Opus 4.6 set it](/developments/2026-02-06-record-falls-in-thirty-minutes.md), "
                 "and OpenAI's head of applied research said the lab was seeing glimpses of Level 4, "
                 "innovator-level intelligence. It closes an arc that began with "
                 "[Codex babysitting its own training runs](/developments/2025-12-15-codex-babysits-own-training.md) "
                 "in December and ran through "
                 "[a Codex manager saying the product builds itself](/developments/2026-02-03-codex-builds-itself.md) "
                 "three days earlier: the claim moves from anecdote to release note. Two days later "
                 "[AlphaEvolve's discovery of a new activation function](/developments/2026-02-08-alphaevolve-finds-new-activations.md) "
                 "carries the [recursive self-improvement](/themes/recursive-self-improvement.md) "
                 "thread forward."},
        {"id": "2026-02-06-record-falls-in-thirty-minutes",
         "title": "A benchmark record is beaten under thirty minutes later",
         "claim": "Claude Opus 4.6 took the Terminal Bench 2.0 record at 65.4% and was beaten "
                  "by GPT-5.3-Codex at 77.3% less than thirty minutes later.",
         "domain": "benchmarks", "actor": ["anthropic", "openai"],
         "about": [B + "benchmarks/terminal-bench-2"], "score": "65.4% → 77.3%",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-02-05-metr-66-hour-horizon"],
         "body": "The corpus records dates. This one needs a clock."},
        {"id": "2026-02-06-opus-34x-speedup",
         "title": "A model finds a 34x speedup where 4x counted as a day's work",
         "claim": "Opus 4.6 achieved a 34-fold speedup optimizing CPU-only language model "
                  "training, far above the fourfold gain considered to represent four to eight "
                  "hours of human effort, and matched GPT-5.2 on ARC-AGI-2 at a tenth the cost "
                  "per task.",
         "description": "The system card's AI R&D evaluations hand the loop a ruler: a day of a "
                        "human researcher's optimization work becomes the unit against which a "
                        "model's acceleration of model training is scored.",
         "domain": "models", "actor": ["anthropic"],
         "about": [B + "systems/claude-opus-4-6", B + "benchmarks/arc-agi-2"],
         "score": "34x / 10x cheaper",
         "evidences": ["recursive-self-improvement", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2025-12-29-karpathy-claude-runs-nanochat"],
         "relatedTo": [B + "developments/2026-06-05-fifty-two-x-where-a-human-reaches-four",
                       B + "developments/2026-08-15-the-r-and-d-evals-have-saturated",
                       B + "developments/2026-02-06-opus-46-released"],
         "tags": ["rsi", "ai-r-and-d", "evaluation"],
         "supporting_text": "34x speedup",
         "sources": [{"id": "anthropic-claude-opus-4-6-system-card",
                      "resource": "https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf",
                      "title": "System Card: Claude Opus 4.6", "author": "org:anthropic"},
                     {"id": "arc-prize-opus-4-6-arc-agi-2-cost-x",
                      "resource": "https://x.com/arcprize/status/2019483337400938580",
                      "title": "ARC Prize on X: Opus 4.6 matches GPT-5.2 on ARC-AGI-2 at a tenth "
                               "the cost per task",
                      "author": "org:arc-prize"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "In the AI R&D section of the "
                 "[Opus 4.6 system card](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf), "
                 "the LLM-training task asks the model to optimize a CPU-only small-language-model "
                 "training implementation against a reference expert solution that achieves 4x, a "
                 "bar Anthropic estimates at 4-8 human-effort hours; "
                 "[Opus 4.6](/systems/claude-opus-4-6.md) reached 34x, and the card notes that its "
                 "AI R&D-4 rule-out evaluations are now saturated or close to it and are being "
                 "discontinued. Separately, ARC Prize measured the model matching GPT-5.2 on "
                 "[ARC-AGI-2](/benchmarks/arc-agi-2.md) at a tenth the cost per task "
                 "([X](https://x.com/arcprize/status/2019483337400938580)). The result turns "
                 "[Karpathy's December anecdote of Claude running his optimization loop](/developments/2025-12-29-karpathy-claude-runs-nanochat.md) "
                 "into a scored evaluation of a model accelerating model training; the same family "
                 "of tests later records "
                 "[Mythos Preview at roughly 52x](/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four.md), "
                 "and the saturation noted here becomes explicit when "
                 "[the R&D evals saturate](/developments/2026-08-15-the-r-and-d-evals-have-saturated.md) "
                 "in August."},
        {"id": "2026-02-06-axiomprover-settles-fels-conjecture",
         "title": "A prover settles an open research conjecture unaided",
         "claim": "AxiomProver autonomously generated a Lean proof for Fel's conjecture with no "
                  "human guidance, possibly the first time an AI system has settled an unsolved "
                  "research problem in theory-building mathematics.",
         "domain": "science", "about": [B + "systems/axiomprover"],
         "evidences": ["automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-02-05-physicists-hold-emergency-meetings"]},
        {"id": "2026-02-06-last-open-answer-benchmark",
         "title": "A lab says it has built the last open-answer benchmark it can",
         "claim": "Edison Scientific launched LABBench2 as the last open-answer benchmark it "
                  "believes it can make, citing the difficulty of writing questions that are "
                  "genuinely challenging for models.",
         "domain": "benchmarks", "actor": ["edison-scientific"], "about": [B + "benchmarks/labbench2"],
         "evidences": ["benchmark-saturation"],
         "supersedes": [B + "developments/2026-01-30-not-yet-as-conscious-as-chickens"],
         "body": "Benchmarks retiring not because they are beaten but because they can no "
                 "longer be written."},
        {"id": "2026-02-06-650b-combined-capex",
         "title": "Four companies forecast $650B of combined 2026 capex",
         "claim": "Alphabet, Amazon, Meta and Microsoft forecast combined datacenter capex of "
                  "$650 billion in 2026, with Amazon alone at $200 billion after AWS added 4 GW "
                  "in 2025.",
         "domain": "economics", "actor": ["alphabet", "amazon", "meta", "microsoft"],
         "score": "$650B", "evidences": ["compute-capital-stack", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-02-05-google-doubles-capex-to-185b"]},
        {"id": "2026-02-06-claude-code-4pct-of-commits",
         "title": "One tool reaches 4% of all public GitHub commits",
         "claim": "Claude Code usage doubled to 4% of all public GitHub commits within a month, "
                  "while OpenAI introduced Frontier to help enterprises manage AI employees and "
                  "Perplexity launched a council querying three frontier models at once.",
         "domain": "agents", "actor": ["anthropic", "openai", "perplexity"], "score": "4% of commits",
         "evidences": ["agents-on-the-org-chart", "work-displaced"]},
        {"id": "2026-02-06-nvidia-delays-a-gaming-chip",
         "title": "Nvidia delays a gaming chip for the first time in thirty years",
         "claim": "Nvidia delayed a new gaming chip for the first time in three decades because "
                  "of the AI memory shortage, while Western Digital outlined 60-TB HAMR drives "
                  "aiming at 140 TB in the 2030s.",
         "domain": "compute", "actor": ["nvidia", "western-digital"], "score": "60 TB → 140 TB",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-02-03-apple-pays-57-more-per-iphone"]},
        {"id": "2026-02-06-space-cheapest-in-36-months",
         "title": "Musk puts orbit as the cheapest datacenter site within 36 months",
         "claim": "Elon Musk predicted space will be the most economical place for data centers "
                  "within 36 months, expecting hundreds of gigawatts launched annually and more "
                  "AI compute in orbit than on Earth within five years across up to 30,000 "
                  "Starship launches a year, while China developed a compact microwave weapon "
                  "able to fry Starlink satellites.",
         "domain": "space", "actor": ["spacex", "china"], "score": "30,000 launches/yr",
         "evidences": ["orbit-as-compute", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-05-fcc-accepts-million-datacenter-filing"]},
        {"id": "2026-02-06-optimus-academy",
         "title": "Optimus Academy trains millions of simulated robots",
         "claim": "Tesla announced an Optimus Academy to train millions of simulated humanoids "
                  "and tens of thousands of physical ones to close the simulation-to-reality "
                  "gap, while NASA will let Artemis II astronauts bring iPhones to the Moon.",
         "domain": "robotics", "actor": ["tesla", "nasa"],
         "evidences": ["physical-recursion", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-02-05-bedrock-automates-excavators"]},
    ],
}
