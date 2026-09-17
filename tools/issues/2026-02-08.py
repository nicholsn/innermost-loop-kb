"""Issue 049 — 2026-02-08. Effectively 100%."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-8-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-08", "title": "Welcome to February 8, 2026", "url": URL,
        "thesis": "The bootstrap completes: the tools now write themselves entirely.",
        "body": """
# Welcome to February 8, 2026

Anthropic's chief product officer says effectively 100% of Anthropic product
code is written by Claude. OpenAI's release cycle has gone from 97 days to 29.
AlphaEvolve is discovering activation functions that beat ReLU threefold.

And the number that makes it concrete: Andon Labs projects a Vending-Bench agent
will earn $16,333 a year within a year, making silicon cheaper to employ than a
minimum-wage human.
""",
    },
    "themes": [
        {"id": "debt-funded-buildout", "type": "Theme",
         "title": "The buildout borrows against the future",
         "first_seen": "2026-02-08", "domain": "economics",
         "body": "Capex outruns cash flow, so it moves onto the balance sheet and then off it: "
                 "century bonds, record debt raises, free cash flow fully consumed, special "
                 "vehicles. The compute is being paid for with claims on a future the compute "
                 "is supposed to produce."},
    ],
    "organizations": [
        {"id": "andon-labs", "type": "Organization", "title": "Andon Labs",
         "body": "Publisher of Vending-Bench; projects agent earnings."},
        {"id": "massachusetts", "type": "Organization", "title": "Commonwealth of Massachusetts"},
        {"id": "svb", "type": "Organization", "title": "Silicon Valley Bank",
         "resource": "https://www.svb.com/"},
        {"id": "kalshi-org", "type": "Organization", "title": "Kalshi",
         "resource": "https://kalshi.com/"},
    ],
    "benchmarks": [
        {"id": "critpt", "type": "Benchmark", "title": "CritPt",
         "measures_capability": "research-level physics problem solving"},
    ],
    "people": [
        {"id": "mike-krieger", "type": "Person", "title": "Mike Krieger", "name": "Mike Krieger",
         "description": "Instagram co-founder and Anthropic's chief product officer, who put the "
                        "share of Anthropic product code written by Claude at effectively 100%.",
         "resource": "https://x.com/mikeyk",
         "sameAs": ["http://www.wikidata.org/entity/Q10329947"],
         "tags": ["executive", "founder"],
         "body": "Mike Krieger co-founded Instagram and is Anthropic's chief product officer. "
                 "In this corpus he appears once, as the executive who confirmed that "
                 "[effectively all of Anthropic's product code is written by Claude]"
                 "(/developments/2026-02-08-100pct-of-product-code.md), the item the "
                 "newsletter treats as completing the bootstrap phase after "
                 "[Boris Cherny's 200 pull requests]"
                 "(/developments/2025-12-27-cherny-200-pull-requests.md) and "
                 "[Dario Amodei's \u201cmuch of the code\u201d]"
                 "(/developments/2026-01-27-amodei-country-of-geniuses-2027.md)."},
    ],
    "roles": [
        {"id": "mike-krieger-anthropic-cpo", "type": "Role",
         "title": "Mike Krieger, Chief Product Officer at Anthropic",
         "roleName": "Chief Product Officer",
         "memberOf": [B + "organizations/anthropic"],
         "holder": [B + "people/mike-krieger"],
         "description": "The role in which he confirmed that effectively 100% of Anthropic "
                        "product code is written by Claude.",
         "body": "The newsletter and the linked Cisco interview identify Mike Krieger as "
                 "Anthropic's chief product officer in the issue that records the "
                 "[effectively-100% figure](/developments/2026-02-08-100pct-of-product-code.md) "
                 "for Claude-written product code."},
    ],
    "developments": [
        {"id": "2026-02-08-100pct-of-product-code",
         "title": "Effectively all of Anthropic's product code is written by Claude",
         "claim": "Anthropic's chief product officer confirmed that effectively 100% of "
                  "Anthropic product code is now written by Claude, while OpenAI cut its model "
                  "release cycle from 97 days to 29.",
         "description": "The newsletter's \u201cbootstrap complete\u201d moment: the tool that writes "
                        "the tools has taken over the entire product codebase of a frontier lab, "
                        "while a rival's release cadence compresses threefold.",
         "domain": "agents", "actor": ["anthropic", "people/mike-krieger", "openai"],
         "about": [B + "systems/claude"], "score": "100% / 97→29 days",
         "evidences": ["recursive-self-improvement", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-02-07-openai-bans-editors-and-terminals",
                        B + "developments/2026-01-27-amodei-country-of-geniuses-2027"],
         "relatedTo": [B + "developments/2025-12-27-cherny-200-pull-requests",
                       B + "developments/2026-02-03-codex-builds-itself",
                       B + "developments/2026-02-06-claude-code-4pct-of-commits"],
         "tags": ["rsi", "ai-r-and-d"],
         "supporting_text": "\u201ceffectively 100%\u201d of Anthropic product code is now written by Claude",
         "sources": [{"id": "krieger-cisco-enterprise-ai-interview",
                      "resource": "https://www.youtube.com/watch?v=CHscuD6Q4xs&t=582s",
                      "title": "Enterprise & AI | Mike Krieger, Chief Product Officer, Anthropic",
                      "author": "org:cisco"},
                     {"id": "openai-release-cadence-x-post",
                      "resource": "https://x.com/chatgpt21/status/2019983107781242936",
                      "title": "OpenAI's model release cycle down from 97 days to 29 (post on X)"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Speaking in Cisco's Enterprise & AI interview series, Anthropic chief product "
                 "officer Mike Krieger put the share of Anthropic product code written by "
                 "[Claude](/systems/claude.md) at \u201ceffectively 100%\u201d "
                 "([interview](https://www.youtube.com/watch?v=CHscuD6Q4xs&t=582s)); the same "
                 "issue records OpenAI's release cadence shortening from 97 days to 29 "
                 "([post](https://x.com/chatgpt21/status/2019983107781242936)). It closes the "
                 "arc that ran from [Boris Cherny's 200 pull requests]"
                 "(/developments/2025-12-27-cherny-200-pull-requests.md) in December through "
                 "[Dario Amodei's \u201cmuch of the code\u201d]"
                 "(/developments/2026-01-27-amodei-country-of-geniuses-2027.md) in January, and "
                 "sits beside OpenAI's [Codex building itself]"
                 "(/developments/2026-02-03-codex-builds-itself.md). In the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) "
                 "trajectory it is the point where the product layer of a frontier lab is fully "
                 "model-written; the model-training layer follows in March, when "
                 "[70-90% of model code](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) "
                 "is reported as Claude-written."},
        {"id": "2026-02-08-alphaevolve-finds-new-activations",
         "title": "AlphaEvolve discovers an activation function that triples ReLU",
         "claim": "DeepMind used AlphaEvolve to discover new nonlinear activation functions "
                  "including one called Turbulent that outperforms ReLU threefold, while xAI's "
                  "Grok-Imagine-Image expanded the image generation Pareto frontier.",
         "description": "The author's \u201cAI is better at designing AI than humans\u201d point applied "
                        "to a component as basic as the nonlinearity, with an LLM-driven "
                        "evolutionary search replacing a design choice made by hand since ReLU.",
         "domain": "models", "actor": ["google-deepmind", "xai"],
         "about": [B + "systems/alphaevolve"], "score": "3x ReLU",
         "occurred_on": "2026-02-05",
         "evidences": ["recursive-self-improvement", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-02-06-gpt53-codex-creates-itself",
                        B + "developments/2025-12-13-tao-erdos-1026"],
         "relatedTo": [B + "developments/2026-03-13-alphaevolve-improves-ramsey-bounds",
                       B + "developments/2026-08-29-a-co-scientist-invents-an-architecture-beating-six-models"],
         "tags": ["rsi", "ai-r-and-d", "autonomous-research"],
         "supporting_text": "discover new nonlinear activation functions like \u201cTurbulent,\u201d",
         "sources": [{"id": "alphaevolve-activation-functions-arxiv",
                      "resource": "https://arxiv.org/abs/2602.05688",
                      "title": "Mining Generalizable Activation Functions",
                      "author": "org:google-deepmind", "last_modified": "2026-02-05"},
                     {"id": "grok-imagine-image-arena-x-post",
                      "resource": "https://x.com/arena/status/2020215933898526791",
                      "title": "Grok-Imagine-Image on the image generation Pareto frontier (Arena post on X)"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "In *Mining Generalizable Activation Functions* "
                 "(arXiv [2602.05688](https://arxiv.org/abs/2602.05688), submitted 5 February), "
                 "DeepMind researchers ran [AlphaEvolve](/systems/alphaevolve.md), with a "
                 "frontier LLM as the mutation operator, over the space of Python functions "
                 "within a FLOP budget, using out-of-distribution performance as the fitness "
                 "signal; the newsletter singles out \u201cTurbulent\u201d, which it reports as "
                 "outperforming ReLU threefold. The same issue notes xAI's Grok-Imagine-Image "
                 "pushing the image-generation Pareto frontier on the [Arena](/benchmarks/lmarena.md) "
                 "leaderboards ([post](https://x.com/arena/status/2020215933898526791)). "
                 "AlphaEvolve entered the corpus [assisting Terence Tao on Erd\u0151s #1026]"
                 "(/developments/2025-12-13-tao-erdos-1026.md) and returns in March with "
                 "[new Ramsey bounds](/developments/2026-03-13-alphaevolve-improves-ramsey-bounds.md); "
                 "here it is turned on a component of the networks it runs on, which in the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) "
                 "trajectory is the step from AI doing mathematics to AI redesigning AI, "
                 "extended in August when a [co-scientist invents an architecture]"
                 "(/developments/2026-08-29-a-co-scientist-invents-an-architecture-beating-six-models.md) "
                 "that beats six frontier models."},
        {"id": "2026-02-08-horizons-become-unmeasurable",
         "title": "Noam Brown predicts autonomy horizons will become unmeasurable",
         "claim": "OpenAI's Noam Brown predicted that by year end autonomy horizons will be so "
                  "unbounded that measuring them becomes the main challenge.",
         "domain": "benchmarks", "actor": ["openai"],
         "evidences": ["benchmark-saturation", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-07-encrypted-solutions-challenge"]},
        {"id": "2026-02-08-kawaii-shells-for-agents",
         "title": "Agents get decorative housing and cron jobs to show up for work",
         "claim": "Companies began selling decorative enclosures for the Mac Minis that host "
                  "OpenClaw agents, one user noting his agents work around the clock without "
                  "eating or complaining, while six agents ran a company autonomously via cron "
                  "jobs that get them to show up for work each day.",
         "domain": "agents",
         "evidences": ["agent-society", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-02-07-mac-mini-racks-as-employees"]},
        {"id": "2026-02-08-agent-outearns-minimum-wage",
         "title": "An agent is projected to out-earn a minimum-wage human",
         "claim": "Andon Labs projects that within a year a state-of-the-art agent on "
                  "Vending-Bench 2 will generate $16,333 annually, making it more profitable to "
                  "employ silicon than a minimum-wage human.",
         "domain": "economics", "actor": ["andon-labs"], "about": [B + "benchmarks/vending-bench-2"],
         "score": "$16,333/yr",
         "evidences": ["work-displaced", "agent-economy", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-01-08-inference-hits-minimum-wage"],
         "body": "January put an hour of inference at minimum wage. This puts a year of agent "
                 "above it."},
        {"id": "2026-02-08-middleware-obsoleted",
         "title": "Middleware frameworks are obsoleted by models handling complexity directly",
         "claim": "Engineers note middleware frameworks are being obsoleted by coding models "
                  "that handle complexity directly, while Anthropic introduced a fast mode for "
                  "Claude Code accelerating it a further 2.5 times.",
         "domain": "agents", "actor": ["anthropic"], "score": "2.5x",
         "evidences": ["software-margin-collapse", "engineer-as-supervisor"]},
        {"id": "2026-02-08-opus-tops-critpt-physics",
         "title": "A model takes first on a research physics benchmark",
         "claim": "Claude Opus 4.6 took first place on the CritPt physics benchmark, with xAI "
                  "co-founder Igor Babuschkin saying a Claude Code moment for research is not "
                  "far off.",
         "domain": "benchmarks", "actor": ["anthropic"], "about": [B + "benchmarks/critpt"],
         "evidences": ["automated-science", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-02-06-axiomprover-settles-fels-conjecture"]},
        {"id": "2026-02-08-replace-dram-with-light",
         "title": "Carmack and Musk brainstorm replacing DRAM with fiber loops",
         "claim": "Nvidia is exploring servers with co-packaged optics to bypass electrical "
                  "bottlenecks while John Carmack and Elon Musk discussed replacing DRAM "
                  "entirely with fiber optic loops or the vacuum of space.",
         "domain": "compute", "actor": ["nvidia"],
         "evidences": ["vertical-silicon", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-02-07-memory-prices-up-90pct"]},
        {"id": "2026-02-08-grid-siphons-car-batteries",
         "title": "A state gives away chargers that siphon car batteries for the grid",
         "claim": "Massachusetts launched a program giving away free bidirectional EV chargers "
                  "that draw on car batteries for grid stability.",
         "domain": "energy", "actor": ["massachusetts"],
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"]},
        {"id": "2026-02-08-spacex-hires-for-orbital-datacenters",
         "title": "SpaceX begins hiring for orbital datacenters",
         "claim": "SpaceX started hiring for orbital AI data centers, while Blue Origin pivoted "
                  "to an interim Blue Moon Mk-1.5 lander to race for the lunar surface.",
         "domain": "space", "actor": ["spacex", "blue-origin"],
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-02-07-moratorium-pushes-compute-to-orbit"]},
        {"id": "2026-02-08-polygenic-screening-cuts-deaths-23pct",
         "title": "Polygenic screening could cut premature deaths by 23%",
         "claim": "Researchers found polygenic risk screening could reduce premature deaths by "
                  "23.3%, while South Korean researchers created a spray that stops bleeding "
                  "instantly.",
         "domain": "biotech", "score": "-23.3%",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-07-rabbit-brain-vitrification"]},
        {"id": "2026-02-08-worst-job-cuts-since-the-recession",
         "title": "January is the worst month for US job cuts since the Great Recession",
         "claim": "January was the worst month for US job cuts since the Great Recession, while "
                  "Silicon Valley Bank reported the top five AI startups have outvalued every "
                  "dot-com era IPO combined.",
         "domain": "economics", "actor": ["svb"],
         "evidences": ["work-displaced", "growth-without-hiring", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-25-graduate-postings-collapse"]},
        {"id": "2026-02-08-currency-gets-in-the-way",
         "title": "Musk says currency will get in the way once the loop closes",
         "claim": "Elon Musk said a $100 trillion Tesla valuation is not impossible but that "
                  "once the solar-to-robot-to-chip loop closes, conventional currency will just "
                  "get in the way, while Kalshi and Polymarket handled $800 million of Super "
                  "Bowl volume.",
         "domain": "economics", "actor": ["tesla", "kalshi-org", "polymarket"], "score": "$800M",
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-25-china-population-falls-again"]},
    ],
}
