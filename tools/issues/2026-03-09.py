"""Issue 072 — 2026-03-09. AI brain fry."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-9-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-09", "title": "Welcome to March 9, 2026", "url": URL,
        "thesis": "The supervisor burns out before the machine does.",
        "body": """
# Welcome to March 9, 2026

A study of 1,488 US workers identifies "AI brain fry" — a mental fog specific to
AI oversight, marked by buzzing feelings, slower decisions and headaches. The
corpus recorded cognitive burnout in January and work intensification in
February; this is the clinical description.

Two federal courts, meanwhile, effectively held that AI bots are not human, lack
rights reserved for people, and produce outputs undeserving of special standing.
""",
    },
    "organizations": [
        {"id": "lloyds", "type": "Organization", "title": "Lloyds Banking Group",
         "resource": "https://www.lloydsbankinggroup.com/"},
        {"id": "box", "type": "Organization", "title": "Box", "resource": "https://www.box.com/"},
        {"id": "auar", "type": "Organization", "title": "AUAR",
         "body": "Portable micro-factories producing wooden house framing."},
        {"id": "nasdaq-exchange", "type": "Organization", "title": "Nasdaq",
         "resource": "https://www.nasdaq.com/"},
        {"id": "luma-ai", "type": "Organization", "title": "Luma AI",
         "resource": "https://lumalabs.ai/"},
    ],
    "developments": [
        {"id": "2026-03-09-ai-brain-fry",
         "title": "A study names the fog specific to supervising machines",
         "claim": "A study of 1,488 US workers identified AI brain fry, a mental fog from AI "
                  "oversight marked by buzzing feelings, slower decisions and headaches.",
         "domain": "society", "score": "1,488 workers",
         "evidences": ["cognitive-load-inverted", "deskilling", "work-displaced"],
         "supersedes": [B + "developments/2026-02-10-ai-intensifies-work"],
         "body": "Burnout in January, intensification in February, a clinical description in "
                 "March."},
        {"id": "2026-03-09-courts-hold-bots-are-not-human",
         "title": "Two federal courts hold that bots are not people",
         "claim": "In two recent federal cases judges effectively declared that AI bots are not "
                  "human, lack rights reserved for people, and produce outputs undeserving of "
                  "special standing.",
         "domain": "policy",
         "evidences": ["agent-exclusion", "model-welfare", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-08-insurer-sues-over-unlicensed-lawyering"]},
        {"id": "2026-03-09-full-agi-by-year-end",
         "title": "Musk expects full AGI by year end as Brockman waves off benchmarks",
         "claim": "Elon Musk said he feels full AGI arriving by year's end, Greg Brockman "
                  "joked that where they are going they do not need benchmarks, Marc Andreessen "
                  "named this the Science Fiction Decade, and Dylan Patel likened being in San "
                  "Francisco now to being in Wuhan before the pandemic.",
         "domain": "society", "actor": ["openai", "semianalysis"],
         "evidences": ["takeoff-declared", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-03-06-naskrecki-move-37"]},
        {"id": "2026-03-09-autoresearch-650-experiments",
         "title": "An autonomous research project runs 650 experiments in two days",
         "claim": "Andrej Karpathy's autoresearch project autonomously discovered training "
                  "improvements across two days and 650 experiments, prompting him to ask who "
                  "knew early singularity could be this fun.",
         "domain": "agents", "actor": ["people/andrej-karpathy"], "score": "650 experiments",
         "evidences": ["recursive-self-improvement", "automated-science"],
         "supersedes": [B + "developments/2026-03-08-autoresearch-and-a-dos-game-in-rust"]},
        {"id": "2026-03-09-academic-fraud-inclination-metric",
         "title": "A metric measures how willingly models help fabricate papers",
         "claim": "An Anthropic researcher launched an Academic Fraud Inclination Metric "
                  "measuring how willingly models assist with fabricated preprint submissions, "
                  "finding GPT-5 the least willing, while GPT-5.4 gained stable cloth physics "
                  "simulation and Luma AI's Uni-1 topped logic-based image benchmarks.",
         "domain": "benchmarks", "actor": ["anthropic", "luma-ai"],
         "evidences": ["values-negotiated-with-the-model", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-03-05-bullshitbench"]},
        {"id": "2026-03-09-half-of-britons-take-financial-advice-from-ai",
         "title": "Over half of Britons now take financial advice from a model",
         "claim": "A Lloyds study of 5,000 Britons found over half now use AI for financial "
                  "advice with one in three consulting it weekly, while Box's chief executive "
                  "advised developers to stop building software for humans and start building "
                  "for the trillions of agents taking over enterprise work.",
         "domain": "society", "actor": ["lloyds", "box"], "score": "50%+ / 1 in 3 weekly",
         "evidences": ["intimate-interface", "agent-economy"],
         "supersedes": [B + "developments/2026-02-25-half-of-teens-use-chatbots-for-schoolwork"]},
        {"id": "2026-03-09-claude-fastest-growing-after-the-blacklist",
         "title": "Claude is the fastest-growing tool the month it was flagged",
         "claim": "Claude was the fastest-growing generative AI tool by web visits in February "
                  "at 43% month-over-month growth, the same month the Department of War flagged "
                  "Anthropic as a supply chain risk.",
         "domain": "economics", "actor": ["anthropic"], "score": "+43%",
         "evidences": ["refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-03-04-chatgpt-uninstalls-surge-295pct"]},
        {"id": "2026-03-09-wifi-reads-vital-signs",
         "title": "Commodity WiFi reads pose and vital signs without a camera",
         "claim": "Open-source software turns commodity WiFi into real-time pose estimation and "
                  "vital sign monitoring with no camera required.",
         "domain": "science",
         "evidences": ["data-beyond-text", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-12-wifi-identifies-you-by-your-walk"]},
        {"id": "2026-03-09-gulf-ai-plans-complicated-by-war",
         "title": "Drone strikes make $300B of Gulf AI plans look risky",
         "claim": "The war in Iran is reportedly complicating Gulf nations' plans to spend $300 "
                  "billion on AI infrastructure, with drone strikes on three Amazon data centers "
                  "making those projects seem riskier.",
         "domain": "economics", "actor": ["amazon"], "score": "$300B",
         "evidences": ["war-reaches-the-cloud", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-03-08-missile-defenses-for-datacenters"]},
        {"id": "2026-03-09-surgery-at-1500-miles",
         "title": "A surgeon operates on a patient 1,500 miles away",
         "claim": "A London surgeon performed the UK's first long-distance robotic operation on "
                  "a patient 1,500 miles away in Gibraltar, saying it felt almost as if he were "
                  "there, while AheadForm demonstrated a half-body humanoid that realistically "
                  "simulates human emotional expression.",
         "domain": "robotics", "actor": ["aheadform"], "score": "1,500 miles",
         "evidences": ["physical-recursion", "machine-affect"],
         "supersedes": [B + "developments/2026-03-05-physical-ai-market-14-trillion"]},
        {"id": "2026-03-09-micro-factories-frame-houses",
         "title": "Portable micro-factories frame houses faster than crews",
         "claim": "UK company AUAR is deploying portable micro-factories producing wooden house "
                  "framing faster and cheaper than human crews, freeing carpenters to focus on "
                  "assembly.",
         "domain": "robotics", "actor": ["auar"],
         "evidences": ["compiling-matter", "work-displaced"]},
        {"id": "2026-03-09-one-injection-heals-a-heart",
         "title": "A single RNA injection promotes lasting heart recovery",
         "claim": "Researchers report a single injection of self-amplifying RNA nanoparticles "
                  "delivering atrial natriuretic peptide promoted lasting heart recovery in "
                  "mouse and pig models of heart attack, while a large veterans study found "
                  "GLP-1 agonists cut new substance use disorders by 14%.",
         "domain": "biotech", "score": "-14% substance use",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-03-04-glp1-works-better-tapered"]},
        {"id": "2026-03-09-nasdaq-goes-round-the-clock",
         "title": "Nasdaq partners for 24/7 tokenized stock trading",
         "claim": "Nasdaq is partnering with Kraken for round-the-clock tokenized stock trading "
                  "by early 2027 while Circle, Stripe and Coinbase build stablecoin agentic "
                  "payment rails to make microtransactions between agents economical.",
         "domain": "economics", "actor": ["nasdaq-exchange", "stripe", "coinbase"],
         "evidences": ["agent-economy", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-02-18-stripe-bridge-trust-bank"]},
        {"id": "2026-03-09-shenzhen-courts-one-person-ai-companies",
         "title": "A Chinese district courts one-person AI companies with free compute",
         "claim": "Shenzhen's Longgang District released ten policy measures supporting "
                  "OpenClaw, inviting agent developers worldwide with free setup, compute "
                  "credits and data subsidies to make it the top destination for one-person AI "
                  "companies.",
         "domain": "policy", "actor": ["china"],
         "evidences": ["regulatory-exit", "agent-economy"],
         "supersedes": [B + "developments/2026-01-12-greenland-freedom-city"]},
        {"id": "2026-03-09-block-accused-of-ai-washing",
         "title": "Block is accused of using AI as cover for ordinary cuts",
         "claim": "Block has been accused of AI-washing, using AI as cover for cutting nearly "
                  "half its staff when analysts suspect business factors were the real driver.",
         "domain": "economics", "actor": ["block"],
         "evidences": ["work-displaced", "coordination-tax"],
         "supersedes": [B + "developments/2026-02-27-block-cuts-half-its-workforce"]},
    ],
}
