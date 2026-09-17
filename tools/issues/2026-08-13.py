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
    "systems": [
        {"id": "grok-4-6", "type": "AISystem", "title": "Grok 4.6",
         "developed_by": [B + "organizations/xai"], "modality": "text",
         "description": "xAI's August 2026 model, reported to rejoin the frontier at a fraction of the cost and on par with GPT-5.6 Sol Max.",
         "resource": "https://x.ai/news/grok-4-6",
         "tags": ["reasoning-model"],
         "body": "Grok 4.6 is xAI's August 2026 release ([xAI](https://x.ai/news/grok-4-6)). The newsletter records it "
                 "[rejoining the frontier](/developments/2026-08-13-a-cofounder-steers-toward-recursive-self-improvement.md) "
                 "at a fraction of the cost and on par with [GPT-5.6 Sol](/systems/gpt-5-6-sol.md) Max, with Elon Musk "
                 "promising a SpaceX-data-marinated 4.7 within a month. It follows [Grok 4.20](/systems/grok-4-20.md) "
                 "in the corpus's Grok lineage."},
    ],
    "people": [
        {"id": "sergey-brin", "type": "Person", "title": "Sergey Brin", "name": "Sergey Brin",
         "description": "Google co-founder who, per Reuters, is using his founder's standing inside the company to steer resources toward recursive self-improvement.",
         "resource": "https://x.com/sergeybrinn",
         "sameAs": ["http://www.wikidata.org/entity/Q92764"],
         "tags": ["founder", "executive"],
         "body": "Sergey Brin co-founded Google in 1998 and, in the newsletter's account of the 2026 reshuffle, "
                 "retakes the bridge of its AI effort as [DeepMind is declared no longer a frontier lab](/developments/2026-08-08-a-lab-declared-no-longer-frontier.md). "
                 "In this corpus he appears when Reuters reports him "
                 "[steering resources toward recursive self-improvement](/developments/2026-08-13-a-cofounder-steers-toward-recursive-self-improvement.md), "
                 "which the newsletter glosses as the point where the technology stops needing him; the same reshuffle "
                 "saw [Demis Hassabis](/people/demis-hassabis.md) [step back from DeepMind's day-to-day](/developments/2026-08-05-a-lab-chief-steps-back-as-agi-feels-close-at-hand.md)."},
    ],
    "roles": [
        {"id": "sergey-brin-google-co-founder", "type": "Role",
         "title": "Sergey Brin, co-founder of Google",
         "roleName": "Co-founder",
         "startDate": "1998",
         "memberOf": [B + "organizations/google"],
         "holder": [B + "people/sergey-brin"],
         "description": "The founder's standing, co-founder gravity in the newsletter's phrase, from which he is reported to be steering Google's resources toward recursive self-improvement.",
         "body": "The newsletter identifies him by this role when it reports him using co-founder gravity to "
                 "[steer resources toward recursive self-improvement](/developments/2026-08-13-a-cofounder-steers-toward-recursive-self-improvement.md) "
                 "inside [Google](/organizations/google.md). It is the role that makes the report matter: not a lab "
                 "head or a strategy officer but the company's founder directing money at the loop."},
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
         "description": "A founder's personal authority is reportedly spent on the loop itself, the newsletter "
                        "noting that the destination is the point where the technology stops needing him.",
         "domain": "models", "occurred_on": "2026-08-12",
         "actor": ["google", "xai", "openai", "cerebras", "people/sergey-brin"], "score": "14x faster",
         "evidences": ["recursive-self-improvement", "price-implosion", "hiring-as-roadmap"],
         "about": [B + "systems/grok-4-6", B + "systems/gpt-5-6-sol"],
         "supersedes": [B + "developments/2026-08-10-a-westinghouse-style-bet-on-diffusion",
                        B + "developments/2026-08-04-recursive-self-improvement-justifies-the-capex",
                        B + "developments/2026-08-05-a-lab-chief-steps-back-as-agi-feels-close-at-hand"],
         "relatedTo": [B + "people/demis-hassabis",
                       B + "developments/2026-08-08-a-lab-declared-no-longer-frontier",
                       B + "developments/2026-07-19-we-want-k2-to-help-build-k3"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-08-04-recursive-self-improvement-justifies-the-capex",
                        "relation_label": "corroborates"}],
         "tags": ["rsi", "ai-r-and-d", "capability-jump"],
         "supporting_text": "steer resources toward recursive self-improvement, the point where the technology stops needing him",
         "sources": [{"id": "reuters-google-ai-reshuffle-executive-moves",
                      "resource": "https://www.reuters.com/world/inside-google-executive-moves-that-led-its-big-ai-reshuffle-2026-08-12/",
                      "title": "Inside Google, the executive moves that led to its big AI reshuffle",
                      "author": "org:reuters", "last_modified": "2026-08-12"},
                     {"id": "openai-previewing-ultrafast",
                      "resource": "https://openai.com/index/previewing-ultrafast/",
                      "title": "Previewing Ultrafast", "author": "org:openai"},
                     {"id": "xai-introducing-grok-4-6",
                      "resource": "https://x.ai/news/grok-4-6",
                      "title": "Introducing Grok 4.6", "author": "org:xai", "last_modified": "2026-08-12"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Reuters' account of the executive moves behind Google's AI reshuffle reports that "
                 "[Sergey Brin](/people/sergey-brin.md) is steering resources toward recursive self-improvement "
                 "([Reuters](https://www.reuters.com/world/inside-google-executive-moves-that-led-its-big-ai-reshuffle-2026-08-12/)), "
                 "what the newsletter calls co-founder gravity and reads as the point where the technology stops "
                 "needing him. It closes a loop "
                 "that opened nine days earlier when "
                 "[DeepMind's strategy chief said the capex is a bet on RSI](/developments/2026-08-04-recursive-self-improvement-justifies-the-capex.md) "
                 "and [Hassabis stepped back from the day-to-day](/developments/2026-08-05-a-lab-chief-steps-back-as-agi-feels-close-at-hand.md): "
                 "the company's founder now personally directs money at the recursion. The same issue notes the "
                 "frontier sprinting around it, with [Grok 4.6](/systems/grok-4-6.md) rejoining the frontier at a "
                 "fraction of the cost and OpenAI previewing Ultrafast, a Cerebras-powered tier running "
                 "[GPT-5.6 Sol](/systems/gpt-5-6-sol.md) 14 times faster."},
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
