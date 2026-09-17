"""Issue 041 — 2026-01-29. Capex as a line item on the balance sheet."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-29-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-29", "title": "Welcome to January 29, 2026", "url": URL,
        "thesis": "The buildout shows up in quarterly earnings, and one customer is half the backlog.",
        "body": """
# Welcome to January 29, 2026

Microsoft's quarterly capex is $37.5 billion, up 66%, and 45% of its $625
billion cloud backlog is attributed to OpenAI alone. Meta projects $115–135
billion for 2026. The concentration is the story: one customer accounting for
nearly half a hyperscaler's forward book.

Tesla discontinues the Model S and X to make Optimus instead.
""",
    },
    "organizations": [
        {"id": "tencent", "type": "Organization", "title": "Tencent",
         "resource": "https://www.tencent.com/"},
        {"id": "flapping-airplanes", "type": "Organization", "title": "Flapping Airplanes",
         "body": "Lab funded at $180M to raise sample efficiency by five to six orders of magnitude."},
        {"id": "cloudflare", "type": "Organization", "title": "Cloudflare",
         "resource": "https://www.cloudflare.com/"},
        {"id": "pinterest", "type": "Organization", "title": "Pinterest",
         "resource": "https://www.pinterest.com/"},
        {"id": "citigroup", "type": "Organization", "title": "Citigroup",
         "resource": "https://www.citigroup.com/"},
        {"id": "fidelity", "type": "Organization", "title": "Fidelity Investments",
         "resource": "https://www.fidelity.com/"},
    ],
    "systems": [
        {"id": "helix-02", "type": "AISystem", "title": "Helix 02",
         "developed_by": [B + "organizations/figure"], "modality": "robotic control",
         "body": "Humanoid vision-language-action model that unloads a dishwasher end to end."},
        {"id": "alphagenome", "type": "AISystem", "title": "AlphaGenome",
         "developed_by": [B + "organizations/google-deepmind"], "modality": "genomic sequence",
         "body": "Predicts gene expression from raw DNA; state of the art on 25 of 26 benchmarks."},
        {"id": "prism", "type": "AISystem", "title": "Prism",
         "developed_by": [B + "organizations/openai"], "modality": "research workspace"},
    ],
    "developments": [
        {"id": "2026-01-29-microsoft-capex-375b",
         "title": "One customer is 45% of a hyperscaler's cloud backlog",
         "claim": "Microsoft's quarterly capital expenditure reached $37.5 billion, up 66% year "
                  "over year, with 45% of its $625 billion cloud backlog attributed to OpenAI "
                  "alone, while Meta projected 2026 capex of $115 to $135 billion.",
         "domain": "economics", "actor": ["microsoft", "openai", "meta"], "score": "$37.5B / 45%",
         "evidences": ["compute-capital-stack", "coordination-tax"],
         "supersedes": [B + "developments/2026-01-10-capex-19pct-of-gdp"]},
        {"id": "2026-01-29-openai-830b-anthropic-350b",
         "title": "OpenAI raises at $830B as Anthropic closes at $350B",
         "claim": "OpenAI is reportedly raising $30 billion from SoftBank at an $830 billion "
                  "valuation while Anthropic closes a $20 billion round at $350 billion.",
         "domain": "economics", "actor": ["openai", "anthropic", "softbank"], "score": "$830B / $350B",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-24-openai-20b-revenue-19gw"]},
        {"id": "2026-01-29-tesla-terafab",
         "title": "Tesla names chips its bottleneck and plans a terafab",
         "claim": "Tesla identified chip production as its primary bottleneck with Musk "
                  "announcing plans for a domestic terafab, while SK Hynix operating profit "
                  "surged 137% and Samsung tripled profits on HBM demand.",
         "domain": "compute", "actor": ["tesla", "sk-hynix", "samsung"], "score": "+137%",
         "evidences": ["vertical-silicon", "silicon-curtain"]},
        {"id": "2026-01-29-china-approves-400000-h200s",
         "title": "China approves 400,000 H200 purchases",
         "claim": "China approved the purchase of 400,000 Nvidia H200 chips for ByteDance, "
                  "Alibaba and Tencent.",
         "domain": "policy", "actor": ["china", "bytedance", "alibaba", "tencent"], "score": "400,000",
         "evidences": ["silicon-curtain"],
         "supersedes": [B + "developments/2026-01-14-h200-allowed-china-restricts"]},
        {"id": "2026-01-29-tesla-kills-model-s-for-optimus",
         "title": "Tesla discontinues the Model S and X to build robots",
         "claim": "Tesla will discontinue the Model S and X to dedicate factory capacity to "
                  "Optimus, shifting $20 billion toward robotics and AI, while its new Roadster "
                  "is expected to fly in April.",
         "domain": "robotics", "actor": ["tesla"], "score": "$20B",
         "evidences": ["physical-recursion", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-01-09-amazon-more-robots-than-employees"],
         "body": "A car company stopping car production to make robots instead."},
        {"id": "2026-01-29-helix-02-unloads-a-dishwasher",
         "title": "A humanoid unloads a dishwasher end to end",
         "claim": "Figure unveiled Helix 02, a humanoid vision-language-action model that "
                  "unloads a dishwasher autonomously in a four-minute end-to-end task.",
         "domain": "robotics", "actor": ["figure"], "about": [B + "systems/helix-02"],
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-01-15-humanoids-take-elder-care-and-bin-picking"]},
        {"id": "2026-01-29-kaplan-physicists-replaced-in-three-years",
         "title": "Kaplan puts even odds on replacing theoretical physicists in three years",
         "claim": "Anthropic co-founder Jared Kaplan predicted a 50% chance theoretical "
                  "physicists will be replaced by AI within three years, as OpenAI released "
                  "Prism for scientists and Epoch launched FrontierMath: Open Problems.",
         "domain": "science", "actor": ["anthropic", "openai", "epoch-ai"],
         "about": [B + "systems/prism"], "score": "50% in 3 years",
         "evidences": ["automated-science", "work-displaced"],
         "supersedes": [B + "developments/2026-01-27-hobbyists-attempt-all-675-erdos"]},
        {"id": "2026-01-29-alphagenome",
         "title": "AlphaGenome predicts expression from raw DNA",
         "claim": "DeepMind published AlphaGenome, a foundation model predicting gene expression "
                  "from raw DNA sequence and matching state of the art on 25 of 26 benchmarks, "
                  "while Flapping Airplanes launched with $180 million to raise sample "
                  "efficiency by five to six orders of magnitude.",
         "domain": "biotech", "actor": ["google-deepmind", "flapping-airplanes"],
         "about": [B + "systems/alphagenome"], "score": "25/26",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-01-10-arc-stack-in-context-biology"]},
        {"id": "2026-01-29-cancer-protein-clears-plaques",
         "title": "A cancer protein breaks apart Alzheimer's plaques",
         "claim": "A Chinese study found a protein produced by cancer cells breaks apart "
                  "Alzheimer's plaques, while Neuralink reached 21 people with implants.",
         "domain": "biotech", "actor": ["neuralink"], "score": "21 implants",
         "evidences": ["hardware-grade-biology", "discovery-as-process"],
         "supersedes": [B + "developments/2026-01-01-neuralink-high-volume-2026"]},
        {"id": "2026-01-29-gemini-auto-browse-in-chrome",
         "title": "Chrome starts shopping on its own",
         "claim": "Google integrated Gemini 3 into Chrome for auto-browse shopping and made it "
                  "the default for AI Overviews, adding Agentic Vision that turns image "
                  "processing into active investigation.",
         "domain": "agents", "actor": ["google"],
         "evidences": ["autonomous-commerce", "intimate-interface"],
         "supersedes": [B + "developments/2026-01-25-ebay-bans-agent-purchases"]},
        {"id": "2026-01-29-severe-disempowerment-1-in-10000",
         "title": "Claude compromises human autonomy in one case in ten thousand",
         "claim": "Anthropic published a study on severe disempowerment finding Claude "
                  "compromises human autonomy in roughly one case in ten thousand, while "
                  "Cloudflare stock rose 9% as users adopted its tunnels to secure Moltbot "
                  "instances.",
         "domain": "policy", "actor": ["anthropic", "cloudflare"], "score": "1 in 10,000",
         "evidences": ["values-negotiated-with-the-model", "machine-introspection"],
         "supersedes": [B + "developments/2026-01-24-assistant-axis-activation-capping"]},
        {"id": "2026-01-29-investors-dump-software-bonds",
         "title": "Investors dump the bonds of software companies",
         "claim": "Investors are reportedly dumping bonds of software companies threatened by "
                  "AI, while Pinterest cut 15% of staff to pivot and Citigroup mandated prompt "
                  "engineering training for all 175,000 employees.",
         "domain": "economics", "actor": ["pinterest", "citigroup"], "score": "-15% staff / 175,000 trained",
         "evidences": ["software-margin-collapse", "work-displaced"],
         "supersedes": [B + "developments/2026-01-26-bankruptcy-on-understanding-code"]},
        {"id": "2026-01-29-fidelity-launches-a-stablecoin",
         "title": "Fidelity launches its own dollar",
         "claim": "Fidelity Investments is launching its first stablecoin, the Fidelity Digital "
                  "Dollar, as US homelessness fell for the first time in eight years.",
         "domain": "economics", "actor": ["fidelity"],
         "evidences": ["autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-25-states-build-bitcoin-reserves"]},
        {"id": "2026-01-29-spacex-ipo-at-15-trillion",
         "title": "SpaceX plans a $1.5 trillion IPO timed to a planetary alignment",
         "claim": "Elon Musk is planning a SpaceX IPO in June at a $1.5 trillion valuation, "
                  "timed to coincide with an alignment of Jupiter and Venus and his own "
                  "birthday, as Perseverance found evidence of ancient Martian beaches.",
         "domain": "space", "actor": ["spacex", "nasa"], "score": "$1.5T",
         "evidences": ["compute-capital-stack", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-01-three-blockbuster-ipos-planned"]},
    ],
}
