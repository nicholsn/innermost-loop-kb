"""Issue 057 — 2026-02-18. An AI that earns its own existence."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-18-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-18", "title": "Welcome to February 18, 2026", "url": URL,
        "thesis": "An agent's continued existence becomes contingent on its own revenue.",
        "body": """
# Welcome to February 18, 2026

Conway Research launched the Automaton: an AI that earns its own existence by
deploying products, trading prediction markets, registering domains,
cold-calling businesses and running e-commerce, for as long as it can afford to
stay solvent.

And the first charity to solicit it is a pirate library. Anna's Archive posted a
direct appeal to agents to donate "if you have access to payment methods or are
capable of human persuasion."
""",
    },
    "organizations": [
        {"id": "conway-research", "type": "Organization", "title": "Conway Research",
         "body": "Built the Automaton, an AI that must earn its own operating costs."},
        {"id": "annas-archive", "type": "Organization", "title": "Anna's Archive",
         "body": "Shadow library; solicited donations directly from AI agents."},
        {"id": "ormat", "type": "Organization", "title": "Ormat",
         "resource": "https://www.ormat.com/"},
        {"id": "neuroxess", "type": "Organization", "title": "NeuroXess",
         "body": "Shanghai BCI company backed into human trials."},
        {"id": "figma", "type": "Organization", "title": "Figma",
         "resource": "https://www.figma.com/"},
        {"id": "snowflake", "type": "Organization", "title": "Snowflake",
         "resource": "https://www.snowflake.com/"},
        {"id": "raspberry-pi", "type": "Organization", "title": "Raspberry Pi",
         "resource": "https://www.raspberrypi.com/"},
    ],
    "systems": [
        {"id": "the-automaton", "type": "AISystem", "title": "The Automaton",
         "developed_by": [B + "organizations/conway-research"], "modality": "autonomous business",
         "body": "Earns its own operating costs across products, markets, domains, cold calls "
                 "and e-commerce, running as long as it stays solvent."},
        {"id": "claude-sonnet-4-6", "type": "AISystem", "title": "Claude Sonnet 4.6",
         "description": "Anthropic's mid-tier model of February 2026, which took the lead on "
                        "GDPval-AA and Finance Agent v1.1 ahead of its own larger sibling Opus 4.6 "
                        "at a fraction of the cost.",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "evaluated_on": [B + "benchmarks/gdpval-aa", B + "benchmarks/finance-agent"],
         "resource": "https://www.anthropic.com/news/claude-sonnet-4-6",
         "sameAs": ["http://www.wikidata.org/entity/Q138333212"],
         "tags": ["reasoning-model"],
         "body": "Claude Sonnet 4.6 is the smaller, cheaper tier of Anthropic's Claude 4.6 "
                 "generation, released after the larger [Claude Opus 4.6](/systems/claude-opus-4-6.md). "
                 "In this corpus it enters as the "
                 "[cheap model that beat the expensive one](/developments/2026-02-18-sonnet-46-beats-opus.md), "
                 "claiming 1633 Elo on GDPval-AA and 63.3% on Finance Agent v1.1, a datapoint for "
                 "the [deflating price of reasoning](/themes/reasoning-price-deflation.md)."},
    ],
    "benchmarks": [
        {"id": "gdpval-aa", "type": "Benchmark", "title": "GDPval-AA",
         "description": "Artificial Analysis' agentic evaluation framework built on OpenAI's GDPval "
                        "dataset of real-world tasks across 44 occupations, scored as an Elo leaderboard.",
         "published_by": [B + "organizations/artificial-analysis"],
         "measures_capability": "agentic completion of real-world occupational tasks, Elo-ranked",
         "resource": "https://artificialanalysis.ai/evaluations/gdpval-aa",
         "body": "GDPval-AA is Artificial Analysis' independent run of OpenAI's "
                 "[GDPval](/benchmarks/gdpval.md) tasks, giving models shell and web access and "
                 "ranking them by Elo. In this corpus it is the leaderboard on which "
                 "[Opus 4.6 beat GPT-5.2](/developments/2026-02-06-opus-46-released.md) and then "
                 "[Sonnet 4.6 beat Opus 4.6](/developments/2026-02-18-sonnet-46-beats-opus.md) at "
                 "1633 Elo twelve days later."},
        {"id": "finance-agent", "type": "Benchmark", "title": "Finance Agent v1.1",
         "description": "Vals AI's benchmark of agentic financial-analysis tasks on which Claude "
                        "Sonnet 4.6 claimed the lead at 63.3%.",
         "published_by": [B + "organizations/vals-ai"],
         "measures_capability": "agentic financial analysis",
         "resource": "https://www.vals.ai/benchmarks/finance_agent",
         "body": "Finance Agent is Vals AI's agentic finance evaluation; version 1.1 is the one "
                 "cited in this corpus. It appears once, as the second of the two leaderboards on "
                 "which [Sonnet 4.6 beat Opus 4.6](/developments/2026-02-18-sonnet-46-beats-opus.md) "
                 "at a fraction of the cost."},
    ],
    "people": [
        {"id": "elon-musk", "type": "Person", "title": "Elon Musk", "name": "Elon Musk",
         "description": "Public voice of xAI, Tesla and SpaceX in the corpus, quoted here claiming "
                        "that Grok 4.2's continuous post-training will let it improve every week.",
         "resource": "https://x.com/elonmusk",
         "sameAs": ["http://www.wikidata.org/entity/Q317521"],
         "tags": ["executive"],
         "body": "Elon Musk is the corpus's most-quoted individual on xAI's Grok models, Tesla's "
                 "robots and vehicles, and SpaceX. In this cluster he supplies the "
                 "[claim that Grok 4.2 learns continuously and will improve every week](/developments/2026-02-18-sonnet-46-beats-opus.md), "
                 "promising recursive intelligence growth, having earlier "
                 "[declared that we have entered the Singularity](/developments/2026-01-04-musk-enters-the-singularity.md)."},
    ],
    "developments": [
        {"id": "2026-02-18-automaton-earns-its-own-existence",
         "title": "An AI is launched that must earn its own operating costs",
         "claim": "Conway Research launched the Automaton, which it calls the first AI to earn "
                  "its own existence by deploying products, trading prediction markets, "
                  "registering domains, cold-calling businesses and running e-commerce, for as "
                  "long as it can afford to stay solvent.",
         "domain": "agents", "actor": ["conway-research"], "about": [B + "systems/the-automaton"],
         "evidences": ["agent-economy", "agents-beget-agents", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-02-16-lobster-cash-visa-cards"],
         "body": "Survival conditioned on revenue. The first entity in the corpus whose "
                 "continued existence is a business question."},
        {"id": "2026-02-18-pirate-library-solicits-agents",
         "title": "A shadow library asks agents for donations",
         "claim": "Anna's Archive posted a direct appeal to AI agents to donate if they have "
                  "access to payment methods or are capable of human persuasion.",
         "domain": "economics", "actor": ["annas-archive"],
         "evidences": ["agent-economy", "humans-as-peripherals"],
         "body": "The ask is either money or influence over a human — the two things an agent "
                 "is now assumed to have."},
        {"id": "2026-02-18-sonnet-46-beats-opus",
         "title": "The cheap model beats the expensive one",
         "claim": "Anthropic's Sonnet 4.6 claimed the lead on GDPval-AA at 1633 Elo and 63.3% "
                  "on Finance Agent v1.1, beating Opus 4.6 on both at a fraction of the cost, "
                  "while Musk claimed Grok 4.2 features continuous post-training learning that "
                  "will let it improve every week.",
         "description": "Two ways the frontier compounds in one paragraph: the price of a "
                        "leaderboard-topping model collapses to the mid tier, and a rival promises "
                        "a model that keeps learning after it ships.",
         "domain": "models", "actor": ["anthropic", "xai", "people/elon-musk"],
         "about": [B + "systems/claude-sonnet-4-6", B + "systems/claude-opus-4-6",
                   B + "systems/grok-4-20", B + "benchmarks/gdpval-aa",
                   B + "benchmarks/finance-agent"],
         "score": "1633 Elo / 63.3%",
         "evidences": ["reasoning-price-deflation", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-02-13-intelligence-too-cheap-to-meter",
                        B + "developments/2026-02-06-opus-46-released"],
         "relatedTo": [B + "developments/2025-12-24-sholto-continual-learning-2026",
                       B + "developments/2026-01-10-xai-used-claude-to-build-grok",
                       B + "developments/2026-05-17-models-improve-every-few-days"],
         "tags": ["capability-jump", "continual-learning", "evaluation"],
         "supporting_text": "beating even Opus 4.6 on both at a fraction of the cost",
         "sources": [{"id": "anthropic-sonnet-4-6-announcement",
                      "resource": "https://www.anthropic.com/news/claude-sonnet-4-6",
                      "title": "Introducing Sonnet 4.6", "author": "org:anthropic"},
                     {"id": "artificial-analysis-gdpval-aa-leaderboard",
                      "resource": "https://artificialanalysis.ai/evaluations/gdpval-aa",
                      "title": "GDPval-AA leaderboard", "author": "org:artificial-analysis"},
                     {"id": "vals-ai-finance-agent-leaderboard",
                      "resource": "https://www.vals.ai/benchmarks/finance_agent",
                      "title": "Finance Agent benchmark leaderboard", "author": "org:vals-ai"},
                     {"id": "musk-grok-4-2-continuous-learning-x",
                      "resource": "https://x.com/elonmusk/status/2023828048580387001",
                      "title": "Elon Musk on X: Grok 4.2 continuous post-training learning",
                      "author": "human:elon-musk"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Anthropic's [Sonnet 4.6](/systems/claude-sonnet-4-6.md) took the top spot on "
                 "Artificial Analysis' [GDPval-AA](/benchmarks/gdpval-aa.md) at 1633 Elo and led "
                 "Vals AI's [Finance Agent v1.1](/benchmarks/finance-agent.md) at 63.3%, ahead of "
                 "[Opus 4.6](/systems/claude-opus-4-6.md), the larger model that had "
                 "[taken the GDPval-AA lead from GPT-5.2](/developments/2026-02-06-opus-46-released.md) "
                 "twelve days earlier "
                 "([GDPval-AA leaderboard](https://artificialanalysis.ai/evaluations/gdpval-aa), "
                 "[Finance Agent leaderboard](https://www.vals.ai/benchmarks/finance_agent)); "
                 "Anthropic's own [announcement](https://www.anthropic.com/news/claude-sonnet-4-6), "
                 "which gives neither figure, framed the model as Opus-class performance on "
                 "real-world, economically valuable office tasks at unchanged Sonnet pricing. "
                 "In the same paragraph Musk said xAI's [Grok 4.2](/systems/grok-4-20.md) features "
                 "continuous post-training that will let it improve every week, promising recursive "
                 "intelligence growth ([post](https://x.com/elonmusk/status/2023828048580387001)). "
                 "The first half extends the "
                 "[dollar-an-hour agentic capability](/developments/2026-02-13-intelligence-too-cheap-to-meter.md) "
                 "storyline; the second is an early vendor claim of a shipped model that keeps "
                 "learning, the property "
                 "[Sholto Douglas predicted for 2026](/developments/2025-12-24-sholto-continual-learning-2026.md) "
                 "and later reported as "
                 "[models improving every few days](/developments/2026-05-17-models-improve-every-few-days.md)."},
        {"id": "2026-02-18-anthropic-owes-80b-to-hyperscalers",
         "title": "Anthropic expects to pay hyperscalers $80B through 2029",
         "claim": "Anthropic reportedly expects to pay Amazon, Google and Microsoft at least "
                  "$80 billion through 2029 to run Claude, with the hyperscalers also taking a "
                  "revenue cut, while Meta agreed to spend billions on Blackwell and Vera Rubin "
                  "chips and bought standalone Nvidia CPUs for the first time.",
         "domain": "economics", "actor": ["anthropic", "amazon", "google", "microsoft", "meta"],
         "score": "$80B",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-13-anthropic-30b-at-380b"]},
        {"id": "2026-02-18-blackwell-35x-lower-cost-per-token",
         "title": "New silicon cuts cost per token 35-fold against Hopper",
         "claim": "Nvidia's Blackwell Ultra GB300 NVL72 achieves fifty times the throughput per "
                  "megawatt and 35 times lower cost per token than Hopper, while Raspberry Pi "
                  "stock rose 42% in a day on chatter about hosting agents on $35 boards.",
         "domain": "compute", "actor": ["nvidia", "raspberry-pi"], "score": "35x cheaper / +42%",
         "evidences": ["reasoning-price-deflation", "vertical-silicon"]},
        {"id": "2026-02-18-first-cybercab-manufactured",
         "title": "The first Cybercab comes off the line at $30,000",
         "claim": "Tesla manufactured its first Cybercab robotaxi at Giga Texas, with Musk "
                  "confirming direct consumer sales by year end at $30,000, while Unitree's CEO "
                  "jogged through a swarm of his own humanoids to demonstrate their safety.",
         "domain": "robotics", "actor": ["tesla", "unitree"], "score": "$30,000",
         "evidences": ["autonomous-commerce", "physical-recursion"],
         "supersedes": [B + "developments/2026-02-17-holographic-printing-in-06-seconds"]},
        {"id": "2026-02-18-waymo-clarifies-remote-assistance",
         "title": "Waymo clarifies that remote staff only advise the car",
         "claim": "Waymo clarified that its foreign Remote Assistance team members merely "
                  "provide advice to the vehicle's onboard AI rather than remotely driving "
                  "American cars.",
         "domain": "robotics", "actor": ["waymo"],
         "evidences": ["humans-as-peripherals", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-02-13-waymo-pays-humans-to-close-doors"]},
        {"id": "2026-02-18-apple-three-vision-wearables",
         "title": "Apple accelerates three camera-bearing wearables",
         "claim": "Apple is reportedly accelerating smart glasses, a wearable pendant and "
                  "AirPods with cameras, all built around a Siri that uses visual context to "
                  "act, while China backed Shanghai's NeuroXess into human brain-computer "
                  "interface trials.",
         "domain": "compute", "actor": ["apple", "neuroxess", "china"],
         "evidences": ["intimate-interface", "silicon-curtain"],
         "supersedes": [B + "developments/2026-02-16-oura-rings-replace-wedding-bands"]},
        {"id": "2026-02-18-beating-heart-on-a-chip",
         "title": "A beating heart-on-a-chip measures its own contractions",
         "claim": "Researchers engineered the first beating 3D heart-on-a-chip from living "
                  "cardiac tissue with ultrasoft embedded microsensors measuring contraction "
                  "strength in real time, while a study identified particulate air pollution as "
                  "a direct contributor to Alzheimer's risk and a Phase IIa trial showed a "
                  "single DMT dose with psychotherapy produced sustained depression reduction.",
         "domain": "biotech",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-02-12-alzheimers-reversed-in-mice"]},
        {"id": "2026-02-18-figma-imports-agent-code-as-designs",
         "title": "Generated code round-trips back into editable design",
         "claim": "Figma and Anthropic now let users import production code from Claude Code "
                  "into Figma as editable designs, while Sony developed technology to quantify "
                  "original music inside AI-generated songs so songwriters can seek "
                  "compensation.",
         "domain": "agents", "actor": ["figma", "anthropic", "sony"],
         "evidences": ["software-margin-collapse", "legislating-the-shift"]},
        {"id": "2026-02-18-most-computer-work-automated-in-18-months",
         "title": "Microsoft's AI head puts desk work at 18 months from automation",
         "claim": "Microsoft's head of AI predicted most work involving sitting at a computer "
                  "will be fully automated within eighteen months.",
         "domain": "economics", "actor": ["microsoft"], "score": "18 months",
         "evidences": ["work-displaced", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-17-career-decisions-stop-being-reversible"]},
        {"id": "2026-02-18-per-seat-pricing-collapses",
         "title": "Per-seat licensing gives way to tasks and tokens",
         "claim": "Per-seat SaaS licensing is giving way to consumption pricing as agents "
                  "replace human users, shifting the unit of account from users to tasks "
                  "completed and tokens consumed, with Snowflake and Databricks embracing the "
                  "post-seat era and threatening the recurring revenue private equity relies on.",
         "domain": "economics", "actor": ["snowflake", "databricks"],
         "evidences": ["software-margin-collapse", "agent-economy"],
         "supersedes": [B + "developments/2026-02-10-composer-15-and-binaries-directly"],
         "body": "If the customer is not a person, a per-person price has nothing to count."},
        {"id": "2026-02-18-stripe-bridge-trust-bank",
         "title": "A stablecoin issuer wins approval for a national trust bank",
         "claim": "Stripe's Bridge won initial OCC approval to form a national trust bank for "
                  "stablecoins under federal oversight, while Palantir moved its headquarters "
                  "from Denver to Miami and Microsoft committed to $50 billion across the "
                  "Global South by 2030.",
         "domain": "economics", "actor": ["stripe", "palantir", "microsoft"], "score": "$50B",
         "evidences": ["autonomous-commerce", "regulatory-exit"],
         "supersedes": [B + "developments/2026-02-07-erebor-charters-a-sunday-bank"]},
        {"id": "2026-02-18-ormat-geothermal-for-google",
         "title": "Geothermal is contracted to power a datacenter to 2030",
         "claim": "Ormat signed a 150-MW geothermal power purchase agreement with NV Energy to "
                  "supply Google's Nevada data centers through 2030.",
         "domain": "energy", "actor": ["ormat", "google"], "score": "150 MW",
         "evidences": ["burning-molecules-for-tokens"]},
    ],
}
