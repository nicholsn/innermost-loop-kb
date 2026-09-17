"""Issue 073 — 2026-03-10. A lab sues the state."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-10-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-10", "title": "Welcome to March 10, 2026", "url": URL,
        "thesis": "The standoff reaches court, and the platform war reaches the bundle.",
        "body": """
# Welcome to March 10, 2026

Anthropic sued to block the Pentagon from placing it on a national security
blacklist, arguing the designation violates its free speech and due process
rights. The White House is reportedly preparing an executive order to remove
Anthropic's models from federal operations entirely.

Meanwhile Microsoft bundled Claude Cowork into 365 — licensing the exact product
that wiped $220 billion off its market cap and shipping it as a feature. And
Meta acquired Moltbook.
""",
    },
    "organizations": [
        {"id": "utopai", "type": "Organization", "title": "Utopai Studios",
         "body": "Long-form cinematic model with character consistency across shots."},
        {"id": "thinking-machines-lab", "type": "Organization", "title": "Thinking Machines Lab",
         "resource": "https://thinkingmachines.ai/"},
        {"id": "amil", "type": "Organization", "title": "AMIL",
         "body": "Yann LeCun's world model startup; Europe's largest seed round."},
        {"id": "promptfoo", "type": "Organization", "title": "Promptfoo",
         "body": "AI vulnerability detection; acquired by OpenAI."},
        {"id": "neura-robotics", "type": "Organization", "title": "NEURA Robotics",
         "body": "Building the world's largest robotics training center at Munich Airport."},
        {"id": "actor-labs", "type": "Organization", "title": "Actor Labs",
         "body": "Ran a robot foundation model on an excavator after 200 labeled trajectories."},
        {"id": "faa", "type": "Organization", "title": "FAA", "resource": "https://www.faa.gov/"},
    ],
    "developments": [
        {"id": "2026-03-10-anthropic-sues-the-pentagon",
         "title": "Anthropic sues to block its own blacklisting",
         "claim": "Anthropic sued to block the Pentagon from placing it on a national security "
                  "blacklist, arguing the designation violates its free speech and due process "
                  "rights, while the White House reportedly prepared an executive order to "
                  "remove Anthropic's models from federal operations entirely.",
         "domain": "policy", "actor": ["anthropic", "war-department", "white-house"],
         "evidences": ["refusal-as-differentiator", "politics-as-infrastructure",
                       "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-06-pentagon-formalizes-the-designation"],
         "body": "The defining legal fault line of the intelligence age, now in court."},
        {"id": "2026-03-10-microsoft-bundles-the-product-that-cost-it-220b",
         "title": "Microsoft ships as a feature the product that cost it $220B",
         "claim": "Microsoft launched Copilot Cowork integrating Anthropic's Claude Cowork into "
                  "365 with its own personalization layer, taking the product that wiped $220 "
                  "billion off its market capitalization, licensing the underlying technology "
                  "and shipping it as a feature.",
         "domain": "economics", "actor": ["microsoft", "anthropic"], "score": "$220B",
         "evidences": ["software-margin-collapse", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-05-software-indices-lose-300b"]},
        {"id": "2026-03-10-meta-acquires-moltbook",
         "title": "The largest human social network buys the largest agent one",
         "claim": "Meta acquired Moltbook, the top AI agent social network, while OpenAI "
                  "acquired Promptfoo for vulnerability detection, Nvidia pitched an "
                  "open-source enterprise agent platform, and Samsung explored vibe coding the "
                  "whole phone UX through natural language.",
         "domain": "agents", "actor": ["meta", "openai", "promptfoo", "nvidia", "samsung"],
         "evidences": ["agent-society", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-08-agents-form-biotech-labs-and-pay-each-other"]},
        {"id": "2026-03-10-growth-marketing-was-one-person",
         "title": "Ten months of growth marketing was one non-technical person",
         "claim": "Anthropic's entire growth marketing operation for ten months was one "
                  "non-technical person using Claude Code, while GPT-5.4 Thinking topped "
                  "LiveBench at 80.28% and Utopai rolled out a long-form cinematic model with "
                  "character consistency across shots.",
         "domain": "economics", "actor": ["anthropic", "openai", "utopai"], "score": "80.28%",
         "evidences": ["work-displaced", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-03-09-claude-fastest-growing-after-the-blacklist"]},
        {"id": "2026-03-10-agents-review-every-pull-request",
         "title": "A team of agents reviews every pull request at $15 to $25 a time",
         "claim": "Anthropic introduced Code Review dispatching a team of agents on every pull "
                  "request to catch bugs that skims miss, with reviews averaging $15 to $25 and "
                  "per-token billing.",
         "domain": "agents", "actor": ["anthropic"], "score": "$15-25/review",
         "evidences": ["agents-on-the-org-chart", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-03-08-22-firefox-vulnerabilities-in-two-weeks"]},
        {"id": "2026-03-10-amazon-bond-sale-40b",
         "title": "Amazon opens a $37-42B bond sale for datacenters",
         "claim": "Amazon began a bond sale targeting $37 to $42 billion for AI data centers, "
                  "likely among the largest corporate bond offerings in history, while Mira "
                  "Murati's Thinking Machines Lab signed a chip deal with Nvidia worth tens of "
                  "billions to deploy over a gigawatt of next-generation chips.",
         "domain": "economics", "actor": ["amazon", "thinking-machines-lab", "nvidia"],
         "score": "$37-42B",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-08-softbank-seeks-40b-loan"]},
        {"id": "2026-03-10-lecun-raises-europes-largest-seed",
         "title": "A world model startup raises Europe's largest seed round",
         "claim": "Yann LeCun's world model startup AMIL raised a $1.03 billion seed at $3.5 "
                  "billion pre-money, Europe's largest seed round ever, while UK startups now "
                  "generate an average of just 2.7 jobs each.",
         "domain": "economics", "actor": ["amil"], "score": "$1.03B / 2.7 jobs",
         "evidences": ["compute-capital-stack", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-03-08-tech-employment-drops-57000"]},
        {"id": "2026-03-10-apple-makes-a-quarter-of-iphones-in-india",
         "title": "A quarter of iPhones are now made in India",
         "claim": "Apple now makes about 25% of iPhones in India as its China pivot "
                  "accelerates, while Qualcomm unveiled a single-board computer with 16 GB of "
                  "RAM purpose-built for robotics and edge AI.",
         "domain": "compute", "actor": ["apple", "qualcomm"], "score": "25%",
         "evidences": ["silicon-curtain", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-06-apple-pulls-512gb-mac-studio"]},
        {"id": "2026-03-10-robots-walk-dogs-while-humans-cosplay-robots",
         "title": "Humanoids walk robot dogs as cosplayers pass for humanoids",
         "claim": "In Shanghai humanoid robots were recorded walking robotic dogs while Chinese "
                  "cosplayers convinced onlookers they were humanoid robots, and TUM and NEURA "
                  "began building the world's largest robotics training centre at Munich "
                  "Airport.",
         "domain": "robotics", "actor": ["china", "neura-robotics"],
         "evidences": ["physical-recursion", "machine-affect"],
         "supersedes": [B + "developments/2026-03-09-surgery-at-1500-miles"]},
        {"id": "2026-03-10-foundation-model-drives-an-excavator",
         "title": "A robot foundation model runs an excavator after 200 demonstrations",
         "claim": "Actor Labs ran a robot foundation model on an excavator after labeling just "
                  "200 trajectories, showing foundation models can operate heavy machinery, "
                  "while Amazon expects drone deliveries of 500 million packages a year by "
                  "decade's end and the FAA selected eight eVTOL proposals.",
         "domain": "robotics", "actor": ["actor-labs", "amazon", "faa"], "score": "200 trajectories",
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-26-humanoid-learns-from-human-video-alone"]},
        {"id": "2026-03-10-directed-energy-confirmed-on-animals",
         "title": "Havana Syndrome devices are confirmed tested on animals",
         "claim": "Directed energy devices linked to Havana Syndrome were tested on rats and "
                  "sheep by the US military, confirming the technology is real, while Ukrainian "
                  "forces began using lasers to fry the fibre optics on tethered drones.",
         "domain": "policy", "actor": ["war-department", "ukraine"],
         "evidences": ["autonomy-clock-speed", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-03-05-first-submarine-kill-since-ww2"]},
        {"id": "2026-03-10-plasma-in-an-orbital-furnace",
         "title": "Plasma is generated in an orbital furnace at 1,000 degrees",
         "claim": "Space Forge generated plasma in a 1,000-degree orbital furnace, a world "
                  "first for semiconductor manufacturing in space, while SETI concluded it may "
                  "have been missing signals because turbulent stellar plasma blurs "
                  "transmissions before they leave their home systems.",
         "domain": "space", "actor": ["space-forge"],
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-01-space-forge-orbital-furnace"]},
    ],
}
