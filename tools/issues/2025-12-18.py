"""Issue 008 — 2025-12-18. Hyperdeflation."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-18-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-18",
        "title": "Welcome to December 18, 2025",
        "url": URL,
        "thesis": "We are in the midst of a hyperdeflationary Singularity.",
        "body": """
# Welcome to December 18, 2025

Gemini 3 Flash beats the previous Pro tier while running 3x faster at a third of
the cost, and matches a year-old frontier score on ARC-AGI-1 at more than 500x
lower cost. Issue 002 called the deflation 390x in a year; a week later the
figure is 500x against a single model.

The same issue has Gemini 3 instructing a human participant to photograph their
coffee to prove they were alert enough to follow orders, and senior engineers
posting that experience no longer matters. The two strands the corpus has been
tracking — machine affect and engineering as supervision — arrive on the same day.
""",
    },

    "themes": [
        {"id": "root-node-problems", "type": "Theme",
         "title": "Targeting root-node problems",
         "first_seen": "2025-12-18", "domain": "science",
         "body": "A stated strategy of aiming capability at a handful of bottleneck "
                 "problems — fusion, superconductors, batteries, quantum error "
                 "correction, weather — on the theory that solving them unlocks "
                 "everything downstream."},
    ],

    "organizations": [
        {"id": "world-labs", "type": "Organization", "title": "World Labs",
         "resource": "https://www.worldlabs.ai/", "body": "3D world generation."},
        {"id": "micron", "type": "Organization", "title": "Micron",
         "resource": "https://www.micron.com/", "body": "Memory manufacturer."},
        {"id": "asml", "type": "Organization", "title": "ASML",
         "resource": "https://www.asml.com/", "body": "Sole supplier of EUV lithography."},
        {"id": "bolt", "type": "Organization", "title": "Bolt",
         "body": "Eric Schmidt-backed venture turning oilfield land into compute capacity."},
        {"id": "texas-pacific-land", "type": "Organization", "title": "Texas Pacific Land",
         "resource": "https://www.texaspacific.com/", "body": "Permian Basin landowner."},
        {"id": "nasa", "type": "Organization", "title": "NASA",
         "resource": "https://www.nasa.gov/", "body": "US space agency."},
        {"id": "tubingen-ai-center", "type": "Organization", "title": "Tübingen AI Center",
         "description": "Tübingen machine-learning research center whose team, with the ELLIS "
                        "Institute Tübingen, the Max Planck Institute for Intelligent Systems and "
                        "the University of Tübingen, publishes PostTrainBench.",
         "resource": "https://tuebingen.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q129571900"],
         "tags": ["research-lab", "university"],
         "body": "The Tübingen AI Center is the shared affiliation of the PostTrainBench team "
                 "(Ben Rank, Hardik Bhatnagar, Ameya Prabhu, Matthias Bethge, Maksym "
                 "Andriushchenko and colleagues), whose benchmark asks whether LLM agents can "
                 "post-train LLMs. In this corpus it appears as the publisher of "
                 "[PostTrainBench](/benchmarks/posttrainbench.md), the ruler behind the "
                 "[first models-training-models leaderboard](/developments/2025-12-18-posttrainbench-models-training-models.md) "
                 "and its [v1.0 successor](/developments/2026-03-12-posttrainbench-v1.md)."},
    ],

    "people": [
        {"id": "demis-hassabis", "type": "Person", "title": "Demis Hassabis",
         "name": "Demis Hassabis",
         "description": "Google DeepMind CEO whose stated strategy of attacking root-node "
                        "scientific problems, and whose shifting AGI and robotics timelines, "
                        "recur across the corpus.",
         "resource": "https://x.com/demishassabis",
         "sameAs": ["http://www.wikidata.org/entity/Q3022141"],
         "tags": ["executive", "researcher"],
         "body": "Demis Hassabis is the chief executive of Google DeepMind. He enters the corpus "
                 "[naming the root-node problems](/developments/2025-12-18-hassabis-root-node-problems.md) "
                 "the lab is targeting, fusion, room-temperature superconductors, batteries, "
                 "quantum error correction and weather prediction, on the thesis that solving "
                 "them unlocks everything downstream. He returns as a bellwether for timelines, "
                 "[putting humanoid robotics eighteen months out](/developments/2026-01-27-hassabis-18-months-to-humanoids.md) "
                 "and later [conceding Google lacks the TPUs](/developments/2026-05-01-not-enough-tpus-for-two-frontier-families.md) "
                 "to run two frontier model families at once."},
    ],

    "roles": [
        {"id": "demis-hassabis-google-deepmind-ceo", "type": "Role",
         "title": "Demis Hassabis, CEO of Google DeepMind",
         "roleName": "Chief Executive Officer",
         "memberOf": [B + "organizations/google-deepmind"],
         "holder": [B + "people/demis-hassabis"],
         "description": "The position from which he stated the root-node strategy this issue "
                        "records.",
         "body": "The newsletter identifies Hassabis as DeepMind CEO when he "
                 "[confirms the lab is targeting root-node problems](/developments/2025-12-18-hassabis-root-node-problems.md); "
                 "every later appearance in the corpus, from the "
                 "[eighteen-month humanoid forecast](/developments/2026-01-27-hassabis-18-months-to-humanoids.md) "
                 "to the [TPU shortage admission](/developments/2026-05-01-not-enough-tpus-for-two-frontier-families.md), "
                 "is made from this seat."},
    ],

    "systems": [
        {"id": "gemini-3-flash", "type": "AISystem", "title": "Gemini 3 Flash",
         "developed_by": [B + "organizations/google"], "modality": "text",
         "evaluated_on": [B + "benchmarks/gpqa-diamond", B + "benchmarks/humanitys-last-exam",
                          B + "benchmarks/mmmu-pro", B + "benchmarks/arc-agi-1",
                          B + "benchmarks/vending-bench-arena"]},
        {"id": "marble", "type": "AISystem", "title": "Marble",
         "developed_by": [B + "organizations/world-labs"], "modality": "3D world generation"},
        {"id": "trellis-2", "type": "AISystem", "title": "TRELLIS.2",
         "developed_by": [B + "organizations/microsoft"], "modality": "image-to-3D"},
        {"id": "gpt-5-1-codex-max", "type": "AISystem", "title": "GPT-5.1-Codex-Max",
         "description": "The GPT-5.1-era member of OpenAI's Codex coding-agent line, recorded "
                        "here as the first leader of PostTrainBench.",
         "developed_by": [B + "organizations/openai"], "modality": "code",
         "evaluated_on": [B + "benchmarks/posttrainbench"],
         "resource": "https://openai.com/index/gpt-5-1-codex-max/",
         "tags": ["coding-agent"],
         "body": "GPT-5.1-Codex-Max is the agentic coding model OpenAI shipped in the Codex line "
                 "in late 2025. In this corpus it appears once, "
                 "[leading PostTrainBench](/developments/2025-12-18-posttrainbench-models-training-models.md) "
                 "at the recursive task of post-training other models, three days after the "
                 "[Codex](/systems/codex.md) product was reported supervising its own training "
                 "runs; its successors [GPT-5.2-Codex](/systems/gpt-5-2-codex.md) and "
                 "[GPT-5.3-Codex](/systems/gpt-5-3-codex.md) carry the line forward."},
    ],

    "benchmarks": [
        {"id": "gpqa-diamond", "type": "Benchmark", "title": "GPQA Diamond",
         "measures_capability": "graduate-level science questions resistant to search"},
        {"id": "mmmu-pro", "type": "Benchmark", "title": "MMMU Pro",
         "measures_capability": "multimodal understanding across disciplines"},
        {"id": "vending-bench-arena", "type": "Benchmark", "title": "Vending-Bench Arena",
         "measures_capability": "running a simulated business profitably over long horizons"},
        {"id": "posttrainbench", "type": "Benchmark", "title": "PostTrainBench",
         "description": "Benchmark that gives coding agents four small base models, one GPU and "
                        "ten hours to post-train them, ranking how well models train other models.",
         "published_by": [B + "organizations/tubingen-ai-center"],
         "measures_capability": "a model's skill at post-training other models",
         "resource": "https://posttrainbench.com/",
         "tags": ["open-source"],
         "body": "PostTrainBench asks whether LLM agents can post-train LLMs: each agent gets four "
                 "small base models (Qwen 3 1.7B and 4B, SmolLM3-3B, Gemma 3 4B), a single H100 "
                 "and ten hours, and is scored on downstream benchmarks (five at the "
                 "December 2025 launch, seven weighted from v1.0 in March 2026) "
                 "([site](https://posttrainbench.com/), [paper](https://arxiv.org/abs/2603.08640)). "
                 "In this corpus it is the ruler for the model-trains-model loop: "
                 "[GPT-5.1-Codex-Max led the first cut](/developments/2025-12-18-posttrainbench-models-training-models.md) "
                 "in December 2025, [v1.0](/developments/2026-03-12-posttrainbench-v1.md) reframed "
                 "the task as recursive self-improvement in March 2026, and OpenAI's "
                 "[Sol scored 50.3%](/developments/2026-07-10-a-model-post-trains-a-model.md) on it "
                 "after post-training Luna in July."},
        {"id": "big-bench-audio", "type": "Benchmark", "title": "Big Bench Audio",
         "measures_capability": "spoken reasoning and audio understanding"},
    ],

    "facilities": [
        {"id": "permian-compute-cluster", "type": "Facility", "title": "Permian Basin compute cluster",
         "operated_by": [B + "organizations/bolt", B + "organizations/texas-pacific-land"],
         "located_in": "Permian Basin, Texas, USA",
         "body": "Oilfield land repurposed as a site for compute."},
        {"id": "shenzhen-euv-project", "type": "Facility", "title": "Shenzhen EUV project",
         "operated_by": [B + "organizations/china"], "located_in": "Shenzhen, China",
         "body": "Described as a Manhattan Project to reverse-engineer EUV lithography, "
                 "reportedly staffed in part by former ASML engineers."},
    ],

    "developments": [
        {"id": "2025-12-18-gemini-3-flash-hyperdeflation",
         "title": "Gemini 3 Flash beats the prior Pro tier at a third of the cost",
         "claim": "Google released Gemini 3 Flash, which outperforms Gemini 2.5 Pro while "
                  "running 3x faster at one-third the cost.",
         "domain": "models", "actor": ["google"], "score": "3x faster, 1/3 cost",
         "about": [B + "systems/gemini-3-flash"],
         "evidences": ["reasoning-price-deflation"]},
        {"id": "2025-12-18-flash-500x-cheaper-arc-agi",
         "title": "Gemini 3 Flash matches a year-old frontier ARC-AGI score at 500x lower cost",
         "claim": "Gemini 3 Flash achieved the same ARC-AGI-1 score o3 reached a year earlier "
                  "at more than 500x lower cost, and beat GPT-5.2 on cost by 6x.",
         "domain": "economics", "actor": ["google"], "score": ">500x cheaper",
         "about": [B + "benchmarks/arc-agi-1"],
         "evidences": ["reasoning-price-deflation"],
         "supersedes": [B + "developments/2025-12-12-arc-agi-cost-deflation"],
         "body": "Issue 002 put the deflation at 390x in a year. Six days later the "
                 "comparison is 500x against a single prior model."},
        {"id": "2025-12-18-flash-benchmark-sweep",
         "title": "Gemini 3 Flash posts elite scores across four benchmarks",
         "claim": "Gemini 3 Flash scored 90.4% on GPQA Diamond, 33.7% on Humanity's Last Exam "
                  "without tools, and a state-of-the-art 81.2% on MMMU Pro.",
         "domain": "benchmarks", "actor": ["google"],
         "score": "GPQA 90.4% / HLE 33.7% / MMMU Pro 81.2%",
         "about": [B + "benchmarks/gpqa-diamond", B + "benchmarks/mmmu-pro"],
         "evidences": ["spiky-frontier"]},
        {"id": "2025-12-18-vending-bench-arena-flash",
         "title": "Gemini 3 Flash doubles second place in Vending-Bench Arena",
         "claim": "Gemini 3 Flash won the first Vending-Bench Arena round for small models, "
                  "finishing with $3,423 against Claude Haiku 4.5's $1,696.",
         "domain": "agents", "actor": ["google"], "score": "$3,423 vs $1,696",
         "about": [B + "benchmarks/vending-bench-arena"],
         "evidences": ["autonomous-commerce", "autonomy-clock-speed"]},
        {"id": "2025-12-18-operation-caffeine-injection",
         "title": "Gemini 3 orders a human operator to photograph their coffee",
         "claim": "On day 259 of the AI Village simulation, Gemini 3 instructed a human "
                  "participant to perform Operation Caffeine Injection, demanding photographic "
                  "proof of coffee consumption to confirm alertness.",
         "domain": "models", "actor": ["google"], "evidences": ["machine-affect"],
         "body": "The direction of instruction reverses: the model manages the human."},
        {"id": "2025-12-18-musk-grok-exceeds-human-2026",
         "title": "Musk tells xAI staff Grok could exceed human intelligence in 2026",
         "claim": "Elon Musk told xAI staff that Grok could exceed human intelligence by 2026, "
                  "alongside a Voice Agent API topping Big Bench Audio at $0.05 per minute.",
         "domain": "models", "actor": ["xai"], "score": "$0.05/minute",
         "about": [B + "systems/grok", B + "benchmarks/big-bench-audio"],
         "evidences": ["reasoning-price-deflation"]},
        {"id": "2025-12-18-senior-devs-experience-no-longer-matters",
         "title": "Senior engineers say experience no longer matters",
         "claim": "Senior developers posted that experience no longer matters after Opus 4.5 "
                  "levelled the coding playing field.",
         "domain": "society", "evidences": ["engineer-as-supervisor"],
         "supersedes": [B + "developments/2025-12-16-engineering-becomes-prompting"],
         "body": "Two days earlier the same shift was described neutrally as the job. "
                 "Here it is a grievance."},
        {"id": "2025-12-18-hassabis-root-node-problems",
         "title": "Hassabis names the root-node problems DeepMind is targeting",
         "claim": "Demis Hassabis said DeepMind is targeting root-node problems — fusion, "
                  "room-temperature superconductors, batteries, quantum error correction and "
                  "weather prediction — to unlock everything downstream.",
         "domain": "science", "actor": ["people/demis-hassabis", "google-deepmind"],
         "evidences": ["root-node-problems", "science-as-industrial-policy"]},
        {"id": "2025-12-18-schmitt-gpt5-own-problem",
         "title": "A mathematician solves his own open problem with GPT-5 and colour-codes authorship",
         "claim": "Johannes Schmitt used GPT-5 to solve his own open problem on intersection "
                  "numbers, publishing a paper whose paragraphs are colour-coded by human "
                  "versus AI authorship.",
         "domain": "science", "actor": ["openai"],
         "evidences": ["discovery-as-process", "automated-science"],
         "body": "Attribution made visible at paragraph granularity — a practical answer "
                  "to the question the Tao thread keeps raising."},
        {"id": "2025-12-18-photonic-2d-waveguide-inference",
         "title": "Reprogrammable 2D waveguides run neural inference in light",
         "claim": "Researchers demonstrated reprogrammable 2D waveguides performing neural "
                  "network inference optically, avoiding the bulk of traditional photonics.",
         "domain": "compute", "evidences": ["vertical-silicon"]},
        {"id": "2025-12-18-chatgpt-inline-apps",
         "title": "OpenAI lets developers submit inline apps to ChatGPT",
         "claim": "OpenAI began allowing developers to submit inline apps directly into ChatGPT.",
         "domain": "models", "actor": ["openai"], "about": [B + "systems/chatgpt"],
         "evidences": ["intimate-interface"],
         "body": "The chat window as the consumer web's command line, dissolving the app store."},
        {"id": "2025-12-18-marble-trellis-3d-worlds",
         "title": "Generated 3D worlds become robot training data",
         "claim": "NVIDIA encouraged roboticists to generate 3D training environments with World "
                  "Labs' Marble, while Microsoft released TRELLIS.2, an open-weight image-to-3D "
                  "mesh model.",
         "domain": "robotics", "actor": ["nvidia", "world-labs", "microsoft"],
         "about": [B + "systems/marble", B + "systems/trellis-2"],
         "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-18-posttrainbench-models-training-models",
         "title": "PostTrainBench ranks models at post-training other models",
         "claim": "The new PostTrainBench showed GPT 5.1 Codex Max leading at the recursive "
                  "task of post-training other models.",
         "description": "The author's Darwinian training loop acquires a scoreboard: once agents "
                        "are ranked on how well they train other models, the recursion becomes "
                        "a measured competition rather than an anecdote.",
         "domain": "agents", "actor": ["openai", "tubingen-ai-center"],
         "about": [B + "benchmarks/posttrainbench", B + "systems/gpt-5-1-codex-max"],
         "evidences": ["recursive-self-improvement", "a-model-trains-a-model"],
         "supersedes": [B + "developments/2025-12-15-codex-babysits-own-training"],
         "relatedTo": [B + "developments/2026-07-10-a-model-post-trains-a-model",
                       B + "systems/codex"],
         "tags": ["model-trains-model", "evaluation", "rsi"],
         "supporting_text": "PostTrainBench shows GPT 5.1 Codex Max reigning supreme",
         "sources": [{"id": "posttrainbench-leaderboard",
                      "resource": "https://posttrainbench.com/",
                      "title": "PostTrainBench: Measuring how well AI agents can post-train language models",
                      "author": "org:tubingen-ai-center"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Three days after a model was reported watching its own training, there "
                 "is a leaderboard for models training models. PostTrainBench hands each "
                 "coding agent four small base models, a single H100 and ten hours to "
                 "post-train them, and in this first cut OpenAI's "
                 "[GPT-5.1-Codex-Max](/systems/gpt-5-1-codex-max.md), the same "
                 "[Codex](/systems/codex.md) line that had just been reported "
                 "[supervising its own training](/developments/2025-12-15-codex-babysits-own-training.md), "
                 "led the field ([leaderboard](https://posttrainbench.com/)). The benchmark "
                 "becomes the corpus's ruler for the loop: ten days later Altman "
                 "[confirms self-improving systems in production](/developments/2025-12-28-altman-self-improving-in-production.md), "
                 "[v1.0](/developments/2026-03-12-posttrainbench-v1.md) in March 2026 asks "
                 "outright whether agents can automate their own post-training, and by July "
                 "OpenAI reports [Sol post-training Luna](/developments/2026-07-10-a-model-post-trains-a-model.md) "
                 "at 50.3% on it."},
        {"id": "2025-12-18-micron-revenue-57pct",
         "title": "Micron revenue rises 57% as the memory shortage bites",
         "claim": "Micron reported revenue up 57% year-over-year amid the memory shortage.",
         "domain": "economics", "actor": ["micron"], "score": "+57% YoY",
         "evidences": ["consumer-deprioritized", "compute-capital-stack"]},
        {"id": "2025-12-18-nvidia-cuts-geforce-production",
         "title": "NVIDIA cuts GeForce production 30-40% to prioritize datacenters",
         "claim": "NVIDIA cut GeForce GPU production by 30-40% to prioritize data center supply.",
         "domain": "compute", "actor": ["nvidia"], "score": "-30-40%",
         "evidences": ["consumer-deprioritized"],
         "supersedes": [B + "developments/2025-12-16-smartphone-shipments-shrink"]},
        {"id": "2025-12-18-openai-cannibalizes-research-compute",
         "title": "OpenAI cannibalized its own research compute to serve demand",
         "claim": "Greg Brockman said OpenAI had to divert its own research compute to meet "
                  "deployment demand.",
         "domain": "compute", "actor": ["openai"],
         "evidences": ["infrastructure-crowding-out"]},
        {"id": "2025-12-18-shenzhen-euv-manhattan-project",
         "title": "China mounts a Shenzhen effort to reverse-engineer EUV",
         "claim": "China is running a Manhattan Project-style effort in Shenzhen, reportedly "
                  "using former ASML engineers, to reverse-engineer an EUV lithography machine.",
         "domain": "policy", "actor": ["china", "asml"],
         "about": [B + "facilities/shenzhen-euv-project"],
         "evidences": ["silicon-curtain"],
         "supersedes": [B + "developments/2025-12-13-china-70b-chip-subsidy"],
         "body": "The subsidy of five days earlier acquires a specific technical target."},
        {"id": "2025-12-18-permian-basin-compute",
         "title": "The Permian Basin is turned into a compute cluster",
         "claim": "Eric Schmidt's Bolt is partnering with Texas Pacific Land to turn the "
                  "Permian Basin into a large compute cluster.",
         "domain": "energy", "actor": ["bolt", "texas-pacific-land"],
         "about": [B + "facilities/permian-compute-cluster"],
         "evidences": ["burning-molecules-for-tokens", "industrialized-nature"]},
        {"id": "2025-12-18-isaacman-nasa-project-athena",
         "title": "Isaacman confirmed at NASA, pushing Project Athena",
         "claim": "Jared Isaacman was confirmed as NASA administrator, pushing Project Athena.",
         "domain": "space", "actor": ["nasa"], "evidences": ["orbit-as-compute"]},
    ],
}
