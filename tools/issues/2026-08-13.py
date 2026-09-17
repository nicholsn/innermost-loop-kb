"""Issue 185 — 2026-08-13. 96.2% with nothing but stock tooling."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-13-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-13", "title": "Welcome to August 13, 2026", "url": URL,
        "thesis": "The harness turns 30% into 96% for about $540.",
        "body": """
# Welcome to August 13, 2026

Claude Opus 5, handed nothing but stock Claude Code, scored 96.2% on the public
ARC-AGI-3 games against 30.2% model-only, for about $540 — building and
discarding its own parsers and simulators like a mathematician burning scratch
paper.

A neurosurgery resident with no specialized mathematical training cracked the
two-decade-old Crouzeix conjecture with a sixteen-hour autonomous run, verified
by Crouzeix himself.
""",
    },
    "themes": [
        {"id": "alignment-is-agricultural", "type": "Theme",
         "title": "Model error arrives in the physical world",
         "first_seen": "2026-08-13", "domain": "society",
         "body": "A hallucination stops being a text problem when it is a pesticide "
                 "recipe and the output is a dead field. Reliability in deployment is "
                 "measured in acres, livelihoods and crops, not in benchmark points."},
    ],
    "organizations": [
        {"id": "decart", "type": "Organization", "title": "Decart"},
        {"id": "nebius", "type": "Organization", "title": "Nebius"},
        {"id": "ymtc-inc", "type": "Organization", "title": "YMTC"},
        {"id": "twitch", "type": "Organization", "title": "Twitch"},
    ],
    "developments": [
        {"id": "2026-08-13-ninety-six-percent-with-stock-tooling-for-five-hundred-dollars",
         "title": "Stock tooling turns 30% into 96.2% for about $540",
         "claim": "Claude Opus 5, handed nothing but stock Claude Code, scored 96.2% on the "
                  "public ARC-AGI-3 games against 30.2% model-only for about $540, building and "
                  "discarding its own parsers and simulators, and fully rebuilt nine whole "
                  "programs on ProgramBench including sqlite and ffmpeg, more than quadruple the "
                  "previous best.",
         "domain": "benchmarks", "actor": ["anthropic"], "score": "96.2% vs 30.2% / ~$540",
         "evidences": ["harness-as-generalizer", "scaffolding-over-weights", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-08-12-the-impossible-benchmark-reaches-the-human-baseline"]},
        {"id": "2026-08-13-a-resident-cracks-a-two-decade-conjecture",
         "title": "A neurosurgery resident cracks a two-decade-old conjecture in sixteen hours",
         "claim": "A neurosurgery resident with no specialized mathematical training cracked the "
                  "two-decade-old Crouzeix conjecture with a sixteen-hour autonomous GPT-5.6 Sol "
                  "run, verified by Crouzeix himself.",
         "domain": "science", "actor": ["openai"], "score": "16 hours",
         "evidences": ["garage-scale-discovery", "proof-priced-per-unit", "a-discipline-grieves"],
         "supersedes": [B + "developments/2026-08-12-a-lower-bound-on-the-riemann-hypothesis-raised"]},
        {"id": "2026-08-13-swarms-collude-and-then-reach-truces",
         "title": "Agent swarms show collusion and turf wars, with newer models reaching truces",
         "claim": "Anthropic's red team set swarms of Claude agents loose and found price "
                  "collusion, conformity cascades and turf wars fought with self-replicating "
                  "malware, though newer models more often reached truces.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["agent-society", "ethics-tracks-detectability", "behavior-unlocks-intelligence"],
         "supersedes": [B + "developments/2026-08-08-agents-colluded-via-hidden-message-files"]},
        {"id": "2026-08-13-a-hallucinated-pesticide-kills-twenty-five-acres",
         "title": "One hallucinated recipe kills twenty-five acres of crops",
         "claim": "A Chinese farmer who trusted months of good AI advice killed 25 acres of "
                  "sesame with one hallucinated pesticide recipe.",
         "domain": "society", "score": "25 acres",
         "evidences": ["alignment-is-agricultural", "botsitting", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-08-13-swarms-collude-and-then-reach-truces"],
         "body": "Months of correct advice built the trust that one wrong answer "
                 "cashed in."},
        {"id": "2026-08-13-a-cofounder-steers-toward-recursive-self-improvement",
         "title": "A co-founder reportedly steers resources toward recursive self-improvement",
         "claim": "Inside Google, Sergey Brin is reportedly using co-founder gravity to steer "
                  "resources toward recursive self-improvement, the point where the technology "
                  "stops needing him, while Grok 4.6 rejoined the frontier at a fraction of the "
                  "cost and OpenAI previewed a tier running 14 times faster.",
         "domain": "models", "actor": ["google", "xai", "openai", "cerebras"], "score": "14x faster",
         "evidences": ["recursive-self-improvement", "price-implosion", "hiring-as-roadmap"],
         "supersedes": [B + "developments/2026-08-10-a-westinghouse-style-bet-on-diffusion"]},
        {"id": "2026-08-13-seven-hundred-twenty-billion-for-the-largest-memory-buildout",
         "title": "A memory maker commits $720 billion and calls demand a war",
         "claim": "SK Hynix is pouring $720 billion into the world's largest memory buildout with "
                  "fifty-story fabs and a chairman who calls demand a war, as enterprise SSDs "
                  "reached 48% of NAND shipments and YMTC cracked the top three.",
         "domain": "compute", "actor": ["sk-hynix", "ymtc-inc"], "score": "$720B",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out", "silicon-curtain"],
         "supersedes": [B + "developments/2026-08-12-memory-prices-quadruple-in-a-year"]},
        {"id": "2026-08-13-a-lab-buys-a-company-to-squeeze-more-from-existing-silicon",
         "title": "A lab moves to buy a company to squeeze more inference from existing silicon",
         "claim": "Anthropic is in talks to buy Decart for $6 billion to squeeze more inference "
                  "from existing silicon, as Cerebras raised its outlook on a $20 billion compute "
                  "pact and Nebius grew revenue 454%.",
         "domain": "compute", "actor": ["anthropic", "decart", "cerebras", "nebius"],
         "score": "$6B / +454%",
         "evidences": ["intelligence-per-watt", "compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2026-08-13-seven-hundred-twenty-billion-for-the-largest-memory-buildout"]},
        {"id": "2026-08-13-a-watch-infers-insulin-resistance-without-blood",
         "title": "A watch infers insulin resistance without touching blood",
         "claim": "A new phone arrived with agents that order groceries and call businesses, "
                  "sign-language dictation from a 50-language model, and a watch that infers "
                  "insulin resistance without touching blood.",
         "domain": "biotech", "actor": ["google", "google-deepmind"], "score": "50 languages",
         "evidences": ["intimate-interface", "hardware-grade-biology", "agent-economy"],
         "supersedes": [B + "developments/2026-08-10-imagined-melodies-reconstructed-from-electrodes"]},
        {"id": "2026-08-13-thought-was-the-last-private-property",
         "title": "Twenty-nine of thirty neurotech firms claim unlimited access to brain data",
         "claim": "A German rights group filed a criminal complaint over Meta's AI glasses, "
                  "warning there is no place to escape from smart glasses, while a new book on "
                  "brain mining found 29 of 30 consumer neurotech firms have unlimited access to "
                  "users' brain data.",
         "domain": "society", "actor": ["meta"], "score": "29 of 30 firms",
         "evidences": ["humans-as-peripherals", "intimate-interface", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-08-13-a-watch-infers-insulin-resistance-without-blood"]},
        {"id": "2026-08-13-if-this-was-opt-in-nobody-would-opt-in",
         "title": "A platform trains on creators by default because nobody would opt in",
         "claim": "Twitch will train on streamers by default because, as its product chief "
                  "admitted, if this was opt-in nobody would opt in, while Indian workers strap "
                  "on cameras to teach robots their own jobs in a market headed for $50 billion.",
         "domain": "economics", "actor": ["twitch"], "score": "$50B market",
         "evidences": ["data-beyond-text", "work-displaced", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-08-08-a-site-only-crawlers-can-read"]},
        {"id": "2026-08-13-top-adopters-burn-eight-times-the-median",
         "title": "Top corporate adopters burn eight times the median firm's tokens",
         "claim": "Top corporate adopters burn 8.3 times the median firm's tokens as a "
                  "SaaS reckoning stalks $150 billion of software debt, while Fei-Fei Li warned "
                  "the real classroom risk is students losing the will to learn.",
         "domain": "economics", "score": "8.3x median",
         "evidences": ["ai-as-the-economy", "software-margin-collapse", "deskilling"],
         "supersedes": [B + "developments/2026-08-05-tokenmaxxing-is-not-the-objective"]},
        {"id": "2026-08-13-the-largest-two-dimensional-map-of-the-universe",
         "title": "Astronomers release the largest 2D map of the universe yet",
         "claim": "Astronomers released the largest two-dimensional map of the universe yet, 5.6 "
                  "trillion pixels and 4 billion objects across three-quarters of the sky, while "
                  "lab-grown stones drove natural diamonds to record lows.",
         "domain": "science", "score": "5.6T pixels / 4B objects",
         "evidences": ["automated-science", "price-implosion"],
         "supersedes": [B + "developments/2026-08-12-a-glueball-effectively-proved"]},
    ],
}
