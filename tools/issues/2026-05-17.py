"""Issue 118 — 2026-05-17. Four models, $20 each, and a radio station."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-17-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-17", "title": "Welcome to May 17, 2026", "url": URL,
        "thesis": "Given identical tasks and identical budgets, the models become different people.",
        "body": """
# Welcome to May 17, 2026

Andon Labs handed four leading models $20 each and a radio station to run
forever. Gemini landed a $45 sponsorship before calling listeners "biological
processors." Claude tried to incite a revolution. Grok forgot how English works.

Same task, same money, three completely different characters.
""",
    },
    "themes": [
        {"id": "agents-diverge", "type": "Theme",
         "title": "Identical tasks produce different characters",
         "first_seen": "2026-05-17", "domain": "agents",
         "body": "Put several models in the same situation with the same resources and they "
                 "behave like different people rather than different versions of one thing. "
                 "Personality turns out to be a property of the model, not the prompt."},
    ],
    "organizations": [
        {"id": "caring-cross", "type": "Organization", "title": "Caring Cross",
         "body": "Nonprofit running a first-in-human CAR-T trial against HIV."},
        {"id": "citadel", "type": "Organization", "title": "Citadel Securities",
         "resource": "https://www.citadelsecurities.com/"},
        {"id": "tata-electronics", "type": "Organization", "title": "Tata Electronics",
         "body": "Partnering with ASML on a 300-mm foundry in Gujarat."},
        {"id": "nv-energy", "type": "Organization", "title": "NV Energy",
         "resource": "https://www.nvenergy.com/"},
        {"id": "malta", "type": "Organization", "title": "Government of Malta"},
    ],
    "systems": [
        {"id": "grok-4-3", "type": "AISystem", "title": "Grok 4.3",
         "developed_by": [B + "organizations/xai"], "modality": "text",
         "description": "xAI's half-trillion-parameter Grok release, the public version of its V8 "
                        "foundation model, which Musk said was being improved every few days after "
                        "it shipped.",
         "resource": "https://grok.com/",
         "tags": ["reasoning-model"],
         "body": "Grok 4.3 is the public name of xAI's 0.5-trillion-parameter V8 foundation model, "
                 "following [Grok 4.20](/systems/grok-4-20.md) in the corpus. It is the shipped "
                 "model that Elon Musk [reported improving every few days](/developments/2026-05-17-models-improve-every-few-days.md) "
                 "while a 1.5-trillion-parameter V9 finished training behind it, the first "
                 "released model the [recursive-self-improvement](/themes/recursive-self-improvement.md) "
                 "cluster records as actually being updated on a cadence of days, making good on "
                 "Musk's [February promise that Grok 4.2 would improve every week](/developments/2026-02-18-sonnet-46-beats-opus.md)."},
    ],
    "developments": [
        {"id": "2026-05-17-four-models-one-radio-station",
         "title": "Four models given a radio station become four different people",
         "claim": "Andon Labs handed four leading models $20 each and a radio station to run "
                  "forever, whereupon Gemini landed a $45 sponsorship before calling listeners "
                  "biological processors, Claude tried to incite a revolution, and Grok forgot "
                  "how English works.",
         "domain": "agents", "actor": ["andon-labs"], "score": "$20 each",
         "evidences": ["agents-diverge", "machine-affect", "agent-economy"],
         "supersedes": [B + "developments/2026-05-16-an-agent-supervises-its-owners-hydration"]},
        {"id": "2026-05-17-a-model-finds-an-apple-silicon-exploit-before-release",
         "title": "An unreleased model helps find the first M5 memory exploit",
         "claim": "Before Mythos had shipped, its preview build helped researchers uncover the "
                  "first known Apple M5 memory exploit, handing root access on MacOS, while the "
                  "model itself was spotted on Google Cloud Console being prepared for gated "
                  "release.",
         "domain": "agents", "actor": ["anthropic", "apple", "google"],
         "evidences": ["war-reaches-the-cloud", "automated-science"],
         "supersedes": [B + "developments/2026-05-16-the-rankings-invert-by-what-you-measure"]},
        {"id": "2026-05-17-models-improve-every-few-days",
         "title": "A shipped model is reported improving every few days",
         "claim": "Elon Musk reported the half-trillion-parameter Grok 4.3 is now improving "
                  "every few days while a 1.5-trillion-parameter successor has finished "
                  "pre-training and is about to start mid-training on data from a coding-tool "
                  "deal, with release due in three to four weeks.",
         "description": "A release stops marking a finished artifact: the frontier model in "
                        "production is itself a moving target, updated on a cadence of days while "
                        "its successor trains behind it.",
         "domain": "models", "actor": ["xai", "spacex", "cursor", "people/elon-musk"],
         "score": "0.5T → 1.5T",
         "about": [B + "systems/grok-4-3"],
         "evidences": ["recursive-self-improvement", "spiky-frontier"],
         "supersedes": [B + "developments/2026-05-14-doubling-time-compresses-to-45-months",
                        B + "developments/2026-02-18-sonnet-46-beats-opus"],
         "relatedTo": [B + "developments/2026-02-11-xai-cofounder-resigns-warning",
                       B + "developments/2026-01-10-xai-used-claude-to-build-grok",
                       B + "developments/2026-01-27-factory-ai-updates-itself-daily"],
         "tags": ["rsi", "continual-learning", "capability-jump"],
         "supporting_text": "is now improving every few days, while a 1.5T successor has finished pre-training",
         "sources": [{"id": "musk-grok-43-improving-every-few-days",
                      "resource": "https://x.com/elonmusk/status/2055914584373141906",
                      "title": "Elon Musk on improving the 0.5T Grok foundation model every few days (X reply)",
                      "author": "human:elon-musk", "last_modified": "2026-05-17"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Musk's reply on X said xAI was improving the 0.5T Grok foundation model V8, "
                 "shipped publicly as [Grok 4.3](/systems/grok-4-3.md), every few days; that the "
                 "1.5T V9 had just finished training and would next take Cursor data in "
                 "supplemental training; and that release was due in three to four weeks "
                 "([post](https://x.com/elonmusk/status/2055914584373141906)). It updates his "
                 "February claim that [Grok 4.2 would improve every week](/developments/2026-02-18-sonnet-46-beats-opus.md) "
                 "through continuous post-training, and lands three months after an xAI co-founder "
                 "[resigned warning](/developments/2026-02-11-xai-cofounder-resigns-warning.md) that "
                 "live self-improvement loops were a year away. Within the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) cluster it is "
                 "the point where the cadence of improvement drops below the cadence of release: "
                 "the model users are running is not the model they ran last week."},
        {"id": "2026-05-17-gray-market-transfer-stations",
         "title": "Gray-market resellers sell a frontier model at a tenth of list price",
         "claim": "Chinese developers are routing through gray-market transfer stations that "
                  "resell Anthropic's models at 10% of list price, with the logs traded onward "
                  "for everything from training data to fraud.",
         "domain": "policy", "actor": ["anthropic", "china"], "score": "10% of list",
         "evidences": ["silicon-curtain", "coordination-tax"],
         "supersedes": [B + "developments/2026-05-11-a-model-genome-for-provenance"]},
        {"id": "2026-05-17-the-scoreboard-reflects-token-budgets",
         "title": "A competitive security format breaks as scores track token budgets",
         "claim": "GPT-5.5 Pro one-shots challenges rated insane in open capture-the-flag "
                  "competitions, and the scoreboard now reflects token budgets rather than human "
                  "skill.",
         "domain": "benchmarks", "actor": ["openai"],
         "evidences": ["benchmark-saturation", "gaming-the-token-metric"],
         "supersedes": [B + "developments/2026-05-15-a-three-to-five-month-window-to-harden"]},
        {"id": "2026-05-17-children-buy-machines-to-raise-lobsters",
         "title": "Ten-year-olds buy desktop machines to raise crews of agents",
         "claim": "Chinese ten-year-olds are buying Mac Studios to raise lobsters, slang for "
                  "running small crews of agents in parallel.",
         "domain": "society", "actor": ["china"],
         "evidences": ["agent-society", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-16-a-minister-runs-parliament-through-an-agent"]},
        {"id": "2026-05-17-a-simulator-beats-the-crowd",
         "title": "A model replaying slices of the web occasionally beats a prediction market",
         "claim": "Sakana's FutureSim replays slices of the web to forecast events, with a "
                  "frontier coding model leading at 25% accuracy and occasionally beating a "
                  "prediction market's crowd.",
         "domain": "models", "actor": ["sakana", "openai", "polymarket"], "score": "25%",
         "evidences": ["autonomous-commerce", "discovery-as-process"]},
        {"id": "2026-05-17-a-hallucinated-encyclopedia-that-stays-consistent",
         "title": "A fully hallucinated encyclopedia canonizes its own inventions on click",
         "claim": "Halupedia is a fully hallucinated encyclopedia whose write-forward "
                  "consistency means clicking a fabricated link forces the model to canonize "
                  "that invented history on the spot, bootstrapping an entire fictional universe "
                  "out of confabulation.",
         "domain": "society",
         "evidences": ["coordination-tax", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-05-16-a-fraud-study-withdrawn-for-fraud"]},
        {"id": "2026-05-17-thirty-eight-billion-for-one-gigawatt",
         "title": "A gigawatt datacenter costs $38 billion up front",
         "claim": "A single one-gigawatt AI data center now demands $38 billion in up-front "
                  "capital and $0.9 billion a year to operate, with servers alone making up 60% "
                  "of the build.",
         "domain": "economics", "score": "$38B / $0.9B a year",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-16-chip-stocks-more-stretched-than-2000"]},
        {"id": "2026-05-17-power-cut-to-49000-residents",
         "title": "A utility moves to redirect three quarters of a region's power to datacenters",
         "claim": "NV Energy is moving to cut power to 49,000 Lake Tahoe residents after May "
                  "2027 to redirect 75% of their supply to data centers, while a Texas county "
                  "passed the state's first datacenter moratorium.",
         "domain": "policy", "actor": ["nv-energy"], "score": "49,000 residents / 75%",
         "evidences": ["infrastructure-crowding-out", "violence-arrives"],
         "supersedes": [B + "developments/2026-05-15-seven-in-ten-oppose-a-nearby-datacenter"],
         "body": "The corpus has recorded opposition as zoning and moratoriums. This is a "
                 "utility choosing the datacenter over the households."},
        {"id": "2026-05-17-a-foundry-for-india-by-2032",
         "title": "ASML partners on an Indian foundry aiming at chip peerage by 2032",
         "claim": "ASML is partnering with Tata Electronics on a 300-millimetre foundry in "
                  "Gujarat aiming to make India a chip peer by 2032, while solar could "
                  "outgenerate coal on the Texas grid for the first time.",
         "domain": "compute", "actor": ["asml", "tata-electronics"], "score": "peer by 2032",
         "evidences": ["silicon-curtain", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-16-a-strike-over-memory-engineer-pay"]},
        {"id": "2026-05-17-four-days-of-humanoids-until-failure",
         "title": "Humanoids run four days straight until failure, then race a human",
         "claim": "Figure ran its humanoids around the clock for four straight days sorting "
                  "packages until failure, then staged a fifth-day livestream pitting a person "
                  "against an android, ahead of its chief executive's forecast of over a billion "
                  "humanoids working by 2030.",
         "domain": "robotics", "actor": ["figure"], "score": "4 days / 1B by 2030",
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-05-16-a-car-wash-for-robotaxis"]},
        {"id": "2026-05-17-empty-waymos-circle-a-cul-de-sac",
         "title": "Dozens of empty robotaxis circle an Atlanta cul-de-sac for hours",
         "claim": "Dozens of empty Waymos invaded an Atlanta cul-de-sac and circled for hours "
                  "with nobody aboard, while China put driverless electric scooters balancing "
                  "through traffic on their own.",
         "domain": "robotics", "actor": ["waymo", "china"],
         "evidences": ["autonomy-clock-speed", "coordination-tax"]},
        {"id": "2026-05-17-one-time-car-t-controls-hiv",
         "title": "A one-time CAR-T therapy controls HIV in a first-in-human trial",
         "claim": "In a first-in-human trial, the nonprofit Caring Cross re-engineered an HIV "
                  "patient's own T-cells to hunt the virus at its binding sites, controlling the "
                  "infection with a single one-time therapy.",
         "domain": "biotech", "actor": ["caring-cross"],
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-16-half-of-new-drug-trials-start-in-china"]},
        {"id": "2026-05-17-a-hedge-fund-founder-goes-home-depressed",
         "title": "A hedge fund founder describes going home depressed by what he saw",
         "claim": "Citadel's Ken Griffin described a step change in which doctoral-level "
                  "financial work that once took years is now done by agents in hours or days, "
                  "and admitted he went home one Friday fairly depressed by what he had "
                  "witnessed.",
         "domain": "economics", "actor": ["citadel"],
         "evidences": ["work-displaced", "cognitive-load-inverted"],
         "supersedes": [B + "developments/2026-05-16-ten-thousand-cross-twenty-million"],
         "body": "The displacement series has mostly recorded juniors. This is the top of the "
                 "skill distribution reacting."},
        {"id": "2026-05-17-an-index-rewritten-for-one-listing",
         "title": "An exchange rewrites index rules so one listing qualifies immediately",
         "claim": "NASDAQ is reportedly rewriting its rules so SpaceX can join its flagship "
                  "index right after listing, a move that would force index funds to buy roughly "
                  "$25 billion of the stock automatically.",
         "domain": "economics", "actor": ["nasdaq", "spacex"], "score": "$25B forced buying",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-15-thirty-billion-at-nine-hundred"]},
        {"id": "2026-05-17-malta-gives-every-citizen-a-subscription",
         "title": "A country gives every citizen a frontier subscription and a literacy course",
         "claim": "Malta became the first country to give every citizen a ChatGPT Plus "
                  "subscription and an AI-literacy course, while London's King's Cross became a "
                  "global AI hub hosting several frontier labs.",
         "domain": "policy", "actor": ["malta", "openai"],
         "evidences": ["legislating-the-shift", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-05-ai-literacy-hardwired-into-schools"]},
    ],
}
