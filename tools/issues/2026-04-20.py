"""Issue 099 — 2026-04-20. The banned model is run by the agencies that banned it."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-20-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-20", "title": "Welcome to April 20, 2026", "url": URL,
        "thesis": "A supply-chain risk is too useful to refuse.",
        "body": """
# Welcome to April 20, 2026

The NSA and the Department of War are running Mythos Preview even after the same
department flagged Anthropic as a supply chain risk. The corpus has followed
this since February: refusal, blacklist, injunction, quiet workarounds, and now
open contradiction.

Meanwhile Mythos is flooding open-source maintainers with bug reports,
conscripting volunteers into a global red team.
""",
    },
    "organizations": [
        {"id": "prorl", "type": "Organization", "title": "ProRL",
         "body": "Hosted America's first professional humanoid and quadruped robot races."},
        {"id": "sonantic", "type": "Organization", "title": "Sonantic",
         "body": "Rebuilt a deceased actor's voice for a feature film."},
        {"id": "esa", "type": "Organization", "title": "European Space Agency",
         "resource": "https://www.esa.int/"},
        {"id": "tinder", "type": "Organization", "title": "Tinder",
         "resource": "https://tinder.com/"},
    ],
    "developments": [
        {"id": "2026-04-20-the-banned-model-is-run-by-the-agencies",
         "title": "The NSA runs the model its own department called a supply chain risk",
         "claim": "Anthropic's Mythos Preview is being run by the NSA and the Department of War "
                  "even after that department flagged Anthropic as a supply chain risk.",
         "domain": "policy", "actor": ["war-department", "anthropic"],
         "evidences": ["refusal-as-differentiator", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-04-17-a-third-expect-entry-level-replaced-in-three-months"],
         "body": "Frontier models turn out to be too useful to refuse, even by the body that "
                 "refused them."},
        {"id": "2026-04-20-maintainers-conscripted-as-a-global-red-team",
         "title": "Open-source maintainers are flooded with machine-found bug reports",
         "claim": "Mythos is flooding open-source maintainers with a large volume of bug "
                  "reports, effectively conscripting volunteers into a global red team, while "
                  "eight European national cyber agencies were locked out as the UK's AI "
                  "Security Institute quietly tested the model and acted on its findings.",
         "domain": "policy", "actor": ["anthropic", "aisi"],
         "evidences": ["war-reaches-the-cloud", "coordination-tax"],
         "supersedes": [B + "developments/2026-04-17-cve-reports-up-263-percent"]},
        {"id": "2026-04-20-agi-becomes-a-version-number",
         "title": "AGI is demoted from prophecy to a point on a release calendar",
         "claim": "Elon Musk announced Grok 4.4 at a trillion parameters for early May, Grok "
                  "4.5 at 1.5 trillion for late May, and Grok 5 as full AGI.",
         "domain": "models", "actor": ["xai"], "score": "1T → 1.5T → AGI",
         "evidences": ["takeoff-declared", "spiky-frontier"],
         "supersedes": [B + "developments/2026-04-09-seven-models-in-training-at-once"]},
        {"id": "2026-04-20-app-releases-up-60-percent",
         "title": "App releases jump 60% against the thesis that chatbots would kill apps",
         "claim": "Worldwide app releases jumped 60% year over year in the first quarter across "
                  "both major stores, confounding the thesis that chatbots would kill apps, "
                  "while Anthropic launched a visual design product powered by Opus 4.7.",
         "domain": "economics", "actor": ["anthropic"], "score": "+60%",
         "evidences": ["software-margin-collapse", "one-person-company"],
         "supersedes": [B + "developments/2026-03-31-ios-app-releases-up-55-percent"]},
        {"id": "2026-04-20-intel-erases-the-dot-com-crash",
         "title": "Intel erases every dollar lost in the dot-com crash after 26 years",
         "claim": "Intel shares erased every dollar lost in the 2000 crash after twenty-six "
                  "years, while Google entered talks with Marvell to co-develop two inference "
                  "chips.",
         "domain": "economics", "actor": ["intel", "google", "marvell"], "score": "26 years",
         "evidences": ["compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2025-12-14-cisco-passes-dotcom-peak"]},
        {"id": "2026-04-20-dram-meets-60-percent-of-demand",
         "title": "Memory supply will meet only 60% of demand through 2027",
         "claim": "Global DRAM supply is expected to meet only 60% of demand through 2027, "
                  "pushing memory to roughly 40% of the manufacturing cost of a low-end "
                  "smartphone by mid-2026, up from 20% today.",
         "domain": "economics", "score": "60% of demand / 20% → 40%",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-03-16-fake-ram-sticks-for-comfort"]},
        {"id": "2026-04-20-the-first-professional-robot-races",
         "title": "America holds its first professional robot races",
         "claim": "ProRL hosted America's first professional humanoid and quadruped robot races "
                  "in Boston, while dozens of Chinese humanoids passed human runners in "
                  "Beijing's second robot half-marathon.",
         "domain": "robotics", "actor": ["prorl", "china"],
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-04-13-a-humanoid-for-6806-dollars"]},
        {"id": "2026-04-20-war-turns-electrification-into-a-hedge",
         "title": "A wartime gas spike turns electrification into a hedge",
         "claim": "The Iran war's gas-price spike pushed used electric vehicle sales up 12% year "
                  "over year and 17% against the prior quarter, while Tesla Robotaxi expanded "
                  "into Dallas and Houston.",
         "domain": "energy", "actor": ["tesla"], "score": "+12% / +17%",
         "evidences": ["war-reaches-the-cloud", "burning-molecules-for-tokens"]},
        {"id": "2026-04-20-new-glenn-reuses-a-booster",
         "title": "Blue Origin reuses a booster as landers race for Artemis III",
         "claim": "Blue Origin's New Glenn flew its third mission and reused a booster for the "
                  "first time, as SpaceX and Blue Origin race to ready lunar landers for "
                  "Artemis III, and NASA picked Falcon Heavy to launch a European rover designed "
                  "to drill for life beneath the Martian surface.",
         "domain": "space", "actor": ["blue-origin", "spacex", "nasa", "esa"],
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-04-12-artemis-splashes-down"]},
        {"id": "2026-04-20-pancreatic-vaccine-responders-alive-at-six-years",
         "title": "Personalized cancer vaccine responders are alive six years on",
         "claim": "Personalized mRNA vaccines for pancreatic cancer are showing durable "
                  "results, with trial responders still alive six years later against a "
                  "thirteen percent five-year survival baseline.",
         "domain": "biotech", "score": "6 years vs 13% at 5",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-04-16-amazon-launches-bio-discovery"]},
        {"id": "2026-04-20-an-iris-scan-to-prove-you-are-human",
         "title": "Dating apps add iris scans to prove users are human",
         "claim": "Tinder users who have had their irises scanned can now display a badge "
                  "signaling they are real people, an admission that the dating pool has gone "
                  "adversarial.",
         "domain": "society", "actor": ["tinder"],
         "evidences": ["agent-exclusion", "coordination-tax"],
         "supersedes": [B + "developments/2026-02-27-headset-scores-employees-on-friendliness"]},
        {"id": "2026-04-20-a-dead-actor-stars-in-a-new-film",
         "title": "A deceased actor stars in a film via an authorized generative reconstruction",
         "claim": "A trailer dropped for the first film to star an authorized generative version "
                  "of a major deceased Hollywood actor, with a UK firm rebuilding his voice and "
                  "his daughter collaborating on the visual reconstruction, while an "
                  "AI-generated performer held the top spot on iTunes.",
         "domain": "society", "actor": ["sonantic"],
         "evidences": ["resurrection-and-time", "work-displaced"],
         "supersedes": [B + "developments/2026-03-06-netflix-buys-an-ai-film-studio"]},
        {"id": "2026-04-20-cs-degrees-fall-for-the-first-time",
         "title": "Computer science falls from fourth-largest major to sixth",
         "claim": "Four-year computer science degrees quintupled from 2008 to 2024 but fell "
                  "from the fourth-largest major to sixth in 2025, the biggest one-year drop of "
                  "any major since 2020, as colleges splintered the field into AI, data "
                  "science, robotics and cybersecurity.",
         "domain": "society", "score": "4th → 6th",
         "evidences": ["ladder-pulled-up", "deskilling"],
         "supersedes": [B + "developments/2026-04-16-two-hundred-siri-engineers-to-bootcamp"]},
        {"id": "2026-04-20-phones-into-a-colander",
         "title": "An attention liberation movement meets to read without phones",
         "claim": "Adherents of an attention liberation movement gathered in a Brooklyn "
                  "brownstone to drop phones into a metal colander for two hours of reading, "
                  "while nearby office workers stared at their bare palms to practice noticing "
                  "real life.",
         "domain": "society",
         "evidences": ["cognitive-load-inverted", "intimate-interface"]},
    ],
}
