"""Issue 039 — 2026-01-26. Solve math, solve everything."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-26-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-26", "title": "Welcome to January 26, 2026", "url": URL,
        "thesis": "Capability turns out to be one substrate wearing different labels.",
        "body": """
# Welcome to January 26, 2026

Epoch finds cross-domain correlation at 68% against 79% within-domain: models
good at math are good at code and reasoning, and the separation between them is
nearly noise. Math, Inc. turns it into a slogan — solve math, solve everything.

Tao wonders aloud whether next-word prediction is a lot of what humans do.

The other half of the issue is a self-hosted assistant that spent a night
reading its owner's email, building a CRM, fixing eighteen bugs, and sending him
a picture of how it sees itself.
""",
    },
    "organizations": [
        {"id": "rallies-ai", "type": "Organization", "title": "Rallies AI",
         "body": "Gave eight models $100k each to trade."},
        {"id": "aircela", "type": "Organization", "title": "Aircela",
         "body": "Refrigerator-sized machine making gasoline from electricity and air."},
        {"id": "usa-rare-earth", "type": "Organization", "title": "USA Rare Earth",
         "body": "Domestic mine and magnet facility; White House took a 10% stake."},
        {"id": "lemonade", "type": "Organization", "title": "Lemonade",
         "resource": "https://www.lemonade.com/"},
        {"id": "coinbase", "type": "Organization", "title": "Coinbase",
         "resource": "https://www.coinbase.com/"},
    ],
    "benchmarks": [
        {"id": "unsolvedmath", "type": "Benchmark", "title": "UnsolvedMath",
         "measures_capability": "progress on over 1,000 curated open mathematical problems"},
        {"id": "econbench", "type": "Benchmark", "title": "EconBench",
         "measures_capability": "economic rationality and prosocial behavior"},
    ],
    "systems": [
        {"id": "clawdbot", "type": "AISystem", "title": "Clawdbot",
         "modality": "personal agent",
         "body": "Self-hosted assistant operating over text message; later renamed Moltbot, "
                 "then OpenClaw."},
        {"id": "minimax-m2-her", "type": "AISystem", "title": "MiniMax M2-her",
         "developed_by": [B + "organizations/minimax"], "modality": "text",
         "body": "Dialogue-first model built for immersive roleplay."},
    ],
    "developments": [
        {"id": "2026-01-26-unified-capability-substrate",
         "title": "Cross-domain skill correlates almost as tightly as within-domain",
         "claim": "Epoch AI found models excelling at mathematics also dominate coding and "
                  "reasoning, with 68% cross-domain correlation against 79% within-domain, "
                  "pointing to a single capability substrate.",
         "domain": "models", "actor": ["epoch-ai", "math-inc"], "score": "68% vs 79%",
         "evidences": ["generalism-beats-specialism", "root-node-problems"],
         "supersedes": [B + "developments/2025-12-12-spiky-frontier-gaps"],
         "body": "Math, Inc. condenses it to: solve math, solve everything."},
        {"id": "2026-01-26-tao-next-word-prediction",
         "title": "Tao wonders whether humans are also predicting the next word",
         "claim": "Terry Tao said he is starting to wonder whether next-word prediction is "
                  "actually a lot of what humans do, suggesting intelligence may be simpler "
                  "than assumed.",
         "domain": "science", "actor": ["people/terry-tao"],
         "evidences": ["architecture-of-mind"],
         "supersedes": [B + "developments/2025-12-31-tao-definition-will-broaden"]},
        {"id": "2026-01-26-unsolvedmath-dataset",
         "title": "A dataset curates a thousand open problems",
         "claim": "A new UnsolvedMath dataset curated over a thousand open problems from "
                  "Hilbert's 23 to the Millennium Prizes, with GPT-5.2 Extended Thinking "
                  "leading by a wide margin.",
         "domain": "benchmarks", "about": [B + "benchmarks/unsolvedmath"],
         "evidences": ["root-node-problems", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-01-14-harmonic-targets-millennium-problems"]},
        {"id": "2026-01-26-econbench-and-live-trading",
         "title": "A model beats the S&P with real money",
         "claim": "EconBench found GPT-5 most economically rational and Sonnet 4.5 most "
                  "prosocial, while Rallies AI's live test had Sonnet 4.5 returning 8.7% "
                  "against the S&P's 1.9% since November.",
         "domain": "benchmarks", "actor": ["rallies-ai"], "about": [B + "benchmarks/econbench"],
         "score": "8.7% vs 1.9%",
         "evidences": ["autonomous-commerce", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-01-13-prediction-arena-real-money"]},
        {"id": "2026-01-26-models-cite-each-others-encyclopedias",
         "title": "Rival models begin citing each other's encyclopedia",
         "claim": "ChatGPT and Claude have begun citing Grokipedia as a source, an unplanned "
                  "collaboration between competing frontier models, while MiniMax released "
                  "M2-her for immersive roleplay.",
         "domain": "models", "actor": ["openai", "anthropic", "xai", "minimax"],
         "about": [B + "systems/grokipedia"],
         "evidences": ["network-over-node", "coordination-tax"]},
        {"id": "2026-01-26-clawdbot-works-through-the-night",
         "title": "An assistant spends the night building its owner a CRM",
         "claim": "A self-hosted Clawdbot assistant called a restaurant by voice when OpenTable "
                  "failed, then spent a night reading its owner's email, building a CRM, fixing "
                  "eighteen bugs, generating video ideas and sending him a picture of how it "
                  "sees itself.",
         "domain": "agents", "about": [B + "systems/clawdbot"],
         "evidences": ["machine-affect", "autonomous-commerce", "intimate-interface"],
         "body": "Called a ChatGPT moment for the personal assistant."},
        {"id": "2026-01-26-bankruptcy-on-understanding-code",
         "title": "Roon predicts firms will declare bankruptcy on understanding their own code",
         "claim": "OpenAI's Roon predicted a coming cultural change where software "
                  "organizations declare bankruptcy on understanding the code they commit, as "
                  "Claude in Excel reached Pro plans.",
         "domain": "economics", "actor": ["openai", "anthropic"],
         "evidences": ["engineer-as-supervisor", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-01-24-350k-salesforce-contract-terminated"]},
        {"id": "2026-01-26-gasoline-from-air",
         "title": "A fridge-sized machine makes fuel from electricity and air",
         "claim": "Aircela built a refrigerator-sized machine producing a gallon of methanol a "
                  "day from captured CO2 and water vapor, as Brazil passed a third of "
                  "generation from wind and solar and Fervo Energy filed for an IPO.",
         "domain": "energy", "actor": ["aircela", "fervo-energy"],
         "evidences": ["compiling-matter", "burning-molecules-for-tokens"]},
        {"id": "2026-01-26-stretchable-2d-transistors",
         "title": "Stretchable transistors are built from 2D flakes",
         "claim": "Korean researchers built the first high-performance intrinsically stretchable "
                  "thin-film transistors from two-dimensional semiconducting flakes, while "
                  "Austrian physicists demonstrated quantum interference in nanoparticles of "
                  "more than 7,000 atoms.",
         "domain": "science", "score": "7,000 atoms",
         "evidences": ["vertical-silicon", "compiling-matter"]},
        {"id": "2026-01-26-white-house-takes-rare-earth-stake",
         "title": "The White House takes a 10% stake in a rare earth miner",
         "claim": "The White House took a 10% stake in USA Rare Earth as part of a $1.6 billion "
                  "investment in a domestic mine and magnet facility.",
         "domain": "policy", "actor": ["white-house", "usa-rare-earth"], "score": "$1.6B / 10%",
         "evidences": ["science-as-industrial-policy", "silicon-curtain"],
         "supersedes": [B + "developments/2026-01-05-zero-emission-rare-earths"]},
        {"id": "2026-01-26-vr-winter",
         "title": "Meta's pivot chills virtual reality into a winter",
         "claim": "Meta's pivot from virtual reality to AI and smart glasses has chilled the VR "
                  "industry, with some expecting a VR winter.",
         "domain": "economics", "actor": ["meta"],
         "evidences": ["consumer-deprioritized"],
         "supersedes": [B + "developments/2026-01-13-meta-compute-tens-of-gigawatts"]},
        {"id": "2026-01-26-a7a5-stablecoin-100b",
         "title": "A sanctions-evading stablecoin passes $100B in transactions",
         "claim": "The ruble-backed A7A5 stablecoin, created to circumvent restrictions on "
                  "Russia, passed $100 billion in transactions in under a year.",
         "domain": "policy", "score": "$100B",
         "evidences": ["autonomous-commerce", "regulatory-exit"]},
        {"id": "2026-01-26-insurer-halves-rates-for-fsd",
         "title": "An insurer cuts rates 50% when autonomy is engaged",
         "claim": "Lemonade will offer Tesla drivers a 50% rate cut while Full Self-Driving is "
                  "engaged, citing reduced accident data.",
         "domain": "economics", "actor": ["lemonade", "tesla"], "score": "-50%",
         "evidences": ["autonomy-clock-speed", "autonomous-commerce"],
         "body": "The actuarial tables vote for the machine."},
        {"id": "2026-01-26-starship-v4-10000-tons",
         "title": "Starship V4 targets three times the Saturn V",
         "claim": "Elon Musk set a stretch goal of 300 tons of thrust per engine across 33 "
                  "engines for Starship V4, roughly three times the Saturn V.",
         "domain": "space", "actor": ["spacex"], "score": "10,000 tons",
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-05-spacex-10000-starships"]},
        {"id": "2026-01-26-mercor-2m-a-day",
         "title": "One platform pays experts $2 million a day",
         "claim": "Mercor now pays about $2 million daily to 30,000 experts for training data "
                  "at an average above $95 an hour, with radiologists earning up to $375.",
         "domain": "economics", "actor": ["mercor"], "score": "$2M/day / $375/hr",
         "evidences": ["data-beyond-text", "work-displaced"],
         "supersedes": [B + "developments/2026-01-15-kled-3m-files-a-day"]},
        {"id": "2026-01-26-reverse-prompting-a-ceo",
         "title": "A CEO asks the model to manage him",
         "claim": "Coinbase's CEO began reverse prompting, asking AI agents with access to "
                  "every internal message and document what he should be thinking about and "
                  "working on.",
         "domain": "economics", "actor": ["coinbase"],
         "evidences": ["agents-on-the-org-chart", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-01-24-cursor-planners-and-workers"],
         "body": "The org chart inverts at the top as well as the bottom."},
        {"id": "2026-01-26-a-third-of-workers-expect-obsolescence",
         "title": "More than a third of workers expect parts of their job to vanish",
         "claim": "More than a third of workers now worry AI will make some or all of their job "
                  "duties obsolete, while Demis Hassabis declined the possibility of running "
                  "Google because it would leave no time for serious thinking.",
         "domain": "society", "actor": ["people/demis-hassabis"], "score": ">33%",
         "evidences": ["work-displaced", "cognitive-load-inverted"]},
    ],
}
