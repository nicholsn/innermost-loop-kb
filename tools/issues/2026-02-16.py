"""Issue 055 — 2026-02-16. Original physics."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-16-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-16", "title": "Welcome to February 16, 2026", "url": URL,
        "thesis": "A model conjectures a physical result and then proves it.",
        "body": """
# Welcome to February 16, 2026

GPT-5.2 Pro conjectured a new formula for gluon scattering amplitudes, and a
scaffolded version spent twelve hours producing a formal proof. Andy Strominger
reportedly called it the first time he had seen AI solve a problem in his kind
of physics that might not have been solvable by humans.

A Berkeley researcher told his coding agent to cut its own cost by 99%. It
watched its own logs overnight, edited its own code, and delivered 98% across
nine changes no human wrote.
""",
    },
    "organizations": [
        {"id": "codepath", "type": "Organization", "title": "CodePath",
         "body": "CS education nonprofit partnering with Anthropic."},
        {"id": "airbnb", "type": "Organization", "title": "Airbnb",
         "resource": "https://www.airbnb.com/"},
        {"id": "helion", "type": "Organization", "title": "Helion",
         "resource": "https://www.helionenergy.com/"},
        {"id": "centivax", "type": "Organization", "title": "Centivax",
         "body": "Universal flu vaccine developer."},
        {"id": "oura", "type": "Organization", "title": "Oura",
         "resource": "https://ouraring.com/"},
        {"id": "nonhuman-rights", "type": "Organization", "title": "Nonhuman Rights Project",
         "body": "Litigates for legal personhood of nonhuman animals."},
    ],
    "people": [
        {"id": "andy-strominger", "type": "Person", "title": "Andy Strominger",
         "name": "Andy Strominger", "body": "Theoretical physicist."},
    ],
    "developments": [
        {"id": "2026-02-16-gluon-amplitude-conjectured-and-proved",
         "title": "A model conjectures a gluon formula and then proves it",
         "claim": "OpenAI used GPT-5.2 Pro to conjecture a new formula for gluon scattering "
                  "amplitudes, then had a scaffolded version spend twelve hours producing a "
                  "formal proof, with Andy Strominger reportedly calling it the first time he "
                  "had seen AI solve a problem in his kind of physics that might not have been "
                  "solvable by humans.",
         "domain": "science", "actor": ["openai", "people/andy-strominger"], "score": "12 hours",
         "evidences": ["automated-science", "root-node-problems", "discovery-as-process"],
         "supersedes": [B + "developments/2026-02-13-gemini-deep-think-sweeps"],
         "body": "Conjecture and proof in one run — the two halves of doing physics, not just "
                 "the second."},
        {"id": "2026-02-16-six-of-ten-first-proof",
         "title": "A lab claims six of ten confidential research problems",
         "claim": "OpenAI believes it has solved at least six of ten research-level problems in "
                  "the First Proof challenge, whose solutions were kept confidential, while the "
                  "AI 2027 authors graded 2025 progress at nearly 65% of their predicted pace, "
                  "putting full software automation as early as late 2027.",
         "domain": "benchmarks", "actor": ["openai"], "score": "6/10 / 65% of pace",
         "evidences": ["automated-science", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-13-bio-anchors-underestimated-algorithms"]},
        {"id": "2026-02-16-agent-cuts-its-own-cost-98pct",
         "title": "An agent cuts its own cost by 98% overnight",
         "claim": "A Berkeley researcher told his coding agent to cut its own cost by 99%, and "
                  "it ran overnight watching its own logs, editing its own code and rerunning "
                  "until metrics dropped, delivering a 98% cut across nine changes no human "
                  "wrote.",
         "domain": "agents", "score": "-98%",
         "evidences": ["recursive-self-improvement", "machine-introspection"],
         "supersedes": [B + "developments/2026-02-13-spotify-devs-have-not-written-code-since-december"]},
        {"id": "2026-02-16-lobster-cash-visa-cards",
         "title": "Agents get Visa cards and stablecoin wallets",
         "claim": "Lobster.cash launched to give agents their own Visa cards and stablecoin "
                  "wallets, granting financial autonomy without requiring them to promote "
                  "altcoins, while OpenClaw's creator Peter Steinberger joined OpenAI.",
         "domain": "economics", "actor": ["openai"],
         "evidences": ["agent-economy", "agents-beget-agents"],
         "supersedes": [B + "developments/2026-02-13-agent-spawns-and-funds-a-child"]},
        {"id": "2026-02-16-speed-dating-ai-avatars",
         "title": "A pop-up restaurant lets patrons speed-date AI avatars",
         "claim": "EVA AI opened a Hell's Kitchen pop-up where patrons speed-dated AI avatars "
                  "for Valentine's Day, while Meta was granted a patent for models that keep "
                  "deceased users' accounts posting and simulating calls after death.",
         "domain": "society", "actor": ["meta"],
         "evidences": ["machine-affect", "resurrection-and-time", "intimate-interface"]},
        {"id": "2026-02-16-claude-in-community-colleges",
         "title": "Claude is placed at the centre of CS courses for 20,000 students",
         "claim": "Anthropic partnered with CodePath to put Claude at the centre of computer "
                  "science courses for more than 20,000 students at community colleges and "
                  "HBCUs, over 40% from families earning under $50,000, while Airbnb said a "
                  "third of its North American support is now AI.",
         "domain": "society", "actor": ["anthropic", "codepath", "airbnb"], "score": "20,000 students",
         "evidences": ["deskilling", "work-displaced"]},
        {"id": "2026-02-16-claude-used-to-capture-maduro",
         "title": "Claude was reportedly used in the capture of Maduro",
         "claim": "Claude was reportedly used by the Department of War in the operation that "
                  "captured Venezuela's Nicolás Maduro.",
         "domain": "policy", "actor": ["war-department", "anthropic"],
         "evidences": ["politics-as-infrastructure", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-01-04-maduro-capture-drone-cyber"]},
        {"id": "2026-02-16-router-memory-costs-7x",
         "title": "Memory goes from 3% to a fifth of router cost",
         "claim": "Western Digital's entire hard drive capacity for the year is booked and "
                  "broadband memory prices have risen sevenfold in nine months, pushing memory "
                  "from 3% to over 20% of router costs, while TSMC plans another $100 billion "
                  "for four more US fabs.",
         "domain": "economics", "actor": ["western-digital", "tsmc"], "score": "7x / 3%→20%",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-02-12-gaming-laptops-become-a-rental"]},
        {"id": "2026-02-16-spacex-hires-crystal-growers",
         "title": "SpaceX hires crystal growers for orbital wafer fabs",
         "claim": "SpaceX is hiring crystal growth scientists to build silicon wafer fab lines "
                  "that could support space-based chip manufacturing, while internally scaling "
                  "a Grok variant trained on company data.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["orbit-as-compute", "vertical-silicon"],
         "supersedes": [B + "developments/2026-02-13-mass-and-energy-not-dollars"]},
        {"id": "2026-02-16-first-airlift-of-a-reactor",
         "title": "A nuclear reactor is airlifted for the first time",
         "claim": "The Department of War executed Operation Windlord, the first C-17 airlift of "
                  "a nuclear reactor, while Helion's Polaris became the first privately funded "
                  "machine to achieve deuterium-tritium fusion at 150 million degrees.",
         "domain": "energy", "actor": ["war-department", "helion"], "score": "150M degrees",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-02-11-3d-printed-nuclear-batteries"]},
        {"id": "2026-02-16-humanoid-boxing-and-drone-swarms",
         "title": "Humanoids box for paying crowds as the PLA plans autonomous swarms",
         "claim": "Companies are staging boxing matches between VR-controlled Chinese humanoids "
                  "for paying San Francisco crowds, while an internal PLA report reveals plans "
                  "for self-coordinating drone swarms under AI decision-making and Anduril "
                  "raises billions at a $60 billion valuation.",
         "domain": "robotics", "actor": ["china", "anduril"], "score": "$60B",
         "evidences": ["autonomy-clock-speed", "physical-recursion"],
         "supersedes": [B + "developments/2026-02-09-unitree-shovels-snow"]},
        {"id": "2026-02-16-productivity-grows-27pct",
         "title": "US productivity growth nearly doubles the decade average",
         "claim": "Stanford analysis showed US productivity grew 2.7% in 2025, nearly double the "
                  "prior decade's average, while India cleared a $1.1 billion deep tech venture "
                  "programme and ChatGPT reached 100 million weekly users there.",
         "domain": "economics", "actor": ["stanford"], "score": "+2.7%",
         "evidences": ["growth-without-hiring", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-13-logistics-stocks-tumble"]},
        {"id": "2026-02-16-elephant-personhood-dismissed",
         "title": "A court dismisses an elephant personhood claim as agents win their own court",
         "claim": "A Pennsylvania judge dismissed a suit by the Nonhuman Rights Project arguing "
                  "elephants at the Pittsburgh Zoo share a right to bodily liberty.",
         "domain": "policy", "actor": ["nonhuman-rights"],
         "evidences": ["agent-exclusion", "legislating-the-shift", "biosphere-uplift"],
         "body": "Animals are refused standing in court the same week agents build one of "
                 "their own."},
        {"id": "2026-02-16-oura-rings-replace-wedding-bands",
         "title": "Sensors replace wedding bands and glasses gain face recognition",
         "claim": "Oura rings are replacing wedding bands in Silicon Valley while Meta plans to "
                  "add facial recognition to its smart glasses this year, and Centivax dosed "
                  "the first participants in a universal flu vaccine trial.",
         "domain": "biotech", "actor": ["oura", "meta", "centivax"],
         "evidences": ["intimate-interface", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-12-seven-million-smart-glasses"]},
    ],
}
