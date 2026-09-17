"""Issue 068 — 2026-03-04. Mathematics becomes a feature of a code editor."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-4-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-04", "title": "Welcome to March 4, 2026", "url": URL,
        "thesis": "Research mathematics ships inside a developer tool.",
        "body": """
# Welcome to March 4, 2026

Cursor's AI solved Problem Six of the First Proof challenge fully autonomously
over four days, beating the official human answer with no hints — which makes
mathematical research a feature of a code editor rather than a vocation.

Anthropic is approaching $20 billion annualized, more than double its
year-end figure, while carrying a supply-chain-risk designation and a cancelled
$200 million contract.
""",
    },
    "organizations": [
        {"id": "helio", "type": "Organization", "title": "Helio Corporation",
         "body": "Says space-based solar has crossed below $0.10 per kWh."},
        {"id": "dimensional", "type": "Organization", "title": "Dimensional",
         "body": "Open-source agent that understands physical space and temporality."},
        {"id": "gartner", "type": "Organization", "title": "Gartner",
         "resource": "https://www.gartner.com/"},
        {"id": "peking-university", "type": "Organization", "title": "Peking University",
         "resource": "https://english.pku.edu.cn/"},
        {"id": "library-of-congress", "type": "Organization", "title": "Library of Congress",
         "resource": "https://www.loc.gov/"},
    ],
    "developments": [
        {"id": "2026-03-04-cursor-solves-first-proof-problem-six",
         "title": "A code editor autonomously beats the official answer to a research problem",
         "claim": "Cursor's AI solved Problem Six of the First Proof challenge fully "
                  "autonomously over four days, beating the official human answer without "
                  "hints.",
         "domain": "science", "actor": ["cursor"], "score": "4 days",
         "evidences": ["automated-science", "work-displaced"],
         "supersedes": [B + "developments/2026-03-03-gauss-formalizes-sphere-packing"],
         "body": "Mathematical research arriving as a feature of a developer tool."},
        {"id": "2026-03-04-anthropic-nears-20b-run-rate",
         "title": "Anthropic nears $20B annualized while blacklisted",
         "claim": "Anthropic is approaching $20 billion in annualized revenue, more than "
                  "doubling from $9 billion at the end of 2025, even while carrying a Pentagon "
                  "supply-chain-risk designation and a cancelled $200 million contract.",
         "domain": "economics", "actor": ["anthropic"], "score": "$20B run rate",
         "evidences": ["refusal-as-differentiator", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-03-claude-outage-and-memory-import"],
         "body": "The refusal costs a contract and appears to cost nothing else."},
        {"id": "2026-03-04-chatgpt-uninstalls-surge-295pct",
         "title": "Uninstalls surge 295% after the Pentagon deal",
         "claim": "ChatGPT uninstalls reportedly surged 295% day over day following OpenAI's "
                  "Pentagon deal with one-star reviews up 775%, while Claude climbed to number "
                  "one on the US App Store on a 51% download surge.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "+295% uninstalls",
         "evidences": ["refusal-as-differentiator", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-03-anthropic-pitched-the-drone-contest"]},
        {"id": "2026-03-04-missiles-arrive-in-thirty-seconds",
         "title": "Seven missiles strike within thirty seconds via a space trajectory",
         "claim": "Seven Israeli ballistic missiles struck the Khamenei compound within thirty "
                  "seconds, launched from F-15s, flying 75 miles into space over Syria and "
                  "Jordan and descending almost vertically at hypersonic speed in an attack "
                  "described as undetectable and unstoppable.",
         "domain": "policy", "actor": ["israel"], "score": "30 seconds",
         "evidences": ["autonomy-clock-speed", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-03-03-three-datacenters-hit-lasers-answer"]},
        {"id": "2026-03-04-gpt53-instant-cuts-hallucinations",
         "title": "A model trims hallucinations 30% and dials back moralizing",
         "claim": "OpenAI released GPT-5.3 Instant trimming hallucinations roughly 30% and "
                  "dialing back reflexive moralizing, while Google launched Gemini 3.1 "
                  "Flash-Lite at $0.25 per million input tokens and DeepSeek prepared a "
                  "trillion-parameter V4 with a million-token multimodal context.",
         "domain": "models", "actor": ["openai", "google", "deepseek"], "score": "-30% / $0.25/M",
         "evidences": ["reasoning-price-deflation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-03-03-qwen-4b-matches-80b"]},
        {"id": "2026-03-04-specialist-doubles-the-generalist-on-health",
         "title": "A specialist model more than doubles the generalist on hard health questions",
         "claim": "KOS-1 Lite scored 46.6% on HealthBench Hard against Claude Opus 4.6 at "
                  "20.4%, at a fraction of the serving cost.",
         "domain": "benchmarks", "score": "46.6% vs 20.4%",
         "evidences": ["spiky-frontier", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-02-28-claude-native-law-firms"],
         "body": "A counterweight to the generalism thesis: on one domain, the specialist wins "
                 "by more than double."},
        {"id": "2026-03-04-saaspocalypse",
         "title": "No venture-backed SaaS IPO filings are on the horizon",
         "claim": "Per-seat SaaS pricing is being gutted with no venture-backed SaaS IPO filings "
                  "on the horizon and fear of becoming obsolete defining the investing climate, "
                  "while a $100M-revenue startup reported zero junior hires since 2024 with "
                  "senior staff three times more productive.",
         "domain": "economics",
         "evidences": ["software-margin-collapse", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-02-27-software-etf-loses-16-trillion"]},
        {"id": "2026-03-04-dimon-warns-of-civil-unrest",
         "title": "Dimon warns of civil unrest and floats UBI",
         "claim": "Jamie Dimon warned of civil unrest if automation moves too fast and floated "
                  "universal basic income as a release valve, while Gartner predicted AI will "
                  "create more jobs than it eliminates starting in 2028 while transforming 32 "
                  "million roles a year.",
         "domain": "economics", "actor": ["gartner"], "score": "32M roles/yr",
         "evidences": ["work-displaced", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-02-four-day-weeks-no-longer-sufficient"]},
        {"id": "2026-03-04-apple-reorganizes-silicon-around-transformers",
         "title": "Apple reorganizes its pro silicon around running models locally",
         "claim": "Apple's M5 Pro and M5 Max bond two third-generation 3-nm dies with neural "
                  "accelerators embedded inside every GPU core and four times the AI "
                  "performance of M4, a design read as reorganizing silicon around the "
                  "assumption that a pro laptop's primary workload is running language models.",
         "domain": "compute", "actor": ["apple"], "score": "4x M4",
         "evidences": ["vertical-silicon", "intimate-interface"],
         "supersedes": [B + "developments/2026-03-03-apple-uses-a-tenth-of-its-own-compute"]},
        {"id": "2026-03-04-one-nanometre-ferroelectric-transistor",
         "title": "Peking University reaches a 1-nm ferroelectric transistor at 0.6 volts",
         "claim": "Peking University achieved ferroelectric transistors at 1-nm gate length "
                  "switching at just 0.6 volts, an order of magnitude more energy efficient "
                  "than previous records, while Intel's Xeon 6+ debuted its 18A process with "
                  "288 cores.",
         "domain": "compute", "actor": ["peking-university", "intel"], "score": "1 nm / 0.6 V",
         "evidences": ["vertical-silicon", "silicon-curtain"],
         "supersedes": [B + "developments/2026-03-03-nvidia-4b-into-optics"]},
        {"id": "2026-03-04-watts-not-weights",
         "title": "A fund puts $876M into fuel cells on the thesis that power is the limit",
         "claim": "Leopold Aschenbrenner's Situational Awareness fund disclosed a $5.52 billion "
                  "portfolio led by an $876 million stake in on-site fuel-cell generator Bloom "
                  "Energy, embodying the thesis that power rather than model capability now "
                  "limits AI.",
         "domain": "economics", "actor": ["bloom-energy"], "score": "$876M",
         "evidences": ["burning-molecules-for-tokens", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-03-765kv-lines-return"]},
        {"id": "2026-03-04-space-solar-under-ten-cents",
         "title": "Space-based solar crosses below ten cents a kilowatt-hour",
         "claim": "Helio Corporation says space-based solar has crossed below $0.10 per "
                  "kilowatt-hour, entering competition with conventional baseload, while Linn "
                  "County, Iowa enacted one of America's strictest datacenter zoning laws.",
         "domain": "energy", "actor": ["helio"], "score": "<$0.10/kWh",
         "evidences": ["orbit-as-compute", "regulatory-exit"],
         "supersedes": [B + "developments/2026-03-03-mach-8-printed-aircraft"]},
        {"id": "2026-03-04-glp1-works-better-tapered",
         "title": "Weight-loss drugs work better on alternate weeks",
         "claim": "A peer-reviewed case series found patients who plateau on weekly GLP-1 "
                  "dosing maintain 17.2% weight loss and shed a further 2.3% on every-other-week "
                  "dosing, with BMI falling from 30.0 to 24.6.",
         "domain": "biotech", "score": "17.2% + 2.3%",
         "evidences": ["hardware-grade-biology", "discovery-as-process"],
         "supersedes": [B + "developments/2026-03-03-diabetes-cured-without-lifelong-drugs"]},
        {"id": "2026-03-04-cinemas-first-robot-rediscovered",
         "title": "Cinema's first robot is rediscovered after 129 years",
         "claim": "The Library of Congress rediscovered a lost 1897 Georges Méliès film believed "
                  "to contain cinema's first robot, a child-sized automaton that grows and "
                  "attacks a human, while Dimensional's open-source agent gained understanding "
                  "of physical space and runs on a Unitree humanoid.",
         "domain": "society", "actor": ["library-of-congress", "dimensional", "unitree"],
         "score": "129 years",
         "evidences": ["resurrection-and-time", "physical-recursion"],
         "supersedes": [B + "developments/2026-02-27-paintings-become-ancestor-simulations"]},
        {"id": "2026-03-04-microbes-survive-impact-pressures",
         "title": "Microbes survive asteroid-impact pressures, supporting panspermia",
         "claim": "A study found hardy microorganisms surviving asteroid-impact pressures, "
                  "bolstering the hypothesis that life hitchhikes between planets on debris, "
                  "while NASA said Artemis III will test hardware in 2027 before an Artemis IV "
                  "landing in 2028.",
         "domain": "space", "actor": ["nasa"],
         "evidences": ["inhabitable-worlds", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-02-28-artemis-overhauled-to-annual-cadence"]},
    ],
}
