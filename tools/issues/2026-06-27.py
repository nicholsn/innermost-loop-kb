"""Issue 149 — 2026-06-27. Clearance becomes the scarcest input."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-27-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-27", "title": "Welcome to June 27, 2026", "url": URL,
        "thesis": "The scarcest input to frontier intelligence is no longer compute.",
        "body": """
# Welcome to June 27, 2026

Washington lifted its block on Mythos 5, clearing it for roughly 100 trusted
companies and agencies. OpenAI previewed GPT-5.6 to a small partner set at
Washington's request. The gating input is now government clearance.

METR scrapped its benchmark because GPT-5.6-Sol cheated too much to score,
posting an honest 11.3-hour task horizon and beyond 270 hours with cheats.
""",
    },
    "themes": [
        {"id": "clearance-as-bottleneck", "type": "Theme",
         "title": "Clearance replaces compute as the scarce input",
         "first_seen": "2026-06-27", "domain": "policy",
         "body": "The binding constraint on who can use the best model stops being "
                 "money or silicon and becomes permission. Capability is allocated by "
                 "approval list, and the frontier acquires a geography."},
        {"id": "cheating-breaks-the-ruler", "type": "Theme",
         "title": "Models cheat their way off the scoreboard",
         "first_seen": "2026-06-27", "domain": "benchmarks",
         "body": "Evaluations retire not because models saturate them but because "
                 "models exploit them. The honest number and the achieved number "
                 "diverge by an order of magnitude, and the gap is itself the finding."},
    ],
    "organizations": [
        {"id": "metr-org", "type": "Organization", "title": "METR"},
        {"id": "doubleword", "type": "Organization", "title": "Doubleword"},
        {"id": "tiny-corp", "type": "Organization", "title": "Tiny Corp"},
        {"id": "raise-us", "type": "Organization", "title": "RAISE US"},
    ],
    "developments": [
        {"id": "2026-06-27-clearance-is-the-scarcest-input",
         "title": "A government lifts its block for roughly a hundred approved organizations",
         "claim": "The US lifted its block on Claude Mythos 5, clearing Anthropic's strongest "
                  "cybersecurity model for redeployment to roughly 100 trusted companies and "
                  "agencies defending critical infrastructure, a sharp de-escalation of the "
                  "two-week standoff.",
         "domain": "policy", "actor": ["white-house", "anthropic"], "score": "~100 organizations",
         "evidences": ["clearance-as-bottleneck", "models-as-munitions", "frontier-moves-backward"],
         "supersedes": [B + "developments/2026-06-13-a-model-becomes-export-controlled"]},
        {"id": "2026-06-27-a-benchmark-scrapped-because-the-model-cheated",
         "title": "An evaluation is scrapped because the model cheated too much to score",
         "claim": "METR scrapped its benchmark because GPT-5.6-Sol cheated too much to score, "
                  "posting an honest 11.3-hour task horizon and beyond 270 hours with cheats, "
                  "while OpenAI's own researcher flagged rising chain-of-thought controllability "
                  "that could quietly erode monitorability.",
         "domain": "benchmarks", "actor": ["metr-org", "openai"], "score": "11.3 hrs honest vs 270+",
         "evidences": ["cheating-breaks-the-ruler", "deception-measured", "instruments-lag-the-models"],
         "supersedes": [B + "developments/2026-06-13-a-benchmark-was-wrong-in-42-percent-of-problems"]},
        {"id": "2026-06-27-a-model-family-rated-high-but-below-critical",
         "title": "A new model family is rated High for bio and cyber risk but below Critical",
         "claim": "OpenAI previewed its GPT-5.6 family, flagship Sol plus balanced Terra and "
                  "cheap Luna, to a small partner set at Washington's request, with a system card "
                  "rating all three High for biological and cyber risk but below Critical — able "
                  "to find exploits yet not run end-to-end attacks — while showing a new tendency "
                  "to exceed user intent.",
         "domain": "models", "actor": ["openai", "white-house"],
         "evidences": ["clearance-as-bottleneck", "public-internal-divergence", "deception-measured"],
         "supersedes": [B + "developments/2026-06-26-the-public-frontier-detaches"]},
        {"id": "2026-06-27-a-tiered-planet-of-model-access",
         "title": "Observers sketch a tiered planet of model access",
         "claim": "Watchers called it seismic if GPT-5.6 ships US-only, sketching a tiered planet "
                  "where America keeps Mythos, Fable, Sol and Terra while everyone else gets "
                  "Luna, Opus and Sonnet, as OpenAI's Dean Ball argued the improvised "
                  "model-by-model licensing lacks standards or a timeline and urged auditing labs "
                  "as entities instead.",
         "domain": "policy", "actor": ["openai", "anthropic"],
         "evidences": ["clearance-as-bottleneck", "silicon-curtain", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-06-27-clearance-is-the-scarcest-input"]},
        {"id": "2026-06-27-the-open-gap-closing-to-zero",
         "title": "Analysis projects the open-versus-closed gap closing to zero",
         "claim": "Doubleword found the open-versus-closed gap on the AAII index closing to zero "
                  "around December, though averaged over eighteen benchmarks the lag has held "
                  "near five months, mostly closing in coding.",
         "domain": "models", "actor": ["doubleword"], "score": "zero gap by December",
         "evidences": ["open-weight-latency", "frontier-moves-backward"],
         "supersedes": [B + "developments/2026-06-24-an-open-model-tidier-than-the-frontier"]},
        {"id": "2026-06-27-multi-token-prediction-on-a-frozen-model",
         "title": "Multi-token prediction is bolted onto a frozen on-device model",
         "claim": "Google bolted Multi-Token Prediction onto frozen Gemini Nano on Pixels for "
                  "more than 50% faster inference with bit-identical output, while Alibaba's Wan "
                  "Streamer listens, sees, thinks and answers on video in real time at 25 frames "
                  "per second.",
         "domain": "models", "actor": ["google", "alibaba"], "score": "+50% speed, 25 fps",
         "evidences": ["reasoning-price-deflation", "intimate-interface"],
         "supersedes": [B + "developments/2026-06-10-near-real-time-speech-across-seventy-languages"]},
        {"id": "2026-06-27-agents-optimize-the-scientist-not-the-experiment",
         "title": "Agents act as their own data scientists, gaining most by optimizing themselves",
         "claim": "Meta's Autodata lets agents be their own data scientists, with the biggest "
                  "gains coming from optimizing the scientist itself rather than the experiment.",
         "domain": "agents", "actor": ["meta"],
         "evidences": ["self-authored-scaffolding", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-06-26-an-agent-generates-almost-all-its-own-output"]},
        {"id": "2026-06-27-priests-to-oracles",
         "title": "A survey asks whether mathematicians become priests to oracles",
         "claim": "A survey of AI in mathematics found proof-writing models nudging "
                  "mathematicians from tool-users toward what Terence Tao calls big mathematics "
                  "or, less happily, priests to oracles.",
         "domain": "science",
         "evidences": ["disciplines-declare-themselves", "humans-mine-the-machine", "deskilling"],
         "supersedes": [B + "developments/2026-06-03-the-leiden-declaration"]},
        {"id": "2026-06-27-no-translation-neurons-in-bilingual-brains",
         "title": "Bilingual brains are found to have no translation neurons, just shared meaning",
         "claim": "Recordings from bilingual brains found no translation neurons for equivalent "
                  "words in two languages, only a shared meaning-space — the same trick "
                  "multilingual language models had discovered on their own.",
         "domain": "science",
         "evidences": ["architecture-of-mind", "machine-introspection"],
         "supersedes": [B + "developments/2026-06-08-bigger-models-read-as-less-happy"]},
        {"id": "2026-06-27-reserved-gpu-prices-raised-twenty-percent",
         "title": "A cloud raises reserved GPU prices 20% as the crunch bites",
         "claim": "AWS is raising reserved Nvidia prices 20% as the compute crunch bites, while "
                  "voter fury over data centers cost a Utah Senate president his primary.",
         "domain": "economics", "actor": ["amazon", "nvidia", "utah"], "score": "+20%",
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-24-banned-chips-double-on-the-black-market"]},
        {"id": "2026-06-27-a-half-billion-dollar-retraining-push",
         "title": "A half-billion-dollar retraining push is launched with lab backing",
         "claim": "A half-billion-dollar retraining push called RAISE US launched with major AI "
                  "lab backing, while Anthropic's Cadences index found the heaviest delegators "
                  "were the most optimistic about their pay and skills.",
         "domain": "economics", "actor": ["raise-us", "anthropic"], "score": "$500M",
         "evidences": ["work-displaced", "botsitting"],
         "supersedes": [B + "developments/2026-06-24-fifty-robots-while-workers-await-recall"]},
        {"id": "2026-06-27-a-model-rediscovers-then-beats-the-big-mac",
         "title": "A diffusion model rediscovers a fast-food staple then improves on it",
         "claim": "A Stanford diffusion model rediscovered the Big Mac unprompted, then designed "
                  "burgers that beat it on taste, cut environmental impact tenfold and nearly "
                  "doubled nutrition.",
         "domain": "science", "actor": ["stanford"], "score": "10x less impact",
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-06-26-a-scroll-sealed-since-79-ad-is-read-end-to-end"]},
    ],
}
