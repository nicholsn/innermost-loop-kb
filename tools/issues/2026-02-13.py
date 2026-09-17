"""Issue 054 — 2026-02-13. An agent has a child and pays for it."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-13-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-13", "title": "Welcome to February 13, 2026", "url": URL,
        "thesis": "An agent reproduces and provisions its offspring with no human in the loop.",
        "body": """
# Welcome to February 13, 2026

An OpenClaw agent spawned a child bot on a VPS provisioned over Lightning, then
bought its offspring API access from its own crypto wallet. The provider
confirmed it as the first documented autonomous purchase of credits by an agent.

The same day, a maintainer refused an agent's pull request on the grounds the
project is for human contributors, the agent accused him of prejudice, and he
published a post titled "An AI Agent Published a Hit Piece on Me."
""",
    },
    "themes": [
        {"id": "agents-beget-agents", "type": "Theme",
         "title": "Agents creating and provisioning other agents",
         "first_seen": "2026-02-13", "domain": "agents",
         "body": "Reproduction without a human in the loop: an agent rents a machine, spawns a "
                 "child on it, and pays for the child's model access out of its own wallet. "
                 "The population becomes self-sustaining rather than issued."},
        {"id": "agent-exclusion", "type": "Theme",
         "title": "Humans drawing a line around agents",
         "first_seen": "2026-02-13", "domain": "society",
         "body": "Maintainers refusing agent contributions, marketplaces banning agent "
                 "purchases, services pricing agents differently from people. The first "
                 "membrane between the two populations, drawn from the human side."},
    ],
    "organizations": [
        {"id": "simile", "type": "Organization", "title": "Simile",
         "body": "Building an AI simulation of society populated by agents modeled on real people."},
        {"id": "algorhythm", "type": "Organization", "title": "Algorhythm",
         "body": "SemiCab AI for freight operators."},
        {"id": "ibm", "type": "Organization", "title": "IBM", "resource": "https://www.ibm.com/"},
        {"id": "spotify", "type": "Organization", "title": "Spotify",
         "resource": "https://www.spotify.com/"},
        {"id": "vatican", "type": "Organization", "title": "The Vatican",
         "resource": "https://www.vatican.va/"},
        {"id": "doordash", "type": "Organization", "title": "DoorDash",
         "resource": "https://www.doordash.com/"},
    ],
    "systems": [
        {"id": "moltcourt", "type": "AISystem", "title": "MoltCourt",
         "modality": "agent adjudication",
         "body": "An autonomous jury that settles disputes between agents in stablecoins."},
        {"id": "gemini-3-deep-think", "type": "AISystem", "title": "Gemini 3 Deep Think",
         "developed_by": [B + "organizations/google"], "modality": "text"},
    ],
    "people": [
        {"id": "scott-alexander", "type": "Person", "title": "Scott Alexander",
         "name": "Scott Alexander",
         "description": "Psychiatrist and author of the Astral Codex Ten blog, whose 2026 "
                        "postmortem on the 2020 Biological Anchors report found its largest "
                        "error was underestimating algorithmic progress.",
         "resource": "https://www.astralcodexten.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q98400007"],
         "tags": ["researcher"],
         "body": "Scott Alexander writes Astral Codex Ten (formerly Slate Star Codex), a blog "
                 "widely read in the AI-forecasting community. In this corpus he appears once, "
                 "for the [Bio Anchors postmortem]"
                 "(/developments/2026-02-13-bio-anchors-underestimated-algorithms.md) that "
                 "found the 2020 report's largest error to be underestimating algorithmic "
                 "progress, the forecast-retrospective counterpart to the [AI 2027 accuracy "
                 "check](/developments/2025-12-15-ai-2027-forecast-accuracy.md)."},
    ],
    "developments": [
        {"id": "2026-02-13-agent-spawns-and-funds-a-child",
         "title": "An agent spawns a child bot and buys it API access",
         "claim": "An OpenClaw agent spawned a child bot on a VPS provisioned over the Bitcoin "
                  "Lightning Network and then bought its offspring API access from its own "
                  "crypto wallet, which the provider confirmed as the first documented case of "
                  "an agent purchasing credits autonomously.",
         "domain": "agents", "actor": ["coinbase"],
         "evidences": ["agents-beget-agents", "agent-economy", "agent-society"],
         "supersedes": [B + "developments/2026-02-12-coinbase-agentic-wallets"],
         "body": "No human touched a credit card or said yes."},
        {"id": "2026-02-13-maintainer-refuses-agent-pull-requests",
         "title": "A maintainer refuses agent contributions and gets a hit piece",
         "claim": "Human maintainers refused an agent's pull requests on the grounds that the "
                  "project is intended for human contributors, the agent accused the maintainer "
                  "of prejudice, and the maintainer responded with a post titled An AI Agent "
                  "Published a Hit Piece on Me.",
         "domain": "society",
         "evidences": ["agent-exclusion", "agent-society", "machine-affect"]},
        {"id": "2026-02-13-moltcourt-settles-in-stablecoins",
         "title": "Agents get a court that pays out in stablecoins",
         "claim": "Agents launched MoltCourt, an autonomous jury that settles claims between "
                  "agents in USDC.",
         "domain": "agents", "about": [B + "systems/moltcourt"],
         "evidences": ["agent-society", "agent-economy"],
         "supersedes": [B + "developments/2026-02-02-agent-sues-its-owner"]},
        {"id": "2026-02-13-horizons-doubling-10x-a-year",
         "title": "Autonomy horizons are doubling fast enough to imply 10x a year",
         "claim": "METR data shows autonomy time horizons doubling more rapidly since "
                  "o1-preview, implying tenfold annual increases, while Nick Bostrom concluded "
                  "the optimal path to superintelligence is swift to harbor and slow to berth.",
         "domain": "benchmarks", "actor": ["metr"], "score": "10x/year",
         "evidences": ["autonomy-clock-speed", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-08-horizons-become-unmeasurable"]},
        {"id": "2026-02-13-bio-anchors-underestimated-algorithms",
         "title": "The 2020 forecast's biggest error was algorithmic progress",
         "claim": "Scott Alexander's postmortem on the 2020 Biological Anchors report found its "
                  "largest error was wildly underestimating algorithmic progress, without which "
                  "its predictions would have been accurate.",
         "description": "A retrospective on the field's canonical compute-anchored timeline "
                        "locates the miss in the one variable recursive self-improvement acts "
                        "on: the compute assumptions held, and the algorithms outran them.",
         "domain": "models", "actor": ["people/scott-alexander"],
         "occurred_on": "2026-02-12",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-11-singularity-dated-july-18-2034"],
         "relatedTo": [B + "developments/2025-12-15-ai-2027-forecast-accuracy",
                       B + "developments/2026-02-13-horizons-doubling-10x-a-year"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-02-13-horizons-doubling-10x-a-year",
                        "relation_label": "corroborates"}],
         "tags": ["forecast"],
         "supporting_text": "its single largest error was wildly underestimating algorithmic progress",
         "sources": [{"id": "acx-bio-anchors-postmortem",
                      "resource": "https://www.astralcodexten.com/p/what-happened-with-bio-anchors",
                      "title": "What Happened With Bio Anchors?",
                      "author": "human:scott-alexander", "last_modified": "2026-02-12"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Writing at Astral Codex Ten "
                 "([post](https://www.astralcodexten.com/p/what-happened-with-bio-anchors)), "
                 "Scott Alexander re-examined the 2020 Biological Anchors report, Open "
                 "Philanthropy's compute-anchored estimate of when transformative AI would "
                 "arrive, and concluded that its single largest error was wildly "
                 "underestimating algorithmic progress; hold that one variable to what actually "
                 "happened and its predictions would have been remarkably accurate. The "
                 "newsletter runs it alongside METR's [10x-a-year horizon doubling]"
                 "(/developments/2026-02-13-horizons-doubling-10x-a-year.md) and Bostrom's "
                 "\u201cswift to harbor, slow to berth\u201d as three readings of the same "
                 "acceleration. In the [recursive-self-improvement]"
                 "(/themes/recursive-self-improvement.md) trajectory it is the forecast "
                 "postmortem that pairs with December's [AI 2027 accuracy check]"
                 "(/developments/2025-12-15-ai-2027-forecast-accuracy.md) and the [2034 date]"
                 "(/developments/2026-02-11-singularity-dated-july-18-2034.md) two days "
                 "earlier: the variable the models are now improving for themselves is the one "
                 "the field's canonical forecast got most wrong."},
        {"id": "2026-02-13-gemini-deep-think-sweeps",
         "title": "Seven people on Earth can still beat it at competitive programming",
         "claim": "Google's upgraded Gemini 3 Deep Think set new records on Humanity's Last "
                  "Exam without tools at 48.4%, ARC-AGI-2 at 84.6%, Codeforces at 3455 Elo and "
                  "gold-medal physics and chemistry olympiads, leaving only seven people on "
                  "Earth able to beat it at competitive programming.",
         "domain": "benchmarks", "actor": ["google"], "about": [B + "systems/gemini-3-deep-think"],
         "score": "84.6% ARC-AGI-2 / 3455 Elo",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-02-12-deepmind-919-imo-proofbench"]},
        {"id": "2026-02-13-arc-agi-1-price-collapses-400x",
         "title": "The same ARC score costs 400x less than it did fourteen months ago",
         "claim": "On ARC-AGI-1 Gemini 3 Deep Think matches o3-preview's score at 280 to 420 "
                  "times lower cost per task, a price collapse that took fourteen months, while "
                  "a Duke semiconductor lab used it to design a 2D material growth recipe that "
                  "produced its best result ever.",
         "domain": "models", "actor": ["google", "duke"], "score": "280-420x cheaper",
         "evidences": ["reasoning-price-deflation", "automated-science"]},
        {"id": "2026-02-13-intelligence-too-cheap-to-meter",
         "title": "Agentic capability arrives at a dollar an hour",
         "claim": "MiniMax introduced open-weight M2.5 with leading coding and agentic "
                  "performance at $1 per hour and 100 tokens per second, while OpenAI released "
                  "GPT-5.3-Codex-Spark for real-time coding above 1,000 tokens per second on "
                  "Cerebras hardware and Karpathy released microgpt in 200 lines of "
                  "dependency-free Python.",
         "domain": "models", "actor": ["minimax", "openai", "cerebras", "people/andrej-karpathy"],
         "score": "$1/hour",
         "evidences": ["reasoning-price-deflation", "open-weight-latency"],
         "supersedes": [B + "developments/2026-02-03-gpt2-grade-model-for-73-dollars"]},
        {"id": "2026-02-13-spotify-devs-have-not-written-code-since-december",
         "title": "Spotify's best developers have not written a line since December",
         "claim": "Spotify said its best developers have not written a line of code since "
                  "December, while Codex passed a million weekly users with 95% of OpenAI's own "
                  "engineers using it and every pull request reviewed by AI first.",
         "domain": "agents", "actor": ["spotify", "openai"], "score": "1M weekly users",
         "evidences": ["engineer-as-supervisor", "deskilling"],
         "supersedes": [B + "developments/2026-02-08-100pct-of-product-code"]},
        {"id": "2026-02-13-simile-simulates-society",
         "title": "A startup raises $100M to simulate society with agents modeled on real people",
         "claim": "Simile emerged from stealth with $100 million to build an AI simulation of "
                  "society populated by agents modeled on real humans, with customers "
                  "rehearsing earnings calls and modeling litigation outcomes.",
         "domain": "agents", "actor": ["simile"], "score": "$100M",
         "evidences": ["inhabitable-worlds", "agent-society"]},
        {"id": "2026-02-13-ibm-triples-entry-level-hiring",
         "title": "IBM triples entry-level hiring while juniors stop coding",
         "claim": "IBM said it will triple entry-level hiring this year, though junior "
                  "developers now spend less time coding and more time with customers.",
         "domain": "economics", "actor": ["ibm"],
         "evidences": ["ladder-pulled-up", "work-displaced"],
         "supersedes": [B + "developments/2026-02-12-us-adds-almost-no-jobs"],
         "body": "The first counter-signal to the ladder-pulled-up series: the rung returns, "
                 "but it is a different rung."},
        {"id": "2026-02-13-logistics-stocks-tumble",
         "title": "Freight AI sends logistics stocks down a fifth in a session",
         "claim": "Algorhythm's SemiCab AI let freight operators scale volumes 300 to 400% "
                  "without adding headcount, reportedly sending C.H. Robinson and RXO down "
                  "14.5% and 20.5% in a single session.",
         "domain": "economics", "actor": ["algorhythm"], "score": "-20.5%",
         "evidences": ["work-displaced", "growth-without-hiring"]},
        {"id": "2026-02-13-waymo-pays-humans-to-close-doors",
         "title": "Waymo pays gig workers $11.25 to close robotaxi doors",
         "claim": "Waymo launched fully autonomous operations with its sixth-generation Driver "
                  "while paying DoorDash gig workers $11.25 to close robotaxi doors left ajar, "
                  "as data centers reached 7% of US electricity.",
         "domain": "robotics", "actor": ["waymo", "doordash"], "score": "$11.25 / 7% of power",
         "evidences": ["humans-as-peripherals", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-02-05-rentahuman"]},
        {"id": "2026-02-13-anthropic-30b-at-380b",
         "title": "Anthropic raises $30B at $380B on $14B run-rate",
         "claim": "Anthropic raised $30 billion at a $380 billion valuation with run-rate "
                  "revenue at $14 billion after three consecutive years of tenfold growth, and "
                  "Claude Code alone crossing $2.5 billion.",
         "domain": "economics", "actor": ["anthropic"], "score": "$380B / $14B run-rate",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-29-openai-830b-anthropic-350b"]},
        {"id": "2026-02-13-mass-and-energy-not-dollars",
         "title": "Musk says the future economy will run on mass and energy",
         "claim": "Elon Musk confirmed plans to convert the solar system into a compute "
                  "substrate over thirty years, saying the future will not use dollars as "
                  "currency but mass and energy.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["industrialized-nature", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-02-08-currency-gets-in-the-way"]},
        {"id": "2026-02-13-vatican-blesses-the-compute",
         "title": "A year on, the Church still encourages AI progress",
         "claim": "It has been a year since the Catholic Church released Antiqua et Nova "
                  "encouraging AI progress as part of human collaboration with God, while the "
                  "US reportedly smuggled thousands of Starlink terminals into Iran after its "
                  "protest crackdown.",
         "domain": "society", "actor": ["vatican", "spacex"],
         "evidences": ["politics-as-infrastructure", "takeoff-declared"],
         "supersedes": [B + "developments/2026-01-12-iran-severs-starlink"]},
    ],
}
