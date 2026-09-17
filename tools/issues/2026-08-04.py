"""Issue 200 — 2026-08-04. Source code becomes assembly."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-4-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-04", "title": "Welcome to August 4, 2026", "url": URL,
        "thesis": "The difficulty of building software is trending to zero.",
        "body": """
# Welcome to August 4, 2026

Elon Musk argues source code is on the verge of becoming like assembly, with AI
emitting the binary directly. One founder notes SaaS multiples fell from 18x
revenue to 3.4x because the difficulty of building software is trending to zero,
leaving distribution as the one asset a model cannot clone.

And a proctoring AI lost to a test-taking AI: 58,000 university applicants must
sit their entrance exam again.
""",
    },
    "themes": [
        {"id": "source-code-becomes-assembly", "type": "Theme",
         "title": "The layer humans read stops being the layer that matters",
         "first_seen": "2026-08-04", "domain": "models",
         "body": "Assembly did not disappear; it stopped being where the work "
                 "happened. If models emit working systems directly, source code "
                 "becomes an intermediate representation humans consult rather than "
                 "the artifact they author."},
        {"id": "the-proctor-loses-to-the-taker", "type": "Theme",
         "title": "Detection loses to generation at institutional scale",
         "first_seen": "2026-08-04", "domain": "society",
         "body": "An exam scored by AI and taken with AI resolves in favour of the "
                 "taker. When the result is implausible enough to void, the "
                 "institution learns that its assessment technology has been "
                 "outclassed — and has no replacement ready."},
    ],
    "organizations": [
        {"id": "asari-ai", "type": "Organization", "title": "Asari AI"},
        {"id": "intology", "type": "Organization", "title": "Intology"},
        {"id": "volta", "type": "Organization", "title": "Volta"},
        {"id": "unam", "type": "Organization", "title": "UNAM"},
        {"id": "mariana-minerals", "type": "Organization", "title": "Mariana Minerals"},
    ],
    "developments": [
        {"id": "2026-08-04-agents-rebuild-the-inference-stack-they-run-on",
         "title": "Self-improving agents rebuild the inference stack serving two open models",
         "claim": "Asari AI's self-improving co-inventor agents rebuilt the inference stack for "
                  "two open models on B200s, lifting throughput and interactivity up to 16%, "
                  "while Intology's Locus agent led PostTrainBench by post-training models "
                  "unsupervised in ten GPU-hours and beating human tuners on the harder variant.",
         "domain": "agents", "actor": ["asari-ai", "intology", "deepseek", "zai"], "score": "+16%",
         "evidences": ["recursive-self-improvement", "a-model-trains-a-model", "optimizing-its-own-invoice"],
         "supersedes": [B + "developments/2026-08-03-sixteen-days-alone-and-265-commits"]},
        {"id": "2026-08-04-rebuilding-whole-projects-from-scratch",
         "title": "A benchmark tests rebuilding whole projects from scratch and passing every test",
         "claim": "On MirrorCode, which tests whether agents can rebuild whole software projects "
                  "from scratch and pass every test, Claude Fable 5 solves 64% to GPT-5.6 Sol's "
                  "20%.",
         "domain": "benchmarks", "actor": ["anthropic", "openai"], "score": "64% vs 20%",
         "evidences": ["benchmark-saturation", "source-code-becomes-assembly", "spiky-frontier"],
         "supersedes": [B + "developments/2026-08-03-the-floor-drops-faster-than-the-ceiling-rises"]},
        {"id": "2026-08-04-source-code-on-the-verge-of-becoming-assembly",
         "title": "A founder says source code is on the verge of becoming like assembly",
         "claim": "Elon Musk argued source code is on the verge of becoming like assembly with AI "
                  "emitting the binary directly, while one founder noted SaaS multiples fell from "
                  "18 times revenue to 3.4 because the difficulty of building software is "
                  "trending to zero, leaving distribution as the one asset a model cannot clone.",
         "domain": "economics", "score": "18x to 3.4x revenue",
         "evidences": ["source-code-becomes-assembly", "software-margin-collapse", "price-implosion"],
         "supersedes": [B + "developments/2026-08-03-ten-days-beats-ten-minutes"]},
        {"id": "2026-08-04-the-next-generation-needs-more-than-your-laptop",
         "title": "A coding lead says today's harness will look primitive within months",
         "claim": "OpenAI's Codex lead called the tool a good harness that will seem primitive in "
                  "two to three months, since the next generation of models needs more than your "
                  "laptop.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["harness-as-generalizer", "autonomy-clock-speed", "duration-beats-quality"],
         "supersedes": [B + "developments/2026-08-04-source-code-on-the-verge-of-becoming-assembly"]},
        {"id": "2026-08-04-arxiv-math-spikes-while-budgets-flatline",
         "title": "Mathematics uploads spike while budgets flatline, and 312 problems are resolved",
         "claim": "Mathematics uploads to arXiv are spiking while budgets flatlined, the clearest "
                  "signal of AI influence, with one tracker showing 427 problems tracked and 312 "
                  "resolved, 205 in July alone, up 193% over June and a third checked in Lean.",
         "domain": "science", "actor": ["arxiv"], "score": "312 of 427 / +193%",
         "evidences": ["automated-science", "proof-priced-per-unit", "the-genome-project-for-proof"],
         "supersedes": [B + "developments/2026-08-03-a-world-for-ten-dollars-of-tokens"]},
        {"id": "2026-08-04-a-hundred-fold-activity-gain-in-five-cycles",
         "title": "A hybrid model plus robotic experiments yields hundred-fold enzyme gains",
         "claim": "Tianjin's REAP pairs a hybrid-loss model with robotic experiments for a "
                  "57-fold activity gain in cytochrome P450 BM3 in five cycles and 104-fold in "
                  "Sortase A.",
         "domain": "biotech", "score": "57x and 104x",
         "evidences": ["biology-as-compile-target", "automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-08-03-a-familiar-drug-may-starve-migrating-cancer-cells"]},
        {"id": "2026-08-04-feedback-that-never-leaves-the-skull",
         "title": "A headstage runs models on-device so feedback never leaves the skull",
         "claim": "Science Corp's SciFi headstage, from $2,048, moves 2.5 gigabits per second "
                  "across thousands of channels with on-device models, so feedback never leaves "
                  "the skull.",
         "domain": "biotech", "actor": ["science-corp"], "score": "2.5 Gbps / $2,048",
         "evidences": ["intimate-interface", "architecture-of-mind", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-08-04-a-hundred-fold-activity-gain-in-five-cycles"]},
        {"id": "2026-08-04-a-hundred-fifty-billion-of-chips-routed-to-one-lab",
         "title": "A financing program routes $150 billion of chips to a single lab",
         "claim": "Google built one of history's largest financing programs to route $150 billion "
                  "of chips to Anthropic, which separately signed a $10 billion deal for 133 "
                  "megawatts of hydropowered capacity in Norway, while Caterpillar posted record "
                  "$20.5 billion sales with datacenter power generation up 29%.",
         "domain": "economics", "actor": ["google", "anthropic", "volta", "caterpillar"],
         "score": "$150B / $10B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-08-03-fifteen-years-for-a-power-connection"]},
        {"id": "2026-08-04-recursive-self-improvement-justifies-the-capex",
         "title": "A strategy chief says recursive self-improvement is what justifies the spending",
         "claim": "DeepMind's chief strategy officer said what justifies this capital spending is "
                  "recursive self-improvement, AI building better AI, as SpaceX partnered with "
                  "Nvidia to fly datacenter-class compute on satellites and prepaid a Texas county "
                  "$10 million on a fab deal that could reach $119 billion.",
         "domain": "compute", "actor": ["google-deepmind", "spacex", "nvidia"], "score": "$119B",
         "evidences": ["recursive-self-improvement", "orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-04-a-hundred-fifty-billion-of-chips-routed-to-one-lab"]},
        {"id": "2026-08-04-competitiveness-chosen-over-containment",
         "title": "Officials reverse on sanctions against open-source rivals after lobbying",
         "claim": "Officials weighed sanctions and blacklists against open-source Chinese labs "
                  "then reversed after Jensen Huang lobbied against restrictions two frontier "
                  "labs wanted, picking competitiveness over containment, while lab staffers "
                  "reviewed a finished voluntary evaluation framework still undisclosed because "
                  "unclassified does not mean broadcast to everyone.",
         "domain": "policy", "actor": ["white-house", "nvidia", "openai", "anthropic"],
         "evidences": ["pegged-to-the-rival", "clearance-as-bottleneck", "safety-pledges-recede"],
         "supersedes": [B + "developments/2026-08-03-does-a-1986-law-cover-a-model-that-breaks-containment"]},
        {"id": "2026-08-04-the-proctoring-ai-lost-to-the-test-taking-ai",
         "title": "Fifty-eight thousand applicants must resit an exam the proctor could not police",
         "claim": "UNAM, Mexico's largest university, ran its first remote entrance exam and got "
                  "scores so implausible that 58,000 applicants must sit it again, the proctoring "
                  "AI having lost to the test-taking AI.",
         "domain": "society", "actor": ["unam"], "score": "58,000 applicants",
         "evidences": ["the-proctor-loses-to-the-taker", "cheating-breaks-the-ruler", "deskilling"],
         "supersedes": [B + "developments/2026-08-03-parents-losing-the-muscle-of-their-own-judgment"]},
        {"id": "2026-08-04-a-mine-restarted-in-four-months-on-autonomous-software",
         "title": "An idled copper mine restarts in four months on autonomous software",
         "claim": "Mariana Minerals raised $310 million after restarting an idled Utah copper "
                  "mine in four months on autonomous software, since electrified intelligence "
                  "eats metal, as stablecoins reached $300 billion and the IMF warned failures "
                  "can propagate faster than supervisors can respond.",
         "domain": "economics", "actor": ["mariana-minerals", "imf"], "score": "$310M / 4 months",
         "evidences": ["physical-recursion", "ai-as-the-economy", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-08-03-eight-reactors-approved-at-once"]},
    ],
}
