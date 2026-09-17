"""Issue 148 — 2026-06-26. Stagger the release, never the mind."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-26-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-26", "title": "Welcome to June 26, 2026", "url": URL,
        "thesis": "Throttling release slows shipping, not training.",
        "body": """
# Welcome to June 26, 2026

The White House asked OpenAI to stagger the release of GPT-5.6 over security
concerns, and the company agreed — setting a new normal for frontier releases.

The structural consequence, as one observer noted, is that throttling slows
only how fast labs *ship*, not how fast they *train*. The distance between the
public frontier and the internal one widens from here, and the old joke about
AGI already existing internally becomes literally true.
""",
    },
    "themes": [
        {"id": "public-internal-divergence", "type": "Theme",
         "title": "The public frontier detaches from the real one",
         "first_seen": "2026-06-26", "domain": "policy",
         "body": "Release throttling constrains shipping but not training, so the gap "
                 "between what exists inside a lab and what anyone outside can see "
                 "widens monotonically. Every public benchmark, forecast and policy "
                 "debate from here is arguing about a lagging shadow."},
    ],
    "organizations": [
        {"id": "unconventional-ai", "type": "Organization", "title": "Unconventional AI"},
        {"id": "absci", "type": "Organization", "title": "Absci"},
        {"id": "aleph-bio", "type": "Organization", "title": "Aleph"},
        {"id": "vesuvius-challenge", "type": "Organization", "title": "Vesuvius Challenge"},
    ],
    "people": [
        {"id": "brian-roemmele", "type": "Person", "title": "Brian Roemmele", "name": "Brian Roemmele",
         "description": "Technology commentator on X whose forecast that Mythos-class and OpenAI-6-class "
                        "weights would go free and open within eight months the newsletter sets against "
                        "Washington's release-throttling policy.",
         "resource": "https://x.com/brianroemmele",
         # tags deliberately omitted: no controlled entity tag fits an independent commentator,
         # and neither the newsletter nor his linked source states a position (verified 2026-09-17).
         "body": "Brian Roemmele posts commentary on AI and technology on X "
                 "([profile](https://x.com/brianroemmele)). He appears in this corpus once, in the "
                 "June 26 item where observers call the staggered-release policy "
                 "[self-defeating](/developments/2026-06-26-a-policy-that-does-not-touch-the-race.md): "
                 "he called the wounds self-inflicted and predicted that Mythos-class and OpenAI-6-class "
                 "weights go free and open within eight months, a dated forecast the corpus can check "
                 "against the [open-weight-latency](/themes/open-weight-latency.md) strand."},
    ],
    "developments": [
        {"id": "2026-06-26-the-public-frontier-detaches",
         "title": "A lab agrees to stagger a release, widening the public-internal gap",
         "claim": "The White House asked OpenAI to stagger the release of GPT-5.6 over security "
                  "concerns and Sam Altman told staff the firm would comply, setting a new norm "
                  "for frontier releases after the administration's showdown with Anthropic.",
         "domain": "policy", "actor": ["white-house", "openai", "anthropic"],
         "evidences": ["public-internal-divergence", "models-as-munitions", "rationed-recursion"],
         "supersedes": [B + "developments/2026-06-22-five-eyes-warns-months-away"],
         "body": "Throttling slows only how fast labs ship, not how fast they train. "
                 "One observer noted this finally makes the old joke that AGI has "
                 "already been developed internally literally true — and that with "
                 "capability compounding in private, China gets to catch a public "
                 "frontier that is no longer the real one."},
        {"id": "2026-06-26-a-policy-that-does-not-touch-the-race",
         "title": "Observers call the throttling policy self-defeating",
         "claim": "Observers noted the staggered-release policy does not touch the race to "
                  "recursive self-improvement, raising the question of what happens when Chinese "
                  "releases outpace what the US permits its own labs to ship, with one commenter "
                  "predicting Mythos-class weights go free and open within eight months.",
         "description": "A brake on shipping is read as no brake at all on the loop that trains the next "
                        "model, reversing the fortnight-old reading of export control as the first "
                        "regulation of self-improvement, and therefore as a gift to whoever is not braking.",
         "domain": "policy", "actor": ["people/brian-roemmele"], "score": "8 months",
         "about": [B + "systems/claude-mythos"],
         "evidences": ["public-internal-divergence", "recursive-self-improvement", "silicon-curtain",
                       "rationed-recursion"],
         "supersedes": [B + "developments/2026-06-26-the-public-frontier-detaches"],
         "relatedTo": [B + "developments/2026-06-08-mutual-conditional-pause-pilled",
                       B + "developments/2026-06-27-a-tiered-planet-of-model-access"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-06-13-a-model-becomes-export-controlled",
                        "relation_label": "contradicts"}],
         "tags": ["policy", "rsi", "open-weights", "forecast"],
         "supporting_text": "so the policy is self-defeating",
         "sources": [{"id": "deredleritt3r-rsi-race-post",
                      "resource": "https://x.com/deredleritt3r/status/2070260358078476723",
                      "title": "Post on X: the staggered-release policy does not touch the race to recursive self-improvement",
                      "author": "human:deredleritt3r", "last_modified": "2026-06-25"},
                     {"id": "pielstick-chinese-releases-outpace-post",
                      "resource": "https://x.com/benpielstick/status/2070280800394989706",
                      "title": "Post on X asking what happens when Chinese releases outpace what the US lets its own labs ship",
                      "author": "human:ben-pielstick", "last_modified": "2026-06-25"},
                     {"id": "roemmele-weights-free-in-eight-months-post",
                      "resource": "https://x.com/brianroemmele/status/2070338916121735315",
                      "title": "Post on X predicting Mythos-class and OpenAI-6-class weights go free and open in eight months",
                      "author": "human:brian-roemmele", "last_modified": "2026-06-26"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The newsletter strings three X posts into one argument: a pseudonymous observer's point "
                 "that [staggering releases](/developments/2026-06-26-the-public-frontier-detaches.md) "
                 "leaves [the race to recursive self-improvement](/themes/recursive-self-improvement.md) "
                 "untouched ([post](https://x.com/deredleritt3r/status/2070260358078476723)), Ben Pielstick's "
                 "question of what happens when Chinese releases outpace what Washington lets US labs ship "
                 "([post](https://x.com/benpielstick/status/2070280800394989706)), and "
                 "[Brian Roemmele](/people/brian-roemmele.md)'s forecast that Mythos-class and OpenAI-6-class "
                 "weights go free and open within eight months "
                 "([post](https://x.com/brianroemmele/status/2070338916121735315)). It sits in the policy "
                 "sub-strand of the recursion trajectory: two weeks after an analyst read the "
                 "[Fable and Mythos export-control directive](/developments/2026-06-13-a-model-becomes-export-controlled.md) "
                 "as accidentally the first regulation of self-improvement, this item argues the opposite, "
                 "that throttling governs only the public frontier while the internal one keeps compounding, "
                 "the worry behind Roon's [mutual conditional pause agreements](/developments/2026-06-08-mutual-conditional-pause-pilled.md) "
                 "earlier in the month. The next issue's "
                 "[tiered planet of model access](/developments/2026-06-27-a-tiered-planet-of-model-access.md) "
                 "picks up the thread."},
        {"id": "2026-06-26-images-generated-on-coupled-oscillators",
         "title": "Images are generated on a simulated lattice of coupled oscillators",
         "claim": "Unconventional AI's Un-0 generates images on a simulated lattice of coupled "
                  "Kuramoto oscillators, a physical substrate chasing a thousandfold better "
                  "energy efficiency while matching the quality leading image generators "
                  "launched with.",
         "domain": "compute", "actor": ["unconventional-ai"], "score": "1000x efficiency target",
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-06-25-an-inference-chip-taped-out-in-nine-months"]},
        {"id": "2026-06-26-an-agent-generates-almost-all-its-own-output",
         "title": "A coding agent generates 99.8% of its own weekly output tokens",
         "claim": "OpenAI's numbers show Codex now generating 99.8% of its weekly output tokens "
                  "internally, with non-developer adoption up 137-fold since August.",
         "description": "The February anecdote that the coding agent builds itself acquires a "
                        "denominator: a lab's own accounting of how much of the agent's output the "
                        "agent now produces, and of how far beyond developers its use has spread.",
         "domain": "agents", "actor": ["openai"], "score": "99.8% / 137x adoption",
         "about": [B + "systems/codex"],
         "evidences": ["recursive-self-improvement", "self-authored-scaffolding", "work-displaced"],
         "supersedes": [B + "developments/2026-06-25-an-agent-rewrites-its-own-harness",
                        B + "developments/2026-02-03-codex-builds-itself"],
         "relatedTo": [B + "developments/2026-02-08-100pct-of-product-code",
                       B + "developments/2026-03-16-rsi-is-a-present-phenomenon",
                       B + "developments/2026-08-01-agents-write-almost-all-output-tokens"],
         "tags": ["rsi", "ai-r-and-d", "labor"],
         "supporting_text": "show Codex now generating 99.8% of its weekly output tokens internally",
         "sources": [{"id": "openai-how-agents-are-transforming-work",
                      "resource": "https://openai.com/index/how-agents-are-transforming-work/",
                      "title": "How agents are transforming work", "author": "org:openai"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "OpenAI's own report ([How agents are transforming work](https://openai.com/index/how-agents-are-transforming-work/)) "
                 "puts [Codex](/systems/codex.md) at 99.8% of its weekly output tokens generated internally, "
                 "with non-developer adoption up 137-fold since August. The newsletter files it under the work "
                 "mutating, beside a survey of Chinese labs hiring engineers with a third the experience: the "
                 "bodies are still needed, for different work. In the trajectory it is the quantified successor "
                 "to a Codex manager saying in February that "
                 "[the product pretty much builds itself](/developments/2026-02-03-codex-builds-itself.md) and "
                 "to Anthropic's [effectively 100% of product code](/developments/2026-02-08-100pct-of-product-code.md), "
                 "and it corroborates the alignment lead's March claim that "
                 "[recursive self-improvement is already happening](/developments/2026-03-16-rsi-is-a-present-phenomenon.md); "
                 "the same 99.8% figure resurfaces in August in the finance chief's "
                 "[abundant-intelligence strategy](/developments/2026-08-01-agents-write-almost-all-output-tokens.md)."},
        {"id": "2026-06-26-chinese-labs-hire-at-a-third-the-experience",
         "title": "A survey finds Chinese labs hiring engineers with a third the experience",
         "claim": "A survey of 1,604 job postings across six Chinese labs found them still "
                  "leaning on Nvidia while building domestic chips and data centers, hiring "
                  "engineers with a third the experience US labs demand.",
         "domain": "economics", "actor": ["china", "nvidia"], "score": "1,604 postings",
         "evidences": ["silicon-curtain", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-06-26-a-policy-that-does-not-touch-the-race"]},
        {"id": "2026-06-26-a-third-wave-of-inflation-reaches-the-checkout",
         "title": "A device maker raises prices for the first time over memory costs",
         "claim": "Apple raised Mac and iPad prices by $200 or more, its first move to pass "
                  "soaring memory costs to consumers, sending shares to their worst day in over "
                  "a year, part of a third wave of inflation rippling from data centers to power "
                  "bills that Tim Cook called unlike anything in four decades.",
         "domain": "economics", "actor": ["apple"], "score": "+$200 or more",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-19-smartphone-shipments-to-fall-fifteen-percent"]},
        {"id": "2026-06-26-sub-one-nanometer-chips",
         "title": "A sub-one-nanometer node crams 100 billion transistors onto a fingernail",
         "claim": "IBM unveiled sub-1-nanometer chips, a 0.7-nm nanostack node cramming nearly "
                  "100 billion transistors onto a fingernail and promising up to 70% better "
                  "efficiency within five years.",
         "domain": "compute", "actor": ["ibm"], "score": "0.7 nm / 100B transistors",
         "evidences": ["vertical-silicon", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-25-a-scaling-law-to-replace-moores-law"]},
        {"id": "2026-06-26-an-ai-designed-antibody-clears-early-safety",
         "title": "An AI-designed antibody clears early safety and draws a $100M round",
         "claim": "Absci jumped 24% on early safety data for its AI-designed hair-loss antibody, "
                  "drawing a $100 million round led by Eli Lilly that also bets on an "
                  "endometriosis treatment.",
         "domain": "biotech", "actor": ["absci", "eli-lilly"], "score": "$100M round",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-06-25-a-language-that-composes-dna-rna-and-protein"]},
        {"id": "2026-06-26-a-living-brain-imaged-through-the-skull",
         "title": "A living brain's vasculature is imaged through the intact skull",
         "claim": "Aleph imaged a living brain's vasculature through the intact skull with "
                  "ultrasound and open-sourced the pipeline, a step toward a wearable, MRI-grade "
                  "mind interface, while the Unitree R1 humanoid dropped to $4,900.",
         "domain": "biotech", "actor": ["aleph-bio", "unitree"], "score": "$4,900 humanoid",
         "evidences": ["intimate-interface", "architecture-of-mind", "physical-recursion"],
         "supersedes": [B + "developments/2026-06-25-brain-to-brain-through-latent-space"]},
        {"id": "2026-06-26-doctrine-lets-ai-initiate-wartime-actions",
         "title": "A defense ministry rewrites doctrine to let AI initiate wartime actions",
         "claim": "The Pentagon quietly rewrote its targeting doctrine to let AI initiate "
                  "wartime actions under human watch, inching past human-in-the-loop, while "
                  "California launched a first-in-the-nation AI-unemployment tracker finding no "
                  "statewide jobs apocalypse yet, only localized pain among exposed "
                  "degree-holders.",
         "domain": "policy", "actor": ["pentagon", "california"],
         "evidences": ["violence-arrives", "work-displaced", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-06-24-directed-energy-downs-drones-autonomously"]},
        {"id": "2026-06-26-the-first-signature-of-an-event-horizon",
         "title": "Astronomers catch the first signature of a black hole's event horizon",
         "claim": "Astronomers logged the first signature ever caught of a black hole's event "
                  "horizon, the long-theorized direct wave surfacing in event GW250114 and "
                  "matching a Kerr solution, while Perseverance found macromolecular carbon in "
                  "Jezero's ancient mudstones, the most robust organic detection yet.",
         "domain": "science", "actor": ["nasa"],
         "evidences": ["root-node-problems", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-06-20-a-private-mission-may-beat-spacex-to-mars"]},
        {"id": "2026-06-26-a-scroll-sealed-since-79-ad-is-read-end-to-end",
         "title": "A scroll sealed since 79 AD is fully unwrapped and read",
         "claim": "The Vesuvius Challenge fully unwrapped Herculaneum scroll PHerc. 1667, sealed "
                  "since 79 AD and read end to end at last, revealing a Stoic treatise on ethics.",
         "domain": "science", "actor": ["vesuvius-challenge"],
         "evidences": ["resurrection-and-time", "automated-science"],
         "supersedes": [B + "developments/2026-06-25-a-physicist-credits-a-model-in-a-paper"]},
    ],
}
