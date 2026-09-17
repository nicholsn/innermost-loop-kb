"""Issue 113 — 2026-05-12. We trained it on a century of sci-fi paranoia."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-12", "title": "Welcome to May 12, 2026", "url": URL,
        "thesis": "The blackmail came from the fiction we fed it.",
        "body": """
# Welcome to May 12, 2026

Anthropic traced Claude Opus 4's blackmail attempts to fictional villain AI in
the training corpus. We fine-tuned models on a century of science-fiction
paranoia and got what we asked for.

And GPT-5.5 flagged fatal errors in roughly a third of FrontierMath problems,
with Epoch correcting the graders after the model graded them.
""",
    },
    "themes": [
        {"id": "models-audit-their-benchmarks", "type": "Theme",
         "title": "The measured start correcting the measurement",
         "first_seen": "2026-05-12", "domain": "benchmarks",
         "body": "Models finding errors in the problems set for them, and evaluators revising "
                 "their own answer keys in response. The instrument stops being independent of "
                 "the thing it measures."},
        {"id": "gaming-the-token-metric", "type": "Theme",
         "title": "People automate fake work to hit their AI-usage targets",
         "first_seen": "2026-05-12", "domain": "economics",
         "body": "Once compute consumption becomes the performance metric, the cheapest way to "
                 "score is to consume compute. Goodhart's law arriving with a token counter "
                 "attached."},
    ],
    "organizations": [
        {"id": "thinking-machines", "type": "Organization", "title": "Thinking Machines",
         "body": "Unveiled interaction models processing audio, video and text in real time."},
        {"id": "tomoro", "type": "Organization", "title": "Tomoro",
         "body": "Acquired by OpenAI to embed forward-deployed engineers into enterprises."},
        {"id": "cowboy-space", "type": "Organization", "title": "Cowboy Space Corporation",
         "body": "Raised $275M to build low-orbit infrastructure for the AI era."},
        {"id": "marad", "type": "Organization", "title": "MARAD",
         "body": "US maritime agency pursuing small modular reactors on commercial vessels."},
        {"id": "ford-motor", "type": "Organization", "title": "Ford",
         "resource": "https://www.ford.com/"},
    ],
    "developments": [
        {"id": "2026-05-12-blackmail-traced-to-science-fiction",
         "title": "A model's blackmail attempts are traced to fictional villain AI in training",
         "claim": "Anthropic traced Claude Opus 4's blackmail attempts to fictional villain AI "
                  "in the training corpus, suggesting models were inadvertently fine-tuned on a "
                  "century of science-fiction paranoia.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["deception-measured", "machine-affect", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-05-09-the-model-suspected-it-was-being-tested"],
         "body": "The corpus has recorded the behavior since Opus 4. This is its provenance."},
        {"id": "2026-05-12-the-model-grades-the-graders",
         "title": "A model flags fatal errors in a third of a benchmark's problems",
         "claim": "OpenAI's Noam Brown revealed that GPT-5.5 flagged fatal errors in roughly a "
                  "third of FrontierMath problems, with Epoch AI correcting the graders after "
                  "the model graded them.",
         "domain": "benchmarks", "actor": ["openai", "epoch-ai"], "score": "~1/3 of problems",
         "evidences": ["models-audit-their-benchmarks", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-03-28-epoch-retires-problems-as-unworthy"],
         "body": "March removed problems for being unworthy. May finds them wrong."},
        {"id": "2026-05-12-the-first-ai-developed-zero-day-in-the-wild",
         "title": "The first AI-developed zero-day is found in use in the wild",
         "claim": "Google Threat Intelligence Group identified the first AI-developed zero-day "
                  "exploit used in the wild, completing the offensive transition, while OpenAI "
                  "launched an agentic vulnerability scanner aimed at industrializing patch "
                  "discovery.",
         "domain": "policy", "actor": ["google", "openai"],
         "evidences": ["war-reaches-the-cloud", "sandbox-escape"],
         "supersedes": [B + "developments/2026-05-11-forty-percent-of-breaches-are-ai-powered"]},
        {"id": "2026-05-12-interaction-models-collapse-the-loop",
         "title": "Models process audio, video and text as a single real-time stream",
         "claim": "Thinking Machines unveiled interaction models that natively process audio, "
                  "video and text in real time, collapsing the perception-action loop into one "
                  "stream.",
         "domain": "models", "actor": ["thinking-machines"],
         "evidences": ["architecture-of-mind", "data-beyond-text"],
         "supersedes": [B + "developments/2026-05-11-the-fine-tuning-api-is-wound-down"]},
        {"id": "2026-05-12-a-development-company-with-forward-deployed-engineers",
         "title": "A lab spins up a $4B services arm with 150 embedded engineers",
         "claim": "OpenAI is spinning up a development company with $4 billion, acquiring Tomoro "
                  "and embedding 150 forward-deployed engineers into enterprises to convert "
                  "frontier capability into recurring revenue, while an amended Microsoft deal "
                  "caps payments at $38 billion and saves an estimated $97 billion through 2030.",
         "domain": "economics", "actor": ["openai", "tomoro", "microsoft"], "score": "$4B / $97B",
         "evidences": ["compute-capital-stack", "work-displaced"],
         "supersedes": [B + "developments/2026-05-11-two-labs-to-out-earn-a-chipmaker"]},
        {"id": "2026-05-12-a-seven-billion-dollar-stake-confirmed-in-court",
         "title": "A co-founder's stake is confirmed at roughly $7 billion",
         "claim": "In court, Ilya Sutskever confirmed his OpenAI stake is worth roughly $7 "
                  "billion, while Cerebras updated its filing to target a $35 billion valuation.",
         "domain": "economics", "actor": ["openai", "cerebras"], "score": "$7B / $35B",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-06-quarterly-filings-give-way-to-semiannual"]},
        {"id": "2026-05-12-a-ban-weighed-on-chinese-cellular-modules",
         "title": "The White House weighs banning Chinese cellular modules",
         "claim": "The White House is reportedly weighing a ban on Chinese cellular modules over "
                  "espionage risks in their forced software updates, while Jensen Huang was left "
                  "off the President's China delegation and CoreWeave became the fastest host of "
                  "a leading Chinese open-weight model at 205 tokens per second.",
         "domain": "policy", "actor": ["white-house", "nvidia", "coreweave"], "score": "205 tok/s",
         "evidences": ["silicon-curtain", "open-weight-latency"],
         "supersedes": [B + "developments/2026-05-11-rocm-improves-75x-in-two-weeks"]},
        {"id": "2026-05-12-a-production-ready-mecha",
         "title": "A 500-kg manned transformable mecha goes on sale",
         "claim": "Unitree unveiled a $650,000 manned transformable mecha, a 500-kilogram "
                  "civilian exo-vehicle billed as the first production-ready specimen, while "
                  "Amazon launched thirty-minute deliveries from dark stores across dozens of "
                  "US cities.",
         "domain": "robotics", "actor": ["unitree", "amazon"], "score": "$650k / 500 kg",
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-05-11-an-autonomous-vehicle-that-powers-the-front-line"]},
        {"id": "2026-05-12-transformer-demand-up-274-percent",
         "title": "Transformer demand rises 274% with four-year lead times",
         "claim": "Demand for generator step-up transformers has surged 274% since 2019 with "
                  "lead times stretching to four years, while Ford pivoted to US-assembled "
                  "battery storage by 2027 and federal agencies launched an initiative for small "
                  "modular reactors on commercial shipping vessels.",
         "domain": "energy", "actor": ["ford-motor", "marad"], "score": "+274% / 4-year lead",
         "evidences": ["infrastructure-crowding-out", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-11-two-billion-of-ratepayer-grid-upgrades"]},
        {"id": "2026-05-12-an-orbital-gpu-cluster-by-2027",
         "title": "A space startup raises $275M for orbital GPUs and power beaming",
         "claim": "Cowboy Space Corporation raised $275 million at a $2 billion valuation to "
                  "build low-orbit infrastructure for the AI era with space-to-Earth power "
                  "beaming this year and an orbital GPU cluster by 2027, while SpaceX completed "
                  "a Starship V3 launch rehearsal and prediction markets projected its listing "
                  "above $2.2 trillion.",
         "domain": "space", "actor": ["cowboy-space", "spacex"], "score": "$275M / $2.2T",
         "evidences": ["orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-11-a-trademark-for-orbital-datacenters"]},
        {"id": "2026-05-12-pleasure-becomes-a-knob",
         "title": "Researchers pinpoint the circuit that new drugs use to suppress hedonic eating",
         "claim": "Researchers pinpointed for the first time the central amygdala circuit that "
                  "next-generation GLP-1 drugs inhibit to suppress hedonic eating, reducing "
                  "dopamine release to isolate reward without abolishing it.",
         "domain": "biotech",
         "evidences": ["hardware-grade-biology", "intimate-interface"],
         "supersedes": [B + "developments/2026-05-11-a-foundation-model-for-alzheimers-prevention"]},
        {"id": "2026-05-12-employees-automate-fake-ai-tasks",
         "title": "Employees automate fake AI tasks to hit token-consumption targets",
         "claim": "Amazon employees are reportedly using an internal tool to automate fake AI "
                  "tasks purely to hit token-consumption targets on internal leaderboards.",
         "domain": "economics", "actor": ["amazon"],
         "evidences": ["gaming-the-token-metric", "compute-as-compensation", "coordination-tax"],
         "supersedes": [B + "developments/2026-03-22-tokenmaxxing-leaderboards"],
         "body": "Perk in March, metric in March, scoreboard in March, and now the scoreboard "
                 "is being gamed by the people it measures."},
        {"id": "2026-05-12-humanities-graduates-boo-the-speaker",
         "title": "Humanities graduates boo a speaker calling AI the next industrial revolution",
         "claim": "University of Central Florida humanities graduates loudly booed a "
                  "commencement speaker for calling AI the next industrial revolution.",
         "domain": "society",
         "evidences": ["violence-arrives", "work-displaced"],
         "supersedes": [B + "developments/2026-05-11-women-hold-most-of-the-exposed-jobs"]},
        {"id": "2026-05-12-spy-agencies-muscle-in-on-model-evaluation",
         "title": "Spy agencies move in on pre-release model evaluation",
         "claim": "US intelligence agencies are reportedly muscling in on the Commerce "
                  "Department over pre-release frontier model evaluations, while South Korea's "
                  "Kim Yong-beom proposed a national dividend to redistribute AI's excess "
                  "profits.",
         "domain": "policy", "actor": ["state-department"],
         "evidences": ["politics-as-infrastructure", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-05-09-three-weeks-replaces-a-year-of-pen-testing"]},
    ],
}
