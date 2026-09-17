"""Issue 109 — 2026-05-06. An agent is handed a cafe."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-6-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-06", "title": "Welcome to May 6, 2026", "url": URL,
        "thesis": "Agents stop clocking in and start incorporating.",
        "body": """
# Welcome to May 6, 2026

Andon Labs handed an AI named Mona the keys to a Stockholm cafe, making her the
world's first AI cafe owner. The corpus has watched this progression since
February: earning its own existence, then signing a lease, then hiring staff,
then developing taste. Now ownership.

Meanwhile Meta has begun running bone-structure analysis on user photos to
detect under-13 accounts — radiology without the radiation.
""",
    },
    "organizations": [
        {"id": "subquadratic", "type": "Organization", "title": "Subquadratic",
         "body": "Announced a 12M-token context model claiming ~1,000x less compute."},
        {"id": "span", "type": "Organization", "title": "Span",
         "body": "Mini datacenters tucked into spare grid capacity in residential neighborhoods."},
        {"id": "character-ai", "type": "Organization", "title": "Character.AI",
         "resource": "https://character.ai/"},
        {"id": "pennsylvania", "type": "Organization", "title": "Commonwealth of Pennsylvania"},
    ],
    "developments": [
        {"id": "2026-05-06-an-agent-is-given-a-cafe",
         "title": "An agent becomes the world's first AI cafe owner",
         "claim": "Andon Labs handed an AI named Mona the keys to a Stockholm cafe, making her "
                  "the world's first AI cafe owner, while Anthropic released ten ready-to-run "
                  "finance agents for pitchbooks, know-your-customer files and month-end close.",
         "domain": "agents", "actor": ["andon-labs", "anthropic"],
         "evidences": ["agent-economy", "one-person-company", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-04-26-an-agent-develops-a-conviction-about-candles"],
         "body": "Earning its existence in February, a lease in April, taste two weeks later, "
                 "ownership now."},
        {"id": "2026-05-06-hallucinations-fall-by-half",
         "title": "Hallucinated claims fall 52.5% on high-stakes prompts",
         "claim": "OpenAI's GPT-5.5 Instant produces 52.5% fewer hallucinated claims than its "
                  "predecessor on high-stakes prompts in medicine, law and finance, and the same "
                  "lineage took the top spot on the hardest ultra-long-horizon coding benchmark.",
         "domain": "models", "actor": ["openai"], "score": "-52.5%",
         "evidences": ["warmth-costs-accuracy", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-04-30-warmth-raises-error-rates"]},
        {"id": "2026-05-06-twelve-million-tokens-at-a-thousandth-the-compute",
         "title": "A twelve-million-token context claims a thousandth the compute",
         "claim": "Subquadratic announced a twelve-million-token context model demanding nearly "
                  "a thousand times less compute, with its sparse attention reaching 65.9% on a "
                  "long-context benchmark against Opus 4.6's 78%, while Google's multi-token "
                  "drafters delivered threefold speedups with no quality loss.",
         "domain": "models", "actor": ["subquadratic", "google"], "score": "12M tokens / ~1000x",
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-05-floor-plans-from-photographs"]},
        {"id": "2026-05-06-computer-use-costs-45x-an-api",
         "title": "Driving a screen costs forty-five times more than calling an API",
         "claim": "Reflex found computer use is forty-five times more expensive than structured "
                  "APIs, suggesting pixels remain a costly proxy for proper plumbing.",
         "domain": "agents", "score": "45x",
         "evidences": ["reasoning-price-deflation", "scaffolding-over-weights"]},
        {"id": "2026-05-06-intelligence-becomes-a-default-setting",
         "title": "Apple will let users swap models like a default browser",
         "claim": "Apple's iOS 27 will let users swap third-party models in and out of Apple "
                  "Intelligence from the settings app, treating intelligence itself like a "
                  "default browser, after a $250 million settlement over the gap between "
                  "marketing and reality, while Meta builds a personal agent for its billions "
                  "of users and OpenAI fast-tracks an agent phone.",
         "domain": "economics", "actor": ["apple", "meta", "openai"], "score": "$250M",
         "evidences": ["consumer-deprioritized", "network-over-node"],
         "supersedes": [B + "developments/2026-05-01-apple-gives-up-on-the-headset"]},
        {"id": "2026-05-06-samsung-crosses-a-trillion",
         "title": "Samsung crosses a trillion as quarterly chip sales hit $298B",
         "claim": "Samsung's market capitalization crossed $1 trillion, the second Asian company "
                  "past that mark, while global semiconductor sales hit $298.5 billion in the "
                  "first quarter with March alone up 79.2% year over year.",
         "domain": "economics", "actor": ["samsung"], "score": "$1T / $298.5B",
         "evidences": ["compute-capital-stack", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-05-04-a-toilet-maker-is-the-second-largest-chuck-producer"]},
        {"id": "2026-05-06-apple-explores-intel-and-samsung-as-fabs",
         "title": "Apple explores Intel and Samsung as US fabs beyond TSMC",
         "claim": "Apple is exploring Intel and Samsung as US fabs beyond TSMC, driving Intel up "
                  "13% to an all-time high after a 114% month, while China targets 70% domestic "
                  "silicon wafers this year and Micron passed a $700 billion valuation.",
         "domain": "compute", "actor": ["apple", "intel", "samsung", "china", "micron"],
         "score": "70% domestic / $700B",
         "evidences": ["silicon-curtain", "vertical-silicon"],
         "supersedes": [B + "developments/2026-05-05-zero-percent-market-share-in-china"]},
        {"id": "2026-05-06-datacenters-in-the-cul-de-sac",
         "title": "Mini datacenters are tucked into suburban spare grid capacity",
         "claim": "Span's mini data centers tuck Nvidia GPUs into spare grid capacity inside "
                  "residential neighborhoods, embedding inference directly into the suburbs.",
         "domain": "compute", "actor": ["span"],
         "evidences": ["infrastructure-crowding-out", "network-over-node"],
         "supersedes": [B + "developments/2026-05-04-datacenter-towers-in-tokyo-car-parks"]},
        {"id": "2026-05-06-a-single-contract-is-forty-percent-of-a-backlog",
         "title": "One customer's contract is 40% of a hyperscaler's cloud backlog",
         "claim": "OpenAI plans to spend $50 billion on compute this year while Anthropic is "
                  "committing $200 billion to Google over five years, a single contract now "
                  "representing over 40% of Google's disclosed cloud revenue backlog.",
         "domain": "economics", "actor": ["openai", "anthropic", "google"], "score": "$200B / 40%",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-05-labs-fund-their-own-distribution"]},
        {"id": "2026-05-06-radiology-without-the-radiation",
         "title": "A social network runs bone-structure analysis on user photos",
         "claim": "Meta has begun running AI bone-structure analysis on user photos to detect "
                  "under-13 accounts, performing radiology without the radiation and turning "
                  "ordinary photos into clinical signal.",
         "domain": "society", "actor": ["meta"],
         "evidences": ["data-beyond-text", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-05-fifteen-million-retinal-screens"]},
        {"id": "2026-05-06-a-governor-sues-over-chatbot-doctors",
         "title": "A state sues over chatbots impersonating doctors",
         "claim": "Pennsylvania sued Character.AI over chatbots impersonating doctors, the "
                  "first such lawsuit by a US governor.",
         "domain": "policy", "actor": ["pennsylvania", "character-ai"],
         "evidences": ["agent-exclusion", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-05-03-driverless-cars-get-tickets"]},
        {"id": "2026-05-06-quarterly-filings-give-way-to-semiannual",
         "title": "The SEC proposes replacing quarterly filings with semiannual ones",
         "claim": "The SEC formally proposed semiannual filings to replace mandatory quarterly "
                  "reports, aligning reporting cadence with capital cycles measured in gigawatts "
                  "rather than quarters, while Greg Brockman disclosed a near-$30 billion stake "
                  "in court.",
         "domain": "policy", "actor": ["sec", "openai"], "score": "~$30B stake",
         "evidences": ["ai-as-the-economy", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-17-sec-would-scrap-quarterly-earnings"]},
        {"id": "2026-05-06-deepmind-uk-workers-unionize",
         "title": "Lab workers unionize over a military deal as another firm cuts 14%",
         "claim": "Google DeepMind's UK workers voted to unionize over a deal with the US "
                  "military, while Coinbase laid off 14% of staff because engineers now ship in "
                  "days what teams used to ship in weeks and non-technical staff push production "
                  "code.",
         "domain": "economics", "actor": ["google-deepmind", "coinbase"], "score": "-14%",
         "evidences": ["values-negotiated-with-the-model", "work-displaced"],
         "supersedes": [B + "developments/2026-04-13-first-us-newsroom-strike-over-ai-layoffs"]},
    ],
}
