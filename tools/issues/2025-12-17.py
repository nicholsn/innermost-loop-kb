"""Issue 007 — 2025-12-17. Discovery deprecated."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-17-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-17",
        "title": "Welcome to December 17, 2025",
        "url": URL,
        "thesis": "The miracle of discovery is being deprecated by the Singularity.",
        "body": """
# Welcome to December 17, 2025

A model put in charge of a wet lab, directing humans and robots to a cloning
protocol 79x more efficient than standard. The claim is not that discovery got
faster but that it stopped being miraculous — and Terry Tao supplies the line
that makes it stick, comparing AI-driven proof to a magic trick whose awe
dissipates once you learn how it was done.

Four days earlier he was the human in the loop. Here he is describing the loop
becoming industrial process.
""",
    },

    "themes": [
        {"id": "discovery-as-process", "type": "Theme",
         "title": "Discovery becomes industrial process",
         "first_seen": "2025-12-17", "domain": "science",
         "body": "Not merely automated but demystified: results arrive on a schedule, "
                 "and the awe attached to them converts into technical respect. The "
                 "newsletter treats the loss of wonder as the real signal."},
        {"id": "politics-as-infrastructure", "type": "Theme",
         "title": "Politics becomes infrastructure",
         "first_seen": "2025-12-17", "domain": "policy",
         "body": "Statecraft reorganized around the buildout: national AI stacks "
                 "exported as policy, permitting rewritten to lay concrete faster."},
    ],

    "organizations": [
        {"id": "red-queen-bio", "type": "Organization", "title": "Red Queen Bio",
         "body": "Biosecurity-focused lab running AI-directed wet-lab work with OpenAI."},
        {"id": "quilter", "type": "Organization", "title": "Quilter",
         "resource": "https://www.quilter.ai/", "body": "AI-driven circuit board design."},
        {"id": "meta", "type": "Organization", "title": "Meta",
         "resource": "https://about.meta.com/", "body": "Released the SAM Audio separation model."},
        {"id": "resemble-ai", "type": "Organization", "title": "Resemble AI",
         "resource": "https://www.resemble.ai/", "body": "Open voice models."},
        {"id": "sk-hynix", "type": "Organization", "title": "SK Hynix",
         "resource": "https://www.skhynix.com/", "body": "Memory maker; co-developing an AI SSD."},
        {"id": "physical-intelligence", "type": "Organization", "title": "Physical Intelligence",
         "resource": "https://www.physicalintelligence.company/",
         "body": "Vision-language-action models for robots."},
        {"id": "waymo", "type": "Organization", "title": "Waymo",
         "resource": "https://waymo.com/", "body": "Autonomous ride-hailing."},
        {"id": "neurobionics", "type": "Organization", "title": "NeuroBionics",
         "body": "Fiber-thin neural interfaces delivered through blood vessels."},
        {"id": "nasdaq", "type": "Organization", "title": "Nasdaq",
         "resource": "https://www.nasdaq.com/", "body": "Exchange; filed for round-the-clock trading."},
    ],

    "systems": [
        {"id": "gpt-image-1-5", "type": "AISystem", "title": "GPT Image 1.5",
         "developed_by": [B + "organizations/openai"], "modality": "image"},
        {"id": "sam-audio", "type": "AISystem", "title": "SAM Audio",
         "developed_by": [B + "organizations/meta"], "modality": "audio",
         "body": "Isolates any sound from any source."},
        {"id": "chatterbox-turbo", "type": "AISystem", "title": "Chatterbox Turbo",
         "developed_by": [B + "organizations/resemble-ai"], "modality": "speech",
         "body": "MIT-licensed, which is the point: a frontier voice engine without "
                 "commercial restrictions."},
        {"id": "cc-agent", "type": "AISystem", "title": "CC",
         "developed_by": [B + "organizations/google"], "modality": "personal agent",
         "body": "Digests a user's digital life into a daily briefing and drafts replies."},
    ],

    "hardware": [
        {"id": "storage-next-ssd", "type": "Hardware", "title": "Storage Next AI SSD",
         "developed_by": [B + "organizations/nvidia", B + "organizations/sk-hynix"],
         "body": "Targeting 100 million IOPS to stream model weights faster than HBM allows."},
        {"id": "trainium", "type": "Hardware", "title": "AWS Trainium",
         "developed_by": [B + "organizations/amazon"],
         "body": "Amazon's training accelerator, tied to a reported OpenAI investment."},
    ],

    "benchmarks": [
        {"id": "frontierscience", "type": "Benchmark", "title": "FrontierScience",
         "published_by": [B + "organizations/openai"],
         "measures_capability": "expert-level scientific reasoning"},
        {"id": "lmarena", "type": "Benchmark", "title": "LMArena",
         "measures_capability": "head-to-head human preference between models"},
    ],

    "facilities": [
        {"id": "tesla-cortex-2", "type": "Facility", "title": "Cortex 2",
         "operated_by": [B + "organizations/tesla"], "located_in": "Texas, USA",
         "capacity": "200 MW", "body": "Permitted cluster for training Optimus."},
    ],

    "developments": [
        {"id": "2025-12-17-gpt5-runs-wet-lab",
         "title": "GPT-5 directs a wet lab to a 79x better cloning protocol",
         "claim": "OpenAI and Red Queen Bio put GPT-5 in charge of a wet lab, where it "
                  "directed humans and robots to invent a cloning protocol 79x more "
                  "efficient than standard methods.",
         "domain": "science", "actor": ["openai", "red-queen-bio"], "score": "79x",
         "evidences": ["discovery-as-process", "automated-science", "compiling-matter"]},
        {"id": "2025-12-17-quilter-two-board-design",
         "title": "Quilter compresses a quarterly board design into under a week",
         "claim": "Quilter's AI designed a two-board computer system in less than a week, "
                  "compressing a quarterly engineering cycle.",
         "domain": "compute", "actor": ["quilter"], "score": "<1 week",
         "evidences": ["discovery-as-process"]},
        {"id": "2025-12-17-tao-magic-dissipates",
         "title": "Tao compares AI-driven proof to a magic trick explained",
         "claim": "Terence Tao compared the era of AI-driven proofs to a magic trick whose "
                  "awe dissipates, or turns into technical respect, once the method is known.",
         "domain": "science", "actor": ["people/terry-tao"],
         "evidences": ["discovery-as-process"],
         "supersedes": [B + "developments/2025-12-13-tao-erdos-1026"],
         "body": "Four days after being the human in the loop, he describes the loop as "
                 "industrial process."},
        {"id": "2025-12-17-frontierscience-benchmark",
         "title": "OpenAI launches the FrontierScience benchmark",
         "claim": "OpenAI launched FrontierScience to test expert-level scientific reasoning.",
         "domain": "benchmarks", "actor": ["openai"], "about": [B + "benchmarks/frontierscience"]},
        {"id": "2025-12-17-chinaxiv-auto-translation",
         "title": "ChinaXiv auto-translates preprints into the global corpus",
         "claim": "ChinaXiv began automatically translating Chinese preprints, unifying them "
                  "with the global scientific corpus.",
         "domain": "science", "evidences": ["automated-science"]},
        {"id": "2025-12-17-gpt-image-1-5-lmarena",
         "title": "GPT Image 1.5 takes the top LMArena spot",
         "claim": "OpenAI released GPT Image 1.5, which immediately took first place on LMArena.",
         "domain": "models", "actor": ["openai"],
         "about": [B + "systems/gpt-image-1-5", B + "benchmarks/lmarena"]},
        {"id": "2025-12-17-meta-sam-audio",
         "title": "Meta's SAM Audio isolates any sound from any source",
         "claim": "Meta unveiled SAM Audio, which isolates any sound from any source.",
         "domain": "models", "actor": ["meta"], "about": [B + "systems/sam-audio"]},
        {"id": "2025-12-17-chatterbox-turbo-mit-licensed",
         "title": "Resemble ships an MIT-licensed frontier voice engine",
         "claim": "Resemble AI released Chatterbox Turbo under an MIT license, giving "
                  "developers a state-of-the-art audio engine without commercial restrictions.",
         "domain": "models", "actor": ["resemble-ai"], "about": [B + "systems/chatterbox-turbo"]},
        {"id": "2025-12-17-google-cc-agent",
         "title": "Google's CC agent digests your digital life into a briefing",
         "claim": "Google's CC agent digests a user's entire digital life into a daily briefing "
                  "and drafts their emails.",
         "domain": "agents", "actor": ["google"], "about": [B + "systems/cc-agent"],
         "evidences": ["intimate-interface"]},
        {"id": "2025-12-17-storage-next-100m-iops",
         "title": "NVIDIA and SK Hynix target 100M IOPS to bypass the memory wall",
         "claim": "NVIDIA and SK Hynix are developing Storage Next, an AI SSD targeting 100 "
                  "million IOPS to feed model weights faster than HBM allows.",
         "domain": "compute", "actor": ["nvidia", "sk-hynix"], "score": "100M IOPS",
         "about": [B + "hardware/storage-next-ssd"],
         "evidences": ["consumer-deprioritized"]},
        {"id": "2025-12-17-amazon-openai-10b-trainium",
         "title": "Amazon discusses $10B into OpenAI tied to Trainium adoption",
         "claim": "Amazon is reportedly discussing a $10 billion investment in OpenAI that "
                  "would see the lab adopt Trainium chips.",
         "domain": "economics", "actor": ["amazon", "openai"], "score": "$10B",
         "about": [B + "hardware/trainium"],
         "evidences": ["vertical-silicon", "compute-capital-stack"]},
        {"id": "2025-12-17-tesla-cortex-2-permit",
         "title": "Tesla permits Cortex 2, a 200-MW cluster for Optimus",
         "claim": "Tesla received a permit for Cortex 2, a 200-MW cluster for training Optimus.",
         "domain": "compute", "actor": ["tesla"], "score": "200 MW",
         "about": [B + "facilities/tesla-cortex-2"]},
        {"id": "2025-12-17-datacenter-thermal-arbitrage",
         "title": "Nearly 7,000 datacenters sit in thermally suboptimal regions",
         "claim": "A new map found nearly 7,000 data centers built in thermally suboptimal "
                  "regions, implying a large relocation arbitrage toward cooler latitudes.",
         "domain": "compute", "score": "~7,000 sites",
         "evidences": ["infrastructure-crowding-out"]},
        {"id": "2025-12-17-stargate-for-countries",
         "title": "OpenAI hires George Osborne to export the American AI stack",
         "claim": "OpenAI hired former UK Chancellor George Osborne to lead Stargate for "
                  "Countries, exporting the American AI stack as a democratic bulwark.",
         "domain": "policy", "actor": ["openai"],
         "evidences": ["politics-as-infrastructure", "silicon-curtain"]},
        {"id": "2025-12-17-speed-act-permitting",
         "title": "Tech giants push the SPEED ACT to fast-track permitting",
         "claim": "Technology companies are pushing the SPEED ACT through Congress to reform "
                  "federal permitting and accelerate the semiconductor buildout.",
         "domain": "policy", "actor": ["us-congress"],
         "evidences": ["politics-as-infrastructure", "infrastructure-crowding-out"]},
        {"id": "2025-12-17-robots-learn-from-human-video",
         "title": "Physical Intelligence aligns human video with robot data",
         "claim": "Physical Intelligence found its vision-language-action models can align "
                  "human video with robot data, letting robots learn by watching people.",
         "domain": "robotics", "actor": ["physical-intelligence"],
         "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-17-waymo-350m-arr",
         "title": "Waymo passes $350M ARR and raises at $100B",
         "claim": "Waymo passed $350 million in annual recurring revenue and is raising capital "
                  "at a $100 billion valuation.",
         "domain": "economics", "actor": ["waymo"], "score": "$350M ARR, $100B valuation"},
        {"id": "2025-12-17-neurobionics-vascular-interface",
         "title": "NeuroBionics reaches the brain through blood vessels",
         "claim": "NeuroBionics is developing fiber-optic-thin neural interfaces that reach the "
                  "brain through blood vessels, avoiding craniotomy.",
         "domain": "biotech", "actor": ["neurobionics"],
         "evidences": ["architecture-of-mind"]},
        {"id": "2025-12-17-embryo-frozen-1994-birth",
         "title": "A healthy baby is born from an embryo frozen in 1994",
         "claim": "Arb Research ranked the birth of a healthy baby from an embryo frozen in "
                  "1994 among the year's top discoveries.",
         "domain": "biotech", "score": "31 years frozen",
         "evidences": ["resurrection-and-time"],
         "body": "Life paused and resumed decades later — the same thread as the "
                 "Victorian model, in biology rather than text."},
        {"id": "2025-12-17-nasdaq-round-the-clock",
         "title": "Nasdaq files for round-the-clock trading",
         "claim": "Nasdaq filed to allow 24-hour stock trading.",
         "domain": "economics", "actor": ["nasdaq"], "evidences": ["autonomous-commerce"]},
    ],
}
