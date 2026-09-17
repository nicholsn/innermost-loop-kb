"""Issue 052 — 2026-02-11. The Singularity gets a date."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-11-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-11", "title": "Welcome to February 11, 2026", "url": URL,
        "thesis": "A regression puts the Singularity on a Tuesday.",
        "body": """
# Welcome to February 11, 2026

A hyperbolic regression of arXiv papers on AI emergence predicts a literal
singularity on Tuesday, July 18, 2034. The corpus has recorded declarations
since Roon on December 27; this is the first one with a weekday.

An xAI co-founder resigned the same day, warning that recursive self-improvement
loops likely go live within twelve months and that 2026 will be the most
consequential year for the species.
""",
    },
    "organizations": [
        {"id": "isomorphic-labs", "type": "Organization", "title": "Isomorphic Labs",
         "resource": "https://www.isomorphiclabs.com/"},
        {"id": "entx", "type": "Organization", "title": "entX",
         "body": "South Australian firm 3D-printing nuclear batteries."},
        {"id": "radiant-nuclear", "type": "Organization", "title": "Radiant Nuclear",
         "body": "Microreactor cleared for a full-power test at DOME."},
        {"id": "luminos", "type": "Organization", "title": "Luminos",
         "body": "Harvard spinout building a complete neuro-electronic interface."},
    ],
    "systems": [
        {"id": "isodde", "type": "AISystem", "title": "IsoDDE",
         "developed_by": [B + "organizations/isomorphic-labs"], "modality": "protein structure",
         "body": "Doubles AlphaFold 3's accuracy on protein-ligand prediction, finding binding "
                 "pockets from sequence alone."},
    ],
    "developments": [
        {"id": "2026-02-11-singularity-dated-july-18-2034",
         "title": "A regression puts the Singularity on a Tuesday in 2034",
         "claim": "A hyperbolic regression of arXiv papers on AI emergence predicts a literal "
                  "singularity on Tuesday, July 18, 2034.",
         "domain": "society", "score": "2034-07-18",
         "evidences": ["takeoff-declared"],
         "supersedes": [B + "developments/2025-12-31-asi-gap-july-2034"],
         "body": "The corpus has recorded declarations since December. This is the first with a "
                 "weekday."},
        {"id": "2026-02-11-xai-cofounder-resigns-warning",
         "title": "An xAI co-founder resigns warning of live loops within a year",
         "claim": "xAI co-founder Jimmy Ba resigned warning that recursive self-improvement "
                  "loops likely go live within twelve months and that 2026 will be the most "
                  "consequential year for the species.",
         "domain": "agents", "actor": ["xai"],
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-08-100pct-of-product-code"]},
        {"id": "2026-02-11-poetiq-55pct-hle",
         "title": "Orchestrating three labs' models takes 55% on Humanity's Last Exam",
         "claim": "Poetiq reached a state-of-the-art 55% on Humanity's Last Exam by "
                  "orchestrating Gemini, GPT and Claude together, while Unsloth released Triton "
                  "kernels enabling twelvefold faster training with 35% less VRAM.",
         "domain": "benchmarks", "actor": ["poetiq", "unsloth-ai"],
         "about": [B + "benchmarks/humanitys-last-exam"], "score": "55% / 12x",
         "evidences": ["network-over-node", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-02-06-opus-46-released"]},
        {"id": "2026-02-11-seedance-cloned-voices-from-photos",
         "title": "A model is suspended after cloning voices from photographs",
         "claim": "ByteDance suspended its Seedance 2.0 model after it reportedly cloned voices "
                  "from facial photographs alone.",
         "domain": "models", "actor": ["bytedance"],
         "evidences": ["coordination-tax", "data-beyond-text"]},
        {"id": "2026-02-11-isodde-doubles-alphafold",
         "title": "IsoDDE doubles AlphaFold 3 on protein-ligand prediction",
         "claim": "Isomorphic Labs unveiled IsoDDE, doubling AlphaFold 3's accuracy on "
                  "protein-ligand prediction and identifying binding pockets from amino acid "
                  "sequence alone.",
         "domain": "biotech", "actor": ["isomorphic-labs"], "about": [B + "systems/isodde"],
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-01-29-alphagenome"]},
        {"id": "2026-02-11-nineteen-agents-optimize-perovskite",
         "title": "Nineteen agents optimize perovskite synthesis in three and a half hours",
         "claim": "A Chinese multi-agent robot system coordinated nineteen language model "
                  "agents to optimize perovskite synthesis in three and a half hours, a task "
                  "that normally takes months.",
         "domain": "science", "actor": ["china"], "score": "3.5 hours",
         "evidences": ["automated-science", "network-over-node"],
         "supersedes": [B + "developments/2026-02-09-no-reason-to-have-grad-students-pipetting"]},
        {"id": "2026-02-11-project-vend-dress-rehearsal",
         "title": "Claude runs Anthropic's vending machines as a rehearsal for business",
         "claim": "Anthropic is running Project Vend, where Claude autonomously manages office "
                  "vending machines as a dress rehearsal for running small businesses.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["agent-economy", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-02-08-agent-outearns-minimum-wage"]},
        {"id": "2026-02-11-alphabet-32b-in-24-hours",
         "title": "Alphabet raises $32 billion of debt in a day",
         "claim": "Alphabet raised $32 billion in debt within 24 hours, the largest corporate "
                  "bond sale ever in some markets, to fund its AI buildout, while Cisco "
                  "unveiled a 102.4 Tbps switch for large clusters.",
         "domain": "economics", "actor": ["alphabet", "cisco"], "score": "$32B / 102.4 Tbps",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-10-alphabet-100-year-bond"]},
        {"id": "2026-02-11-3d-printed-nuclear-batteries",
         "title": "Nuclear batteries are 3D-printed to run for years",
         "claim": "South Australian firm entX is 3D-printing nuclear batteries that run for "
                  "years without recharging, while the DOE cleared Radiant Nuclear for the "
                  "first full-power microreactor test at DOME this summer.",
         "domain": "energy", "actor": ["entx", "radiant-nuclear", "doe"],
         "evidences": ["burning-molecules-for-tokens", "compiling-matter"]},
        {"id": "2026-02-11-dyson-swarm-design-confirmed",
         "title": "SpaceX confirms an Earth-centered Dyson Swarm design",
         "claim": "SpaceX confirmed the design of its Earth-centered Dyson Swarm with a "
                  "sun-synchronous halo and low-orbit shells, with Musk saying fission reactors "
                  "are not needed for his lunar colony, while Amazon won FCC approval for 4,500 "
                  "more satellites.",
         "domain": "space", "actor": ["spacex", "amazon", "fcc"], "score": "4,500 satellites",
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-02-10-travel-to-the-moon-for-anyone"]},
        {"id": "2026-02-11-luminos-neuro-electronic-interface",
         "title": "A Harvard spinout aims to read and write neurons over 6 mm",
         "claim": "Harvard's Adam Cohen launched Luminos to build a complete neuro-electronic "
                  "interface able to read and write to neurons across a six-millimetre field, "
                  "while the Allen Institute and Anthropic began designing custom DNA and the "
                  "Arc Institute found systemic hypoxia suppresses tumor growth.",
         "domain": "biotech", "actor": ["luminos", "allen-institute-ai", "anthropic", "arc-institute"],
         "evidences": ["hardware-grade-biology", "intimate-interface"],
         "supersedes": [B + "developments/2026-02-10-mining-parasites-for-medicine"]},
        {"id": "2026-02-11-drone-warfare-over-el-paso",
         "title": "Cartel drones are disabled over US soil",
         "claim": "The Department of War reportedly disabled Mexican cartel drones over El "
                  "Paso, marking transnational drone warfare on US soil.",
         "domain": "policy", "actor": ["war-department"],
         "evidences": ["autonomy-clock-speed", "politics-as-infrastructure"]},
        {"id": "2026-02-11-nvidia-20x-ibm-with-a-tenth-the-staff",
         "title": "Nvidia is worth 20x 1985 IBM with a tenth the employees",
         "claim": "Nvidia is now twenty times more valuable than IBM in 1985 while employing a "
                  "tenth as many people, as the US population is expected to decline for the "
                  "first time and Mark Zuckerberg joined the move to Miami with a $200 million "
                  "house.",
         "domain": "economics", "actor": ["nvidia", "meta"], "score": "20x value / 0.1x staff",
         "evidences": ["growth-without-hiring", "regulatory-exit"],
         "supersedes": [B + "developments/2026-02-09-last-chance-to-secure-employment"]},
    ],
}
