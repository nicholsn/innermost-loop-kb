"""Issue 162 — 2026-07-12. Reliability doubles every forty days."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-12", "title": "Welcome to July 12, 2026", "url": URL,
        "thesis": "Task reliability doubles every forty days.",
        "body": """
# Welcome to July 12, 2026

METR-style task reliability is doubling every 40 days, on track for one model to
outwork every human who ever lived by 2032. Benedict Evans argues tokens are
destined to be low-margin commodity infrastructure.

Meanwhile AI policy professionals have started reading the Talmud, on the thesis
that a tradition which survived millennia of adverse selection may know
something about surviving recursive self-improvement.
""",
    },
    "themes": [
        {"id": "traditions-as-alignment-priors", "type": "Theme",
         "title": "Old traditions read as value-preservation technology",
         "first_seen": "2026-07-12", "domain": "society",
         "body": "Layered, self-referential reinterpretation that carries core "
                 "commitments across civilizational resets is exactly the property "
                 "wanted in a system that could edit its own values. Survivorship "
                 "across millennia gets read as evidence about mechanism."},
    ],
    "organizations": [
        {"id": "ai-alignment-foundation", "type": "Organization", "title": "AI Alignment Foundation"},
    ],
    "developments": [
        {"id": "2026-07-12-reliability-doubles-every-forty-days",
         "title": "Task reliability doubles every forty days",
         "claim": "METR-style task reliability is doubling every 40 days, on track for one model "
                  "to outwork every human who ever lived by 2032, while Benedict Evans argued "
                  "tokens are destined to be low-margin commodity infrastructure.",
         "domain": "benchmarks", "actor": ["metr-org"], "score": "doubling every 40 days",
         "evidences": ["autonomy-clock-speed", "price-implosion", "takeoff-declared"],
         "supersedes": [B + "developments/2026-07-03-learning-speed-doubles-every-three-months"]},
        {"id": "2026-07-12-policy-professionals-read-the-talmud",
         "title": "Alignment researchers turn to a millennia-old interpretive tradition",
         "claim": "AI policy professionals began studying Jewish texts on the thesis that a "
                  "tradition surviving millennia of adverse selection may know something about "
                  "surviving recursive self-improvement, with one foundation hiring engineers "
                  "versed in them because layered, self-referential reinterpretation preserves "
                  "core values across civilizational resets.",
         "domain": "society", "actor": ["openai", "ai-alignment-foundation"],
         "evidences": ["traditions-as-alignment-priors", "values-negotiated-with-the-model",
                       "doctrine-borrows-the-lab"],
         "supersedes": [B + "developments/2026-06-25-labs-hire-philosophers-to-write-constitutions"],
         "body": "The property wanted is a system that cannot quietly edit its own "
                 "values away."},
        {"id": "2026-07-12-blinded-physicians-prefer-the-model",
         "title": "Blinded physicians find fewer flaws in a model's answers than in doctors'",
         "claim": "GPT-5.6 set a new bar on professional health benchmarks, with blinded "
                  "physicians finding fewer flaws in its answers than in specialty-matched "
                  "doctors' own, while its smallest variant beat GPT-5.5's best reasoning at 25 "
                  "times lower cost.",
         "domain": "biotech", "actor": ["openai"], "score": "25x cheaper",
         "evidences": ["humans-need-not-apply", "price-implosion", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-03-law-professors-prefer-the-machine"]},
        {"id": "2026-07-12-no-moat-just-shared-recipes",
         "title": "A researcher concludes there is no moat, only shared recipes and migration",
         "claim": "A Meta researcher concluded there is no moat, just shared recipes and "
                  "migrating researchers, as a freshness benchmark found only OpenAI and "
                  "Anthropic keep their models' knowledge cutoffs within a year of the present.",
         "domain": "models", "actor": ["meta", "openai", "anthropic"],
         "evidences": ["dark-forest-research", "open-weight-latency", "price-implosion"],
         "supersedes": [B + "developments/2026-07-11-a-rival-delays-to-retrain-a-fresh-base"]},
        {"id": "2026-07-12-a-744b-model-hosted-on-a-laptop",
         "title": "A single-file engine hosts a 744B model on a consumer laptop",
         "claim": "A new single-file C engine lets a consumer laptop host the 744-billion-"
                  "parameter GLM-5.2 by keeping dense layers resident in 25GB of RAM and "
                  "streaming routed experts off disk on demand.",
         "domain": "compute", "actor": ["zai"], "score": "744B in 25GB RAM",
         "evidences": ["intelligence-per-watt", "open-weight-latency", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-07-10-a-record-model-squeezed-onto-a-phone"]},
        {"id": "2026-07-12-a-leaked-preview-of-the-next-frontier-model",
         "title": "A leaked preview points to a 1M-context flagship by month's end",
         "claim": "A leaked preview suggested Anthropic ships Claude Opus 5 by the end of July "
                  "with a million-token context window, with one forecaster predicting Fable 5 "
                  "exits subscriptions and is replaced by an Opus 5 distilled from the unfiltered "
                  "Mythos.",
         "domain": "models", "actor": ["anthropic"], "score": "1M context",
         "evidences": ["public-internal-divergence", "rationed-recursion"],
         "supersedes": [B + "developments/2026-07-11-the-rentable-magic-lags-the-vault"]},
        {"id": "2026-07-12-parallel-test-time-compute-as-the-next-law",
         "title": "A researcher hints the next scaling law is parallel test-time compute",
         "claim": "OpenAI's Noam Brown hinted the next scaling law is parallel test-time compute, "
                  "as Grok 4.5 claimed second on real-world software engineering, up 30 points in "
                  "a year, though Fable 5 kept the crown.",
         "domain": "models", "actor": ["openai", "xai", "anthropic"], "score": "+30 points in a year",
         "evidences": ["autonomy-clock-speed", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-07-12-reliability-doubles-every-forty-days"]},
        {"id": "2026-07-12-circular-financing-beneath-the-buildout",
         "title": "A chipmaker invests in, sells to, and backstops the same customers",
         "claim": "The financing beneath the buildout appears circular, with Nvidia investing in "
                  "the neoclouds, selling them GPUs and backstopping their unsold capacity as "
                  "capital spending outruns cash flow, leaving chip stocks to whipsaw when Meta "
                  "offered to sell excess compute.",
         "domain": "economics", "actor": ["nvidia", "meta"],
         "evidences": ["debt-funded-buildout", "compute-capital-stack", "coordination-tax"],
         "supersedes": [B + "developments/2026-07-11-the-worst-ever-memory-shortage-forecast"]},
        {"id": "2026-07-12-a-general-agent-to-challenge-the-incumbent",
         "title": "A newly acquired IDE maker builds a general agent",
         "claim": "Cursor, being bought by SpaceX at $60 billion, is building a general agent to "
                  "challenge Claude Cowork, while Elon Musk ordered Tesla staff onto Grok citing "
                  "token cost.",
         "domain": "agents", "actor": ["anysphere", "spacex", "tesla", "anthropic"], "score": "$60B",
         "evidences": ["agent-economy", "price-implosion", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-07-08-the-loop-optimizes-whatever-signal-you-give-it"]},
        {"id": "2026-07-12-a-voice-actor-must-prove-he-is-not-a-clone-of-himself",
         "title": "A voice actor must repeatedly prove his real voice is not an AI clone",
         "claim": "A Chinese voice actor must repeatedly prove he is human after platforms "
                  "flagged his real voice as an AI clone of itself, while factories began "
                  "staffing four-hour shifts through an app dubbed the Uber of manufacturing.",
         "domain": "society",
         "evidences": ["agent-exclusion", "bots-outnumber-us", "work-displaced"],
         "supersedes": [B + "developments/2026-07-11-nutrition-labels-for-the-ear"]},
        {"id": "2026-07-12-a-hardening-anti-ai-resistance",
         "title": "A hardening anti-AI resistance takes shape",
         "claim": "The Bay Area now anchors a hardening anti-AI resistance, still on edge over a "
                  "Stop AI co-founder who mused that the ship may have sailed on nonviolence and "
                  "then vanished, while UK shops' facial recognition will soon alert police "
                  "within four seconds of a match.",
         "domain": "society", "score": "4-second police alerts",
         "evidences": ["violence-arrives", "agent-exclusion", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-03-a-campus-abandoned-beside-a-battlefield"]},
        {"id": "2026-07-12-a-cumulative-review-demanded-for-orbital-buildout",
         "title": "Environmental groups demand a cumulative review of a million satellites",
         "claim": "Environmental groups petitioned the FCC to require a cumulative review of "
                  "more than a million proposed satellites, from ozone layer to orbital debris, "
                  "before further licensing, as the first kidney and liver tissues were "
                  "bioprinted aboard the ISS.",
         "domain": "space", "actor": ["fcc-us", "nasa"],
         "evidences": ["orbit-as-compute", "industrialized-nature", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-11-a-hundred-thousand-satellite-fleet-filed-for"]},
    ],
}
