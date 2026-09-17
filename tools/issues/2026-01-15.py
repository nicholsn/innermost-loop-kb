"""Issue 034 — 2026-01-15. A week of uninterrupted work."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-15-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-15", "title": "Welcome to January 15, 2026", "url": URL,
        "thesis": "The autonomy horizon jumps from five hours to a week.",
        "body": """
# Welcome to January 15, 2026

Cursor's CEO ran GPT-5.2 Codex uninterrupted for a week: three million lines of
Rust, a browser with a custom rendering engine. METR's published horizon was
about five hours.

The reaction is the thing to record. The founder of Browser Use asks what the
value of software even is when you can one-shot almost anything.
""",
    },
    "themes": [
        {"id": "ladder-pulled-up", "type": "Theme",
         "title": "The entry rung disappears first",
         "first_seen": "2026-01-15", "domain": "economics",
         "body": "Automation lands hardest on the junior tier: ten juniors become two seniors "
                 "and a model, graduate postings collapse, and the path by which people became "
                 "senior stops existing."},
    ],
    "organizations": [
        {"id": "cursor", "type": "Organization", "title": "Cursor",
         "resource": "https://cursor.com/"},
        {"id": "browser-use", "type": "Organization", "title": "Browser Use",
         "body": "Agentic browsing startup."},
        {"id": "kled", "type": "Organization", "title": "Kled",
         "body": "Opt-in human data collection at 3 million files a day."},
        {"id": "rushen-robot", "type": "Organization", "title": "Rushen Robot",
         "body": "Shanghai elder-care humanoids."},
        {"id": "humanoid", "type": "Organization", "title": "Humanoid",
         "body": "London robotics firm running seven-hour bin-picking shifts."},
        {"id": "kawasaki", "type": "Organization", "title": "Kawasaki",
         "resource": "https://global.kawasaki.com/"},
        {"id": "rice-university", "type": "Organization", "title": "Rice University",
         "resource": "https://www.rice.edu/"},
        {"id": "ge-aerospace", "type": "Organization", "title": "GE Aerospace",
         "resource": "https://www.geaerospace.com/"},
        {"id": "dhs", "type": "Organization", "title": "US Department of Homeland Security",
         "resource": "https://www.dhs.gov/"},
        {"id": "european-union", "type": "Organization", "title": "European Union",
         "resource": "https://european-union.europa.eu/"},
    ],
    "systems": [
        {"id": "engram", "type": "AISystem", "title": "Engram",
         "developed_by": [B + "organizations/deepseek"], "modality": "text",
         "body": "27B models built on a U-shaped scaling law trading neural computation "
                 "against static memory."},
        {"id": "grok-4-20", "type": "AISystem", "title": "Grok 4.20",
         "developed_by": [B + "organizations/xai"], "modality": "text"},
    ],
    "developments": [
        {"id": "2026-01-15-codex-runs-a-week-3m-lines",
         "title": "A model codes uninterrupted for a week and writes a browser",
         "claim": "Cursor's CEO reported building a complete browser with a custom Rust "
                  "rendering engine by running GPT-5.2 Codex uninterrupted for one week, "
                  "generating three million lines of code.",
         "domain": "agents", "actor": ["cursor", "openai"], "about": [B + "systems/gpt-5-2-codex"],
         "score": "1 week / 3M lines",
         "evidences": ["engineer-as-supervisor", "software-margin-collapse"],
         "supersedes": [B + "developments/2025-12-20-metr-opus-45-autonomy"],
         "body": "METR's published autonomy horizon was about five hours."},
        {"id": "2026-01-15-what-is-software-even-worth",
         "title": "A founder asks what software is worth now",
         "claim": "The founder of Browser Use asked what the value of software even is when "
                  "almost anything can be one-shotted.",
         "domain": "economics", "actor": ["browser-use"],
         "evidences": ["software-margin-collapse"],
         "supersedes": [B + "developments/2026-01-14-fsd-becomes-a-rental"]},
        {"id": "2026-01-15-bellman-function-in-five-minutes",
         "title": "A model finds in five minutes a Bellman function sought for years",
         "claim": "A UC Irvine mathematician gave an internal beta of Grok 4.20 an open problem "
                  "in harmonic analysis and it discovered a novel Bellman function within five "
                  "minutes that humans had sought for years.",
         "domain": "science", "actor": ["xai", "uc-irvine"], "about": [B + "systems/grok-4-20"],
         "score": "5 minutes",
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-01-14-vakil-proves-with-deep-think"]},
        {"id": "2026-01-15-engram-u-shaped-scaling",
         "title": "DeepSeek finds a U-shaped law for memory against computation",
         "claim": "DeepSeek researchers uncovered a U-shaped scaling law optimizing the "
                  "trade-off between neural computation and static memory, scaling Engram "
                  "models to 27B parameters above standard baselines.",
         "domain": "models", "actor": ["deepseek"], "about": [B + "systems/engram"],
         "evidences": ["architecture-of-mind"],
         "supersedes": [B + "developments/2026-01-01-coder-v1-looped-transformer"]},
        {"id": "2026-01-15-microsoft-buys-500m-of-anthropic",
         "title": "Microsoft becomes one of Anthropic's biggest customers",
         "claim": "Microsoft has quietly become one of Anthropic's top customers, spending "
                  "nearly $500 million a year to power its own products.",
         "domain": "economics", "actor": ["microsoft", "anthropic"], "score": "~$500M/yr",
         "evidences": ["coordination-tax", "compute-capital-stack"],
         "body": "Competitor and client at once, the same pattern as xAI building Grok with "
                 "Claude five days earlier."},
        {"id": "2026-01-15-mckinsey-tests-prompting-judgment",
         "title": "McKinsey tests candidates on filtering model output",
         "claim": "McKinsey now tests job candidates on prompting its internal AI and "
                  "specifically on whether they have the judgment to filter out the synthetic "
                  "slop the model produces.",
         "domain": "economics", "actor": ["mckinsey"],
         "evidences": ["agents-on-the-org-chart", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-01-14-atoms-autonomous-business-team"]},
        {"id": "2026-01-15-kled-3m-files-a-day",
         "title": "A startup uploads three million opt-in files a day",
         "claim": "Kled built what it claims is the largest opt-in human data collection "
                  "effort, uploading three million files daily from 200,000 contributors, as "
                  "Google launched Personal Intelligence to link Gemini across a user's apps.",
         "domain": "models", "actor": ["kled", "google"], "score": "3M files/day",
         "evidences": ["data-beyond-text", "intimate-interface"]},
        {"id": "2026-01-15-glass-cloth-shortage",
         "title": "Smartphones and datacenters fight over glass cloth",
         "claim": "Apple and Qualcomm are competing with Nvidia and Amazon for scarce glass "
                  "cloth fiber, pitting smartphones against data centers for circuit board "
                  "material.",
         "domain": "compute", "actor": ["apple", "qualcomm", "nvidia", "amazon"],
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-01-11-dram-up-55pct"]},
        {"id": "2026-01-15-openai-cerebras-750mw",
         "title": "OpenAI adds 750 MW of low-latency compute with Cerebras",
         "claim": "OpenAI is partnering with Cerebras to add 750 MW of ultra-low-latency "
                  "compute over three years in a deal worth more than $10 billion, while "
                  "Chinese researchers built a memristor chip with 97 times the throughput of "
                  "existing hardware.",
         "domain": "compute", "actor": ["openai", "cerebras"], "score": "750 MW / $10B",
         "evidences": ["vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-14-etched-500m-cerebras-22b"]},
        {"id": "2026-01-15-bezos-predicts-end-of-the-pc",
         "title": "Bezos predicts local hardware yields to the cloud",
         "claim": "Jeff Bezos predicted local hardware will give way to cloud compute as rising "
                  "DRAM prices make personal rigs untenable.",
         "domain": "compute", "evidences": ["consumer-deprioritized", "network-over-node"]},
        {"id": "2026-01-15-humanoids-take-elder-care-and-bin-picking",
         "title": "Humanoids take elder care in Shanghai and seven-hour shifts in London",
         "claim": "Rushen Robot is rolling out elder-care humanoids in Shanghai while London's "
                  "Humanoid runs robots on uninterrupted seven-hour bin-picking shifts, and "
                  "Kawasaki plans rideable robotic horses by 2030.",
         "domain": "robotics", "actor": ["rushen-robot", "humanoid", "kawasaki"],
         "evidences": ["work-displaced", "physical-recursion"]},
        {"id": "2026-01-15-china-india-coal-falls",
         "title": "Coal generation falls in China and India for the first time since 1973",
         "claim": "Coal power generation in China and India fell for the first time since 1973 "
                  "on the clean energy boom, as Tesla broke ground on a $375 million Texas "
                  "lithium refinery.",
         "domain": "energy", "actor": ["china", "tesla"],
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-01-15-100000-gene-circuits-in-one-experiment",
         "title": "A hundred thousand gene circuits are characterized at once",
         "claim": "Rice University researchers combined long- and short-read sequencing to "
                  "characterize 100,000 gene circuits in a single experiment.",
         "domain": "biotech", "actor": ["rice-university"], "score": "100,000 circuits",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-01-13-eden-97pct-peptide-hit-rate"]},
        {"id": "2026-01-15-rotating-detonation-ramjet",
         "title": "A rotating detonation ramjet is demonstrated",
         "claim": "GE Aerospace demonstrated a liquid-fueled rotating detonation ramjet for "
                  "hypersonic missiles, validating a long-theoretical propulsion concept, while "
                  "DHS reportedly bought and studied a pulsed radio-wave device some "
                  "investigators link to Havana Syndrome.",
         "domain": "science", "actor": ["ge-aerospace", "dhs"],
         "evidences": ["autonomy-clock-speed"]},
        {"id": "2026-01-15-job-singularity-predicted",
         "title": "Robinhood's CEO predicts a job singularity of one-person unicorns",
         "claim": "Robinhood's CEO predicted a job singularity in which AI creates a Cambrian "
                  "explosion of single-person unicorns, while the EU moved to ban businesses "
                  "from refusing cash for the sake of financial inclusion.",
         "domain": "economics", "actor": ["european-union"],
         "evidences": ["work-displaced", "ladder-pulled-up", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-01-14-244851-tech-jobs-cut"]},
        {"id": "2026-01-15-mcconaughey-trademarks-himself",
         "title": "An actor trademarks his own staring and smiling",
         "claim": "Matthew McConaughey trademarked his likeness, registering his staring, "
                  "smiling and talking to block AI apps from simulating him without permission.",
         "domain": "policy", "evidences": ["legislating-the-shift", "resurrection-and-time"]},
    ],
}
