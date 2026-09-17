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
    "people": [
        {"id": "sarah-friar", "type": "Person", "title": "Sarah Friar", "name": "Sarah Friar",
         "description": "OpenAI's chief financial officer, whose abundant-intelligence strategy priced the company's plans off an 80% cut and agents writing 99.8% of output tokens.",
         "resource": "https://x.com/sarahfriar",
         "sameAs": ["http://www.wikidata.org/entity/Q107434318"],
         "tags": ["executive"],
         "body": "Sarah Friar is OpenAI's chief financial officer, previously chief executive of Nextdoor. "
                 "In this corpus she appears as the author of the "
                 "[abundant-intelligence strategy](/developments/2026-08-01-agents-write-almost-all-output-tokens.md) "
                 "of August 2026 and, two days earlier, as the executive who told employees that "
                 "[July's revenue run-rate topped the entire second quarter](/developments/2026-07-30-solo-founders-run-million-dollar-companies.md)."},
    ],
    "roles": [
        {"id": "sarah-friar-openai-cfo", "type": "Role",
         "title": "Sarah Friar, chief financial officer at OpenAI",
         "roleName": "Chief Financial Officer",
         "memberOf": [B + "organizations/openai"],
         "holder": [B + "people/sarah-friar"],
         "description": "The position from which she laid out OpenAI's abundant-intelligence strategy and reported the July 2026 revenue run-rate.",
         "body": "As OpenAI's finance chief she framed the company's "
                 "[abundant-intelligence strategy](/developments/2026-08-01-agents-write-almost-all-output-tokens.md) "
                 "around an 80% price cut, a billion users and agents writing 99.8% of output tokens, and told "
                 "employees that [July's run-rate exceeded all of Q2](/developments/2026-07-30-solo-founders-run-million-dollar-companies.md)."},
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
         "description": "The recursive loop restated as corporate strategy: a lab's finance chief "
                        "prices abundance off gains the models produced for themselves, in a plan "
                        "written from behind in the race.",
         "domain": "economics", "actor": ["openai", "people/sarah-friar"],
         "score": "99.8% of tokens",
         "about": [B + "systems/codex", B + "systems/claude-code", B + "systems/gpt-5-6-sol"],
         "evidences": ["optimizing-its-own-invoice", "price-implosion", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price",
                        B + "developments/2026-06-26-an-agent-generates-almost-all-its-own-output"],
         "relatedTo": [B + "developments/2026-02-03-codex-builds-itself",
                       B + "developments/2026-02-08-100pct-of-product-code",
                       B + "developments/2026-07-30-solo-founders-run-million-dollar-companies"],
         "tags": ["rsi", "ai-r-and-d"],
         "supporting_text": "agents writing 99.8% of output tokens",
         "sources": [{"id": "openai-building-abundant-intelligence",
                      "resource": "https://openai.com/index/building-abundant-intelligence/",
                      "title": "Building abundant intelligence", "author": "org:openai"},
                     {"id": "wsj-how-openai-lost-its-ai-crown",
                      "resource": "https://www.wsj.com/tech/ai/how-openai-lost-its-ai-crownand-the-fight-to-win-it-back-7d069695",
                      "title": "How OpenAI Lost Its AI Crown, and the Fight to Win It Back",
                      "author": "org:wall-street-journal"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "OpenAI's chief financial officer [Sarah Friar](/people/sarah-friar.md) laid out an "
                 "\"abundant intelligence\" strategy ([OpenAI](https://openai.com/index/building-abundant-intelligence/)) "
                 "built on three numbers: the [80% GPT-5.6 price cut](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) "
                 "of two days earlier, a billion users, and agents writing 99.8% of output tokens, the figure "
                 "first reported in June when [Codex](/systems/codex.md) was found "
                 "[generating almost all of its own weekly output](/developments/2026-06-26-an-agent-generates-almost-all-its-own-output.md). "
                 "It landed alongside a Wall Street Journal postmortem "
                 "([WSJ](https://www.wsj.com/tech/ai/how-openai-lost-its-ai-crownand-the-fight-to-win-it-back-7d069695)) "
                 "on how the company lost its lead to Anthropic's [Claude Code](/systems/claude-code.md) and "
                 "near-trillion valuation, an account OpenAI answers with [Sol](/systems/gpt-5-6-sol.md) and a "
                 "Codex super app. In the trajectory it is the moment the loop's outputs, self-written kernels "
                 "and self-generated tokens, become the headline of a lab's business plan rather than a "
                 "research aside, following the February reports that [Codex builds itself](/developments/2026-02-03-codex-builds-itself.md) "
                 "and that [all of Anthropic's product code is written by Claude](/developments/2026-02-08-100pct-of-product-code.md), "
                 "and a day before an Anthropic researcher argued that "
                 "[labs will compete with their own customers](/developments/2026-08-02-labs-will-compete-with-their-own-customers.md)."},
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
