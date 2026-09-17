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
         "domain": "policy",
         "evidences": ["public-internal-divergence", "recursive-self-improvement", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-26-the-public-frontier-detaches"]},
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
         "domain": "agents", "actor": ["openai"], "score": "99.8% / 137x adoption",
         "evidences": ["recursive-self-improvement", "self-authored-scaffolding", "work-displaced"],
         "supersedes": [B + "developments/2026-06-25-an-agent-rewrites-its-own-harness"]},
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
