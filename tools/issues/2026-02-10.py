"""Issue 051 — 2026-02-10. A hundred-year bond for a five-year buildout."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-10-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-10", "title": "Welcome to February 10, 2026", "url": URL,
        "thesis": "The buildout starts borrowing against the next century.",
        "body": """
# Welcome to February 10, 2026

Alphabet is lining up banks for a rare 100-year bond to fund datacenter
construction — mortgaging the next century to build the intelligence of this
one. OpenAI begins testing ads for free users the same week.

The White House pushes a compact to keep the expansion from bankrupting
households or draining water supplies, while demanding 40% of Taiwan's chip
production relocate to the US.
""",
    },
    "organizations": [
        {"id": "lockheed-martin", "type": "Organization", "title": "Lockheed Martin",
         "resource": "https://www.lockheedmartin.com/"},
        {"id": "pony-ai", "type": "Organization", "title": "Pony AI",
         "resource": "https://www.pony.ai/"},
        {"id": "ditto-bio", "type": "Organization", "title": "Ditto Bio",
         "body": "Mining parasite biology for autoimmune therapies."},
    ],
    "developments": [
        {"id": "2026-02-10-alphabet-100-year-bond",
         "title": "Alphabet lines up a hundred-year bond for datacenters",
         "claim": "Alphabet is lining up banks to sell a rare 100-year bond to fund data center "
                  "construction, mortgaging the next century to build the intelligence of this "
                  "one.",
         "domain": "economics", "actor": ["alphabet"], "score": "100-year",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-09-t-glass-shortage"]},
        {"id": "2026-02-10-ads-arrive-in-chatgpt",
         "title": "OpenAI begins testing ads for free users",
         "claim": "OpenAI began testing advertisements in ChatGPT for free users, with Altman "
                  "reportedly claiming the company is again exceeding 10% monthly growth.",
         "domain": "economics", "actor": ["openai"], "score": ">10% monthly",
         "evidences": ["autonomous-commerce", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-02-05-software-indices-lose-300b"]},
        {"id": "2026-02-10-composer-15-and-binaries-directly",
         "title": "Musk predicts models will skip source code entirely",
         "claim": "Cursor launched Composer 1.5, a sub-trillion-parameter model built with "
                  "twenty times more RL scaling, while Elon Musk predicted the trajectory ends "
                  "with models generating binaries and pixels directly, skipping source code.",
         "domain": "models", "actor": ["cursor"],
         "evidences": ["software-margin-collapse", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-02-08-middleware-obsoleted"]},
        {"id": "2026-02-10-white-house-compact-and-40pct-of-taiwan",
         "title": "The White House seeks 40% of Taiwan's chip production",
         "claim": "The White House is pushing a compact to keep datacenter expansion from "
                  "bankrupting households or draining water supplies while demanding 40% of "
                  "Taiwan's chip production relocate to the US, as Tencent released a 2-bit "
                  "model that holds accuracy under extreme compression.",
         "domain": "policy", "actor": ["white-house", "tencent"], "score": "40%",
         "evidences": ["silicon-curtain", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-03-apple-pays-57-more-per-iphone"]},
        {"id": "2026-02-10-lamprey-submersible",
         "title": "A submersible hitches rides on host vessels to recharge",
         "claim": "Lockheed Martin unveiled the LampreyMMAUV, a submersible that attaches to "
                  "host vessels to recharge, mimicking a parasite to extend its range.",
         "domain": "robotics", "actor": ["lockheed-martin"],
         "evidences": ["autonomy-clock-speed", "industrialized-nature"]},
        {"id": "2026-02-10-pony-ai-commercial-production",
         "title": "Driverless cars enter commercial production with Toyota",
         "claim": "Pony AI began commercial production of driverless cars with Toyota, while "
                  "Google used Android Auto data to predict crash risk from hard-braking events "
                  "and the US moved to ban Chinese software in connected vehicles.",
         "domain": "robotics", "actor": ["pony-ai", "toyota", "google"],
         "evidences": ["autonomous-commerce", "silicon-curtain"],
         "supersedes": [B + "developments/2026-02-07-waymo-world-model"]},
        {"id": "2026-02-10-california-air-improves",
         "title": "California air quality improves with EV registrations",
         "claim": "California air quality is improving in correlation with zero-emission "
                  "vehicle registrations.",
         "domain": "energy", "evidences": ["biosphere-uplift", "burning-molecules-for-tokens"]},
        {"id": "2026-02-10-travel-to-the-moon-for-anyone",
         "title": "SpaceX says it will build a system for anyone to reach the Moon",
         "claim": "Elon Musk announced SpaceX will build a system allowing anyone to travel to "
                  "the Moon and Mars, clarifying that launches will still go directly from "
                  "Earth to Mars because of lunar fuel scarcity.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-02-09-self-growing-city-on-the-moon"]},
        {"id": "2026-02-10-mining-parasites-for-medicine",
         "title": "A startup mines parasite biology for autoimmune therapy",
         "claim": "Ditto Bio launched to mine parasite biology for autoimmune therapies, while "
                  "Ozempic was found to restore knee cartilage independent of weight loss and a "
                  "Harvard study linked moderate caffeine to lower dementia risk.",
         "domain": "biotech", "actor": ["ditto-bio", "harvard"],
         "evidences": ["hardware-grade-biology", "discovery-as-process"],
         "supersedes": [B + "developments/2026-02-09-omega-3-and-dementia"]},
        {"id": "2026-02-10-ai-intensifies-work",
         "title": "A study finds AI tools intensify work rather than reduce it",
         "claim": "A study found AI tools intensify work rather than reduce it, pushing "
                  "employees to work faster and longer, while US AI startups adopted 996 hours "
                  "just as China cracked down on the practice.",
         "domain": "economics", "actor": ["china"],
         "evidences": ["cognitive-load-inverted", "work-displaced"],
         "supersedes": [B + "developments/2026-01-09-cognitive-burnout"],
         "body": "The January burnout finding now has a mechanism: the time freed is "
                 "immediately reallocated."},
        {"id": "2026-02-10-kalshi-perfect-on-the-fed",
         "title": "A prediction market has called every Fed decision since 2022",
         "claim": "Kalshi has predicted every Federal Reserve rate decision correctly since "
                  "2022, while AI accounted for 35% of European venture deals in 2025.",
         "domain": "economics", "actor": ["kalshi-org"], "score": "35% of EU deals",
         "evidences": ["autonomous-commerce", "work-displaced"]},
    ],
}
