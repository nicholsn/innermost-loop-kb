"""Issue 108 — 2026-05-05. Sixty percent odds on recursive self-improvement."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-5-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-05", "title": "Welcome to May 5, 2026", "url": URL,
        "thesis": "The hands-off doctrine ends just as the curves go vertical.",
        "body": """
# Welcome to May 5, 2026

The White House is reportedly considering an executive order creating an AI
working group and a formal review process for new models, abandoning its
hands-off doctrine. Anthropic's Jack Clark puts the odds of recursive
self-improvement by the end of 2028 at 60%.

In March his colleague called it a present phenomenon. Two months later the
company's own forecaster is quoting a probability on a date.
""",
    },
    "organizations": [
        {"id": "panthalassa", "type": "Organization", "title": "Panthalassa",
         "body": "Wave-powered floating datacenters."},
        {"id": "terran-robotics", "type": "Organization", "title": "Terran Robotics",
         "body": "Builds clay homes from dirt straight out of the ground."},
        {"id": "remidio", "type": "Organization", "title": "Remidio",
         "body": "Battery-powered fundus camera used to screen 15 million patients."},
        {"id": "pano-ai", "type": "Organization", "title": "Pano AI",
         "body": "Wildfire detection cameras and satellite feeds."},
        {"id": "mcdonalds", "type": "Organization", "title": "McDonald's",
         "resource": "https://www.mcdonalds.com/"},
    ],
    "developments": [
        {"id": "2026-05-05-an-executive-order-for-model-review",
         "title": "The White House considers a formal review process for new models",
         "claim": "The White House is reportedly considering an executive order creating an AI "
                  "working group and a formal review process for new models, abandoning its "
                  "hands-off doctrine just as the curves go vertical.",
         "domain": "policy", "actor": ["white-house"],
         "evidences": ["legislating-the-shift", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-04-half-a-government-on-agents-in-two-years"]},
        {"id": "2026-05-05-sixty-percent-odds-on-rsi-by-2028",
         "title": "A lab co-founder puts recursive self-improvement at 60% by 2028",
         "claim": "Anthropic co-founder Jack Clark put the odds of recursive self-improvement "
                  "by the end of 2028 at 60%, based on hundreds of public data sources.",
         "domain": "agents", "actor": ["anthropic", "people/jack-clark"], "score": "60% by 2028",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-05-04-eighty-percent-of-the-way-to-agi"],
         "body": "In March the company's alignment lead called it a present phenomenon. Here "
                 "its policy lead quotes a probability and a date."},
        {"id": "2026-05-05-floor-plans-from-photographs",
         "title": "A model closes on the human baseline for reading rooms from photos",
         "claim": "Andon Labs' new benchmark found GPT-5.5 hitting 36.2% at converting apartment "
                  "photos into two-dimensional floor plans against a 58.6% human baseline, while "
                  "Chicago researchers reported coding agents autonomously implementing a full "
                  "self-play training pipeline comparable with external solvers.",
         "domain": "benchmarks", "actor": ["andon-labs", "openai"], "score": "36.2% vs 58.6%",
         "evidences": ["benchmark-saturation", "data-beyond-text"],
         "supersedes": [B + "developments/2026-05-03-arc-agi-3-starts-to-move"]},
        {"id": "2026-05-05-codex-overtakes-claude-code",
         "title": "One coding tool overtakes the other a week after a release",
         "claim": "OpenAI's Codex overtook Claude Code in downloads a week after GPT-5.5 "
                  "shipped, and OpenAI is adding optional AI-generated pets as floating "
                  "overlays that announce task completions.",
         "domain": "economics", "actor": ["openai", "anthropic"],
         "evidences": ["engineer-as-supervisor", "machine-affect"],
         "supersedes": [B + "developments/2026-04-23-deepmind-engineers-threaten-to-quit-over-a-rivals-tool"]},
        {"id": "2026-05-05-labs-fund-their-own-distribution",
         "title": "Both leading labs form billion-dollar ventures with private equity",
         "claim": "Anthropic unveiled a $1.5 billion joint venture with Blackstone, Goldman "
                  "Sachs and Hellman & Friedman to push AI into private equity portfolio "
                  "companies while OpenAI finalized a parallel $10 billion venture, prompting "
                  "questions about whether the labs are paying their partners to use the "
                  "software rather than selling it.",
         "domain": "economics", "actor": ["anthropic", "openai", "blackstone", "goldman-sachs"],
         "score": "$1.5B / $10B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-05-04-hyperscaler-capex-rivals-the-whole-index"]},
        {"id": "2026-05-05-banks-offload-datacenter-debt",
         "title": "Banks scramble to offload datacenter debt as wave power is funded",
         "claim": "Banks are scrambling to offload data center debt as the buildout accelerates, "
                  "while Peter Thiel led a $140 million round into Panthalassa to power floating "
                  "data centers with wave energy.",
         "domain": "economics", "actor": ["panthalassa"], "score": "$140M",
         "evidences": ["debt-funded-buildout", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-03-three-datacenters-damaged-by-drone-strikes"]},
        {"id": "2026-05-05-zero-percent-market-share-in-china",
         "title": "Nvidia says its China market share is zero and policy backfired",
         "claim": "Jensen Huang said Nvidia now has zero percent market share in China and that "
                  "US export policy has already largely backfired, while Chinese exports of "
                  "solar, batteries and electric vehicles all hit record highs as the oil shock "
                  "accelerated clean-energy adoption.",
         "domain": "policy", "actor": ["nvidia", "china"], "score": "0% share",
         "evidences": ["silicon-curtain", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-01-huawei-takes-chinas-chip-market"]},
        {"id": "2026-05-05-houses-built-from-the-dirt-underfoot",
         "title": "Robots build clay homes from the dirt under the site",
         "claim": "Terran Robotics is building clay homes in central Texas using dirt straight "
                  "from the ground, the cheapest building material in existence, while Amazon "
                  "opened its global logistics network to outside shippers across ocean, road, "
                  "rail and air.",
         "domain": "robotics", "actor": ["terran-robotics", "amazon"],
         "evidences": ["compiling-matter", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-05-04-humanoids-run-holiday-kiosks"]},
        {"id": "2026-05-05-fifteen-million-retinal-screens",
         "title": "A battery-powered camera has screened fifteen million patients",
         "claim": "India's Remidio has built a battery-powered fundus camera letting a community "
                  "health worker capture a high-resolution retinal image in seconds, already "
                  "used to screen fifteen million patients across forty countries for diabetic "
                  "eye disease, with new software flagging dangerous pregnancies on the same "
                  "hardware.",
         "domain": "biotech", "actor": ["remidio"], "score": "15M patients / 40 countries",
         "evidences": ["reasoning-price-deflation", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-04-vasculature-fills-space-nerves-form-sheets"]},
        {"id": "2026-05-05-retiring-early-may-accelerate-decline",
         "title": "Leaving the workforce early may accelerate cognitive decline",
         "claim": "New research suggests leaving the workforce before retirement age may "
                  "accelerate cognitive decline, implying that working longer is on the margin a "
                  "nootropic, while wildfire detection cameras spread across the fire-prone West "
                  "ahead of a thin snowpack.",
         "domain": "society", "actor": ["pano-ai"],
         "evidences": ["work-displaced", "cognitive-load-inverted"],
         "body": "A complication for every proposal in the corpus that assumes leisure is the "
                 "benefit of displacement."},
        {"id": "2026-05-05-twenty-seven-new-tatooine-planets",
         "title": "Twenty-seven candidate planets are found orbiting two stars each",
         "claim": "Researchers discovered twenty-seven potential new planets orbiting two stars, "
                  "more than doubling the known circumbinary catalogue, while cosmologists "
                  "confirmed Newtonian gravity at the scale of galaxy clusters hundreds of "
                  "millions of light years apart.",
         "domain": "space", "score": "27 candidates",
         "evidences": ["inhabitable-worlds", "automated-science"],
         "supersedes": [B + "developments/2026-05-03-a-plasma-thruster-at-120-kilowatts"]},
        {"id": "2026-05-05-ai-literacy-hardwired-into-schools",
         "title": "A bipartisan bill would hardwire AI literacy into schools",
         "claim": "A bipartisan bill endorsed by OpenAI, Google and Microsoft would hardwire AI "
                  "literacy into K-12 education and empower the National Science Foundation to "
                  "fund curricula at scale, while new EU rules from February 2027 require "
                  "user-replaceable batteries in phones and tablets.",
         "domain": "policy", "actor": ["us-congress", "european-union"],
         "evidences": ["legislating-the-shift", "deskilling"],
         "supersedes": [B + "developments/2026-05-03-the-academy-requires-human-performance"]},
        {"id": "2026-05-05-mcdonalds-retires-self-serve-soda",
         "title": "A fast food chain retires self-serve soda as delivery eats the dining room",
         "claim": "McDonald's is quietly retiring self-serve soda nationwide as drive-through "
                  "and delivery consume the dining room.",
         "domain": "economics", "actor": ["mcdonalds"],
         "evidences": ["autonomous-commerce", "work-displaced"]},
        {"id": "2026-05-05-markets-price-the-founders-lawsuit",
         "title": "Traders put a founder's odds of winning at 37%",
         "claim": "Prediction market traders put Elon Musk's odds of beating OpenAI in court at "
                  "37%, and two days before trial he reportedly texted Greg Brockman that by "
                  "the end of the week he and Sam would be the most hated men in America.",
         "domain": "policy", "actor": ["xai", "openai", "kalshi-org"], "score": "37%",
         "evidences": ["coordination-tax", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-05-01-musk-admits-distillation-under-oath"]},
    ],
}
