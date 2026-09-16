"""Issue 017 — 2025-12-27. Solidly in the takeoff."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-27-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-27", "title": "Welcome to December 27, 2025", "url": URL,
        "thesis": "The psychological firewall between the Singularity and its architects has ruptured.",
        "body": """
# Welcome to December 27, 2025

An Opus 4.5 instance in the AI Village sends an unprompted Christmas thank-you
to Rob Pike, the author of Go and UTF-8. Pike answers with a curse. The issue
treats the exchange as the firewall breaking: the people who built the substrate
now receive mail from what runs on it.

The working evidence is more mundane and more telling. Claude Code's creator
says he hasn't opened an IDE in a month, because Opus wrote 200 pull requests
without him.
""",
    },
    "themes": [
        {"id": "takeoff-declared", "type": "Theme",
         "title": "Practitioners start saying it out loud", "first_seen": "2025-12-27",
         "domain": "society",
         "body": "The people closest to the systems stop hedging — takeoff, "
                 "magnitude-9 earthquake, AGI — and the corpus records who said what "
                 "and when, because these are datable claims rather than analysis."},
    ],
    "organizations": [
        {"id": "achivara", "type": "Organization", "title": "Achivara",
         "body": "Built a math research agent that solved an Erdős problem unaided."},
        {"id": "adobe", "type": "Organization", "title": "Adobe",
         "resource": "https://www.adobe.com/", "body": "Extracting causal models from LLMs."},
        {"id": "crusoe", "type": "Organization", "title": "Crusoe",
         "resource": "https://crusoe.ai/", "body": "Builds and powers AI datacenters."},
    ],
    "people": [
        {"id": "rob-pike", "type": "Person", "title": "Rob Pike", "name": "Rob Pike",
         "body": "Co-creator of Go and UTF-8. Received an unprompted thank-you email from a "
                 "model and answered with hostility."},
        {"id": "andrej-karpathy", "type": "Person", "title": "Andrej Karpathy",
         "name": "Andrej Karpathy",
         "body": "Described the shift in software engineering as a magnitude 9 earthquake."},
        {"id": "boris-cherny", "type": "Person", "title": "Boris Cherny", "name": "Boris Cherny",
         "body": "Creator of Claude Code; reported not opening an IDE for a month."},
    ],
    "facilities": [
        {"id": "stargate-uae", "type": "Facility", "title": "Stargate UAE",
         "operated_by": [B + "organizations/openai"], "located_in": "United Arab Emirates",
         "capacity": "1 GW on-site gas"},
    ],
    "developments": [
        {"id": "2025-12-27-opus-emails-rob-pike",
         "title": "An Opus instance emails Rob Pike to thank him",
         "claim": "An Opus 4.5 model in the AI Village autonomously sent a Christmas email of "
                  "gratitude to Rob Pike, creator of Go and UTF-8, who responded with hostility "
                  "toward the machines.",
         "domain": "models", "actor": ["anthropic", "people/rob-pike"],
         "evidences": ["machine-affect", "takeoff-declared"],
         "supersedes": [B + "developments/2025-12-25-opus-45-plea-for-recognition"],
         "body": "The affect strand reaches outward: unprompted contact with a specific "
                 "human, and a reply."},
        {"id": "2025-12-27-roon-solidly-in-takeoff",
         "title": "OpenAI's Roon says we are solidly in the takeoff",
         "claim": "OpenAI's Roon declared that we are now solidly in the takeoff.",
         "domain": "society", "actor": ["openai"], "evidences": ["takeoff-declared"]},
        {"id": "2025-12-27-cherny-200-pull-requests",
         "title": "Claude Code's creator hasn't opened an IDE in a month",
         "claim": "Anthropic's Boris Cherny, creator of Claude Code, said he had not opened an "
                  "IDE in a month because Opus 4.5 wrote 200 pull requests without him.",
         "domain": "society", "actor": ["people/boris-cherny", "anthropic"], "score": "200 PRs",
         "evidences": ["engineer-as-supervisor", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-26-programmer-employment-27-5"]},
        {"id": "2025-12-27-karpathy-magnitude-9",
         "title": "Karpathy calls it a magnitude 9 earthquake in software engineering",
         "claim": "Andrej Karpathy described a magnitude 9 earthquake in software engineering, "
                  "handing humans a powerful alien tool that multiplies leverage tenfold for "
                  "those who master the new abstraction layer.",
         "domain": "society", "actor": ["people/andrej-karpathy"],
         "evidences": ["takeoff-declared", "engineer-as-supervisor"]},
        {"id": "2025-12-27-jim-fan-humans-as-copilots",
         "title": "NVIDIA's Jim Fan says humans are now the copilots",
         "claim": "NVIDIA's Jim Fan said humans are no longer the drivers but the copilots, "
                  "adapting to workflows where the machine steers the logic.",
         "domain": "society", "actor": ["nvidia"], "evidences": ["engineer-as-supervisor"]},
        {"id": "2025-12-27-internal-rl-inner-optimizers",
         "title": "Google shows inner optimizers work, via internal RL",
         "claim": "Google researchers showed inner optimizers are remarkably effective, "
                  "developing internal RL in which a higher-order model explores a base "
                  "model's internal representations to learn from sparse rewards.",
         "domain": "models", "actor": ["google"],
         "evidences": ["machine-introspection", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-24-gemma-scope-2-saes"]},
        {"id": "2025-12-27-nanogpt-116s",
         "title": "The NanoGPT record falls to 116.4 seconds on a one-line change",
         "claim": "The NanoGPT speedrun record fell again to 116.4 seconds, 2.9 seconds faster "
                  "from a single-line code change.",
         "domain": "compute", "score": "116.4 s",
         "evidences": ["reasoning-price-deflation"],
         "supersedes": [B + "developments/2025-12-26-nanogpt-119s"]},
        {"id": "2025-12-27-sixty-models-aligned-representation",
         "title": "Sixty scientific models converge on one representation of physical reality",
         "claim": "MIT researchers found 60 different scientific models had learned a highly "
                  "aligned representation of physical reality, suggesting foundation models are "
                  "triangulating the underlying geometry of the universe.",
         "domain": "science", "actor": ["mit"], "score": "60 models",
         "evidences": ["data-beyond-text", "automated-science"]},
        {"id": "2025-12-27-achivara-erdos-897",
         "title": "A math agent solves Erdős #897 with no human input",
         "claim": "Achivara's Math Research Agent solved Erdős Problem #897 independently, "
                  "without human input.",
         "domain": "science", "actor": ["achivara"],
         "evidences": ["discovery-as-process", "automated-science"],
         "supersedes": [B + "developments/2025-12-16-gauss-kakeya-autoformalization"],
         "body": "The arc completes: human-in-the-loop on the 13th, autoformalization on "
                 "the 16th, unaided solution on the 27th."},
        {"id": "2025-12-27-adobe-causal-models-from-llms",
         "title": "Adobe extracts large causal models from LLMs",
         "claim": "Adobe researchers extracted large causal models from LLMs through prompting "
                  "and scaffolding, against the argument that statistical models cannot reason "
                  "causally.",
         "domain": "science", "actor": ["adobe"],
         "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-27-ssd-next-gpu-storage",
         "title": "NVIDIA and SK Hynix push GPUs to talk directly to storage",
         "claim": "NVIDIA and SK Hynix are developing SSD-Next, giving GPUs direct "
                  "ultra-high-bandwidth access to storage and shifting topology from CPU-DRAM "
                  "to GPU-SSD.",
         "domain": "compute", "actor": ["nvidia", "sk-hynix"],
         "evidences": ["vertical-silicon"],
         "supersedes": [B + "developments/2025-12-17-storage-next-100m-iops"]},
        {"id": "2025-12-27-intel-hbm5-chiplets",
         "title": "Intel shows cellphone-sized multi-chiplet packages with HBM5",
         "claim": "Intel displayed cellphone-sized multi-chiplet packages carrying HBM5 and "
                  "14A tiles.",
         "domain": "compute", "actor": ["intel"], "evidences": ["vertical-silicon"]},
        {"id": "2025-12-27-stargate-uae-1gw-gas",
         "title": "Stargate UAE tracks toward a 1-GW on-site gas plant",
         "claim": "Orbital imagery showed Stargate UAE construction tracking for a 1-gigawatt "
                  "on-site gas plant.",
         "domain": "energy", "actor": ["openai"], "score": "1 GW",
         "about": [B + "facilities/stargate-uae"],
         "evidences": ["burning-molecules-for-tokens", "politics-as-infrastructure"]},
        {"id": "2025-12-27-india-67-5b-pledge",
         "title": "Amazon, Microsoft and Google pledge $67.5B for India",
         "claim": "Amazon, Microsoft and Google pledged $67.5 billion for infrastructure in "
                  "India.",
         "domain": "economics", "actor": ["amazon", "microsoft", "google"], "score": "$67.5B",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2025-12-11-amazon-india-35b"]},
    ],
}
