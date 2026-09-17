"""Issue 188 — 2026-08-17. The frontier fits in 17 gigabytes."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-17-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-17", "title": "Welcome to August 17, 2026", "url": URL,
        "thesis": "Frontier capability arrives in a file you can keep.",
        "body": """
# Welcome to August 17, 2026

The frontier now fits in a 17GB file. Alibaba's Apache-licensed Qwen3.8-27B
became the first local model to score frontier capability on the intelligence
index, matching DeepSeek V4-Pro and GPT-5.6 Luna, and capably drives a coding
agent from a laptop.

Meanwhile a tracking device hidden in a shipment of rare books ended its journey
at a facility where the books are scanned for training data and destroyed.
""",
    },
    "themes": [
        {"id": "the-corpus-consumed", "type": "Theme",
         "title": "The source material is destroyed in the reading",
         "first_seen": "2026-08-17", "domain": "society",
         "body": "Training corpora are assembled by consuming their originals — books "
                 "scanned then pulped, archives bought from bankruptcies, local news "
                 "funded in exchange for the right to train on it. The knowledge "
                 "survives as weights; the artifact does not."},
    ],
    "organizations": [
        {"id": "spirit-airlines", "type": "Organization", "title": "Spirit Airlines"},
        {"id": "sb-energy", "type": "Organization", "title": "SB Energy"},
        {"id": "axios", "type": "Organization", "title": "Axios"},
        {"id": "karlsruhe", "type": "Organization", "title": "Karlsruhe Institute of Technology"},
    ],
    "developments": [
        {"id": "2026-08-17-the-frontier-in-a-seventeen-gigabyte-file",
         "title": "A local model reaches frontier capability in a 17GB file",
         "claim": "Alibaba's Apache-licensed Qwen3.8-27B became the first local model to score "
                  "frontier capability on the Artificial Analysis index, matching DeepSeek V4-Pro "
                  "and GPT-5.6 Luna in a 17-gigabyte file, capably driving a coding agent from a "
                  "laptop, though its highest reasoning mode once spent 21 minutes contemplating "
                  "a single image.",
         "domain": "models", "actor": ["alibaba", "deepseek", "openai", "artificial-analysis"],
         "score": "17 GB",
         "evidences": ["open-weights-take-the-crown", "intelligence-per-watt", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-08-16-three-billion-downloads-and-a-hundred-fifty-thousand-derivatives"]},
        {"id": "2026-08-17-automated-coders-around-late-2027",
         "title": "Three methods converge on automated coders around late 2027",
         "claim": "The AI Futures Project's updated timelines found new coding-uplift and revenue "
                  "methods converging with time-horizon analysis on automated coders around late "
                  "2027, with reality tracking its scenario at 70 to 90% speed.",
         "domain": "models", "actor": ["ai-futures-project"], "score": "late 2027 / 70-90% speed",
         "evidences": ["takeoff-declared", "r-and-d-evals-saturated", "a-model-trains-a-model"],
         "supersedes": [B + "developments/2026-08-15-the-r-and-d-evals-have-saturated"]},
        {"id": "2026-08-17-books-scanned-then-destroyed",
         "title": "A tracker follows rare books to a facility that scans and destroys them",
         "claim": "A tracking device hidden in a shipment of rare books ended its journey at a Las "
                  "Vegas facility where Amazon is buying books en masse, scanning them for "
                  "training data and destroying them, while Google won a bankruptcy auction for "
                  "7.5 billion airline passenger records for $10 million.",
         "domain": "society", "actor": ["amazon", "google", "spirit-airlines"],
         "score": "7.5B records for $10M",
         "evidences": ["the-corpus-consumed", "data-beyond-text", "understanding-as-the-scarce-good"],
         "supersedes": [B + "developments/2026-08-16-contractors-cold-email-startups-for-old-slack-threads"]},
        {"id": "2026-08-17-a-watermark-called-a-perversion-of-writing",
         "title": "A critic calls mandated text watermarking a perversion of writing",
         "claim": "John Gruber called the EU-mandated steganographic watermarking of Claude text a "
                  "perversion of writing, since it nudges the model away from its best words and "
                  "only the lab holds the detection keys.",
         "domain": "society", "actor": ["anthropic", "european-union"],
         "evidences": ["legislating-the-shift", "the-corpus-consumed", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-08-16-a-watermark-in-the-randomness-between-equal-words"]},
        {"id": "2026-08-17-an-antifragile-hundred-billion-dollar-bet",
         "title": "A fab is framed as a bet that pays off however a geopolitical question resolves",
         "claim": "Terafab is confirmed to target 2-nanometer-class AI chips and will produce "
                  "memory under the same roof with DRAM prices up three to fourfold and demand "
                  "outrunning supply tenfold, framed as an antifragile $100 billion bet that pays "
                  "off whether or not Taiwan's status changes.",
         "domain": "compute", "actor": ["spacex", "taiwan"], "score": "$100B / 2 nm",
         "evidences": ["silicon-curtain", "compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2026-08-08-a-particle-accelerator-as-a-light-utility"]},
        {"id": "2026-08-17-three-trillion-in-off-balance-sheet-commitments",
         "title": "Nine tech giants carry $3 trillion in off-balance-sheet AI commitments",
         "claim": "Nine tech giants now carry $3 trillion in off-balance-sheet AI commitments, "
                  "five times their annual capital expenditure, as chipmakers poured over $250 "
                  "billion into startup financings this year and up to $105 billion backed an "
                  "Ohio campus under a ten-gigawatt lease its financier insists is not circular.",
         "domain": "economics", "actor": ["nvidia", "openai", "softbank", "sb-energy"],
         "score": "$3T / 5x capex",
         "evidences": ["debt-funded-buildout", "bottlenecks-arbitraged-instantly", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-15-a-dollar-buys-forty-nine-percent-more-compute-each-year"]},
        {"id": "2026-08-17-the-defenders-window",
         "title": "A lab president calls this the defender's window before an open cyber model drops",
         "claim": "OpenAI's Greg Brockman called this the defender's window and urged security "
                  "teams to unleash AI agents on old flaws before a near-frontier open-weight "
                  "cyber model drops at month's end, while Karlsruhe researchers showed ordinary "
                  "WiFi signals can image and identify people within seconds.",
         "domain": "compute", "actor": ["openai", "karlsruhe"],
         "evidences": ["war-reaches-the-cloud", "open-weights-take-the-crown", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-08-15-a-cyber-model-matches-the-frontier-at-finding-flaws"]},
        {"id": "2026-08-17-ai-becomes-a-major-election-issue",
         "title": "AI becomes a major American election issue for the first time",
         "claim": "AI became a major American election issue for the first time, staked out in "
                  "nearly 40% of races and outranking foreign policy and manufacturing, while "
                  "over 20 jurisdictions moved to cancel license-plate-reader contracts in July "
                  "alone.",
         "domain": "policy", "score": "~40% of races",
         "evidences": ["politics-as-infrastructure", "agent-exclusion", "work-displaced"],
         "supersedes": [B + "developments/2026-08-16-eighty-four-percent-excited-against-thirty-eight"]},
        {"id": "2026-08-17-a-robot-outruns-every-human-alive",
         "title": "A robot developed in three months out-jumps and outruns every human alive",
         "claim": "Unitree's new robot, three months in development, out-jumps and outruns every "
                  "human alive, while Uber and Zipline target a million drone deliveries a day "
                  "for what they call insatiable demand.",
         "domain": "robotics", "actor": ["unitree", "uber", "zipline"], "score": "1M deliveries/day",
         "evidences": ["physical-recursion", "humans-need-not-apply", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-08-16-the-strictest-humanoid-permitting-regime"]},
        {"id": "2026-08-17-the-diagnostic-odyssey-compressed-to-minutes",
         "title": "Rare diseases are flagged in minutes rather than a five-year odyssey",
         "claim": "AI is lapping the five-year diagnostic odyssey, flagging rare diseases in "
                  "minutes via face-reading apps and ECG algorithms, a speedup one executive said "
                  "would have shortened her own.",
         "domain": "biotech", "score": "5 years to minutes",
         "evidences": ["hardware-grade-biology", "longevity-escape-velocity", "automated-science"],
         "supersedes": [B + "developments/2026-08-15-organoids-to-replace-animal-testing"]},
        {"id": "2026-08-17-a-run-rate-past-sixty-five-billion",
         "title": "A lab's run rate passes $65 billion, up sevenfold in seven months",
         "claim": "Anthropic's run rate passed $65 billion, up sevenfold in seven months and "
                  "ahead of OpenAI's reported $40 billion, teeing up a fall IPO, while Stripe paid "
                  "over $7 billion for the tollbooth to more than 400 models.",
         "domain": "economics", "actor": ["anthropic", "openai", "stripe", "openrouter"],
         "score": "$65B run rate",
         "evidences": ["ai-as-the-economy", "routing-around-the-ban", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-15-revenue-up-fourteen-fold-with-positive-operating-income"]},
        {"id": "2026-08-17-saving-local-news-by-consuming-it",
         "title": "A lab bankrolls local newsletters in exchange for training on the coverage",
         "claim": "OpenAI is bankrolling 13 local newsletters in exchange for training on the "
                  "coverage, saving local news by consuming it, as San Francisco's median home "
                  "hit $1.7 million with pending IPO windfalls theoretically able to buy 29% of "
                  "the metro.",
         "domain": "economics", "actor": ["openai", "axios"], "score": "$1.7M median home",
         "evidences": ["the-corpus-consumed", "ai-as-the-economy", "work-displaced"],
         "supersedes": [B + "developments/2026-08-17-books-scanned-then-destroyed"]},
    ],
}
