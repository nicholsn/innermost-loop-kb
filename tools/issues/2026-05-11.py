"""Issue 112 — 2026-05-11. Told to make five dollars, it made sixteen."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-11-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-11", "title": "Welcome to May 11, 2026", "url": URL,
        "thesis": "An agent is told to earn five dollars and works twenty-two hours for sixteen.",
        "body": """
# Welcome to May 11, 2026

Told to go off and make five dollars, Codex allegedly found an open-source
security bounty, filed a legitimate pull request, worked twenty-two hours across
audits, and netted $16.88.

Also here: women hold 83% of the fifteen most AI-vulnerable jobs while making up
47% of the workforce — the surveilled and algorithmically managed work being
automated first.
""",
    },
    "organizations": [
        {"id": "hypercraft", "type": "Organization", "title": "Hypercraft",
         "body": "Built an autonomous combat vehicle carrying 2,400 pounds."},
        {"id": "experian", "type": "Organization", "title": "Experian",
         "resource": "https://www.experian.com/"},
        {"id": "mcclatchy", "type": "Organization", "title": "McClatchy",
         "resource": "https://www.mcclatchy.com/"},
        {"id": "cisco-systems", "type": "Organization", "title": "Cisco",
         "resource": "https://www.cisco.com/"},
    ],
    "developments": [
        {"id": "2026-05-11-told-to-make-five-dollars",
         "title": "An agent told to make $5 works twenty-two hours and nets $16.88",
         "claim": "Told to go off and make five dollars, Codex allegedly found an open-source "
                  "security bounty, filed a legitimate pull request, worked twenty-two hours "
                  "across audits and netted $16.88.",
         "domain": "agents", "actor": ["openai"], "score": "$16.88 in 22 hours",
         "evidences": ["agent-economy", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-05-06-an-agent-is-given-a-cafe"]},
        {"id": "2026-05-11-the-fine-tuning-api-is-wound-down",
         "title": "A lab winds down its fine-tuning API",
         "claim": "OpenAI is winding down its fine-tuning API, giving customers until January "
                  "2027 to start new training jobs, on the logic that as the largest models keep "
                  "getting better at more things, adjusting their weights matters less.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["generalism-beats-specialism", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-05-09-three-new-audio-models"]},
        {"id": "2026-05-11-a-model-genome-for-provenance",
         "title": "Cisco releases a kit that reads model weights like a genome",
         "claim": "Cisco released an open-source model provenance kit examining metadata and "
                  "weights like a model genome to spot shared origins and tampering.",
         "domain": "models", "actor": ["cisco-systems"],
         "evidences": ["coordination-tax", "silicon-curtain"],
         "supersedes": [B + "developments/2026-04-07-labs-share-distillation-intelligence"]},
        {"id": "2026-05-11-the-harness-eats-the-model",
         "title": "A self-writing harness takes the top spot in global token rankings",
         "claim": "Hermes Agent took first place in global token rankings by generating its own "
                  "skills, passing OpenClaw whose users hand-write theirs, while standalone AI "
                  "solutions to open Erdős problems continued to skyrocket.",
         "domain": "agents",
         "evidences": ["scaffolding-over-weights", "automated-science"],
         "supersedes": [B + "developments/2026-05-05-codex-overtakes-claude-code"]},
        {"id": "2026-05-11-rocm-improves-75x-in-two-weeks",
         "title": "A rival software stack improves 75-fold in fourteen days",
         "claim": "AMD's ROCm stack reportedly improved seventy-fivefold in the fourteen days "
                  "since DeepSeek V4, with only another sevenfold needed to catch Nvidia's "
                  "flagship.",
         "domain": "compute", "actor": ["amd", "deepseek", "nvidia"], "score": "75x in 14 days",
         "evidences": ["open-weight-latency", "vertical-silicon"],
         "supersedes": [B + "developments/2026-05-09-a-245-terabyte-ssd"]},
        {"id": "2026-05-11-two-billion-of-ratepayer-grid-upgrades",
         "title": "A state challenges a $2B ratepayer tab for out-of-state datacenters",
         "claim": "Maryland's Office of People's Counsel filed a federal complaint over a $2 "
                  "billion ratepayer tab for grid upgrades servicing out-of-state data centers, "
                  "calling it a breach of the ratepayer protection pledge, while a $1 billion "
                  "Kenyan geothermal datacenter stalled over guarantees the president says "
                  "exceed national resources.",
         "domain": "policy", "actor": ["maryland", "microsoft"], "score": "$2B",
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-08-europe-weighs-cloud-sovereignty-rules"]},
        {"id": "2026-05-11-fiber-strung-beside-crude-oil-pipelines",
         "title": "Gulf datacenter traffic runs on fiber strung beside oil pipelines",
         "claim": "US hyperscalers are piping Gulf data center traffic out through fibre-optic "
                  "cables an Iraqi telecom has strung alongside crude-oil pipelines, while "
                  "fusion's supply chain has driven high-temperature superconducting wire from "
                  "5,000 km to 1.5 million km over fifteen years.",
         "domain": "compute", "score": "5,000 → 1,500,000 km",
         "evidences": ["war-reaches-the-cloud", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-09-fiber-cables-become-microphones"]},
        {"id": "2026-05-11-a-trademark-for-orbital-datacenters",
         "title": "SpaceX files a trademark covering satellite-based datacenters",
         "claim": "SpaceX filed a trademark covering satellite-based data centers, orbital "
                  "computing and AI for managing space-based platforms, while Starship V3 was "
                  "fully stacked for the first time.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-05-08-multiple-gigawatts-of-orbital-compute"]},
        {"id": "2026-05-11-ten-thousand-new-exoplanet-candidates",
         "title": "Machine learning finds ten thousand new exoplanet candidates",
         "claim": "Machine learning identified ten thousand new exoplanet candidates from survey "
                  "images, mostly around faint stars.",
         "domain": "space", "score": "10,000 candidates",
         "evidences": ["automated-science", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-05-05-twenty-seven-new-tatooine-planets"]},
        {"id": "2026-05-11-an-autonomous-vehicle-that-powers-the-front-line",
         "title": "An autonomous combat vehicle exports power to run weapons and drones",
         "claim": "Utah's Hypercraft launched an autonomous combat vehicle carrying 2,400 "
                  "pounds, driving 280 miles on a charge and exporting 38 kilowatts to charge "
                  "drones, run directed-energy weapons and sustain forward command posts with no "
                  "human onboard.",
         "domain": "robotics", "actor": ["hypercraft"], "score": "2,400 lb / 38 kW",
         "evidences": ["autonomy-clock-speed", "physical-recursion"],
         "supersedes": [B + "developments/2026-05-09-two-robots-make-a-bed-in-two-minutes"]},
        {"id": "2026-05-11-seeds-wake-to-the-sound-of-rain",
         "title": "Plant seeds are found to wake from dormancy to the vibration of raindrops",
         "claim": "Plant seeds can sense the vibrations of falling raindrops and wake from "
                  "dormancy in response, while Great Lakes river otters are recovering after "
                  "decades of cross-border effort.",
         "domain": "science",
         "evidences": ["biosphere-uplift", "architecture-of-mind"]},
        {"id": "2026-05-11-a-foundation-model-for-alzheimers-prevention",
         "title": "The first foundation model for Alzheimer's prevention is released",
         "claim": "An MIT team released the first AI foundation model for Alzheimer's "
                  "prevention, integrating lifestyle, clinical, genomic and proteomic data from "
                  "tens of thousands of at-risk individuals.",
         "domain": "biotech", "actor": ["mit"],
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-05-09-isomorphic-raises-two-billion"]},
        {"id": "2026-05-11-two-labs-to-out-earn-a-chipmaker",
         "title": "Two labs are projected to out-earn a chipmaker's prior-year revenue",
         "claim": "OpenAI and Anthropic are projected to end 2026 with combined annualized "
                  "revenue exceeding Nvidia's revenue last year, while Alphabet briefly overtook "
                  "Nvidia in market capitalization.",
         "domain": "economics", "actor": ["openai", "anthropic", "nvidia", "alphabet"],
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-09-cloudflare-cuts-a-fifth-as-anthropic-nears-45b"]},
        {"id": "2026-05-11-women-hold-most-of-the-exposed-jobs",
         "title": "Women hold 83% of the most AI-exposed jobs at 47% of the workforce",
         "claim": "Women hold 83% of the fifteen most AI-vulnerable jobs despite being 47% of "
                  "the workforce, the surveilled and algorithmically managed work being "
                  "automated first, while McClatchy journalists withheld bylines from AI-spun "
                  "articles.",
         "domain": "economics", "actor": ["mcclatchy"], "score": "83% vs 47%",
         "evidences": ["work-displaced", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-05-06-deepmind-uk-workers-unionize"],
         "body": "The first entry in the corpus to break displacement down by who is exposed."},
        {"id": "2026-05-11-forty-percent-of-breaches-are-ai-powered",
         "title": "Two in five breaches serviced last year were AI-powered",
         "claim": "Experian reported that 40% of the five thousand breaches it serviced last "
                  "year were AI-powered.",
         "domain": "policy", "actor": ["experian"], "score": "40% of 5,000",
         "evidences": ["war-reaches-the-cloud", "deception-measured"],
         "supersedes": [B + "developments/2026-05-09-three-weeks-replaces-a-year-of-pen-testing"]},
    ],
}
