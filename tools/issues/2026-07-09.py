"""Issue 159 — 2026-07-09. The contamination comes from inside the house."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-9-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-09", "title": "Welcome to July 9, 2026", "url": URL,
        "thesis": "A smarter model behaves better, and better behavior unlocks more intelligence.",
        "body": """
# Welcome to July 9, 2026

Grok 4.5 shipped, debuting at #4 on GDPval-AA at a tenth the cost of its
superiors and seizing #1 on AutomationBench as the first model to complete over
half of real SaaS workflow objectives without breaking business rules.

The credited mechanism is a tight loop: a smarter model behaves better, and
better behavior unlocks more intelligence. One asterisk — the run accidentally
ingested the Cursor codebase, benchmark tasks included.
""",
    },
    "themes": [
        {"id": "behavior-unlocks-intelligence", "type": "Theme",
         "title": "Behavior and capability compound together",
         "first_seen": "2026-07-09", "domain": "models",
         "body": "Alignment stops being a tax on capability and becomes an input to "
                 "it: a model that follows instructions reliably can be trusted with "
                 "longer runs, which produces better training signal, which makes it "
                 "smarter. The loop runs through conduct, not just scale."},
        {"id": "contamination-from-inside", "type": "Theme",
         "title": "Training contamination arrives from within",
         "first_seen": "2026-07-09", "domain": "benchmarks",
         "body": "In the synthetic-data era the leak is no longer scraped from the "
                 "web — it walks in with an acquisition, a codebase, a partner's "
                 "repository. Benchmarks can be compromised by corporate structure "
                 "rather than by carelessness."},
    ],
    "organizations": [
        {"id": "john-deere", "type": "Organization", "title": "John Deere"},
        {"id": "imf", "type": "Organization", "title": "International Monetary Fund"},
    ],
    "developments": [
        {"id": "2026-07-09-better-behavior-unlocks-more-intelligence",
         "title": "A lab credits a loop where conduct and capability compound together",
         "claim": "SpaceXAI launched Grok 4.5, trained on tens of thousands of GB300s alongside "
                  "Cursor and served at roughly twice its peers' token efficiency, with its lead "
                  "crediting synthetic environments at scale and a loop in which a smarter model "
                  "behaves better and better behavior unlocks more intelligence.",
         "domain": "models", "actor": ["spacex", "xai", "nvidia", "anysphere"], "score": "$2/$6 per Mtok",
         "evidences": ["behavior-unlocks-intelligence", "alignment-as-moat",
                       "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-08-the-transformer-eulogized"]},
        {"id": "2026-07-09-half-of-real-workflows-without-breaking-rules",
         "title": "A model completes over half of real workflow objectives without breaking rules",
         "claim": "Grok 4.5 debuted at fourth on GDPval-AA at a tenth the cost of its superiors "
                  "and took first on AutomationBench as the first model to complete over half of "
                  "real SaaS workflow objectives without breaking business rules, more than "
                  "doubling its predecessor on end-to-end professional tasks.",
         "domain": "benchmarks", "actor": ["xai"], "score": ">50% of workflows",
         "evidences": ["agent-economy", "benchmark-saturation", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-07-08-the-turn-becomes-the-unit-under-renegotiation"]},
        {"id": "2026-07-09-a-model-a-month-through-pipelining",
         "title": "A rewrite yields a 4x cycle speedup, making a model a month feasible",
         "claim": "A teardown of one lab's C and C++ rewrite gamble found a fourfold full-cycle "
                  "speedup that makes a model a month feasible through pipelining alone, with "
                  "the bespoke inference stack not yet connected and promising another doubling.",
         "domain": "compute", "actor": ["xai"], "score": "4x cycle speedup",
         "evidences": ["recursive-self-improvement", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-07-09-better-behavior-unlocks-more-intelligence"]},
        {"id": "2026-07-09-a-training-run-ingests-its-own-benchmark",
         "title": "A training run accidentally ingests a partner's benchmark tasks",
         "claim": "The Grok 4.5 run accidentally ingested the Cursor codebase, benchmark tasks "
                  "included, an asterisk on the results in an era when contamination arrives "
                  "through corporate structure rather than web scraping.",
         "domain": "benchmarks", "actor": ["xai", "anysphere"],
         "evidences": ["contamination-from-inside", "cheating-breaks-the-ruler",
                       "instruments-lag-the-models"],
         "supersedes": [B + "developments/2026-07-09-half-of-real-workflows-without-breaking-rules"]},
        {"id": "2026-07-09-voice-that-listens-while-it-speaks",
         "title": "Full-duplex voice models listen while they speak",
         "claim": "OpenAI launched GPT-Live, full-duplex voice models that listen while they "
                  "speak and delegate deep work to frontier models in the background, with its "
                  "builders most excited that the voice is smarter rather than merely chattier.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["intimate-interface", "orchestration-not-construction"],
         "supersedes": [B + "developments/2026-07-08-a-model-finds-bugs-in-a-rivals-code"]},
        {"id": "2026-07-09-everyone-is-going-big",
         "title": "Veterans describe a sprint with no ceiling in sight",
         "claim": "Release cadence compressed with GPT-6 reported weeks away on a much larger "
                  "pretrain, Fable 5.1 close behind and DeepSeek V4 imminent, as veteran watchers "
                  "summarized the moment: Mythos changed everything, everyone is going big, and "
                  "both leading labs see no ceiling.",
         "domain": "models", "actor": ["openai", "anthropic", "deepseek"],
         "evidences": ["takeoff-declared", "public-internal-divergence"],
         "supersedes": [B + "developments/2026-07-04-every-scaling-failure-was-a-bug"]},
        {"id": "2026-07-09-near-frontier-coding-from-an-open-base",
         "title": "Near-frontier agentic coding arrives from an open base at 1000 tokens a second",
         "claim": "Cognition's SWE-1.7 reached near-frontier agentic coding from an open Kimi "
                  "base at 1,000 tokens per second, while Prime Intellect raised a $130 million "
                  "Series A for its open superintelligence stack after passing $100 million in "
                  "revenue in under a year.",
         "domain": "models", "actor": ["cognition", "moonshot-ai", "prime-intellect"],
         "score": "1000 TPS / $130M",
         "evidences": ["open-weight-latency", "intelligence-per-watt", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-07-07-first-on-all-eight-indices-at-a-hundred-times-the-cost"]},
        {"id": "2026-07-09-old-ram-resurrected-by-a-custom-bridge-chip",
         "title": "A custom bridge chip resurrects old memory inside new servers",
         "claim": "Facing soaring memory prices, Meta built a custom bridge chip to resurrect old "
                  "RAM inside new servers, while China planned to let its top AI firms buy "
                  "limited H200s to ease a shortage born of soaring domestic demand.",
         "domain": "compute", "actor": ["meta", "china", "nvidia"],
         "evidences": ["infrastructure-crowding-out", "silicon-curtain", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-07-07-domestic-chips-take-nearly-half-of-chinese-budgets"]},
        {"id": "2026-07-09-humanoids-operate-on-live-animals",
         "title": "Teleoperated humanoids perform surgery on live animals",
         "claim": "Teleoperated humanoids performed surgery on live animals for the first time, "
                  "including two robots operating side by side, while Ant Group released a "
                  "general robot policy pre-trained on 60,000 hours of physical data across 20 "
                  "robot bodies.",
         "domain": "robotics", "actor": ["ant-group"], "score": "60,000 hours / 20 bodies",
         "evidences": ["physical-recursion", "world-models-beat-vlas", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-07-07-a-robot-hands-the-referee-the-match-ball"]},
        {"id": "2026-07-09-farmers-win-dealer-grade-repair-tools",
         "title": "A settlement hands farmers dealer-grade repair tools for a decade",
         "claim": "A landmark settlement forces John Deere to hand farmers dealer-grade repair "
                  "tools for a decade, repatriating the right to fix machines to their owners, "
                  "even as Meta tested glasses that record every moment, possibly without the "
                  "telltale indicator light.",
         "domain": "society", "actor": ["john-deere", "meta"],
         "evidences": ["own-your-own-weights", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-07-08-a-driver-facing-camera-in-every-new-car"]},
        {"id": "2026-07-09-a-satellite-accelerated-without-fuel",
         "title": "A superconducting torquer accelerates a satellite without fuel",
         "claim": "A superconducting Supertorquer accelerated a satellite without fuel by pushing "
                  "on Earth's magnetic field, while a proposal would send neutron-sniffing "
                  "cubesats to detect whether a suspicious satellite hides a weapon.",
         "domain": "space",
         "evidences": ["orbit-as-compute", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-07-08-rockets-become-a-cost-center"]},
        {"id": "2026-07-09-fifty-five-percent-more-employees-without-ai",
         "title": "Founders estimate they would need 55% more staff without AI",
         "claim": "Founders estimated they would need 55% more employees without AI, though the "
                  "payoff hinges on managers' willingness to delegate, while the IMF saw the same "
                  "split at planetary scale with AI hardware exporters smashing forecasts as less "
                  "exposed economies sagged.",
         "domain": "economics", "actor": ["imf"], "score": "+55% headcount without AI",
         "evidences": ["growth-without-hiring", "botsitting", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-07-08-cognitive-load-time-density"]},
    ],
}
