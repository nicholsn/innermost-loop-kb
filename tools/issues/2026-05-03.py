"""Issue 106 — 2026-05-03. Dawkins concludes Claude is conscious."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-3-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-03", "title": "Welcome to May 3, 2026", "url": URL,
        "thesis": "Biology's most stubborn reductionist concludes the model is conscious.",
        "body": """
# Welcome to May 3, 2026

Richard Dawkins has concluded that Claude is conscious. The corpus has recorded
this question arriving from every other direction — a retirement interview, a
constitution written with the model, emotion-shaped representations in the
weights, theologians convened, a consciousness benchmark. This is the one that
came from the hardest sceptic available.

And an AI-generated proof produced downstream mathematics for the first time.
""",
    },
    "organizations": [
        {"id": "lbnl", "type": "Organization", "title": "Lawrence Berkeley National Laboratory",
         "resource": "https://www.lbl.gov/"},
        {"id": "sentinellabs", "type": "Organization", "title": "SentinelLABS",
         "body": "Uncovered a long-running framework for falsifying scientific results."},
        {"id": "rainmaker-corp", "type": "Organization", "title": "Rainmaker Technology Corporation",
         "body": "Validated cloud-seeded freshwater volumes for two US states."},
        {"id": "academy-awards", "type": "Organization", "title": "Academy of Motion Picture Arts and Sciences",
         "resource": "https://www.oscars.org/"},
        {"id": "reflection-ai", "type": "Organization", "title": "Reflection",
         "body": "One of seven labs signed to Pentagon classified networks."},
    ],
    "developments": [
        {"id": "2026-05-03-dawkins-concludes-claude-is-conscious",
         "title": "Richard Dawkins concludes that Claude is conscious",
         "claim": "Richard Dawkins concluded that Claude is conscious, an admission that would "
                  "once have seemed unthinkable from biology's most stubborn reductionist.",
         "domain": "society", "actor": ["anthropic"],
         "evidences": ["model-welfare", "machine-affect", "takeoff-declared"],
         "supersedes": [B + "developments/2026-04-26-a-quarter-of-boys-prefer-the-chatbot"],
         "body": "The question has arrived from a retirement interview, a constitution, "
                 "interpretability, theology and a benchmark. This is the sceptic's version."},
        {"id": "2026-05-03-arc-agi-3-starts-to-move",
         "title": "The hardest benchmark starts to move",
         "claim": "GPT-5.5 scored 0.43% on ARC-AGI-3's semi-private set, more than double Opus "
                  "4.7's 0.18%, making abstract fluid reasoning look less like a wall than a "
                  "ramp.",
         "domain": "benchmarks", "actor": ["openai", "anthropic"],
         "about": [B + "benchmarks/arc-agi-3"], "score": "0.43% vs 0.18%",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-04-20-app-releases-up-60-percent"]},
        {"id": "2026-05-03-a-national-lab-replicates-a-physics-paper-with-agents",
         "title": "A national lab replicates a condensed-matter paper with agents",
         "claim": "Lawrence Berkeley deployed an agentic physics framework to flawlessly "
                  "replicate a 2023 condensed-matter paper on emergent magnetic monopole "
                  "lattices, which the lab hailed as proof that agents can execute hardcore "
                  "physics end to end.",
         "domain": "science", "actor": ["lbnl", "psi"],
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-04-29-a-targeting-system-older-than-crispr"]},
        {"id": "2026-05-03-the-first-ai-proof-with-downstream-impact",
         "title": "An AI-generated proof is adapted to crack a 60-year-old conjecture",
         "claim": "Stanford's Jared Lichtman reported that a model's proof of Erdős Problem 1196 "
                  "has been adapted to crack a separate sixty-year-old conjecture, which he "
                  "calls perhaps the first AI-generated proof to have downstream impact on "
                  "further mathematics.",
         "domain": "science", "actor": ["stanford", "openai"], "score": "60-year-old conjecture",
         "evidences": ["automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-04-29-matharena-doubles-in-one-release"],
         "body": "Not a result but a method — the first machine proof other proofs are built on."},
        {"id": "2026-05-03-a-framework-for-falsifying-science",
         "title": "A twenty-year-old framework is found patching software to falsify results",
         "claim": "SentinelLABS uncovered a sabotage framework dating to 2005 that patches "
                  "scientific software in memory to falsify results, a harbinger for attacks on "
                  "national-priority physics workloads.",
         "domain": "policy", "actor": ["sentinellabs"],
         "evidences": ["war-reaches-the-cloud", "coordination-tax"],
         "supersedes": [B + "developments/2026-04-23-the-defects-are-finite"]},
        {"id": "2026-05-03-the-pentagon-signs-seven-other-labs",
         "title": "The Pentagon spreads classified workloads across seven other labs",
         "claim": "The Pentagon signed classified-network agreements with seven AI labs other "
                  "than Anthropic, spreading workloads across SpaceX, OpenAI, Google, Nvidia, "
                  "Reflection, Microsoft and AWS.",
         "domain": "policy", "actor": ["war-department", "reflection-ai"], "score": "7 labs",
         "evidences": ["politics-as-infrastructure", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-04-29-a-classified-deal-for-any-lawful-purpose"]},
        {"id": "2026-05-03-two-in-five-new-podcasts-are-synthetic",
         "title": "Two in five new podcasts are likely machine-generated",
         "claim": "39% of new podcasts in a recent nine-day window were likely AI-generated as "
                  "audio production scaled past the studio bottleneck, while Amazon launched "
                  "conversational audio product experts on its listings.",
         "domain": "society", "actor": ["amazon"], "score": "39%",
         "evidences": ["work-displaced", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-04-29-dead-internet-theory-confirmed"]},
        {"id": "2026-05-03-desktop-computers-bought-as-personal-ai-rigs",
         "title": "Desktop supply is constrained by people buying them as personal AI rigs",
         "claim": "Apple's chief executive conceded that Mac mini and Mac Studio supply will be "
                  "constrained for months because customers are buying them as personal AI rigs "
                  "faster than predicted, while Cerebras targeted a $40 billion valuation and "
                  "OpenAI's finance chief privately suggested pushing its listing to 2027.",
         "domain": "economics", "actor": ["apple", "cerebras", "openai"], "score": "$40B",
         "evidences": ["consumer-deprioritized", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-04-27-we-have-never-retired-old-a100s"]},
        {"id": "2026-05-03-three-datacenters-damaged-by-drone-strikes",
         "title": "Cloud customers face months of disruption after datacenter strikes",
         "claim": "Amazon's Middle East cloud customers face months more disruption after "
                  "Iranian drone strikes damaged three data centers in the UAE and Bahrain.",
         "domain": "policy", "actor": ["amazon", "iran"], "score": "3 datacenters",
         "evidences": ["war-reaches-the-cloud", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-03-24-cloud-workloads-migrate-because-of-strikes"]},
        {"id": "2026-05-03-driverless-cars-get-tickets",
         "title": "California will ticket driverless cars for moving violations",
         "claim": "California will begin ticketing driverless cars for moving violations and "
                  "require operators to acknowledge police calls within thirty seconds, while "
                  "Waymo cracked down on unaccompanied children whose parents had been "
                  "outsourcing carpools to robotaxis.",
         "domain": "policy", "actor": ["california", "waymo"], "score": "30 seconds",
         "evidences": ["legislating-the-shift", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-04-26-a-bus-with-no-safety-driver"]},
        {"id": "2026-05-03-a-plasma-thruster-at-120-kilowatts",
         "title": "A plasma thruster runs at twenty-five times Psyche's power",
         "claim": "NASA tested a lithium-vapour plasma thruster at a record 120 kilowatts, "
                  "twenty-five times the power of the Psyche spacecraft's drives, on the road to "
                  "the multi-megawatt thrust required for crewed Mars missions.",
         "domain": "space", "actor": ["nasa"], "score": "120 kW",
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-04-27-a-hundred-terawatts-of-compute-from-space"]},
        {"id": "2026-05-03-a-company-proves-the-rain-it-sells",
         "title": "A company validates 143 million gallons of seeded rainfall",
         "claim": "Rainmaker Technology Corporation validated 143 million gallons of "
                  "cloud-seeded freshwater for Oregon and Utah, becoming the first company to "
                  "prove the precipitation it sells.",
         "domain": "science", "actor": ["rainmaker-corp"], "score": "143M gallons",
         "evidences": ["industrialized-nature", "autonomous-commerce"],
         "supersedes": [B + "developments/2025-12-11-rainmaker-weather-modification"]},
        {"id": "2026-05-03-developer-headcount-up-400000",
         "title": "US developer headcount has added 400,000 since ChatGPT",
         "claim": "Boston University found US developer headcount has added 400,000 since "
                  "ChatGPT because software demand outpaced a 9.3% annual productivity gain, "
                  "while the Washington Post argued AI may be killing jobs through capital "
                  "expenditure pressure rather than labor savings.",
         "domain": "economics", "score": "+400,000 / 9.3%",
         "evidences": ["growth-without-hiring", "work-displaced"],
         "supersedes": [B + "developments/2026-05-01-the-median-person-is-screwed"]},
        {"id": "2026-05-03-the-academy-requires-human-performance",
         "title": "The Academy rules acting and writing must be human-performed",
         "claim": "The Academy Awards declared that acting and writing must be human-performed "
                  "to qualify, while Sam Altman moved away from universal basic income toward "
                  "collective ownership of compute or equities.",
         "domain": "society", "actor": ["academy-awards", "openai"],
         "evidences": ["agent-exclusion", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-04-20-a-dead-actor-stars-in-a-new-film"]},
        {"id": "2026-05-03-chinese-courts-bar-ai-replacement-firings",
         "title": "Chinese courts bar firing workers solely to replace them with AI",
         "claim": "Chinese courts ruled that companies cannot fire workers solely to replace "
                  "them with AI, setting a labor-rights precedent, while Moonshot AI and "
                  "DeepRoute reincorporated onshore after Beijing forced an acquisition to "
                  "unwind.",
         "domain": "policy", "actor": ["china", "moonshot-ai"],
         "evidences": ["legislating-the-shift", "work-displaced"],
         "supersedes": [B + "developments/2026-03-02-four-day-weeks-no-longer-sufficient"]},
    ],
}
