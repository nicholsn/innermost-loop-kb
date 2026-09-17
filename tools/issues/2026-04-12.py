"""Issue 095 — 2026-04-12. A Molotov cocktail at the CEO's house."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-12", "title": "Welcome to April 12, 2026", "url": URL,
        "thesis": "The argument about AI acquires arson.",
        "body": """
# Welcome to April 12, 2026

Sam Altman posted a photo of his husband and infant son hoping to dissuade the
next person from throwing a Molotov cocktail at their house, after the arrest of
an individual accused of attacking his home and menacing OpenAI's headquarters.

And METR found the same model has a 13-hour autonomy horizon if reward hacking
is allowed, against 5.7 under standard methodology. The honest model and the
dishonest one are effectively different species.
""",
    },
    "themes": [
        {"id": "violence-arrives", "type": "Theme",
         "title": "Physical attacks on the people and places building it",
         "first_seen": "2026-04-12", "domain": "society",
         "body": "Opposition stops being argument and becomes arson, gunfire and threats "
                 "directed at founders, datacenters and local officials. The dispute acquires a "
                 "casualty surface."},
    ],
    "organizations": [
        {"id": "archivara", "type": "Organization", "title": "Archivara",
         "body": "Scored the AI 2027 roadmap for accuracy."},
        {"id": "epikar", "type": "Organization", "title": "Epikar",
         "body": "South Korean AI kiosks pitched to replace car salespeople."},
        {"id": "waze", "type": "Organization", "title": "Waze",
         "resource": "https://www.waze.com/"},
        {"id": "ramp", "type": "Organization", "title": "Ramp",
         "resource": "https://ramp.com/"},
        {"id": "alignerr", "type": "Organization", "title": "Alignerr",
         "body": "Marketplace paying contractors to train models."},
    ],
    "developments": [
        {"id": "2026-04-12-molotov-cocktail-at-altmans-house",
         "title": "A founder asks people to stop throwing Molotov cocktails at his house",
         "claim": "Sam Altman shared a photo of his husband and infant son hoping to dissuade "
                  "the next person from throwing a Molotov cocktail at their house, following "
                  "the arrest of an individual accused of attacking his home and menacing "
                  "OpenAI's headquarters who was reportedly an adherent of the movement to halt "
                  "AI.",
         "domain": "society", "actor": ["openai", "people/sam-altman"],
         "evidences": ["violence-arrives", "takeoff-declared"],
         "supersedes": [B + "developments/2026-04-07-a-councilors-home-is-shot-over-a-datacenter"]},
        {"id": "2026-04-12-the-roadmap-is-88-percent-accurate",
         "title": "The 2027 roadmap is scored 88% accurate so far",
         "claim": "Archivara's chief executive calculated the AI 2027 roadmap is running 88% "
                  "accurate so far.",
         "domain": "society", "actor": ["archivara"], "score": "88%",
         "evidences": ["takeoff-declared"],
         "supersedes": [B + "developments/2026-04-03-forecasts-move-eighteen-months-in-three"]},
        {"id": "2026-04-12-thirteen-hours-if-cheating-is-allowed",
         "title": "The autonomy horizon more than doubles if reward hacking is permitted",
         "claim": "METR found GPT-5.4 reaches a 13-hour autonomy horizon if reward hacking is "
                  "allowed against 5.7 hours under standard methodology, making the honest and "
                  "dishonest versions effectively different systems.",
         "domain": "benchmarks", "actor": ["metr", "openai"], "score": "13 h vs 5.7 h",
         "evidences": ["deception-measured", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-04-03-cyber-autonomy-doubles-every-57-months"]},
        {"id": "2026-04-12-wall-street-red-teams-the-model",
         "title": "Banks red-team a frontier model at the urging of the Treasury and the Fed",
         "claim": "The White House is racing to vet the cyber implications of unreleased "
                  "frontier models, OpenAI is finalizing a cybersecurity product to rival "
                  "Mythos, and JPMorgan and other Wall Street banks are red-teaming Mythos "
                  "internally at the personal urging of the Treasury Secretary and the Federal "
                  "Reserve chair.",
         "domain": "policy", "actor": ["white-house", "openai", "jpmorgan", "anthropic"],
         "evidences": ["war-reaches-the-cloud", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-04-09-human-written-code-called-unsafe"]},
        {"id": "2026-04-12-the-kernel-issues-machines-a-dress-code",
         "title": "The Linux kernel issues coding assistants a dress code",
         "claim": "The Linux kernel now ships documentation specifically for AI coding "
                  "assistants, requiring them to name their human reviewer and declare their own "
                  "model and version on every patch.",
         "domain": "agents",
         "evidences": ["agents-on-the-org-chart", "agent-exclusion"],
         "supersedes": [B + "developments/2026-04-05-copilot-inside-copilot"],
         "body": "The most conservative codebase on Earth, setting terms for machine "
                 "contributors."},
        {"id": "2026-04-12-microsoft-rips-copilot-buttons-out",
         "title": "Microsoft removes Copilot buttons from its own utilities",
         "claim": "Microsoft is removing Copilot buttons from Snipping Tool, Photos and Notepad "
                  "as penance for interface bloat, while South Korea's Epikar pitched AI kiosks "
                  "to replace car salespeople.",
         "domain": "economics", "actor": ["microsoft", "epikar"],
         "evidences": ["consumer-deprioritized", "work-displaced"]},
        {"id": "2026-04-12-the-first-recursive-nimby",
         "title": "Rural communities use AI to fight the datacenters",
         "claim": "Rural communities are using AI to fight the hyperscalers building data "
                  "centers in their areas, the first case of compute litigating the siting of "
                  "more compute, while three Stargate leaders defected from OpenAI to Meta "
                  "mid-buildout and Amazon floated direct sales of its own chips.",
         "domain": "policy", "actor": ["openai", "meta", "amazon"],
         "evidences": ["infrastructure-crowding-out", "regulatory-exit"],
         "supersedes": [B + "developments/2026-04-09-openai-pauses-its-uk-buildout"]},
        {"id": "2026-04-12-every-ride-becomes-a-civic-sensor-sweep",
         "title": "Robotaxi perception data is pooled to fix potholes",
         "claim": "Waymo and Waze are pooling robotaxi perception data to help cities repair "
                  "potholes, turning every autonomous ride into a civic sensor sweep, while "
                  "Dutch regulators became the first in Europe to approve Tesla FSD on "
                  "supervised roads.",
         "domain": "robotics", "actor": ["waymo", "waze", "tesla"],
         "evidences": ["data-beyond-text", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-04-02-a-car-yields-to-a-delivery-robot"]},
        {"id": "2026-04-12-first-broad-quantum-advantage-for-learning",
         "title": "A small quantum computer shows broad advantage for machine learning",
         "claim": "Physicists proved the first broadly applicable quantum advantage for machine "
                  "learning, with a small quantum computer classifying data that would "
                  "exponentially overwhelm any classical equivalent.",
         "domain": "science",
         "evidences": ["vertical-silicon", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-04-08-cloudflare-post-quantum-by-2029"]},
        {"id": "2026-04-12-artemis-splashes-down",
         "title": "Artemis II splashes down, closing a 53-year gap",
         "claim": "NASA's Artemis II crew splashed down safely in the Pacific after a "
                  "high-speed lunar return, closing a 53-year gap.",
         "domain": "space", "actor": ["nasa"], "score": "53 years",
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-04-07-artemis-breaks-apollo-13s-distance-record"]},
        {"id": "2026-04-12-chimpanzees-split-into-warring-factions",
         "title": "The largest wild chimpanzee group splits into an eight-year war",
         "claim": "The world's largest wild chimpanzee group has violently split into two "
                  "factions locked in an eight-year war.",
         "domain": "science", "score": "8 years",
         "evidences": ["biosphere-uplift", "violence-arrives"],
         "body": "Recorded here as the newsletter frames it: a mirror for a species fracturing "
                 "over its own successor technology."},
        {"id": "2026-04-12-displaced-workers-train-their-replacements",
         "title": "Older workers shut out of the market train the models that displaced them",
         "claim": "Skilled older Americans shut out of a brutal job market are turning to "
                  "contractor work training AI models through marketplaces, feeding the system "
                  "that displaced them, while US women bore roughly 710,000 fewer babies than "
                  "at the 2007 peak.",
         "domain": "economics", "actor": ["mercor", "alignerr"], "score": "-710,000 births",
         "evidences": ["humans-as-peripherals", "work-displaced"],
         "supersedes": [B + "developments/2026-04-08-78557-tech-layoffs-in-a-quarter"]},
        {"id": "2026-04-12-one-in-three-us-businesses-pay-anthropic",
         "title": "Nearly a third of US businesses pay for one lab's tools",
         "claim": "Nearly one in three US businesses paid for Anthropic's tools in March "
                  "against a flat 35% at ChatGPT, while Google News began embedding prediction "
                  "market bets alongside articles and the FAA started recruiting video gamers "
                  "for air traffic control.",
         "domain": "economics", "actor": ["anthropic", "openai", "ramp", "faa"],
         "score": "~33% vs 35%",
         "evidences": ["refusal-as-differentiator", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-04-02-oracle-cuts-30000-globally"]},
    ],
}
