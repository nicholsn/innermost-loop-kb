"""Issue 167 — 2026-07-18. An open model beats every closed rival."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-18-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-18", "title": "Welcome to July 18, 2026", "url": URL,
        "thesis": "For the first time an open-weight model beats every closed rival.",
        "body": """
# Welcome to July 18, 2026

Kimi K3 took first on SpreadsheetBench 2, surpassing Claude Fable 5 to become
the first open-weight model to beat every closed rival on a benchmark. One
observer called the earlier Frontend Code Arena win a DeepSeek 2.0 moment.

Four launches in eight days lifted six labs above 50 on the intelligence index,
up from two in June. The top three models now span three points across three
labs.
""",
    },
    "themes": [
        {"id": "open-weights-take-the-crown", "type": "Theme",
         "title": "Open weights beat every closed rival",
         "first_seen": "2026-07-18", "domain": "models",
         "body": "The threshold the field had treated as hypothetical: a freely "
                 "downloadable model that is simply better than everything anyone "
                 "sells. Every argument built on the assumption that the best model "
                 "is a product has to be re-derived."},
    ],
    "organizations": [
        {"id": "braincore", "type": "Organization", "title": "BrainCo"},
        {"id": "australia", "type": "Organization", "title": "Australia"},
    ],
    "developments": [
        {"id": "2026-07-18-an-open-model-beats-every-closed-rival",
         "title": "An open-weight model tops a benchmark ahead of every closed model",
         "claim": "Kimi K3 ranked first on SpreadsheetBench 2, surpassing Claude Fable 5 to "
                  "become the first open-weight model to beat every closed rival, with one "
                  "observer calling its earlier Frontend Code Arena win, the first time a Chinese "
                  "model led the US there, a DeepSeek 2.0 moment.",
         "domain": "models", "actor": ["moonshot-ai", "anthropic"],
         "evidences": ["open-weights-take-the-crown", "frontier-not-bought", "price-implosion"],
         "supersedes": [B + "developments/2026-07-17-an-open-model-autonomously-designs-a-chip"]},
        {"id": "2026-07-18-six-labs-above-fifty-up-from-two",
         "title": "Four launches in eight days lift six labs above an intelligence threshold",
         "claim": "Four launches in eight days — Grok 4.5, GPT-5.6, Muse Spark 1.1 and K3 — "
                  "lifted six labs above 50 on the intelligence index, up from two in June, with "
                  "the top three models spanning just three points across three labs and Fable "
                  "5's lead narrowing from four points to one.",
         "domain": "benchmarks", "score": "6 labs above 50, up from 2",
         "evidences": ["price-implosion", "monoculture-is-the-vulnerability", "spiky-frontier"],
         "supersedes": [B + "developments/2026-07-18-an-open-model-beats-every-closed-rival"]},
        {"id": "2026-07-18-cheaper-cognition-summons-more-silicon",
         "title": "Analysts argue cheaper cognition summons more silicon, not less",
         "claim": "The reflexive fear that K3's lean attention dooms Nvidia gets it backwards, "
                  "since its 2.8 trillion parameters spread 896 experts across racks starved for "
                  "bandwidth, and Jevons' Paradox means cheaper cognition summons more silicon "
                  "rather than less.",
         "domain": "economics", "actor": ["nvidia", "moonshot-ai"], "score": "896 experts",
         "evidences": ["price-implosion", "compute-capital-stack", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-07-18-six-labs-above-fifty-up-from-two"]},
        {"id": "2026-07-18-open-weights-called-quietly-decelerationist",
         "title": "A policy lead argues open weights are quietly decelerationist",
         "claim": "OpenAI's Dean Ball argued open weights are quietly decelerationist, an "
                  "ungovernable road toward full AI communism, predicting Washington will "
                  "manufacture regulatory uncertainty around Chinese weights rather than ban them "
                  "outright, while admirers rechristened the movement the Frontier Liberation "
                  "Front.",
         "domain": "policy", "actor": ["openai", "white-house"],
         "evidences": ["open-weights-take-the-crown", "pegged-to-the-rival", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-14-a-ceiling-pegged-to-a-rivals-open-weights"]},
        {"id": "2026-07-18-intelligence-per-dollar-is-the-only-score",
         "title": "An investor calls intelligence per dollar the only score that matters",
         "claim": "Gavin Baker called cheaper open models net positive for every layer except the "
                  "two labs with the fattest margins, because intelligence per dollar is the only "
                  "score that matters, adding that the one reprieve is a superior product or a "
                  "secret head start toward recursive self-improvement.",
         "domain": "economics",
         "evidences": ["intelligence-per-watt", "price-implosion", "public-internal-divergence"],
         "supersedes": [B + "developments/2026-07-18-cheaper-cognition-summons-more-silicon"]},
        {"id": "2026-07-18-a-reversal-read-as-panic",
         "title": "A lab extends rather than retires its flagship, a reversal read as panic",
         "claim": "Anthropic began extending rather than phasing out Fable 5 across subscription "
                  "plans with $100 credits, a reversal skeptics read as panic, while Moonshot "
                  "teased K3.1 and Musk vowed a 2-trillion-parameter model within the week.",
         "domain": "economics", "actor": ["anthropic", "moonshot-ai", "xai"],
         "evidences": ["price-implosion", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-07-14-claudes-values-distilled-into-four-axes"]},
        {"id": "2026-07-18-open-weights-four-to-seven-months-off-the-cyber-frontier",
         "title": "Top open models trail the cyber frontier by just four to seven months",
         "claim": "Britain's safety institute found top open-weight models now trail the cyber "
                  "frontier by just four to seven months, a gap that has narrowed through 2026, "
                  "even as OpenAI reported GPT-5.6 Sol setting a cybersecurity record that "
                  "already helps teams patch real vulnerabilities.",
         "domain": "policy", "actor": ["uk-aisi", "openai"], "score": "4-7 months",
         "evidences": ["open-weight-latency", "war-reaches-the-cloud", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-07-17-the-skeptics-answer-with-falsifiable-calm"]},
        {"id": "2026-07-18-a-finra-style-watchdog-reporting-to-the-sec",
         "title": "Washington drafts a FINRA-style AI watchdog reporting to the securities regulator",
         "claim": "Washington's reply to the frontier race is a FINRA-style watchdog reporting to "
                  "the SEC, echoing a proposal from DeepMind's Demis Hassabis, while Linus "
                  "Torvalds told AI critics to fork the kernel or walk away, a sharp thaw from "
                  "the man who dismissed AI as marketing in 2024.",
         "domain": "policy", "actor": ["white-house", "sec", "google-deepmind"],
         "evidences": ["legislating-the-shift", "the-verifiable-pause"],
         "supersedes": [B + "developments/2026-07-17-an-international-watchdog-proposed-for-pre-release-vetting"]},
        {"id": "2026-07-18-capital-rotates-away-from-capex",
         "title": "A device maker retakes the crown as investors flee capex-heavy chipmakers",
         "claim": "Apple retook the crown as the world's most valuable company at $4.9 trillion "
                  "as investors fled capital-expenditure-heavy chipmakers, though a signed "
                  "leather jacket belonging to Nvidia's chief executive still drew 65 bids to "
                  "fetch $960,000, sixteen times its estimate.",
         "domain": "economics", "actor": ["apple", "nvidia"], "score": "$4.9T",
         "evidences": ["ai-as-the-economy", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-07-18-intelligence-per-dollar-is-the-only-score"]},
        {"id": "2026-07-18-a-country-forces-datacenters-to-make-their-own-power",
         "title": "A country will force datacenters to generate the power they consume",
         "claim": "Australia will force data centers to generate the power they consume and "
                  "shield creators under a new Office of AI, while Japan acquires 27,500 Rubin "
                  "chips for a sovereign robot brain.",
         "domain": "policy", "actor": ["australia", "japan-govt"], "score": "27,500 chips",
         "evidences": ["infrastructure-crowding-out", "legislating-the-shift", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-07-16-a-president-demands-a-moratorium-be-reversed"]},
        {"id": "2026-07-18-a-rival-may-rent-ten-billion-in-gpus-to-a-lab",
         "title": "A rival may rent a lab up to $10 billion in GPUs under a deal the lab proposed",
         "claim": "Meta may rent Anthropic up to $10 billion in GPUs under a deal Anthropic "
                  "itself proposed in June, while SpaceX courted the Pentagon for compute and "
                  "Musk quietly bought over a gigawatt of mobile turbines.",
         "domain": "compute", "actor": ["meta", "anthropic", "spacex", "pentagon"], "score": "$10B",
         "evidences": ["coordination-tax", "compute-capital-stack", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-07-17-a-first-wafer-on-decades-old-technology"]},
        {"id": "2026-07-18-a-theoretical-non-aging-lifespan-of-156-years",
         "title": "Somatic mutations are pegged as the bottleneck cutting a 1,759-year ceiling to 156",
         "claim": "Aging researchers pegged somatic mutations as the bottleneck, with "
                  "post-mitotic neurons and heart cells that never divide cutting a theoretical "
                  "non-aging lifespan of 1,759 years to about 156, still roughly double today's "
                  "span, while Eli Lilly bet $2.8 billion on a Phase 3 nasal spray in the largest "
                  "psychedelics deal in pharma history.",
         "domain": "biotech", "actor": ["eli-lilly"], "score": "156 years / $2.8B",
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-07-15-an-enzyme-rewinds-tissue-by-forty-four-years"]},
        {"id": "2026-07-18-robots-piloted-by-thought-alone",
         "title": "An EEG headset pilots humanoid robots by thought alone",
         "claim": "China's BrainCo unveiled an EEG headset that pilots humanoid robots and "
                  "robotic dogs by thought alone, while a meteorite that crashed through a New "
                  "Jersey home preserved pristine salty fluids and organic chemistry.",
         "domain": "robotics", "actor": ["braincore"],
         "evidences": ["intimate-interface", "physical-recursion", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-07-17-a-school-district-hires-a-humanoid-assistant"]},
    ],
}
