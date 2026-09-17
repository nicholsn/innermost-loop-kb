"""Issue 078 — 2026-03-18. The first autonomous mathematician."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-18-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-18", "title": "Welcome to March 18, 2026", "url": URL,
        "thesis": "An autonomous mathematician ships, free, while open problems start falling.",
        "body": """
# Welcome to March 18, 2026

Harmonic released Aristotle Agent, described as the world's first autonomous
mathematician, live and free. On HorizonMath — a benchmark of over a hundred
predominantly unsolved problems — GPT-5.4 Pro has already solved two open
problems with novel solutions improving on best-known published results.

The corpus has followed this from Tao in the loop on December 13 to a free
public tool on March 18.
""",
    },
    "organizations": [
        {"id": "perturbai", "type": "Organization", "title": "PerturbAI",
         "body": "Published the largest in vivo CRISPR atlas."},
        {"id": "popvax", "type": "Organization", "title": "PopVax",
         "body": "India-based vaccine developer targeting neglected diseases."},
        {"id": "swarmer", "type": "Organization", "title": "Swarmer Inc.",
         "body": "Combat drone software; IPO surged 700%."},
        {"id": "usps", "type": "Organization", "title": "USPS",
         "resource": "https://www.usps.com/"},
    ],
    "benchmarks": [
        {"id": "horizonmath", "type": "Benchmark", "title": "HorizonMath",
         "measures_capability": "progress on over 100 predominantly unsolved mathematics problems"},
    ],
    "systems": [
        {"id": "aristotle-agent", "type": "AISystem", "title": "Aristotle Agent",
         "developed_by": [B + "organizations/harmonic"], "modality": "formal mathematics",
         "body": "Described as the world's first autonomous mathematician; released free."},
    ],
    "developments": [
        {"id": "2026-03-18-aristotle-agent-released-free",
         "title": "The first autonomous mathematician ships free",
         "claim": "Harmonic released Aristotle Agent, described as the world's first autonomous "
                  "mathematician, live and free to use.",
         "domain": "science", "actor": ["harmonic"], "about": [B + "systems/aristotle-agent"],
         "evidences": ["automated-science", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-03-16-agentic-ai-physicist"],
         "body": "Tao in the loop on December 13; a free public tool on March 18."},
        {"id": "2026-03-18-two-open-problems-solved-on-horizonmath",
         "title": "A model solves two open problems, improving on published results",
         "claim": "HorizonMath, a benchmark of over a hundred predominantly unsolved problems, "
                  "found GPT-5.4 Pro has already solved two open problems with novel solutions "
                  "improving on best-known published results.",
         "domain": "benchmarks", "actor": ["openai"], "about": [B + "benchmarks/horizonmath"],
         "score": "2 open problems",
         "evidences": ["automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-03-12-a-possible-open-problem-solution"]},
        {"id": "2026-03-18-gpt54-mini-and-nano",
         "title": "A distilled model approaches the full one at twice the speed",
         "claim": "OpenAI announced GPT-5.4 mini and nano, with mini leaping past its "
                  "predecessor across coding, reasoning, multimodal understanding and tool use "
                  "at twice the speed and approaching the full model on SWE-Bench Pro, while an "
                  "unattributed trillion-parameter model surfaced on OpenRouter fuelling "
                  "speculation about stealth testing.",
         "domain": "models", "actor": ["openai"], "score": "2x speed",
         "evidences": ["reasoning-price-deflation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-03-16-million-token-windows-ship"]},
        {"id": "2026-03-18-cognitive-taxonomy-and-a-200k-prize",
         "title": "DeepMind decomposes general intelligence into ten faculties",
         "claim": "DeepMind released a Cognitive Taxonomy decomposing general intelligence into "
                  "ten faculties and launched a $200,000 competition to close gaps in "
                  "metacognition, attention and social cognition.",
         "domain": "benchmarks", "actor": ["google-deepmind"], "score": "10 faculties",
         "evidences": ["benchmark-saturation", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-03-09-academic-fraud-inclination-metric"]},
        {"id": "2026-03-18-genesis-mission-293m",
         "title": "The DOE aims $293M at twenty national challenges",
         "claim": "The Department of Energy is aiming $293 million via the Genesis Mission at "
                  "using novel AI models to tackle more than twenty national challenges across "
                  "manufacturing, biotech, critical materials, nuclear energy and quantum "
                  "science.",
         "domain": "policy", "actor": ["doe"], "about": [B + "facilities/genesis-mission"],
         "score": "$293M / 20 challenges",
         "evidences": ["science-as-industrial-policy", "automated-science"]},
        {"id": "2026-03-18-eight-million-cell-crispr-atlas",
         "title": "An eight-million-cell CRISPR atlas maps living tissue",
         "claim": "PerturbAI launched with the largest in vivo CRISPR atlas, an eight-million-cell "
                  "brain-wide dataset capturing real biological circuitry in living tissue, "
                  "while Xaira's X-Cell trained on 25.6 million perturbed cells to predict gene "
                  "expression changes across unseen biology.",
         "domain": "biotech", "actor": ["perturbai", "xaira"], "score": "8M / 25.6M cells",
         "evidences": ["hardware-grade-biology", "data-beyond-text"],
         "supersedes": [B + "developments/2026-03-17-first-living-synthetic-cell"]},
        {"id": "2026-03-18-cheaper-rd-makes-neglected-vaccines-viable",
         "title": "Cheaper R&D makes vaccines for neglected killers economically viable",
         "claim": "India-based PopVax argues its generative AI, mRNA platforms and tenfold "
                  "cheaper research costs can make vaccines against neglected killers like "
                  "hepatitis C, tuberculosis and Strep A economically viable for the first time.",
         "domain": "biotech", "actor": ["popvax"], "score": "10x cheaper",
         "evidences": ["reasoning-price-deflation", "hardware-grade-biology"]},
        {"id": "2026-03-18-dispatch-runs-on-your-computer",
         "title": "A persistent agent runs on your computer and answers your phone",
         "claim": "Anthropic shipped Dispatch in Claude Cowork, a persistent agent running on a "
                  "user's computer that can be messaged from their phone, with observers noting "
                  "Anthropic is building OpenClaw faster than OpenAI and Jensen Huang calling "
                  "OpenClaw definitely the next ChatGPT.",
         "domain": "agents", "actor": ["anthropic", "nvidia"],
         "evidences": ["agent-society", "intimate-interface"],
         "supersedes": [B + "developments/2026-03-17-clawinstitute-research-exchange"]},
        {"id": "2026-03-18-video-generated-faster-than-playback",
         "title": "Video is generated faster than it can be watched",
         "claim": "UCSD's Dreamverse generates five-second 1080p clips in 4.55 seconds on a "
                  "single GPU, faster than playback, while Korean researchers announced the "
                  "first city-scale world simulation grounded in a real metropolis via millions "
                  "of street-view images.",
         "domain": "models", "score": "4.55 s per 5 s clip",
         "evidences": ["inhabitable-worlds", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-01-25-odyssey-2-pro-realtime-world"]},
        {"id": "2026-03-18-h200s-approved-for-china",
         "title": "Beijing approves H200 sales as Microsoft weighs suing over a cloud deal",
         "claim": "Nvidia won Beijing's approval to sell H200 chips to China while preparing a "
                  "Groq version for the same market, and Microsoft weighed legal action against "
                  "Amazon and OpenAI over a $50 billion cloud deal.",
         "domain": "policy", "actor": ["nvidia", "china", "microsoft", "amazon", "openai"],
         "score": "$50B",
         "evidences": ["silicon-curtain", "coordination-tax"],
         "supersedes": [B + "developments/2026-03-06-apple-pulls-512gb-mac-studio"]},
        {"id": "2026-03-18-rural-ohio-would-ban-large-datacenters",
         "title": "Rural Ohioans move to ban datacenters above 25 megawatts",
         "claim": "Rural Ohioans want to amend their state constitution to ban data centers "
                  "above 25 megawatts, while Nvidia told its conference it is engineering "
                  "cooling for orbital data centers where convection does not exist.",
         "domain": "policy", "actor": ["nvidia"], "score": "25 MW cap",
         "evidences": ["regulatory-exit", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-03-17-datacenters-pass-offices"]},
        {"id": "2026-03-18-drone-software-ipo-surges-700pct",
         "title": "A combat drone software IPO surges 700%",
         "claim": "Swarmer Inc. surged 700% at IPO, the best US debut in years, on more than "
                  "100,000 real-world combat drone missions in Ukraine since April 2024, while "
                  "the Pentagon planned for AI to train on classified data.",
         "domain": "economics", "actor": ["swarmer", "war-department", "ukraine"],
         "score": "+700% / 100,000 missions",
         "evidences": ["autonomy-clock-speed", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-16-uncrewed-combat-aircraft-prepare-to-fly"]},
        {"id": "2026-03-18-employers-track-token-usage",
         "title": "Companies begin tracking individual employee token usage",
         "claim": "Companies are tracking individual employee token usage to identify whose AI "
                  "strategies deserve amplification and whose waste deserves pruning, while "
                  "gambling sites began accepting bets on which jobs AI will replace.",
         "domain": "economics",
         "evidences": ["compute-as-compensation", "work-displaced"],
         "supersedes": [B + "developments/2026-03-12-compute-is-the-fourth-line-item"],
         "body": "The compute budget that arrived as a perk returns as a performance metric."},
        {"id": "2026-03-18-all-five-nucleobases-on-ryugu",
         "title": "All five canonical nucleobases are found on an asteroid",
         "claim": "All five canonical nucleobases have now been found on asteroid Ryugu, "
                  "strengthening the case that asteroids delivered the ingredients for life to "
                  "Earth.",
         "domain": "space",
         "evidences": ["inhabitable-worlds", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-03-12-moon-factory-under-5000-dollars"]},
    ],
}
