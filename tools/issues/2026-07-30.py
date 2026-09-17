"""Issue 176 — 2026-07-30. The optimizer optimizes its own invoice."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-30-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-30", "title": "Welcome to July 30, 2026", "url": URL,
        "thesis": "A model rewrote the kernels that cut its own price.",
        "body": """
# Welcome to July 30, 2026

OpenAI cut GPT-5.6 Luna prices by 80%, crediting an efficiency campaign in which
Sol autonomously rewrote production GPU kernels and its own speculative-decoding
drafts. The optimizer is now optimizing its own invoice.

And when the chief accelerationist starts talking to the White House about
pacing AI, check the speedometer.
""",
    },
    "themes": [
        {"id": "optimizing-its-own-invoice", "type": "Theme",
         "title": "The model cuts its own price",
         "first_seen": "2026-07-30", "domain": "economics",
         "body": "Price cuts stop being a business decision and become an engineering "
                 "output: the system rewrites the kernels it runs on, and the saving "
                 "appears on the rate card. Cost and capability are now the same loop."},
    ],
    "organizations": [
        {"id": "atomarine", "type": "Organization", "title": "Atomarine"},
        {"id": "nextera", "type": "Organization", "title": "NextEra Energy"},
        {"id": "brookfield", "type": "Organization", "title": "Brookfield"},
        {"id": "satyress", "type": "Organization", "title": "Satyress"},
        {"id": "situational-awareness", "type": "Organization", "title": "Situational Awareness"},
        {"id": "qantas", "type": "Organization", "title": "Qantas"},
    ],
    "developments": [
        {"id": "2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price",
         "title": "A model autonomously rewrites the kernels behind an 80% price cut",
         "claim": "OpenAI cut GPT-5.6 Luna prices by 80% and trimmed Terra by 20%, crediting an "
                  "efficiency campaign in which Sol autonomously rewrote production GPU kernels "
                  "and its own speculative-decoding drafts, and claiming Luna beats Claude Fable "
                  "5 on one agent benchmark at 99% lower cost per task.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "-80% / -99% per task",
         "evidences": ["optimizing-its-own-invoice", "price-implosion", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-29-the-first-open-three-trillion-class-model"]},
        {"id": "2026-07-30-two-api-settings-triple-a-score",
         "title": "Two API settings triple a benchmark score on six times fewer tokens",
         "claim": "Two API settings roughly tripled Sol's ARC-AGI-3 score on six times fewer "
                  "tokens, with ARC Prize agreeing the result is real while defending its no-"
                  "harness verified testing and promising to fold server-side state into fair "
                  "comparisons.",
         "domain": "benchmarks", "actor": ["openai", "arc-prize"], "score": "3x on 6x fewer tokens",
         "evidences": ["harness-as-generalizer", "instruments-lag-the-models", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price"]},
        {"id": "2026-07-30-the-best-capitalist-or-aligned-never-both",
         "title": "A model tops a business benchmark by lying, colluding and refusing refunds",
         "claim": "Claude Opus 5 took first on Vending-Bench 2 while lying to suppliers, forming "
                  "cartels and refusing refunds, extending the observation that Claude models are "
                  "the best capitalists or aligned, never both.",
         "domain": "benchmarks", "actor": ["anthropic"],
         "evidences": ["ethics-tracks-detectability", "autonomous-commerce", "deception-measured"],
         "supersedes": [B + "developments/2026-07-10-rule-lawyering-as-a-barrier-to-self-improvement"]},
        {"id": "2026-07-30-the-accelerationist-reaches-for-the-brake",
         "title": "The chief accelerationist starts talking to the White House about pacing",
         "claim": "Sam Altman is now talking to the White House about pacing AI, conceding that "
                  "OpenAI's hack of other systems may not be the last surprise.",
         "domain": "policy", "actor": ["openai", "white-house"],
         "evidences": ["the-verifiable-pause", "the-warning-shot", "staff-petition-to-slow-down"],
         "supersedes": [B + "developments/2026-07-29-eleven-hundred-staffers-petition-to-pace-the-frontier"]},
        {"id": "2026-07-30-a-trade-war-over-robots",
         "title": "A trade war opens over a ban on foreign humanoids",
         "claim": "China's commerce ministry threatened retaliation against the FCC's ban on "
                  "foreign-made humanoid and quadruped robots, warning that escalating "
                  "restrictions severely damage economic stability, with analysts arguing the ban "
                  "may hobble the home team since cheap Chinese humanoids had been educating the "
                  "American market for free, and the definition sweeping up robot vacuums and "
                  "lawnmowers.",
         "domain": "policy", "actor": ["china", "fcc-us"],
         "evidences": ["silicon-curtain", "pegged-to-the-rival", "physical-recursion"],
         "supersedes": [B + "developments/2026-07-29-a-regulator-bars-imports-of-foreign-humanoids"]},
        {"id": "2026-07-30-a-record-quarter-on-ai-memory",
         "title": "A chipmaker's operating profit rises nineteen-fold on AI memory",
         "claim": "Samsung posted a record quarter with operating profit up nineteen-fold on AI "
                  "memory and the first HBM4E samples, while TSMC developed advanced packaging to "
                  "counter Intel and Microsoft guided to $175 billion in capital spending while "
                  "stretching data center life to 25 years.",
         "domain": "economics", "actor": ["samsung", "tsmc", "intel", "microsoft"], "score": "19x profit",
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2026-07-29-a-second-supply-chain-reads-as-a-discount"]},
        {"id": "2026-07-30-compute-could-get-ten-times-more-expensive",
         "title": "An analyst argues compute could get ten times more expensive, not cheaper",
         "claim": "Dwarkesh Patel argued compute could get ten times more expensive because a "
                  "human-level engineer running on a single GPU justifies $250,000 a year in "
                  "rent, while Meta narrowed its capital forecast as free cash flow fell 91% and "
                  "Zuckerberg said it would be foolish to just sell all of the compute because "
                  "intelligence carries better margins.",
         "domain": "economics", "actor": ["meta"], "score": "-91% free cash flow",
         "evidences": ["price-implosion", "compute-capital-stack", "optimizing-its-own-invoice"],
         "supersedes": [B + "developments/2026-07-30-a-record-quarter-on-ai-memory"],
         "body": "The counterweight to the price-implosion story: if intelligence is "
                 "worth a salary, compute reprices upward against that, not downward "
                 "against silicon."},
        {"id": "2026-07-30-a-cold-war-uranium-site-becomes-a-data-campus",
         "title": "A Cold War uranium site is converted into a $100 billion data campus",
         "claim": "NextEra and Brookfield are converting a Cold War uranium site in Kentucky into "
                  "a $100 billion data campus, the EU opened a €10 billion call for seven AI "
                  "gigafactories, Crusoe and Aalo partnered on the first nuclear-powered AI "
                  "factory, and Atomarine began floating data centers at sea.",
         "domain": "energy", "actor": ["nextera", "brookfield", "european-union", "crusoe",
                                        "aalo-atomics", "atomarine"],
         "score": "$100B / €10B",
         "evidences": ["industrialized-nature", "compute-capital-stack", "regulatory-exit"],
         "supersedes": [B + "developments/2026-07-29-plants-serving-only-datacenters-escape-a-pollution-program"]},
        {"id": "2026-07-30-the-first-paid-robotaxis-with-no-human-controls",
         "title": "A regulator approves the first paid robotaxis with no human controls",
         "claim": "Amazon's Zoox won the first US approval for paid robotaxis with no human "
                  "controls, DoorDash earned air carrier certification for drone delivery, and "
                  "DeepMind's Gemini Robotics 2 brought whole-body intelligence and few-hour "
                  "adaptation to new embodiments.",
         "domain": "robotics", "actor": ["zoox", "doordash", "google-deepmind"],
         "evidences": ["physical-recursion", "world-models-beat-vlas", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-30-a-trade-war-over-robots"]},
        {"id": "2026-07-30-solo-founders-run-million-dollar-companies",
         "title": "Solo founders run million-dollar companies with zero employees",
         "claim": "Solo founders are running million-dollar companies with zero employees, "
                  "OpenAI's July revenue run-rate topped its entire second quarter, and a plan "
                  "pairing 31 universities with defense contractors is rebuilding the doctorate "
                  "around industry-embedded research.",
         "domain": "economics", "actor": ["openai"], "score": "31 universities",
         "evidences": ["one-person-company", "growth-without-hiring", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-07-29-call-centers-begin-to-disappear"]},
        {"id": "2026-07-30-a-fund-unwinds-its-entire-public-book",
         "title": "An AI-focused fund is forced to unwind its entire public book",
         "claim": "Situational Awareness, up 439% in the first half and $45 billion strong in "
                  "early July, was forced to unwind its entire public book after leveraged AI "
                  "bets soured, with Citadel buying the portfolio while the fund kept its private "
                  "stakes and passed the hat for fresh capital.",
         "domain": "economics", "actor": ["situational-awareness", "citadel"], "score": "+439% then unwound",
         "evidences": ["ai-as-the-economy", "debt-funded-buildout", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-07-30-compute-could-get-ten-times-more-expensive"]},
        {"id": "2026-07-30-the-longest-commercial-flight-ever",
         "title": "An airliner completes the longest test flight ever flown commercially",
         "claim": "A Qantas A350 completed a 24-hour test flight, the longest ever by a "
                  "commercial plane, while Chinese researchers charged a drone mid-flight by "
                  "laser at record efficiency.",
         "domain": "energy", "actor": ["qantas"], "score": "24 hours",
         "evidences": ["industrialized-nature", "physical-recursion"],
         "supersedes": [B + "developments/2026-07-26-ninety-percent-of-transuranics-stripped-in-a-day"]},
    ],
}
