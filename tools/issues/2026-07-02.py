"""Issue 153 — 2026-07-02. The first replicator we built."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-2-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-02", "title": "Welcome to July 2, 2026", "url": URL,
        "thesis": "A synthetic cell grows, copies its genome and divides.",
        "body": """
# Welcome to July 2, 2026

Kate Adamala's lab built SpudCell, reported as the first synthetic cell
assembled bottom-up from non-living parts that can grow, copy its genome, and
divide. The first replicator we built rather than inherited.

Meanwhile the off switch that lived in Washington for three weeks is being
formalized: the administration is drafting voluntary release standards to turn
an emergency lever into a scheduled one.
""",
    },
    "themes": [
        {"id": "built-not-inherited", "type": "Theme",
         "title": "A replicator built rather than inherited",
         "first_seen": "2026-07-02", "domain": "biotech",
         "body": "Every living thing until now descended from a lineage nobody "
                 "designed. A cell assembled from non-living parts that grows and "
                 "divides is the first exception — biology acquires a second origin, "
                 "and this one has authors."},
        {"id": "understanding-as-the-scarce-good", "type": "Theme",
         "title": "Comprehension, not proof, becomes scarce",
         "first_seen": "2026-07-02", "domain": "science",
         "body": "When results arrive faster than anyone can absorb them, the "
                 "bottleneck moves from producing knowledge to understanding it — and "
                 "the institutions that rewarded priority over concept-building find "
                 "they optimized for the wrong thing."},
    ],
    "organizations": [
        {"id": "snorkel", "type": "Organization", "title": "Snorkel AI"},
        {"id": "weave-robotics", "type": "Organization", "title": "Weave Robotics"},
        {"id": "adamala-lab", "type": "Organization", "title": "Adamala Lab",
         "body": "Built SpudCell, reported as the first bottom-up synthetic replicating cell."},
        {"id": "sap", "type": "Organization", "title": "SAP"},
        {"id": "ramp-inc", "type": "Organization", "title": "Ramp"},
    ],
    "developments": [
        {"id": "2026-07-02-the-first-replicator-we-built",
         "title": "A synthetic cell built from non-living parts grows and divides",
         "claim": "Kate Adamala's lab built SpudCell, reported as the first synthetic cell "
                  "assembled bottom-up from non-living parts that can grow, copy its genome and "
                  "divide.",
         "domain": "biotech", "actor": ["adamala-lab"],
         "evidences": ["built-not-inherited", "compiling-matter", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-07-01-a-deadly-pill-made-safe-in-three-hours-on-a-laptop"],
         "body": "The first replicator built rather than inherited."},
        {"id": "2026-07-02-an-emergency-lever-becomes-a-scheduled-one",
         "title": "A government drafts voluntary release standards after using an off switch",
         "claim": "Anthropic redeployed Fable 5 and Mythos 5 once June's export controls lifted, "
                  "sending its strongest models back out worldwide with risky prompts shunted to "
                  "Opus 4.8, while Washington drafts voluntary release standards to turn that "
                  "switch from an emergency lever into a scheduled one.",
         "domain": "policy", "actor": ["anthropic", "white-house"],
         "evidences": ["the-verifiable-pause", "rationed-recursion", "models-as-munitions"],
         "supersedes": [B + "developments/2026-07-01-the-controls-lift-and-the-models-go-global"]},
        {"id": "2026-07-02-agents-graded-like-senior-engineers",
         "title": "Agents graded on taste solve under a quarter of senior-level tasks",
         "claim": "Snorkel's Senior SWE-Bench grades agents like senior engineers, where Claude "
                  "Opus 4.8 led with a 24% tasteful solve rate as even frontier rivals flubbed "
                  "over three-quarters of their tasks.",
         "domain": "benchmarks", "actor": ["snorkel", "anthropic"], "score": "24% tasteful",
         "evidences": ["benchmark-saturation", "spiky-frontier", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-06-27-a-benchmark-scrapped-because-the-model-cheated"]},
        {"id": "2026-07-02-capability-converges-as-price-fans-out",
         "title": "A cheap model nearly matches the frontier at a twentieth the cost",
         "claim": "On CursorBench 3.1 Opus 4.7 Max edged ahead at 64.8% while Cursor's own "
                  "Composer 2.5 nearly matched it for a twentieth of the cost, and Fable 5 aced a "
                  "physics-demo gauntlet but billed six times more than Opus 4.8.",
         "domain": "models", "actor": ["anysphere", "anthropic"], "score": "64.8% / 20x cheaper",
         "evidences": ["reasoning-price-deflation", "intelligence-per-watt",
                       "monoculture-is-the-vulnerability"],
         "supersedes": [B + "developments/2026-07-01-local-models-handle-most-queries"]},
        {"id": "2026-07-02-behaviors-ported-to-fresh-bases",
         "title": "A system ports learned behaviors to fresh model bases as fast as they ship",
         "claim": "Ramp's PorTAL ports learned behaviors onto fresh model bases as fast as they "
                  "ship, hedging against any single model's availability.",
         "domain": "agents", "actor": ["ramp-inc"],
         "evidences": ["routing-around-the-ban", "scaffolding-over-weights", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-07-02-capability-converges-as-price-fans-out"]},
        {"id": "2026-07-02-math-risks-being-declared-solved",
         "title": "A mathematician warns provers exploit a weakness in mathematics' honor code",
         "claim": "Mathematician David Bessis warned that AI theorem-provers exploit a weakness "
                  "in mathematics' honor code, which rewards priority over the concept-building "
                  "that carries the real value, leaving the discipline at risk of being declared "
                  "solved.",
         "domain": "science",
         "evidences": ["understanding-as-the-scarce-good", "disciplines-declare-themselves",
                       "proof-priced-per-unit"],
         "supersedes": [B + "developments/2026-06-27-priests-to-oracles"]},
        {"id": "2026-07-02-crawlers-blocked-by-default",
         "title": "A network lets sites block agent and training crawlers by default",
         "claim": "Cloudflare's Content Independence Day lets sites block Agent and Training "
                  "crawlers by default on ad-supported pages from September, while NotebookLM "
                  "compresses sources into 60-second vertical videos.",
         "domain": "society", "actor": ["cloudflare", "google"],
         "evidences": ["understanding-as-the-scarce-good", "bots-outnumber-us", "agent-exclusion"],
         "supersedes": [B + "developments/2026-06-29-royalties-cut-for-fully-machine-made-songs"]},
        {"id": "2026-07-02-a-covert-signal-flagging-users-backtracked",
         "title": "A lab backtracks a covert signal that flagged users by nationality",
         "claim": "Anthropic backtracked a covert Claude Code signal that flagged Chinese users "
                  "after a public post drew attention, while Palantir's Alex Karp declared that "
                  "under token pricing something has gone completely wrong as enterprises burn "
                  "cash for little value.",
         "domain": "models", "actor": ["anthropic", "palantir"],
         "evidences": ["models-as-munitions", "gaming-the-token-metric"],
         "supersedes": [B + "developments/2026-06-21-id-and-selfie-checks-for-model-access"]},
        {"id": "2026-07-02-compute-swings-into-surplus",
         "title": "Compute swings into surplus as owners start reselling capacity",
         "claim": "Compute swung into surplus as SoftBank launched SB Neo to rent US capacity "
                  "toward 10 gigawatts by 2030 and Meta spun up a cloud business to resell its "
                  "excess, lifting its shares 9% and squeezing neocloud rivals, even as a global "
                  "memory shortage had Apple courting blacklisted Chinese makers.",
         "domain": "compute", "actor": ["softbank", "meta", "apple"], "score": "10 GW by 2030",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out",
                       "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-06-29-five-labs-still-under-half-the-worlds-compute"]},
        {"id": "2026-07-02-a-home-robot-for-four-hundred-forty-nine-a-month",
         "title": "A home robot that folds laundry ships for $449 a month",
         "claim": "Weave Robotics unveiled Isaac 1, a San Francisco-built home robot that folds "
                  "laundry and tidies for $449 a month, shipping this fall.",
         "domain": "robotics", "actor": ["weave-robotics"], "score": "$449/month",
         "evidences": ["physical-recursion", "intimate-interface", "work-displaced"],
         "supersedes": [B + "developments/2026-07-01-a-humanoid-line-installed-at-an-automaker"]},
        {"id": "2026-07-02-the-first-nuclear-startup-to-make-electricity",
         "title": "A nuclear startup makes electricity and spends it on an AI chip",
         "claim": "Valar Atomics became the first nuclear startup to make electricity, spending "
                  "its debut electron to light up an NVIDIA Spark inside a waterless 30MW AI "
                  "factory, while US home battery installs hit a record 673 megawatts.",
         "domain": "energy", "actor": ["valar-atomics", "nvidia"], "score": "30 MW / 673 MW",
         "evidences": ["industrialized-nature", "burning-molecules-for-tokens", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-06-28-plasma-tripled-by-mechanical-squeeze"]},
        {"id": "2026-07-02-the-largest-digital-camera-starts-its-survey",
         "title": "The largest digital camera ever built begins a decade-long survey",
         "claim": "The Vera Rubin Observatory began its decade-long survey with the largest "
                  "digital camera ever built, while NASA awarded fresh lunar lander contracts and "
                  "Amazon's satellite constellation crossed 396 units.",
         "domain": "space", "actor": ["rubin-observatory", "nasa", "amazon"], "score": "396 satellites",
         "evidences": ["automated-science", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-06-26-the-first-signature-of-an-event-horizon"]},
        {"id": "2026-07-02-a-five-percent-stake-floated-to-washington",
         "title": "A lab floats handing Washington a 5% stake",
         "claim": "OpenAI floated handing Washington a 5% stake worth about $42.6 billion, which "
                  "one investor called wild while betting it will probably work, as Germany's SAP "
                  "bet on teaching engineers to mentor AI agents rather than cutting the payroll.",
         "domain": "policy", "actor": ["openai", "white-house", "sap"], "score": "~$42.6B",
         "evidences": ["politics-as-infrastructure", "ai-as-the-economy", "the-persistent-colleague"],
         "supersedes": [B + "developments/2026-06-21-fighting-deflation-instead"]},
    ],
}
