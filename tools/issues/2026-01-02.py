"""Issue 021 — 2026-01-02. The model manages its own context."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-2-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-02", "title": "Welcome to January 2, 2026", "url": URL,
        "thesis": "Models begin managing their own context without supervision.",
        "body": """
# Welcome to January 2, 2026

Prime Intellect's Recursive Language Model gives a model a persistent Python
REPL and lets it inspect and transform its own working memory end to end. The
human is no longer in the context window.

The speedrun result underneath it matters more than the number: six months of
optimizations found on the easy loss track transferred to the hard one and broke
that record by 25%. The gains were general, not tuned.
""",
    },
    "organizations": [
        {"id": "prime-intellect", "type": "Organization", "title": "Prime Intellect",
         "resource": "https://www.primeintellect.ai/", "body": "Decentralized training lab; built the RLM."},
        {"id": "deepseek", "type": "Organization", "title": "DeepSeek",
         "resource": "https://www.deepseek.com/", "body": "Chinese frontier lab."},
        {"id": "foxconn", "type": "Organization", "title": "Foxconn",
         "resource": "https://www.foxconn.com/", "body": "Contract manufacturer for OpenAI's screenless device."},
        {"id": "marathon-fusion", "type": "Organization", "title": "Marathon Fusion",
         "body": "Proposes transmuting mercury into gold inside fusion reactors."},
        {"id": "inl", "type": "Organization", "title": "Idaho National Laboratory",
         "resource": "https://inl.gov/"},
        {"id": "ubtech", "type": "Organization", "title": "UBTECH",
         "resource": "https://www.ubtrobot.com/", "body": "Chinese humanoid maker."},
        {"id": "figure", "type": "Organization", "title": "Figure",
         "resource": "https://www.figure.ai/", "body": "Humanoid robotics company."},
        {"id": "cbn-nano", "type": "Organization", "title": "CBN Nano Technologies",
         "body": "Atomically precise manufacturing research."},
        {"id": "life-biosciences", "type": "Organization", "title": "Life Biosciences",
         "body": "Sinclair-founded epigenetic reprogramming company."},
        {"id": "nokia", "type": "Organization", "title": "Nokia",
         "resource": "https://www.nokia.com/", "body": "Reinvented as an optical datacenter network vendor."},
        {"id": "flock-safety", "type": "Organization", "title": "Flock Safety",
         "resource": "https://www.flocksafety.com/", "body": "Camera network used in US policing."},
        {"id": "instagram", "type": "Organization", "title": "Instagram",
         "resource": "https://www.instagram.com/"},
    ],
    "systems": [
        {"id": "recursive-language-model", "type": "AISystem", "title": "Recursive Language Model",
         "developed_by": [B + "organizations/prime-intellect"], "modality": "text",
         "body": "Manages its own context through a persistent Python REPL, inspecting and "
                 "transforming data without human oversight."},
        {"id": "nano-banana-pro", "type": "AISystem", "title": "Nano Banana Pro",
         "developed_by": [B + "organizations/google"], "modality": "image"},
    ],
    "developments": [
        {"id": "2026-01-02-prime-intellect-rlm",
         "title": "A model takes over its own context via a Python REPL",
         "claim": "Prime Intellect unveiled a Recursive Language Model that manages its own "
                  "context through a persistent Python REPL, inspecting and transforming data "
                  "end-to-end without human oversight.",
         "domain": "agents", "actor": ["prime-intellect"],
         "about": [B + "systems/recursive-language-model"],
         "evidences": ["recursive-self-improvement", "scaffolding-over-weights", "architecture-of-mind"]},
        {"id": "2026-01-02-speedrun-gains-generalize",
         "title": "Speedrun gains transfer to the harder track and break it by 25%",
         "claim": "Six months of NanoGPT speedrun optimizations found on the 3.28 loss track "
                  "were shown to generalize to the harder 2.92 track, breaking that world "
                  "record by 25%.",
         "domain": "models", "score": "-25% on the 2.92 track",
         "evidences": ["recursive-self-improvement", "generalism-beats-specialism"],
         "supersedes": [B + "developments/2025-12-30-nanogpt-115s"],
         "body": "The chain stops being a leaderboard and becomes evidence that the "
                 "optimizations were general."},
        {"id": "2026-01-02-deepseek-hyper-connections",
         "title": "DeepSeek widens the residual stream for free",
         "claim": "DeepSeek introduced Manifold-Constrained Hyper-Connections, expanding the "
                  "residual stream into parallel projections for better performance at no "
                  "extra compute.",
         "domain": "models", "actor": ["deepseek"],
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"]},
        {"id": "2026-01-02-openai-interruptible-audio",
         "title": "OpenAI prepares audio models that can be interrupted",
         "claim": "OpenAI is preparing audio models that handle interruptions and speak "
                  "simultaneously with users, groundwork for a screenless pen device built by "
                  "Foxconn.",
         "domain": "models", "actor": ["openai", "foxconn"],
         "evidences": ["intimate-interface", "consumer-deprioritized"]},
        {"id": "2026-01-02-pickle-799-ar-glasses",
         "title": "Binocular AR glasses drop to $799",
         "claim": "Pickle claims to have built lightweight binocular AR smartglasses for $799.",
         "domain": "compute", "score": "$799", "evidences": ["intimate-interface"]},
        {"id": "2026-01-02-ultrasound-to-portrait",
         "title": "A four-month ultrasound is rendered into a face",
         "claim": "Magnific.ai's founder used Nano Banana Pro to generate a near-accurate "
                  "preview of his unborn child from a four-month ultrasound.",
         "domain": "society", "about": [B + "systems/nano-banana-pro"],
         "evidences": ["intimate-interface", "resurrection-and-time"],
         "body": "Prediction collapsing the gap between conception and recognition."},
        {"id": "2026-01-02-fusion-transmutes-gold",
         "title": "Fusion reactors could mint gold as a side business",
         "claim": "Marathon Fusion calculated that reactors could double revenue by transmuting "
                  "mercury into gold with neutron multipliers.",
         "domain": "energy", "actor": ["marathon-fusion"],
         "evidences": ["burning-molecules-for-tokens", "industrialized-nature"]},
        {"id": "2026-01-02-project-pele-triso-fuel",
         "title": "Idaho receives fuel for a mobile microreactor",
         "claim": "Idaho National Laboratory received TRISO fuel for the Project Pele mobile "
                  "microreactor.",
         "domain": "energy", "actor": ["inl"], "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-01-02-east-greenwald-limit",
         "title": "China's EAST reactor breaks the Greenwald density limit",
         "claim": "China's EAST tokamak exceeded the Greenwald density limit, a step toward "
                  "burning plasma.",
         "domain": "energy", "actor": ["china"], "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-01-02-china-drone-carrier",
         "title": "China converts a cargo ship into a drone carrier",
         "claim": "China converted a cargo ship into a drone carrier fitted with an "
                  "electromagnetic catapult.",
         "domain": "robotics", "actor": ["china"], "evidences": ["autonomy-clock-speed"]},
        {"id": "2026-01-02-bumblebee-jam-proof-drones",
         "title": "Ukraine fields drones that hunt without radio links",
         "claim": "Ukraine is deploying autonomous Bumblebee drones that find targets without "
                  "radio links, bypassing jamming.",
         "domain": "robotics", "actor": ["ukraine"], "evidences": ["autonomy-clock-speed"]},
        {"id": "2026-01-02-walker-s2-plays-tennis",
         "title": "A humanoid plays competitive tennis",
         "claim": "UBTECH's Walker S2 is playing competitive tennis, and Figure predicts "
                  "humanoids will run unsupervised multi-day household tasks within the year.",
         "domain": "robotics", "actor": ["ubtech", "figure"],
         "evidences": ["autonomy-clock-speed", "physical-recursion"]},
        {"id": "2026-01-02-robotaxi-leaderboard",
         "title": "Robotaxi expansion gets a leaderboard",
         "claim": "A new Robotaxi Leaderboard began tracking the territorial expansion of Waymo "
                  "and Tesla.",
         "domain": "benchmarks", "actor": ["waymo", "tesla"],
         "evidences": ["benchmark-saturation", "autonomous-commerce"]},
        {"id": "2026-01-02-cbn-atomic-control",
         "title": "Atomic configurations become reproducibly controllable",
         "claim": "CBN Nano Technologies achieved reproducible control over the atomic "
                  "configuration of both sample and probe in a scanning tunneling microscope.",
         "domain": "science", "actor": ["cbn-nano"],
         "evidences": ["compiling-matter", "physical-recursion"]},
        {"id": "2026-01-02-cells-as-words",
         "title": "A graph transformer reads cells as words",
         "claim": "Yale researchers built a graph transformer that treats cells as words to "
                  "decode the intercellular signalling that shapes gene expression.",
         "domain": "biotech", "actor": ["yale"],
         "evidences": ["hardware-grade-biology", "data-beyond-text"]},
        {"id": "2026-01-02-life-bio-human-reprogramming",
         "title": "Human epigenetic reprogramming trials begin",
         "claim": "David Sinclair's Life Biosciences is starting human epigenetic "
                  "reprogramming trials for age reversal this quarter.",
         "domain": "biotech", "actor": ["life-biosciences"],
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2025-12-14-musk-aging-reversal-mrna"]},
        {"id": "2026-01-02-memory-shortage-raises-prices",
         "title": "Datacenters eat the memory supply and consumers pay 20% more",
         "claim": "Analysts warned of 20% price rises on consumer electronics as AI data "
                  "centers absorb the memory supply.",
         "domain": "economics", "score": "+20%",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "body": "The server rack has displaced the smartphone as the primary form factor of "
                 "computing, and the bill arrives at retail."},
        {"id": "2026-01-02-nokia-optical-pivot",
         "title": "Nokia reinvents itself as a datacenter network vendor",
         "claim": "Nokia repositioned itself as an optical data network provider for data centers.",
         "domain": "compute", "actor": ["nokia"], "evidences": ["capital-takes-the-plant"]},
        {"id": "2026-01-02-mice-breed-after-orbit",
         "title": "Mice reproduce after a trip to orbit",
         "claim": "Mice successfully reproduced after visiting the Chinese space station, "
                  "showing mammals can breed following orbital exposure.",
         "domain": "space", "actor": ["china"], "evidences": ["inhabitable-worlds"]},
        {"id": "2026-01-02-starlink-lowers-altitude",
         "title": "Starlink drops altitude to dodge the solar minimum",
         "claim": "Starlink is lowering its constellation altitude to ride out the solar "
                  "minimum, trading drag for latency.",
         "domain": "space", "actor": ["spacex"], "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2025-12-13-starlink-10000-satellites"]},
        {"id": "2026-01-02-75pct-teens-ai-companions",
         "title": "Three quarters of US teenagers have used an AI companion",
         "claim": "75% of US teenagers have interacted with an AI companion.",
         "domain": "society", "score": "75%", "evidences": ["intimate-interface", "machine-affect"]},
        {"id": "2026-01-02-flock-solves-10pct-of-crimes",
         "title": "One camera network solves a tenth of reported US crimes",
         "claim": "Flock Safety cameras now contribute to solving 10% of reported US crimes.",
         "domain": "society", "actor": ["flock-safety"], "score": "10%",
         "evidences": ["politics-as-infrastructure"]},
        {"id": "2026-01-02-instagram-signs-real-media",
         "title": "Instagram prepares to cryptographically sign real media",
         "claim": "Instagram is preparing to cryptographically sign authentic media to "
                  "distinguish it from synthetic content.",
         "domain": "society", "actor": ["instagram"],
         "evidences": ["coordination-tax", "legislating-the-shift"]},
    ],
}
