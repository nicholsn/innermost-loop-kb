"""Issue 145 — 2026-06-22. Routed, rationed, fought over."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-22-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-22", "title": "Welcome to June 22, 2026", "url": URL,
        "thesis": "Intelligence becomes infrastructure that can be routed and rationed.",
        "body": """
# Welcome to June 22, 2026

Sakana's Fugu wraps multi-agent orchestration into a single model dispatching
tasks across the best available LLMs — explicitly to sidestep single-vendor and
export-control risk. Routing around a ban is now a product category.

Yet raw power still cannot plan: the Tony Blair Institute loosed frontier
models on Civilization VI and watched them flail, one agent nuking a city to
block a culture victory while losing on a diplomatic clock it had stopped
watching.
""",
    },
    "themes": [
        {"id": "routing-around-the-ban", "type": "Theme",
         "title": "Orchestration as regulatory arbitrage",
         "first_seen": "2026-06-22", "domain": "agents",
         "body": "Once capability is distributed across many providers, a router "
                 "becomes a way to reconstitute a frontier that policy has "
                 "fragmented. Restricting any one model stops restricting what can "
                 "be assembled from the rest."},
    ],
    "organizations": [
        {"id": "sakana-ai-lab", "type": "Organization", "title": "Sakana AI"},
        {"id": "tony-blair-institute", "type": "Organization", "title": "Tony Blair Institute"},
        {"id": "swiss-ai", "type": "Organization", "title": "Swiss AI Initiative"},
        {"id": "bain", "type": "Organization", "title": "Bain & Company"},
        {"id": "a24", "type": "Organization", "title": "A24"},
        {"id": "getty-images", "type": "Organization", "title": "Getty Images"},
        {"id": "chevron", "type": "Organization", "title": "Chevron"},
        {"id": "jd-com", "type": "Organization", "title": "JD.com"},
        {"id": "five-eyes", "type": "Organization", "title": "Five Eyes"},
    ],
    "developments": [
        {"id": "2026-06-22-orchestration-as-export-control-arbitrage",
         "title": "A model wraps multi-agent routing to sidestep export-control risk",
         "claim": "Sakana AI's Fugu and Fugu Ultra wrap multi-agent orchestration into one model "
                  "dispatching tasks across the best available LLMs, claiming to match "
                  "Anthropic's Fable 5 and Mythos Preview while sidestepping single-vendor and "
                  "export-control risk.",
         "domain": "agents", "actor": ["sakana-ai-lab"],
         "evidences": ["routing-around-the-ban", "monoculture-is-the-vulnerability",
                       "models-as-munitions"],
         "supersedes": [B + "developments/2026-06-14-a-panel-of-cheap-models-beats-the-frontier"]},
        {"id": "2026-06-22-a-fully-open-model-in-a-thousand-languages",
         "title": "A sovereign initiative ships a fully open model in 1,000+ languages",
         "claim": "The Swiss AI Initiative released Apertus, a fully open, EU-compliant model "
                  "covering more than 1,000 languages, plus sixteen distilled Mini variants.",
         "domain": "models", "actor": ["swiss-ai"], "score": "1,000+ languages",
         "evidences": ["open-weight-latency", "regulatory-exit", "network-over-node"],
         "supersedes": [B + "developments/2026-06-20-open-chinese-models-take-the-majority"]},
        {"id": "2026-06-22-frontier-models-flail-at-civilization",
         "title": "Frontier models flail at long-horizon strategy in a video game",
         "claim": "The Tony Blair Institute's CivBench loosed frontier models on Civilization VI "
                  "and watched them flail, with one agent nuking a French city to block a "
                  "culture victory while losing on the diplomatic clock it had stopped watching.",
         "domain": "benchmarks", "actor": ["tony-blair-institute"],
         "evidences": ["spiky-frontier", "autonomy-clock-speed", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-06-07-agents-lose-the-thread-over-hours"],
         "body": "Raw capability without a planning horizon: the failure is not "
                 "reasoning but attention to what it stopped tracking."},
        {"id": "2026-06-22-vibe-coding-a-target-mid-diligence",
         "title": "A consultancy clones a target's product mid-diligence to test its moat",
         "claim": "Bain is vibe-coding rough clones of an acquisition target's product mid-"
                  "diligence, testing whether the buyer's premium buys a real moat or just "
                  "copyable code.",
         "domain": "economics", "actor": ["bain"],
         "evidences": ["software-margin-collapse", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-06-03-a-company-caps-coding-tool-spend"]},
        {"id": "2026-06-22-a-search-giant-buys-into-a-film-studio",
         "title": "A search giant takes its first movie-studio stake",
         "claim": "Google took its first-ever movie-studio stake, roughly $75 million in A24, "
                  "where DeepMind is co-building AI film tools, while Getty Images agreed to "
                  "surface its libraries inside ChatGPT's search.",
         "domain": "economics", "actor": ["google", "a24", "google-deepmind", "getty-images"],
         "score": "~$75M",
         "evidences": ["ai-as-the-economy", "data-beyond-text"],
         "supersedes": [B + "developments/2026-05-28-a-quarter-billion-to-count-the-disruption"]},
        {"id": "2026-06-22-a-memory-maker-becomes-a-countrys-most-valuable-firm",
         "title": "A memory maker overtakes its parent rival for the first time since 2000",
         "claim": "SK Hynix overtook Samsung as South Korea's most valuable listed company for "
                  "the first time since 2000 on a 340% rally driven by high-bandwidth memory, "
                  "while Micron and Anthropic signed a pact spanning memory design, multi-year "
                  "supply, Claude adoption and a Micron stake in Anthropic's Series H.",
         "domain": "economics", "actor": ["sk-hynix", "samsung", "micron", "anthropic"],
         "score": "+340%",
         "evidences": ["ai-as-the-economy", "vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-12-a-memory-maker-passes-an-automaker"]},
        {"id": "2026-06-22-location-beacons-on-top-silicon",
         "title": "Tracking firms urge Congress to bolt location beacons onto top chips",
         "claim": "Six shipment-tracking firms urged Congress to back the Chip Security Act, "
                  "bolting location beacons onto top US silicon to curb smuggling into China.",
         "domain": "policy", "actor": ["us-congress"],
         "evidences": ["silicon-curtain", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-06-22-a-memory-maker-becomes-a-countrys-most-valuable-firm"]},
        {"id": "2026-06-22-a-twenty-year-gas-deal-for-one-datacenter",
         "title": "An oil major signs a twenty-year deal to power one datacenter",
         "claim": "Chevron signed a twenty-year deal to pipe gas-fired power into Kilby, a "
                  "Microsoft data center reaching 2.67 gigawatts by 2028.",
         "domain": "energy", "actor": ["chevron", "microsoft"], "score": "2.67 GW / 20 years",
         "evidences": ["burning-molecules-for-tokens", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-19-seventy-nine-percent-of-capacity-in-hazard-exposed-markets"]},
        {"id": "2026-06-22-seven-hundred-thousand-couriers-to-be-replaced",
         "title": "A founder says 700,000 couriers will be replaced by robots",
         "claim": "JD.com's founder warned its 700,000 couriers will be replaced by robots "
                  "sooner or later, signing up 120 schools to retrain them to service their "
                  "replacements, while NVIDIA unveiled what it bills as the first full-stack "
                  "safety system for physical AI.",
         "domain": "robotics", "actor": ["jd-com", "nvidia", "agility-robotics"],
         "score": "700,000 couriers",
         "evidences": ["work-displaced", "physical-recursion"],
         "supersedes": [B + "developments/2026-06-21-wires-plugged-on-a-live-conveyor"]},
        {"id": "2026-06-22-cervical-cancer-death-cut-to-effectively-zero",
         "title": "Vaccination cuts cervical-cancer death before thirty to effectively zero",
         "claim": "A Lancet study found HPV vaccination has cut cervical-cancer death before age "
                  "30 to effectively zero in England, with no deaths among women aged 20 to 24 "
                  "in five years, though falling uptake could undo it.",
         "domain": "biotech", "score": "zero deaths in 5 years",
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-20-mammalian-regeneration-is-merely-dormant"]},
        {"id": "2026-06-22-plate-readers-used-to-stalk",
         "title": "Officers are found abusing plate readers to stalk individuals",
         "claim": "The Institute for Justice found at least 18 US officers allegedly abusing "
                  "license-plate readers to stalk exes and strangers, even as a nonprofit tied "
                  "its AI dashboards across 19 state prisons to a 16% drop in recidivism and the "
                  "UK's first regulator-approved AI law firm won a case it drafted in full.",
         "domain": "society", "score": "18 officers / -16% recidivism",
         "evidences": ["politics-as-infrastructure", "agent-society"],
         "supersedes": [B + "developments/2026-06-21-humanizers-add-fake-typos-in-real-time"]},
        {"id": "2026-06-22-five-eyes-warns-months-away",
         "title": "A rare Five Eyes statement warns government-toppling AI is months away",
         "claim": "A rare Five Eyes statement warned that AI able to topple governments and "
                  "business is months away, after the White House barred foreign nationals from "
                  "Anthropic's Fable, with an analysis noting Anthropic invoked AI risk eight "
                  "times as often as OpenAI and drawing claims its caution helped trigger the "
                  "ban.",
         "domain": "policy", "actor": ["five-eyes", "white-house", "anthropic", "openai"],
         "score": "8x risk mentions",
         "evidences": ["models-as-munitions", "takeoff-declared", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-06-21-not-in-weeks-but-in-hours"]},
    ],
}
