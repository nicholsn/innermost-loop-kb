"""Issue 131 — 2026-06-04. The bots pass the humans."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-4-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-04", "title": "Welcome to June 4, 2026", "url": URL,
        "thesis": "Bots overtake humans in online traffic for the first time.",
        "body": """
# Welcome to June 4, 2026

Cloudflare's chief executive conceded it happened faster than he predicted:
bots have passed humans in online traffic for the first time in history. Meta
is monetizing the shift with a tireless salesforce across WhatsApp, Messenger
and Instagram; Amazon is feeding the bots product photos of items that may not
exist.

Four lab chiefs — Hassabis, Altman, Amodei, Suleyman — signed an open letter
asking Congress to mandate screening of synthetic DNA orders, warning that AI
now outperforms PhD-level virologists.
""",
    },
    "themes": [
        {"id": "bots-outnumber-us", "type": "Theme",
         "title": "Machine traffic exceeds human traffic",
         "first_seen": "2026-06-04", "domain": "agents",
         "body": "The web's majority user stops being a person. Every assumption "
                 "built on the opposite — advertising, ranking, rate limits, the "
                 "meaning of a page view — was designed for a population that no "
                 "longer holds the floor."},
    ],
    "organizations": [
        {"id": "miso-labs", "type": "Organization", "title": "Miso Labs"},
        {"id": "sichuan", "type": "Organization", "title": "Sichuan"},
        {"id": "uc-berkeley", "type": "Organization", "title": "UC Berkeley"},
    ],
    "developments": [
        {"id": "2026-06-04-bots-pass-humans-online",
         "title": "Bots pass humans in online traffic for the first time",
         "claim": "Cloudflare's Matthew Prince conceded that bots have passed humans in online "
                  "traffic for the first time in history, and that it happened faster than he "
                  "predicted.",
         "domain": "agents", "actor": ["cloudflare"],
         "evidences": ["bots-outnumber-us", "agent-society", "agent-economy"],
         "supersedes": [B + "developments/2026-06-02-social-engineering-without-the-social"]},
        {"id": "2026-06-04-a-tireless-salesforce-across-three-apps",
         "title": "A platform ships a tireless salesforce across its messaging apps",
         "claim": "Meta launched the Meta Business Agent, which qualifies leads, books "
                  "appointments and closes deals across WhatsApp, Messenger and Instagram while "
                  "wiring into hundreds of systems, as Amazon began surfacing AI-generated "
                  "product photos that critics warn may depict items that do not exist.",
         "domain": "agents", "actor": ["meta", "amazon"],
         "evidences": ["autonomous-commerce", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-05-28-a-brokerage-opens-to-agents"]},
        {"id": "2026-06-04-answer-engine-optimization-poisons-a-forum",
         "title": "A forum bans posts after companies gamed answer-engine optimization",
         "claim": "The r/biohackers community banned new peptide and HRT posts after companies "
                  "gamed answer engine optimization, seeding threads so that ChatGPT and Google "
                  "would cite their brands.",
         "domain": "society",
         "evidences": ["gaming-the-token-metric", "bots-outnumber-us", "agent-exclusion"],
         "supersedes": [B + "developments/2026-06-03-a-sandbox-at-the-operating-system-layer"]},
        {"id": "2026-06-04-a-laptop-multimodal-model-under-apache",
         "title": "An encoder-free multimodal model runs on a laptop under Apache 2.0",
         "claim": "Google's Gemma 4 12B pipes vision and audio straight into the LLM backbone, "
                  "runs on a laptop and nearly matches its 26B Mixture-of-Experts sibling at "
                  "under half the memory, all under Apache 2.0, as the family passed 150 "
                  "million downloads.",
         "domain": "models", "actor": ["google"], "score": "150M downloads",
         "evidences": ["open-weight-latency", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-06-02-open-weights-undercut-by-forty-fold"]},
        {"id": "2026-06-04-a-voice-cloned-faster-than-reaction-time",
         "title": "An open voice model clones anyone in ten seconds and replies in 110ms",
         "claim": "Miso Labs' Miso-TTS clones a voice from a ten-second clip and replies in 110 "
                  "milliseconds, faster than human reaction time, while staying on-premises so "
                  "enterprises keep their data in house.",
         "domain": "models", "actor": ["miso-labs"], "score": "110 ms",
         "evidences": ["intimate-interface", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-05-09-three-new-audio-models"]},
        {"id": "2026-06-04-chip-supply-trails-demand-for-years",
         "title": "A foundry chief warns chip supply will trail demand for years",
         "claim": "TSMC's C.C. Wei warned chip supply will trail demand for years as "
                  "hyperscalers spend roughly $725 billion on AI in 2026, while forecasting 30% "
                  "sales growth and pledging to skip the abrupt price hikes that recently "
                  "roiled the memory market.",
         "domain": "compute", "actor": ["tsmc"], "score": "$725B hyperscaler spend",
         "evidences": ["infrastructure-crowding-out", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-02-an-ai-bet-dethrones-the-combustion-engine"]},
        {"id": "2026-06-04-replenishing-more-water-than-consumed",
         "title": "A hyperscaler pledges to replenish more water than it consumes",
         "claim": "Google pledged to replenish more water than it consumes by 2030, having "
                  "returned over 7 billion gallons in 2025 across 165 projects backed by $500 "
                  "million, while the EU's Cloud and AI Development Act aims to triple European "
                  "data-center capacity.",
         "domain": "energy", "actor": ["google", "european-union"], "score": "7B gallons returned",
         "evidences": ["infrastructure-crowding-out", "industrialized-nature"],
         "supersedes": [B + "developments/2026-06-02-eighty-billion-in-equity-as-a-tax-break-dies"]},
        {"id": "2026-06-04-datacenters-launched-off-a-strip-mined-moon",
         "title": "A company films datacenter satellites launched off a strip-mined Moon",
         "claim": "SpaceX released a video of itself electromagnetically launching data-center "
                  "satellites off a strip-mined Moon, a vision its $1.77 trillion IPO is "
                  "intended to fund, after winning a property-tax break for its $55 billion "
                  "Terafab.",
         "domain": "space", "actor": ["spacex"], "score": "$1.77T IPO",
         "evidences": ["orbit-as-compute", "industrialized-nature"],
         "supersedes": [B + "developments/2026-06-03-orbital-manufacturing-cleared-for-test"]},
        {"id": "2026-06-04-a-million-drone-deliveries",
         "title": "A retailer crosses a million drone deliveries",
         "claim": "Walmart crossed 1 million drone deliveries with Wing and Zipline across 66 "
                  "stores in four states, averaging 23 minutes per delivery, with 40% of that "
                  "first million landing in a single quarter.",
         "domain": "robotics", "actor": ["walmart", "wing", "zipline"], "score": "1M deliveries",
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-05-16-a-car-wash-for-robotaxis"]},
        {"id": "2026-06-04-ninety-percent-of-drones-intercepted",
         "title": "European officials believe AI and robotics may decide a war",
         "claim": "European officials now believe AI and robotics may deliver victory in "
                  "Ukraine, with jam-resistant targeting and defenses intercepting roughly 90% "
                  "of incoming drones.",
         "domain": "policy", "actor": ["ukraine", "european-union"], "score": "~90% intercepted",
         "evidences": ["violence-arrives", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-06-01-humanoids-headed-for-a-battlefield"]},
        {"id": "2026-06-04-four-lab-chiefs-ask-congress-to-screen-dna",
         "title": "Four lab chiefs ask Congress to mandate synthetic DNA screening",
         "claim": "Hassabis, Altman, Amodei and Suleyman signed an open letter urging Congress "
                  "to mandate customer screening for synthetic DNA and to screen the synthesis "
                  "equipment itself, warning that AI now outperforms PhD-level virologists.",
         "domain": "policy", "actor": ["google-deepmind", "openai", "anthropic", "microsoft"],
         "evidences": ["hardware-grade-biology", "legislating-the-shift", "compiling-matter"],
         "supersedes": [B + "developments/2026-06-03-testing-instead-of-licensing"],
         "body": "Co-signed by Nobel laureate David Baker and former national-security "
                 "officials. The same mastery of biology that promises cures lowers the "
                 "barrier to plagues."},
        {"id": "2026-06-04-a-third-of-a-cs-class-fails",
         "title": "A third of an intro CS class fails amid a cheating wave",
         "claim": "Failing grades soared at UC Berkeley, reaching 35% in its introductory "
                  "computing course, amid an AI-cheating wave, while Meta scaled back keylogging "
                  "of its own staff used to train its AI.",
         "domain": "society", "actor": ["uc-berkeley", "meta"], "score": "35% F rate",
         "evidences": ["deskilling", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-06-02-a-union-fences-off-the-classroom"]},
    ],
}
