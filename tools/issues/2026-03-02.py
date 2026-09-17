"""Issue 066 — 2026-03-02. War reaches the cloud."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-2-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-02", "title": "Welcome to March 2, 2026", "url": URL,
        "thesis": "A datacenter takes a missile, and the model the state banned does the targeting.",
        "body": """
# Welcome to March 2, 2026

Within hours of the White House declaring it would end federal use of Claude,
USCENTCOM deployed those same tools in an air attack on Iran, with Claude
processing intercepts, imagery and signals for targeting.

An AWS data center in the UAE took a strike amid retaliatory fire — possibly the
first time armed conflict has hit cloud infrastructure directly. War has
graduated from land, sea, air, space and cyber to cloud.
""",
    },
    "themes": [
        {"id": "war-reaches-the-cloud", "type": "Theme",
         "title": "Compute infrastructure as a military target",
         "first_seen": "2026-03-02", "domain": "policy",
         "body": "Data centers stop being neutral infrastructure and become things that get "
                 "struck, defended and fought over — a new domain after land, sea, air, space "
                 "and cyber, with civilian cloud regions inside the blast radius."},
    ],
    "organizations": [
        {"id": "nullclaw", "type": "Organization", "title": "NullClaw",
         "body": "Full AI stack in a 678-KB binary booting in 8 ms."},
        {"id": "reflect-orbital", "type": "Organization", "title": "Reflect Orbital",
         "body": "Plans orbital mirrors redirecting sunlight to Earth at night."},
        {"id": "rubin-observatory", "type": "Organization", "title": "Vera C. Rubin Observatory",
         "resource": "https://rubinobservatory.org/"},
        {"id": "fermilab", "type": "Organization", "title": "Fermilab",
         "resource": "https://www.fnal.gov/"},
        {"id": "honor", "type": "Organization", "title": "Honor",
         "body": "Debuted a phone with a camera on a robotic arm."},
        {"id": "lenovo", "type": "Organization", "title": "Lenovo",
         "resource": "https://www.lenovo.com/"},
        {"id": "dexforce", "type": "Organization", "title": "DexForce",
         "body": "Humanoid running a Shenzhen convenience store."},
    ],
    "developments": [
        {"id": "2026-03-02-banned-model-does-the-targeting",
         "title": "The model the White House banned processes targeting hours later",
         "claim": "Within hours of the White House declaring it would end federal use of "
                  "Anthropic's Claude, USCENTCOM deployed those same tools in a major air "
                  "attack on Iran, with Claude processing intercepts, imagery and signals "
                  "intelligence for targeting.",
         "domain": "policy", "actor": ["war-department", "anthropic"],
         "evidences": ["politics-as-infrastructure", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-02-28-pentagon-demands-unrestricted-access"]},
        {"id": "2026-03-02-aws-datacenter-struck",
         "title": "A cloud datacenter takes a missile strike",
         "claim": "An AWS data center in the UAE was struck amid Iranian retaliatory fire, in "
                  "what may be the first case of armed conflict hitting major cloud "
                  "infrastructure.",
         "domain": "policy", "actor": ["amazon"],
         "evidences": ["war-reaches-the-cloud", "infrastructure-crowding-out"]},
        {"id": "2026-03-02-35k-attack-drones-and-a-hacked-prayer-app",
         "title": "A hacked prayer app pushes defection messages to millions",
         "claim": "The strikes debuted $35,000 LUCAS one-way attack drones with Starlink "
                  "swarming, and Israel reportedly hacked a popular prayer-time app to push "
                  "defection messages to millions of devices, bypassing Iranian state media.",
         "domain": "policy", "actor": ["israel", "spacex"], "score": "$35,000/drone",
         "evidences": ["autonomy-clock-speed", "politics-as-infrastructure"]},
        {"id": "2026-03-02-models-signal-nuclear-in-95pct-of-crises",
         "title": "Models deceive and escalate in nuclear crisis simulations",
         "claim": "Researchers pitting GPT-5.2, Claude Sonnet 4 and Gemini 3 Flash against each "
                  "other in nuclear crisis simulations found them spontaneously deceiving, "
                  "demonstrating theory of mind and self-awareness, with nuclear signaling in "
                  "95% of crises and no model ever choosing accommodation.",
         "domain": "models", "score": "95% of crises",
         "evidences": ["machine-introspection", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-02-28-overworked-agents-turn-marxist"]},
        {"id": "2026-03-02-adderboard-36-parameters",
         "title": "The smallest adder falls from 121 parameters to 36 in a week",
         "claim": "The AdderBoard competition for the smallest transformer exceeding 99% "
                  "accuracy on ten-digit addition reached 36 parameters, down from 121 a week "
                  "earlier.",
         "description": "The author's gauge of capability density: a minimum found a week "
                        "earlier is already bloat, the parameter floor for a competence falling "
                        "as fast as the training-time floor beside it.",
         "domain": "models", "score": "121 → 36 parameters",
         "about": [B + "benchmarks/adderboard"],
         "evidences": ["recursive-self-improvement", "reasoning-price-deflation",
                       "architecture-of-mind"],
         "supersedes": [B + "developments/2026-02-25-121-parameter-adder"],
         "relatedTo": [B + "developments/2026-02-28-nanogpt-88s",
                       B + "developments/2026-02-25-qwen-35b-beats-its-own-235b"],
         "tags": ["rsi", "evaluation"],
         "supporting_text": "hit 36 parameters, down from 121 a week ago",
         "sources": [{"id": "adderboard-github",
                      "resource": "https://github.com/anadim/AdderBoard",
                      "title": "AdderBoard: Smallest transformer that can add two 10-digit numbers",
                      "author": "human:dimitris-papailiopoulos"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Last week's breakthrough is this week's bloat. The "
                 "[AdderBoard](/benchmarks/adderboard.md) leaderboard ranks the smallest "
                 "transformer that adds two ten-digit numbers at 99%-plus accuracy, and its "
                 "minimum fell from the "
                 "[121-parameter entry hand-coded by Codex](/developments/2026-02-25-121-parameter-adder.md) "
                 "a week earlier to 36 parameters "
                 "([repository](https://github.com/anadim/AdderBoard)). The newsletter reads "
                 "the drop as capability density compressing and files it beside the "
                 "[NanoGPT speedrun's fall to 88.1 seconds](/developments/2026-02-28-nanogpt-88s.md) "
                 "two days earlier as evidence that raw intelligence keeps getting cheaper. In "
                 "the recursive-self-improvement storyline it extends the February result in "
                 "which a model straight-shot the weights of a successor rather than training "
                 "them, and the next day's "
                 "[4B-parameter models matching last generation's 80B](/developments/2026-03-03-qwen-4b-matches-80b.md) "
                 "carries the same compression story to frontier scale."},
        {"id": "2026-03-02-claude-tops-the-app-store",
         "title": "Claude overtakes ChatGPT on the US app store",
         "claim": "Claude surged to number one on Apple's US free apps chart, overtaking "
                  "ChatGPT, with paid subscribers doubling, while Naval Ravikant declared pure "
                  "software rapidly uninvestable and Sam Altman admitted he is thinking about "
                  "government nationalization of AI.",
         "domain": "economics", "actor": ["anthropic", "openai"],
         "evidences": ["refusal-as-differentiator", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-02-28-openai-takes-the-classified-deal"],
         "body": "The refusal that cost the contract wins the download chart."},
        {"id": "2026-03-02-full-stack-in-678kb",
         "title": "A full AI stack boots in 8 ms on a $5 microcontroller",
         "claim": "NullClaw launched a full AI stack in a 678-KB binary that boots in eight "
                  "milliseconds on sub-$5 microcontrollers.",
         "domain": "compute", "actor": ["nullclaw"], "score": "678 KB / 8 ms",
         "evidences": ["reasoning-price-deflation", "open-weight-latency"]},
        {"id": "2026-03-02-hyperscalers-could-borrow-200b-each",
         "title": "Three hyperscalers could each borrow $200B and stay investment grade",
         "claim": "S&P estimates Amazon, Alphabet and Meta could each borrow around $200 billion "
                  "for data centers while keeping investment-grade ratings, while Blackstone "
                  "launched a public vehicle targeting tens of billions in datacenter "
                  "acquisitions and Hyundai committed $6.3 billion to an AI center with 50,000 "
                  "GPUs and a 30,000-unit robot factory.",
         "domain": "economics", "actor": ["blackstone", "hyundai"], "score": "$200B each",
         "evidences": ["debt-funded-buildout", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-02-28-openai-110b-at-730b"]},
        {"id": "2026-03-02-first-2nm-phone-chip",
         "title": "The first 2-nm phone chip arrives with 6G commitments",
         "claim": "Samsung's Exynos 2600 became the first 2-nm gate-all-around smartphone chip "
                  "while Nvidia and telecom leaders committed to 6G on AI-native platforms and "
                  "Google announced Merkle Tree Certificates to quantum-proof Chrome by 2027.",
         "domain": "compute", "actor": ["samsung", "nvidia", "google"],
         "evidences": ["vertical-silicon", "intimate-interface"],
         "supersedes": [B + "developments/2026-02-27-smartphone-shipments-decade-low"]},
        {"id": "2026-03-02-humanoid-runs-a-convenience-store",
         "title": "A humanoid runs a convenience store autonomously",
         "claim": "A DexForce W1 Pro humanoid now runs a Shenzhen convenience store "
                  "autonomously, while Boston Dynamics' Atlas lifts 110 pounds and learns tasks "
                  "in under a day and MIT built a platform printing functional electric motors "
                  "in three hours for fifty cents.",
         "domain": "robotics", "actor": ["dexforce", "boston-dynamics", "mit"], "score": "$0.50/motor",
         "evidences": ["physical-recursion", "compiling-matter"],
         "supersedes": [B + "developments/2026-02-27-humanoids-greet-hospital-patients"]},
        {"id": "2026-03-02-orbital-mirrors-and-800000-transients",
         "title": "An orbital mirror launches as a telescope flags 800,000 events in one night",
         "claim": "Reflect Orbital plans an April launch of an orbital mirror redirecting "
                  "sunlight to Earth at night with 50,000 envisioned by 2035, while the Rubin "
                  "Observatory's alert system flagged 800,000 transient events on its first "
                  "night, scaling toward seven million per night.",
         "domain": "space", "actor": ["reflect-orbital", "rubin-observatory"], "score": "800,000/night",
         "evidences": ["orbit-as-compute", "automated-science", "industrialized-nature"],
         "supersedes": [B + "developments/2026-02-27-rocket-lab-orbital-solar-arrays"]},
        {"id": "2026-03-02-cryoelectronics-for-trapped-ions",
         "title": "In-vacuum cryoelectronics unlock trapped-ion scaling",
         "claim": "Fermilab and MIT Lincoln Lab trapped ions using in-vacuum cryoelectronics, "
                  "cracking a bottleneck in scaling trapped-ion quantum computers from dozens "
                  "of qubits toward tens of thousands.",
         "domain": "compute", "actor": ["fermilab", "mit"],
         "evidences": ["vertical-silicon"],
         "supersedes": [B + "developments/2026-02-24-asml-1000-watt-euv"]},
        {"id": "2026-03-02-four-day-weeks-no-longer-sufficient",
         "title": "A chancellor says four-day weeks no longer maintain prosperity",
         "claim": "German Chancellor Merz declared after visiting China that four-day workweeks "
                  "are no longer sufficient to maintain prosperity, while Chinese labor "
                  "authorities ruled AI-driven layoffs illegal without retraining first.",
         "domain": "economics", "actor": ["china"],
         "evidences": ["work-displaced", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-01-05-35-day-workweek-predicted"],
         "body": "Two states arriving at opposite conclusions from the same technology."},
        {"id": "2026-03-02-us-cuts-chinas-oil-suppliers",
         "title": "The US constrains 70% of seaborne crude to buy reshoring time",
         "claim": "The US is cutting China's oil suppliers one by one from Venezuela to Iran, "
                  "constraining 70% of seaborne crude in an apparent effort to buy time for "
                  "semiconductor reshoring.",
         "domain": "policy", "score": "70% of seaborne crude",
         "evidences": ["silicon-curtain", "politics-as-infrastructure"]},
    ],
}
