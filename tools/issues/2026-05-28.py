"""Issue 126 — 2026-05-28. The practice-run phase."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-28-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-28", "title": "Welcome to May 28, 2026", "url": URL,
        "thesis": "The agentic era is recast as a warm-up lap.",
        "body": """
# Welcome to May 28, 2026

Demis Hassabis expects AGI around 2030, now sees 2029 as plausible, and
considers 2026's agentic era a warm-up lap. The benchmarks agree: DeepSWE
arrives with contamination-free repos and hand-written behavioral verifiers.

Axiom quietly published eight AI-authored papers to arXiv, five already
accepted at peer-reviewed journals.
""",
    },
    "organizations": [
        {"id": "datacurve", "type": "Organization", "title": "Datacurve"},
        {"id": "axiom-math", "type": "Organization", "title": "Axiom",
         "body": "AI mathematics lab; publishes AxiomProver papers to arXiv."},
        {"id": "buspatrol", "type": "Organization", "title": "BusPatrol"},
        {"id": "robinhood", "type": "Organization", "title": "Robinhood"},
        {"id": "nvision", "type": "Organization", "title": "NVision",
         "body": "German quantum sensing company."},
        {"id": "lombardy", "type": "Organization", "title": "Lombardy",
         "body": "Italian region; hiked datacenter construction fees in green zones."},
        {"id": "american-airlines", "type": "Organization", "title": "American Airlines"},
        {"id": "illinois", "type": "Organization", "title": "Illinois"},
        {"id": "amazon-mgm", "type": "Organization", "title": "Amazon MGM Studios"},
    ],
    "developments": [
        {"id": "2026-05-28-the-agentic-era-is-a-warm-up-lap",
         "title": "A lab chief calls the agentic era a warm-up lap",
         "claim": "Demis Hassabis said he expects AGI around 2030, now sees 2029 as plausible, "
                  "and considers 2026's agentic era a warm-up lap.",
         "domain": "models", "actor": ["google-deepmind"], "score": "2029-2030",
         "evidences": ["takeoff-declared", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-05-15-two-versions-of-2028"]},
        {"id": "2026-05-28-a-contamination-free-software-benchmark",
         "title": "A software benchmark ships contamination-free repos and behavioral verifiers",
         "claim": "Datacurve launched DeepSWE, a long-horizon software engineering benchmark "
                  "with 91 contamination-free repos across 5 languages, solutions 5.5 times "
                  "denser than SWE-bench Pro, and hand-written behavioral verifiers.",
         "domain": "benchmarks", "actor": ["datacurve"], "score": "91 repos / 5.5x density",
         "evidences": ["benchmark-saturation", "models-audit-their-benchmarks"],
         "supersedes": [B + "developments/2026-05-25-a-benchmark-of-twenty-three-real-saas-systems"]},
        {"id": "2026-05-28-a-world-model-of-protein-biology",
         "title": "A world model of protein biology is released",
         "claim": "The Chan Zuckerberg Biohub released a world model of protein biology built "
                  "on ESMC, a language model trained on 2.8 billion sequences from across all "
                  "of life, plus ESMFold2 for atomic structures and an ESM Atlas mapping 6.8 "
                  "billion proteins.",
         "domain": "biotech", "actor": ["czi"], "score": "2.8B sequences / 6.8B proteins",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-05-11-a-foundation-model-for-alzheimers-prevention"]},
        {"id": "2026-05-28-eight-ai-papers-five-accepted",
         "title": "Eight AI-authored papers appear on arXiv, five already accepted",
         "claim": "Axiom revealed that eight AxiomProver papers have quietly appeared on arXiv "
                  "since February, with five already accepted at peer-reviewed journals, "
                  "including proofs that 100% of primes are partially regular and that "
                  "Ramanujan's tau misses 100% of primes.",
         "domain": "science", "actor": ["axiom-math"], "score": "8 papers / 5 accepted",
         "evidences": ["automated-science", "proof-priced-per-unit", "root-node-problems"],
         "supersedes": [B + "developments/2026-05-24-nine-more-erdos-problems-at-a-few-hundred-dollars-each"]},
        {"id": "2026-05-28-cve-issuance-hits-thirteen-a-day",
         "title": "AI bug-finders push kernel CVE issuance to thirteen a day",
         "claim": "AI bug-finders surfaced new Linux vulnerability classes and pushed CVE "
                  "issuance to what a stable kernel maintainer called thirteen a day, prompting "
                  "him to open Rust Week with the claim that Rust is going to save us from "
                  "untrusted data.",
         "domain": "compute", "score": "13 CVEs/day",
         "evidences": ["risk-becomes-uninsurable", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-05-24-ten-thousand-critical-vulnerabilities-surfaced"]},
        {"id": "2026-05-28-school-bus-cameras-become-plate-readers",
         "title": "School bus AI cameras are converted into police plate readers",
         "claim": "BusPatrol, which installed AI cameras on tens of thousands of US school "
                  "buses, plans to convert them into automatic license plate readers and hand "
                  "the data to police.",
         "domain": "society", "actor": ["buspatrol"],
         "evidences": ["politics-as-infrastructure", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-05-24-an-agency-suspends-its-public-database"]},
        {"id": "2026-05-28-a-brokerage-opens-to-agents",
         "title": "A brokerage opens trading and credit decisions to agents",
         "claim": "Robinhood opened to agents, letting customers hand trading and credit-card "
                  "decisions to AI over MCP.",
         "domain": "agents", "actor": ["robinhood"],
         "evidences": ["autonomous-commerce", "agent-economy"],
         "supersedes": [B + "developments/2026-05-20-agents-transact-while-devices-are-off"]},
        {"id": "2026-05-28-atoms-placed-on-demand",
         "title": "Atoms gain simultaneous spatial and chemical control",
         "claim": "CBN Nano Technologies achieved the first simultaneous spatial and chemical "
                  "control over mechanosynthetic carbon fabrication using an inverted-mode "
                  "scanning tunneling microscope, moving diamondoid mechanosynthesis a notch "
                  "closer to practice.",
         "domain": "science", "actor": ["cbn-nano"],
         "evidences": ["compiling-matter"],
         "supersedes": [B + "developments/2026-05-14-drugs-crystallized-in-microgravity"]},
        {"id": "2026-05-28-an-arm-chip-outscores-x86",
         "title": "An ARM server chip outscores the best x86 parts",
         "claim": "Nvidia's upcoming ARM64-based Vera CPU posted what the company called the "
                  "best performance ever seen on ARM, outscoring top Intel and AMD x86-64 "
                  "chips, as Nvidia scales spending on its Taiwanese supply chain to as much as "
                  "$150 billion a year.",
         "domain": "compute", "actor": ["nvidia", "arm"], "score": "$150B/yr supply chain",
         "evidences": ["vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-21-nvidia-posts-a-record-quarter-while-conceding-china"]},
        {"id": "2026-05-28-a-region-doubles-datacenter-fees",
         "title": "An Italian region hikes datacenter fees up to 200%",
         "claim": "Lombardy hiked construction fees up to 200% for data centers in green zones, "
                  "nudging operators toward disused industrial sites.",
         "domain": "policy", "actor": ["lombardy"], "score": "+200%",
         "evidences": ["infrastructure-crowding-out", "regulatory-exit"],
         "supersedes": [B + "developments/2026-05-21-a-city-bans-large-datacenters"]},
        {"id": "2026-05-28-five-hundred-aircraft-get-satellite-internet",
         "title": "An airline puts satellite internet on 500+ narrow-body aircraft",
         "claim": "American Airlines is outfitting more than 500 narrow-body aircraft with "
                  "Starlink, while the EU proposed satellite spectrum rules letting Starlink "
                  "bid for direct-to-mobile airwaves while reserving most licenses for locals.",
         "domain": "space", "actor": ["american-airlines", "spacex", "european-union"],
         "score": "500+ aircraft",
         "evidences": ["orbit-as-compute", "network-over-node"]},
        {"id": "2026-05-28-a-third-party-safety-audit-mandate",
         "title": "A state mandates third-party AI safety audits",
         "claim": "Illinois passed SB 315, requiring frontier labs to publish catastrophic-risk "
                  "plans alongside a first-in-the-nation third-party AI safety audit mandate.",
         "domain": "policy", "actor": ["illinois"],
         "evidences": ["legislating-the-shift", "safety-pledges-recede"],
         "supersedes": [B + "developments/2026-05-21-ninety-day-pre-release-notifications"]},
        {"id": "2026-05-28-a-quarter-billion-to-count-the-disruption",
         "title": "A foundation commits $250M to forecast AI's economic impact",
         "claim": "The OpenAI Foundation committed $250 million to forecasting AI's economic "
                  "impact and shepherding workers through post-AI disruption, while Amazon MGM "
                  "Studios launched a fund to finance cinematic AI shows and films.",
         "domain": "economics", "actor": ["openai-foundation", "amazon-mgm"], "score": "$250M",
         "evidences": ["work-displaced", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-05-21-a-hundred-billion-in-philanthropy-becomes-liquid"]},
    ],
}
