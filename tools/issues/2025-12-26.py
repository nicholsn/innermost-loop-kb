"""Issue 016 — 2025-12-26. The yardstick snaps."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-26-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-26", "title": "Welcome to December 26, 2025", "url": URL,
        "thesis": "The yardstick has snapped.",
        "body": """
# Welcome to December 26, 2025

The ARC Prize Foundation declares ARC-AGI-1 and ARC-AGI-2 saturated — its own
tests can no longer bound the frontier — and moves the goalposts to Millennium
Problem complexity. Two days after a harness took ARC-AGI-2 to 75%, the
benchmark is retired. The next yardstick is not a human exam but the unsolved
limits of mathematics.

Meanwhile, in Beijing, Linkerbot humanoids assemble and test their own hands.
""",
    },
    "themes": [
        {"id": "benchmark-saturation", "type": "Theme",
         "title": "Benchmarks retire faster than they can be built",
         "first_seen": "2025-12-26", "domain": "benchmarks",
         "body": "Tests stop bounding the thing they measure and are abandoned by "
                 "their own authors. The replacement is not a harder exam but open "
                 "mathematics — measurement conceding to research."},
        {"id": "work-displaced", "type": "Theme",
         "title": "Measured displacement of knowledge work", "first_seen": "2025-12-26",
         "domain": "society",
         "body": "Not a forecast but a count: employment falling in a named "
                 "profession, with credible predictions that remote work as a "
                 "category follows."},
    ],
    "organizations": [
        {"id": "arc-prize", "type": "Organization", "title": "ARC Prize Foundation",
         "resource": "https://arcprize.org/", "body": "Publishes the ARC-AGI benchmarks."},
        {"id": "linkerbot", "type": "Organization", "title": "Linkerbot",
         "description": "Beijing dexterous-hand and humanoid maker whose robots were shown assembling and testing their own hands.",
         "resource": "https://www.linkerbot.cn/",
         "tags": ["startup"],
         "body": "Linkerbot (灵心巧手) is a Beijing robotics company that builds dexterous robotic hands and the "
                 "humanoids that carry them. Its single appearance in this corpus is the "
                 "[self-assembly loop](/developments/2025-12-26-linkerbot-self-assembly.md) in which its humanoids "
                 "assemble and test their own hands, the physical counterpart to the software recursion the newsletter "
                 "tracks under [physical recursion](/themes/physical-recursion.md)."},
        {"id": "bank-of-america", "type": "Organization", "title": "Bank of America",
         "resource": "https://www.bankofamerica.com/", "body": "Forecasts chip sector revenue."},
        {"id": "apple", "type": "Organization", "title": "Apple",
         "description": "Consumer-electronics and in-house-silicon giant that appears in this corpus mostly as the incumbent being displaced in the chip supply chain and as a late, outsourcing adopter of frontier models.",
         "resource": "https://www.apple.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q312"],
         "tags": ["big-tech"],
         "body": "Long TSMC's largest customer, Apple designs its own silicon and runs one of the largest installed device "
                 "bases in the world. In this corpus it is a foil rather than a frontier actor: "
                 "[NVIDIA displaces it as TSMC's top customer](/developments/2025-12-26-nvidia-displaces-apple-at-tsmc.md) "
                 "as the silicon food chain inverts toward datacenters, it "
                 "[puts Siri on Gemini](/developments/2026-01-13-apple-siri-on-gemini.md) rather than on a model of its own, "
                 "and it [pays more per phone](/developments/2026-02-03-apple-pays-57-more-per-iphone.md) as AI outbids it for memory."},
    ],
    "people": [
        {"id": "shane-legg", "type": "Person", "title": "Shane Legg", "name": "Shane Legg",
         "body": "DeepMind co-founder; predicted remote work vanishing within a decade."},
        {"id": "jurgen-schmidhuber", "type": "Person", "title": "Jürgen Schmidhuber",
         "name": "Jürgen Schmidhuber", "body": "Unveiled the PoPE positional embedding."},
    ],
    "developments": [
        {"id": "2025-12-26-arc-declares-saturation",
         "title": "ARC Prize declares its own benchmarks saturated",
         "claim": "The ARC Prize Foundation declared ARC-AGI-1 and ARC-AGI-2 saturated, saying "
                  "current tests can no longer bound frontier fluid intelligence, and moved "
                  "the target to Millennium Problem complexity.",
         "domain": "benchmarks", "actor": ["arc-prize"],
         "about": [B + "benchmarks/arc-agi-1", B + "benchmarks/arc-agi-2"],
         "evidences": ["benchmark-saturation", "root-node-problems"],
         "supersedes": [B + "developments/2025-12-24-poetiq-harness-arc-agi-2"],
         "body": "Two days after a harness reached 75%, the test is retired by its authors. "
                 "The replacement is open mathematics."},
        {"id": "2025-12-26-linkerbot-self-assembly",
         "title": "Linkerbot humanoids assemble and test their own hands",
         "claim": "In Beijing, Linkerbot humanoids are assembling and testing their own hands, "
                  "closing a loop of robotic self-replication.",
         "description": "The newsletter's first sighting of robots building robots rather than what "
                        "powers them: the robot builds the part of itself that does the building, which "
                        "the author reads as a preview of von Neumann machines.",
         "domain": "robotics", "actor": ["linkerbot"],
         "evidences": ["physical-recursion", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-20-catl-humanoid-battery-lines"],
         "relatedTo": [B + "developments/2025-12-26-arc-declares-saturation",
                       B + "developments/2026-09-15-robots-making-robots"],
         "tags": ["robotics", "rsi"],
         "supporting_text": "assembling and testing their own hands",
         "sources": [{"id": "robo-tuo-x-linkerbot-hands",
                      "resource": "https://x.com/Robo_Tuo/status/2003475372856475902",
                      "title": "Post on X: Linkerbot humanoids assembling and testing their own hands",
                      "last_modified": "2025-12-23"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "CATL had humanoids building batteries; here they build the robots. The newsletter cites an X post "
                 "([Robo_Tuo](https://x.com/Robo_Tuo/status/2003475372856475902)) of [Linkerbot](/organizations/linkerbot.md) "
                 "humanoids in Beijing assembling and then testing their own hands, and pairs it with the same day's "
                 "[ARC saturation](/developments/2025-12-26-arc-declares-saturation.md) as the physical half of a cognitive "
                 "escape velocity. It extends the [CATL battery lines](/developments/2025-12-20-catl-humanoid-battery-lines.md) "
                 "of six days earlier from robots building what powers robots to robots building robots, the storyline that "
                 "reaches a [fully automated humanoid production line](/developments/2026-09-15-robots-making-robots.md) in "
                 "September 2026."},
        {"id": "2025-12-26-nanogpt-119s",
         "title": "The NanoGPT speedrun breaks two minutes at 119.3 seconds",
         "claim": "The NanoGPT training speedrun record fell to 119.3 seconds, breaking the "
                  "two-minute barrier.",
         "domain": "compute", "score": "119.3 s",
         "evidences": ["reasoning-price-deflation"],
         "supersedes": [B + "developments/2025-12-25-nanogpt-122s"]},
        {"id": "2025-12-26-programmer-employment-27-5",
         "title": "US programmer employment falls 27.5% in two years",
         "claim": "US programmer employment dropped 27.5% over two years.",
         "domain": "society", "score": "-27.5%",
         "evidences": ["work-displaced", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2025-12-18-senior-devs-experience-no-longer-matters"],
         "body": "The grievance of the 18th arrives as a labour statistic."},
        {"id": "2025-12-26-legg-remote-work-decade",
         "title": "Shane Legg predicts remote work vanishes within a decade",
         "claim": "DeepMind co-founder Shane Legg predicted all remote work will vanish within "
                  "a decade, displaced by agents.",
         "domain": "society", "actor": ["people/shane-legg"], "score": "within 10 years",
         "evidences": ["work-displaced"]},
        {"id": "2025-12-26-ai-50-percent-of-vc",
         "title": "AI takes half of global venture funding and mints 50 billionaires",
         "claim": "The AI sector minted 50 new billionaires during the year while capturing 50% "
                  "of all global venture funding.",
         "domain": "economics", "score": "50% of global VC",
         "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-26-midha-10b-for-one-gigawatt",
         "title": "A former a16z partner raises $10B for a single gigawatt",
         "claim": "Ex-a16z partner Anjney Midha is raising $10 billion to build a single "
                  "gigawatt of AI capacity.",
         "domain": "economics", "score": "$10B for 1 GW",
         "evidences": ["capital-takes-the-plant"],
         "body": "Venture capital mutating into infrastructure finance."},
        {"id": "2025-12-26-schmidhuber-pope",
         "title": "Schmidhuber unveils PoPE, a geometric fix to the Transformer",
         "claim": "Jürgen Schmidhuber unveiled PoPE, a polar coordinate positional embedding "
                  "improving performance from genomics to symbolic music.",
         "domain": "models", "actor": ["people/jurgen-schmidhuber"],
         "evidences": ["generalism-beats-specialism"]},
        {"id": "2025-12-26-deepmind-decade-time-skip",
         "title": "DeepMind targets problems where AI can skip a decade",
         "claim": "DeepMind is focusing on scientific problems where AI can fast-forward "
                  "progress by a decade.",
         "domain": "science", "actor": ["google-deepmind"],
         "evidences": ["root-node-problems"],
         "supersedes": [B + "developments/2025-12-18-hassabis-root-node-problems"]},
        {"id": "2025-12-26-openai-capability-overhang",
         "title": "OpenAI names a capability overhang between potential and use",
         "claim": "OpenAI declared a capability overhang between model potential and actual "
                  "consumer usage, and plans to push reasoning models harder into healthcare, "
                  "business and daily life in 2026.",
         "domain": "society", "actor": ["openai"], "evidences": ["intimate-interface"]},
        {"id": "2025-12-26-gemini-20-percent-traffic",
         "title": "Gemini takes 20% of traffic as Grok leads time spent",
         "claim": "Gemini reportedly reached 20% of traffic while Grok took the lead in time "
                  "spent.",
         "domain": "society", "actor": ["google", "xai"], "score": "20% traffic"},
        {"id": "2025-12-26-nvidia-displaces-apple-at-tsmc",
         "title": "NVIDIA is set to displace Apple as TSMC's largest customer",
         "claim": "NVIDIA is projected to displace Apple as TSMC's largest customer in 2026, "
                  "taking 20% of revenue.",
         "domain": "compute", "actor": ["nvidia", "tsmc", "apple"], "score": "20% of revenue",
         "evidences": ["consumer-deprioritized", "vertical-silicon"]},
        {"id": "2025-12-26-groq-deal-pays-for-itself",
         "title": "The Groq acquisition pays for itself overnight",
         "claim": "NVIDIA's $20 billion Groq acquisition was offset immediately as its market "
                  "capitalisation rose more than $30 billion.",
         "domain": "economics", "actor": ["nvidia", "groq"], "score": "+$30B market cap",
         "supersedes": [B + "developments/2025-12-25-nvidia-acquires-groq-20b"]},
        {"id": "2025-12-26-bofa-1t-chip-sales",
         "title": "Bank of America forecasts $1T in chip sales",
         "claim": "Bank of America forecast the chip sector will exceed $1 trillion in sales "
                  "next year.",
         "domain": "economics", "actor": ["bank-of-america"], "score": "$1T",
         "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-26-hbm-executives-fired",
         "title": "Hyperscalers fire executives who fail to secure HBM",
         "claim": "US hyperscalers began firing executives who failed to secure high bandwidth "
                  "memory, stationing replacements in South Korea to press for supply.",
         "domain": "compute", "evidences": ["consumer-deprioritized"],
         "supersedes": [B + "developments/2025-12-18-micron-revenue-57pct"]},
        {"id": "2025-12-26-china-maglev-700kmh",
         "title": "A Chinese maglev reaches 700 km/h in two seconds",
         "claim": "China's latest maglev test reached a record 700 km/h in two seconds on a "
                  "400-metre track, hinting at electromagnetic launch for aerospace.",
         "domain": "energy", "actor": ["china"], "score": "700 km/h in 2 s"},
    ],
}
