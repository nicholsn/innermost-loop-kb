"""Issue 074 — 2026-03-12. A benchmark for self-improvement."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-12", "title": "Welcome to March 12, 2026", "url": URL,
        "thesis": "Self-improvement gets a leaderboard, and reasoning gets a thousand times cheaper.",
        "body": """
# Welcome to March 12, 2026

PostTrainBench v1.0 evaluates whether agents can automate their own
post-training. Opus 4.6 with Claude Code came first. The corpus recorded a
leaderboard for models post-training models in December; now it has a version
number.

Altman says a hard reasoning problem has become a thousand times cheaper to
solve in the sixteen months since o1.
""",
    },
    "themes": [
        {"id": "compute-as-compensation", "type": "Theme",
         "title": "Access to compute becomes part of the package",
         "first_seen": "2026-03-12", "domain": "economics",
         "body": "Compute budgets negotiated alongside salary, bonus and equity; token usage "
                 "tracked per employee. What a worker can spend on inference becomes both a "
                 "perk and a performance metric."},
    ],
    "organizations": [
        {"id": "att", "type": "Organization", "title": "AT&T",
         "resource": "https://www.att.com/"},
        {"id": "nebius", "type": "Organization", "title": "Nebius",
         "resource": "https://nebius.com/"},
        {"id": "atlassian", "type": "Organization", "title": "Atlassian",
         "resource": "https://www.atlassian.com/"},
        {"id": "anthropic-institute", "type": "Organization", "title": "Anthropic Institute",
         "body": "Led by Jack Clark; guides public understanding of the transition."},
        {"id": "princeton-univ", "type": "Organization", "title": "Princeton University",
         "resource": "https://www.princeton.edu/"},
        {"id": "zoox", "type": "Organization", "title": "Zoox",
         "resource": "https://zoox.com/"},
    ],
    "developments": [
        {"id": "2026-03-12-posttrainbench-v1",
         "title": "A benchmark measures whether agents can post-train themselves",
         "claim": "PostTrainBench v1.0 evaluated whether language model agents can automate "
                  "their own post-training for recursive self-improvement, finding Claude Opus "
                  "4.6 with Claude Code the most capable such agent.",
         "domain": "benchmarks", "actor": ["anthropic"],
         "evidences": ["recursive-self-improvement", "benchmark-saturation"],
         "supersedes": [B + "developments/2025-12-18-posttrainbench-models-training-models"]},
        {"id": "2026-03-12-reasoning-1000x-cheaper-in-16-months",
         "title": "Hard reasoning gets a thousand times cheaper in sixteen months",
         "claim": "Sam Altman revealed that solving a hard reasoning problem has become a "
                  "thousand times cheaper in the sixteen months since o1, comparing it to "
                  "GPT-5.4.",
         "domain": "economics", "actor": ["openai", "people/sam-altman"], "score": "1000x / 16 months",
         "evidences": ["reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-02-13-arc-agi-1-price-collapses-400x"]},
        {"id": "2026-03-12-nemotron-3-super-no-wall",
         "title": "Nvidia sees no wall in post-training and opens a 120B model",
         "claim": "Nvidia said it sees no wall in post-training and announced Nemotron 3 Super, "
                  "a 120-billion-parameter hybrid model with 12 billion active parameters, "
                  "released with permissive licensing, open data and open training "
                  "infrastructure.",
         "domain": "models", "actor": ["nvidia"], "score": "120B / 12B active",
         "evidences": ["open-weight-latency", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-03-08-nanogpt-86s"]},
        {"id": "2026-03-12-vulnerabilities-in-forty-year-old-code",
         "title": "A model finds new vulnerabilities in forty-year-old Apple II code",
         "claim": "Opus 4.6 found new vulnerabilities in Apple II code from forty years ago, "
                  "extending AI security auditing across the full history of computing.",
         "domain": "agents", "actor": ["anthropic"], "score": "40 years",
         "evidences": ["automated-science", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-03-10-agents-review-every-pull-request"]},
        {"id": "2026-03-12-codex-passes-1b-arr",
         "title": "Codex passes a billion in annual run rate",
         "claim": "OpenAI's Codex passed $1 billion in annual run-rate revenue by the end of "
                  "January, and the company plans to bring Sora video generation inside "
                  "ChatGPT, while Anthropic added a side-chain command to Claude Code for "
                  "talking while the agent works.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "$1B ARR",
         "evidences": ["compute-capital-stack", "engineer-as-supervisor"]},
        {"id": "2026-03-12-amazon-enjoins-an-agentic-browser",
         "title": "Amazon wins an injunction against an agentic browser",
         "claim": "Amazon won a temporary injunction against Perplexity's Comet AI browser, "
                  "while YouTube expanded likeness detection to officials and journalists and "
                  "China restricted agent apps at state enterprises over security risks.",
         "domain": "policy", "actor": ["amazon", "perplexity", "youtube", "china"],
         "evidences": ["agent-exclusion", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-09-courts-hold-bots-are-not-human"]},
        {"id": "2026-03-12-whole-cell-simulated-in-4d",
         "title": "A minimal cell is brought to life in four dimensions on a computer",
         "claim": "A consortium published a whole-cell spatial and kinetic model bringing a "
                  "genetically minimal cell to life in four dimensions on a computer, "
                  "simulating genetic processes, metabolism, growth and division across an "
                  "entire cell cycle, while Princeton released a library of 206 agentic skills "
                  "for autonomous biomedical research.",
         "domain": "biotech", "actor": ["princeton-univ"], "score": "206 skills",
         "evidences": ["hardware-grade-biology", "automated-science", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-03-05-evo-2-designs-bacteriophages"]},
        {"id": "2026-03-12-a-possible-open-problem-solution",
         "title": "Epoch investigates an apparent solution to an open problem",
         "claim": "Epoch AI is investigating an apparent GPT-5.4 Pro solution to a problem from "
                  "FrontierMath Open Problems, which would be unprecedented, and guesses the "
                  "solution is right.",
         "domain": "science", "actor": ["epoch-ai", "openai"],
         "evidences": ["automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-03-06-novel-observations-on-open-problems"]},
        {"id": "2026-03-12-att-commits-250b",
         "title": "A telco commits $250B to network buildout",
         "claim": "AT&T committed more than $250 billion over five years to expand US network "
                  "infrastructure and hire thousands of technicians, while Nvidia is investing "
                  "$2 billion in Nebius to deploy over 5 GW of systems by 2030.",
         "domain": "compute", "actor": ["att", "nvidia", "nebius"], "score": "$250B / 5 GW",
         "evidences": ["compute-capital-stack", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-03-10-amazon-bond-sale-40b"]},
        {"id": "2026-03-12-homomorphic-encryption-5000x",
         "title": "Intel accelerates fully homomorphic encryption five thousandfold",
         "claim": "Intel demonstrated Heracles, accelerating fully homomorphic encryption five "
                  "thousand times over top server CPUs, while Meta prepared four new AI chip "
                  "generations by end of 2027 and Apple's folding iPhone will open into a "
                  "tablet interface.",
         "domain": "compute", "actor": ["intel", "meta", "apple"], "score": "5,000x",
         "evidences": ["vertical-silicon"],
         "supersedes": [B + "developments/2026-03-10-apple-makes-a-quarter-of-iphones-in-india"]},
        {"id": "2026-03-12-compute-is-the-fourth-line-item",
         "title": "Compute becomes the fourth line item in a pay package",
         "claim": "Tech job candidates now ask about AI compute budgets, with compute becoming "
                  "the fourth line item in Silicon Valley pay packages after salary, bonus and "
                  "equity, while Atlassian cut 10% of its workforce to self-fund AI investment.",
         "domain": "economics", "actor": ["atlassian"], "score": "-1,600 jobs",
         "evidences": ["compute-as-compensation", "work-displaced"],
         "supersedes": [B + "developments/2026-03-09-block-accused-of-ai-washing"]},
        {"id": "2026-03-12-anthropic-institute-launches",
         "title": "Anthropic launches an institute to guide the public through the transition",
         "claim": "Anthropic launched the Anthropic Institute led by cofounder Jack Clark, "
                  "predicting far more dramatic progress in the next two years and aiming to "
                  "guide the public through the transition to more powerful systems.",
         "domain": "society", "actor": ["anthropic-institute", "people/jack-clark"],
         "evidences": ["takeoff-declared", "values-negotiated-with-the-model"]},
        {"id": "2026-03-12-moon-factory-under-5000-dollars",
         "title": "A Moon factory is built for under five thousand dollars",
         "claim": "GRU Space built what it calls the world's first Moon Factory for under "
                  "$5,000, capable of autonomously mining lunar regolith and turning it into "
                  "structural bricks, while NASA's administrator said he is more than 90% "
                  "confident Mars samples contain evidence of microbial life.",
         "domain": "space", "actor": ["gru-space", "nasa"], "score": "<$5,000 / >90%",
         "evidences": ["industrialized-nature", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-03-08-dart-moved-two-asteroids-around-the-sun"]},
    ],
}
