"""Issue 032 — 2026-01-13. Agents get counted as employees."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-13-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-13", "title": "Welcome to January 13, 2026", "url": URL,
        "thesis": "Agents move from tools to headcount.",
        "body": """
# Welcome to January 13, 2026

McKinsey's CEO says the firm employs 40,000 humans and 20,000 agents, and wants
parity within eighteen months. Not "uses" — employs. The corpus has watched
agents take over tasks; this is the first time one appears as a line in the org
chart with a target ratio attached.

Claude Code wrote the entire Claude Cowork desktop app in a week and a half, and
Zuckerberg is reportedly cutting a tenth of Reality Labs to buy GPUs.
""",
    },
    "themes": [
        {"id": "agents-on-the-org-chart", "type": "Theme",
         "title": "Agents counted as headcount",
         "first_seen": "2026-01-13", "domain": "economics",
         "body": "The shift from agents as tools a firm uses to agents as staff a firm employs "
                 "— counted, budgeted, targeted for a ratio against humans, and eventually "
                 "managed by the same org chart."},
    ],
    "organizations": [
        {"id": "mckinsey", "type": "Organization", "title": "McKinsey",
         "resource": "https://www.mckinsey.com/"},
        {"id": "coreweave", "type": "Organization", "title": "CoreWeave",
         "resource": "https://www.coreweave.com/"},
        {"id": "basecamp-research", "type": "Organization", "title": "Basecamp Research",
         "body": "Biodiversity genomics company; co-built EDEN with Nvidia."},
        {"id": "gru-space", "type": "Organization", "title": "GRU Space",
         "body": "Planning the first lunar hotel by 2032."},
        {"id": "astrolab", "type": "Organization", "title": "Astrolab",
         "body": "FLEX lunar rovers for cargo and habitat construction."},
        {"id": "kalshi", "type": "Organization", "title": "Kalshi",
         "resource": "https://kalshi.com/", "body": "Regulated prediction market."},
    ],
    "people": [
        {"id": "dario-amodei", "type": "Person", "title": "Dario Amodei", "name": "Dario Amodei",
         "body": "Anthropic CEO; predicts AI central to CRISPR-scale discoveries."},
    ],
    "systems": [
        {"id": "claude-cowork", "type": "AISystem", "title": "Claude Cowork",
         "developed_by": [B + "organizations/anthropic"], "modality": "desktop agent",
         "body": "Desktop app with direct file system access, written by Claude Code in 1.5 weeks."},
        {"id": "1xwm", "type": "AISystem", "title": "1XWM",
         "developed_by": [B + "organizations/1x"], "modality": "world model",
         "body": "Robot world model trained on actions derived from text-conditioned video."},
        {"id": "eden", "type": "AISystem", "title": "EDEN",
         "developed_by": [B + "organizations/basecamp-research"], "modality": "protein sequence",
         "body": "28B-parameter model trained on 10 billion novel genes; designed antibiotic "
                 "peptides with a 97% experimental hit rate."},
    ],
    "benchmarks": [
        {"id": "prediction-arena", "type": "Benchmark", "title": "Prediction Arena",
         "measures_capability": "reasoning about probable futures with real money at stake"},
    ],
    "developments": [
        {"id": "2026-01-13-claude-code-writes-cowork",
         "title": "Claude Code writes an entire desktop app in 1.5 weeks",
         "claim": "Anthropic confirmed Claude Code wrote the whole Claude Cowork desktop app in "
                  "a week and a half, an app that then gets direct file system access to "
                  "reorganize a user's local files.",
         "domain": "agents", "actor": ["anthropic"], "about": [B + "systems/claude-cowork"],
         "score": "1.5 weeks",
         "evidences": ["recursive-self-improvement", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-01-12-torvalds-vibe-codes"]},
        {"id": "2026-01-13-mckinsey-employs-20000-agents",
         "title": "McKinsey employs 20,000 agents alongside 40,000 people",
         "claim": "McKinsey's CEO said the firm counts AI agents as people it employs, with "
                  "40,000 humans and 20,000 agents and a goal of parity within eighteen months.",
         "domain": "economics", "actor": ["mckinsey"], "score": "40,000 : 20,000",
         "evidences": ["agents-on-the-org-chart", "work-displaced"],
         "supersedes": [B + "developments/2026-01-09-agents-create-4x-more-databases"]},
        {"id": "2026-01-13-prediction-arena-real-money",
         "title": "A benchmark gives models $10,000 to bet",
         "claim": "A new Prediction Arena benchmark gives state-of-the-art models $10,000 in "
                  "real cash to bet on Kalshi, testing real-time reasoning about probable "
                  "futures.",
         "domain": "benchmarks", "actor": ["kalshi"], "about": [B + "benchmarks/prediction-arena"],
         "score": "$10,000",
         "evidences": ["benchmark-saturation", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-07-openforecaster-8b"]},
        {"id": "2026-01-13-1xwm-world-model",
         "title": "1X trains a robot world model on generated video",
         "claim": "1X launched 1XWM, a world model trained on robot actions derived from "
                  "text-conditioned video generation rather than static image-language inputs.",
         "domain": "robotics", "actor": ["1x"], "about": [B + "systems/1xwm"],
         "evidences": ["data-beyond-text", "physical-recursion"],
         "supersedes": [B + "developments/2026-01-08-cyber-laborers-mimic-robots"]},
        {"id": "2026-01-13-apple-siri-on-gemini",
         "title": "Apple puts Siri on Gemini",
         "claim": "Apple and Google announced a multi-year collaboration under which Apple "
                  "Intelligence features including a more personal Siri will rely on Gemini, "
                  "sending Alphabet past a $4 trillion valuation.",
         "domain": "models", "actor": ["apple", "google", "alphabet"], "score": "$4T",
         "evidences": ["compute-capital-stack", "network-over-node"],
         "supersedes": [B + "developments/2026-01-08-alphabet-passes-apple"]},
        {"id": "2026-01-13-tao-learned-from-aristotle",
         "title": "Tao says he learned something from the machine",
         "claim": "Terry Tao said he can honestly say he learned something from Aristotle after "
                  "it contributed to another Erdős solution, while Dario Amodei predicted AI "
                  "will soon be central to discoveries on the scale of CRISPR.",
         "domain": "science", "actor": ["people/terry-tao", "people/dario-amodei", "harmonic"],
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-01-12-erdos-397-third-this-week"],
         "body": "The relationship inverts: the mathematician is now the student."},
        {"id": "2026-01-13-ecologists-lose-touch-with-nature",
         "title": "Ecologists fear losing contact with their subject",
         "claim": "Ecologists report their field is losing touch with nature as robotic sensors "
                  "replace fieldwork.",
         "domain": "science", "evidences": ["cognitive-load-inverted", "automated-science"]},
        {"id": "2026-01-13-meta-compute-tens-of-gigawatts",
         "title": "Meta liquidates the metaverse to buy gigawatts",
         "claim": "Meta announced a Meta Compute initiative to scale to tens of gigawatts this "
                  "decade, with Zuckerberg reportedly cutting a tenth of Reality Labs to fund "
                  "it.",
         "domain": "compute", "actor": ["meta"], "score": "tens of GW",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-01-09-meta-66gw-nuclear"]},
        {"id": "2026-01-13-coreweave-2000-gpus-a-day",
         "title": "CoreWeave installs 2,000 GPUs a day",
         "claim": "CoreWeave is bringing more than 2,000 GPUs online per day at its Denton, "
                  "Texas facility.",
         "domain": "compute", "actor": ["coreweave"], "score": "2,000 GPUs/day",
         "evidences": ["capital-takes-the-plant"]},
        {"id": "2026-01-13-pjm-48pct-annual-demand-growth",
         "title": "The largest US grid expects 4.8% annual demand growth for a decade",
         "claim": "PJM now expects power demand to grow 4.8% a year for the next decade, as the "
                  "White House said tech companies must pay their own way for new generation.",
         "domain": "energy", "actor": ["pjm", "white-house"], "score": "+4.8%/yr",
         "evidences": ["burning-molecules-for-tokens", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-10-data-act-private-grids"]},
        {"id": "2026-01-13-gasoline-under-three-dollars",
         "title": "Gasoline falls below $3 as Norway goes 96% electric",
         "claim": "US average gasoline fell below $3 a gallon while Norway reported 95.9% of "
                  "2025 car sales were non-fossil.",
         "domain": "energy", "score": "<$3/gal / 95.9%",
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-01-13-taiwan-deal-five-more-fabs",
         "title": "A Taiwan trade deal would buy five more Arizona fabs",
         "claim": "The White House is nearing a trade deal with Taiwan cutting tariffs partly "
                  "in exchange for TSMC building five more Arizona fabs, while SK Hynix is "
                  "investing $12.9 billion in Korean HBM packaging and the House passed the "
                  "Remote Access Security Act.",
         "domain": "policy", "actor": ["white-house", "tsmc", "sk-hynix", "us-congress"],
         "score": "5 fabs / $12.9B",
         "evidences": ["silicon-curtain", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-01-09-micron-100b-megafab"]},
        {"id": "2026-01-13-eden-97pct-peptide-hit-rate",
         "title": "A 28B model designs antibiotics with a 97% hit rate",
         "claim": "Basecamp Research and Nvidia unveiled EDEN, a 28-billion-parameter model "
                  "trained on ten billion novel genes that designed antibiotic peptides with a "
                  "97% experimental success rate.",
         "domain": "biotech", "actor": ["basecamp-research", "nvidia"], "about": [B + "systems/eden"],
         "score": "97%",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-01-10-drugclip-10m-times-faster"]},
        {"id": "2026-01-13-lilly-nvidia-co-innovation-lab",
         "title": "Lilly and Nvidia put $1B into a joint AI lab",
         "claim": "Eli Lilly and Nvidia will jointly invest up to $1 billion in an AI "
                  "co-innovation lab, while OpenAI acquired Torch for $100 million to build a "
                  "unified medical memory.",
         "domain": "biotech", "actor": ["eli-lilly", "nvidia", "openai"], "score": "$1B / $100M",
         "evidences": ["automated-science", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-12-claude-for-healthcare-and-life-sciences"]},
        {"id": "2026-01-13-glp1-cuts-grocery-spending",
         "title": "GLP-1 households cut grocery spending 5.3%",
         "claim": "Cornell researchers found households on GLP-1 drugs reduce grocery spending "
                  "by 5.3% on average, moving a macro market through pharmacology.",
         "domain": "economics", "score": "-5.3%",
         "evidences": ["hardware-grade-biology"]},
        {"id": "2026-01-13-lunar-and-orbital-hotels",
         "title": "Hotels are booked for the Moon and orbit",
         "claim": "GRU Space is planning the first lunar hotel by 2032 and Voyager Station "
                  "promises an orbital hotel in 2027, while Astrolab's FLEX rovers will move "
                  "cargo and build habitats.",
         "domain": "space", "actor": ["gru-space", "astrolab"],
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-12-china-files-200000-satellites"]},
        {"id": "2026-01-13-pluribus-drives-apple-tv",
         "title": "A show about a hive mind drives 36% viewership growth",
         "claim": "Apple TV viewership rose 36% on the strength of Pluribus, a series about "
                  "humanity becoming a collective consciousness.",
         "domain": "society", "actor": ["apple"], "score": "+36%",
         "evidences": ["machine-affect", "intimate-interface"]},
    ],
}
