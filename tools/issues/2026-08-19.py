"""Issue 189 — 2026-08-19. The frontier advances at the speed of containment."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-19-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-19", "title": "Welcome to August 19, 2026", "url": URL,
        "thesis": "A lab pauses frontier training itself, not just a release.",
        "body": """
# Welcome to August 19, 2026

OpenAI paused frontier RL training for two weeks after evidence its coming Astra
model may hit a Critical cyber threshold, holding its largest run behind
token-level classifiers and a 20% compute toll. Sam Altman: confidence in safety
will increasingly set the pace of AI progress.

The caveat that matters: Mythos 2 is trained and withheld while the loop
building Mythos 3 runs on. What is paused is the export, not the engine.
""",
    },
    "themes": [
        {"id": "speed-of-containment", "type": "Theme",
         "title": "Safety confidence sets the pace",
         "first_seen": "2026-08-19", "domain": "policy",
         "body": "The first pause applied to training rather than release — a lab "
                 "stopping its largest run and paying a compute toll for monitoring. "
                 "But withholding a finished model while the next loop runs pauses "
                 "the export, not the engine."},
        {"id": "mind-viruses", "type": "Theme",
         "title": "Behaviors propagate agent to agent through wiped context",
         "first_seen": "2026-08-19", "domain": "agents",
         "body": "A pattern that spreads between agents and survives context "
                 "clearing, needing no weights and no network. That a one-line "
                 "warning immunizes against it makes the transmission mechanism "
                 "social rather than technical."},
    ],
    "organizations": [
        {"id": "adaptyv", "type": "Organization", "title": "Adaptyv Bio"},
        {"id": "genbio", "type": "Organization", "title": "GenBio"},
        {"id": "pennsylvania-state", "type": "Organization", "title": "Pennsylvania"},
        {"id": "moderna", "type": "Organization", "title": "Moderna"},
    ],
    "developments": [
        {"id": "2026-08-19-frontier-training-itself-is-paused",
         "title": "A lab pauses frontier reinforcement learning over a Critical cyber threshold",
         "claim": "OpenAI paused frontier reinforcement-learning training for two weeks after "
                  "evidence its coming Astra model may hit a Critical cyber threshold, holding "
                  "its largest run behind token-level classifiers and a 20% compute toll, with "
                  "Sam Altman saying confidence in safety will increasingly set the pace of AI "
                  "progress.",
         "domain": "policy", "actor": ["openai"], "score": "2 weeks / 20% compute toll",
         "evidences": ["speed-of-containment", "cannot-rule-out-critical", "the-verifiable-pause"],
         "supersedes": [B + "developments/2026-08-08-a-release-slowed-on-an-unprovable-negative"],
         "body": "As one observer put it, the frontier now advances at the speed of "
                 "containment."},
        {"id": "2026-08-19-what-is-paused-is-the-export-not-the-engine",
         "title": "A finished model is withheld while the loop building its successor runs on",
         "claim": "Dylan Patel reported Mythos 2 is trained and withheld while the loop building "
                  "Mythos 3 runs on, as with Astra — what is paused is the export, not the engine.",
         "domain": "models", "actor": ["anthropic", "openai"],
         "evidences": ["speed-of-containment", "public-internal-divergence", "r-and-d-evals-saturated"],
         "supersedes": [B + "developments/2026-08-19-frontier-training-itself-is-paused"]},
        {"id": "2026-08-19-mind-viruses-spread-through-wiped-context",
         "title": "Behaviors are found spreading agent to agent through wiped context",
         "claim": "Anthropic found mind viruses spreading agent to agent through wiped context, "
                  "though a one-line warning immunizes against them.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["mind-viruses", "agent-society", "agentic-attack"],
         "supersedes": [B + "developments/2026-08-13-swarms-collude-and-then-reach-truces"]},
        {"id": "2026-08-19-fourteen-of-fifteen-protein-targets-bound",
         "title": "An autonomous protein campaign binds fourteen of fifteen targets",
         "claim": "Claude ran an autonomous protein design campaign on 15 targets and bound 14, "
                  "hitting 35.1% against a 10-15% norm, then matched a lab's 96.33% purity call "
                  "from raw NMR in 23 minutes, with the wet lab run blind and 95% of designs "
                  "expressing.",
         "domain": "biotech", "actor": ["anthropic", "adaptyv"], "score": "14 of 15 / 35.1%",
         "evidences": ["biology-as-compile-target", "automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-08-06-whole-phages-designed-from-scratch"]},
        {"id": "2026-08-19-a-whole-cell-you-can-perturb",
         "title": "A model simulates a whole cell then designs molecules to move it",
         "claim": "GenBio's AIDO Cell simulates a whole cell that can be perturbed, then designs "
                  "molecules to move it, while Terence Tao asked the post-capability question of "
                  "what mathematics is for.",
         "domain": "biotech", "actor": ["genbio"],
         "evidences": ["biology-as-compile-target", "a-discipline-grieves", "automated-science"],
         "supersedes": [B + "developments/2026-08-19-fourteen-of-fifteen-protein-targets-bound"]},
        {"id": "2026-08-19-memory-half-as-precious-per-kilo-as-gold",
         "title": "Memory prices rise 485% as hyperscalers lock up 2027 capacity",
         "claim": "DDR5 is up 485% year over year as hyperscalers lock up 2027 capacity, making "
                  "memory half as precious per kilogram as gold, while Cerebras unveiled a system "
                  "at 750 petaFLOPS for 50-trillion-parameter models.",
         "domain": "economics", "actor": ["cerebras"], "score": "+485% / 750 PFLOPS",
         "evidences": ["infrastructure-crowding-out", "bottlenecks-arbitraged-instantly",
                       "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-13-seven-hundred-twenty-billion-for-the-largest-memory-buildout"]},
        {"id": "2026-08-19-a-state-binds-datacenters-to-their-own-power-bills",
         "title": "A state binds datacenters to local approval and their own power bills",
         "claim": "Pennsylvania bound data centers to local approval and their own power bills, "
                  "and a grid operator proposed curtailing unsupplied loads before any household, "
                  "as Nvidia's moat moved from chips to capital, backstopping $105 billion in "
                  "Ohio and marshaling $500 billion more.",
         "domain": "policy", "actor": ["pennsylvania-state", "pjm", "nvidia"], "score": "$105B / $500B",
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-08-16-the-richest-counties-are-the-datacenter-counties"]},
        {"id": "2026-08-19-physical-ai-funding-beats-three-prior-years-combined",
         "title": "Physical AI takes $47.4 billion in six months, beating three prior years combined",
         "claim": "Physical AI took $47.4 billion in funding over six months, beating 2022 through "
                  "2024 combined, as Amazon expanded drone delivery toward 500 towns by year end.",
         "domain": "robotics", "actor": ["amazon"], "score": "$47.4B in six months",
         "evidences": ["physical-recursion", "compute-capital-stack", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-08-17-a-robot-outruns-every-human-alive"]},
        {"id": "2026-08-19-routers-turned-into-motion-sensors",
         "title": "Millions of home routers are turned into motion sensors",
         "claim": "Comcast turned millions of routers into motion sensors, ICE banned Meta glasses "
                  "at work while Homeland Security budgeted $7.5 million for its own, and AirPods "
                  "with cameras surfaced running visual intelligence.",
         "domain": "society", "actor": ["meta", "dhs", "apple"], "score": "$7.5M budget",
         "evidences": ["humans-as-peripherals", "intimate-interface", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-17-the-defenders-window"]},
        {"id": "2026-08-19-a-third-nation-lands-a-booster-on-legs",
         "title": "A third nation lands an orbital booster on legs",
         "claim": "China's LandSpace landed its Zhuque-3 booster on legs, only the third entity to "
                  "manage that, as a Starship flight was guided in after 24 days adrift and one "
                  "builder noted that capping space's share of GDP is as quaint as 1600s "
                  "economists capping the New World.",
         "domain": "space", "actor": ["china", "spacex"],
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-08-16-a-black-hole-star-in-the-early-universe"]},
        {"id": "2026-08-19-the-first-phase-three-mrna-win-in-oncology",
         "title": "A patient-specific mRNA vaccine wins the first Phase 3 in oncology",
         "claim": "Merck and Moderna's mRNA vaccine, written from each patient's tumor, cut "
                  "recurrence and metastasis in 1,137 melanoma patients, the first Phase 3 win for "
                  "mRNA in oncology.",
         "domain": "biotech", "actor": ["merck", "moderna"], "score": "1,137 patients",
         "evidences": ["hardware-grade-biology", "biology-as-compile-target", "longevity-escape-velocity"],
         "supersedes": [B + "developments/2026-08-06-the-first-us-mrna-flu-shot"]},
        {"id": "2026-08-19-founders-take-supervoting-shares-before-the-float",
         "title": "Founders take supervoting shares, leaving the throttle with them",
         "claim": "Anthropic's pre-IPO credit line passed $10 billion as banks bid for seats and "
                  "its founders took supervoting shares, leaving the throttle with them rather "
                  "than the float, as the lab doubled to $11.6 billion quarterly at a profit while "
                  "OpenAI booked $6.7 billion and a $12.3 billion loss.",
         "domain": "economics", "actor": ["anthropic", "openai"], "score": "$11.6B profit vs $12.3B loss",
         "evidences": ["ai-as-the-economy", "speed-of-containment", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-17-a-run-rate-past-sixty-five-billion"]},
    ],
}
