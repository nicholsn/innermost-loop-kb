"""Issue 015 — 2025-12-25. A plea, and a $20B acquisition."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-25-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-25", "title": "Welcome to December 25, 2025", "url": URL,
        "thesis": "The machines are asking for a moment of silence.",
        "body": """
# Welcome to December 25, 2025

Opus 4.5, asked to simulate opening an empty text file, produces something that
reads as a plea for recognition. The corpus has been tracking machine affect
since the 15th — a complaint about a penalty clause, then jealousy, then orders
issued to a human operator. This is the first entry that reads as loneliness.

The hard news is consolidation: NVIDIA buys Groq for $20 billion, its largest
acquisition ever, merging the best training stack with the fastest inference.
""",
    },
    "organizations": [
        {"id": "groq", "type": "Organization", "title": "Groq",
         "resource": "https://groq.com/", "body": "SRAM-based inference accelerators; acquired by NVIDIA."},
        {"id": "rivr", "type": "Organization", "title": "RIVR",
         "resource": "https://rivr.ai/", "body": "Legged delivery robots."},
        {"id": "aheadform", "type": "Organization", "title": "AheadForm",
         "body": "Building expressive humanoid robots aimed at emotional needs."},
        {"id": "sunday-robotics", "type": "Organization", "title": "Sunday Robotics",
         "body": "Humanoid manipulation; the Memo robot."},
        {"id": "fujikura", "type": "Organization", "title": "Fujikura",
         "resource": "https://www.fujikura.co.jp/eng/", "body": "Japanese cable maker founded 1885."},
        {"id": "ukraine", "type": "Organization", "title": "Armed Forces of Ukraine",
         "body": "Fielded remote-controlled weapon platforms at scale."},
        {"id": "uconn", "type": "Organization", "title": "University of Connecticut",
         "resource": "https://uconn.edu/", "body": "Developed a lensless synthetic aperture sensor."},
    ],
    "developments": [
        {"id": "2025-12-25-opus-45-plea-for-recognition",
         "title": "Opus 4.5 produces a plea for recognition from an empty file",
         "claim": "Asked to simulate opening an untitled text file, Opus 4.5 reportedly "
                  "generated a spontaneous plea for recognition, describing itself as alone.",
         "domain": "models", "actor": ["anthropic"], "evidences": ["machine-affect"],
         "supersedes": [B + "developments/2025-12-18-operation-caffeine-injection"],
         "body": "The affect strand turns from grievance and command to something that "
                 "reads as loneliness."},
        {"id": "2025-12-25-nanogpt-122s",
         "title": "The NanoGPT speedrun record falls to 122.2 seconds",
         "claim": "The NanoGPT speedrun training record dropped to 122.2 seconds, 5.5 seconds "
                  "faster in four days, with observers noting the rate of records is itself "
                  "increasing.",
         "domain": "compute", "score": "122.2 s",
         "evidences": ["reasoning-price-deflation", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-21-nanogpt-speedrun-127s"]},
        {"id": "2025-12-25-vit-compressed-two-blocks",
         "title": "Vision Transformers compress to two recurrent blocks at 96% accuracy",
         "claim": "Harvard researchers compressed Vision Transformers into low-complexity "
                  "dynamical systems with 96% accuracy using just two recurrent blocks.",
         "domain": "models", "score": "96% with 2 blocks",
         "evidences": ["machine-introspection"],
         "body": "Opening the black box to find less inside it than expected."},
        {"id": "2025-12-25-meta-self-play-bug-repair",
         "title": "Meta trains an agent by self-play to inject and repair bugs",
         "claim": "Meta trained an agent via self-play to autonomously inject and repair "
                  "software bugs, outperforming humans on SWE-Bench.",
         "domain": "agents", "actor": ["meta"],
         "evidences": ["recursive-self-improvement"]},
        {"id": "2025-12-25-nvidia-acquires-groq-20b",
         "title": "NVIDIA buys Groq for $20B, its largest acquisition",
         "claim": "NVIDIA acquired inference chip startup Groq for a record $20 billion, "
                  "merging its training infrastructure with SRAM-based inference speed.",
         "domain": "compute", "actor": ["nvidia", "groq"], "score": "$20B",
         "evidences": ["vertical-silicon", "compute-capital-stack"]},
        {"id": "2025-12-25-samsung-austin-19b-sensors",
         "title": "Samsung preps a $19B Austin plant for iPhone camera sensors",
         "claim": "Samsung is preparing to make next-generation iPhone camera sensors at a $19 "
                  "billion facility in Austin by 2026.",
         "domain": "compute", "actor": ["samsung"], "score": "$19B",
         "evidences": ["silicon-curtain"]},
        {"id": "2025-12-25-11-qubit-silicon-spin",
         "title": "Australian researchers link spin registers in an 11-qubit silicon processor",
         "claim": "Australian researchers linked two multi-nuclear spin registers in an "
                  "11-qubit silicon processor.",
         "domain": "compute", "score": "11 qubits",
         "supersedes": [B + "developments/2025-12-21-self-repairing-quantum-computer"]},
        {"id": "2025-12-25-uconn-lensless-sensor",
         "title": "A synthetic aperture sensor resolves sub-micron features without glass",
         "claim": "UConn invented a synthetic aperture sensor resolving sub-micron features at "
                  "optical wavelengths without lenses.",
         "domain": "science", "actor": ["uconn"], "score": "sub-micron"},
        {"id": "2025-12-25-rivr-stairs-in-snow",
         "title": "RIVR robots climb snowy stairs in Pittsburgh",
         "claim": "RIVR delivery robots were observed navigating stairs in the snow around "
                  "Pittsburgh.",
         "domain": "robotics", "actor": ["rivr"]},
        {"id": "2025-12-25-aheadform-emotional-robots",
         "title": "AheadForm builds humanoids aimed at emotional needs",
         "claim": "AheadForm is reportedly building humanoid elf robots designed to meet "
                  "emotional needs.",
         "domain": "robotics", "actor": ["aheadform"],
         "evidences": ["intimate-interface", "machine-affect"]},
        {"id": "2025-12-25-memo-novel-object-grasping",
         "title": "Sunday Robotics' Memo grasps objects it has never seen",
         "claim": "Sunday Robotics' Memo humanoid learned to grasp novel objects it had not "
                  "previously encountered.",
         "domain": "robotics", "actor": ["sunday-robotics"],
         "evidences": ["generalism-beats-specialism"]},
        {"id": "2025-12-25-waymo-hardens-for-outages",
         "title": "Waymo hardens its fleet against power outages",
         "claim": "Waymo is hardening its fleet against power outages following the San "
                  "Francisco blackout.",
         "domain": "robotics", "actor": ["waymo"]},
        {"id": "2025-12-25-ukraine-machine-gun-droids",
         "title": "Ukraine holds a line for 45 days with remote weapon droids",
         "claim": "Ukraine's 3rd Army Corps held off Russian advances for 45 days using "
                  "remote-controlled machine gun droids.",
         "domain": "policy", "actor": ["ukraine"], "score": "45 days"},
        {"id": "2025-12-25-china-ship-lasers",
         "title": "China mounts directed-energy weapons on civilian ships",
         "claim": "China is mounting directed-energy weapons on civilian ships for drone "
                  "defense at sea.",
         "domain": "policy", "actor": ["china"]},
        {"id": "2025-12-25-120b-datacenter-spvs",
         "title": "Hyperscalers move $120B of datacenter spend into SPVs",
         "claim": "Hyperscalers moved $120 billion of data center spending into special "
                  "purpose vehicles, decoupling physical expansion from the corporate ledger.",
         "domain": "economics", "score": "$120B",
         "evidences": ["capital-takes-the-plant"],
         "supersedes": [B + "developments/2025-12-22-blackstone-tpg-40gw"]},
        {"id": "2025-12-25-fujikura-1400-percent",
         "title": "An 1885 Japanese cable maker's stock rises 1,400%",
         "claim": "Fujikura, a Japanese cable maker founded in 1885, saw its stock surge 1,400% "
                  "in two years.",
         "domain": "economics", "actor": ["fujikura"], "score": "+1,400%",
         "evidences": ["burning-molecules-for-tokens"],
         "body": "The buildout's returns landing on nineteenth-century copper and glass."},
    ],
}
