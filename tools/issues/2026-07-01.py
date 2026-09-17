"""Issue 152 — 2026-07-01. The Singularity clears customs."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-1-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-01", "title": "Welcome to July 1, 2026", "url": URL,
        "thesis": "The export controls lift and the models go back out worldwide.",
        "body": """
# Welcome to July 1, 2026

Washington lifted export controls on Fable 5 and Mythos 5, and Anthropic is
redeploying globally — paired with fresh safeguards, a partner framework for
scoring jailbreak severity, and pledges to co-author standards for future
models.

Alex Stamos welcomed the White House to the AI safety club while calling the
détente a huge own goal, betting Chinese models pull ahead on cyber within six
months.
""",
    },
    "themes": [
        {"id": "intelligence-per-watt", "type": "Theme",
         "title": "Efficiency becomes the unit of merit",
         "first_seen": "2026-07-01", "domain": "compute",
         "body": "When capability converges, the question stops being what a model "
                 "can do and becomes what it costs to do it. Local models handling "
                 "the overwhelming majority of real queries reframes the frontier as "
                 "a small, expensive tail."},
    ],
    "organizations": [
        {"id": "together-ai", "type": "Organization", "title": "Together AI"},
        {"id": "conception", "type": "Organization", "title": "Conception"},
        {"id": "ubtech-robotics", "type": "Organization", "title": "UBTech Robotics"},
        {"id": "blackrock", "type": "Organization", "title": "BlackRock"},
        {"id": "henrico-county", "type": "Organization", "title": "Henrico County"},
    ],
    "developments": [
        {"id": "2026-07-01-the-controls-lift-and-the-models-go-global",
         "title": "Export controls lift and a lab redeploys its strongest models worldwide",
         "claim": "Anthropic is redeploying Claude Fable 5 globally after Washington lifted "
                  "export controls on Fable 5 and Mythos 5, pairing the return with fresh "
                  "cybersecurity safeguards, a partner framework for scoring jailbreak severity, "
                  "and pledges to detect risks, co-author standards for future models and flag "
                  "malicious activity.",
         "domain": "policy", "actor": ["anthropic", "white-house"],
         "evidences": ["models-as-munitions", "clearance-as-bottleneck", "the-verifiable-pause"],
         "supersedes": [B + "developments/2026-06-27-clearance-is-the-scarcest-input"],
         "body": "Alex Stamos welcomed the White House to the AI safety club while "
                 "calling the détente a huge own goal for the US, betting Chinese "
                 "models pull ahead on cyber within six months."},
        {"id": "2026-07-01-cheaper-by-the-token-pricier-by-the-task",
         "title": "A cheaper model bills more per task by reasoning more",
         "claim": "Claude Sonnet 5 nears Opus 4.8 at introductory prices of $2 and $10 per "
                  "million tokens, though analysts note it runs cheaper by the token yet pricier "
                  "by the task, burning enough extra reasoning to outbill Opus anyway.",
         "domain": "economics", "actor": ["anthropic"], "score": "$2 / $10 per Mtok",
         "evidences": ["reasoning-price-deflation", "gaming-the-token-metric"],
         "supersedes": [B + "developments/2026-06-28-ai-spend-halved-by-routing-and-caching"]},
        {"id": "2026-07-01-local-models-handle-most-queries",
         "title": "Local models are found able to handle 88.7% of chat queries",
         "claim": "Stanford and Together AI proposed intelligence per watt as a metric, finding "
                  "local models can already handle 88.7% of chat queries, while OpenAI quietly "
                  "halved inference costs and Google's zero-shot tabular foundation model retired "
                  "feature engineering behind a single SQL call.",
         "domain": "compute", "actor": ["stanford", "together-ai", "openai", "google"],
         "score": "88.7% of queries local",
         "evidences": ["intelligence-per-watt", "reasoning-price-deflation", "open-weight-latency"],
         "supersedes": [B + "developments/2026-07-01-cheaper-by-the-token-pricier-by-the-task"]},
        {"id": "2026-07-01-a-surveillance-regime-proposed-to-police-intelligence",
         "title": "A safety institute proposes polygraphs and prison to police AI research",
         "claim": "Researchers at MIRI called for a surveillance regime of polygraphs, prison "
                  "sentences and embedded auditors to police intelligence research itself.",
         "domain": "policy", "actor": ["miri"],
         "evidences": ["the-verifiable-pause", "legislating-the-shift", "agent-exclusion"],
         "supersedes": [B + "developments/2026-06-29-a-duty-of-loyalty-for-agents"]},
        {"id": "2026-07-01-sixty-databases-in-one-workbench",
         "title": "A lab wires sixty-plus databases into one reproducible science workbench",
         "claim": "Anthropic's Claude Science wires more than 60 databases into one reproducible "
                  "workbench and Basecamp's EDEN models let researchers text-prompt antibiotics "
                  "against drug-resistant pathogens, while OpenAI's GeneBench-Pro showed headroom "
                  "remains with its best model passing just 28.7% of 129 research-level problems.",
         "domain": "biotech", "actor": ["anthropic", "basecamp-research", "openai"],
         "score": "28.7% of 129 problems",
         "evidences": ["automated-science", "hardware-grade-biology", "spiky-frontier"],
         "supersedes": [B + "developments/2026-06-28-a-novel-alzheimers-compound-from-a-garage"]},
        {"id": "2026-07-01-a-billion-dollar-army-of-forward-deployed-engineers",
         "title": "A cloud raises a $1B army of forward-deployed engineers",
         "claim": "Amazon raised a $1 billion army of forward-deployed engineers to embed agents "
                  "inside every enterprise.",
         "domain": "economics", "actor": ["amazon"], "score": "$1B",
         "evidences": ["agent-economy", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-06-29-five-archetypes-replace-job-titles"]},
        {"id": "2026-07-01-exports-top-a-hundred-billion-in-a-month",
         "title": "A country's monthly exports top $100B for the first time on chip shipments",
         "claim": "South Korea's June exports topped $100 billion for the first time on record SK "
                  "Hynix and Samsung shipments, while ByteDance planted a $39 billion data center "
                  "in Brazil and Amazon's transatlantic cable surfaced in Ireland to feed "
                  "European AI.",
         "domain": "economics", "actor": ["sk-hynix", "samsung", "bytedance", "amazon"],
         "score": "$100B+ / $39B",
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "network-over-node"],
         "supersedes": [B + "developments/2026-06-29-a-five-hundred-eighty-five-billion-semiconductor-complex"]},
        {"id": "2026-07-01-a-county-begs-schools-to-kill-the-lights",
         "title": "A county asks schools to cut power as datacenters spike rates 25%",
         "claim": "Henrico County begged schools to kill the lights as data centers spiked its "
                  "rates 25%, while SpaceX halved Starlink prices in Memphis to placate neighbors "
                  "of xAI's Colossus.",
         "domain": "energy", "actor": ["henrico-county", "spacex", "xai"], "score": "+25% rates",
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-27-reserved-gpu-prices-raised-twenty-percent"]},
        {"id": "2026-07-01-a-humanoid-line-installed-at-an-automaker",
         "title": "An automaker installs its first humanoid production line",
         "claim": "Tesla's first Optimus humanoid line is being installed in Fremont with dozens "
                  "more planned, while UBTech's $17,650 companion robot shipped in China and "
                  "South Korea moved to drill its entire military into drone operators.",
         "domain": "robotics", "actor": ["tesla", "ubtech-robotics"], "score": "$17,650",
         "evidences": ["physical-recursion", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-06-28-a-three-hundred-dollar-wristband-teaches-robot-hands"]},
        {"id": "2026-07-01-sentences-read-from-the-brain-without-surgery",
         "title": "Sentences are read from brain recordings without surgery at 61% accuracy",
         "claim": "Meta's Brain2Qwerty v2 reads sentences from magnetoencephalography recordings "
                  "at 61% accuracy with no surgery and open code, while Neuralink threaded "
                  "electrodes through the dura without ever cutting it.",
         "domain": "biotech", "actor": ["meta", "neuralink"], "score": "61% accuracy",
         "evidences": ["intimate-interface", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-06-26-a-living-brain-imaged-through-the-skull"]},
        {"id": "2026-07-01-a-deadly-pill-made-safe-in-three-hours-on-a-laptop",
         "title": "A virtual heart turns a deadly drug into its safe twin in three hours",
         "claim": "One startup's virtual heart turned a deadly pill into its safe twin in three "
                  "hours on a laptop, a fix that once cost $6 billion, while Conception grew the "
                  "first human eggs from blood-derived stem cells.",
         "domain": "biotech", "actor": ["conception"], "score": "3 hours vs $6B",
         "evidences": ["hardware-grade-biology", "compiling-matter", "garage-scale-discovery"],
         "supersedes": [B + "developments/2026-07-01-sixty-databases-in-one-workbench"]},
        {"id": "2026-07-01-the-labor-apocalypse-keeps-missing",
         "title": "AI-heavy firms grew white-collar headcount and entry-level roles",
         "claim": "AI-heavy firms grew white-collar headcount 10.2%, with entry-level roles up "
                  "12%, and OpenAI's economist insisted AI will not make workers superfluous.",
         "domain": "economics", "actor": ["openai"], "score": "+10.2% / +12% entry-level",
         "evidences": ["work-displaced", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-06-29-a-thirteen-percent-hit-that-is-not-going-away"],
         "body": "Directly contradicts the Canaries Dashboard finding two days earlier. "
                 "Both are kept: the disagreement is the state of the evidence."},
    ],
}
