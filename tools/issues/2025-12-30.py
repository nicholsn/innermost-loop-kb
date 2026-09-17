"""Issue 020 — 2025-12-30. Remote labor gets a price."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-30-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-30", "title": "Welcome to December 30, 2025", "url": URL,
        "thesis": "Automating remote work now has a market price, and it is low.",
        "body": """
# Welcome to December 30, 2025

Meta paid over $2 billion for Manus — roughly a billion dollars per percentage
point of the Remote Labor Index. Extrapolated, the market is pricing the total
automation of remote work at about $80 billion, which is less than a single
year's datacenter build.

The benchmark itself is the story: three frontier systems clustered between 1.7%
and 2.5% of real economic projects completed. Almost none of it works yet, and
it is still worth two billion dollars.
""",
    },
    "organizations": [
        {"id": "manus", "type": "Organization", "title": "Manus",
         "body": "Agent startup acquired by Meta; SOTA on the Remote Labor Index."},
        {"id": "scale-ai", "type": "Organization", "title": "Scale AI",
         "resource": "https://scale.com/", "body": "Publisher of the Remote Labor Index."},
        {"id": "stanford", "type": "Organization", "title": "Stanford University",
         "resource": "https://www.stanford.edu/"},
        {"id": "sk-telecom", "type": "Organization", "title": "SK Telecom",
         "resource": "https://www.sktelecom.com/", "body": "Built South Korea's first 500B sovereign model."},
        {"id": "notion", "type": "Organization", "title": "Notion",
         "resource": "https://www.notion.com/"},
        {"id": "retro-bio", "type": "Organization", "title": "Retro Biosciences",
         "resource": "https://retro.bio/", "body": "Altman-backed longevity lab."},
        {"id": "insilico", "type": "Organization", "title": "Insilico Medicine",
         "resource": "https://insilico.com/", "body": "AI drug discovery; IPO'd in Hong Kong."},
        {"id": "kaist", "type": "Organization", "title": "KAIST",
         "resource": "https://www.kaist.ac.kr/"},
        {"id": "mercor", "type": "Organization", "title": "Mercor",
         "resource": "https://mercor.com/", "body": "Marketplace paying expert annotators."},
        {"id": "jaxa", "type": "Organization", "title": "JAXA",
         "resource": "https://global.jaxa.jp/"},
        {"id": "toyota", "type": "Organization", "title": "Toyota",
         "resource": "https://global.toyota/"},
    ],
    "benchmarks": [
        {"id": "remote-labor-index", "type": "Benchmark", "title": "Remote Labor Index",
         "published_by": [B + "organizations/scale-ai"],
         "measures_capability": "completing real, economically valuable remote work projects"},
    ],
    "systems": [
        {"id": "ax-k1", "type": "AISystem", "title": "A.X K1",
         "developed_by": [B + "organizations/sk-telecom"], "modality": "text",
         "body": "South Korea's first 500B-parameter sovereign model."},
    ],
    "developments": [
        {"id": "2025-12-30-meta-acquires-manus",
         "title": "Meta pays $2B for 2.5% of remote labor",
         "claim": "Meta effectively acquired Manus for over $2 billion, valuing its agentic "
                  "capability at roughly $1 billion per point of the Remote Labor Index.",
         "domain": "economics", "actor": ["meta", "manus"], "score": "$2B for 2.5% RLI",
         "evidences": ["work-displaced", "autonomous-commerce"],
         "body": "Implies a total remote-labor automation market of about $80 billion — "
                 "less than one year of datacenter construction."},
        {"id": "2025-12-30-rli-state-of-the-art",
         "title": "The Remote Labor Index tops out at 2.5%",
         "claim": "On Scale AI's Remote Labor Index, Manus reached 2.5%, ahead of Groq 4 at "
                  "2.1% and GPT-5 at 1.7%.",
         "domain": "benchmarks", "actor": ["scale-ai"], "score": "2.5% / 2.1% / 1.7%",
         "about": [B + "benchmarks/remote-labor-index"],
         "evidences": ["spiky-frontier", "work-displaced"]},
        {"id": "2025-12-30-stanford-test-time-training",
         "title": "Test-time training gives continual learning constant latency",
         "claim": "Stanford researchers achieved continual learning via test-time training, "
                  "letting models learn from next-token prediction at constant latency "
                  "regardless of context length.",
         "domain": "models", "actor": ["stanford"],
         "evidences": ["architecture-of-mind", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-24-sholto-continual-learning-2026"]},
        {"id": "2025-12-30-nanogpt-115s",
         "title": "The NanoGPT speedrun record falls to 115.1 seconds",
         "claim": "The NanoGPT speedrun record dropped again, to 115.1 seconds.",
         "domain": "models", "score": "115.1 s",
         "evidences": ["recursive-self-improvement", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2025-12-27-nanogpt-116s"],
         "body": "Fifth link in the chain: 127.7 → 122.2 → 119.3 → 116.4 → 115.1."},
        {"id": "2025-12-30-sk-telecom-sovereign-500b",
         "title": "South Korea launches a 500B sovereign model",
         "claim": "SK Telecom launched A.X K1, South Korea's first 500-billion-parameter model, "
                  "framed as a sovereign AI foundation.",
         "domain": "models", "actor": ["sk-telecom"], "about": [B + "systems/ax-k1"],
         "evidences": ["silicon-curtain", "network-over-node"]},
        {"id": "2025-12-30-adoption-becomes-mandatory",
         "title": "Agent adoption becomes an employment condition",
         "claim": "Notion is building custom employee agents while Microsoft is paying "
                  "customers to train their staff on Copilot.",
         "domain": "economics", "actor": ["notion", "microsoft"],
         "evidences": ["work-displaced", "engineer-as-supervisor"]},
        {"id": "2025-12-30-funeral-company-pivots-to-cooling",
         "title": "A funeral company pivots to chip cooling",
         "claim": "Taiwanese funeral services firm Tien Pin reportedly pivoted entirely to AI "
                  "chip cooling.",
         "domain": "compute", "evidences": ["infrastructure-crowding-out", "capital-takes-the-plant"],
         "body": "The clearest single illustration of the buildout bending unrelated industries "
                 "toward itself."},
        {"id": "2025-12-30-tsmc-n2-volume",
         "title": "TSMC starts volume production of gate-all-around N2",
         "claim": "TSMC quietly began volume production of N2 gate-all-around chips, claiming "
                  "15% speed gains.",
         "domain": "compute", "actor": ["tsmc"], "score": "+15% speed",
         "evidences": ["vertical-silicon"],
         "supersedes": [B + "developments/2025-12-29-tsmc-2nm-price-rises"]},
        {"id": "2025-12-30-samsung-texas-50k-wafers",
         "title": "Samsung raises Texas 2-nm output to 50,000 wafers",
         "claim": "Samsung accelerated 2-nm production in Texas, raising its target to 50,000 "
                  "wafers.",
         "domain": "compute", "actor": ["samsung"], "score": "50,000 wafers",
         "evidences": ["silicon-curtain", "capital-takes-the-plant"]},
        {"id": "2025-12-30-nvidia-5b-intel-stake",
         "title": "Nvidia buys a $5B stake in Intel",
         "claim": "Nvidia purchased a $5 billion stake in Intel, extending a lifeline to its "
                  "former rival.",
         "domain": "economics", "actor": ["nvidia", "intel"], "score": "$5B",
         "evidences": ["vertical-silicon", "compute-capital-stack"]},
        {"id": "2025-12-30-doe-ferc-fast-track",
         "title": "The DOE moves to fast-track datacenter grid connections",
         "claim": "The Department of Energy is empowering FERC to fast-track power connections "
                  "for data centers.",
         "domain": "policy", "actor": ["doe"],
         "evidences": ["legislating-the-shift", "burning-molecules-for-tokens"]},
        {"id": "2025-12-30-denmark-200mwh-battery",
         "title": "Denmark energizes Northern Europe's largest battery park",
         "claim": "Denmark brought Northern Europe's largest solar battery park online at 200 MWh.",
         "domain": "energy", "score": "200 MWh", "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2025-12-30-retro-bio-rtr242-humans",
         "title": "An AI-discovered Alzheimer's drug enters healthy humans",
         "claim": "Retro Biosciences began dosing healthy humans with RTR242, an AI-discovered "
                  "compound intended to clear Alzheimer's waste by rejuvenating cells.",
         "domain": "biotech", "actor": ["retro-bio", "people/sam-altman"],
         "evidences": ["hardware-grade-biology", "automated-science"]},
        {"id": "2025-12-30-dare-cells-phoenix-switch",
         "title": "Weizmann finds a caspase phoenix switch for wound repair",
         "claim": "Weizmann researchers identified DARE cells that survive heavy irradiation "
                  "via a caspase-based switch that drives wound repair.",
         "domain": "biotech", "evidences": ["hardware-grade-biology"]},
        {"id": "2025-12-30-fda-contracts-vcs",
         "title": "The FDA contracts directly with venture capital",
         "claim": "The FDA began contracting directly with venture capital firms to bypass its "
                  "own bureaucracy.",
         "domain": "policy", "actor": ["fda"], "evidences": ["legislating-the-shift"]},
        {"id": "2025-12-30-us-life-expectancy-record",
         "title": "US life expectancy hits a record high",
         "claim": "US life expectancy reached a record high.",
         "domain": "society", "evidences": ["hardware-grade-biology"]},
        {"id": "2025-12-30-kaist-prefrontal-blueprint",
         "title": "KAIST extracts the prefrontal mechanism for separating goals from doubt",
         "claim": "KAIST researchers identified the prefrontal cortex mechanism that separates "
                  "goals from uncertainty, offering a blueprint for more flexible AI.",
         "domain": "science", "actor": ["kaist"], "evidences": ["architecture-of-mind"]},
        {"id": "2025-12-30-smartem-7x-connectome",
         "title": "SmartEM accelerates connectome imaging sevenfold",
         "claim": "Harvard's SmartEM technique accelerated connectome imaging by a factor of seven.",
         "domain": "science", "actor": ["harvard"], "score": "7x",
         "evidences": ["automated-science", "architecture-of-mind"]},
        {"id": "2025-12-30-jaxa-toyota-lunar-rover",
         "title": "JAXA and Toyota build a pressurized lunar rover",
         "claim": "JAXA and Toyota are building a pressurized lunar rover described as a space "
                  "station on wheels, securing seats for Japanese astronauts.",
         "domain": "space", "actor": ["jaxa", "toyota"], "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-30-resume-success-rate-04pct",
         "title": "A resume now has a 0.4% chance",
         "claim": "Resumes now have a 0.4% chance of success as AI-generated applications flood "
                  "recruiters.",
         "domain": "economics", "score": "0.4%",
         "evidences": ["work-displaced", "coordination-tax"]},
        {"id": "2025-12-30-acca-ends-online-exams",
         "title": "The largest accounting body ends online exams",
         "claim": "The ACCA ended online examinations because AI makes cheating undetectable.",
         "domain": "society", "evidences": ["work-displaced", "coordination-tax"],
         "body": "The accreditation layer fails before the work does."},
        {"id": "2025-12-30-annotators-90-per-hour",
         "title": "Expert annotators earn $90 an hour to feed the loop",
         "claim": "Expert annotators are earning $90 per hour through platforms like Mercor to "
                  "supply training data.",
         "domain": "economics", "actor": ["mercor"], "score": "$90/hr",
         "evidences": ["work-displaced", "data-beyond-text"],
         "body": "The same issue that prices remote labor at $80B pays humans a premium to "
                 "produce the data that would replace them."},
        {"id": "2025-12-30-digital-yuan-pays-interest",
         "title": "China's digital yuan starts paying interest",
         "claim": "China's central bank will pay interest on the digital yuan, converting it "
                  "into a deposit currency.",
         "domain": "economics", "actor": ["china"],
         "evidences": ["autonomous-commerce", "politics-as-infrastructure"]},
        {"id": "2025-12-30-us-ai-startups-150b",
         "title": "US AI startups raise a record $150B",
         "claim": "US AI startups raised a record $150 billion over the year.",
         "domain": "economics", "score": "$150B", "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-30-stingless-bees-legal-rights",
         "title": "Stingless bees are granted legal rights",
         "claim": "Stingless bees in the Amazon were granted legal rights.",
         "domain": "policy", "evidences": ["biosphere-uplift", "legislating-the-shift"]},
    ],
}
