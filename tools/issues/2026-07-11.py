"""Issue 161 — 2026-07-11. The magic you can rent lags the magic in the vault."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-11-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-11", "title": "Welcome to July 11, 2026", "url": URL,
        "thesis": "A fifty-year-old conjecture falls in under an hour.",
        "body": """
# Welcome to July 11, 2026

A day after release, GPT-5.6 Sol Ultra proved the fifty-year-old Cycle Double
Cover Conjecture using 64 subagents in under an hour. Careful readers noted the
Erdős unit-distance solver was something else entirely — which means the lab has
been sitting on stronger models for months.

The magic you can rent lags the magic in the vault.
""",
    },
    "organizations": [
        {"id": "quantumdiamonds", "type": "Organization", "title": "QuantumDiamonds"},
        {"id": "nrc", "type": "Organization", "title": "Nuclear Regulatory Commission"},
        {"id": "vivani", "type": "Organization", "title": "Vivani Medical"},
        {"id": "malaysia", "type": "Organization", "title": "Malaysia"},
        {"id": "fcc-us", "type": "Organization", "title": "Federal Communications Commission"},
    ],
    "developments": [
        {"id": "2026-07-11-a-fifty-year-conjecture-falls-in-an-hour",
         "title": "A fifty-year-old conjecture falls to 64 subagents in under an hour",
         "claim": "A day after release, GPT-5.6 Sol Ultra proved the fifty-year-old Cycle Double "
                  "Cover Conjecture using 64 subagents in under an hour, while Grok 4.5 "
                  "constructed an explicit counterexample showing hypercontractivity already "
                  "fails on the 4-sphere, making a 2021 theorem sharp.",
         "domain": "science", "actor": ["openai", "xai"], "score": "64 subagents, <1 hour",
         "evidences": ["proof-priced-per-unit", "automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-06-28-an-erdos-problem-formalized-at-unprecedented-scale"]},
        {"id": "2026-07-11-the-rentable-magic-lags-the-vault",
         "title": "Readers deduce a lab has been sitting on stronger models for months",
         "claim": "Careful readers noted the Erdős unit-distance solver was a different system "
                  "entirely, implying OpenAI has been sitting on stronger models for months — the "
                  "magic available to rent lagging the magic in the vault.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["public-internal-divergence", "most-people-never-see-the-frontier",
                       "clearance-as-bottleneck"],
         "supersedes": [B + "developments/2026-07-11-a-fifty-year-conjecture-falls-in-an-hour"]},
        {"id": "2026-07-11-a-photo-finish-at-half-the-price",
         "title": "A challenger ties for first in frontend coding at half the price",
         "claim": "GPT-5.6-sol tied Claude Fable 5 for first in frontend coding at half the "
                  "price, a first for OpenAI, while analysts observed that Fable 5 is now the "
                  "entire case for an Anthropic subscription because Opus 4.8 loses even to the "
                  "older GPT-5.5.",
         "domain": "benchmarks", "actor": ["openai", "anthropic"], "score": "tied at half price",
         "evidences": ["price-implosion", "spiky-frontier", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-07-10-veblen-pricing-at-the-frontier"]},
        {"id": "2026-07-11-a-fourteen-billion-model-beats-the-giants-on-evenhandedness",
         "title": "A 14B model beats every frontier giant at ideological evenhandedness",
         "claim": "A new political-consistency benchmark found a specially trained 14-billion-"
                  "parameter model beating every frontier giant at ideological evenhandedness, "
                  "while a benchmark treating an obscure board game as a proxy for learning on "
                  "the job saw a new 39.7% state of the art still trailing expert humans.",
         "domain": "benchmarks", "score": "39.7% vs expert humans",
         "evidences": ["spiky-frontier", "values-negotiated-with-the-model",
                       "monoculture-is-the-vulnerability"],
         "supersedes": [B + "developments/2026-06-08-deterrence-by-betrayal"]},
        {"id": "2026-07-11-a-rival-delays-to-retrain-a-fresh-base",
         "title": "A lab delays its flagship a second time to retrain a fresh base",
         "claim": "Google delayed Gemini 3.5 Pro a second time to retrain a fresh two-million-"
                  "token-context base, even as leaks touted its best design taste yet and an "
                  "internal checkpoint already led Design Arena.",
         "domain": "models", "actor": ["google"], "score": "2M context",
         "evidences": ["public-internal-divergence", "spiky-frontier"],
         "supersedes": [B + "developments/2026-07-11-a-photo-finish-at-half-the-price"]},
        {"id": "2026-07-11-nutrition-labels-for-the-ear",
         "title": "A music coalition seeks AI-generated and AI-assisted track labels",
         "claim": "A music-industry coalition asked streaming services to tag tracks AI-generated "
                  "or AI-assisted, nutrition labels for the ear, while Meta scrapped a feature "
                  "that generated images of public accounts by default after unions and agencies "
                  "revolted.",
         "domain": "society", "actor": ["meta"],
         "evidences": ["agent-exclusion", "work-displaced"],
         "supersedes": [B + "developments/2026-07-08-every-public-profile-opted-in"]},
        {"id": "2026-07-11-a-government-takes-ten-percent-of-a-chipmaker",
         "title": "A government converts $9B in grants into a 10% stake in a chipmaker",
         "claim": "The White House converted $9 billion in grants into a 10% stake in Intel and "
                  "nudged Apple toward Intel's fabs during tariff talks, while loosening chip "
                  "exports to the UAE and learning that OpenAI and Google sell models to "
                  "blacklisted Chinese giants through Singapore subsidiaries.",
         "domain": "policy", "actor": ["white-house", "intel", "apple", "openai", "google"],
         "score": "10% stake",
         "evidences": ["politics-as-infrastructure", "silicon-curtain", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-07-05-heads-of-state-court-ceos-personally"]},
        {"id": "2026-07-11-the-worst-ever-memory-shortage-forecast",
         "title": "A memory chief forecasts the worst-ever shortage in 2027",
         "claim": "SK Hynix's chief, fresh off a record Nasdaq debut, forecast the worst-ever "
                  "memory shortage in 2027 with scarcity past 2030, while the five biggest "
                  "data-center spenders doubled their debt to $350 billion and felt the bond "
                  "market flinch.",
         "domain": "economics", "actor": ["sk-hynix"], "score": "$350B debt",
         "evidences": ["infrastructure-crowding-out", "debt-funded-buildout", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-07-07-a-twenty-year-lease-reincarnates-a-bitcoin-miner"]},
        {"id": "2026-07-11-three-gigawatts-of-factory-built-microreactors",
         "title": "A $145B agreement would deploy 3 GW of factory-built microreactors",
         "claim": "A $145 billion, 40-year agreement would deploy three gigawatts of "
                  "factory-built microreactors by 2035, as the Nuclear Regulatory Commission "
                  "narrowed environmental reviews to help quadruple nuclear capacity by 2050.",
         "domain": "energy", "actor": ["nrc"], "score": "$145B / 3 GW",
         "evidences": ["industrialized-nature", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-07-08-a-uranium-free-laser-fusion-pilot"]},
        {"id": "2026-07-11-chatbots-embedded-in-tactical-planning",
         "title": "A study finds militant factions embedding chatbots in tactical planning",
         "claim": "A Cambridge study found Boko Haram factions embedding chatbots in tactical "
                  "planning, as regulators ordered robotaxi developers to stop interfering with "
                  "first responders and the first US eVTOL pilot-program flights carried organs "
                  "rather than passengers.",
         "domain": "policy", "actor": ["cambridge"],
         "evidences": ["violence-arrives", "agent-society", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-07-a-cyber-agency-scans-federal-code-with-a-frontier-model"]},
        {"id": "2026-07-11-a-glp-1-implant-as-a-twice-yearly-update",
         "title": "An under-the-skin implant would make GLP-1 therapy twice-yearly",
         "claim": "Vivani's under-the-skin semaglutide implant would make GLP-1 therapy a "
                  "twice-yearly firmware update, while Xreal packed a 147-inch virtual screen "
                  "into 62-gram $299 glasses.",
         "domain": "biotech", "actor": ["vivani", "xreal"], "score": "62 g / $299",
         "evidences": ["hardware-grade-biology", "longevity-escape-velocity", "intimate-interface"],
         "supersedes": [B + "developments/2026-07-05-a-hundred-fifty-eight-alzheimers-drugs-in-trials"]},
        {"id": "2026-07-11-software-postings-up-since-an-agent-launched",
         "title": "Software job postings rise 15% since a coding agent launched",
         "claim": "Software job postings are up 15% since Claude Code launched, destruction "
                  "flipping to creation, as China dropped its urban job target from its five-year "
                  "plan for the first time in decades.",
         "domain": "economics", "actor": ["anthropic", "china"], "score": "+15% postings",
         "evidences": ["work-displaced", "post-labor-instruments", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-07-03-participation-at-a-fifty-year-low"]},
        {"id": "2026-07-11-a-hundred-thousand-satellite-fleet-filed-for",
         "title": "A company files for a 100,000-satellite fleet nine times its current size",
         "claim": "SpaceX filed for a 100,000-satellite Gen3 fleet nine times its current size "
                  "and herded Starlink into ever-lower shells, while the FCC approved a 60-foot "
                  "orbiting mirror to sell sunlight after dark over astronomers' objections.",
         "domain": "space", "actor": ["spacex", "fcc-us"], "score": "100,000 satellites",
         "evidences": ["orbit-as-compute", "industrialized-nature", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-07-10-a-million-satellite-inference-swarm"]},
    ],
}
