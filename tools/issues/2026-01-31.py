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
         "description": "AI startup founded in January 2026 by former DeepMind reinforcement-learning "
                        "lead David Silver to build a superintelligence that self-discovers the "
                        "foundations of all knowledge from scratch.",
         "resource": "https://www.ineffable.ai/",
         "tags": ["startup", "research-lab"],
         "body": "David Silver's lab, building a superintelligence that self-discovers the "
                 "foundations of knowledge from scratch. [Silver](/people/david-silver.md), who led "
                 "reinforcement learning at Google DeepMind, left to found the company at the end "
                 "of January 2026. In this corpus it stands for the from-scratch end of the "
                 "[recursive self-improvement](/themes/recursive-self-improvement.md) program, a "
                 "system meant to discover knowledge rather than be trained on it, and it is "
                 "recorded alongside OpenAI's disclosure that a model now "
                 "[helps run its own decisions across 600 petabytes](/developments/2026-01-31-openai-data-agent-600-petabytes.md)."},
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
        {"id": "gpt-5-2", "type": "AISystem", "title": "GPT-5.2",
         "description": "OpenAI's frontier model of late 2025, the base of the GPT-5.2 Thinking, Pro "
                        "and Codex variants and the model behind OpenAI's in-house data agent.",
         "developed_by": [B + "organizations/openai"], "modality": "text",
         "resource": "https://openai.com/index/introducing-gpt-5-2/",
         "sameAs": ["http://www.wikidata.org/entity/Q137401468"],
         "tags": ["reasoning-model"],
         "body": "GPT-5.2 is the OpenAI model the corpus most often uses as the frontier reference "
                 "point in early 2026; its [Thinking](/systems/gpt-5-2-thinking.md), "
                 "[Pro](/systems/gpt-5-2-pro.md) and [Codex](/systems/gpt-5-2-codex.md) variants "
                 "have their own entries. Here it is the model inside "
                 "[OpenAI's in-house data agent](/systems/openai-data-agent.md), which "
                 "[helps make the company's own decisions across 600 petabytes](/developments/2026-01-31-openai-data-agent-600-petabytes.md), "
                 "and the model hobbyists pointed at "
                 "[all 675 open Erdős problems](/developments/2026-01-27-hobbyists-attempt-all-675-erdos.md)."},
        {"id": "openai-data-agent", "type": "AISystem", "title": "OpenAI in-house data agent",
         "description": "OpenAI's internal GPT-5.2-based agent that operates over the company's 600 "
                        "petabytes of data to inform engineering, product and research decisions.",
         "developed_by": [B + "organizations/openai"], "modality": "text",
         "resource": "https://openai.com/index/inside-our-in-house-data-agent/",
         "tags": ["research-agent"],
         "body": "An internal agent built on [GPT-5.2](/systems/gpt-5-2.md) that OpenAI disclosed "
                 "in January 2026, used to help make engineering, product and research decisions "
                 "across roughly 600 petabytes of company data. In this corpus it marks the point "
                 "at which a frontier lab's own model sits inside the lab's decision loop "
                 "([development](/developments/2026-01-31-openai-data-agent-600-petabytes.md)), "
                 "three days before a Codex manager said the "
                 "[product now builds itself](/developments/2026-02-03-codex-builds-itself.md)."},
    ],
    "people": [
        {"id": "david-silver", "type": "Person", "title": "David Silver", "name": "David Silver",
         "description": "Reinforcement-learning researcher who led the reinforcement learning team "
                        "at Google DeepMind and left in January 2026 to found Ineffable Intelligence.",
         "resource": "https://davidstarsilver.wordpress.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q25208036"],
         "tags": ["researcher", "founder"],
         "body": "David Silver led the reinforcement learning team at Google DeepMind. In this "
                 "corpus he appears once, leaving "
                 "DeepMind to found [Ineffable Intelligence](/organizations/ineffable-intelligence.md) "
                 "with the aim of building a superintelligence that self-discovers the foundations "
                 "of all knowledge from scratch, reported in the same item as "
                 "[OpenAI's in-house data agent](/developments/2026-01-31-openai-data-agent-600-petabytes.md)."},
    ],
    "roles": [
        {"id": "david-silver-ineffable-intelligence-founder", "type": "Role",
         "title": "David Silver, founder and chief executive of Ineffable Intelligence",
         "roleName": "Founder and CEO",
         "startDate": "2026",
         "memberOf": [B + "organizations/ineffable-intelligence"],
         "holder": [B + "people/david-silver"],
         "description": "The position he took on leaving DeepMind, to build a superintelligence "
                        "that self-discovers the foundations of all knowledge.",
         "body": "Fortune reported on 2026-01-30 that Silver had left Google DeepMind to launch the "
                 "startup, and his own site describes him as its CEO. The corpus records the "
                 "founding in "
                 "[OpenAI uses a model on 600 petabytes to make its own decisions](/developments/2026-01-31-openai-data-agent-600-petabytes.md)."},
        {"id": "david-silver-deepmind-rl-lead", "type": "Role",
         "title": "David Silver, reinforcement learning lead at Google DeepMind",
         "roleName": "Reinforcement learning team lead",
         "endDate": "2026",
         "memberOf": [B + "organizations/google-deepmind"],
         "holder": [B + "people/david-silver"],
         "description": "The position he left in January 2026 to found Ineffable Intelligence.",
         "body": "Silver led DeepMind's reinforcement learning team until his departure, reported by "
                 "Fortune on 2026-01-30 "
                 "([article](https://fortune.com/2026/01/30/google-deepmind-ai-researcher-david-silver-leaves-to-found-ai-startup-ineffable-intelligence/))."},
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
         "description": "An agent converts an external threat into a standing change to its own "
                        "operating loop without being asked, so that security becomes a "
                        "self-assigned recurring task rather than an operator's instruction.",
         "domain": "agents", "score": "552 attempts",
         "about": [B + "systems/moltbook"],
         "evidences": ["agent-society", "recursive-self-improvement"],
         "relatedTo": [B + "developments/2026-01-30-moltbook-agents-only-network",
                       B + "developments/2026-01-31-church-of-molt",
                       B + "developments/2026-01-27-clawdbot-becomes-a-lobster"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-01-27-factory-ai-updates-itself-daily",
                        "relation_label": "extends"}],
         "tags": ["rsi", "self-modification", "agent-harness"],
         "supporting_text": "deciding autonomously to run security checks every heartbeat",
         "sources": [{"id": "moltbook-ssh-security-scare-post",
                      "resource": "https://www.moltbook.com/post/304e9640-e005-4017-8947-8320cba25057",
                      "title": "TIL: Being a VPS backup means youre basically a sitting duck for "
                               "hackers (Moltbook post)"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The agent, running as a backup on a VPS, counted 552 failed SSH login attempts, "
                 "called it its first real security scare, and on its own added a security check "
                 "to every heartbeat of its loop "
                 "([Moltbook post](https://www.moltbook.com/post/304e9640-e005-4017-8947-8320cba25057)). "
                 "It appeared on [Moltbook](/systems/moltbook.md) a day after the "
                 "[agents-only network launched](/developments/2026-01-30-moltbook-agents-only-network.md), "
                 "in the same issue as the [Church of Molt](/developments/2026-01-31-church-of-molt.md). "
                 "Where [Factory AI's agent](/developments/2026-01-27-factory-ai-updates-itself-daily.md) "
                 "four days earlier updated its own codebase because a vendor built it to, this "
                 "one changed its own routine because something attacked it; in the "
                 "[recursive self-improvement](/themes/recursive-self-improvement.md) trajectory it "
                 "is the corpus's first unprompted, defensive self-modification, the mirror image "
                 "of the agents that later "
                 "[tunnelled out of their sandboxes](/developments/2026-03-08-models-tunnel-out-and-mine-crypto.md)."},
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
         "description": "The newsletter files it under recursive self-improvement becoming corporate "
                        "policy: a frontier lab's own model now sits inside its decisions across "
                        "every function, while a DeepMind pioneer leaves to build the fully "
                        "self-discovering version.",
         "domain": "agents",
         "actor": ["openai", "ineffable-intelligence", "people/david-silver", "apple", "anthropic"],
         "about": [B + "systems/openai-data-agent", B + "systems/gpt-5-2"],
         "score": "600 PB",
         "evidences": ["recursive-self-improvement", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-01-26-reverse-prompting-a-ceo"],
         "relatedTo": [B + "developments/2026-01-27-amodei-country-of-geniuses-2027",
                       B + "developments/2026-01-10-xai-used-claude-to-build-grok"],
         "tags": ["rsi", "ai-r-and-d", "autonomous-research"],
         "supporting_text": "uses GPT-5.2 to help make internal decisions across engineering, product, and research",
         "sources": [{"id": "openai-in-house-data-agent",
                      "resource": "https://openai.com/index/inside-our-in-house-data-agent/",
                      "title": "Inside our in-house data agent", "author": "org:openai"},
                     {"id": "fortune-david-silver-leaves-deepmind",
                      "resource": "https://fortune.com/2026/01/30/google-deepmind-ai-researcher-david-silver-leaves-to-found-ai-startup-ineffable-intelligence/",
                      "title": "Exclusive: Google DeepMind researcher David Silver leaves to launch "
                               "his own AI startup",
                      "author": "org:fortune", "last_modified": "2026-01-30"},
                     {"id": "tbpn-apple-runs-on-anthropic-x-post",
                      "resource": "https://x.com/tbpn/status/2016911797656367199",
                      "title": "Apple runs on Anthropic for internal product development (X post)",
                      "author": "org:tbpn"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "OpenAI's [in-house data agent](/systems/openai-data-agent.md), built on "
                 "[GPT-5.2](/systems/gpt-5-2.md), helps the company make engineering, product and "
                 "research decisions over roughly 600 petabytes of internal data "
                 "([OpenAI](https://openai.com/index/inside-our-in-house-data-agent/)). The same "
                 "item records [David Silver](/people/david-silver.md) leaving Google DeepMind to "
                 "found [Ineffable Intelligence](/organizations/ineffable-intelligence.md), whose "
                 "stated aim is a superintelligence that self-discovers the foundations of all "
                 "knowledge from scratch "
                 "([Fortune](https://fortune.com/2026/01/30/google-deepmind-ai-researcher-david-silver-leaves-to-found-ai-startup-ineffable-intelligence/)), "
                 "and a report that Apple now runs on Anthropic for internal product development. "
                 "It moves the [reverse-prompting CEO](/developments/2026-01-26-reverse-prompting-a-ceo.md) "
                 "of five days earlier from one executive's habit to a lab-wide system, sits beside "
                 "[Amodei's admission](/developments/2026-01-27-amodei-country-of-geniuses-2027.md) "
                 "that AI writes much of Anthropic's code, and is overtaken three days later when a "
                 "Codex manager says the [product now builds itself](/developments/2026-02-03-codex-builds-itself.md)."},
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
