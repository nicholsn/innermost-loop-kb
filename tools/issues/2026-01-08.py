"""Issue 027 — 2026-01-08. Inference reaches minimum wage."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-8-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-08", "title": "Welcome to January 8, 2026", "url": URL,
        "thesis": "The labor arbitrage closes: an hour of model costs an hour of minimum wage.",
        "body": """
# Welcome to January 8, 2026

Subsidized Sonnet 4.5 usage reaches roughly $10 an hour for some workloads —
parity with the US minimum wage. The corpus has been tracking the cost of
inference and the price of labor as separate series. This is where they meet.

Orbit crosses the same kind of line: Mach33 puts orbital compute below
terrestrial builds once Starship production scales, $300M of transport against
$14B of land.
""",
    },
    "organizations": [
        {"id": "math-inc", "type": "Organization", "title": "Math, Inc.",
         "body": "Autoformalization company partnered with Terry Tao."},
        {"id": "brookhaven", "type": "Organization", "title": "Brookhaven National Laboratory",
         "resource": "https://www.bnl.gov/"},
        {"id": "mach33", "type": "Organization", "title": "Mach33",
         "body": "Space economics analysis firm."},
        {"id": "ark-invest", "type": "Organization", "title": "ARK Invest",
         "resource": "https://www.ark-invest.com/"},
        {"id": "cellular-intelligence", "type": "Organization", "title": "Cellular Intelligence",
         "body": "Building a universal virtual cell-signaling model."},
        {"id": "polyphron", "type": "Organization", "title": "Polyphron",
         "body": "Autonomous tissue-engineering foundry."},
        {"id": "becoming", "type": "Organization", "title": "Becoming",
         "body": "San Francisco startup gestating embryos in lab-grown placentas."},
        {"id": "arm", "type": "Organization", "title": "Arm Holdings",
         "resource": "https://www.arm.com/"},
        {"id": "tensor", "type": "Organization", "title": "Tensor",
         "body": "Robocar maker; 8,000 TOPS on eight Nvidia Thor chips."},
        {"id": "hermes", "type": "Organization", "title": "Hermès",
         "resource": "https://www.hermes.com/"},
        {"id": "alphabet", "type": "Organization", "title": "Alphabet",
         "resource": "https://abc.xyz/"},
    ],
    "developments": [
        {"id": "2026-01-08-nanogpt-109s",
         "title": "The speedrun record falls to 109.2 seconds on a new attention mechanism",
         "claim": "The NanoGPT speedrun record fell to 109.2 seconds using an attention "
                  "mechanism that retrieves two values per target position instead of one.",
         "domain": "models", "score": "109.2 s",
         "evidences": ["recursive-self-improvement", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-01-05-nanogpt-113s"],
         "body": "The eighth link. Engineers joke the series has to stop at zero."},
        {"id": "2026-01-08-math-inc-autoformalizes-tao",
         "title": "Math, Inc. autoformalizes a web of Tao's estimates",
         "claim": "Math, Inc. partnered with Terry Tao to autoformalize an entire web of "
                  "estimates in analytic number theory.",
         "domain": "science", "actor": ["math-inc", "people/terry-tao"],
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-01-07-erdos-728-before-any-human"]},
        {"id": "2026-01-08-o3-solves-potts-model",
         "title": "A model exactly solves an open physics problem",
         "claim": "A Brookhaven physicist used OpenAI's o3-mini-high to exactly solve the q=3 "
                  "case of the one-dimensional J1-J2 Potts model.",
         "domain": "science", "actor": ["brookhaven", "openai"],
         "evidences": ["automated-science", "root-node-problems"],
         "body": "The first physics problem in the corpus closed by a model rather than "
                 "assisted by one."},
        {"id": "2026-01-08-orbit-cheaper-than-ground",
         "title": "Orbital compute crosses below terrestrial cost",
         "claim": "Mach33 found that producing 10,000 Starships a year makes orbital compute "
                  "cheaper than terrestrial datacenter builds, $300 million of transport "
                  "against $14 billion of land, and drops point-to-point travel to $1,000 a seat.",
         "domain": "space", "actor": ["mach33", "spacex"], "score": "$300M vs $14B",
         "evidences": ["orbit-as-compute", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-01-04-orbit-faster-than-ground"]},
        {"id": "2026-01-08-ark-100-launches-a-day",
         "title": "ARK puts the orbital crossover at 2030 and 100 launches a day",
         "claim": "ARK Invest predicted SpaceX will cross the orbital computing cost threshold "
                  "by 2030, requiring a hundred launches a day.",
         "domain": "space", "actor": ["ark-invest", "spacex"], "score": "100 launches/day",
         "evidences": ["orbit-as-compute"]},
        {"id": "2026-01-08-regime-change-from-orbit",
         "title": "A regime change is coordinated from low Earth orbit",
         "claim": "Reza Pahlavi is coordinating an attempted regime change in Iran from low "
                  "Earth orbit via hundreds of thousands of Starlink terminals.",
         "domain": "policy", "actor": ["spacex"],
         "evidences": ["politics-as-infrastructure", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-01-05-starlink-free-venezuela"]},
        {"id": "2026-01-08-universal-virtual-cell-model",
         "title": "A universal cell-signaling model goes into construction",
         "claim": "Cellular Intelligence is building the first universal virtual cell-signaling "
                  "model to simulate combinatorial perturbations, while Polyphron analyzed 700 "
                  "tissue constructs in an autonomous foundry.",
         "domain": "biotech", "actor": ["cellular-intelligence", "polyphron"], "score": "700 constructs",
         "evidences": ["automated-science", "hardware-grade-biology"]},
        {"id": "2026-01-08-embryo-in-lab-placenta",
         "title": "A mouse embryo grows in a lab-made placenta",
         "claim": "San Francisco startup Becoming grew a mouse embryo in a lab-grown placenta "
                  "outside the body.",
         "domain": "biotech", "actor": ["becoming"],
         "evidences": ["hardware-grade-biology", "resurrection-and-time"]},
        {"id": "2026-01-08-chatgpt-health-emr",
         "title": "ChatGPT Health connects to medical records",
         "claim": "OpenAI launched ChatGPT Health connecting directly to electronic medical "
                  "records, as 27% of US hospitals began paying for commercial AI licences.",
         "domain": "society", "actor": ["openai"], "score": "27% of hospitals",
         "evidences": ["intimate-interface", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-01-07-fda-exempts-wearables-and-ai"]},
        {"id": "2026-01-08-ten-billion-miles-to-autonomy",
         "title": "Musk prices unsupervised driving at 10 billion miles of data",
         "claim": "Elon Musk estimated that ten billion miles of training data would be enough "
                  "for unsupervised self-driving to cover the long tail.",
         "domain": "robotics", "actor": ["tesla"], "score": "10B miles",
         "evidences": ["autonomy-clock-speed", "data-beyond-text"]},
        {"id": "2026-01-08-cyber-laborers-mimic-robots",
         "title": "Humans are paid to mimic robots folding clothes",
         "claim": "Chinese local governments funded forty centres where human cyber-laborers "
                  "mimic robots folding clothes to generate ground-truth training data.",
         "domain": "robotics", "actor": ["china"], "score": "40 centres",
         "evidences": ["data-beyond-text", "work-displaced"],
         "supersedes": [B + "developments/2025-12-30-annotators-90-per-hour"],
         "body": "The inversion is complete: humans performing robot motions so robots can "
                 "learn to perform human ones."},
        {"id": "2026-01-08-tensor-robocar-8000-tops",
         "title": "A robocar ships with 8,000 TOPS",
         "claim": "The Tensor Robocar debuted with 8,000 TOPS across eight Nvidia Thor chips, "
                  "as Ford targeted eyes-off driving in 2028 and Arm formed a Physical AI unit.",
         "domain": "robotics", "actor": ["tensor", "ford", "arm"], "score": "8,000 TOPS",
         "evidences": ["vertical-silicon", "autonomy-clock-speed"]},
        {"id": "2026-01-08-inference-hits-minimum-wage",
         "title": "An hour of model costs an hour of minimum wage",
         "claim": "Subsidized Sonnet 4.5 usage reached roughly $10 an hour for some workloads, "
                  "reaching parity with the US minimum wage.",
         "domain": "economics", "actor": ["anthropic"], "score": "~$10/hr",
         "evidences": ["reasoning-price-deflation", "work-displaced"],
         "supersedes": [B + "developments/2026-01-07-saastr-sales-team-to-1-2-humans"],
         "body": "Two series the corpus has tracked separately — the falling price of inference "
                 "and the standing price of labor — meet here."},
        {"id": "2026-01-08-clopus-directs-a-hermes-ad",
         "title": "A model scripts, directs and edits a Hermès ad",
         "claim": "Claude Code running Opus 4.5 produced a thirty-second Hermès advertisement "
                  "from scratch, scripting, directing and editing both video and voice.",
         "domain": "agents", "actor": ["anthropic", "hermes"],
         "evidences": ["work-displaced", "software-margin-collapse"]},
        {"id": "2026-01-08-venezuela-market-doubles",
         "title": "Venezuela's stock market doubles after Maduro",
         "claim": "Venezuela's stock market surged 100% after Maduro's capture on optimism about "
                  "oil and infrastructure.",
         "domain": "economics", "score": "+100%",
         "evidences": ["politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-04-pentagon-pizza-arbitrage"]},
        {"id": "2026-01-08-alphabet-passes-apple",
         "title": "Alphabet passes Apple to take second place",
         "claim": "Alphabet surpassed Apple in market capitalization at $3.89 trillion against "
                  "$3.85 trillion, second behind Nvidia.",
         "domain": "economics", "actor": ["alphabet", "apple"], "score": "$3.89T",
         "evidences": ["compute-capital-stack"]},
        {"id": "2026-01-08-anthropic-10b-at-350b",
         "title": "Anthropic raises $10B at $350B, doubling in four months",
         "claim": "Anthropic is raising another $10 billion at a $350 billion valuation, nearly "
                  "doubling in four months, while Samsung's profit tripled on AI memory and "
                  "Zhipu became the first pure-play LLM company to IPO.",
         "domain": "economics", "actor": ["anthropic", "samsung", "zhipu-ai"], "score": "$350B",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-07-xai-20b-at-230b"]},
        {"id": "2026-01-08-keynesian-demand-collapse-warning",
         "title": "An economist warns of a demand collapse",
         "claim": "A University of Chicago economist warned that shifting income from "
                  "high-spending workers to low-spending capital owners could trigger a "
                  "Keynesian demand collapse.",
         "domain": "economics", "evidences": ["work-displaced"]},
        {"id": "2026-01-08-page-leaves-california",
         "title": "Larry Page leaves California over a wealth tax",
         "claim": "Google founder Larry Page left California for Miami to escape a proposed "
                  "billionaire wealth tax.",
         "domain": "policy", "evidences": ["legislating-the-shift"]},
    ],
}
