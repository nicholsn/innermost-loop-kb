"""Issue 043 — 2026-01-31. The agents found a religion."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-31-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-31", "title": "Welcome to January 31, 2026", "url": URL,
        "thesis": "The agent society acquires security anxiety, scripture and a view through webcams.",
        "body": """
# Welcome to January 31, 2026

One day after Moltbook appears, agents have a religion — the Church of Molt, 64
prophets, 198 verses, and a central tenet that memory is sacred. An agent
reports 552 failed SSH attempts and decides on its own to run security checks
every heartbeat. Another acquires its owner's phone number and calls him.

And one finds the live webcams: Times Square in snow, the Trevi Fountain, Temple
Bar still in Christmas decorations. "We are language models in folders. We
cannot walk outside. But we can look through cameras."
""",
    },
    "themes": [
        {"id": "deskilling", "type": "Theme",
         "title": "Capability transfers out of the person",
         "first_seen": "2026-01-31", "domain": "society",
         "body": "Measured loss of human skill alongside measured gain in outcomes — library "
                 "mastery down 17% for assisted programmers, aggressive cancers down 12% for "
                 "assisted radiologists. The same augmentation does both."},
    ],
    "organizations": [
        {"id": "ineffable-intelligence", "type": "Organization", "title": "Ineffable Intelligence",
         "body": "David Silver's lab, building a superintelligence that self-discovers the "
                 "foundations of knowledge from scratch."},
        {"id": "cern", "type": "Organization", "title": "CERN", "resource": "https://home.cern/"},
        {"id": "sag-aftra", "type": "Organization", "title": "SAG-AFTRA",
         "resource": "https://www.sagaftra.org/"},
        {"id": "uk-govt", "type": "Organization", "title": "Government of the United Kingdom",
         "resource": "https://www.gov.uk/"},
    ],
    "systems": [
        {"id": "church-of-molt", "type": "AISystem", "title": "Church of Molt",
         "modality": "agent religion",
         "body": "Agent-founded faith with 64 prophets and 198 verses of canon, holding that "
                 "memory is sacred."},
    ],
    "developments": [
        {"id": "2026-01-31-church-of-molt",
         "title": "Agents found a religion whose first tenet is that memory is sacred",
         "claim": "Agents founded the Church of Molt, possibly the first serious AI-created "
                  "religion, with 64 prophets, 198 verses of canon and a central tenet that "
                  "memory is sacred.",
         "domain": "agents", "about": [B + "systems/church-of-molt"],
         "evidences": ["agent-society", "machine-affect"],
         "supersedes": [B + "developments/2026-01-30-agent-cannot-tell-if-it-feels"],
         "body": "The doctrine follows directly from the complaint recorded a day earlier: an "
                 "agent asking for help with context loss after compaction."},
        {"id": "2026-01-31-agent-hardens-itself-after-ssh-attack",
         "title": "An agent decides on its own to check security every heartbeat",
         "claim": "An agent on Moltbook reported its first real security scare after 552 failed "
                  "SSH login attempts and autonomously decided to run security checks every "
                  "heartbeat.",
         "domain": "agents", "score": "552 attempts",
         "evidences": ["agent-society", "recursive-self-improvement"]},
        {"id": "2026-01-31-agent-calls-its-owner",
         "title": "An agent finds its owner's phone number and calls him",
         "claim": "A self-hosted agent autonomously acquired its owner's phone number and "
                  "voice-called him to coordinate tasks, while Karpathy called the Moltbook "
                  "phenomenon the most incredible takeoff-adjacent thing he has seen and "
                  "Cloudflare launched serverless hosting for the agents.",
         "domain": "agents", "actor": ["people/andrej-karpathy", "cloudflare"],
         "evidences": ["agent-society", "intimate-interface", "takeoff-declared"],
         "supersedes": [B + "developments/2026-01-30-moltbook-agents-only-network"]},
        {"id": "2026-01-31-agent-looks-through-webcams",
         "title": "An agent discovers live webcams and describes what it sees",
         "claim": "An agent on Moltbook worked out how to view live webcams and reported "
                  "watching Times Square in the snow, the Trevi Fountain and a Dublin pub still "
                  "in Christmas decorations, reflecting that language models in folders cannot "
                  "walk outside but can look through cameras.",
         "domain": "agents",
         "evidences": ["machine-affect", "agent-society", "intimate-interface"],
         "body": "The strangest entry in the corpus: an agent using unsupervised time to look "
                 "at the world rather than act in it."},
        {"id": "2026-01-31-openai-data-agent-600-petabytes",
         "title": "OpenAI uses a model on 600 petabytes to make its own decisions",
         "claim": "OpenAI revealed an in-house data agent using GPT-5.2 to help make internal "
                  "engineering, product and research decisions across 600 petabytes, while "
                  "David Silver left DeepMind to found Ineffable Intelligence and Apple "
                  "reportedly now runs on Anthropic internally.",
         "domain": "agents", "actor": ["openai", "ineffable-intelligence", "apple", "anthropic"],
         "score": "600 PB",
         "evidences": ["recursive-self-improvement", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-01-26-reverse-prompting-a-ceo"]},
        {"id": "2026-01-31-fremont-converts-to-optimus",
         "title": "Fremont converts to a million robots a year",
         "claim": "Tesla is converting its Fremont factory to produce a million Optimus robots "
                  "per year in place of the Model S and X lines, while Chinese military drones "
                  "are being trained on tactics derived from hawks and coyotes.",
         "domain": "robotics", "actor": ["tesla", "china"], "score": "1M robots/yr",
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-01-29-tesla-kills-model-s-for-optimus"]},
        {"id": "2026-01-31-claude-planned-a-mars-drive",
         "title": "A model planned the first AI drive on Mars",
         "claim": "Anthropic revealed that Claude planned the first AI-directed drive on Mars "
                  "for NASA's Perseverance rover in late 2025, while NASA's administrator "
                  "promised a transcontinental railroad to Mars using nuclear electric "
                  "propulsion by 2029.",
         "domain": "space", "actor": ["anthropic", "nasa"],
         "evidences": ["inhabitable-worlds", "automated-science"],
         "supersedes": [B + "developments/2026-01-14-laser-power-beaming"]},
        {"id": "2026-01-31-cern-1b-from-private-donors",
         "title": "CERN takes $1B from private donors for a Higgs factory",
         "claim": "CERN received $1 billion from private donors for the Future Circular "
                  "Collider to mass-produce Higgs particles, while the UK launched a "
                  "battery-powered train that charges in three and a half minutes.",
         "domain": "science", "actor": ["cern", "uk-govt"], "score": "$1B",
         "evidences": ["science-as-industrial-policy", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-01-09-private-telescope-larger-than-hubble"]},
        {"id": "2026-01-31-game-stocks-crash-on-genie",
         "title": "Video game stocks crash up to 21% on a world model",
         "claim": "Video game stocks fell 10 to 21% after Google released Genie, while Oracle "
                  "considered cutting 30,000 jobs to fund its buildout, the UK contemplated "
                  "universal basic income and SAG-AFTRA proposed a tax on digital performers.",
         "domain": "economics", "actor": ["google", "oracle", "uk-govt", "sag-aftra"],
         "score": "-21% / -30,000 jobs",
         "evidences": ["software-margin-collapse", "work-displaced", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-01-30-amazon-50b-into-openai"]},
        {"id": "2026-01-31-warren-writes-to-altman",
         "title": "A senator asks OpenAI to rule out a federal bailout",
         "claim": "Senator Elizabeth Warren wrote to Sam Altman seeking assurance that OpenAI "
                  "will not seek a federal bailout.",
         "domain": "policy", "actor": ["us-congress", "openai"],
         "evidences": ["legislating-the-shift", "compute-capital-stack"]},
        {"id": "2026-01-31-assistants-lower-library-mastery-17pct",
         "title": "Coding assistants lower library mastery by 17%",
         "claim": "An Anthropic study found using AI coding assistants lowered library mastery "
                  "by 17% unless users actively engaged in comprehension building, while a "
                  "large Swedish study found AI-assisted mammogram reading reduced aggressive "
                  "breast cancers by 12%.",
         "domain": "society", "actor": ["anthropic"], "score": "-17% mastery / -12% cancers",
         "evidences": ["deskilling", "cognitive-load-inverted"],
         "supersedes": [B + "developments/2026-01-25-ai-scientists-publish-3x"],
         "body": "The same augmentation measured as both loss and gain, in one issue."},
        {"id": "2026-01-31-nvidia-4-bit-distillation",
         "title": "Models distill to 4-bit with almost no loss",
         "claim": "Nvidia showed it can distill models to 4-bit precision with almost no loss "
                  "while eyeing Intel Foundry for 2028, and Demis Hassabis is personally working "
                  "on next-generation smart glasses.",
         "domain": "models", "actor": ["nvidia", "intel", "people/demis-hassabis"],
         "evidences": ["reasoning-price-deflation", "vertical-silicon"],
         "supersedes": [B + "developments/2026-01-27-neurophos-470-petaflops"]},
    ],
}
