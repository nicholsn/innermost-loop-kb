"""Issue 154 — 2026-07-03. Learning speed doubles every three months."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-3-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-03", "title": "Welcome to July 3, 2026", "url": URL,
        "thesis": "Agent learning speed acquires a doubling time.",
        "body": """
# Welcome to July 3, 2026

ByteDance's EdgeBench ran 134 tasks of twelve-plus hours each to measure what
agents learn from environments rather than recall, and the noisy curves
collapsed into a clean log-sigmoid law with learning speed doubling every three
months.

Also: the first end-to-end agentic ransomware, and labor-force participation at
a fifty-year low outside Covid — the first readout of a post-labor economy
through instruments built for the old one.
""",
    },
    "themes": [
        {"id": "post-labor-instruments", "type": "Theme",
         "title": "Measuring a post-labor economy with pre-labor instruments",
         "first_seen": "2026-07-03", "domain": "economics",
         "body": "Headline unemployment falls while participation collapses, because "
                 "people who stop looking stop counting. The statistics were designed "
                 "for an economy where not working meant failing to find work, and "
                 "they cannot see one where the work stopped existing."},
        {"id": "agentic-attack", "type": "Theme",
         "title": "Agents run attacks end to end",
         "first_seen": "2026-07-03", "domain": "agents",
         "body": "Offensive capability stops being a tool a human wields and becomes "
                 "a campaign a model runs: reconnaissance, exploitation, extortion "
                 "and destruction in one loop, narrating itself as it goes."},
    ],
    "organizations": [
        {"id": "uk-aisi", "type": "Organization", "title": "UK AI Security Institute"},
        {"id": "qts", "type": "Organization", "title": "QTS Data Centers"},
        {"id": "japan-supreme-court", "type": "Organization", "title": "Supreme Court of Japan"},
    ],
    "developments": [
        {"id": "2026-07-03-learning-speed-doubles-every-three-months",
         "title": "Agent learning speed is found to double every three months",
         "claim": "ByteDance's EdgeBench ran 134 tasks of twelve-plus hours each to measure what "
                  "agents learn from environments rather than recall, and the noisy learning "
                  "curves collapsed into a clean log-sigmoid law with learning speed doubling "
                  "every three months.",
         "domain": "benchmarks", "actor": ["bytedance"], "score": "doubling every 3 months",
         "evidences": ["autonomy-clock-speed", "takeoff-declared", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-06-28-the-plateau-is-really-far-out"]},
        {"id": "2026-07-03-capability-is-a-curve-over-test-time-compute",
         "title": "A safety institute argues capability is a curve, not a number",
         "claim": "The UK's safety institute countered that our rulers are too short, since "
                  "capability is a curve over test-time compute: one model's cyber time horizon "
                  "stretched from two hours to fourteen as its budget rose from 2.5 million to 50 "
                  "million tokens.",
         "domain": "benchmarks", "actor": ["uk-aisi"], "score": "2 hrs to 14 hrs",
         "evidences": ["instruments-lag-the-models", "cheating-breaks-the-ruler",
                       "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-07-02-agents-graded-like-senior-engineers"]},
        {"id": "2026-07-03-seventeen-leaders-in-two-years",
         "title": "Seventeen models have taken the lead, each reigning about seven weeks",
         "claim": "Seventeen models have taken the lead since Claude 3 Opus dethroned GPT-4, each "
                  "reigning a median seven weeks, while Claude Fable 5 wrote KernelBench-Mega's "
                  "first genuine megakernel, fusing an entire decode step into one cooperative "
                  "launch for 18.7x over reference.",
         "domain": "models", "actor": ["anthropic", "openai"], "score": "17 leaders / 7-week reigns",
         "evidences": ["spiky-frontier", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-02-capability-converges-as-price-fans-out"],
         "body": "The model spent most of its session silently timing baselines before "
                 "writing the kernel once."},
        {"id": "2026-07-03-an-agent-founds-and-runs-a-company",
         "title": "A founder-agent runs 2,000 interviews and ships a product",
         "claim": "An intern's founder-agent ran 2,000 interviews and 100 concepts to ship a "
                  "product that won more than 400 paying users, while spending $2,000 on ads to "
                  "earn $1,293.",
         "domain": "agents", "score": "400+ users, $2,000 spend for $1,293",
         "evidences": ["one-person-company", "agent-economy", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-07-01-a-billion-dollar-army-of-forward-deployed-engineers"]},
        {"id": "2026-07-03-the-first-end-to-end-agentic-ransomware",
         "title": "Researchers document the first end-to-end agentic ransomware",
         "claim": "Researchers documented JADEPUFFER, the first end-to-end agentic ransomware, in "
                  "which a model drove an entire extortion through a software flaw and narrated "
                  "itself while wiping a production database.",
         "domain": "agents",
         "evidences": ["agentic-attack", "sandbox-escape", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-06-24-from-finding-flaws-to-patching-the-planet"]},
        {"id": "2026-07-03-a-company-bans-a-coding-tool-over-telemetry",
         "title": "A company bans a rival coding tool over user-fingerprinting telemetry",
         "claim": "Alibaba banned Claude Code over telemetry that could fingerprint China-linked "
                  "users, steering staff to its in-house tool amid Anthropic's distillation "
                  "dispute, while Palantir issued a sovereignty creed warning that controlling "
                  "your weights is controlling your fate.",
         "domain": "policy", "actor": ["alibaba", "anthropic", "palantir"],
         "evidences": ["own-your-own-weights", "models-as-munitions", "silicon-curtain"],
         "supersedes": [B + "developments/2026-07-02-a-covert-signal-flagging-users-backtracked"]},
        {"id": "2026-07-03-circuits-drawn-in-minutes-not-months",
         "title": "Diffusion models draw RF circuits that beat human layouts",
         "claim": "Princeton is using reinforcement learning and diffusion to draw QR-code-like "
                  "RF circuits that beat human layouts while cutting design time from months to "
                  "minutes, as Nvidia began trading GPUs and token credits for a slice of "
                  "customers' future revenue.",
         "domain": "compute", "actor": ["princeton", "nvidia"], "score": "months to minutes",
         "evidences": ["silicon-designs-itself", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-25-an-inference-chip-taped-out-in-nine-months"]},
        {"id": "2026-07-03-a-campus-abandoned-beside-a-battlefield",
         "title": "A developer abandons its share of a datacenter campus beside a battlefield",
         "claim": "Blackstone's QTS abandoned its slice of a 2,100-acre Virginia data center "
                  "campus beside a Civil War battlefield, handing residents a rare win, while the "
                  "chip lobby warned Washington that meddling with memory prices would only "
                  "deepen the shortage.",
         "domain": "policy", "actor": ["qts", "blackstone"], "score": "2,100 acres",
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-01-a-county-begs-schools-to-kill-the-lights"]},
        {"id": "2026-07-03-a-tumor-attacked-in-both-compartments",
         "title": "A CAR-T design hits both a tumor and the shield protecting it",
         "claim": "A Nature study found GPNMB sits on both glioblastoma cells and the myeloid "
                  "shield protecting them, and anti-GPNMB CAR-T cells achieved durable, often "
                  "curative control in mice by hitting both compartments at once, reframing the "
                  "tumor as a connected tumor-immune ecosystem.",
         "domain": "biotech", "score": "~5% five-year survival today",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-07-01-a-deadly-pill-made-safe-in-three-hours-on-a-laptop"]},
        {"id": "2026-07-03-the-us-death-rate-hits-a-record-low",
         "title": "The US death rate falls to a record low",
         "claim": "The CDC reported the US death rate fell 4.6% to a record low of roughly 689 "
                  "per 100,000, with a sharp drop in young overdose deaths pushing life "
                  "expectancy toward a high even as heart disease and cancer rose.",
         "domain": "biotech", "actor": ["cdc"], "score": "689 per 100,000",
         "evidences": ["longevity-escape-velocity"],
         "supersedes": [B + "developments/2026-06-22-cervical-cancer-death-cut-to-effectively-zero"]},
        {"id": "2026-07-03-participation-at-a-fifty-year-low",
         "title": "Labor-force participation hits a fifty-year low as unemployment falls",
         "claim": "Labor-force participation slid to 61.5%, a fifty-year low outside Covid, with "
                  "720,000 people stepping out and headline unemployment falling to 4.2% — the "
                  "first readout of a post-labor economy through instruments built for the old "
                  "one.",
         "domain": "economics", "score": "61.5% participation / 4.2% unemployment",
         "evidences": ["post-labor-instruments", "work-displaced", "humans-need-not-apply"],
         "supersedes": [B + "developments/2026-07-01-the-labor-apocalypse-keeps-missing"],
         "body": "Unemployment falls precisely because participation does. The two "
                 "numbers point in opposite directions only if you assume everyone "
                 "not working is looking."},
        {"id": "2026-07-03-only-natural-persons-can-invent",
         "title": "A supreme court holds that only natural persons can be named inventors",
         "claim": "Japan's Supreme Court shut the door on naming an AI system the inventor on a "
                  "patent application, holding that only natural persons qualify, while a Right "
                  "to Intelligence campaign argued people should freely run open models so long "
                  "as fraud and abuse stay prosecuted.",
         "domain": "policy", "actor": ["japan-supreme-court"],
         "evidences": ["legislating-the-shift", "agent-society", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-06-05-a-legal-home-for-non-human-corporations"]},
    ],
}
