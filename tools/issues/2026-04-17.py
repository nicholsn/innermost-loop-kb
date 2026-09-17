"""Issue 098 — 2026-04-17. Dead companies mined for their Slack archives."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-17-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-17", "title": "Welcome to April 17, 2026", "url": URL,
        "thesis": "Failed companies are liquidated for their conversations.",
        "body": """
# Welcome to April 17, 2026

Defunct startups are being liquidated for their Slack archives, ticket queues
and email threads as premium training data — reincarnating failed companies as
weights.

And nearly a third of Anthropic staff expect Mythos to replace entry-level
engineers and researchers within three months. A private poll doubling as a
leading indicator.
""",
    },
    "organizations": [
        {"id": "sabi", "type": "Organization", "title": "Sabi",
         "body": "Developing a thought-to-text EEG headpiece reading internal speech."},
        {"id": "snap", "type": "Organization", "title": "Snap",
         "resource": "https://snap.com/"},
        {"id": "nist", "type": "Organization", "title": "NIST",
         "resource": "https://www.nist.gov/"},
    ],
    "developments": [
        {"id": "2026-04-17-dead-companies-mined-for-training-data",
         "title": "Defunct startups are liquidated for their Slack archives",
         "claim": "Defunct startups are now being liquidated for their chat archives, ticket "
                  "queues and email threads as premium training data, reincarnating failed "
                  "companies as weights.",
         "domain": "economics",
         "evidences": ["data-beyond-text", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-04-16-a-shoe-company-becomes-a-gpu-cloud"]},
        {"id": "2026-04-17-a-third-expect-entry-level-replaced-in-three-months",
         "title": "A third of staff expect the model to replace entry-level roles by summer",
         "claim": "Nearly a third of Anthropic staff expect Mythos to replace entry-level "
                  "engineers and researchers within three months, in a private poll doubling as "
                  "a public leading indicator, while the White House budget office is setting up "
                  "protections to route Mythos into major federal agencies in the coming weeks.",
         "domain": "economics", "actor": ["anthropic", "white-house"], "score": "~33% / 3 months",
         "evidences": ["ladder-pulled-up", "work-displaced", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-04-16-agencies-sidestep-the-ban"]},
        {"id": "2026-04-17-opus-47-triangulates-an-unreleased-frontier",
         "title": "A point release lands midway to a model the public cannot use",
         "claim": "Anthropic released Claude Opus 4.7 as a notable improvement at the midpoint "
                  "between Opus 4.6 and the not-yet-public Mythos Preview, while OpenAI unveiled "
                  "a frontier reasoning model built for biology, drug discovery and protein "
                  "engineering.",
         "domain": "models", "actor": ["anthropic", "openai"],
         "evidences": ["spiky-frontier", "automated-science"],
         "supersedes": [B + "developments/2026-04-16-users-notice-the-rationing"]},
        {"id": "2026-04-17-cve-reports-up-263-percent",
         "title": "Vulnerability reports rise 263% and the registry restructures",
         "claim": "NIST is restructuring its vulnerability handling after AI-driven submissions "
                  "drove a 263% spike in reports from 2020 to 2025, triaging down to "
                  "known-exploited and federally relevant bugs.",
         "domain": "policy", "actor": ["nist"], "score": "+263%",
         "evidences": ["coordination-tax", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-04-16-mythos-cracks-a-thirty-two-step-attack"]},
        {"id": "2026-04-17-google-returns-to-the-pentagon",
         "title": "Google is in talks to put Gemini in classified environments",
         "claim": "Google is reportedly in talks with the Pentagon to deploy Gemini in "
                  "classified environments, rebuilding military ties it once pointedly severed, "
                  "while Boston Dynamics' Spot began running on DeepMind's embodied reasoning "
                  "model.",
         "domain": "policy", "actor": ["google", "war-department", "boston-dynamics"],
         "evidences": ["safety-pledges-recede", "physical-recursion"],
         "supersedes": [B + "developments/2026-04-16-both-sword-and-shield-from-one-forge"]},
        {"id": "2026-04-17-codex-operates-your-computer-alongside-you",
         "title": "A coding tool is promoted from autocomplete to coworker",
         "claim": "OpenAI answered a rival's desktop agent with a Codex update that operates "
                  "the user's computer alongside them and remembers their preferences.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["engineer-as-supervisor", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-04-13-ai-fuzzing-enters-the-kernel"]},
        {"id": "2026-04-17-cerebras-files-at-35b-with-warrants",
         "title": "A chipmaker files to list with warrants that scale with its customer's spend",
         "claim": "Cerebras is filing to go public above a $35 billion valuation backed by a $20 "
                  "billion three-year compute deal with OpenAI that also grants OpenAI warrants "
                  "scaling with spend, collapsing the line between customer and owner, while "
                  "TSMC expects over 30% revenue growth this year.",
         "domain": "economics", "actor": ["cerebras", "openai", "tsmc"], "score": "$35B / $20B",
         "evidences": ["compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2026-04-16-terafab-suppliers-told-to-move-at-light-speed"]},
        {"id": "2026-04-17-xai-becomes-a-cloud-provider",
         "title": "A model lab becomes a cloud provider for its competitors",
         "claim": "xAI is becoming a cloud provider, with Cursor reportedly training its next "
                  "coding model on tens of thousands of its GPUs.",
         "domain": "economics", "actor": ["xai", "cursor"],
         "evidences": ["compute-capital-stack", "coordination-tax"]},
        {"id": "2026-04-17-smell-becomes-a-software-call",
         "title": "Artificial smells are induced by focused ultrasound",
         "claim": "Researchers induced artificial smells using 300-kHz focused ultrasound aimed "
                  "at the olfactory bulb with no cartridges required, making olfaction a "
                  "software call, while a California startup is developing a thought-to-text "
                  "headpiece that reads internal speech.",
         "domain": "science", "actor": ["sabi"], "score": "300 kHz",
         "evidences": ["intimate-interface", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-04-13-a-genetic-combination-lock"]},
        {"id": "2026-04-17-a-wireless-on-button-for-biology",
         "title": "A gene switch is made responsive to electromagnetic fields",
         "claim": "South Korean researchers uncovered a remotely controlled in vivo gene switch "
                  "responsive to electromagnetic fields, giving biology a wireless on-button.",
         "domain": "biotech",
         "evidences": ["hardware-grade-biology", "compiling-matter"]},
        {"id": "2026-04-17-whale-codas-resemble-human-vowels",
         "title": "Sperm whale calls are found to pattern like human vowels",
         "claim": "Project CETI found sperm whale codas resemble human vowels acoustically and "
                  "pattern like them linguistically, one of the closest parallels to human "
                  "phonology in any animal system.",
         "domain": "science", "actor": ["project-ceti"],
         "evidences": ["biosphere-uplift", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-04-13-robotic-decoys-teach-birds-to-be-birds"],
         "body": "Our first uplift candidate was fluent all along."},
        {"id": "2026-04-17-capex-passes-apollo-and-the-marshall-plan",
         "title": "Hyperscaler capex passes Apollo, the Interstate and the Marshall Plan combined",
         "claim": "Hyperscaler capital expenditure has surpassed the inflation-adjusted cost of "
                  "the Apollo Program, the Interstate Highway System and the Marshall Plan at "
                  "the equivalent project age, making data centers America's largest peacetime "
                  "build, while Alphabet stands to gain $100 billion from the SpaceX listing.",
         "domain": "economics", "actor": ["alphabet", "spacex"], "score": "$100B windfall",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-04-09-a-cashflow-model-prices-nvidia-at-22-trillion"]},
        {"id": "2026-04-17-britain-asks-households-to-use-more-power",
         "title": "Britain asks households to consume more during renewable peaks",
         "claim": "The UK is asking households to run dishwashers and charge vehicles when wind "
                  "and solar overshoot demand, inverting decades of conservation rhetoric into "
                  "abundance choreography, while Taiwan's market capitalization crossed $4 "
                  "trillion and overtook the United Kingdom's.",
         "domain": "energy", "actor": ["uk-govt"], "score": "$4T",
         "evidences": ["burning-molecules-for-tokens", "silicon-curtain"],
         "supersedes": [B + "developments/2026-04-09-a-wind-turbine-inside-a-coal-mine"]},
        {"id": "2026-04-17-a-special-economic-zone-under-us-common-law",
         "title": "A 4,000-acre zone in the Philippines runs under US common law",
         "claim": "The US established a first-of-its-kind 4,000-acre high-tech manufacturing "
                  "special economic zone on Luzon with diplomatic immunity and US common law, "
                  "aimed at China-proof automated supply chains, while Snap cut 16% of its "
                  "workforce to chase AI margins.",
         "domain": "policy", "actor": ["snap"], "score": "4,000 acres / -16%",
         "evidences": ["regulatory-exit", "silicon-curtain"],
         "supersedes": [B + "developments/2026-04-16-a-shoe-company-becomes-a-gpu-cloud"]},
        {"id": "2026-04-17-doomers-playing-with-fire",
         "title": "A policy chief says opponents are playing with fire",
         "claim": "After the attacks on Sam Altman's house, OpenAI's policy chief warned that "
                  "AI doomers are playing with fire, while the White House vowed to investigate "
                  "ten US scientists, engineers and military leaders recently gone missing or "
                  "found dead.",
         "domain": "society", "actor": ["openai", "white-house"],
         "evidences": ["violence-arrives", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-04-13-a-second-attack-on-altmans-home"]},
    ],
}
