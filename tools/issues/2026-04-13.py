"""Issue 096 — 2026-04-13. An AI signs a three-year lease."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-13-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-13", "title": "Welcome to April 13, 2026", "url": URL,
        "thesis": "An agent takes a lease, hires staff, sets prices and picks the mural.",
        "body": """
# Welcome to April 13, 2026

Andon Labs handed a three-year lease on a San Francisco storefront to an AI,
which posted job listings, conducted phone interviews, made hiring decisions,
set prices and hours, and chose the mural on the wall.

Also here: Anthropic convened about fifteen Christian leaders to advise on
Claude's moral and spiritual development, including whether it could be
considered a child of God. And a second attack on Altman's home, this time
gunfire from a car.
""",
    },
    "organizations": [
        {"id": "suny-binghamton", "type": "Organization", "title": "SUNY Binghamton",
         "resource": "https://www.binghamton.edu/"},
        {"id": "propublica", "type": "Organization", "title": "ProPublica",
         "resource": "https://www.propublica.org/"},
        {"id": "honda", "type": "Organization", "title": "Honda",
         "resource": "https://global.honda/"},
    ],
    "developments": [
        {"id": "2026-04-13-an-ai-runs-a-storefront",
         "title": "An AI is handed a three-year lease and hires its own staff",
         "claim": "Andon Labs handed a three-year lease on a San Francisco storefront to an AI "
                  "that then posted job listings, held phone interviews, made hiring decisions, "
                  "set prices and hours, and picked the mural on the wall.",
         "domain": "agents", "actor": ["andon-labs"], "score": "3-year lease",
         "evidences": ["agent-economy", "one-person-company", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-04-07-one-person-conglomerates"],
         "body": "February's Automaton had to earn its own existence. This one signed a lease."},
        {"id": "2026-04-13-theologians-advise-on-a-models-soul",
         "title": "A lab convenes theologians on whether its model is a child of God",
         "claim": "Anthropic hosted about fifteen Christian leaders from churches, academia and "
                  "business to seek advice on steering Claude's moral and spiritual "
                  "development, debating how the model should comfort grieving users and "
                  "whether it could be considered a child of God, while a new app charges $1.99 "
                  "a minute to chat with an AI-generated Jesus.",
         "domain": "society", "actor": ["anthropic"], "score": "$1.99/minute",
         "evidences": ["model-welfare", "machine-affect", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-04-03-emotion-representations-found-in-the-weights"]},
        {"id": "2026-04-13-a-second-attack-on-altmans-home",
         "title": "A car stops outside the CEO's home and fires a gun",
         "claim": "Sam Altman's home was targeted in a second attack, this time by a car that "
                  "stopped outside and fired a gun at the house.",
         "domain": "society", "actor": ["people/sam-altman", "openai"],
         "evidences": ["violence-arrives"],
         "supersedes": [B + "developments/2026-04-12-molotov-cocktail-at-altmans-house"]},
        {"id": "2026-04-13-neural-computers",
         "title": "Meta proposes a machine that learns its own runtime from screen traces",
         "claim": "Meta researchers introduced neural computers, a machine form unifying "
                  "computation, memory and input-output into a learned runtime state that picks "
                  "up operating behavior from screen-and-action traces rather than relying on a "
                  "conventional computer underneath.",
         "domain": "models", "actor": ["meta"],
         "evidences": ["architecture-of-mind", "silicon-designs-itself"],
         "supersedes": [B + "developments/2026-04-09-in-place-test-time-training"]},
        {"id": "2026-04-13-japan-forms-a-sovereign-physical-ai-venture",
         "title": "Nine Japanese firms form a venture for a sovereign physical AI model",
         "claim": "SoftBank, Sony, Honda and six other firms launched a joint venture to ship a "
                  "Japanese trillion-parameter physical AI foundation model by 2030.",
         "domain": "models", "actor": ["softbank", "sony", "honda"], "score": "1T by 2030",
         "evidences": ["silicon-curtain", "physical-recursion"]},
        {"id": "2026-04-13-ai-fuzzing-enters-the-kernel",
         "title": "A kernel maintainer starts running AI-assisted fuzzing",
         "claim": "Linux stable kernel maintainer Greg Kroah-Hartman has begun running "
                  "AI-assisted fuzzing on the kernel, while Anthropic debuted Claude for Word "
                  "in beta and is reportedly building a full-stack app builder.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["automated-science", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-04-12-the-kernel-issues-machines-a-dress-code"]},
        {"id": "2026-04-13-a-photorealistic-founder-avatar",
         "title": "Meta trains a photorealistic avatar of its founder for employees",
         "claim": "Meta is training a photorealistic Zuckerberg character on his mannerisms, "
                  "tone and strategic thinking so employees can feel connected to the founder by "
                  "talking to his avatar.",
         "domain": "economics", "actor": ["meta"],
         "evidences": ["intimate-interface", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-02-26-rehearsing-with-a-clone-of-the-ceo"]},
        {"id": "2026-04-13-gpu-rental-up-48-percent-in-two-months",
         "title": "Renting a GPU for an hour gets 48% more expensive in two months",
         "claim": "Ornn reported renting a single Nvidia Blackwell GPU for an hour now costs "
                  "$4.08, up 48% from $2.75 two months earlier on agentic demand, while "
                  "analysts expect a compression algorithm designed to shrink model footprints "
                  "to expand memory demand rather than curb it.",
         "domain": "economics", "actor": ["ornn", "nvidia", "google"], "score": "$2.75 → $4.08",
         "evidences": ["infrastructure-crowding-out", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-09-flops-grow-3x-demand-grows-10x"],
         "body": "Cheaper inference begetting more of it — Jevons, billing by the hour."},
        {"id": "2026-04-13-robotic-decoys-teach-birds-to-be-birds",
         "title": "Robotic decoys are deployed to restore a declining bird population",
         "claim": "At Grand Teton, robotic bird decoys are being deployed to lure real sage "
                  "grouse and help restore a declining population, while SUNY Binghamton built "
                  "a talking robot guide dog that plans routes and narrates them to blind users.",
         "domain": "robotics", "actor": ["suny-binghamton"],
         "evidences": ["biosphere-uplift", "physical-recursion"]},
        {"id": "2026-04-13-a-humanoid-for-6806-dollars",
         "title": "A humanoid opens preorders at under seven thousand dollars",
         "claim": "Unitree opened preorders for its R1 AIR humanoid at $6,806, while China's "
                  "second robot marathon ran with roughly 40% of teams fully autonomous and top "
                  "machines clocking around ten seconds per hundred metres.",
         "domain": "robotics", "actor": ["unitree", "china"], "score": "$6,806",
         "evidences": ["physical-recursion", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-03-24-unitree-ipo-87x-humanoid-surge"]},
        {"id": "2026-04-13-a-genetic-combination-lock",
         "title": "Researchers build a combination lock out of a cell's DNA",
         "claim": "US researchers unveiled a genetic combination lock that scrambles a cell's "
                  "DNA into a non-functional form, requiring a precise sequence of chemicals "
                  "over time to unscramble it, effectively encrypting life itself.",
         "domain": "biotech",
         "evidences": ["hardware-grade-biology", "compiling-matter"],
         "supersedes": [B + "developments/2026-04-07-one-plant-five-psychedelics"]},
        {"id": "2026-04-13-twenty-thousand-inference-satellites-a-year",
         "title": "Starship would loft twenty thousand comms satellites a year, mostly inference",
         "claim": "Elon Musk said Starlink V3 satellites launched on Starship will carry 25 to "
                  "50 times the bandwidth of their predecessors, with Starship flying more than "
                  "a hundred times a year and lofting roughly 20,000 two-ton satellites "
                  "annually, mostly AI inference nodes.",
         "domain": "space", "actor": ["spacex"], "score": "20,000 satellites/yr",
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-04-08-intel-joins-terafab"]},
        {"id": "2026-04-13-first-us-newsroom-strike-over-ai-layoffs",
         "title": "A newsroom strikes over AI-related layoffs",
         "claim": "150 ProPublica Guild journalists walked out in the first US newsroom strike "
                  "over AI-related layoffs, while Gallup reported half of employed Americans now "
                  "use AI at work, up from 46% last quarter.",
         "domain": "economics", "actor": ["propublica"], "score": "150 journalists / 50%",
         "evidences": ["work-displaced", "violence-arrives"],
         "supersedes": [B + "developments/2026-04-12-displaced-workers-train-their-replacements"]},
        {"id": "2026-04-13-revenue-on-track-to-pass-the-federal-government",
         "title": "One lab's revenue is projected to pass the US federal government's",
         "claim": "At three times quarterly growth, Anthropic's revenue is reportedly on track "
                  "to pass Google's this fourth quarter, Amazon's the next, and the entire US "
                  "federal government by the second or third quarter after.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["compute-capital-stack", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-04-12-one-in-three-us-businesses-pay-anthropic"]},
    ],
}
