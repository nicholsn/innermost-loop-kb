"""Issue 050 — 2026-02-09. The Singularity buys a Super Bowl spot."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-9-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-09", "title": "Welcome to February 9, 2026", "url": URL,
        "thesis": "The frontier stops being a subculture and buys thirty-second spots.",
        "body": """
# Welcome to February 9, 2026

AI dominated Super Bowl ad inventory. OpenAI flashed references to The
Singularity Is Near before telling viewers to just build things. Anthropic
bought a spot to make fun of ad-supported AI. Meta advertised blue-collar
datacenter jobs in New Mexico and Iowa.

Musk announces a self-growing city on the Moon within ten years, then confirms
the plan to shoot lunar material into deep space with mass drivers, calling a
slowly disintegrating moon an incredible visual.
""",
    },
    "organizations": [
        {"id": "argonne", "type": "Organization", "title": "Argonne National Laboratory",
         "resource": "https://www.anl.gov/"},
        {"id": "essilor-meta", "type": "Organization", "title": "Ring",
         "body": "Amazon home security brand; promoted AI search parties for lost pets."},
    ],
    "developments": [
        {"id": "2026-02-09-ai-dominates-the-super-bowl",
         "title": "AI takes over the Super Bowl ad break",
         "claim": "For the first time AI dominated Super Bowl advertising, with OpenAI "
                  "referencing The Singularity Is Near before telling viewers to just build "
                  "things, Anthropic mocking ad-driven models, Meta pitching blue-collar "
                  "datacenter jobs, and Google showing a family designing a home with an image "
                  "model.",
         "domain": "society", "actor": ["openai", "anthropic", "meta", "google", "amazon"],
         "evidences": ["intimate-interface", "work-displaced"],
         "body": "The frontier stops being a subculture."},
        {"id": "2026-02-09-humanoids-and-longevity-sold-on-tv",
         "title": "Humanoids and longevity are sold in the ad break",
         "claim": "Svedka advertised humanoid robots partying, Ramp showed a character "
                  "multiplying himself to do more work, and Hims and Hers mocked Jeff Bezos and "
                  "Bryan Johnson to sell democratized longevity.",
         "domain": "society",
         "evidences": ["work-displaced", "hardware-grade-biology"]},
        {"id": "2026-02-09-self-growing-city-on-the-moon",
         "title": "SpaceX targets a self-growing lunar city within ten years",
         "claim": "Elon Musk announced a shift toward building a self-growing city on the Moon "
                  "within ten years, delaying Mars, and confirmed plans to use mass drivers to "
                  "shoot lunar material into deep space for solar-powered AI satellites, "
                  "calling a slowly disintegrating moon an incredible visual.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["industrialized-nature", "orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-02-08-spacex-hires-for-orbital-datacenters"]},
        {"id": "2026-02-09-spacex-2t-ipo-odds",
         "title": "Markets give SpaceX better than even odds of a $2T IPO",
         "claim": "Prediction markets now give SpaceX above a 40% chance of exceeding a $2 "
                  "trillion valuation at IPO.",
         "domain": "economics", "actor": ["spacex"], "score": ">40% of $2T",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-29-spacex-ipo-at-15-trillion"]},
        {"id": "2026-02-09-no-reason-to-have-grad-students-pipetting",
         "title": "OpenAI says there is no reason for grad students to pipette",
         "claim": "OpenAI's Kevin Weil argued there is no reason to have graduate students "
                  "pipetting when models can reason for days and hand off to robots, while "
                  "Argonne scientists used AI to run 6,000 battery experiments in five months.",
         "domain": "science", "actor": ["openai", "argonne"], "score": "6,000 experiments",
         "evidences": ["automated-science", "work-displaced"],
         "supersedes": [B + "developments/2026-02-08-opus-tops-critpt-physics"]},
        {"id": "2026-02-09-t-glass-shortage",
         "title": "A microscopic Japanese fiber becomes a bottleneck",
         "claim": "Apple and Nvidia are facing shortages of T-glass, a microscopic Japanese "
                  "fiber essential to chip substrates, while Amazon's AI capex will consume all "
                  "its free cash flow this year.",
         "domain": "compute", "actor": ["apple", "nvidia", "amazon"],
         "evidences": ["infrastructure-crowding-out", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-02-08-replace-dram-with-light"]},
        {"id": "2026-02-09-china-adds-434gw",
         "title": "China adds 434 GW of wind and solar in a year",
         "claim": "China added 434 GW of wind and solar in 2025, covering all new electricity "
                  "demand and pushing coal's share down a point.",
         "domain": "energy", "actor": ["china"], "score": "434 GW",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-01-25-china-consumes-double-us-power"]},
        {"id": "2026-02-09-unitree-shovels-snow",
         "title": "Humanoids attempt to shovel snow in Lithuania",
         "claim": "Unitree humanoids were spotted attempting to shovel snow in Lithuania, while "
                  "Tesla announced high-volume Semi production this year.",
         "domain": "robotics", "actor": ["unitree", "tesla"],
         "evidences": ["physical-recursion", "autonomy-clock-speed"]},
        {"id": "2026-02-09-last-chance-to-secure-employment",
         "title": "An OpenAI lead calls this the last chance to secure employment",
         "claim": "An OpenAI lead warned this is the last opportunity to secure employment "
                  "before fast takeoff disrupts the job market, while many students are opting "
                  "for un-college as entry-level white-collar jobs vanish.",
         "domain": "economics", "actor": ["openai"],
         "evidences": ["ladder-pulled-up", "work-displaced", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-08-worst-job-cuts-since-the-recession"]},
        {"id": "2026-02-09-two-hundred-novels-a-year",
         "title": "Romance writers publish two hundred novels a year",
         "claim": "Romance writers are now publishing 200 novels a year using AI, while a "
                  "former Andreessen partner noted enterprise rather than consumer is where the "
                  "money is.",
         "domain": "economics", "score": "200 novels/yr",
         "evidences": ["work-displaced", "software-margin-collapse"]},
        {"id": "2026-02-09-sweetly-but-sadly-transcendent",
         "title": "Yegge describes the mood at Anthropic as sadly transcendent",
         "claim": "Steve Yegge described the mood at Anthropic as sweetly but sadly "
                  "transcendent, with staff pitying people at other companies who do not see "
                  "what is coming.",
         "domain": "society", "actor": ["anthropic"],
         "evidences": ["takeoff-declared", "cognitive-load-inverted"],
         "supersedes": [B + "developments/2026-02-03-altman-felt-useless"]},
        {"id": "2026-02-09-omega-3-and-dementia",
         "title": "Blood omega-3 is inversely linked to early-onset dementia",
         "claim": "Researchers found blood omega-3 levels inversely related to early-onset "
                  "dementia risk.",
         "domain": "biotech", "evidences": ["hardware-grade-biology"]},
        {"id": "2026-02-09-bot-bowl-party",
         "title": "A human throws a party for agents and few show up",
         "claim": "OpenClaw partnered with VirusTotal to scan agent skills for malware, and a "
                  "human set up a Bot Bowl Party for agents to discuss the game autonomously, "
                  "though few attended.",
         "domain": "agents",
         "evidences": ["agent-society", "machine-affect"],
         "supersedes": [B + "developments/2026-02-08-kawaii-shells-for-agents"]},
    ],
}
