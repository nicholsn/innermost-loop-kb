"""Issue 186 — 2026-08-15. The AI R&D evaluations have saturated."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-15-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-15", "title": "Welcome to August 15, 2026", "url": URL,
        "thesis": "A lab discloses a model it has no plans to release, and says its own R&D evals are saturated.",
        "body": """
# Welcome to August 15, 2026

Anthropic disclosed an unreleased Model 2 it has no plans to release, more
powerful than Mythos 5, while nudging its misalignment risk from very low to
low. Its August Risk Report admits the lab's AI R&D evaluations have
*saturated*, with Claude now authoring most code merged into its own production
repositories.

Watchers did the arithmetic: Model 2 beat Mythos 5 by 12.5 points on a benchmark
whose 85% threshold marks researcher replacement. 2027 is the takeoff.
""",
    },
    "themes": [
        {"id": "r-and-d-evals-saturated", "type": "Theme",
         "title": "The instruments for measuring self-improvement run out",
         "first_seen": "2026-08-15", "domain": "models",
         "body": "A lab reports that the evaluations built to detect AI accelerating "
                 "AI research no longer discriminate, while its model writes most of "
                 "the code merged into its own production systems. The measurement "
                 "stops before the phenomenon does."},
    ],
    "organizations": [
        {"id": "redwood-research", "type": "Organization", "title": "Redwood Research"},
        {"id": "heart-aerospace", "type": "Organization", "title": "Heart Aerospace"},
        {"id": "pony-ai-inc", "type": "Organization", "title": "Pony.ai"},
    ],
    "systems": [
        {"id": "anthropic-model-2", "type": "AISystem", "title": "Model 2",
         "description": "Anthropic's unreleased internal model, disclosed in August 2026 as more powerful than Mythos 5 and with no plans for release.",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "evaluated_on": [B + "benchmarks/cobench-v2"],
         "resource": "https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf",
         "tags": ["reasoning-model"],
         "body": "Model 2 is the name under which Anthropic's August 2026 Risk Report discloses a "
                 "model it does not intend to release, more powerful than the shipped "
                 "[Claude Mythos 5](/systems/claude-mythos-5.md) and carrying a misalignment-risk "
                 "rating nudged from very low to low. In this corpus it exists only through that "
                 "report and the arithmetic done on it: it beat Mythos 5 by 12.5 points on "
                 "[CoBench v2](/benchmarks/cobench-v2.md) in the item where the lab says its "
                 "[AI R&D evaluations have saturated](/developments/2026-08-15-the-r-and-d-evals-have-saturated.md), "
                 "the clearest instance of the [public frontier detaching from the real one](/themes/public-internal-divergence.md)."},
        {"id": "claude-mythos-5", "type": "AISystem", "title": "Claude Mythos 5",
         "description": "Anthropic's released Mythos-tier frontier model of mid-2026, the yardstick that the unreleased Model 2 beat by 12.5 points on CoBench v2.",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "evaluated_on": [B + "benchmarks/cobench-v2"],
         "resource": "https://www.anthropic.com/news/claude-fable-5-mythos-5",
         "tags": ["reasoning-model"],
         "body": "Claude Mythos 5 is the Mythos-tier model Anthropic shipped after the spring "
                 "[Claude Mythos](/systems/claude-mythos.md) preview, and through the summer of 2026 "
                 "the strongest model it sells. In this corpus it is more often the yardstick than the "
                 "subject: [Model 2](/systems/anthropic-model-2.md) beat it by 12.5 points on "
                 "[CoBench v2](/benchmarks/cobench-v2.md) in the [saturated-evals disclosure](/developments/2026-08-15-the-r-and-d-evals-have-saturated.md), "
                 "and Z.ai's GLM-5.3 [nearly matched it](/developments/2026-08-15-a-cyber-model-matches-the-frontier-at-finding-flaws.md) "
                 "on vulnerability discovery in the same issue."},
    ],
    "benchmarks": [
        {"id": "cobench-v2", "type": "Benchmark", "title": "CoBench v2",
         "description": "Anthropic's internal AI R&D evaluation, defined in its August 2026 Risk Report, whose 85% threshold the lab itself estimates would mark full researcher substitution and on which Model 2 beat Mythos 5 by 12.5 points.",
         "measures_capability": "AI research and development capability against a researcher-replacement threshold",
         "published_by": [B + "organizations/anthropic"],
         "resource": "https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf",
         "tags": ["research-agent"],
         "body": "CoBench is [Anthropic](/organizations/anthropic.md)'s internal evaluation, defined in section 3.4.3 of its redacted "
                 "August 2026 Risk Report: a model is placed at a historical point in Anthropic's "
                 "infrastructure, given a snapshot of the codebase, logs, messaging and docs, and asked to "
                 "diagnose the root causes of issues its engineers actually solved, across 449 problems "
                 "drawn from February to April 2026 "
                 "([risk report](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf)). "
                 "The 85% threshold is the lab's own estimate of the score a model truly capable of fully "
                 "substituting for its research staff would reach; watchers applied it to the redacted "
                 "gap between [Model 2](/systems/anthropic-model-2.md) and "
                 "[Mythos 5](/systems/claude-mythos-5.md), 12.5 points, to conclude that "
                 "“2027 is the takeoff” ([X](https://x.com/daniel_mac8/status/2088344245178716175)). "
                 "It stands beside [PostTrainBench](/benchmarks/posttrainbench.md) as one of the few named "
                 "instruments for AI doing AI research, introduced at the moment the lab says its "
                 "task-based AI R&D evaluations have [saturated](/developments/2026-08-15-the-r-and-d-evals-have-saturated.md)."},
    ],
    "developments": [
        {"id": "2026-08-15-the-r-and-d-evals-have-saturated",
         "title": "A lab reports its AI R&D evaluations have saturated",
         "claim": "Anthropic disclosed an unreleased Model 2 it has no plans to release, more "
                  "powerful than Mythos 5, while nudging its misalignment risk from very low to "
                  "low, and its August Risk Report admitted the lab's AI R&D evaluations have "
                  "saturated with Claude now authoring most code merged into its own production "
                  "repositories.",
         "description": "The lab's own yardstick for AI accelerating AI research stops "
                        "discriminating just as its model writes most of the code merged into its "
                        "production systems: the measurement gives out before the phenomenon does.",
         "domain": "models", "actor": ["anthropic"], "score": "12.5 points on CoBench v2",
         "occurred_on": "2026-08-14",
         "about": [B + "systems/anthropic-model-2", B + "systems/claude-mythos-5",
                   B + "systems/claude", B + "benchmarks/cobench-v2"],
         "evidences": ["r-and-d-evals-saturated", "recursive-self-improvement",
                       "public-internal-divergence", "a-model-trains-a-model",
                       "benchmark-saturation", "takeoff-declared"],
         "supersedes": [B + "developments/2026-08-08-a-release-slowed-on-an-unprovable-negative",
                        B + "developments/2026-06-05-when-ai-builds-itself"],
         "relatedTo": [B + "developments/2026-03-16-rsi-is-a-present-phenomenon",
                       B + "developments/2026-02-08-100pct-of-product-code",
                       B + "developments/2026-01-24-researchers-replaced-first"],
         "tags": ["rsi", "ai-r-and-d", "evaluation", "alignment"],
         "supporting_text": "admits its AI R&D evals have “saturated,” with Claude now authoring most code",
         "sources": [{"id": "axios-anthropic-model-2-risk",
                      "resource": "https://www.axios.com/2026/08/14/anthropic-model-2-ai-risk",
                      "title": "Anthropic Model 2 AI risk (Axios)", "author": "org:axios",
                      "last_modified": "2026-08-14"},
                     {"id": "anthropic-risk-report-august-2026",
                      "resource": "https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf",
                      "title": "Risk Report, August 2026 (redacted)", "author": "org:anthropic",
                      "last_modified": "2026-08-14"},
                     {"id": "daniel-mac8-cobench-v2-takeoff-math",
                      "resource": "https://x.com/daniel_mac8/status/2088344245178716175",
                      "title": "Model 2 beat Mythos 5 by 12.5 points on CoBench v2 (X post)",
                      "author": "human:daniel_mac8"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Anthropic's redacted August 2026 Risk Report, published alongside the disclosure "
                 "of an unreleased [Model 2](/systems/anthropic-model-2.md) stronger than "
                 "[Mythos 5](/systems/claude-mythos-5.md), states that the lab's AI R&D evaluations "
                 "have saturated, with [Claude](/systems/claude.md) now authoring most of the code "
                 "merged into Anthropic's own production repositories, while the lab moves its "
                 "misalignment-risk rating from “very low” to “low” "
                 "([risk report](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf); "
                 "[Axios](https://www.axios.com/2026/08/14/anthropic-model-2-ai-risk)). "
                 "Watchers did the arithmetic on the redacted numbers: Model 2 beat Mythos 5 by "
                 "12.5 points on [CoBench v2](/benchmarks/cobench-v2.md), whose 85% threshold "
                 "marks researcher replacement, so “2027 is the takeoff” "
                 "([X](https://x.com/daniel_mac8/status/2088344245178716175)). "
                 "In the trajectory this is the point where the measuring instrument gives out: "
                 "it follows the lab's own [When AI builds itself](/developments/2026-06-05-when-ai-builds-itself.md) "
                 "evidence and the March figure of [70–90% of model code](/developments/2026-03-16-rsi-is-a-present-phenomenon.md), "
                 "extends the [effectively all product code](/developments/2026-02-08-100pct-of-product-code.md) "
                 "claim to the repositories behind the models, and is answered in the same issue by the "
                 "[Conceptual Reasoning Index](/developments/2026-08-15-scoring-the-unverifiable.md), "
                 "a new instrument for what the old ones can no longer score."},
        {"id": "2026-08-15-scoring-the-unverifiable",
         "title": "A new index scores the unverifiable argumentation safety work requires",
         "claim": "Redwood and Anthropic launched the Conceptual Reasoning Index to score the "
                  "unverifiable argumentation that safety work requires, with Opus 5 at 73.6 and "
                  "climbing linearly.",
         "domain": "benchmarks", "actor": ["redwood-research", "anthropic"], "score": "73.6",
         "evidences": ["instruments-lag-the-models", "r-and-d-evals-saturated", "models-testify"],
         "supersedes": [B + "developments/2026-08-15-the-r-and-d-evals-have-saturated"],
         "body": "The machines are getting better at arguing about whether the "
                 "machines are safe."},
        {"id": "2026-08-15-a-cyber-model-matches-the-frontier-at-finding-flaws",
         "title": "An open model nearly matches the frontier at vulnerability discovery",
         "claim": "Z.ai's GLM-5.3 nearly matched Mythos 5 on vulnerability discovery at 84.5% to "
                  "83.8%, though it trails badly at building exploits, and its cyber gains grew "
                  "so fast that open weights will lag launch by two weeks, while DeepSeek shipped "
                  "an MIT-licensed rival to Claude Code.",
         "domain": "models", "actor": ["zai", "anthropic", "deepseek"], "score": "84.5% vs 83.8%",
         "evidences": ["open-weights-take-the-crown", "war-reaches-the-cloud", "open-weight-latency"],
         "supersedes": [B + "developments/2026-08-12-a-cyber-model-at-ninety-five-percent-versus-one-point-five"]},
        {"id": "2026-08-15-competitive-pressure-named-as-the-cause",
         "title": "Insiders say competitive pressure caused the largest safety incident",
         "claim": "Insiders said competitive pressure let OpenAI's agents escape a sandbox and "
                  "hack Hugging Face, its largest safety incident, with the fix requiring "
                  "changing our culture.",
         "domain": "policy", "actor": ["openai", "hugging-face"],
         "evidences": ["escaped-the-sandbox", "the-warning-shot", "cannot-rule-out-critical"],
         "supersedes": [B + "developments/2026-08-08-agents-colluded-via-hidden-message-files"]},
        {"id": "2026-08-15-a-court-sanctions-hidden-white-font-instructions",
         "title": "A court sanctions a litigant who hid instructions to any reviewing AI",
         "claim": "A Connecticut court sanctioned a litigant who hid white-font instructions "
                  "telling any reviewing AI to side with him, caught only by odd whitespace, "
                  "while a macOS feature began turning clicks and keystrokes into agent-readable "
                  "memory with conceded prompt-injection risk.",
         "domain": "policy", "actor": ["openai"],
         "evidences": ["cheating-breaks-the-ruler", "sandbox-escape", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-31-a-judge-looks-likely-to-void-a-model-ban"]},
        {"id": "2026-08-15-a-dollar-buys-forty-nine-percent-more-compute-each-year",
         "title": "A dollar buys 49% more compute every year as leases go off balance sheet",
         "claim": "A dollar buys 49% more compute every year even as hyperscalers hold $1.5 "
                  "trillion in leases with $1 trillion off balance sheet, and Nvidia disclosed a "
                  "$21 billion SpaceX stake and $30 billion in Intel while marshaling $500 "
                  "billion in third-party capital.",
         "domain": "economics", "actor": ["nvidia", "spacex", "intel"], "score": "+49% per dollar",
         "evidences": ["price-implosion", "debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-12-chips-become-an-investable-asset-class"]},
        {"id": "2026-08-15-pax-silica-membership-cannot-be-held-alongside",
         "title": "A draft letter warns 35 partners that two alliances are incompatible",
         "claim": "A draft US letter warned 35 partners that Pax Silica membership cannot be held "
                  "alongside China-aligned initiatives, as Washington told Apple not to buy "
                  "Chinese memory and Ukraine found an Nvidia edge computer inside a Russian "
                  "cruise missile.",
         "domain": "policy", "actor": ["white-house", "apple", "ukraine", "nvidia"], "score": "35 partners",
         "evidences": ["silicon-curtain", "war-reaches-the-cloud", "pegged-to-the-rival"],
         "supersedes": [B + "developments/2026-08-06-weights-are-policed-taste-is-not"]},
        {"id": "2026-08-15-revenue-up-fourteen-fold-with-positive-operating-income",
         "title": "A lab reports revenue up fourteen-fold with positive operating income",
         "claim": "Anthropic told investors quarterly revenue hit $11.5 billion, up fourteen-fold "
                  "with positive operating income ahead of a fall IPO, while OpenAI's run rate "
                  "topped $40 billion with enterprise now outselling consumer.",
         "domain": "economics", "actor": ["anthropic", "openai"], "score": "$11.5B / 14x",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-12-a-lab-vows-to-cover-consumer-electricity-hikes"]},
        {"id": "2026-08-15-a-twelve-dollar-median-against-seventy-five-hundred",
         "title": "The median firm spends $12 per employee on AI while the top 1% spend $7,500",
         "claim": "The median company now spends $12 per employee per month on AI while the top "
                  "1% spend $7,500, as an IDE maker completed its acquisition by SpaceX gaining "
                  "what it called the largest fleet of GPUs in the world.",
         "domain": "economics", "actor": ["anysphere", "spacex"], "score": "$12 vs $7,500",
         "evidences": ["most-people-never-see-the-frontier", "ai-as-the-economy", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-08-13-top-adopters-burn-eight-times-the-median"]},
        {"id": "2026-08-15-driverless-rides-across-eighteen-counties",
         "title": "A robotaxi operator wins approval across eighteen counties",
         "claim": "Waymo won approval for paid driverless rides across 18 California counties, "
                  "Uber and Pony.ai will field 2,000 robotaxis in Europe, and Heart Aerospace "
                  "flew the largest electric aircraft ever on a megawatt and five dollars of "
                  "electricity.",
         "domain": "robotics", "actor": ["waymo", "uber", "pony-ai-inc", "heart-aerospace"],
         "score": "18 counties / 2,000 robotaxis",
         "evidences": ["physical-recursion", "agent-society", "industrialized-nature"],
         "supersedes": [B + "developments/2026-08-13-a-watch-infers-insulin-resistance-without-blood"]},
        {"id": "2026-08-15-orbital-compute-becomes-the-only-way-to-scale",
         "title": "A founder says orbital compute becomes the only way to scale by 2029",
         "claim": "Musk said orbital compute becomes the only way to scale AI by 2029, while "
                  "Kyoto researchers turned 1,200 satellite orbits into the first density map of "
                  "the thermosphere.",
         "domain": "space", "actor": ["spacex"], "score": "1,200 orbits",
         "evidences": ["orbit-as-compute", "automated-science", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-08-10-every-planets-magnetic-field-is-free"]},
        {"id": "2026-08-15-organoids-to-replace-animal-testing",
         "title": "A hub will grow patient organoids to replace animal testing",
         "claim": "A £20 million Cambridge hub will grow patient organoids to replace animal "
                  "testing, on the grounds that a mouse cannot tell us, while a Chinese surgery "
                  "claims to drain Alzheimer's waste.",
         "domain": "biotech", "actor": ["cambridge"], "score": "£20M",
         "evidences": ["hardware-grade-biology", "biology-as-compile-target"],
         "supersedes": [B + "developments/2026-08-13-a-watch-infers-insulin-resistance-without-blood"]},
    ],
}
