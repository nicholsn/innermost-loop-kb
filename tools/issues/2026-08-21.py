"""Issue 190 — 2026-08-21. Tokens become the central currency."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-21-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-21", "title": "Welcome to August 21, 2026", "url": URL,
        "thesis": "A payments giant buys the mint of the intelligence economy.",
        "body": """
# Welcome to August 21, 2026

Stripe's $7 billion purchase of OpenRouter — a 90-person gateway routing across
400+ models from 80+ providers — is its largest acquisition ever and a wager
that no single model wins. Patrick Collison calls tokens the central currency
for companies building with AI.

And prompting escapes the keyboard: a model learns a new physical task from a
three-to-twelve-second demonstration, scoring 59% with zero gradient updates.
""",
    },
    "themes": [
        {"id": "physical-prompting", "type": "Theme",
         "title": "A demonstration becomes the prompt",
         "first_seen": "2026-08-21", "domain": "robotics",
         "body": "A few seconds of video dropped into a context window teaches a new "
                 "manipulation task with no gradient updates. In-context learning "
                 "crosses into the physical world, and improvised tool use emerges "
                 "from pretraining rather than instruction."},
    ],
    "organizations": [
        {"id": "generalist-ai", "type": "Organization", "title": "Generalist"},
        {"id": "supcon", "type": "Organization", "title": "SUPCON"},
        {"id": "nevada", "type": "Organization", "title": "Nevada"},
        {"id": "groq-inc", "type": "Organization", "title": "Groq"},
        {"id": "independence-mo", "type": "Organization", "title": "Independence, Missouri"},
    ],
    "developments": [
        {"id": "2026-08-21-a-payments-giant-buys-the-mint",
         "title": "A payments giant makes its largest acquisition ever to buy a model gateway",
         "claim": "Stripe's more than $7 billion purchase of OpenRouter, the 90-person gateway "
                  "routing requests across more than 400 models from over 80 providers, is the "
                  "payments giant's largest acquisition ever and a wager that no single model "
                  "wins, with Patrick Collison calling tokens the central currency for companies "
                  "building with AI.",
         "domain": "economics", "actor": ["stripe", "openrouter"], "score": "$7B+",
         "evidences": ["routing-around-the-ban", "monoculture-is-the-vulnerability", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-08-17-a-run-rate-past-sixty-five-billion"]},
        {"id": "2026-08-21-an-s-1-that-could-beat-the-record",
         "title": "A lab's IPO could match or beat the record share sale",
         "claim": "Anthropic reportedly expects its mega-IPO, which could file publicly by month's "
                  "end, to match or beat SpaceX's record $75 billion share sale, backed by a $65 "
                  "billion revenue run rate and quarterly revenue above $11.5 billion, up from "
                  "$787 million a year earlier.",
         "domain": "economics", "actor": ["anthropic", "spacex"], "score": "$787M to $11.5B in a year",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-19-founders-take-supervoting-shares-before-the-float"]},
        {"id": "2026-08-21-silicon-financed-like-sovereign-debt",
         "title": "A chipmaker seeks up to $100 billion for custom AI silicon",
         "claim": "Broadcom is in talks to raise more than $60 billion, potentially $100 billion "
                  "with the junior tranche, for custom AI chips benefiting Anthropic and others, "
                  "financing silicon like sovereign debt.",
         "domain": "economics", "actor": ["broadcom", "anthropic"], "score": "$60-100B",
         "evidences": ["debt-funded-buildout", "vertical-silicon", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-08-21-an-s-1-that-could-beat-the-record"]},
        {"id": "2026-08-21-trillions-of-tokens-a-week-to-write-its-own-software",
         "title": "A social network burns trillions of tokens a week writing its own software",
         "claim": "Meta has quietly become one of Microsoft's largest AI customers, burning "
                  "trillions of tokens a week through Azure largely to write its own software, "
                  "while Slack Code gave five different agent products dedicated channels to "
                  "write, review and ship code in the open.",
         "domain": "agents", "actor": ["meta", "microsoft", "anthropic", "openai", "cognition"],
         "evidences": ["the-persistent-colleague", "agents-on-the-org-chart", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-08-13-if-this-was-opt-in-nobody-would-opt-in"]},
        {"id": "2026-08-21-a-billion-downloads-and-a-hundred-thousand-variants",
         "title": "An open family crosses a billion downloads and 100,000 community variants",
         "claim": "Google's Gemma crossed one billion downloads and 100,000 community variants, "
                  "running everywhere from orbiting satellites to a health app with 100 million "
                  "downloads in India.",
         "domain": "models", "actor": ["google"], "score": "1B downloads / 100,000 variants",
         "evidences": ["open-weights-take-the-crown", "most-people-never-see-the-frontier"],
         "supersedes": [B + "developments/2026-08-16-three-billion-downloads-and-a-hundred-fifty-thousand-derivatives"]},
        {"id": "2026-08-21-a-physical-prompt-teaches-a-new-task",
         "title": "A three-second demonstration teaches a new physical task with no training",
         "claim": "Generalist's GEN-1.5 learns a new physical task from a physical prompt, a "
                  "three-to-twelve-second demonstration dropped into its context window, scoring "
                  "59% with zero gradient updates and 83% after five minutes of data, with "
                  "improvised tool use emerging unprompted from pretraining.",
         "domain": "robotics", "actor": ["generalist-ai"], "score": "59% zero-shot / 83% after 5 min",
         "evidences": ["physical-prompting", "world-models-beat-vlas", "physical-recursion"],
         "supersedes": [B + "developments/2026-08-12-the-first-human-to-robot-transfer-scaling-law"]},
        {"id": "2026-08-21-seven-thousand-robotaxis-approved-for-one-city",
         "title": "A state approves up to 7,000 robotaxis for one city",
         "claim": "Nevada approved up to 7,000 robotaxis for Las Vegas from Tesla, Waymo and "
                  "Uber's partners, and Waymo arrives with its own custom chip, a 1,000-TOPS part "
                  "on a 5-nanometer process that sharpens reflexes while loosening its Nvidia "
                  "dependence.",
         "domain": "robotics", "actor": ["nevada", "waymo", "tesla", "uber", "tsmc"],
         "score": "7,000 robotaxis / 1,000 TOPS",
         "evidences": ["physical-recursion", "vertical-silicon", "agent-society"],
         "supersedes": [B + "developments/2026-08-15-driverless-rides-across-eighteen-counties"]},
        {"id": "2026-08-21-humanoid-robocops-issue-a-hundred-seventy-thousand-warnings",
         "title": "Humanoid traffic officers issue 170,000 warnings in one city",
         "claim": "SUPCON's humanoid robocops have issued 170,000 polite traffic warnings in "
                  "Hangzhou, while humanoid makers sell robots to state training centers that "
                  "sell teleoperation data back, a circular economy behind Unitree's $50 billion "
                  "debut.",
         "domain": "robotics", "actor": ["supcon", "unitree"], "score": "170,000 warnings / $50B",
         "evidences": ["physical-recursion", "agent-society", "data-beyond-text"],
         "supersedes": [B + "developments/2026-08-21-seven-thousand-robotaxis-approved-for-one-city"]},
        {"id": "2026-08-21-a-licensed-inference-chip-for-a-restricted-market",
         "title": "A chipmaker reportedly plans a licensed inference part for a restricted market",
         "claim": "Nvidia reportedly plans a Groq-licensed inference processor variant for China "
                  "by year-end to fight Huawei amid an inference chip famine, though it denies any "
                  "such roadmap.",
         "domain": "compute", "actor": ["nvidia", "groq-inc", "huawei"],
         "evidences": ["silicon-curtain", "infrastructure-crowding-out", "pegged-to-the-rival"],
         "supersedes": [B + "developments/2026-08-17-an-antifragile-hundred-billion-dollar-bet"]},
        {"id": "2026-08-21-a-dozen-towns-recall-officials-over-datacenters",
         "title": "Residents of a dozen towns move to recall officials over datacenter deals",
         "claim": "Residents of a dozen towns are recalling officials over data center deals, with "
                  "the scrutiny going fully bipartisan, complete with a party committee memo "
                  "calling it a sleeper issue.",
         "domain": "policy", "actor": ["independence-mo"],
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure", "over-automation-is-rational"],
         "supersedes": [B + "developments/2026-08-17-ai-becomes-a-major-election-issue"]},
        {"id": "2026-08-21-a-third-of-submissions-fully-synthetic",
         "title": "A third of music submissions are fully synthetic while AI draws under 0.5% of listening",
         "claim": "Apple Music will label songs Made With AI, fitting since a third of submissions "
                  "are now fully synthetic while AI music draws under 0.5% of listening, as Japan "
                  "approved a comply-or-explain code urging AI firms to disclose models and "
                  "training data.",
         "domain": "society", "actor": ["apple", "japan-govt"], "score": "33% of submissions / <0.5% listening",
         "evidences": ["agent-exclusion", "legislating-the-shift", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-08-17-a-watermark-called-a-perversion-of-writing"]},
        {"id": "2026-08-21-more-screen-time-predicted-better-cognition",
         "title": "An eight-year study finds more childhood screen time predicted better cognition",
         "claim": "An eight-year Finnish study found more childhood screen time predicted better "
                  "teenage cognition, while the Treasury limited children's savings accounts to "
                  "broad, low-fee equity funds.",
         "domain": "society", "actor": ["us-treasury-dept"],
         "evidences": ["deskilling", "most-people-never-see-the-frontier"],
         "supersedes": [B + "developments/2026-08-13-top-adopters-burn-eight-times-the-median"],
         "body": "A counterweight to the year's dominant story about screens and "
                 "cognition, kept for that reason."},
    ],
}
