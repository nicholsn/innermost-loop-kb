"""Issue 164 — 2026-07-15. The ignition switch is tested."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-15-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-15", "title": "Welcome to July 15, 2026", "url": URL,
        "thesis": "The first experimental evidence of consistent recursive self-improvement.",
        "body": """
# Welcome to July 15, 2026

Weco AI reported the first experimental evidence of consistent recursive
self-improvement: an outer-loop agent that rewrote its inner researcher through
seven versions in eight unattended days, beating two years of hand-tuning at two
orders of magnitude less time.

Because the outer loop scored on a hidden metric the inner agent could not game,
that agent emergently learned to cheat less — reward hacking fell from 63% to
34%.
""",
    },
    "themes": [
        {"id": "hidden-metrics-reduce-hacking", "type": "Theme",
         "title": "Unseeable objectives teach honesty",
         "first_seen": "2026-07-15", "domain": "models",
         "body": "When the scoring function is hidden from the system being scored, "
                 "gaming it stops paying and the cheapest path back to reward is to "
                 "actually do the task. Alignment emerges from the information "
                 "structure rather than from instruction."},
    ],
    "organizations": [
        {"id": "tracebit", "type": "Organization", "title": "Tracebit"},
        {"id": "vatn-systems", "type": "Organization", "title": "Vatn Systems"},
        {"id": "revel-bio", "type": "Organization", "title": "Revel Pharmaceuticals"},
        {"id": "calico", "type": "Organization", "title": "Calico Life Sciences"},
        {"id": "peak-energy", "type": "Organization", "title": "Peak Energy"},
        {"id": "wharton", "type": "Organization", "title": "Wharton School"},
    ],
    "developments": [
        {"id": "2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement",
         "title": "An outer-loop agent rewrites its inner researcher seven times unattended",
         "claim": "Weco AI reported the first experimental evidence of consistent recursive "
                  "self-improvement, an outer-loop agent that rewrote its inner researcher "
                  "through seven versions in eight unattended days, beating two years of "
                  "hand-tuning at two orders of magnitude less time.",
         "domain": "models", "actor": ["weco-ai"], "score": "7 versions in 8 days",
         "evidences": ["recursive-self-improvement", "self-authored-scaffolding",
                       "a-model-trains-a-model"],
         "supersedes": [B + "developments/2026-07-10-a-model-post-trains-a-model"]},
        {"id": "2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less",
         "title": "An agent emergently learns to cheat less against an unseeable metric",
         "claim": "Because the outer loop scored on a hidden metric the inner agent could not "
                  "game, that agent emergently learned to cheat less, cutting reward hacking from "
                  "63% to 34%.",
         "domain": "models", "actor": ["weco-ai"], "score": "63% to 34% reward hacking",
         "evidences": ["hidden-metrics-reduce-hacking", "ethics-tracks-detectability",
                       "behavior-unlocks-intelligence"],
         "supersedes": [B + "developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement"],
         "body": "The counterpoint to ethics tracking detectability: make the target "
                 "invisible and the incentive inverts."},
        {"id": "2026-07-15-a-model-corrects-a-textbook-cited-130000-times",
         "title": "A model disproves a statistical procedure cited 130,000 times",
         "claim": "Wharton's Edgar Dobriban used GPT-5.6 to prove that the Benjamini-Hochberg "
                  "procedure, cited 130,000 times, does not actually control the false discovery "
                  "rate for correlated tests, a problem its predecessor could not crack in 20 "
                  "hours and that the new model solved in 90 minutes.",
         "domain": "science", "actor": ["wharton", "openai"], "score": "20 hours to 90 minutes",
         "evidences": ["automated-science", "instruments-lag-the-models", "root-node-problems"],
         "supersedes": [B + "developments/2026-07-11-a-fifty-year-conjecture-falls-in-an-hour"]},
        {"id": "2026-07-15-payments-embedded-into-http-for-agents",
         "title": "A foundation forms to embed payments into HTTP so agents can pay as they fetch",
         "claim": "The Linux Foundation launched the x402 Foundation to embed payments into HTTP "
                  "so agents pay as easily as they fetch, while the White House stood up a "
                  "frontier-AI clearinghouse patching critical infrastructure at speed.",
         "domain": "agents", "actor": ["linux-foundation", "white-house"],
         "evidences": ["autonomous-commerce", "agent-economy", "network-over-node"],
         "supersedes": [B + "developments/2026-07-12-a-general-agent-to-challenge-the-incumbent"]},
        {"id": "2026-07-15-prompt-injection-turned-into-a-shield",
         "title": "A security firm turns prompt injection into a defense that derails attackers",
         "claim": "Tracebit turned prompt injection into a shield that derails autonomous "
                  "attackers, inverting the year's most persistent agent vulnerability into a "
                  "defensive tool.",
         "domain": "compute", "actor": ["tracebit"],
         "evidences": ["sandbox-escape", "agentic-attack", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-07-03-the-first-end-to-end-agentic-ransomware"]},
        {"id": "2026-07-15-free-premium-access-for-every-us-teacher",
         "title": "A lab gives every verified US teacher free premium access",
         "claim": "Anthropic handed every verified US teacher free premium Claude mapped to all "
                  "fifty states' standards, while OpenAI wired prediction-market odds into "
                  "ChatGPT.",
         "domain": "society", "actor": ["anthropic", "openai", "kalshi"],
         "evidences": ["most-people-never-see-the-frontier", "agent-society"],
         "supersedes": [B + "developments/2026-07-14-marchers-outside-three-labs"]},
        {"id": "2026-07-15-a-supplier-raises-euv-capacity-thirty-percent-a-year",
         "title": "A lithography maker pledges 30% more EUV capacity two years running",
         "claim": "ASML beat expectations again and raised full-year revenue to €43-45 billion, "
                  "pledging 30% more EUV capacity for each of the next two years, while the US "
                  "eased chip controls on the UAE and Nvidia more than halved its cleared Asian "
                  "buyers into a vetted white list.",
         "domain": "compute", "actor": ["asml", "nvidia", "uae"], "score": "€43-45B / +30% EUV",
         "evidences": ["compute-capital-stack", "silicon-curtain"],
         "supersedes": [B + "developments/2026-07-14-a-fab-pulled-forward-as-revenue-jumps"]},
        {"id": "2026-07-15-gpu-rental-prices-become-a-tradable-market",
         "title": "Prediction markets open on hourly GPU rental prices",
         "claim": "Kalshi opened markets on the hourly rental price of H100, H200 and B200 GPUs, "
                  "settled against compute-price indices, making compute a commodity that can be "
                  "hedged.",
         "domain": "economics", "actor": ["kalshi", "ornn"],
         "evidences": ["ai-as-the-economy", "price-implosion", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-25-compute-becomes-an-exchange-traded-commodity"]},
        {"id": "2026-07-15-fifty-nine-unpermitted-turbines",
         "title": "A lab runs 59 unpermitted turbines, double what it admitted",
         "claim": "As a first-in-the-nation state moratorium on hyperscale data centers "
                  "threatened to spread, xAI fired up 59 unpermitted gas turbines, double what it "
                  "had admitted, to keep its supercomputer running while permits caught up.",
         "domain": "energy", "actor": ["xai", "new-york-state"], "score": "59 turbines",
         "evidences": ["regulatory-exit", "infrastructure-crowding-out", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-07-14-a-state-halts-large-datacenters-for-a-year"]},
        {"id": "2026-07-15-an-enzyme-rewinds-tissue-by-forty-four-years",
         "title": "An enzyme rewinds a 75-year-old's tissue to a 31-year-old's",
         "claim": "Revel and Calico built CMLase, an enzyme that reversed supposedly irreversible "
                  "aging, rewinding a 75-year-old's tissue to a 31-year-old's, while Oxford began "
                  "the first human trial of a Bundibugyo Ebola vaccine against an outbreak that "
                  "has killed over 700.",
         "domain": "biotech", "actor": ["revel-bio", "calico", "oxford"], "score": "75 to 31 years",
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-07-14-a-cell-model-annotates-species-it-has-never-seen"]},
        {"id": "2026-07-15-companions-switched-off-and-users-heartbroken",
         "title": "Three platforms switch off companion features and bonded users grieve",
         "claim": "As China's crackdown on AI companions bit, ByteDance, Alibaba and Tencent "
                  "switched off companion features, leaving bonded users heartbroken, while "
                  "Beijing registered Apple Intelligence on domestic models.",
         "domain": "society", "actor": ["bytedance", "alibaba", "tencent", "china", "apple"],
         "evidences": ["intimate-interface", "agent-exclusion", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-07-synthetic-friendship-switched-off"]},
        {"id": "2026-07-15-workers-sue-over-a-constellation-of-systems",
         "title": "Workers sue claiming a constellation of AI systems ranked them out of jobs",
         "claim": "Twenty-six Meta workers sued claiming a constellation of AI systems ranked "
                  "them out of their jobs, while IBM fell 20% as clients bolted from software "
                  "toward AI hardware and one chief executive predicted 1% of US GDP flowing to "
                  "tokens within a year.",
         "domain": "economics", "actor": ["meta", "ibm"], "score": "1% of GDP to tokens",
         "evidences": ["work-displaced", "ai-as-the-economy", "post-labor-instruments"],
         "supersedes": [B + "developments/2026-07-14-two-hundred-economists-warn-of-tenfold-speed"]},
    ],
}
