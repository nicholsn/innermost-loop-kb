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
    "people": [
        {"id": "jimmy-ba", "type": "Person", "title": "Jimmy Ba", "name": "Jimmy Ba",
         "description": "Machine-learning researcher, co-author of the Adam optimizer and xAI "
                        "co-founder, who resigned in February 2026 warning that recursive "
                        "self-improvement loops would likely go live within twelve months.",
         "resource": "https://x.com/jimmybajimmyba",
         "sameAs": ["http://www.wikidata.org/entity/Q50380592"],
         "tags": ["researcher", "founder"],
         "body": "Jimmy Ba is a Canadian machine-learning researcher, known for co-authoring the "
                 "Adam optimizer, and one of the founding team of [xAI](/organizations/xai.md). "
                 "In this corpus he appears once, at the moment of his departure: [an xAI "
                 "co-founder resigns warning of live loops within a year]"
                 "(/developments/2026-02-11-xai-cofounder-resigns-warning.md), a twelve-month "
                 "horizon on recursive self-improvement delivered from inside a frontier lab."},
    ],
    "roles": [
        {"id": "jimmy-ba-xai-cofounder", "type": "Role",
         "title": "Jimmy Ba, co-founder of xAI",
         "roleName": "Co-founder",
         "memberOf": [B + "organizations/xai"],
         "holder": [B + "people/jimmy-ba"],
         "description": "The position he resigned from in February 2026 with the warning that "
                        "recursive self-improvement loops likely go live within twelve months.",
         "body": "The newsletter identifies Jimmy Ba as an xAI co-founder in the issue that "
                 "records [his resignation](/developments/2026-02-11-xai-cofounder-resigns-warning.md); "
                 "the following issue notes Musk [restructuring xAI's teams]"
                 "(/developments/2026-02-12-compute-shifts-to-realtime-video.md) after the "
                 "co-founders' exit."},
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
         "description": "A frontier-lab co-founder puts a twelve-month horizon on live loops "
                        "as he leaves, a forecast delivered on the way out rather than in a "
                        "fundraising pitch or a product launch.",
         "domain": "agents", "actor": ["xai", "people/jimmy-ba"], "score": "12 months",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-08-100pct-of-product-code"],
         "relatedTo": [B + "developments/2026-01-04-musk-enters-the-singularity",
                       B + "developments/2026-01-10-xai-used-claude-to-build-grok",
                       B + "developments/2026-02-12-compute-shifts-to-realtime-video"],
         "tags": ["rsi", "forecast"],
         "supporting_text": "\u201crecursive self-improvement loops likely go live in the next 12 months\u201d",
         "sources": [{"id": "jimmy-ba-resignation-x-post",
                      "resource": "https://x.com/jimmybajimmyba/status/2021374875793801447",
                      "title": "Jimmy Ba's resignation note from xAI (post on X)",
                      "author": "human:jimmy-ba"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Jimmy Ba, a co-founder of [xAI](/organizations/xai.md), announced his "
                 "resignation on X with the warning that recursive self-improvement loops "
                 "\u201clikely go live in the next 12 months\u201d and that 2026 would be the most "
                 "consequential year for the species "
                 "([post](https://x.com/jimmybajimmyba/status/2021374875793801447)). It lands "
                 "three days after Anthropic's [effectively-100% product code]"
                 "(/developments/2026-02-08-100pct-of-product-code.md) and five weeks after his "
                 "company's owner [declared the Singularity entered]"
                 "(/developments/2026-01-04-musk-enters-the-singularity.md); the next issue "
                 "records Musk [restructuring xAI's teams]"
                 "(/developments/2026-02-12-compute-shifts-to-realtime-video.md) after the "
                 "co-founders' exit. In the [takeoff-declared](/themes/takeoff-declared.md) "
                 "series it is a dated horizon for live loops from a frontier-lab co-founder, to "
                 "be set against the [eight-months-to-intern-researchers report]"
                 "(/developments/2026-01-09-openai-eight-months-to-intern-researchers.md) from "
                 "OpenAI a month earlier."},
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
