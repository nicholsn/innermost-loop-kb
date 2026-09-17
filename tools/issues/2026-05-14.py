"""Issue 115 — 2026-05-14. Capability doubling compresses to 4.5 months."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-14-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-14", "title": "Welcome to May 14, 2026", "url": URL,
        "thesis": "The ceiling stops being capability and becomes a token budget.",
        "body": """
# Welcome to May 14, 2026

The UK's AI Security Institute finds capability doubling time compressed to 4.5
months, with the leading models showing no clear ceiling — only a token budget.

And a lab called Recursive Superintelligence emerged from stealth with $650
million, betting that AI conducting experiments on how to safely improve itself
is the fastest path to superintelligence.
""",
    },
    "organizations": [
        {"id": "nous-research", "type": "Organization", "title": "Nous Research",
         "body": "Published a pretraining speedup by averaging contiguous token embeddings."},
        {"id": "recursive-superintelligence", "type": "Organization",
         "title": "Recursive Superintelligence",
         "body": "Emerged from stealth with $650M to have AI run experiments on improving itself."},
        {"id": "varda-space", "type": "Organization", "title": "Varda",
         "resource": "https://www.varda.com/"},
        {"id": "cms", "type": "Organization", "title": "CMS",
         "resource": "https://www.cms.gov/"},
        {"id": "tokyo-science", "type": "Organization", "title": "Institute of Science Tokyo",
         "body": "Opened a fully automated medicine lab staffed by humanoids."},
    ],
    "developments": [
        {"id": "2026-05-14-doubling-time-compresses-to-45-months",
         "title": "Capability doubling time compresses to four and a half months",
         "claim": "The UK's AI Security Institute found capability doubling time has compressed "
                  "to 4.5 months, with the leading models showing no clear ceiling, only a token "
                  "budget.",
         "domain": "benchmarks", "actor": ["aisi"], "score": "4.5-month doubling",
         "evidences": ["autonomy-clock-speed", "takeoff-declared"],
         "supersedes": [B + "developments/2026-05-09-a-sixteen-hour-horizon-at-the-edge-of-the-ruler"]},
        {"id": "2026-05-14-the-first-model-to-clear-both-cyber-ranges",
         "title": "A model becomes the first to clear both national cyber ranges",
         "claim": "Mythos Preview became the first model to clear both of the UK institute's "
                  "cyber ranges, solving one in six of ten attempts and the previously unbroken "
                  "second in three of ten, against three of ten for GPT-5.5 on the easier range.",
         "domain": "benchmarks", "actor": ["anthropic", "aisi"], "score": "6/10 and 3/10",
         "evidences": ["war-reaches-the-cloud", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-05-01-an-early-checkpoint-matches-the-unreleased-frontier"]},
        {"id": "2026-05-14-recursive-superintelligence-raises-650m",
         "title": "A lab raises $650M to have AI experiment on improving itself",
         "claim": "Recursive Superintelligence emerged from stealth with $650 million at a $4.65 "
                  "billion valuation, staffed by former research leads from five major labs, "
                  "betting that AI conducting experiments on how to safely improve itself is the "
                  "fastest path to superintelligence.",
         "domain": "agents", "actor": ["recursive-superintelligence"], "score": "$650M at $4.65B",
         "evidences": ["recursive-self-improvement", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-13-agents-write-their-own-goals"]},
        {"id": "2026-05-14-token-superposition-training",
         "title": "Averaging token embeddings gives a threefold pretraining speedup",
         "claim": "Nous Research's token superposition training delivers a two- to threefold "
                  "wall-clock pretraining speedup at matched compute by averaging contiguous "
                  "bags of token embeddings, with no architecture change required.",
         "domain": "models", "actor": ["nous-research"], "score": "2-3x",
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-12-interaction-models-collapse-the-loop"]},
        {"id": "2026-05-14-claude-for-small-business",
         "title": "A toggle install plugs a model into payroll, invoices and sales",
         "claim": "Anthropic launched Claude for Small Business, a toggle install connecting it "
                  "to accounting, payments, marketing and document software to run payroll, "
                  "close the books, chase invoices and execute sales campaigns, and announced a "
                  "monthly programmatic-usage credit signalling a shift toward as-you-go "
                  "enterprise pricing.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["one-person-company", "work-displaced"],
         "supersedes": [B + "developments/2026-05-13-claude-for-the-legal-industry"]},
        {"id": "2026-05-14-gpu-hours-as-philanthropy",
         "title": "A foundation buys $108M of compute and donates it",
         "claim": "The Jensen and Lori Huang foundation bought $108.3 million of CoreWeave "
                  "compute and donated it to universities and nonprofits, turning GPU hours into "
                  "philanthropy, while Sam Altman is reportedly considering a new compute "
                  "company majority-owned by OpenAI but not anchored to it.",
         "domain": "economics", "actor": ["nvidia", "coreweave", "openai"], "score": "$108.3M",
         "evidences": ["compute-as-compensation", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-12-a-development-company-with-forward-deployed-engineers"]},
        {"id": "2026-05-14-an-app-store-for-robot-motions",
         "title": "A robot task-motion app store opens",
         "claim": "Unitree opened the first robot task-motion app store, letting owners "
                  "one-tap install choreography and martial arts routines onto their machines, "
                  "while Figure livestreamed humanoids running a full eight-hour shift to a peak "
                  "of 300,000 concurrent viewers.",
         "domain": "robotics", "actor": ["unitree", "figure"], "score": "300,000 viewers",
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-05-13-a-humanoid-that-climbs-vertical-steel"]},
        {"id": "2026-05-14-a-lab-staffed-entirely-by-robots",
         "title": "Tokyo opens a fully automated medicine lab staffed by humanoids",
         "claim": "Tokyo's Institute of Science opened the first fully automated medicine "
                  "laboratory staffed entirely by humanoids and robots, targeting two thousand "
                  "research machines by 2040 to automate experiments, cell culture and "
                  "discovery.",
         "domain": "science", "actor": ["tokyo-science"], "score": "2,000 by 2040",
         "evidences": ["automated-science", "physical-recursion"],
         "supersedes": [B + "developments/2026-05-13-the-cocktail-party-problem-solved"]},
        {"id": "2026-05-14-drugs-crystallized-in-microgravity",
         "title": "A space firm sends drugs to orbit to grow novel crystals",
         "claim": "Varda announced a collaboration with United Therapeutics to send "
                  "small-molecule drugs to low orbit to grow novel crystals in microgravity for "
                  "rare pulmonary disease, with its president predicting 195 of the next 200 "
                  "products manufactured in space will be pharmaceuticals.",
         "domain": "space", "actor": ["varda-space"], "score": "195 of 200",
         "evidences": ["orbit-as-compute", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-13-a-power-grid-in-orbit"]},
        {"id": "2026-05-14-a-root-canal-from-59000-years-ago",
         "title": "A Neanderthal molar shows an invasive dental procedure 59,000 years ago",
         "claim": "A Neanderthal molar from a Siberian cave shows evidence of an invasive dental "
                  "procedure, essentially a root canal, performed 59,000 years ago, while US "
                  "health authorities launched a ten-year payment model rewarding measurable "
                  "outcomes rather than required check-ins.",
         "domain": "biotech", "actor": ["cms"], "score": "59,000 years",
         "evidences": ["resurrection-and-time", "legislating-the-shift"]},
        {"id": "2026-05-14-nvidia-crosses-55-trillion",
         "title": "Nvidia becomes the first company past $5.5 trillion",
         "claim": "Nvidia became the first company to cross a $5.5 trillion market "
                  "capitalization, while Anthropic overtook OpenAI inside one corporate card "
                  "provider's customer base at 34.4% to 32.3% and a quarter of Washington's "
                  "13,000 lobbyists now work AI issues, up from 11% in 2023.",
         "domain": "economics", "actor": ["nvidia", "anthropic", "openai", "ramp"],
         "score": "$5.5T / 25% of lobbyists",
         "evidences": ["ai-as-the-economy", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-11-two-labs-to-out-earn-a-chipmaker"]},
        {"id": "2026-05-14-employees-protest-mouse-tracking",
         "title": "Employees protest software that drafts every cursor twitch into training",
         "claim": "Meta employees are protesting mouse-tracking software on their machines that "
                  "drafts every cursor movement into training their own replacements, while "
                  "Poland pushed a 3% digital services tax on US giants and OpenAI's policy chief "
                  "floated a global AI governance body modeled on the IAEA.",
         "domain": "economics", "actor": ["meta", "openai"],
         "evidences": ["humans-as-peripherals", "work-displaced"],
         "supersedes": [B + "developments/2026-05-12-employees-automate-fake-ai-tasks"]},
    ],
}
