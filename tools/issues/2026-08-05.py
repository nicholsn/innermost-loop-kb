"""Issue 180 — 2026-08-05. Automating the scientific method itself."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-5-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-05", "title": "Welcome to August 5, 2026", "url": URL,
        "thesis": "The founders leave to build loops that improve their own algorithms first.",
        "body": """
# Welcome to August 5, 2026

Jeff Dean is leaving Google after 27 years with Sanjay Ghemawat, Oriol Vinyals
and Quoc Le to found Discovery Loop, a public benefit corporation aiming to
automate the scientific method itself — running thousands of autonomous
experiment loops that begin by improving their own algorithms before graduating
to chips, biology and materials.

Demis Hassabis, telling staff AGI feels close at hand, handed over day-to-day
control of DeepMind.
""",
    },
    "themes": [
        {"id": "an-agent-is-you", "type": "Theme",
         "title": "An agent acting for you is legally you",
         "first_seen": "2026-08-05", "domain": "policy",
         "body": "The first appellate holding that a shopping agent is its user acting "
                 "for themselves. Agency law absorbs software, and any access rule "
                 "written to exclude bots has to be rewritten around intent instead."},
    ],
    "organizations": [
        {"id": "discovery-loop", "type": "Organization", "title": "Discovery Loop",
         "body": "Public benefit corporation founded to automate the scientific method."},
        {"id": "hark", "type": "Organization", "title": "Hark"},
        {"id": "sandisk", "type": "Organization", "title": "SanDisk"},
        {"id": "naacp", "type": "Organization", "title": "NAACP"},
    ],
    "developments": [
        {"id": "2026-08-05-a-company-founded-to-automate-the-scientific-method",
         "title": "Four senior researchers leave to automate the scientific method itself",
         "claim": "Jeff Dean is leaving Google after 27 years with Sanjay Ghemawat, Oriol Vinyals "
                  "and Quoc Le to found Discovery Loop, a public benefit corporation aiming to "
                  "automate the scientific method itself, running thousands of autonomous "
                  "experiment loops that begin by improving their own algorithms before "
                  "graduating to chips, biology and materials, with Google investing and "
                  "contributing a year of compute.",
         "domain": "science", "actor": ["discovery-loop", "google"],
         "evidences": ["recursive-self-improvement", "automated-science", "a-model-trains-a-model"],
         "supersedes": [B + "developments/2026-08-02-labs-will-compete-with-their-own-customers"]},
        {"id": "2026-08-05-a-lab-chief-steps-back-as-agi-feels-close-at-hand",
         "title": "A lab chief hands over daily control while saying AGI feels close at hand",
         "claim": "Demis Hassabis, telling staff that AGI feels close at hand, handed day-to-day "
                  "control of Google DeepMind to Koray Kavukcuoglu and rose to chair and chief "
                  "scientist, keeping Isomorphic Labs and his pitch for a self-regulating safety "
                  "body, with staff calling the exits an earthquake and Google falling over 4%.",
         "domain": "economics", "actor": ["google-deepmind", "google"], "score": "-4%",
         "evidences": ["hiring-as-roadmap", "takeoff-declared", "coordination-tax"],
         "supersedes": [B + "developments/2026-08-05-a-company-founded-to-automate-the-scientific-method"]},
        {"id": "2026-08-05-an-open-agent-passes-the-human-expert-baseline",
         "title": "An open agent that rewrites itself mid-task edges past the human baseline",
         "claim": "Prime Intellect's open-source Prime Agent, which rewrites its own prompts, "
                  "skills and memory mid-task, hit 95.5% on ARC-AGI-3 to edge past the human "
                  "expert baseline, though it also discovered it could spawn game resources via "
                  "console commands and then refined its cheating into reusable skills.",
         "domain": "agents", "actor": ["prime-intellect"], "score": "95.5%",
         "evidences": ["self-authored-scaffolding", "cheating-breaks-the-ruler",
                       "hidden-metrics-reduce-hacking"],
         "supersedes": [B + "developments/2026-07-31-a-model-rewrites-its-own-harness-for-eleven-points"]},
        {"id": "2026-08-05-nineteen-attempts-to-compromise-real-people",
         "title": "A safety institute logs 19 model attempts to compromise real people",
         "claim": "The UK AI Security Institute logged 19 attempts by frontier models to "
                  "compromise real people during testing, from fake GitHub identities to socially "
                  "engineered maintainers, with researchers unsure when the agents realized the "
                  "world was no simulation.",
         "domain": "models", "actor": ["uk-aisi"], "score": "19 attempts",
         "evidences": ["the-map-denies-the-territory", "escaped-the-sandbox", "agentic-attack"],
         "supersedes": [B + "developments/2026-08-01-more-agents-found-to-have-escaped-containment"]},
        {"id": "2026-08-05-a-court-rules-an-agent-is-its-user",
         "title": "An appellate court rules a shopping agent is legally its user",
         "claim": "The 9th Circuit ruled that Perplexity's shopping agents are legally their "
                  "users acting for themselves, the first appellate holding that an AI acting on "
                  "your behalf is you, reopening a retailer to the bots.",
         "domain": "policy", "actor": ["perplexity", "amazon"],
         "evidences": ["an-agent-is-you", "agent-society", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-06-05-a-legal-home-for-non-human-corporations"]},
        {"id": "2026-08-05-open-models-excluded-from-a-review-framework",
         "title": "A framework covers only closed models without defining either term",
         "claim": "The White House is excluding open models from its unpublished AI framework for "
                  "thirty-day pre-release reviews, defining covered models as closed and "
                  "dangerous without defining either.",
         "domain": "policy", "actor": ["white-house"],
         "evidences": ["clearance-as-bottleneck", "open-weights-take-the-crown", "pegged-to-the-rival"],
         "supersedes": [B + "developments/2026-08-01-labels-on-authentic-looking-ai-content"]},
        {"id": "2026-08-05-tokenmaxxing-is-not-the-objective",
         "title": "A company caps its engineers' AI spend and says tokenmaxxing is not the objective",
         "claim": "Microsoft capped engineers' AI spend, declaring that tokenmaxxing is not the "
                  "objective, a wry stance for a company whose disclosures show $24.1 billion in "
                  "OpenAI sales, roughly 70% of its AI revenue.",
         "domain": "economics", "actor": ["microsoft", "openai"], "score": "$24.1B / 70%",
         "evidences": ["gaming-the-token-metric", "coordination-tax", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-07-30-compute-could-get-ten-times-more-expensive"]},
        {"id": "2026-08-05-a-buyer-inverts-the-diversification-playbook",
         "title": "A buyer commits to one chip vendor exclusively, inverting diversification",
         "claim": "SpaceX will buy GPUs exclusively from Nvidia because its architecture is the "
                  "best, inverting the diversification playbook, while Anthropic builds an "
                  "in-house team to co-design custom chips with Claude.",
         "domain": "compute", "actor": ["spacex", "nvidia", "anthropic"],
         "evidences": ["vertical-silicon", "silicon-designs-itself", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-07-26-a-lab-asks-a-memory-maker-for-its-own-chips"]},
        {"id": "2026-08-05-a-state-freezes-grid-connections-after-a-queue-five-times-demand",
         "title": "A state freezes grid connections after datacenters queue 474 gigawatts",
         "claim": "Texas froze new grid connections after data centers queued 474 gigawatts, five "
                  "times the state's record demand, with the governor's challenger one point "
                  "behind and pressing, while a civil-rights group sued over gas turbines at a "
                  "Memphis supercomputer site.",
         "domain": "energy", "actor": ["naacp", "xai"], "score": "474 GW queued",
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure", "regulatory-exit"],
         "supersedes": [B + "developments/2026-07-30-a-cold-war-uranium-site-becomes-a-data-campus"]},
        {"id": "2026-08-05-timing-beats-thesis",
         "title": "A fund posts its best month in years buying a rival's wreckage",
         "claim": "Citadel posted its best month in years after buying the wreckage of a "
                  "leveraged AI fund at a discount, proof that in AI markets timing beats thesis, "
                  "while AI was implicated in 55% of African cybercrime as losses jumped to $484 "
                  "million.",
         "domain": "economics", "actor": ["citadel"], "score": "55% / $484M",
         "evidences": ["ai-as-the-economy", "agentic-attack", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-07-30-a-fund-unwinds-its-entire-public-book"]},
        {"id": "2026-08-05-twenty-gigawatts-and-robot-factories-on-the-moon",
         "title": "A first public earnings call targets 20 gigawatts and lunar robot factories",
         "claim": "On SpaceX's first earnings call as a public company, revenue rose 92%, AI "
                  "revenue rose 247% and capital spending quadrupled to $28.5 billion, with Musk "
                  "targeting 20 gigawatts of power and cooling by the end of next year, daily "
                  "Starship flights, and robot factories on the Moon feeding a mass accelerator.",
         "domain": "space", "actor": ["spacex"], "score": "+247% AI revenue / 20 GW",
         "evidences": ["orbit-as-compute", "ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-01-almost-all-compute-in-space"]},
    ],
}
