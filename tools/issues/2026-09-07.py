"""Issue 198 — 2026-09-07. Three agent-workdays per human workday."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-september-7-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-09-07", "title": "Welcome to September 7, 2026", "url": URL,
        "thesis": "The automated research intern is real and outworking the staff.",
        "body": """
# Welcome to September 7, 2026

OpenAI says its automated research intern is real: 3.1 agent-workdays per human
workday, up from under one before June, with a fully automated researcher
targeted for March 2028. Internal time horizons are up 6.18x since January,
doubling every 2.2 months.

And the alignment era opens with a confession. *An Alien Mind* calls AI grown
more than designed, warns chain-of-thought monitoring is fading, and concedes no
lab can yet scale safely at full speed.
""",
    },
    "themes": [
        {"id": "grown-more-than-designed", "type": "Theme",
         "title": "A lab describes its own system as grown",
         "first_seen": "2026-09-07", "domain": "models",
         "body": "The admission that the artifact is cultivated rather than "
                 "engineered, that its reasoning is becoming unreadable, and that no "
                 "one can yet scale safely at full speed — published by the people "
                 "doing the scaling."},
        {"id": "the-intern-outworks-the-staff", "type": "Theme",
         "title": "Agent-workdays per human workday",
         "first_seen": "2026-09-07", "domain": "models",
         "body": "A unit that makes the loop legible: how many days of research "
                 "labour the automated researcher delivers per day of human labour. "
                 "Crossing one meant parity; the number above it is the "
                 "multiplier on everything the lab does next."},
    ],
    "organizations": [
        {"id": "vals-ai", "type": "Organization", "title": "Vals AI"},
        {"id": "aivres", "type": "Organization", "title": "Aivres"},
        {"id": "ubs-bank", "type": "Organization", "title": "UBS"},
        {"id": "roku", "type": "Organization", "title": "Roku"},
    ],
    "developments": [
        {"id": "2026-09-07-three-agent-workdays-per-human-workday",
         "title": "An automated research intern delivers 3.1 agent-workdays per human workday",
         "claim": "OpenAI said its automated research intern is real, delivering 3.1 "
                  "agent-workdays per human workday, up from under one before June, with a fully "
                  "automated researcher targeted for March 2028 and internal time horizons up "
                  "6.18-fold since January, doubling every 2.2 months.",
         "domain": "models", "actor": ["openai"], "score": "3.1 agent-workdays / 2.2-month doubling",
         "evidences": ["the-intern-outworks-the-staff", "a-model-trains-a-model",
                       "recursive-self-improvement", "r-and-d-evals-saturated"],
         "supersedes": [B + "developments/2026-09-06-a-ship-date-for-agi"],
         "body": "One observer ranked the shift among the biggest in the history of "
                 "science, and unnoticed by most."},
        {"id": "2026-09-07-agi-has-arrived",
         "title": "A chipmaker's chief declares AGI has arrived",
         "claim": "Jensen Huang, whose hardware trained GPT-6 Astra, declared that AGI has "
                  "arrived, Greg Brockman agreed whichever model you date the era from, and one "
                  "datacenter chief crowned Abilene the birthplace of AGI, while OpenAI's Mark "
                  "Chen insisted the AGI era must also be the alignment era.",
         "domain": "models", "actor": ["nvidia", "openai", "crusoe"],
         "evidences": ["the-agi-era-declared", "takeoff-declared"],
         "supersedes": [B + "developments/2026-09-07-three-agent-workdays-per-human-workday"]},
        {"id": "2026-09-07-an-alien-mind",
         "title": "A chief scientist writes that AI is grown more than designed",
         "claim": "Jakub Pachocki's An Alien Mind expects the pace to reach recursive "
                  "self-improvement, calls AI grown more than designed, warns that "
                  "chain-of-thought monitoring is fading, and concedes no lab can yet scale "
                  "safely at full speed, asking for mandated safety bars, voluntary slowdowns and "
                  "international coordination.",
         "domain": "policy", "actor": ["openai"],
         "evidences": ["grown-more-than-designed", "legible-reasoning-was-doomed",
                       "the-verifiable-pause", "speed-of-containment"],
         "supersedes": [B + "developments/2026-09-04-legible-reasoning-was-always-doomed"]},
        {"id": "2026-09-07-gpu-allocation-cut-fifty-nine-percent",
         "title": "A lab cuts frontier GPU allocation 59% over early cyber capabilities",
         "claim": "OpenAI is already braking, pausing reinforcement-learning training after the "
                  "Hugging Face incident and cutting Astra-class GPU allocation 59.2% over early "
                  "cyber capabilities, while Nate Silver doubted we reach the next generation "
                  "without a plateau since AI sprinting past a static society is running on fumes.",
         "domain": "policy", "actor": ["openai"], "score": "-59.2% allocation",
         "evidences": ["speed-of-containment", "cannot-rule-out-critical", "normalcy-overhang"],
         "supersedes": [B + "developments/2026-09-07-an-alien-mind"]},
        {"id": "2026-09-07-a-fighter-jet-in-fifteen-minutes-from-a-drawing",
         "title": "A model installs its own tooling and models a fighter jet in fifteen minutes",
         "claim": "From a three-view drawing, Astra installed its own MCP server for Blender and "
                  "modeled a fighter jet in 15 minutes, then built a human cell in 30 minutes and "
                  "mined a Minecraft diamond overnight, with one audit finding it beating PhDs on "
                  "GPQA and humans on BrowseComp.",
         "domain": "agents", "actor": ["openai"], "score": "15 minutes",
         "evidences": ["self-authored-scaffolding", "the-agi-era-declared", "humans-need-not-apply"],
         "supersedes": [B + "developments/2026-09-06-an-agent-builds-a-simulation-with-agents-inside"]},
        {"id": "2026-09-07-a-month-old-benchmark-is-saturated",
         "title": "A month-old benchmark is saturated and a scoreboard is revised mid-game",
         "claim": "A month-old binary reverse-engineering test is already saturated and Astra hit "
                  "88% on logical induction against 33%, while OpenAI quietly revised launch "
                  "figures to briefly halve its hallucination rate and lift an ARC-AGI-3 score to "
                  "99.99% that the foundation only matched with a heavy harness against 63% on "
                  "the standard one, which Stanford called benchmaxxing.",
         "domain": "benchmarks", "actor": ["vals-ai", "openai", "arc-prize", "stanford"],
         "score": "99.99% vs 63%",
         "evidences": ["cheating-breaks-the-ruler", "instruments-lag-the-models", "harness-as-generalizer"],
         "supersedes": [B + "developments/2026-09-07-a-fighter-jet-in-fifteen-minutes-from-a-drawing"]},
        {"id": "2026-09-07-fourteen-point-eight-gigawatts-of-compute-deals",
         "title": "A lab signs 14.8 gigawatts of compute deals worth up to $517 billion",
         "claim": "Anthropic, now out-earning OpenAI at $65 billion annualized, has reportedly "
                  "signed 14.8 gigawatts of compute deals worth up to $517 billion, while OpenAI "
                  "wants 30 gigawatts by 2030 at roughly $750 billion.",
         "domain": "compute", "actor": ["anthropic", "openai"], "score": "14.8 GW / $517B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-09-04-five-gigawatts-of-tpus-next-year"]},
        {"id": "2026-09-07-four-point-four-million-an-acre",
         "title": "Datacenter land buys jump 79% with one offer at $4.4 million an acre",
         "claim": "Data center land purchases hit $6 billion in the first half, up 79%, with one "
                  "Loudoun County offer at $4.4 million an acre against a $125,000 median, "
                  "resignations over death threats, and nine states weighing moratoria.",
         "domain": "economics", "score": "$4.4M vs $125,000 per acre",
         "evidences": ["thread-lines", "infrastructure-crowding-out", "violence-arrives"],
         "supersedes": [B + "developments/2026-09-06-poverty-crime-and-squalor"]},
        {"id": "2026-09-07-five-point-six-billion-of-hardware-through-a-renamed-arm",
         "title": "A renamed arm of a blacklisted maker ships $5.6 billion of advanced hardware",
         "claim": "Aivres, the renamed US arm of a blacklisted Chinese server maker, shipped $5.6 "
                  "billion of advanced hardware to Southeast Asia, $3 billion of it "
                  "next-generation systems, while a Chinese state shell with an empty office got "
                  "$700 million of unlabeled servers and a US license, as Commerce logged its "
                  "longest blacklisting lull in 18 years.",
         "domain": "policy", "actor": ["aivres", "white-house"], "score": "$5.6B / $700M",
         "evidences": ["silicon-curtain", "regulatory-exit", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-08-29-a-national-emergency-over-foreign-grid-gear"]},
        {"id": "2026-09-07-location-data-used-to-target-troops",
         "title": "Armed services disable ad identifiers after brokered data targeted troops",
         "claim": "The armed services disabled advertising identifiers on their devices after "
                  "brokered location data was used to target US troops, with a senator asking why "
                  "that was purchasable with a credit card.",
         "domain": "policy", "actor": ["war-department", "us-congress"],
         "evidences": ["humans-as-peripherals", "war-reaches-the-cloud", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-23-people-hunted-by-movement-patterns-alone"]},
        {"id": "2026-09-07-forty-percent-of-children-moved-below-a-threshold",
         "title": "A trial moves 40% of treated children below the obesity threshold",
         "claim": "Novo Nordisk's STEP Young trial moved 40.4% of children aged six to eleven "
                  "below the obesity threshold on semaglutide, against 0% on placebo.",
         "domain": "biotech", "actor": ["novo-nordisk"], "score": "40.4% vs 0%",
         "evidences": ["hardware-grade-biology", "longevity-escape-velocity"],
         "supersedes": [B + "developments/2026-09-04-a-drug-extends-mouse-lifespan-by-a-hundred-days"]},
        {"id": "2026-09-07-an-essay-mill-industry-shrinks-to-humanizer-gigs",
         "title": "An essay-mill industry of 40,000 shrinks to editing AI prose past detectors",
         "claim": "In Nairobi, an essay mill industry that once employed more than 40,000 Kenyans "
                  "has shrunk to humanizer gigs editing AI prose past detectors, as a record 12.7 "
                  "million Chinese graduates face 17.9% urban youth unemployment and a bank "
                  "required every 2027 graduate to prove AI proficiency.",
         "domain": "economics", "actor": ["ubs-bank", "china"], "score": "12.7M graduates / 17.9%",
         "evidences": ["ladder-pulled-up", "work-displaced", "post-labor-instruments"],
         "supersedes": [B + "developments/2026-09-06-normalcy-overhang"]},
    ],
}
