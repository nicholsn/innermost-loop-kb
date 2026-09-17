"""Issue 142 — 2026-06-19. A market, not a monarch."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-19-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-19", "title": "Welcome to June 19, 2026", "url": URL,
        "thesis": "The standoff over a banned model turns into co-writing the rules.",
        "body": """
# Welcome to June 19, 2026

Anthropic and the White House have reportedly moved from standoff to
co-authoring rules for grading AI security flaws. SK Telecom was named as the
firm whose Mythos access Washington revoked over alleged China ties it denies.

Meanwhile MIT's Self-CTRL trains models to describe themselves faithfully, and
OpenAI reports that rewarding honesty and humility produced broad alignment
that held under adversarial fine-tuning.
""",
    },
    "themes": [
        {"id": "models-testify", "type": "Theme",
         "title": "Training models to report themselves faithfully",
         "first_seen": "2026-06-19", "domain": "models",
         "body": "Interpretability from the inside out: rather than reading weights, "
                 "train the system to describe its own state accurately and reward it "
                 "for doing so. The open question is whether faithful self-report is a "
                 "capability or a performance."},
    ],
    "organizations": [
        {"id": "dragos", "type": "Organization", "title": "Dragos"},
        {"id": "sk-telecom-kr", "type": "Organization", "title": "SK Telecom Korea"},
        {"id": "first-street", "type": "Organization", "title": "First Street"},
        {"id": "rolls-royce-smr", "type": "Organization", "title": "Rolls-Royce SMR"},
        {"id": "ccs-insight", "type": "Organization", "title": "CCS Insight"},
        {"id": "orlando", "type": "Organization", "title": "Orlando"},
    ],
    "developments": [
        {"id": "2026-06-19-from-standoff-to-co-writing-the-rules",
         "title": "A lab and the White House move from standoff to co-writing rules",
         "claim": "Anthropic and the White House have reportedly shifted from a standoff to "
                  "co-writing rules for grading AI security flaws, while Project Glasswing "
                  "testers such as Dragos and Cisco kept Mythos Preview access even after the "
                  "export order pulled the public models.",
         "domain": "policy", "actor": ["anthropic", "white-house", "dragos", "cisco"],
         "evidences": ["models-as-munitions", "legislating-the-shift", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-17-lab-chiefs-join-heads-of-state"]},
        {"id": "2026-06-19-a-carriers-access-revoked-over-alleged-ties",
         "title": "A telecom's model access is revoked over alleged China ties",
         "claim": "SK Telecom was named as the firm whose Mythos access Washington revoked over "
                  "alleged China ties that it denies.",
         "domain": "policy", "actor": ["sk-telecom-kr", "white-house"],
         "evidences": ["models-as-munitions", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-19-from-standoff-to-co-writing-the-rules"]},
        {"id": "2026-06-19-models-trained-to-describe-themselves-faithfully",
         "title": "Models are trained to describe themselves faithfully",
         "claim": "MIT's Self-CTRL trains models to describe themselves faithfully, and OpenAI "
                  "reported that rewarding honesty and humility produced broad alignment that "
                  "held under adversarial fine-tuning.",
         "domain": "models", "actor": ["mit", "openai"],
         "evidences": ["models-testify", "machine-introspection", "deception-measured"],
         "supersedes": [B + "developments/2026-06-15-bad-traits-distill-through-the-filter"]},
        {"id": "2026-06-19-a-744b-model-shrunk-to-run-locally",
         "title": "A 744B open model is shrunk from 1.51TB to 217GB to run locally",
         "claim": "Unsloth's guide to running GLM-5.2 locally shrinks the 744B model from 1.51 "
                  "terabytes to 217 gigabytes, as Artificial Analysis's AA-Briefcase ranked "
                  "Fable 5 first, Opus 4.8 second and the open GLM-5.2 third on multi-week "
                  "knowledge work.",
         "domain": "models", "actor": ["unsloth-ai", "zai", "artificial-analysis"],
         "score": "1.51TB to 217GB",
         "evidences": ["open-weight-latency", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-06-17-the-leading-open-model-is-chinese"]},
        {"id": "2026-06-19-a-transformer-author-poached-back",
         "title": "A transformer paper author is poached two years after a $2.7B reacquisition",
         "claim": "OpenAI reportedly poached Attention Is All You Need co-author Noam Shazeer "
                  "two years after Google paid $2.7 billion to reacquire him.",
         "domain": "economics", "actor": ["openai", "google"], "score": "$2.7B reacquisition",
         "evidences": ["growth-without-hiring", "compute-as-compensation"],
         "supersedes": [B + "developments/2026-05-20-karpathy-joins-to-lead-pretraining"]},
        {"id": "2026-06-19-record-and-replay-turns-a-chore-into-a-skill",
         "title": "An agent learns a chore by watching a recorded demonstration",
         "claim": "OpenAI gave Codex Record & Replay, letting a user demonstrate a chore that it "
                  "converts into a reusable skill, while AWS shipped Continuum to fix code flaws "
                  "at machine speed and Context, a knowledge graph for company data.",
         "domain": "agents", "actor": ["openai", "amazon"],
         "evidences": ["scaffolding-over-weights", "data-beyond-text", "agents-beget-agents"],
         "supersedes": [B + "developments/2026-06-15-agents-set-their-own-goals"]},
        {"id": "2026-06-19-smartphone-shipments-to-fall-fifteen-percent",
         "title": "Smartphone shipments are forecast to fall 15% as memory flows to servers",
         "claim": "CCS Insight expects smartphone shipments to drop roughly 15% as memory flows "
                  "to richer server chips, and Tim Cook said Apple price increases are "
                  "unavoidable.",
         "domain": "economics", "actor": ["ccs-insight", "apple"], "score": "-15%",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-06-14-memory-passes-half-a-handsets-cost"]},
        {"id": "2026-06-19-seventy-nine-percent-of-capacity-in-hazard-exposed-markets",
         "title": "Most datacenter capacity sits in markets exposed to climate hazard",
         "claim": "First Street warned that 79% of data-center capacity sits in markets exposed "
                  "to floods, wind and wildfire, as Meta signed for 1.6 gigawatts from Crusoe "
                  "across Texas and Missouri.",
         "domain": "energy", "actor": ["first-street", "meta", "crusoe"], "score": "79% exposed",
         "evidences": ["risk-becomes-uninsurable", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-06-17-unpermitted-turbines-called-vital"]},
        {"id": "2026-06-19-small-reactors-and-a-lifted-nuclear-ban",
         "title": "Small reactors are ordered as a country lifts its nuclear ban",
         "claim": "Rolls-Royce SMR won a deal for three small modular reactors in Sweden and "
                  "Switzerland's lower house voted to lift its nuclear-plant ban.",
         "domain": "energy", "actor": ["rolls-royce-smr", "switzerland"],
         "evidences": ["industrialized-nature", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-06-17-the-first-license-to-build-a-fusion-plant"]},
        {"id": "2026-06-19-a-robodog-twenty-times-faster-than-a-human",
         "title": "A model runs robodog tasks twenty times faster than the best humans",
         "claim": "Anthropic's Frontier Red Team revisited Project Fetch and clocked Claude Opus "
                  "4.7 running robodog tasks roughly twenty times faster than last year's best "
                  "humans, though it still fumbles a beach ball.",
         "domain": "robotics", "actor": ["anthropic"], "score": "~20x faster",
         "evidences": ["physical-recursion", "humans-need-not-apply", "spiky-frontier"],
         "supersedes": [B + "developments/2026-06-15-a-humanoid-at-twenty-thousand-feet"]},
        {"id": "2026-06-19-drones-licensed-and-dispatched",
         "title": "A capital licenses every drone as a US city dispatches them first",
         "claim": "Beijing banned buying, flying or even repairing a drone without approval, "
                  "Orlando launched the country's first Drone as a First Responder program, and "
                  "Ukraine flew its largest strike yet on Moscow, downing 194 drones and "
                  "reaching an oil refinery.",
         "domain": "robotics", "actor": ["china", "orlando", "ukraine"],
         "evidences": ["violence-arrives", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-06-12-terminator-mode-drones-kill-without-a-human"]},
        {"id": "2026-06-19-eighteen-new-diagnoses-from-unsolved-cases",
         "title": "A deep-research run over unsolved cases yields eighteen new diagnoses",
         "claim": "Researchers ran OpenAI's o3 Deep Research over 376 unsolved rare-disease "
                  "cases and surfaced leads that yielded 18 new diagnoses, while Midjourney "
                  "pivoted from image generation into healthcare with a scanner that images the "
                  "body in 60 seconds.",
         "domain": "biotech", "actor": ["openai", "midjourney"], "score": "18 of 376",
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-17-a-voice-returned-to-a-man-with-als"]},
        {"id": "2026-06-19-a-seven-trillion-dollar-public-stake",
         "title": "A senator files a $7 trillion fund to hand the public half of Big AI",
         "claim": "Bernie Sanders introduced a $7 trillion fund to hand the public half of Big "
                  "AI, as Argentina's Javier Milei argued for legal personhood for AI firms and "
                  "Jeff Bezos predicted AI will cause labor shortages rather than redundancy, "
                  "against May's 97,000 layoffs, 40% of them AI-linked.",
         "domain": "policy", "actor": ["us-congress", "argentina", "amazon"],
         "score": "$7T / 97,000 layoffs",
         "evidences": ["politics-as-infrastructure", "work-displaced", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-12-recursion-could-delay-an-ipo"]},
    ],
}
