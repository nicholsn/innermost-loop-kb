"""Issue 022 — 2026-01-03. The datacenter becomes a sovereign."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-3-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-03", "title": "Welcome to January 3, 2026", "url": URL,
        "thesis": "Compute stops renting and starts governing itself.",
        "body": """
# Welcome to January 3, 2026

Anthropic buys a million TPUs straight from Broadcom and hands the physical
operations to crypto-miners, skipping the cloud providers entirely. A Bloom
survey finds 38% of data centers expect to generate their own power by 2030.
The pattern is the same twice: the compute layer acquiring the attributes of a
state — its own silicon, its own grid, its own territory.

Elsewhere the efficiency story gets a rare gift: Apple shows hyperparameter
sweeps are scale-invariant, so settings found on toys transfer to real models.
""",
    },
    "organizations": [
        {"id": "terawulf", "type": "Organization", "title": "TeraWulf",
         "resource": "https://www.terawulf.com/", "body": "Bitcoin miner turned AI datacenter operator."},
        {"id": "princeton", "type": "Organization", "title": "Princeton University",
         "resource": "https://www.princeton.edu/"},
        {"id": "bloom-energy", "type": "Organization", "title": "Bloom Energy",
         "resource": "https://www.bloomenergy.com/", "body": "Fuel cell maker; surveyed datacenter self-generation."},
        {"id": "kioxia", "type": "Organization", "title": "Kioxia",
         "resource": "https://www.kioxia.com/", "body": "NAND flash manufacturer."},
        {"id": "flocean", "type": "Organization", "title": "Flocean",
         "body": "Subsea desalination at 600 m depth."},
        {"id": "crick-institute", "type": "Organization", "title": "Francis Crick Institute",
         "resource": "https://www.crick.ac.uk/"},
        {"id": "novo-nordisk", "type": "Organization", "title": "Novo Nordisk",
         "resource": "https://www.novonordisk.com/"},
        {"id": "baidu", "type": "Organization", "title": "Baidu",
         "resource": "https://www.baidu.com/", "body": "Chinese robotaxi and model developer."},
        {"id": "zipline", "type": "Organization", "title": "Zipline",
         "resource": "https://www.flyzipline.com/", "body": "Delivery drone operator."},
    ],
    "systems": [
        {"id": "diffthinker", "type": "AISystem", "title": "DiffThinker", "modality": "image",
         "body": "Treats logical reasoning as image-to-image diffusion, beating GPT-5 on "
                 "logic tasks."},
        {"id": "optimus", "type": "AISystem", "title": "Tesla Optimus",
         "description": "Tesla's humanoid robot, reported in the corpus walking office perimeters "
                        "and sorting Legos as robotics enters its mundane-utility phase.",
         "developed_by": [B + "organizations/tesla"], "modality": "robotic control",
         "resource": "https://www.tesla.com/AI",
         "sameAs": ["http://www.wikidata.org/entity/Q108167797"],
         "body": "Optimus is [Tesla](/organizations/tesla.md)'s humanoid robot. It enters this corpus in "
                 "the January 3, 2026 issue, [walking the perimeter of Palo Alto offices and sorting "
                 "Legos](/developments/2026-01-03-optimus-patrols-and-sorts.md), the newsletter's example "
                 "of robotics reaching the mundane-utility phase that precedes ubiquity and its proof that "
                 "dexterity is a data problem. It is also a lateral reference for "
                 "[CATL's humanoid deployment on battery lines](/developments/2025-12-20-catl-humanoid-battery-lines.md), "
                 "the corpus's physical-recursion entry, and a comparator for XPENG's "
                 "[IRON](/systems/xpeng-iron.md) in the September 15 issue."},
    ],
    "developments": [
        {"id": "2026-01-03-apple-scale-invariant-sweeps",
         "title": "Hyperparameter sweeps turn out to be scale-invariant",
         "claim": "Apple researchers showed hyperparameter settings found on 50M-parameter "
                  "models transfer intact to 7B-plus models, eliminating the tuning tax of "
                  "large-scale training.",
         "domain": "models", "actor": ["apple"],
         "evidences": ["reasoning-price-deflation", "generalism-beats-specialism"]},
        {"id": "2026-01-03-princeton-deep-delta-learning",
         "title": "Princeton reframes the residual stream as a geometric flow",
         "claim": "Princeton introduced Deep Delta Learning, treating the transformer residual "
                  "stream as a continuous flow that cleans its own feature subspaces layer by "
                  "layer.",
         "domain": "models", "actor": ["princeton"], "evidences": ["architecture-of-mind"],
         "supersedes": [B + "developments/2026-01-02-deepseek-hyper-connections"]},
        {"id": "2026-01-03-diffthinker-reasoning-as-images",
         "title": "Reasoning as diffusion beats GPT-5 on logic",
         "claim": "Chinese researchers unveiled DiffThinker, which outperforms GPT-5 by "
                  "treating logical reasoning as an image-to-image diffusion task.",
         "domain": "models", "about": [B + "systems/diffthinker"],
         "evidences": ["architecture-of-mind", "data-beyond-text"],
         "body": "An argument that high-level cognition is spatial planning at high resolution."},
        {"id": "2026-01-03-anthropic-1m-tpus-direct",
         "title": "Anthropic buys a million TPUs and skips the cloud",
         "claim": "Anthropic is purchasing one million TPUv7 chips directly from Broadcom and "
                  "outsourcing physical operations to crypto-miners such as TeraWulf, building "
                  "a vertically integrated compute silo.",
         "domain": "compute", "actor": ["anthropic", "broadcom", "terawulf"], "score": "1M TPUv7",
         "evidences": ["vertical-silicon", "compute-capital-stack", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2025-12-12-broadcom-anthropic-tpu-order"]},
        {"id": "2026-01-03-38pct-datacenters-self-generate",
         "title": "38% of datacenters expect to make their own power",
         "claim": "A Bloom Energy survey found 38% of data centers expect to generate their own "
                  "power by 2030, decoupling from the public grid.",
         "domain": "energy", "actor": ["bloom-energy"], "score": "38% by 2030",
         "evidences": ["burning-molecules-for-tokens", "politics-as-infrastructure"],
         "body": "Server farms as islanded city-states."},
        {"id": "2026-01-03-tsmc-revenue-doubles-kioxia-540",
         "title": "TSMC revenue doubles and Kioxia rises 540%",
         "claim": "TSMC's revenue doubled and Kioxia's stock rose 540% as demand for NAND flash "
                  "to store synthetic data outran supply.",
         "domain": "economics", "actor": ["tsmc", "kioxia"], "score": "+540%",
         "evidences": ["compute-capital-stack", "consumer-deprioritized"]},
        {"id": "2026-01-03-china-algae-great-green-wall",
         "title": "China crusts the desert with engineered algae",
         "claim": "China is deploying bio-engineered blue-green algae to crust over 6,667 "
                  "hectares of desert, using microbes as terraforming agents.",
         "domain": "science", "actor": ["china"], "score": "6,667 hectares",
         "evidences": ["industrialized-nature", "biosphere-uplift"]},
        {"id": "2026-01-03-flocean-subsea-desalination",
         "title": "The first commercial subsea desalination plant launches",
         "claim": "Flocean is launching commercial desalination 600 metres below the North Sea, "
                  "using hydrostatic pressure to halve energy use.",
         "domain": "energy", "actor": ["flocean"], "score": "-50% energy",
         "evidences": ["industrialized-nature"]},
        {"id": "2026-01-03-globalbuildingatlas-97pct",
         "title": "97% of Earth's buildings are mapped in 3D",
         "claim": "The GlobalBuildingAtlas mapped 97% of Earth's structures in 3D, producing a "
                  "2.75-billion-building digital twin.",
         "domain": "science", "score": "2.75B buildings",
         "evidences": ["data-beyond-text", "physical-recursion"]},
        {"id": "2026-01-03-mri-guided-microrobots",
         "title": "MRI steers microrobots through blood vessels in 30 ms",
         "claim": "Researchers built magnetic microrobots guided by real-time MRI that navigate "
                  "the vascular system with 30-millisecond precision.",
         "domain": "biotech", "score": "30 ms", "evidences": ["hardware-grade-biology"]},
        {"id": "2026-01-03-crick-lung-on-chip",
         "title": "A donor's own lung is grown on a chip to test their treatment",
         "claim": "The Francis Crick Institute grew a lung-on-chip from a single donor's stem "
                  "cells to test personalized tuberculosis treatments.",
         "domain": "biotech", "actor": ["crick-institute"],
         "evidences": ["hardware-grade-biology", "automated-science"]},
        {"id": "2026-01-03-evoke-failure-reframes-alzheimers",
         "title": "A failed trial reframes Alzheimer's as metabolic",
         "claim": "The failure of Novo Nordisk's EVOKE trial redirected GLP-1 Alzheimer's work "
                  "toward combination therapies treating dementia as a metabolic disorder.",
         "domain": "biotech", "actor": ["novo-nordisk"], "evidences": ["discovery-as-process"]},
        {"id": "2026-01-03-optimus-patrols-and-sorts",
         "title": "Optimus walks the perimeter and sorts Legos",
         "claim": "Tesla's Optimus is patrolling Palo Alto office perimeters and sorting Legos.",
         "domain": "robotics", "actor": ["tesla"], "about": [B + "systems/optimus"],
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "body": "Mundane utility is the phase before ubiquity."},
        {"id": "2026-01-03-london-waymo-baidu-head-to-head",
         "title": "London becomes the US-China autonomy testbed",
         "claim": "London is hosting both Waymo and Baidu robotaxis, putting US and Chinese "
                  "autonomy stacks head to head in one city.",
         "domain": "robotics", "actor": ["waymo", "baidu"],
         "evidences": ["silicon-curtain", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-02-robotaxi-leaderboard"]},
        {"id": "2026-01-03-zipline-delivers-to-pastures",
         "title": "Delivery drones lower packages into pastures",
         "claim": "Zipline drones are lowering packages directly into pastures.",
         "domain": "robotics", "actor": ["zipline"], "evidences": ["autonomous-commerce"]},
        {"id": "2026-01-03-artemis-ii-february-6",
         "title": "Artemis II gets a February 6 launch window",
         "claim": "NASA confirmed the Artemis II launch window opens February 6, sending "
                  "astronauts around the Moon for the first time in over fifty years.",
         "domain": "space", "actor": ["nasa"], "occurred_on": "2026-01-03",
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2025-12-19-artemis-ii-months-away"]},
    ],
}
