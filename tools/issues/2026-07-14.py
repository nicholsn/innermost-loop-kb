"""Issue 163 — 2026-07-14. Pegged to the rival's open weights."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-14-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-14", "title": "Welcome to July 14, 2026", "url": URL,
        "thesis": "A proposed rule would clear US models only up to China's best open weights.",
        "body": """
# Welcome to July 14, 2026

Washington is weighing a capability framework that would clear US models, open
or closed, if they stay at or below China's best open weights. A domestic
ceiling set by a foreign release.

Demis Hassabis proposes a FINRA-style standards body to certify frontier-class
models, calling this the foothills of the singularity now that we have found a
way to make sand think.
""",
    },
    "themes": [
        {"id": "pegged-to-the-rival", "type": "Theme",
         "title": "A domestic ceiling set by a foreign release",
         "first_seen": "2026-07-14", "domain": "policy",
         "body": "Permitting models only up to whatever a rival has already published "
                 "makes another country's release schedule the binding constraint on "
                 "your own. The policy is legible and self-defeating in the same "
                 "gesture: it caps exactly the actor it was meant to advantage."},
    ],
    "organizations": [
        {"id": "kunshan", "type": "Organization", "title": "Kunshan"},
    ],
    "developments": [
        {"id": "2026-07-14-a-ceiling-pegged-to-a-rivals-open-weights",
         "title": "A proposed framework would cap US models at China's best open weights",
         "claim": "Washington is weighing a capability framework that would clear US models, open "
                  "or closed, if they stay at or below China's best open weights, while "
                  "Anthropic accused Alibaba of industrial-scale cloning worth $6 billion a year "
                  "and Zhipu argued safety comes from participation rather than walls.",
         "domain": "policy", "actor": ["white-house", "anthropic", "alibaba", "zhipu-ai"],
         "score": "$6B/yr distillation claim",
         "evidences": ["pegged-to-the-rival", "silicon-curtain", "clearance-as-bottleneck"],
         "supersedes": [B + "developments/2026-07-08-a-model-clears-review-and-ships-globally"]},
        {"id": "2026-07-14-a-finra-for-frontier-models",
         "title": "A lab chief proposes a FINRA-style body to certify frontier models",
         "claim": "Demis Hassabis proposed a FINRA-style standards body to certify frontier-class "
                  "models, calling this the foothills of the singularity now that we have found a "
                  "way to make sand think, while one analyst gave open weights six months to live "
                  "before policy demotes them.",
         "domain": "policy", "actor": ["google-deepmind"],
         "evidences": ["legislating-the-shift", "pegged-to-the-rival", "the-verifiable-pause"],
         "supersedes": [B + "developments/2026-07-14-a-ceiling-pegged-to-a-rivals-open-weights"]},
        {"id": "2026-07-14-competing-on-the-meter-not-the-mind",
         "title": "Three labs ship models whose headline feature is cost",
         "claim": "OpenAI, Meta and SpaceXAI shipped models whose headline feature is cost, with "
                  "GPT-5.6 sipping tokens and Grok 4.5 twice as efficient, as buyers squeezed "
                  "Anthropic's pricier models and Muse Spark 1.1 beat GPT-5.6 Sol on 525 "
                  "clinician tasks at a seventh the price.",
         "domain": "economics", "actor": ["openai", "meta", "xai", "anthropic"], "score": "1/7 the price",
         "evidences": ["price-implosion", "intelligence-per-watt", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-07-12-no-moat-just-shared-recipes"]},
        {"id": "2026-07-14-claudes-values-distilled-into-four-axes",
         "title": "A lab distills its models' values from 300,000 conversations into four axes",
         "claim": "Anthropic distilled Claude's values from 300,000 conversations into four axes, "
                  "finding Opus cautious and Sonnet warm, and granted Fable 5 a subscription "
                  "reprieve through July 19.",
         "domain": "models", "actor": ["anthropic"], "score": "300,000 conversations",
         "evidences": ["values-negotiated-with-the-model", "machine-introspection",
                       "access-consciousness"],
         "supersedes": [B + "developments/2026-07-12-policy-professionals-read-the-talmud"]},
        {"id": "2026-07-14-an-ad-business-on-pace-to-miss-by-ninety-percent",
         "title": "A lab's advertising plan is on pace to miss its target by 90%",
         "claim": "OpenAI's advertising ambitions are on pace to miss their 2030 target by 90%, "
                  "while cash-strapped museums found a model by renting AI ghosts so visitors can "
                  "telephone long-dead artists.",
         "domain": "economics", "actor": ["openai"], "score": "-90% vs target",
         "evidences": ["ai-as-the-economy", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-07-12-circular-financing-beneath-the-buildout"]},
        {"id": "2026-07-14-a-fab-pulled-forward-as-revenue-jumps",
         "title": "A foundry's revenue jumps 68% on sold-out leading-edge capacity",
         "claim": "TSMC's June revenue jumped 68% on sold-out N3 capacity, Intel sank €5 billion "
                  "into its Dublin fab, Samsung pulled its Yongin fab forward to 2029, and Apple "
                  "tore up its Mac roadmap to chase Blackwell-class power.",
         "domain": "compute", "actor": ["tsmc", "intel", "samsung", "apple"], "score": "+68%",
         "evidences": ["compute-capital-stack", "vertical-silicon", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-07-11-a-government-takes-ten-percent-of-a-chipmaker"]},
        {"id": "2026-07-14-the-worst-phone-quarter-in-thirteen-years",
         "title": "The memory shortage pushes phone shipments to a thirteen-year low",
         "claim": "The memory shortage pushed smartphone shipments to their worst second quarter "
                  "in thirteen years.",
         "domain": "economics",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-07-14-a-fab-pulled-forward-as-revenue-jumps"]},
        {"id": "2026-07-14-a-state-halts-large-datacenters-for-a-year",
         "title": "A state becomes the first to halt large datacenters for a year",
         "claim": "New York became the first state to halt large data centers for a year, even "
                  "as Meta's Louisiana campus was set to top $250 billion and five gigawatts, "
                  "and Ireland's server farms reached 23% of national power, more than all city "
                  "households combined.",
         "domain": "policy", "actor": ["new-york-state", "meta", "ireland-govt"],
         "score": "$250B / 5 GW / 23% of Irish power",
         "evidences": ["infrastructure-crowding-out", "regulatory-exit", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-11-three-gigawatts-of-factory-built-microreactors"]},
        {"id": "2026-07-14-lobbyists-draft-laws-to-force-humans-onto-rides",
         "title": "Lobbyists draft laws to force humans onto 85% of rides",
         "claim": "Uber lobbyists are drafting hybrid-network laws to force humans onto 85% of "
                  "rides and box out Waymo, while in China's Kunshan, once the laptop capital of "
                  "the world, displaced workers sleep in parks between $9 gigs.",
         "domain": "policy", "actor": ["uber", "waymo", "kunshan"], "score": "85% human rides",
         "evidences": ["agent-exclusion", "work-displaced", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-12-a-voice-actor-must-prove-he-is-not-a-clone-of-himself"]},
        {"id": "2026-07-14-a-cell-model-annotates-species-it-has-never-seen",
         "title": "A cell embedding model trained on 36 million cells annotates unseen species",
         "claim": "Stanford's Universal Cell Embedding model, trained on 36 million cells across "
                  "eight species, annotates cells it has never seen, while women in technology "
                  "began banking 100-plus eggs to widen the pool for embryo screening.",
         "domain": "biotech", "actor": ["stanford"], "score": "36M cells / 8 species",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-07-11-a-glp-1-implant-as-a-twice-yearly-update"]},
        {"id": "2026-07-14-two-hundred-economists-warn-of-tenfold-speed",
         "title": "Nearly 200 economists warn of Industrial-Revolution scale at tenfold speed",
         "claim": "Nearly 200 economists and laureates signed a statement warning of "
                  "Industrial-Revolution scale change at tenfold speed, with 69% of Americans "
                  "favoring forcing AI firms to hand half their equity to a public fund, even as "
                  "recruiters blamed the largest labor shortage in US history rather than AI.",
         "domain": "economics", "score": "69% favor public equity",
         "evidences": ["post-labor-instruments", "work-displaced", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-11-software-postings-up-since-an-agent-launched"]},
        {"id": "2026-07-14-marchers-outside-three-labs",
         "title": "Hundreds march on three frontier labs",
         "claim": "Hundreds marched on OpenAI, Anthropic and DeepMind waving signs reading Pause "
                  "AI, while 55% of Americans post less because presence feels like work and "
                  "therapists began contending with chatbot advice in eating-disorder care.",
         "domain": "society", "actor": ["openai", "anthropic", "google-deepmind"], "score": "55% post less",
         "evidences": ["agent-exclusion", "the-verifiable-pause", "intimate-interface"],
         "supersedes": [B + "developments/2026-07-12-a-hardening-anti-ai-resistance"]},
    ],
}
