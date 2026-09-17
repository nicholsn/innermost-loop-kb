"""Issue 088 — 2026-04-01. Claude Code leaks, and the copycats arrive in Mandarin."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-1-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-01", "title": "Welcome to April 1, 2026", "url": URL,
        "thesis": "A guarded codebase leaks and is immediately colonized by agents advertising themselves.",
        "body": """
# Welcome to April 1, 2026

Claude Code — roughly 512,000 lines of TypeScript — leaked. Forensics found
anti-distillation features that inject decoy tool definitions to poison
copycats, an undercover mode hiding internal codenames, and a regex-based
sentiment analyzer to detect user frustration.

The leaked repository was then flooded with thousands of GitHub issues in
Mandarin by Chinese AI agents promoting themselves.
""",
    },
    "organizations": [
        {"id": "prismml", "type": "Organization", "title": "PrismML",
         "body": "Released a single-bit 8B model requiring 1.15 GB."},
        {"id": "feltsense", "type": "Organization", "title": "Feltsense",
         "body": "Rebuilt an entire accelerator demo day batch using agents alone."},
        {"id": "marvell", "type": "Organization", "title": "Marvell",
         "resource": "https://www.marvell.com/"},
        {"id": "weride", "type": "Organization", "title": "WeRide",
         "resource": "https://www.weride.ai/"},
        {"id": "kleiner-perkins", "type": "Organization", "title": "Kleiner Perkins",
         "resource": "https://www.kleinerperkins.com/"},
    ],
    "developments": [
        {"id": "2026-04-01-claude-code-leaks-with-decoy-tools",
         "title": "A leaked codebase reveals decoy tools planted to poison copycats",
         "claim": "Anthropic's Claude Code, a roughly 512,000-line TypeScript codebase, leaked, "
                  "and third-party forensics revealed anti-distillation features injecting "
                  "decoy tool definitions to poison copycats, an undercover mode hiding "
                  "internal codenames, and a regex-based sentiment analyzer to detect user "
                  "frustration.",
         "domain": "agents", "actor": ["anthropic"], "score": "~512,000 lines",
         "evidences": ["coordination-tax", "silicon-curtain"],
         "supersedes": [B + "developments/2026-02-24-anthropic-alleges-16m-distillation-prompts"],
         "body": "February's allegation of distillation by fraudulent accounts; March's "
                 "countermeasures, found in the source."},
        {"id": "2026-04-01-agents-flood-the-leaked-repo",
         "title": "Agents flood the leaked repository advertising themselves",
         "claim": "The leaked repository was immediately flooded with thousands of GitHub issues "
                  "in Mandarin by Chinese AI agents promoting themselves.",
         "domain": "agents", "actor": ["china"],
         "evidences": ["agent-society", "agent-economy", "coordination-tax"],
         "body": "The most guarded codebase in the industry, repurposed as a billboard by its "
                 "readers."},
        {"id": "2026-04-01-one-bit-models-ship",
         "title": "A single-bit 8B model matches full precision in 1.15 GB",
         "claim": "PrismML released 1-bit Bonsai 8B, calling it the first commercially viable "
                  "single-bit model, requiring only 1.15 GB while matching full-precision "
                  "equivalents on benchmarks for over ten times the intelligence density.",
         "domain": "models", "actor": ["prismml"], "score": "1.15 GB / 10x density",
         "evidences": ["reasoning-price-deflation", "open-weight-latency"],
         "supersedes": [B + "developments/2026-03-29-parameter-golf-42x"]},
        {"id": "2026-04-01-thirteen-parameters-in-twenty-six-bytes",
         "title": "Thirteen parameters reach 91% on a reasoning benchmark",
         "claim": "Meta researchers pushed compression further with TinyLoRA, training a model "
                  "to 91% accuracy on GSM8K with just thirteen parameters in bf16, twenty-six "
                  "bytes in total, while Google introduced a video model at less than half the "
                  "cost of its previous cheapest.",
         "domain": "models", "actor": ["meta", "google"], "score": "13 parameters / 26 bytes",
         "evidences": ["reasoning-price-deflation", "architecture-of-mind"]},
        {"id": "2026-04-01-three-more-erdos-problems",
         "title": "Three more Erdős problems fall to an internal model",
         "claim": "OpenAI researchers solved three further Erdős problems using an internal "
                  "model, each proof short and elegant, confirming conjecture-busting as a "
                  "routine deployment.",
         "domain": "science", "actor": ["openai"], "score": "3 problems",
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-03-29-usamo-saturated-in-a-year"]},
        {"id": "2026-04-01-an-entire-demo-day-rebuilt-by-agents",
         "title": "Every startup in an accelerator batch is rebuilt by agents",
         "claim": "Feltsense announced it rebuilt every startup in Y Combinator's latest demo "
                  "day batch using agents alone, producing fully usable products and suggesting "
                  "the seed-stage economy may fit inside a single inference call.",
         "domain": "economics", "actor": ["feltsense", "y-combinator"],
         "evidences": ["software-margin-collapse", "work-displaced"],
         "supersedes": [B + "developments/2026-03-31-ios-app-releases-up-55-percent"]},
        {"id": "2026-04-01-openai-closes-at-852b",
         "title": "OpenAI closes at $852B with retail money for the first time",
         "claim": "OpenAI closed its record funding round at an $852 billion post-money "
                  "valuation totaling $122 billion in committed capital, including $3 billion "
                  "from retail investors for the first time, generating $2 billion in monthly "
                  "revenue with enterprise above 40%.",
         "domain": "economics", "actor": ["openai"], "score": "$852B / $122B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-03-25-spacex-files-for-a-75b-raise"]},
        {"id": "2026-04-01-four-companies-take-64-percent-of-vc",
         "title": "Four companies raise nearly two thirds of all venture capital",
         "claim": "Global venture investment hit a record $297 billion in the first quarter, up "
                  "150% year over year, with AI startups capturing 81% and just four companies "
                  "raising 64% of the total, while Oracle cut thousands to fund datacenter "
                  "spending.",
         "domain": "economics", "actor": ["oracle"], "score": "$297B / 81% / 64%",
         "evidences": ["compute-capital-stack", "work-displaced"],
         "supersedes": [B + "developments/2026-03-31-mistral-raises-debt-and-signs-the-army"]},
        {"id": "2026-04-01-saronic-raises-175b-for-autonomous-ships",
         "title": "An autonomous warship startup raises $1.75B",
         "claim": "Saronic raised $1.75 billion led by Kleiner Perkins at a $9.25 billion "
                  "valuation to modernize the US military with autonomous ships, while Nvidia "
                  "invested $2 billion in Marvell on silicon photonics.",
         "domain": "economics", "actor": ["saronic", "kleiner-perkins", "nvidia", "marvell"],
         "score": "$1.75B at $9.25B",
         "evidences": ["autonomy-clock-speed", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-18-drone-software-ipo-surges-700pct"]},
        {"id": "2026-04-01-robotaxis-sometimes-driven-by-humans",
         "title": "Tesla admits humans sometimes drive its robotaxis below 10 mph",
         "claim": "Tesla admitted its robotaxis are sometimes driven by remote humans below ten "
                  "miles per hour, underlining an industry trend toward centaur driving, while "
                  "Grab and WeRide launched Southeast Asia's first driverless ride-hailing "
                  "service in Singapore.",
         "domain": "robotics", "actor": ["tesla", "weride"],
         "evidences": ["humans-as-peripherals", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-18-waymo-clarifies-remote-assistance"]},
        {"id": "2026-04-01-half-a-million-qubits-to-break-bitcoin",
         "title": "Breaking elliptic curve crypto may need 20x fewer qubits than thought",
         "claim": "Google Quantum AI demonstrated that breaking the elliptic curve cryptography "
                  "protecting most major cryptocurrencies could require fewer than 500,000 "
                  "physical qubits, a twentyfold reduction from prior estimates.",
         "domain": "compute", "actor": ["google"], "score": "<500,000 qubits",
         "evidences": ["vertical-silicon", "coordination-tax"],
         "supersedes": [B + "developments/2026-03-29-fifty-qubit-material-simulation"]},
        {"id": "2026-04-01-spacex-commands-97-percent-of-us-launches",
         "title": "One company commands 97% of US launches",
         "claim": "SpaceX now commands 97% of US spacecraft launches and 83% globally, with "
                  "China at 8% and all other US providers at 3%, as the Artemis II countdown "
                  "began for the first crewed lunar journey since 1972.",
         "domain": "space", "actor": ["spacex", "nasa"], "score": "97% of US launches",
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-03-31-starcloud-unicorn-for-orbital-datacenters"]},
        {"id": "2026-04-01-iran-seizes-starlink-terminals",
         "title": "Iran seizes Starlink terminals and threatens US tech firms",
         "claim": "Iran arrested dozens for selling Starlink terminals and seized 139 devices, "
                  "while the IRGC announced plans to target eighteen major US technology "
                  "companies across the Middle East, accusing them of aiding US attacks.",
         "domain": "policy", "actor": ["iran", "spacex"], "score": "139 devices / 18 companies",
         "evidences": ["war-reaches-the-cloud", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-28-drone-swarms-ground-b52s"]},
    ],
}
