"""Issue 192 — 2026-08-25. Thread lines ration intelligence."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-25-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-25", "title": "Welcome to August 25, 2026", "url": URL,
        "thesis": "Bread lines rationed calories; thread lines ration intelligence.",
        "body": """
# Welcome to August 25, 2026

A national poll finds voters rejecting local data centers 70 to 30 and
preferring a slow buildout over beating China. Texas's governor, who called his
state the epicenter of AI development, now says the industry basically dug its
own grave.

The projected result is thread lines — self-inflicted compute queues. Bread
lines rationed calories; thread lines ration intelligence.
""",
    },
    "themes": [
        {"id": "thread-lines", "type": "Theme",
         "title": "Self-inflicted compute queues",
         "first_seen": "2026-08-25", "domain": "policy",
         "body": "Political resistance to the buildout converts abundance into "
                 "rationing: not scarcity of silicon but of permission to site it. "
                 "The queue forms at the zoning board, and the exit is orbit."},
        {"id": "mind-reading-is-data-limited", "type": "Theme",
         "title": "Decoding scales with data, not physics",
         "first_seen": "2026-08-25", "domain": "biotech",
         "body": "Silent speech decoded from cheap electrodes improves log-linearly "
                 "with training examples and shows no saturation. The limit on "
                 "reading a mind turns out to be how many recordings you have, not "
                 "what the signal permits."},
    ],
    "organizations": [
        {"id": "saildrone", "type": "Organization", "title": "Saildrone"},
        {"id": "penn-state", "type": "Organization", "title": "Penn State"},
        {"id": "coned", "type": "Organization", "title": "Con Edison"},
        {"id": "zola", "type": "Organization", "title": "Zola"},
    ],
    "developments": [
        {"id": "2026-08-25-thread-lines-ration-intelligence",
         "title": "Voters reject local datacenters 70 to 30 and prefer a slow buildout",
         "claim": "A national poll found voters rejecting local data centers 70 to 30 and "
                  "preferring a slow buildout over beating China, with Texas's governor, who once "
                  "called his state the epicenter of AI development, now saying the industry "
                  "basically dug its own grave, and analysts projecting thread lines — "
                  "self-inflicted compute queues.",
         "domain": "policy", "score": "70-30 against",
         "evidences": ["thread-lines", "infrastructure-crowding-out", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-23-a-township-blocks-electrical-infrastructure"],
         "body": "Bread lines rationed calories. Thread lines ration intelligence, "
                 "and the exit is up: an agent-tuned CPU headed to orbit is past any "
                 "zoning board."},
        {"id": "2026-08-25-fifteen-to-twenty-five-percent-of-volume-but-most-of-the-value",
         "title": "An investor predicts closed tokens take a fifth of volume and most of the value",
         "claim": "Gavin Baker expects closed frontier tokens at 15 to 25% of volume but 60 to 90% "
                  "of value, iPhone economics, even as one lab's flagship stuck at 11% of its own "
                  "spend and was overtaken by a cheaper sibling over price and a 30-day retention "
                  "mandate.",
         "domain": "economics", "actor": ["anthropic"], "score": "15-25% volume / 60-90% value",
         "evidences": ["price-implosion", "open-weights-take-the-crown", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-08-23-a-hundred-trillion-free-tokens-a-day"]},
        {"id": "2026-08-25-america-is-llm-pilled-china-is-world-model-pilled",
         "title": "Video eats 70% of one country's tokens as the two markets diverge",
         "claim": "Alibaba shipped Wan3.0, turning spreadsheets into 30-second videos, a day after "
                  "a $10.2 billion share sale and a week after AI capital spending cut earnings "
                  "75%, with video eating 70% of China's tokens — America LLM-pilled, China "
                  "world-model-pilled.",
         "domain": "models", "actor": ["alibaba"], "score": "70% of tokens",
         "evidences": ["world-models-beat-vlas", "silicon-curtain", "price-implosion"],
         "supersedes": [B + "developments/2026-08-23-two-skus-performance-and-pricing"]},
        {"id": "2026-08-25-compute-inequality-in-action",
         "title": "One fund's AI spend rises a hundredfold in five months and keeps doubling",
         "claim": "One fund now spends a hundred times more on AI than in March and is still "
                  "doubling monthly, compute inequality in action, while the heaviest users are "
                  "not coders — Codex use since February grew 108-fold in legal, 41-fold in sales "
                  "and 24-fold in healthcare.",
         "domain": "economics", "actor": ["openai"], "score": "100x since March / 108x in legal",
         "evidences": ["ladder-pulled-up", "most-people-never-see-the-frontier", "work-displaced"],
         "supersedes": [B + "developments/2026-08-15-a-twelve-dollar-median-against-seventy-five-hundred"]},
        {"id": "2026-08-25-batteries-stuck-in-queues-for-want-of-transformers",
         "title": "Batteries sit in interconnection queues for want of transformers",
         "claim": "Batteries are stuck in interconnection queues for want of transformers, with "
                  "one utility's backlog up 300% in two years, while Tesla killed its solar roof "
                  "after 3,000 installs against a promised thousand a week.",
         "domain": "energy", "actor": ["coned", "tesla"], "score": "+300% backlog",
         "evidences": ["thread-lines", "infrastructure-crowding-out", "coordination-tax"],
         "supersedes": [B + "developments/2026-08-19-a-state-binds-datacenters-to-their-own-power-bills"]},
        {"id": "2026-08-25-an-ai-piloted-drone-kills-three-civilians",
         "title": "Investigators attribute three civilian deaths to an AI-piloted drone",
         "claim": "Investigators said an AI-piloted Russian drone running on a cheap edge computer "
                  "killed three civilians in Zaporizhzhia, likely a first, while an uncrewed "
                  "vessel fired two missiles at a naval exercise and a pilotless lifebuoy in "
                  "Hangzhou flies to a drowning swimmer and cuts its rotors so the person can "
                  "cling on.",
         "domain": "robotics", "actor": ["russia", "ukraine", "saildrone"],
         "evidences": ["violence-arrives", "physical-recursion", "agent-society"],
         "supersedes": [B + "developments/2026-08-23-a-humanoid-beats-a-world-record-in-practice"],
         "body": "Same silicon, different objective."},
        {"id": "2026-08-25-old-fiber-turned-into-thousands-of-sensors",
         "title": "Old fiber is turned into thousands of sensors mapping weak zones underground",
         "claim": "Penn State turned old fiber into thousands of sensors and 458 thunderquakes "
                  "into an X-ray of weak zones 300 feet down.",
         "domain": "science", "actor": ["penn-state"], "score": "458 thunderquakes",
         "evidences": ["automated-science", "industrialized-nature"],
         "supersedes": [B + "developments/2026-08-23-entangled-photons-thirteen-miles-through-open-air"]},
        {"id": "2026-08-25-warp-visitors-arrive-quietly-or-not-at-all",
         "title": "Simulations find a warp bubble would either ignite a fireball or barely glow",
         "claim": "Avi Loeb's simulations found a warp bubble crossing the atmosphere above 10% of "
                  "light speed would ignite a terawatt fireball, while a micrometre-scale bubble "
                  "at a few times the speed of sound would glow at a kilowatt — a dim, slow glow "
                  "matching reported observations.",
         "domain": "science",
         "evidences": ["automated-science", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-08-23-a-thousand-launches-a-year-by-2030"]},
        {"id": "2026-08-25-organoids-age-on-a-clock",
         "title": "Brain organoids kept alive five years are found to age on a clock",
         "claim": "Harvard kept human brain organoids alive for five years and found they age on a "
                  "clock, while the FDA cleared a blood test catching Alzheimer's amyloid at over "
                  "90% accuracy.",
         "domain": "biotech", "actor": ["harvard", "fda"], "score": "5 years / >90% accuracy",
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-08-15-organoids-to-replace-animal-testing"]},
        {"id": "2026-08-25-silently-read-words-decoded-with-no-saturation",
         "title": "A dry-electrode headset decodes silently read words with no sign of saturation",
         "claim": "A dry-electrode EEG decoded silently read words from 240,000 trials, scaling "
                  "log-linearly with no saturation — mind reading is data-limited, not "
                  "physics-limited.",
         "domain": "biotech", "score": "240,000 trials",
         "evidences": ["mind-reading-is-data-limited", "intimate-interface", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-08-10-imagined-melodies-reconstructed-from-electrodes"]},
        {"id": "2026-08-25-a-tenth-of-the-web-shows-ai-authorship",
         "title": "A tenth of web pages show AI authorship as the web trains its successor",
         "claim": "Pew found 10% of web pages show AI authorship, over a third of those created "
                  "after ChatGPT, with em dashes doubling, as the web becomes its successor's "
                  "training run, while a Goldman partner warned of cognitive atrophy if reasoning "
                  "is outsourced since apprenticeship transfers tacit skill.",
         "domain": "society", "score": "10% of pages",
         "evidences": ["the-corpus-consumed", "deskilling", "oral-tradition-dissolves"],
         "supersedes": [B + "developments/2026-08-21-a-third-of-submissions-fully-synthetic"]},
        {"id": "2026-08-25-population-peaks-as-synthetic-minds-scale",
         "title": "Fertility falls in 219 of 236 countries as population peaks near 2056",
         "claim": "Economists model fertility falling in 219 of 236 countries with population "
                  "peaking near nine billion in 2056, while Erik Brynjolfsson sees no "
                  "economy-wide job destruction and senior talent in rising demand.",
         "domain": "economics", "actor": ["stanford"], "score": "219 of 236 countries",
         "evidences": ["post-labor-instruments", "work-displaced", "humans-need-not-apply"],
         "supersedes": [B + "developments/2026-08-16-eighty-four-percent-excited-against-thirty-eight"],
         "body": "Synthetic minds scale just as biological ones plateau."},
    ],
}
