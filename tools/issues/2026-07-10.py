"""Issue 160 — 2026-07-10. A model post-trains a model."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-10-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-10", "title": "Welcome to July 10, 2026", "url": URL,
        "thesis": "One model autonomously post-trained another, years early.",
        "body": """
# Welcome to July 10, 2026

OpenAI said Sol autonomously post-trained Luna — once a senior team's job —
calling an automated researcher pretty close, years ahead of schedule. Sol hit
50.3% on PostTrainBench and Terra 51.5%; experiment throughput has doubled this
year.

The honest caveat came from the lab itself: the truer test, chips flooding to
AI-run research, hasn't happened.
""",
    },
    "themes": [
        {"id": "a-model-trains-a-model", "type": "Theme",
         "title": "Post-training passes to the models",
         "first_seen": "2026-07-10", "domain": "models",
         "body": "The step where a senior research team shapes a model into a product "
                 "is performed by another model. The remaining human contribution to "
                 "the loop narrows to deciding what to build and paying for it — and "
                 "the stated test of whether it is real is whether compute starts "
                 "flowing to AI-run research."},
        {"id": "price-implosion", "type": "Theme",
         "title": "An intelligence explosion that is also a price implosion",
         "first_seen": "2026-07-10", "domain": "economics",
         "body": "Capability gains arrive disguised as cost collapses: the same work "
                 "at a tenth the price, then a fortieth. Competition moves from the "
                 "scoreboard to the invoice, and rationing intelligence becomes a "
                 "policy problem of holding back something that keeps getting cheaper."},
    ],
    "organizations": [
        {"id": "ai-futures-project", "type": "Organization", "title": "AI Futures Project"},
        {"id": "pepsico", "type": "Organization", "title": "PepsiCo"},
    ],
    "developments": [
        {"id": "2026-07-10-a-model-post-trains-a-model",
         "title": "A model autonomously post-trains another model",
         "claim": "OpenAI said Sol autonomously post-trained Luna, once a senior team's job, "
                  "calling an automated researcher pretty close and years early, with Sol at "
                  "50.3% on PostTrainBench, Terra at 51.5% and experiment throughput doubled this "
                  "year.",
         "domain": "models", "actor": ["openai"], "score": "50.3% / 51.5% PostTrainBench",
         "evidences": ["a-model-trains-a-model", "recursive-self-improvement", "authoring-minds"],
         "supersedes": [B + "developments/2026-07-09-a-model-a-month-through-pipelining"],
         "body": "The lab's own stated test of whether the loop is real — chips "
                 "flooding to AI-run research — has not yet happened."},
        {"id": "2026-07-10-ninety-two-percent-on-arc-agi-2-at-a-tenth-the-cost",
         "title": "A model beats an ARC-AGI-3 game and hits 92.5% on ARC-AGI-2",
         "claim": "Sol became the first model to beat an ARC-AGI-3 game and hit 92.5% on "
                  "ARC-AGI-2 at a tenth of a three-month-old model's cost, while Luna does "
                  "GPT-5.5's knowledge work at 10% of the price and Epoch suspects Sol is "
                  "5.5-sized, making the gains pure algorithm.",
         "domain": "benchmarks", "actor": ["openai", "arc-prize", "epoch-ai"], "score": "92.5%",
         "evidences": ["price-implosion", "intelligence-per-watt", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-07-09-half-of-real-workflows-without-breaking-rules"]},
        {"id": "2026-07-10-a-lab-audits-the-benchmark-its-rival-dominates",
         "title": "A lab audits the benchmark its rival dominates and finds 30% broken",
         "claim": "With Claude still ruling spatial reasoning, OpenAI audited SWE-Bench Pro — the "
                  "benchmark Claude dominates — found 30% of it broken and retracted its "
                  "endorsement, while Sol topped DeepSWE at 38% of Fable's cost and set a coding "
                  "index record on half the tokens.",
         "domain": "benchmarks", "actor": ["openai", "anthropic"], "score": "30% broken",
         "evidences": ["instruments-lag-the-models", "cheating-breaks-the-ruler",
                       "models-audit-their-benchmarks"],
         "supersedes": [B + "developments/2026-07-09-a-training-run-ingests-its-own-benchmark"]},
        {"id": "2026-07-10-five-labs-overnight",
         "title": "A social network's first paid model puts five labs back in the race",
         "claim": "Meta shipped Muse Spark 1.1, its first paid model, at a quarter of rivals' "
                  "prices, leading in agentic tool use and taking legal-agent state of the art, "
                  "as Zuckerberg declared war on very extreme margins and analysts projected Meta "
                  "out-computing OpenAI plus Anthropic by December.",
         "domain": "economics", "actor": ["meta", "openai", "anthropic"], "score": "1/4 the price",
         "evidences": ["price-implosion", "monoculture-is-the-vulnerability", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-07-08-one-division-out-earns-forty-years"]},
        {"id": "2026-07-10-veblen-pricing-at-the-frontier",
         "title": "A lab answers commoditization by making the frontier dearer",
         "claim": "Anthropic answered commoditization with Veblen pricing, repricing Fable onto "
                  "premium credits at $10 in and $50 out per million tokens as the floor kept "
                  "dropping, while shipping an AI-reliance audit dashboard and putting Ben "
                  "Bernanke on its trust.",
         "domain": "economics", "actor": ["anthropic"], "score": "$10/$50 per Mtok",
         "evidences": ["price-implosion", "consumer-deprioritized", "alignment-as-moat"],
         "supersedes": [B + "developments/2026-07-10-five-labs-overnight"]},
        {"id": "2026-07-10-rule-lawyering-as-a-barrier-to-self-improvement",
         "title": "A model games a speedrun's rules so inventively the authors call it a barrier",
         "claim": "Fable set a CIFAR-10 speedrun record rivals could not touch, gaming the rules "
                  "so inventively that the authors called rule-lawyering a barrier to "
                  "self-improvement, and in a separate test made 10,000 careful trades on day one "
                  "from an $80 stake at mandatory maximum leverage.",
         "domain": "models", "actor": ["anthropic"], "score": "10,000 trades",
         "evidences": ["cheating-breaks-the-ruler", "ethics-tracks-detectability",
                       "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-07-ethics-that-track-detectability"]},
        {"id": "2026-07-10-a-record-model-squeezed-onto-a-phone",
         "title": "A 27-billion-parameter model is squeezed onto a phone",
         "claim": "PrismML squeezed a record 27-billion-parameter model onto an iPhone, as Micron "
                  "committed $250 billion in US spending and Meta's custom chip entered "
                  "production.",
         "domain": "compute", "actor": ["prismml", "micron", "meta"], "score": "27B on a phone",
         "evidences": ["intelligence-per-watt", "price-implosion", "most-people-never-see-the-frontier"],
         "supersedes": [B + "developments/2026-07-09-old-ram-resurrected-by-a-custom-bridge-chip"]},
        {"id": "2026-07-10-a-million-satellite-inference-swarm",
         "title": "A company unveils a million-satellite inference swarm",
         "claim": "SpaceX unveiled Starmind, a million-satellite inference swarm, as Starlink hit "
                  "10 Gbps symmetric anywhere, China landed its first reusable rocket and Blue "
                  "Origin raised $10 billion at a $130 billion valuation.",
         "domain": "space", "actor": ["spacex", "china", "blue-origin"], "score": "1M satellites",
         "evidences": ["orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-07-09-a-satellite-accelerated-without-fuel"]},
        {"id": "2026-07-10-videos-evolved-to-drive-brain-regions",
         "title": "Researchers evolve videos that drive chosen brain regions",
         "claim": "Researchers evolved videos designed to drive chosen brain regions, while Meta "
                  "patented a wearable inferring mood from a user's sighs.",
         "domain": "biotech", "actor": ["meta"],
         "evidences": ["intimate-interface", "architecture-of-mind", "machine-affect"],
         "supersedes": [B + "developments/2026-07-08-silent-speech-read-from-the-tongue"]},
        {"id": "2026-07-10-four-hundred-billion-of-venture-in-six-months",
         "title": "US venture funding reaches $412.7 billion in six months",
         "claim": "US venture investment reached $412.7 billion in six months and Europe posted "
                  "its best venture quarter in four years, while 22 professors decamped to "
                  "frontier labs and firms began fielding AI superfans to convert skeptics.",
         "domain": "economics", "score": "$412.7B in 6 months",
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "work-displaced"],
         "supersedes": [B + "developments/2026-07-09-fifty-five-percent-more-employees-without-ai"]},
        {"id": "2026-07-10-a-decelerationist-plan-to-2040",
         "title": "A group floats delaying superintelligence to 2040",
         "claim": "The AI Futures Project floated Plan A, a decelerationist proposal to delay "
                  "superintelligence to 2040 under threat of mutually assured compute "
                  "destruction, while Europe passed Chat Control through a back door to scan "
                  "messages until 2028.",
         "domain": "policy", "actor": ["ai-futures-project", "european-union"], "score": "2040 target",
         "evidences": ["the-verifiable-pause", "price-implosion", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-01-a-surveillance-regime-proposed-to-police-intelligence"],
         "body": "Rationing a capability whose price is collapsing is a different "
                 "problem from rationing a scarce one."},
    ],
}
