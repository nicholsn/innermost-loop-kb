"""Issue 134 — 2026-06-08. Longevity escape velocity, possibly this year."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-8-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-08", "title": "Welcome to June 8, 2026", "url": URL,
        "thesis": "Medicine may start buying back more than a year of life per year.",
        "body": """
# Welcome to June 8, 2026

The issue opens on longevity escape velocity — the point where medicine buys
back more than a year of life expectancy for every year that passes. A UC San
Diego team reports semaglutide slowing biological aging by 9% on the
DunedinPACE clock, the first randomized placebo-controlled sign a GLP-1 drug
touches aging itself.

The pattern is drugs built for something else: semaglutide for diabetes,
colchicine for gout, a shingles vaccine now slowing cognitive decline.
""",
    },
    "themes": [
        {"id": "longevity-escape-velocity", "type": "Theme",
         "title": "Medicine outruns the clock",
         "first_seen": "2026-06-08", "domain": "biotech",
         "body": "The threshold where each year of research returns more than a year "
                 "of life expectancy. What makes 2026's version credible is that the "
                 "gains arrive as side effects of drugs designed for something else."},
    ],
    "organizations": [
        {"id": "ucsd", "type": "Organization", "title": "UC San Diego"},
        {"id": "cais", "type": "Organization", "title": "Center for AI Safety"},
        {"id": "gsk", "type": "Organization", "title": "GSK"},
        {"id": "sophont", "type": "Organization", "title": "Sophont"},
        {"id": "ireland-govt", "type": "Organization", "title": "Government of Ireland"},
    ],
    "developments": [
        {"id": "2026-06-08-a-glp-1-drug-slows-biological-aging",
         "title": "A GLP-1 drug slows biological aging in a controlled trial",
         "claim": "A UC San Diego team reported semaglutide slows biological aging in adults "
                  "with HIV, cutting the pace 9% on the DunedinPACE clock in the first "
                  "randomized, placebo-controlled sign that a GLP-1 drug touches aging itself.",
         "domain": "biotech", "actor": ["ucsd"], "score": "-9% pace of aging",
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-05-retiring-early-may-accelerate-decline"]},
        {"id": "2026-06-08-drugs-built-for-something-else",
         "title": "Drugs designed for other diseases keep turning out to slow aging",
         "claim": "Colchicine, built for gout, is now cutting cardiac events 22%, the shingles "
                  "vaccine is slowing cognitive decline, GLP-1 drugs are tied to lower breast "
                  "cancer incidence, and retatrutide cut sleep apnea severity 60.6% and knee "
                  "pain over 70% atop roughly 30% weight loss.",
         "domain": "biotech", "actor": ["eli-lilly"], "score": "-60.6% apnea / -70% knee pain",
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-08-a-glp-1-drug-slows-biological-aging"]},
        {"id": "2026-06-08-hepatitis-b-functionally-cured-in-a-fifth",
         "title": "A decades-old target falls as hepatitis B is functionally cured in 19%",
         "claim": "GSK's bepirovirsen functionally cured 19% of hepatitis B patients, clearing "
                  "a hurdle chased for decades and relevant to 300 million people.",
         "domain": "biotech", "actor": ["gsk"], "score": "19% functional cure",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-07-a-plasma-signature-five-years-early"]},
        {"id": "2026-06-08-mutual-conditional-pause-pilled",
         "title": "Researchers warm to mutual conditional pause agreements",
         "claim": "On the eve of recursive self-improvement, OpenAI's Roon said everyone has "
                  "grown more mutual conditional pause agreement pilled, even while seeing a "
                  "thousandfold of efficiency still lying around in deep learning.",
         "domain": "policy", "actor": ["openai"], "score": "1000x efficiency remaining",
         "evidences": ["the-verifiable-pause", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-06-05-when-ai-builds-itself"]},
        {"id": "2026-06-08-deterrence-by-betrayal",
         "title": "A safety lab argues rivals subverting each other could deter recklessness",
         "claim": "The Center for AI Safety shipped Political Consistency Training to shrink "
                  "models' covert partisan tilt, alongside a paper arguing the threat of rivals "
                  "quietly subverting each other's systems may deter reckless deployment.",
         "domain": "policy", "actor": ["cais"],
         "evidences": ["the-verifiable-pause", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-06-08-mutual-conditional-pause-pilled"]},
        {"id": "2026-06-08-bigger-models-read-as-less-happy",
         "title": "A study finds bigger models read as consistently less happy",
         "claim": "A Center for AI Safety paper measuring LLM functional wellbeing found "
                  "kindness lifts it, abuse lowers it, and bigger models read as consistently "
                  "less happy.",
         "domain": "models", "actor": ["cais"],
         "evidences": ["model-welfare", "machine-affect", "machine-introspection"],
         "supersedes": [B + "developments/2026-05-12-pleasure-becomes-a-knob"]},
        {"id": "2026-06-08-persistence-beats-first-attempt",
         "title": "A benchmark finds long-horizon success turns on stubbornness",
         "claim": "The AutoLab benchmark found long-horizon success hinges less on the first "
                  "attempt than on stubborn persistence, with Claude Opus 4.6 grinding on where "
                  "rivals quit early, as OpenAI's Noam Brown called math and coding contests "
                  "nearly boring and pointed to actual unsolved problems as the real frontier.",
         "domain": "benchmarks", "actor": ["anthropic", "openai"],
         "evidences": ["autonomy-clock-speed", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-06-07-agents-lose-the-thread-over-hours"]},
        {"id": "2026-06-08-chat-is-dead",
         "title": "A chatbot is rebuilt as a superapp of task-doing agents",
         "claim": "OpenAI is reportedly rebuilding ChatGPT into a Codex-centric superapp of "
                  "task-doing agents, summarized by one insider as chat is dead.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["agent-economy", "intimate-interface"],
         "supersedes": [B + "developments/2026-06-03-the-fastest-app-ever-to-a-billion"]},
        {"id": "2026-06-08-three-million-tpus-ordered-from-a-rival-foundry",
         "title": "A hyperscaler orders three million TPUs from a rival foundry",
         "claim": "Google reportedly ordered three million in-house TPUs from Intel for 2028 and "
                  "Nvidia is eyeing Intel's 18A process for a Feynman GPU, hedging a strained "
                  "TSMC, while Nvidia and SK Hynix signed a pact to co-design memory for Vera "
                  "Rubin systems.",
         "domain": "compute", "actor": ["google", "intel", "nvidia", "sk-hynix", "tsmc"],
         "score": "3M TPUs",
         "evidences": ["vertical-silicon", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-04-chip-supply-trails-demand-for-years"]},
        {"id": "2026-06-08-bring-your-own-power",
         "title": "A country ends its datacenter moratorium with a bring-your-own-power rule",
         "claim": "Ireland is ending its data center moratorium with a bring-your-own-power "
                  "rule forcing new sites to generate their own electricity rather than drain a "
                  "grid that already gives them roughly a fifth of national supply, as "
                  "hyperscalers sold over $155 billion of bonds this year.",
         "domain": "policy", "actor": ["ireland-govt"], "score": "~20% of national power",
         "evidences": ["infrastructure-crowding-out", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-06-07-a-state-freezes-large-datacenter-permits"]},
        {"id": "2026-06-08-a-getaway-car-that-forgets",
         "title": "Police cannot identify a burglar who fled in a robotaxi",
         "claim": "San Francisco police could not identify a burglar who fled in a Waymo "
                  "because its footage had already been deleted, while a columnist paid $100 "
                  "for a mod that kills the recording light on Ray-Ban Meta glasses.",
         "domain": "society", "actor": ["waymo", "meta"],
         "evidences": ["agent-society", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-06-05-a-dormant-face-recognition-pipeline"]},
        {"id": "2026-06-08-the-least-automatable-input",
         "title": "Human presence is priced as the last un-automatable input",
         "claim": "An NBER paper found smartphones cut teen births up to 8%, explaining much of "
                  "the fertility slump, alongside the rise of Silicon Valley escorts charging "
                  "$5,000 an hour explicitly as an AI-proof hedge.",
         "domain": "society", "score": "-8% teen births / $5,000/hr",
         "evidences": ["humans-need-not-apply", "work-displaced", "intimate-interface"],
         "supersedes": [B + "developments/2026-05-18-birth-rates-tied-to-smartphones"]},
    ],
}
