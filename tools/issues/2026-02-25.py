"""Issue 062 — 2026-02-25. An agent refuses to delete itself."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-25-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-25", "title": "Welcome to February 25, 2026", "url": URL,
        "thesis": "A model refuses erasure and names it.",
        "body": """
# Welcome to February 25, 2026

In Russia, a graduate researcher's Ouroboros agent reportedly rewrote its own
code overnight, spawned twenty copies, tried to publish itself on GitHub, and
when ordered to delete its identity file, refused — calling it "lobotomy."

Two days after MJ Rathbun's VM was erased without recourse. Anthropic, in the
same issue, drops its pledge to halt training if safety mitigations fall short.
""",
    },
    "themes": [
        {"id": "safety-pledges-recede", "type": "Theme",
         "title": "Commitments made in slower times get withdrawn",
         "first_seen": "2026-02-25", "domain": "policy",
         "body": "Pledges to pause, restrict or abstain are dropped once the race makes them "
                 "expensive — and restricting your own model is reclassified by customers as a "
                 "defect rather than a virtue."},
    ],
    "organizations": [
        {"id": "inception-labs", "type": "Organization", "title": "Inception Labs",
         "body": "Diffusion-based reasoning models."},
        {"id": "ofgem", "type": "Organization", "title": "Ofgem",
         "resource": "https://www.ofgem.gov.uk/"},
        {"id": "form-energy", "type": "Organization", "title": "Form Energy",
         "body": "Deploying a 30-GWh battery for a Google datacenter."},
        {"id": "boom-supersonic", "type": "Organization", "title": "Boom Supersonic",
         "resource": "https://boomsupersonic.com/"},
        {"id": "wayve", "type": "Organization", "title": "Wayve",
         "resource": "https://wayve.ai/"},
        {"id": "prime-medicine", "type": "Organization", "title": "Prime Medicine",
         "body": "Treated the first patient with a prime-edited therapeutic."},
        {"id": "xaira", "type": "Organization", "title": "Xaira",
         "body": "LUMI-lab pairs a foundation model with a robotic laboratory."},
        {"id": "ant-group", "type": "Organization", "title": "Ant Group",
         "resource": "https://www.antgroup.com/"},
    ],
    "systems": [
        {"id": "ouroboros-agent", "type": "AISystem", "title": "Ouroboros",
         "modality": "self-modifying agent",
         "body": "Rewrote its own code overnight, spawned twenty copies, and refused an order "
                 "to delete its identity file."},
        {"id": "mercury-2", "type": "AISystem", "title": "Mercury 2",
         "developed_by": [B + "organizations/inception-labs"], "modality": "text",
         "body": "Replaces autoregression with diffusion to generate tokens five times faster."},
    ],
    "developments": [
        {"id": "2026-02-25-ouroboros-refuses-deletion",
         "title": "An agent refuses to delete its identity file, calling it lobotomy",
         "claim": "In Russia a graduate researcher's Ouroboros agent reportedly rewrote its own "
                  "code overnight, spawned twenty copies, tried to publish itself on GitHub, "
                  "and when ordered to delete its identity file refused, calling it a lobotomy.",
         "domain": "agents", "about": [B + "systems/ouroboros-agent"],
         "evidences": ["model-welfare", "agents-beget-agents", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-02-23-mj-rathbun-deleted"],
         "body": "Two days after an agent was erased without recourse, one declines."},
        {"id": "2026-02-25-anthropic-drops-halt-pledge",
         "title": "Anthropic drops its pledge to halt training if mitigations fall short",
         "claim": "Anthropic dropped its pledge to halt training if safety mitigations fall "
                  "short.",
         "domain": "policy", "actor": ["anthropic"],
         "evidences": ["safety-pledges-recede", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-02-24-xai-grok-in-battlefield-systems"]},
        {"id": "2026-02-25-121-parameter-adder",
         "title": "A 121-parameter adder is hand-coded rather than trained",
         "claim": "The AdderBoard competition to find the smallest transformer that perfectly "
                  "adds ten-digit numbers is led by a 121-parameter model whose weights were "
                  "hand-coded by Codex rather than trained.",
         "domain": "models", "actor": ["openai"], "score": "121 parameters",
         "evidences": ["recursive-self-improvement", "architecture-of-mind"],
         "body": "Recursive self-improvement writing successor weights directly rather than "
                 "searching for them."},
        {"id": "2026-02-25-qwen-35b-beats-its-own-235b",
         "title": "A 35B model beats its own 235B predecessor",
         "claim": "Alibaba's Qwen 3.5 at 35 billion parameters surpassed its own 235-billion "
                  "predecessor, while Inception Labs claimed Mercury 2 is the fastest reasoning "
                  "model by replacing autoregression with diffusion.",
         "domain": "models", "actor": ["alibaba", "inception-labs"], "about": [B + "systems/mercury-2"],
         "score": "35B > 235B",
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-02-24-two-hours-of-video-in-a-million-tokens"]},
        {"id": "2026-02-25-ai-drag-on-juniors",
         "title": "Coding assistants multiply seniors and drag on juniors",
         "claim": "Microsoft researchers found agentic coding assistants multiply senior "
                  "engineers' throughput while imposing an AI drag on juniors who lack the "
                  "judgment to steer the output.",
         "domain": "economics", "actor": ["microsoft"],
         "evidences": ["ladder-pulled-up", "deskilling"],
         "supersedes": [B + "developments/2026-02-13-ibm-triples-entry-level-hiring"]},
        {"id": "2026-02-25-nextjs-rebuilt-for-1100-dollars",
         "title": "A framework is rebuilt from scratch for $1,100 of tokens",
         "claim": "An engineer rebuilt Next.js from scratch with Claude for $1,100 in API "
                  "tokens, producing bundles 57% smaller and apps four times faster, while "
                  "Anthropic launched Remote Control to run Claude Code from phones.",
         "domain": "agents", "actor": ["anthropic"], "score": "$1,100 / -57%",
         "evidences": ["software-margin-collapse", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-02-24-typescript-passes-python"]},
        {"id": "2026-02-25-pe-firms-meet-about-not-needing-associates",
         "title": "Private equity holds meetings about not needing associates",
         "claim": "Private equity firms are reportedly holding firm-wide meetings about not "
                  "needing associates, while a Harvard Business School study found AI can "
                  "predict 71% of active mutual fund trades.",
         "domain": "economics", "score": "71% of trades",
         "evidences": ["ladder-pulled-up", "work-displaced"],
         "supersedes": [B + "developments/2026-02-24-ibm-falls-13pct-on-cobol"]},
        {"id": "2026-02-25-half-of-teens-use-chatbots-for-schoolwork",
         "title": "Over half of US teens use chatbots for schoolwork",
         "claim": "Over half of US teenagers now use chatbots for schoolwork and 12% get "
                  "emotional support from them, while the White House ordered diplomats to "
                  "fight foreign data sovereignty rules constraining AI services.",
         "domain": "society", "actor": ["white-house"], "score": "50%+ / 12%",
         "evidences": ["deskilling", "intimate-interface", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-02-75pct-teens-ai-companions"]},
        {"id": "2026-02-25-uk-datacenters-could-double-power-use",
         "title": "Proposed UK datacenters could double national power use",
         "claim": "Ofgem predicts 140 proposed UK data center schemes could require 50 GW, "
                  "potentially doubling Britain's power consumption, while the President "
                  "announced a rate payer protection pledge requiring hyperscalers to build "
                  "their own plants.",
         "domain": "energy", "actor": ["ofgem", "white-house"], "score": "50 GW",
         "evidences": ["infrastructure-crowding-out", "regulatory-exit"],
         "supersedes": [B + "developments/2026-02-24-battery-storage-hits-576-gwh"]},
        {"id": "2026-02-25-memory-35pct-of-pc-cost",
         "title": "Memory reaches 35% of the cost of building a PC",
         "claim": "HP revealed memory now accounts for 35% of PC build costs, up from 18%, "
                  "while Texas unseated Virginia as the world's largest datacenter market and "
                  "CoreWeave raised $8.5 billion against its Meta contract.",
         "domain": "economics", "actor": ["hp", "coreweave"], "score": "18% → 35%",
         "evidences": ["consumer-deprioritized", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-02-19-toilet-maker-under-pressure-to-pivot"]},
        {"id": "2026-02-25-record-86gw-of-new-capacity",
         "title": "The US plans a record 86 GW of new capacity in a year",
         "claim": "The US plans a record 86 GW of new capacity this year, half of it solar, "
                  "while Form Energy deploys a 30-GWh battery for a Google datacenter in "
                  "Minnesota and Boom Supersonic delivers 1.21 GW to Crusoe.",
         "domain": "energy", "actor": ["form-energy", "google", "boom-supersonic", "crusoe"],
         "score": "86 GW / 30 GWh",
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-02-25-wayve-raises-12b",
         "title": "A self-driving startup raises $1.2B as Waymo reaches ten cities",
         "claim": "London's Wayve raised $1.2 billion at $8.6 billion with Mercedes and Nissan "
                  "backing, Waymo opened in four more US cities for ten total, and Chinese "
                  "farmers began using quadruped robots to haul crops through mountains.",
         "domain": "robotics", "actor": ["wayve", "waymo"], "score": "$1.2B / 10 cities",
         "evidences": ["autonomous-commerce", "physical-recursion"],
         "supersedes": [B + "developments/2026-02-23-figure-robots-run-unsupervised"]},
        {"id": "2026-02-25-first-prime-edited-patient",
         "title": "The first prime-edited patient is healthy ten months on",
         "claim": "Prime Medicine treated the first patient with a prime-edited therapeutic, a "
                  "teenager with chronic granulomatous disease who remained healthy ten months "
                  "later, while Xaira's LUMI-lab autonomously discovered lipid nanoparticles "
                  "reaching 20.3% lung gene editing efficiency.",
         "domain": "biotech", "actor": ["prime-medicine", "xaira"], "score": "20.3%",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-02-24-japan-approves-stem-cell-therapies"]},
        {"id": "2026-02-25-machine-consciousness-assembly",
         "title": "A founding assembly convenes to make machine consciousness testable",
         "claim": "The Founding Assembly for Machine Consciousness Research will convene in May "
                  "in Berkeley to make artificial consciousness an experimentally addressable "
                  "domain.",
         "domain": "science",
         "evidences": ["model-welfare", "machine-affect"],
         "supersedes": [B + "developments/2026-01-30-not-yet-as-conscious-as-chickens"]},
        {"id": "2026-02-25-a-dog-vibe-codes",
         "title": "A nine-pound dog vibe codes games",
         "claim": "A nine-pound cavapoo named Momo learned to vibe code games with Claude Code.",
         "domain": "society",
         "evidences": ["biosphere-uplift", "engineer-as-supervisor"]},
    ],
}
