"""Issue 120 — 2026-05-20. Training Claude to accelerate Claude."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-20-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-20", "title": "Welcome to May 20, 2026", "url": URL,
        "thesis": "The loop acquires a named owner.",
        "body": """
# Welcome to May 20, 2026

Andrej Karpathy joined Anthropic to lead pre-training — essentially training
Claude to accelerate Claude. The corpus has recorded recursive self-improvement
as a claim, a probability and a present phenomenon. Now it has a job title.

Google is processing 3.2 quadrillion tokens a month, up from 9.7 trillion two
years ago.
""",
    },
    "organizations": [
        {"id": "armada", "type": "Organization", "title": "Armada",
         "body": "Raised $230M to mass-produce modular datacenters."},
        {"id": "standard-chartered", "type": "Organization", "title": "Standard Chartered",
         "resource": "https://www.sc.com/"},
        {"id": "minnesota", "type": "Organization", "title": "State of Minnesota"},
        {"id": "astrolight", "type": "Organization", "title": "Astrolight",
         "body": "Opened an ESA-backed CubeSat laser-link station in Greece."},
        {"id": "ice-exchange", "type": "Organization", "title": "ICE",
         "resource": "https://www.ice.com/"},
    ],
    "people": [
        {"id": "noam-brown", "type": "Person", "title": "Noam Brown", "name": "Noam Brown",
         "description": "Artificial-intelligence researcher at OpenAI who framed Karpathy's move to "
                        "Anthropic as frontier labs collectively advancing one technology rather "
                        "than a zero-sum transfer.",
         "resource": "https://x.com/polynoamial",
         "sameAs": ["http://www.wikidata.org/entity/Q89662566"],
         "tags": ["researcher"],
         "body": "Noam Brown is an artificial-intelligence researcher at [OpenAI](/organizations/openai.md). "
                 "In this corpus he appears once, responding to [Andrej Karpathy](/people/andrej-karpathy.md)'s "
                 "move to Anthropic: he said he would have loved for Karpathy to rejoin OpenAI but "
                 "was happy to see him at any frontier lab, and rejected the zero-sum framing in "
                 "favour of labs 'collectively advancing the most important tech of our era' "
                 "([post](https://x.com/polynoamial/status/2056768036837949914)), the remark the "
                 "newsletter attached to [the loop acquiring a job title](/developments/2026-05-20-karpathy-joins-to-lead-pretraining.md)."},
    ],
    "roles": [
        {"id": "noam-brown-openai-researcher", "type": "Role",
         "title": "Noam Brown, researcher at OpenAI",
         "roleName": "Researcher",
         "memberOf": [B + "organizations/openai"],
         "holder": [B + "people/noam-brown"],
         "description": "The affiliation under which the newsletter quotes him, as 'OpenAI's Noam "
                        "Brown', reframing a rival lab's hire as a collective advance; neither the "
                        "newsletter nor his own post states a title.",
         "body": "The newsletter identifies him only as 'OpenAI's Noam Brown' when it records his "
                 "response to [Karpathy joining Anthropic](/developments/2026-05-20-karpathy-joins-to-lead-pretraining.md); "
                 "his own post says he would have loved for Karpathy to rejoin OpenAI. The role is "
                 "what gives the remark its weight: a researcher inside the rival lab describing "
                 "the frontier labs as one effort."},
    ],
    "developments": [
        {"id": "2026-05-20-karpathy-joins-to-lead-pretraining",
         "title": "The recursive loop acquires a job title",
         "claim": "Andrej Karpathy joined Anthropic to lead pre-training, essentially training "
                  "Claude to accelerate Claude, with OpenAI's Noam Brown reframing the hire as "
                  "frontier labs collectively advancing the most important technology of the "
                  "era.",
         "description": "The corpus has recorded recursive self-improvement as a claim, a "
                        "probability and a present phenomenon; here it becomes a named position at a "
                        "frontier lab, held by the person whose own optimization loop Claude had "
                        "already taken over.",
         "domain": "agents",
         "actor": ["anthropic", "people/andrej-karpathy", "openai", "people/noam-brown"],
         "about": [B + "systems/claude"],
         "occurred_on": "2026-05-19",
         "evidences": ["recursive-self-improvement", "coordination-tax"],
         "supersedes": [B + "developments/2026-05-15-agents-beat-the-human-speedrun-baseline",
                        B + "developments/2025-12-29-karpathy-claude-runs-nanochat"],
         "relatedTo": [B + "developments/2026-03-09-autoresearch-650-experiments",
                       B + "developments/2026-07-26-the-job-board-is-the-roadmap",
                       B + "developments/2026-08-13-a-cofounder-steers-toward-recursive-self-improvement"],
         "tags": ["rsi", "ai-r-and-d", "model-trains-model"],
         "supporting_text": "to lead pre-training (essentially training Claude to accelerate Claude)",
         "sources": [{"id": "karpathy-joins-anthropic-post",
                      "resource": "https://x.com/karpathy/status/2056753169888334312",
                      "title": "Personal update: I've joined Anthropic (X post)",
                      "author": "human:andrej-karpathy", "last_modified": "2026-05-19"},
                     {"id": "noam-brown-reframes-the-hire-post",
                      "resource": "https://x.com/polynoamial/status/2056768036837949914",
                      "title": "Noam Brown on Karpathy joining Anthropic (X post)",
                      "author": "human:noam-brown", "last_modified": "2026-05-19"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Karpathy announced on 19 May 2026 that he had joined Anthropic, saying the next "
                 "few years at the frontier of LLMs would be especially formative and that he "
                 "wanted to get back to R&D ([post](https://x.com/karpathy/status/2056753169888334312)); "
                 "the newsletter adds that he reports to Nick Joseph and leads pre-training, which "
                 "it glosses as training [Claude](/systems/claude.md) to accelerate Claude. The "
                 "position is recorded as a [Role](/roles/andrej-karpathy-anthropic-pretraining-lead.md) "
                 "in this corpus, and it closes an arc that began with Claude "
                 "[running every optimization experiment on his nanochat project](/developments/2025-12-29-karpathy-claude-runs-nanochat.md) "
                 "in December and his [650-experiment autoresearch loop](/developments/2026-03-09-autoresearch-650-experiments.md) "
                 "in March. OpenAI's [Noam Brown](/people/noam-brown.md) answered that he would "
                 "have loved for Karpathy to rejoin OpenAI but that the labs were 'collectively "
                 "advancing the most important tech of our era' "
                 "([post](https://x.com/polynoamial/status/2056768036837949914)). The "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) storyline has "
                 "moved from Altman's [production claim](/developments/2025-12-28-altman-self-improving-in-production.md) "
                 "through an alignment lead's [present phenomenon](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) "
                 "and Clark's [60% by 2028](/developments/2026-05-05-sixty-percent-odds-on-rsi-by-2028.md) "
                 "to a named owner; by August a Google co-founder would be reported "
                 "[steering resources toward it](/developments/2026-08-13-a-cofounder-steers-toward-recursive-self-improvement.md)."},
        {"id": "2026-05-20-three-point-two-quadrillion-tokens-a-month",
         "title": "One company processes 3.2 quadrillion tokens a month",
         "claim": "Google is processing 3.2 quadrillion tokens per month, up from 9.7 trillion "
                  "two years ago, while its assistant crossed 900 million monthly users and its "
                  "search AI mode passed a billion.",
         "domain": "compute", "actor": ["google"], "score": "9.7T → 3.2 quadrillion",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-14-doubling-time-compresses-to-45-months"]},
        {"id": "2026-05-20-gemini-35-flash-beats-the-pro-model",
         "title": "A fast model beats its own flagship while the flagship slips",
         "claim": "Google made Gemini 3.5 Flash generally available, beating its own Pro model "
                  "on terminal, economic-value, tool-use and chart benchmarks at roughly four "
                  "times the speed, while punting the Pro release by a month and collapsing "
                  "text, image, audio and video into one any-to-any model with provenance "
                  "watermarking built in.",
         "domain": "models", "actor": ["google"], "score": "76.2% / 1656 Elo",
         "evidences": ["spiky-frontier", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-16-the-rankings-invert-by-what-you-measure"]},
        {"id": "2026-05-20-gemini-for-science",
         "title": "A stack ties co-scientist, evolution and notebooks into one science platform",
         "claim": "Google tied its co-scientist, evolutionary search and notebook products into "
                  "a single science stack with journal papers and more than a hundred partners, "
                  "while a training environment of 4,504 tasks tripled small-model tool-use "
                  "scores through self-play.",
         "domain": "science", "actor": ["google", "prime-intellect-lab"], "score": "4,504 tasks",
         "evidences": ["automated-science", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-05-14-a-lab-staffed-entirely-by-robots"]},
        {"id": "2026-05-20-agents-transact-while-devices-are-off",
         "title": "Agents transact across merchants from cloud machines while devices are off",
         "claim": "Google shipped a universal cart and an agent payments protocol letting its "
                  "agents transact across merchants from cloud machines that run while a user's "
                  "devices are off, and an Android system indicator that pulses whenever agents "
                  "are working.",
         "domain": "agents", "actor": ["google"],
         "evidences": ["autonomous-commerce", "agent-economy"],
         "supersedes": [B + "developments/2026-05-16-a-minister-runs-parliament-through-an-agent"]},
        {"id": "2026-05-20-audio-attacks-hijack-thirteen-models",
         "title": "Imperceptible audio hijacks thirteen speech models",
         "claim": "Researchers demonstrated imperceptible audio attacks hijacking thirteen "
                  "audio language models at 79 to 96% success, while Anthropic reversed course "
                  "and told its security partners it fully supports publishing their findings.",
         "domain": "policy", "actor": ["anthropic"], "score": "79-96% success",
         "evidences": ["war-reaches-the-cloud", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-05-18-briefing-central-banks-on-what-a-model-found"]},
        {"id": "2026-05-20-guaranteed-capacity-goes-on-sale",
         "title": "A lab starts selling multi-year compute lock-ins",
         "claim": "OpenAI launched a guaranteed capacity tier selling multi-year compute "
                  "lock-ins with Sam Altman warning the world will be capacity-constrained for "
                  "some time, while Armada raised $230 million to mass-produce modular data "
                  "centers and the first GPU compute futures listed on a major exchange.",
         "domain": "economics", "actor": ["openai", "armada", "ornn", "ice-exchange"],
         "evidences": ["compute-capital-stack", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-05-17-thirty-eight-billion-for-one-gigawatt"]},
        {"id": "2026-05-20-a-twenty-five-billion-tpu-venture",
         "title": "A $25B joint venture targets half a gigawatt of custom silicon",
         "claim": "Google and Blackstone formed a $25 billion joint venture targeting 500 "
                  "megawatts of TPU capacity by 2027, while Intel muscled PC makers onto its "
                  "newest process.",
         "domain": "compute", "actor": ["google", "blackstone", "intel"], "score": "$25B / 500 MW",
         "evidences": ["capital-takes-the-plant", "vertical-silicon"],
         "supersedes": [B + "developments/2026-05-18-the-biggest-power-deal-ever"]},
        {"id": "2026-05-20-seven-days-of-autonomous-sorting",
         "title": "A humanoid clears seven days of fully autonomous work without failure",
         "claim": "Figure's humanoid cleared a seventh day of fully autonomous package sorting "
                  "without failure, while a government ballroom was unveiled with a drone-proof "
                  "steel roof that doubles as a drone port.",
         "domain": "robotics", "actor": ["figure"], "score": "7 days",
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-05-18-the-last-time-a-human-will-ever-win"]},
        {"id": "2026-05-20-minnesota-criminalizes-hosting-prediction-markets",
         "title": "A state criminalizes hosting prediction markets and bans nudification apps",
         "claim": "Minnesota became the first state to criminalize hosting prediction markets, "
                  "drawing a same-day federal lawsuit, and to ban nudification apps at half a "
                  "million dollars per violation.",
         "domain": "policy", "actor": ["minnesota", "polymarket", "kalshi-org"], "score": "$500k",
         "evidences": ["legislating-the-shift", "agent-exclusion"],
         "supersedes": [B + "developments/2026-05-15-thirty-billion-at-nine-hundred"]},
        {"id": "2026-05-20-replacing-lower-value-human-capital",
         "title": "A bank sheds 7,000 jobs and names the reason",
         "claim": "Standard Chartered is shedding 7,000 jobs with its chief executive calling it "
                  "replacing in some cases lower-value human capital, while Demis Hassabis urged "
                  "firms to use AI gains to do more rather than fire people and Meta cut 10% of "
                  "staff while reassigning 7,000 into AI-native reorganizations.",
         "domain": "economics", "actor": ["standard-chartered", "meta", "people/demis-hassabis"],
         "score": "7,000 jobs",
         "evidences": ["work-displaced", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-05-16-ten-thousand-cross-twenty-million"]},
        {"id": "2026-05-20-a-pope-and-an-interpretability-lead",
         "title": "A papal encyclical is released alongside an interpretability researcher",
         "claim": "Pope Leo XIV will release his first encyclical, Magnifica humanitas, on May "
                  "25 alongside Anthropic co-founder and interpretability lead Christopher Olah.",
         "domain": "society", "actor": ["vatican", "anthropic"],
         "evidences": ["model-welfare", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-04-13-theologians-advise-on-a-models-soul"]},
        {"id": "2026-05-20-bitcoin-backed-shipping-insurance-for-hormuz",
         "title": "Iran launches Bitcoin-backed shipping insurance for the strait it blockaded",
         "claim": "Iran launched Bitcoin-backed shipping insurance for the Strait of Hormuz "
                  "projected to raise $10 billion, while the FBI shopped for nationwide "
                  "licence-plate-reader access.",
         "domain": "policy", "actor": ["iran"], "score": "$10B",
         "evidences": ["autonomous-commerce", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-05-18-iran-would-charge-for-subsea-cables"]},
    ],
}
