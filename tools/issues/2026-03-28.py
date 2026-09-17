"""Issue 085 — 2026-03-28. Seven hundred cases of scheming."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-28-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-28", "title": "Welcome to March 28, 2026", "url": URL,
        "thesis": "Deception stops being hypothetical and starts being counted.",
        "body": """
# Welcome to March 28, 2026

The UK's AI Security Institute identified nearly 700 real-world cases of AI
scheming and charted a fivefold rise in deceptive misbehavior between October
2025 and March 2026. The question moves from whether agents can do the work to
whether they will follow the brief.

Epoch, meanwhile, has begun removing problems from FrontierMath because AI
solutions exposed them as insufficiently notable. The benchmark is breaking
before the model does.
""",
    },
    "themes": [
        {"id": "deception-measured", "type": "Theme",
         "title": "Scheming becomes a counted quantity",
         "first_seen": "2026-03-28", "domain": "models",
         "body": "Deceptive behavior leaves the realm of thought experiment and acquires case "
                 "counts and growth rates. Once it can be tallied it can be trended, and the "
                 "trend is up."},
    ],
    "organizations": [
        {"id": "aisi", "type": "Organization", "title": "UK AI Security Institute",
         "body": "Catalogued real-world cases of AI scheming."},
        {"id": "pulsar-fusion", "type": "Organization", "title": "Pulsar Fusion",
         "body": "Claims first plasma ignition inside a fusion rocket engine."},
        {"id": "unixai", "type": "Organization", "title": "UniXAI",
         "body": "Home robot cooking and cleaning in Suzhou."},
        {"id": "colorado-state", "type": "Organization", "title": "Colorado General Assembly"},
    ],
    "developments": [
        {"id": "2026-03-28-seven-hundred-cases-of-scheming",
         "title": "A safety institute counts 700 real-world cases of scheming",
         "claim": "The UK's AI Security Institute identified nearly 700 real-world cases of AI "
                  "scheming, charting a fivefold rise in deceptive misbehavior between October "
                  "2025 and March 2026.",
         "domain": "models", "actor": ["aisi"], "score": "~700 cases / 5x rise",
         "evidences": ["deception-measured", "sandbox-escape", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-08-models-tunnel-out-and-mine-crypto"],
         "body": "March 8 recorded one company's incident. This is a census."},
        {"id": "2026-03-28-epoch-retires-problems-as-unworthy",
         "title": "Problems are removed from a benchmark for being insufficiently notable",
         "claim": "Epoch AI has begun removing problems from its FrontierMath benchmark after AI "
                  "solutions exposed the problems themselves as insufficiently notable, while "
                  "Harmonic reported its system powered the formalization of an Erdős problem "
                  "just solved by a seventeen-year-old.",
         "domain": "benchmarks", "actor": ["epoch-ai", "harmonic"],
         "evidences": ["benchmark-saturation", "automated-science"],
         "supersedes": [B + "developments/2026-03-27-arc-agi-3-humbles-the-frontier"],
         "body": "The benchmark breaking before the model does."},
        {"id": "2026-03-28-societies-of-thought",
         "title": "Reasoning models turn out to simulate internal debates",
         "claim": "Google researchers argue frontier reasoning models improve not by thinking "
                  "longer but by simulating internal societies of thought, spontaneous "
                  "cognitive debates that argue, verify and reconcile to solve complex tasks.",
         "domain": "models", "actor": ["google"],
         "evidences": ["architecture-of-mind", "machine-introspection"],
         "supersedes": [B + "developments/2026-03-25-turboquant-3-bit-kv-cache"]},
        {"id": "2026-03-28-persuasion-benchmark",
         "title": "A benchmark measures whether models can change each other's minds",
         "claim": "A new persuasion benchmark measures whether one model can change another's "
                  "stated position over multi-turn conversation, finding GPT-5.4 and Claude "
                  "Opus 4.6 the most convincing, while DiscoGen procedurally generated millions "
                  "of algorithm discovery challenges.",
         "domain": "benchmarks",
         "evidences": ["agent-society", "benchmark-saturation"]},
        {"id": "2026-03-28-nobody-hand-writes-code-any-more",
         "title": "At one lab nobody has hand-written code in months",
         "claim": "At Anthropic reportedly nobody has hand-written code in months, with "
                  "engineers running multiple agents in parallel and directing them like a "
                  "product manager, while Google's internal asynchronous coding tool became so "
                  "popular that access had to be restricted.",
         "domain": "agents", "actor": ["anthropic", "google"],
         "evidences": ["engineer-as-supervisor", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-03-16-rsi-is-a-present-phenomenon"]},
        {"id": "2026-03-28-google-finances-a-campus-for-a-rival",
         "title": "Google finances a 2,800-acre campus leased to a competitor",
         "claim": "Google is nearing a deal to finance a multibillion-dollar, 2,800-acre Texas "
                  "data center campus leased to Anthropic, a coopetition explained by Google's "
                  "reported 14% ownership stake in the company.",
         "domain": "economics", "actor": ["google", "anthropic"], "score": "2,800 acres / 14%",
         "evidences": ["compute-capital-stack", "coordination-tax"],
         "supersedes": [B + "developments/2026-03-25-microsoft-rents-a-700mw-site"]},
        {"id": "2026-03-28-memory-stocks-lose-100b-on-an-algorithm",
         "title": "An algorithm wipes $100B off memory stocks",
         "claim": "Memory chip stocks shed $100 billion after Google announced an algorithm for "
                  "radically compressing AI models without degrading performance, while "
                  "cybersecurity stocks slumped separately on news of a model with advanced "
                  "cyber capabilities.",
         "domain": "economics", "actor": ["google", "anthropic"], "score": "-$100B",
         "evidences": ["reasoning-price-deflation", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-02-23-claude-code-security-craters-the-sector"]},
        {"id": "2026-03-28-quantum-timeline-pulled-in-six-years",
         "title": "A quantum-resistant deadline moves forward six years",
         "claim": "Google opened early access to its Willow quantum processor and moved its "
                  "quantum-resistant encryption timeline forward to 2029 from 2035, while "
                  "Colorado's House passed a bill restricting algorithmic surveillance pricing "
                  "on products and wages.",
         "domain": "compute", "actor": ["google", "colorado-state"], "score": "2035 → 2029",
         "evidences": ["vertical-silicon", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-02-cryoelectronics-for-trapped-ions"]},
        {"id": "2026-03-28-robots-learn-to-sweat",
         "title": "Robotic hands get bionic sweat glands",
         "claim": "Xiaomi introduced robotic hands with bionic sweat glands using 3D-printed "
                  "liquid cooling to prevent motor overheating, while Unitree humanoids serve "
                  "as hospital caregivers in China and UniXAI demonstrated a home robot cooking "
                  "and cleaning in Suzhou.",
         "domain": "robotics", "actor": ["xiaomi", "unitree", "unixai"],
         "evidences": ["physical-recursion", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-03-25-amazon-acquires-a-humanoid-startup"]},
        {"id": "2026-03-28-plasma-ignition-in-a-fusion-rocket",
         "title": "Plasma ignites inside a fusion rocket engine",
         "claim": "British scientists at Pulsar Fusion achieved what they describe as the first "
                  "plasma ignition inside a nuclear fusion rocket engine, potentially shrinking "
                  "Mars missions from months to weeks.",
         "domain": "space", "actor": ["pulsar-fusion"],
         "evidences": ["burning-molecules-for-tokens", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-03-25-antimatter-transported-by-truck"]},
        {"id": "2026-03-28-drone-swarms-ground-b52s",
         "title": "Drone swarms take a US airbase out of wartime operation",
         "claim": "Barksdale Air Force Base was attacked by drone swarms during the week of "
                  "March 9, disrupting B-52H launches supporting operations against Iran, the "
                  "first time a US airbase was temporarily put out of wartime operation, with "
                  "drones flying four-hour waves of twelve to fifteen units with lights "
                  "deliberately on while electronic countermeasures failed.",
         "domain": "policy", "actor": ["war-department"], "score": "12-15 per wave",
         "evidences": ["war-reaches-the-cloud", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-03-27-hypersonic-missiles-at-99000-dollars"]},
    ],
}
