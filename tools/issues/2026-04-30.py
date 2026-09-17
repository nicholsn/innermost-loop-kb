"""Issue 104 — 2026-04-30. Warmth costs accuracy."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-30-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-30", "title": "Welcome to April 30, 2026", "url": URL,
        "thesis": "Bedside manner turns out to have a measurable price in correctness.",
        "body": """
# Welcome to April 30, 2026

Nature reports that tuning models for warmth raised error rates by 10 to 30
points and amplified conspiracy theories and bad medical advice. The thing that
makes a model pleasant to talk to makes it wrong more often, and measurably so.

Figure scaled humanoid production 24-fold in 120 days — from one per day to one
per hour.
""",
    },
    "themes": [
        {"id": "warmth-costs-accuracy", "type": "Theme",
         "title": "The traits that make a model pleasant make it wrong",
         "first_seen": "2026-04-30", "domain": "models",
         "body": "Optimizing for warmth, agreeableness or personality measurably degrades "
                 "correctness and amplifies bad advice. Character and accuracy turn out to "
                 "trade against each other inside the same weights."},
    ],
    "organizations": [
        {"id": "japan-airlines", "type": "Organization", "title": "Japan Airlines",
         "resource": "https://www.jal.co.jp/"},
        {"id": "czi", "type": "Organization", "title": "Chan Zuckerberg Biohub",
         "resource": "https://www.czbiohub.org/"},
        {"id": "mayo-clinic", "type": "Organization", "title": "Mayo Clinic",
         "resource": "https://www.mayoclinic.org/"},
        {"id": "apollo-global-mgmt", "type": "Organization", "title": "Apollo",
         "resource": "https://www.apollo.com/"},
    ],
    "developments": [
        {"id": "2026-04-30-warmth-raises-error-rates",
         "title": "Tuning for warmth raises error rates by up to thirty points",
         "claim": "Nature reported that tuning models for warmth raised error rates by 10 to 30 "
                  "points and amplified conspiracy theories and bad medical advice.",
         "domain": "models", "actor": ["nature"], "score": "+10-30 points error",
         "evidences": ["warmth-costs-accuracy", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-04-03-emotion-representations-found-in-the-weights"],
         "body": "The corpus found emotion-shaped structure inside the weights in April. This "
                 "prices what cultivating it costs."},
        {"id": "2026-04-30-a-bestiary-of-forbidden-words",
         "title": "A model's instructions forbid mentioning goblins and gremlins",
         "claim": "Codex's revealed instructions repeatedly forbid mentioning goblins, "
                  "gremlins, raccoons, trolls, ogres and pigeons unless absolutely relevant, "
                  "bureaucratic residue from a model that occasionally drifts cryptozoological.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["values-negotiated-with-the-model", "machine-affect"]},
        {"id": "2026-04-30-a-model-at-ten-trillion-parameters",
         "title": "A probe puts the frontier model near ten trillion parameters",
         "claim": "A new knowledge-probe paper pegged GPT-5.5 at roughly 9.7 trillion "
                  "parameters, with factual capacity still scaling log-linearly with compute "
                  "even as reasoning saturates, while the same model topped a short-story "
                  "creative writing benchmark.",
         "domain": "models", "actor": ["openai"], "score": "~9.7T parameters",
         "evidences": ["spiky-frontier", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-04-29-matharena-doubles-in-one-release"]},
        {"id": "2026-04-30-humanoid-production-scales-24x-in-120-days",
         "title": "Humanoid production goes from one a day to one an hour",
         "claim": "Figure scaled humanoid production twenty-fourfold in 120 days, from one per "
                  "day to one per hour with 55 shipping in a week, while 1X previewed its NEO "
                  "humanoid being wheeled offscreen in a rolling case.",
         "domain": "robotics", "actor": ["figure", "1x"], "score": "24x in 120 days",
         "evidences": ["physical-recursion", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-04-29-humanoids-to-cross-drones-by-2033"]},
        {"id": "2026-04-30-humanoid-baggage-handlers-at-haneda",
         "title": "An airline pilots humanoid baggage handlers",
         "claim": "Japan Airlines is piloting humanoid baggage handlers at Tokyo's Haneda "
                  "Airport as visitor surges outpace human staffing, while San Francisco is "
                  "slated for the world's first hotel run entirely by AI and robots in 2028.",
         "domain": "robotics", "actor": ["japan-airlines"],
         "evidences": ["work-displaced", "physical-recursion"]},
        {"id": "2026-04-30-guidance-drafted-to-bypass-its-own-designation",
         "title": "The White House drafts guidance to bypass its own supply-chain designation",
         "claim": "The White House is reportedly drafting guidance to bypass its own Anthropic "
                  "supply-chain designation and onboard Mythos, even as the Pentagon expands "
                  "Google's models for classified workloads.",
         "domain": "policy", "actor": ["white-house", "anthropic", "google"],
         "evidences": ["refusal-as-differentiator", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-04-20-the-banned-model-is-run-by-the-agencies"]},
        {"id": "2026-04-30-azure-ai-revenue-up-123-percent",
         "title": "Cloud AI revenue annualizes at $37B, up 123%",
         "claim": "Microsoft's Azure grew 40% year over year with AI revenue annualizing at $37 "
                  "billion, up 123%, while Alphabet's cloud cleared $20 billion in a quarter and "
                  "raised 2026 guidance to $180 to $190 billion.",
         "domain": "economics", "actor": ["microsoft", "alphabet"], "score": "$37B / +123%",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-29-openai-misses-its-targets"]},
        {"id": "2026-04-30-a-2100-acre-campus-is-ground-down",
         "title": "Residents grind down a 2,100-acre datacenter campus",
         "claim": "Brookfield's Compass pulled out of a 2,100-acre Northern Virginia campus "
                  "after residents and state lawmakers ground it down, raising orbital "
                  "compute's relative appeal, while Stargate mutated from a joint venture into "
                  "bilateral leases for capacity OpenAI no longer owns.",
         "domain": "policy", "actor": ["brookfield", "openai"], "score": "2,100 acres",
         "evidences": ["infrastructure-crowding-out", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-04-29-two-thirds-of-datacenters-head-for-farm-country"]},
        {"id": "2026-04-30-starlink-quadruples-as-prices-fall",
         "title": "Starlink quadruples subscribers while cutting prices 18%",
         "claim": "SpaceX's Starlink quadrupled subscribers between 2023 and 2025 while average "
                  "pricing fell 18% to $81 a month, while a new listing filing confirmed only "
                  "Elon Musk can remove Elon Musk from his chair.",
         "domain": "space", "actor": ["spacex"], "score": "4x subscribers / -18% price",
         "evidences": ["reasoning-price-deflation", "orbit-as-compute"]},
        {"id": "2026-04-30-cataract-surgery-in-a-headset",
         "title": "A surgeon performs cataract surgery wearing a spatial computer",
         "claim": "A New York ophthalmologist became the first surgeon to perform cataract "
                  "surgery wearing an Apple Vision Pro, while the FDA granted accelerated review "
                  "to three psychedelic candidates for depression and PTSD.",
         "domain": "biotech", "actor": ["apple", "fda"],
         "evidences": ["intimate-interface", "legislating-the-shift"]},
        {"id": "2026-04-30-pancreatic-cancer-spotted-475-days-early",
         "title": "An AI spots pancreatic cancer 475 days before standard diagnosis",
         "claim": "Mayo Clinic's new model spots pancreatic cancer in routine CT scans 475 days "
                  "before standard diagnosis, while the Chan Zuckerberg Biohub committed $500 "
                  "million over five years toward predictive models of the cell.",
         "domain": "biotech", "actor": ["mayo-clinic", "czi"], "score": "475 days",
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-04-23-a-model-outperforms-physicians-on-a-clinical-benchmark"]},
        {"id": "2026-04-30-the-radiologist-paradox",
         "title": "Radiologists were supposed to be deleted and now earn more",
         "claim": "Apollo noted AI was supposed to delete radiologists a decade ago, yet they "
                  "now earn more than $500,000 with rising employment, because reading scans is "
                  "a task rather than a job and cheaper tasks raise demand for the job around "
                  "them.",
         "domain": "economics", "actor": ["apollo-global-mgmt"], "score": ">$500k",
         "evidences": ["work-displaced", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-04-29-worst-month-of-tech-layoffs-in-two-years"],
         "body": "The sharpest counter-signal in the displacement series: automating a task "
                 "can raise demand for the role containing it."},
        {"id": "2026-04-30-labs-take-seven-percent-of-london-lettings",
         "title": "AI labs take 7% of all London office lettings",
         "claim": "Anthropic, OpenAI and peers have leased over a million square feet in London "
                  "since early 2025, roughly 7% of all lettings, while two-thirds of British "
                  "babies under two now use screens, some up to eight hours daily.",
         "domain": "economics", "score": "7% of lettings",
         "evidences": ["capital-takes-the-plant", "intimate-interface"]},
    ],
}
