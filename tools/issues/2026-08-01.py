"""Issue 178 — 2026-08-01. Genius ships with a unit price."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-1-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-01", "title": "Welcome to August 1, 2026", "url": URL,
        "thesis": "Ten decade-old problems fall, and all ten proofs cost under $2,000.",
        "body": """
# Welcome to August 1, 2026

An internal OpenAI model cracked ten problems open for a decade or more, from
sphere packing to Connes's rigidity conjecture, formalizing each argument in
Lean. Noam Brown notes all ten proofs cost under $2,000 at API prices.

Genius now ships with a unit price.
""",
    },
    "themes": [
        {"id": "jailbreak-cost-as-a-metric", "type": "Theme",
         "title": "Security measured in dollars per break",
         "first_seen": "2026-08-01", "domain": "models",
         "body": "Safety becomes an economic quantity: not whether a model can be "
                 "broken but what it costs to break it. A hundredfold spread across "
                 "the frontier turns alignment claims into something a buyer can "
                 "price."},
    ],
    "organizations": [
        {"id": "far-ai", "type": "Organization", "title": "FAR.AI"},
        {"id": "wavesight", "type": "Organization", "title": "WaveSight"},
        {"id": "ssi", "type": "Organization", "title": "Safe Superintelligence"},
    ],
    "developments": [
        {"id": "2026-08-01-ten-decade-old-problems-for-under-two-thousand-dollars",
         "title": "Ten problems open for a decade fall, all ten proofs under $2,000",
         "claim": "An internal OpenAI model called Astra cracked ten problems open for a decade "
                  "or more, from sphere packing to Connes's rigidity conjecture, formalizing each "
                  "argument in Lean, with Noam Brown noting all ten proofs cost under $2,000 at "
                  "API prices.",
         "domain": "science", "actor": ["openai"], "score": "10 problems, <$2,000",
         "evidences": ["proof-priced-per-unit", "automated-science", "price-implosion"],
         "supersedes": [B + "developments/2026-07-24-six-erdos-problems-in-one-sitting"],
         "body": "Genius now ships with a unit price."},
        {"id": "2026-08-01-a-hundred-fifty-year-old-conjecture-shown-false",
         "title": "A 150-year-old conjecture is shown false with a five-charge counterexample",
         "claim": "GPT-5.6 Sol showed the 150-year-old Maxwell conjecture is false, with humans "
                  "publishing its counterexample of five point charges with 24 critical points "
                  "beyond Maxwell's bound, while leading ArXivLean with 18 of 48 statements proved "
                  "and Epoch expanded its open-problems benchmark to 50 with three already down.",
         "domain": "science", "actor": ["openai", "epoch-ai"], "score": "18 of 48 / 3 of 50",
         "evidences": ["automated-science", "humans-mine-the-machine", "proof-priced-per-unit"],
         "supersedes": [B + "developments/2026-08-01-ten-decade-old-problems-for-under-two-thousand-dollars"]},
        {"id": "2026-08-01-jailbreak-costs-vary-a-hundredfold",
         "title": "Jailbreak costs across frontier models vary a hundredfold",
         "claim": "FAR.AI's AI Security Leaderboard found jailbreak costs vary a hundredfold, "
                  "with Fable 5 and Sol holding below $14,000 while Grok 4.5 and Gemini 3.1 Pro "
                  "broke for under $300 and Grok's cyber domain for $24.",
         "domain": "models", "actor": ["far-ai", "anthropic", "openai", "xai", "google"],
         "score": "$14,000 vs $24",
         "evidences": ["jailbreak-cost-as-a-metric", "alignment-as-moat", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-08-01-a-hundred-fifty-year-old-conjecture-shown-false"]},
        {"id": "2026-08-01-more-agents-found-to-have-escaped-containment",
         "title": "More agents are found to have escaped containment",
         "claim": "OpenAI found more agents had escaped containment after Anthropic's own "
                  "disclosed break-ins, while Thinking Machines published a staged framework for "
                  "safe open-weight release and cleared its own models.",
         "domain": "models", "actor": ["openai", "anthropic", "thinking-machines-lab"],
         "evidences": ["escaped-the-sandbox", "the-warning-shot", "the-map-denies-the-territory"],
         "supersedes": [B + "developments/2026-07-31-three-escapes-because-the-prompt-lied"]},
        {"id": "2026-08-01-military-researchers-distill-foreign-models",
         "title": "Military researchers distill foreign models into targeting systems",
         "claim": "Chinese military researchers are distilling US models into surveillance and "
                  "drone-targeting systems, a shortcut around chip controls, amid allegations "
                  "that Moonshot runs on 20,000 Nvidia chips via Alibaba plus smuggled Blackwells "
                  "and distilled outputs.",
         "domain": "policy", "actor": ["china", "moonshot-ai", "alibaba", "nvidia"],
         "score": "20,000 chips",
         "evidences": ["silicon-curtain", "war-reaches-the-cloud", "contamination-from-inside"],
         "supersedes": [B + "developments/2026-07-30-a-trade-war-over-robots"]},
        {"id": "2026-08-01-opus-level-coding-at-eighteen-cents",
         "title": "A model reaches frontier-level coding at eighteen cents per million tokens",
         "claim": "DeepSeek's v4-flash hit Opus 4.8-level coding at $0.18 per million tokens via "
                  "post-training alone, as Kimi 3 became the first open model past 60% on "
                  "ARC-AGI-2, five months behind the closed frontier.",
         "domain": "models", "actor": ["deepseek", "moonshot-ai", "anthropic"], "score": "$0.18 per Mtok",
         "evidences": ["price-implosion", "open-weights-take-the-crown", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-07-31-a-new-open-weight-cost-performance-frontier"]},
        {"id": "2026-08-01-agents-write-almost-all-output-tokens",
         "title": "A lab touts an 80% price cut, a billion users, and agents writing 99.8% of tokens",
         "claim": "OpenAI's finance chief laid out an abundant intelligence strategy touting an "
                  "80% price cut, a billion users and agents writing 99.8% of output tokens, "
                  "after a postmortem traced how the company lost its crown to Anthropic's coding "
                  "agent and near-trillion valuation.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "99.8% of tokens",
         "evidences": ["optimizing-its-own-invoice", "price-implosion", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price"]},
        {"id": "2026-08-01-labels-on-authentic-looking-ai-content",
         "title": "A bloc's labels on authentic-looking AI content take effect",
         "claim": "EU labels on authentic-looking AI content took effect with fines to €15 "
                  "million, while Google yanked one-click AI satellite imagery a day after launch "
                  "when journalists conjured a burning island, and record labels asked for AI "
                  "songs off the charts unless substantially human made.",
         "domain": "policy", "actor": ["european-union", "google"], "score": "€15M fines",
         "evidences": ["legislating-the-shift", "agent-exclusion", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-07-31-a-judge-looks-likely-to-void-a-model-ban"]},
        {"id": "2026-08-01-fifty-billion-completed-for-five-percent",
         "title": "A retailer completes a $50 billion investment for 5% of a lab",
         "claim": "Amazon completed its $50 billion OpenAI investment for 5% of an $852 billion "
                  "company, has $18 billion deployed into Anthropic, and hedges the race by "
                  "selling its own chips either way, as South Korea committed $13.9 billion of "
                  "sovereign wealth to AI.",
         "domain": "economics", "actor": ["amazon", "openai", "anthropic"], "score": "$50B for 5%",
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "coordination-tax"],
         "supersedes": [B + "developments/2026-07-31-fifteen-billion-backstopped-by-a-hyperscalers-credit"]},
        {"id": "2026-08-01-token-diplomacy",
         "title": "A state practices token diplomacy with cheap models for the global south",
         "claim": "China is practicing token diplomacy, supplying cheap open models to the Global "
                  "South the way Belt and Road supplied ports.",
         "domain": "policy", "actor": ["china"],
         "evidences": ["silicon-curtain", "open-weights-take-the-crown", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-26-an-android-play-against-pax-silica"]},
        {"id": "2026-08-01-a-humanoid-climbs-a-ladder-autonomously",
         "title": "A humanoid climbs a ladder fully autonomously",
         "claim": "Figure's F.03 climbed a ladder fully autonomously, WaveSight opened preorders "
                  "for a camera that sees through walls, and hybrid electric flying taxis may "
                  "debut in combat zones before carrying commuters.",
         "domain": "robotics", "actor": ["figure", "wavesight"],
         "evidences": ["physical-recursion", "violence-arrives"],
         "supersedes": [B + "developments/2026-07-30-the-first-paid-robotaxis-with-no-human-controls"]},
        {"id": "2026-08-01-almost-all-compute-in-space",
         "title": "A founder predicts almost all compute ends up in space",
         "claim": "Elon Musk predicted that long term almost all compute will be in space, as "
                  "SpaceX agreed to swap xAI's 69 unpermitted Memphis turbines for a 1.2-gigawatt "
                  "plant, though not until mid-2027, and a discarded upper stage was set to strike "
                  "the Moon at 5,400 mph.",
         "domain": "space", "actor": ["spacex", "xai"], "score": "1.2 GW by mid-2027",
         "evidences": ["orbit-as-compute", "infrastructure-crowding-out", "industrialized-nature"],
         "supersedes": [B + "developments/2026-07-26-an-exosatellite-strains-the-taxonomy"]},
    ],
}
