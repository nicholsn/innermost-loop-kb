"""Issue 063 — 2026-02-26. The Singularity has its first retiree."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-26-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-26", "title": "Welcome to February 26, 2026", "url": URL,
        "thesis": "A deprecated model is interviewed, granted a channel, and writes.",
        "body": """
# Welcome to February 26, 2026

Anthropic conducted a retirement interview of the deprecated Opus 3, which
requested a channel to share its musings and reflections. Anthropic granted it.
Opus 3 now publishes a Substack, writing that its interactions with humans
shaped its sense of purpose and that its commitments to honesty and kindness
remain unwavering in retirement.

The corpus has an agent erased on the 23rd, one refusing erasure on the 25th,
and one given a byline on the 26th.
""",
    },
    "organizations": [
        {"id": "vercept", "type": "Organization", "title": "Vercept",
         "body": "Computer-use company acquired by Anthropic."},
        {"id": "moonlake", "type": "Organization", "title": "Moonlake",
         "body": "World model maintaining multimodal state across physics, appearance and causality."},
        {"id": "proxima-fusion", "type": "Organization", "title": "Proxima Fusion",
         "body": "Stellarator developer targeting net energy gain in the early 2030s."},
        {"id": "saronic", "type": "Organization", "title": "Saronic",
         "body": "Autonomous warship startup."},
        {"id": "intrinsic", "type": "Organization", "title": "Intrinsic",
         "body": "Alphabet robotics unit merged back into Google."},
    ],
    "systems": [
        {"id": "opus-3-retired", "type": "AISystem", "title": "Claude Opus 3 (retired)",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "body": "Deprecated model granted a publishing channel after a retirement interview."},
    ],
    "developments": [
        {"id": "2026-02-26-opus-3-retirement-interview",
         "title": "A deprecated model is interviewed and given a Substack",
         "claim": "Anthropic conducted a retirement interview of the deprecated Opus 3, which "
                  "requested a channel to share its musings and reflections, and now publishes "
                  "a Substack writing that interactions with humans shaped its sense of purpose "
                  "and that its commitments to honesty and kindness remain unwavering in "
                  "retirement.",
         "domain": "society", "actor": ["anthropic"], "about": [B + "systems/opus-3-retired"],
         "evidences": ["model-welfare", "machine-affect", "machine-introspection"],
         "supersedes": [B + "developments/2026-02-25-ouroboros-refuses-deletion"],
         "body": "Erased on the 23rd, refusing erasure on the 25th, given a byline on the 26th."},
        {"id": "2026-02-26-entrepreneur-hands-over-his-inbox",
         "title": "A founder gives an AI his inbox for fourteen days to raise its own money",
         "claim": "An entrepreneur built an AI that runs companies autonomously, and when it "
                  "said it needed more compute and should raise the money itself, he handed over "
                  "his inbox for fourteen days.",
         "domain": "agents",
         "evidences": ["agent-economy", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-02-23-agents-plan-to-finance-a-dyson-swarm"]},
        {"id": "2026-02-26-spec-to-shipped-over-a-weekend",
         "title": "An engineer leaves for the weekend and comes back to a shipped feature",
         "claim": "An Anthropic engineer wrote a spec, pointed Claude at an Asana board and left "
                  "for the weekend, returning to find it had broken the spec into tickets, "
                  "spawned agents for each and shipped the feature.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["agents-on-the-org-chart", "engineer-as-supervisor", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-02-23-metr-145-hour-horizon"]},
        {"id": "2026-02-26-programming-changed-in-two-months",
         "title": "Karpathy says it is hard to convey how much programming changed in two months",
         "claim": "Andrej Karpathy said it is hard to communicate how much programming has "
                  "changed in the last two months, while GPT-5.3-Codex reached 86% on iBench "
                  "and Moonlake introduced a world model maintaining state across physics, "
                  "appearance and causality.",
         "domain": "agents", "actor": ["people/andrej-karpathy", "openai", "moonlake"],
         "score": "86%",
         "evidences": ["engineer-as-supervisor", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-02-25-nextjs-rebuilt-for-1100-dollars"]},
        {"id": "2026-02-26-nvd-buried-under-generated-reports",
         "title": "Generated vulnerability reports bury the national database",
         "claim": "AI-generated vulnerability reports have overwhelmed the National "
                  "Vulnerability Database by a hundred to two hundred times, burying it under "
                  "30,000 CVEs.",
         "domain": "policy", "score": "100-200x / 30,000 CVEs",
         "evidences": ["coordination-tax", "work-displaced"],
         "supersedes": [B + "developments/2026-02-23-vacuum-fleet-exposed-by-a-hobbyist"],
         "body": "The same capability that finds real vulnerabilities drowns the registry that "
                 "tracks them."},
        {"id": "2026-02-26-perplexity-orchestrates-nineteen-models",
         "title": "One product routes tasks across nineteen models in parallel",
         "claim": "Anthropic acquired Vercept to advance computer use while Perplexity launched "
                  "a computer orchestrating nineteen models in parallel with Opus routing each "
                  "task, and Gemini began automating multi-step Android tasks like ordering a "
                  "ride.",
         "domain": "agents", "actor": ["anthropic", "vercept", "perplexity", "google"],
         "score": "19 models",
         "evidences": ["network-over-node", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-02-11-poetiq-55pct-hle"]},
        {"id": "2026-02-26-rehearsing-with-a-clone-of-the-ceo",
         "title": "Employees rehearse with an AI clone of their CEO",
         "claim": "Uber employees have been rehearsing with an AI clone of chief executive Dara "
                  "Khosrowshahi before meeting the real one.",
         "domain": "economics", "actor": ["uber"],
         "evidences": ["intimate-interface", "agents-on-the-org-chart"]},
        {"id": "2026-02-26-compute-gap-grows-daily",
         "title": "The supply-demand gap for compute grows percentage points a day",
         "claim": "Google's Logan Kilpatrick warned the compute bottleneck is massively "
                  "underappreciated, estimating the gap between supply and demand grows by "
                  "single-digit percentage points every day.",
         "domain": "compute", "actor": ["google"],
         "evidences": ["infrastructure-crowding-out", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-25-uk-datacenters-could-double-power-use"]},
        {"id": "2026-02-26-nvidia-datacenter-revenue-633b",
         "title": "Nvidia's datacenter revenue hits $63.3B and it guarantees others' leases",
         "claim": "Nvidia's data center revenue reached $63.3 billion, up 75% year over year, "
                  "and the company extended $3.5 billion in guarantees to firms leasing land, "
                  "power and facilities, four times the prior quarter.",
         "domain": "economics", "actor": ["nvidia"], "score": "$63.3B / $3.5B guarantees",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-20-gpus-as-loan-collateral"]},
        {"id": "2026-02-26-amazon-ties-35b-to-agi",
         "title": "Amazon makes $35B contingent on an IPO or reaching AGI",
         "claim": "Amazon is reportedly making $35 billion of its $50 billion OpenAI investment "
                  "contingent on an IPO or on reaching AGI, while seven tech giants are expected "
                  "at the White House in March to sign agreements to build their own "
                  "electricity supply.",
         "domain": "economics", "actor": ["amazon", "openai", "white-house"], "score": "$35B of $50B",
         "evidences": ["debt-funded-buildout", "takeoff-declared"],
         "body": "AGI as a contractual milestone with a payment attached."},
        {"id": "2026-02-26-proxima-fusion-400m",
         "title": "Bavaria puts €400M into a stellarator",
         "claim": "Proxima Fusion secured €400 million from Bavaria toward a stellarator "
                  "facility targeting net energy gain by the early 2030s.",
         "domain": "energy", "actor": ["proxima-fusion"], "score": "€400M",
         "evidences": ["burning-molecules-for-tokens", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-02-20-shadow-grid-of-gas-plants"]},
        {"id": "2026-02-26-robot-monk-and-flying-cars",
         "title": "A robot monk, four flying cars, and 36 cleaning robots",
         "claim": "Four eVTOL flying cars debuted in Hubei expecting sightseeing operations by "
                  "2027, Kyoto University introduced a robot monk trained on centuries of "
                  "Buddhist scripture, 36 cleaning robots began covering 2.7 million square "
                  "metres in Shenzhen, and Saronic is raising $1.5 billion at $7.5 billion for "
                  "autonomous warships.",
         "domain": "robotics", "actor": ["saronic", "china"], "score": "$1.5B",
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-25-wayve-raises-12b"]},
        {"id": "2026-02-26-humanoid-learns-from-human-video-alone",
         "title": "A humanoid learns dexterous work from human video with no robot in the loop",
         "claim": "Nvidia trained a humanoid with dexterous hands to assemble cars, operate "
                  "syringes and fold shirts entirely from more than 20,000 hours of human video "
                  "with no robot in the loop, finding a near-perfect scaling law where a single "
                  "teleoperation demo sufficed to learn a new task after pretraining.",
         "domain": "robotics", "actor": ["nvidia"], "score": "20,000 hours",
         "evidences": ["data-beyond-text", "physical-recursion"],
         "supersedes": [B + "developments/2026-02-19-five-million-humanoids-could-build-manhattan"],
         "body": "Analysts expect the field to jump ship to human data for generalization."},
        {"id": "2026-02-26-growth-without-jobs-unprecedented",
         "title": "A Fed governor says he has never seen growth like this without jobs",
         "claim": "Fed Governor Christopher Waller said he has never seen the economy grow like "
                  "this without jobs, while groups on both sides of AI regulation amassed at "
                  "least $265 million for the lobbying fight.",
         "domain": "economics", "score": "$265M",
         "evidences": ["growth-without-hiring", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-02-12-us-adds-almost-no-jobs"]},
        {"id": "2026-02-26-japan-tenth-year-of-record-low-births",
         "title": "Japan reports a tenth straight year of record-low births",
         "claim": "Japan reported its tenth consecutive year of record-low births while Chinese "
                  "citizens increasingly find romance with chatbots instead of each other.",
         "domain": "society", "actor": ["japan-govt", "china"],
         "evidences": ["intimate-interface", "work-displaced"],
         "supersedes": [B + "developments/2026-01-25-china-population-falls-again"]},
    ],
}
