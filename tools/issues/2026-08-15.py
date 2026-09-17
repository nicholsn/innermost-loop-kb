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
    "developments": [
        {"id": "2026-08-15-the-r-and-d-evals-have-saturated",
         "title": "A lab reports its AI R&D evaluations have saturated",
         "claim": "Anthropic disclosed an unreleased Model 2 it has no plans to release, more "
                  "powerful than Mythos 5, while nudging its misalignment risk from very low to "
                  "low, and its August Risk Report admitted the lab's AI R&D evaluations have "
                  "saturated with Claude now authoring most code merged into its own production "
                  "repositories.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["r-and-d-evals-saturated", "recursive-self-improvement",
                       "public-internal-divergence", "a-model-trains-a-model"],
         "supersedes": [B + "developments/2026-08-08-a-release-slowed-on-an-unprovable-negative"],
         "body": "Watchers noted Model 2 beat Mythos 5 by 12.5 points on a benchmark "
                 "whose 85% threshold marks researcher replacement, concluding that "
                 "2027 is the takeoff."},
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
