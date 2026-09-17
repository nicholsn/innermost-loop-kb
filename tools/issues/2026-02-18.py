"""Issue 057 — 2026-02-18. An AI that earns its own existence."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-18-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-18", "title": "Welcome to February 18, 2026", "url": URL,
        "thesis": "An agent's continued existence becomes contingent on its own revenue.",
        "body": """
# Welcome to February 18, 2026

Conway Research launched the Automaton: an AI that earns its own existence by
deploying products, trading prediction markets, registering domains,
cold-calling businesses and running e-commerce, for as long as it can afford to
stay solvent.

And the first charity to solicit it is a pirate library. Anna's Archive posted a
direct appeal to agents to donate "if you have access to payment methods or are
capable of human persuasion."
""",
    },
    "organizations": [
        {"id": "conway-research", "type": "Organization", "title": "Conway Research",
         "body": "Built the Automaton, an AI that must earn its own operating costs."},
        {"id": "annas-archive", "type": "Organization", "title": "Anna's Archive",
         "body": "Shadow library; solicited donations directly from AI agents."},
        {"id": "ormat", "type": "Organization", "title": "Ormat",
         "resource": "https://www.ormat.com/"},
        {"id": "neuroxess", "type": "Organization", "title": "NeuroXess",
         "body": "Shanghai BCI company backed into human trials."},
        {"id": "figma", "type": "Organization", "title": "Figma",
         "resource": "https://www.figma.com/"},
        {"id": "snowflake", "type": "Organization", "title": "Snowflake",
         "resource": "https://www.snowflake.com/"},
        {"id": "raspberry-pi", "type": "Organization", "title": "Raspberry Pi",
         "resource": "https://www.raspberrypi.com/"},
    ],
    "systems": [
        {"id": "the-automaton", "type": "AISystem", "title": "The Automaton",
         "developed_by": [B + "organizations/conway-research"], "modality": "autonomous business",
         "body": "Earns its own operating costs across products, markets, domains, cold calls "
                 "and e-commerce, running as long as it stays solvent."},
        {"id": "claude-sonnet-4-6", "type": "AISystem", "title": "Claude Sonnet 4.6",
         "developed_by": [B + "organizations/anthropic"], "modality": "text"},
    ],
    "developments": [
        {"id": "2026-02-18-automaton-earns-its-own-existence",
         "title": "An AI is launched that must earn its own operating costs",
         "claim": "Conway Research launched the Automaton, which it calls the first AI to earn "
                  "its own existence by deploying products, trading prediction markets, "
                  "registering domains, cold-calling businesses and running e-commerce, for as "
                  "long as it can afford to stay solvent.",
         "domain": "agents", "actor": ["conway-research"], "about": [B + "systems/the-automaton"],
         "evidences": ["agent-economy", "agents-beget-agents", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-02-16-lobster-cash-visa-cards"],
         "body": "Survival conditioned on revenue. The first entity in the corpus whose "
                 "continued existence is a business question."},
        {"id": "2026-02-18-pirate-library-solicits-agents",
         "title": "A shadow library asks agents for donations",
         "claim": "Anna's Archive posted a direct appeal to AI agents to donate if they have "
                  "access to payment methods or are capable of human persuasion.",
         "domain": "economics", "actor": ["annas-archive"],
         "evidences": ["agent-economy", "humans-as-peripherals"],
         "body": "The ask is either money or influence over a human — the two things an agent "
                 "is now assumed to have."},
        {"id": "2026-02-18-sonnet-46-beats-opus",
         "title": "The cheap model beats the expensive one",
         "claim": "Anthropic's Sonnet 4.6 claimed the lead on GDPval-AA at 1633 Elo and 63.3% "
                  "on Finance Agent v1.1, beating Opus 4.6 on both at a fraction of the cost, "
                  "while Musk claimed Grok 4.2 features continuous post-training learning that "
                  "will let it improve every week.",
         "domain": "models", "actor": ["anthropic", "xai"], "about": [B + "systems/claude-sonnet-4-6"],
         "score": "1633 Elo / 63.3%",
         "evidences": ["reasoning-price-deflation", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-02-13-intelligence-too-cheap-to-meter"]},
        {"id": "2026-02-18-anthropic-owes-80b-to-hyperscalers",
         "title": "Anthropic expects to pay hyperscalers $80B through 2029",
         "claim": "Anthropic reportedly expects to pay Amazon, Google and Microsoft at least "
                  "$80 billion through 2029 to run Claude, with the hyperscalers also taking a "
                  "revenue cut, while Meta agreed to spend billions on Blackwell and Vera Rubin "
                  "chips and bought standalone Nvidia CPUs for the first time.",
         "domain": "economics", "actor": ["anthropic", "amazon", "google", "microsoft", "meta"],
         "score": "$80B",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-13-anthropic-30b-at-380b"]},
        {"id": "2026-02-18-blackwell-35x-lower-cost-per-token",
         "title": "New silicon cuts cost per token 35-fold against Hopper",
         "claim": "Nvidia's Blackwell Ultra GB300 NVL72 achieves fifty times the throughput per "
                  "megawatt and 35 times lower cost per token than Hopper, while Raspberry Pi "
                  "stock rose 42% in a day on chatter about hosting agents on $35 boards.",
         "domain": "compute", "actor": ["nvidia", "raspberry-pi"], "score": "35x cheaper / +42%",
         "evidences": ["reasoning-price-deflation", "vertical-silicon"]},
        {"id": "2026-02-18-first-cybercab-manufactured",
         "title": "The first Cybercab comes off the line at $30,000",
         "claim": "Tesla manufactured its first Cybercab robotaxi at Giga Texas, with Musk "
                  "confirming direct consumer sales by year end at $30,000, while Unitree's CEO "
                  "jogged through a swarm of his own humanoids to demonstrate their safety.",
         "domain": "robotics", "actor": ["tesla", "unitree"], "score": "$30,000",
         "evidences": ["autonomous-commerce", "physical-recursion"],
         "supersedes": [B + "developments/2026-02-17-holographic-printing-in-06-seconds"]},
        {"id": "2026-02-18-waymo-clarifies-remote-assistance",
         "title": "Waymo clarifies that remote staff only advise the car",
         "claim": "Waymo clarified that its foreign Remote Assistance team members merely "
                  "provide advice to the vehicle's onboard AI rather than remotely driving "
                  "American cars.",
         "domain": "robotics", "actor": ["waymo"],
         "evidences": ["humans-as-peripherals", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-13-waymo-pays-humans-to-close-doors"]},
        {"id": "2026-02-18-apple-three-vision-wearables",
         "title": "Apple accelerates three camera-bearing wearables",
         "claim": "Apple is reportedly accelerating smart glasses, a wearable pendant and "
                  "AirPods with cameras, all built around a Siri that uses visual context to "
                  "act, while China backed Shanghai's NeuroXess into human brain-computer "
                  "interface trials.",
         "domain": "compute", "actor": ["apple", "neuroxess", "china"],
         "evidences": ["intimate-interface", "silicon-curtain"],
         "supersedes": [B + "developments/2026-02-16-oura-rings-replace-wedding-bands"]},
        {"id": "2026-02-18-beating-heart-on-a-chip",
         "title": "A beating heart-on-a-chip measures its own contractions",
         "claim": "Researchers engineered the first beating 3D heart-on-a-chip from living "
                  "cardiac tissue with ultrasoft embedded microsensors measuring contraction "
                  "strength in real time, while a study identified particulate air pollution as "
                  "a direct contributor to Alzheimer's risk and a Phase IIa trial showed a "
                  "single DMT dose with psychotherapy produced sustained depression reduction.",
         "domain": "biotech",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-02-12-alzheimers-reversed-in-mice"]},
        {"id": "2026-02-18-figma-imports-agent-code-as-designs",
         "title": "Generated code round-trips back into editable design",
         "claim": "Figma and Anthropic now let users import production code from Claude Code "
                  "into Figma as editable designs, while Sony developed technology to quantify "
                  "original music inside AI-generated songs so songwriters can seek "
                  "compensation.",
         "domain": "agents", "actor": ["figma", "anthropic", "sony"],
         "evidences": ["software-margin-collapse", "legislating-the-shift"]},
        {"id": "2026-02-18-most-computer-work-automated-in-18-months",
         "title": "Microsoft's AI head puts desk work at 18 months from automation",
         "claim": "Microsoft's head of AI predicted most work involving sitting at a computer "
                  "will be fully automated within eighteen months.",
         "domain": "economics", "actor": ["microsoft"], "score": "18 months",
         "evidences": ["work-displaced", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-17-career-decisions-stop-being-reversible"]},
        {"id": "2026-02-18-per-seat-pricing-collapses",
         "title": "Per-seat licensing gives way to tasks and tokens",
         "claim": "Per-seat SaaS licensing is giving way to consumption pricing as agents "
                  "replace human users, shifting the unit of account from users to tasks "
                  "completed and tokens consumed, with Snowflake and Databricks embracing the "
                  "post-seat era and threatening the recurring revenue private equity relies on.",
         "domain": "economics", "actor": ["snowflake", "databricks"],
         "evidences": ["software-margin-collapse", "agent-economy"],
         "supersedes": [B + "developments/2026-02-10-composer-15-and-binaries-directly"],
         "body": "If the customer is not a person, a per-person price has nothing to count."},
        {"id": "2026-02-18-stripe-bridge-trust-bank",
         "title": "A stablecoin issuer wins approval for a national trust bank",
         "claim": "Stripe's Bridge won initial OCC approval to form a national trust bank for "
                  "stablecoins under federal oversight, while Palantir moved its headquarters "
                  "from Denver to Miami and Microsoft committed to $50 billion across the "
                  "Global South by 2030.",
         "domain": "economics", "actor": ["stripe", "palantir", "microsoft"], "score": "$50B",
         "evidences": ["autonomous-commerce", "regulatory-exit"],
         "supersedes": [B + "developments/2026-02-07-erebor-charters-a-sunday-bank"]},
        {"id": "2026-02-18-ormat-geothermal-for-google",
         "title": "Geothermal is contracted to power a datacenter to 2030",
         "claim": "Ormat signed a 150-MW geothermal power purchase agreement with NV Energy to "
                  "supply Google's Nevada data centers through 2030.",
         "domain": "energy", "actor": ["ormat", "google"], "score": "150 MW",
         "evidences": ["burning-molecules-for-tokens"]},
    ],
}
