"""Issue 127 — 2026-05-29. Alignment becomes a moat."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-29-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-29", "title": "Welcome to May 29, 2026", "url": URL,
        "thesis": "When the safest model is also the strongest, alignment stops being a tax.",
        "body": """
# Welcome to May 29, 2026

Opus 4.8 lands as a modest but tangible improvement that still posts SOTA on
SWE-Bench Pro and Humanity's Last Exam. Anthropic raises $65 billion at a $900
billion valuation, passing OpenAI.

And mathematicians disprove the sum-product conjecture over the reals using
methods lifted from the AI solution to the unit distance conjecture — scavenging
spoils from the intelligence outpacing them.
""",
    },
    "themes": [
        {"id": "alignment-as-moat", "type": "Theme",
         "title": "Alignment stops being a tax",
         "first_seen": "2026-05-29", "domain": "models",
         "body": "Safety work had been priced as drag on capability. Once the safest "
                 "frontier model is also the most capable one, the relationship "
                 "inverts and alignment becomes the differentiator competitors "
                 "cannot cheaply copy."},
        {"id": "humans-mine-the-machine", "type": "Theme",
         "title": "Humans scavenge machine proofs for methods",
         "first_seen": "2026-05-29", "domain": "science",
         "body": "Researchers stop competing with machine results and start reading "
                 "them: the technique inside an AI proof becomes a tool humans carry "
                 "to the next problem."},
    ],
    "organizations": [
        {"id": "kirkland-ellis", "type": "Organization", "title": "Kirkland & Ellis"},
        {"id": "red-hat", "type": "Organization", "title": "Red Hat"},
        {"id": "shift-robotics", "type": "Organization", "title": "Shift"},
        {"id": "wix", "type": "Organization", "title": "Wix"},
        {"id": "dell", "type": "Organization", "title": "Dell Technologies"},
        {"id": "geely", "type": "Organization", "title": "Geely"},
    ],
    "developments": [
        {"id": "2026-05-29-the-safest-model-is-also-the-strongest",
         "title": "The safest frontier model is also the strongest",
         "claim": "Anthropic launched Opus 4.8, a modest but tangible improvement posting a "
                  "state-of-the-art 69.2% on SWE-Bench Pro, 57.9% on Humanity's Last Exam with "
                  "tools and 1890 on GDPval-AA, pairing fresh honesty gains with misalignment "
                  "rates rivalling the unreleased Mythos Preview.",
         "domain": "models", "actor": ["anthropic"], "score": "69.2% SWE-Bench Pro",
         "evidences": ["alignment-as-moat", "refusal-as-differentiator", "spiky-frontier"],
         "supersedes": [B + "developments/2026-05-25-a-benchmark-of-twenty-three-real-saas-systems"]},
        {"id": "2026-05-29-swarms-of-subagents-carry-migrations",
         "title": "Swarms of parallel subagents carry codebase-scale migrations",
         "claim": "Claude Code added dynamic workflows that spin up swarms of parallel "
                  "subagents to carry codebase-scale migrations across hundreds of thousands of "
                  "lines from kickoff to merge, with the existing test suite as the only gate.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["agents-beget-agents", "engineer-as-supervisor", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-05-22-thirty-five-hours-of-autonomous-execution"]},
        {"id": "2026-05-29-humans-lift-methods-from-a-machine-proof",
         "title": "Humans disprove a conjecture using methods lifted from an AI proof",
         "claim": "Tim Gowers reported that a major additive combinatorics problem fell to "
                  "people using methods lifted from the AI solution to the unit distance "
                  "conjecture, disproving the sum-product conjecture over the reals.",
         "domain": "science", "evidences": ["humans-mine-the-machine", "discovery-as-process",
                                            "automated-science"],
         "supersedes": [B + "developments/2026-05-21-a-conjecture-is-disproved"]},
        {"id": "2026-05-29-sixty-five-billion-at-nine-hundred",
         "title": "A lab raises $65B at a $900B valuation and passes its rival",
         "claim": "Anthropic raised $65 billion at a $900 billion valuation, vaulting past "
                  "OpenAI's $730 billion.",
         "domain": "economics", "actor": ["anthropic", "openai"], "score": "$65B at $900B",
         "evidences": ["compute-capital-stack", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-05-15-thirty-billion-at-nine-hundred"]},
        {"id": "2026-05-29-thirty-six-billion-of-debt-to-lease-tpus",
         "title": "A $36B debt deal is shopped to buy TPUs for one lab to lease",
         "claim": "Apollo and Blackstone are shopping a roughly $36 billion debt deal to buy "
                  "Google TPUs for Anthropic to lease, with Broadcom backstopping the largest "
                  "tranches.",
         "domain": "economics", "actor": ["apollo-global", "blackstone", "broadcom", "anthropic"],
         "score": "$36B", "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-20-a-twenty-five-billion-tpu-venture"]},
        {"id": "2026-05-29-ai-server-revenue-up-757-percent",
         "title": "A server maker's AI revenue rises 757%",
         "claim": "Dell's AI server revenue rose 757% to $16.1 billion, while the EU readied "
                  "emergency powers to override chip contracts during shortages.",
         "domain": "economics", "actor": ["dell", "european-union"], "score": "+757% to $16.1B",
         "evidences": ["ai-as-the-economy", "silicon-curtain"],
         "supersedes": [B + "developments/2026-05-12-transformer-demand-up-274-percent"]},
        {"id": "2026-05-29-a-law-firm-builds-rather-than-rents",
         "title": "A law firm sets aside $500M to build its own tools",
         "claim": "Kirkland & Ellis set aside $500 million to build its own AI tools rather "
                  "than rent its rivals', while Meta began charging for AI features for the "
                  "first time at $7.99 a month.",
         "domain": "economics", "actor": ["kirkland-ellis", "meta"], "score": "$500M",
         "evidences": ["software-margin-collapse", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-05-13-claude-for-the-legal-industry"]},
        {"id": "2026-05-29-five-billion-to-secure-the-open-source-supply-chain",
         "title": "IBM and Red Hat pledge $5B to secure the open-source supply chain",
         "claim": "IBM and Red Hat pledged $5 billion and 20,000 engineers to Project "
                  "Lightwell, an AI clearinghouse to secure the open-source supply chain.",
         "domain": "compute", "actor": ["ibm", "red-hat"], "score": "$5B / 20,000 engineers",
         "evidences": ["risk-becomes-uninsurable", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-05-28-cve-issuance-hits-thirteen-a-day"]},
        {"id": "2026-05-29-a-side-channel-in-your-idle-drive",
         "title": "An SSD side-channel fingerprints open apps by disk timing",
         "claim": "Researchers revealed an AI-based SSD side-channel attack that fingerprints "
                  "the sites and apps a user has open purely by timing disk contention.",
         "domain": "compute",
         "evidences": ["sandbox-escape", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-05-20-audio-attacks-hijack-thirteen-models"]},
        {"id": "2026-05-29-free-cleaning-in-exchange-for-training-data",
         "title": "A startup offers free home cleaning in exchange for training footage",
         "claim": "Shift offers free home cleaning to customers who let it film the work so "
                  "robots can learn the chore, while Waymo prepares the Ojai, a roomier "
                  "robotaxi co-built with Geely's Zeekr, for unsupervised public rides.",
         "domain": "robotics", "actor": ["shift-robotics", "waymo", "geely"],
         "evidences": ["data-beyond-text", "physical-recursion"],
         "supersedes": [B + "developments/2026-05-26-robotaxis-as-an-instrument-of-independence"]},
        {"id": "2026-05-29-a-rocket-explodes-on-the-test-stand",
         "title": "A rival rocket explodes during a static fire",
         "claim": "Blue Origin's New Glenn exploded during a static fire, likely benching it "
                  "from Artemis for a year and handing SpaceX the near-term lead.",
         "domain": "space", "actor": ["blue-origin", "spacex", "nasa"],
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-05-26-orbital-solar-ten-x-per-generation"]},
        {"id": "2026-05-29-a-leaderboard-killed-for-being-gamed",
         "title": "A company kills an internal AI leaderboard after staff gamed it",
         "claim": "Amazon killed an internal AI leaderboard after staff gamed it with costly "
                  "busywork, while Wix cut roughly 20% of staff citing AI's fast evolution.",
         "domain": "economics", "actor": ["amazon", "wix"], "score": "-20% at Wix",
         "evidences": ["gaming-the-token-metric", "work-displaced"],
         "supersedes": [B + "developments/2026-05-12-employees-automate-fake-ai-tasks"]},
    ],
}
