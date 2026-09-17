"""Issue 130 — 2026-06-03. Benchmark it, don't license it."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-3-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-03", "title": "Welcome to June 3, 2026", "url": URL,
        "thesis": "Washington chooses testing over licensing.",
        "body": """
# Welcome to June 3, 2026

An executive order directs agencies to build a classified test of AI cyber
capabilities and invites developers to *voluntarily* share covered frontier
models for up to 30 days before release — while forbidding any mandatory
licensing regime. The ninety-day FDA-style notification floated in May arrives
as a thirty-day voluntary one.

Sixteen mathematicians answer with the Leiden Declaration, asking their field
to disclose AI use and keep humans accountable for correctness.
""",
    },
    "themes": [
        {"id": "disciplines-declare-themselves", "type": "Theme",
         "title": "Disciplines issue declarations",
         "first_seen": "2026-06-03", "domain": "science",
         "body": "Fields that cannot outrun the models start writing constitutions "
                 "instead: disclosure rules, accountability clauses, statements of "
                 "what a human must still sign for. The declaration is what a "
                 "profession produces when the argument is already lost on capability."},
    ],
    "organizations": [
        {"id": "imu", "type": "Organization", "title": "International Mathematical Union",
         "body": "Backed the Leiden Declaration on AI and Mathematics."},
        {"id": "ny-fed", "type": "Organization", "title": "Federal Reserve Bank of New York"},
        {"id": "thrive-holdings", "type": "Organization", "title": "Thrive Holdings",
         "body": "Buying accounting firms to automate white-collar work."},
    ],
    "developments": [
        {"id": "2026-06-03-testing-instead-of-licensing",
         "title": "An executive order chooses testing over licensing",
         "claim": "The White House issued an executive order directing agencies to build a "
                  "classified test of AI cyber capabilities and inviting developers to "
                  "voluntarily share covered frontier models for up to 30 days before release, "
                  "while forbidding any mandatory licensing regime.",
         "domain": "policy", "actor": ["white-house"], "score": "30 days, voluntary",
         "evidences": ["legislating-the-shift", "safety-pledges-recede"],
         "supersedes": [B + "developments/2026-05-28-a-third-party-safety-audit-mandate"],
         "body": "The ninety-day FDA-style pre-release notification briefed to labs in "
                 "May arrives as a thirty-day voluntary one."},
        {"id": "2026-06-03-the-leiden-declaration",
         "title": "Sixteen mathematicians publish a declaration on AI and mathematics",
         "claim": "Sixteen mathematicians backed by the International Mathematical Union "
                  "published the Leiden Declaration on AI and Mathematics, asking the field to "
                  "disclose AI use and keep humans accountable for correctness, weeks after a "
                  "model disproved an 80-year-old Erdős conjecture.",
         "domain": "science", "actor": ["imu"],
         "evidences": ["disciplines-declare-themselves", "automated-science",
                       "humans-mine-the-machine"],
         "supersedes": [B + "developments/2026-05-29-humans-lift-methods-from-a-machine-proof"]},
        {"id": "2026-06-03-code-bought-from-app-developers",
         "title": "A platform buys code from its own app developers to train on",
         "claim": "Google is quietly buying code from Play Store developers to train its coding "
                  "tools, while Microsoft launched a seven-model MAI family including a "
                  "reasoning model it claims beats Sonnet 4.6 and a 5-billion-parameter coder "
                  "cheaper than Haiku.",
         "domain": "models", "actor": ["google", "microsoft"],
         "evidences": ["data-beyond-text", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-25-an-ide-startup-becomes-a-frontier-lab"]},
        {"id": "2026-06-03-law-professors-prefer-the-machine",
         "title": "Law professors prefer AI answers three times in four",
         "claim": "A Stanford blind study found law professors preferred AI answers to student "
                  "legal questions in roughly 75% of 3,000 comparisons, flagging them as "
                  "harmful a third as often as human ones.",
         "domain": "society", "actor": ["stanford"], "score": "75% of 3,000",
         "evidences": ["humans-need-not-apply", "work-displaced"],
         "supersedes": [B + "developments/2026-05-29-a-law-firm-builds-rather-than-rents"]},
        {"id": "2026-06-03-the-fastest-app-ever-to-a-billion",
         "title": "A chatbot becomes the fastest app ever to a billion monthly users",
         "claim": "ChatGPT became the fastest app ever to a billion monthly users, even as "
                  "Claude's smaller base compounds far faster at 640% a year, and Codex passed "
                  "5 million weekly users.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "1B MAU / +640%/yr",
         "evidences": ["ai-as-the-economy", "intimate-interface"],
         "supersedes": [B + "developments/2026-05-16-chatgpt-and-codex-merge"]},
        {"id": "2026-06-03-a-sandbox-at-the-operating-system-layer",
         "title": "An operating system ships a sandbox for agents",
         "claim": "Microsoft launched Scout, an always-on assistant across Outlook and Teams, "
                  "Project Solara for agent-first devices, and Execution Containers, a "
                  "Windows-level sandbox already adopted by OpenAI, Nvidia, Manus and Nous "
                  "Research.",
         "domain": "agents", "actor": ["microsoft", "openai", "nvidia", "manus", "nous-research"],
         "evidences": ["agent-economy", "sandbox-escape"],
         "supersedes": [B + "developments/2026-06-02-the-oral-tradition-may-not-survive"]},
        {"id": "2026-06-03-a-model-defends-a-hundred-fifty-organizations",
         "title": "A defensive model is extended to 150 critical-infrastructure organizations",
         "claim": "Anthropic expanded Project Glasswing, opening Claude Mythos Preview to "
                  "roughly 150 organizations across power, water, healthcare and other newly "
                  "defended sectors.",
         "domain": "policy", "actor": ["anthropic"], "score": "~150 organizations",
         "evidences": ["war-reaches-the-cloud", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-06-02-a-european-agency-gets-the-weapon"]},
        {"id": "2026-06-03-the-tpu-debt-deal-prices",
         "title": "The record TPU credit deal prices at 5.75%",
         "claim": "Broadcom's backstop of a record $36 billion private-credit deal, structured "
                  "to buy Google TPUs and lease them to Anthropic, compressed senior-tranche "
                  "yields to about 5.75%, with the unbacked slice paying 8 to 9%, part of over "
                  "$27 billion borrowed this year to pour concrete around GPUs.",
         "domain": "economics", "actor": ["broadcom", "google", "anthropic", "coreweave"],
         "score": "5.75% senior / 8-9% unbacked",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-29-thirty-six-billion-of-debt-to-lease-tpus"]},
        {"id": "2026-06-03-a-quantum-chip-designed-by-an-agent",
         "title": "A topological quantum chip is designed with the company's own agent",
         "claim": "Microsoft unveiled Majorana 2, a topological quantum chip designed with its "
                  "own agentic AI, improving qubit reliability a thousandfold and pulling its "
                  "scalable-quantum target forward to 2029.",
         "domain": "compute", "actor": ["microsoft"], "score": "1000x reliability, 2029",
         "evidences": ["silicon-designs-itself", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-05-26-a-pure-play-quantum-foundry"]},
        {"id": "2026-06-03-orbital-manufacturing-cleared-for-test",
         "title": "Reentry capsules that manufacture in orbit are cleared for testing",
         "claim": "SpaceX won FAA approval to test its Starfall capsules, reentry vehicles that "
                  "will manufacture in orbit before splashing into the Pacific, with "
                  "commentators noting a vehicle precise enough to land cargo is precise enough "
                  "to deliver kinetic weapons anywhere on Earth.",
         "domain": "space", "actor": ["spacex", "faa"],
         "evidences": ["orbit-as-compute", "violence-arrives"],
         "supersedes": [B + "developments/2026-05-29-a-rocket-explodes-on-the-test-stand"]},
        {"id": "2026-06-03-remote-work-not-ai-explains-graduate-unemployment",
         "title": "Remote work, not AI, explains most graduate unemployment",
         "claim": "New York Fed researchers found that remote work, not AI, explains nearly "
                  "two-thirds of rising unemployment among young graduates, since employers "
                  "stopped hiring juniors they could not mentor in person.",
         "domain": "economics", "actor": ["ny-fed"], "score": "~2/3 of the rise",
         "evidences": ["ladder-pulled-up", "oral-tradition-dissolves"],
         "supersedes": [B + "developments/2026-05-11-women-hold-most-of-the-exposed-jobs"],
         "body": "A counterweight to the year's dominant story: the junior rung is "
                 "disappearing for reasons that predate the models."},
        {"id": "2026-06-03-a-company-caps-coding-tool-spend",
         "title": "A company caps engineers at $1,500 a month per coding tool",
         "claim": "Uber capped engineers at $1,500 a month per coding tool after burning a "
                  "year's budget in four months, while Thrive Holdings bet $1 billion buying "
                  "accounting firms to automate white-collar work.",
         "domain": "economics", "actor": ["uber", "thrive-holdings"], "score": "$1,500/mo cap",
         "evidences": ["gaming-the-token-metric", "work-displaced"],
         "supersedes": [B + "developments/2026-05-29-a-leaderboard-killed-for-being-gamed"]},
    ],
}
