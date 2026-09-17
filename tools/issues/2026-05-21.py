"""Issue 121 — 2026-05-21. A conjecture is disproved."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-21-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-21", "title": "Welcome to May 21, 2026", "url": URL,
        "thesis": "A general-purpose model disproves a long-standing conjecture with ideas of its own.",
        "body": """
# Welcome to May 21, 2026

An internal OpenAI model disproved Erdős's planar unit distance conjecture,
contradicting decades of belief that square grids were optimal — and it came
from a general-purpose model, not a mathematical one. A mathematician described
its reasoning trying a vast array of ideas before honing in with what he called
original ingenious ideas.

Altman called it a kinda big milestone evoking complicated feelings.
""",
    },
    "organizations": [
        {"id": "bexorg", "type": "Organization", "title": "Bexorg",
         "body": "Restoring some function to intact brains from deceased donors."},
        {"id": "intuit", "type": "Organization", "title": "Intuit",
         "resource": "https://www.intuit.com/"},
        {"id": "st-charles", "type": "Organization", "title": "St. Charles City, Missouri"},
        {"id": "commonwealth-prize", "type": "Organization", "title": "Commonwealth Short Story Prize",
         "body": "Whose 2026 winner was immediately accused of being AI-generated."},
    ],
    "developments": [
        {"id": "2026-05-21-a-conjecture-is-disproved",
         "title": "A general-purpose model disproves Erdős's unit distance conjecture",
         "claim": "An internal OpenAI model disproved Erdős's long-standing planar unit distance "
                  "conjecture in discrete geometry, contradicting decades of belief that square "
                  "grids were optimal, with mathematician Arul Shankar noting its reasoning "
                  "tried a vast array of ideas across mathematics before honing in with what he "
                  "called original ingenious ideas.",
         "domain": "science", "actor": ["openai"],
         "evidences": ["automated-science", "root-node-problems", "discovery-as-process"],
         "supersedes": [B + "developments/2026-05-03-the-first-ai-proof-with-downstream-impact"],
         "body": "Notably from a general-purpose model rather than a mathematics-specialized "
                 "one. Altman called it a kinda big milestone evoking complicated feelings."},
        {"id": "2026-05-21-millennium-median-pulled-to-2032",
         "title": "A forecaster pulls her median for the Millennium Prizes to 2032",
         "claim": "Epoch AI's Yafah Edelman pulled her median for solving most Millennium Prize "
                  "Problems forward to 2032, with Noam Brown noting that less than a year ago "
                  "frontier models were merely at olympiad gold level.",
         "domain": "science", "actor": ["epoch-ai", "openai"], "score": "2032",
         "evidences": ["automated-science", "takeoff-declared"],
         "supersedes": [B + "developments/2026-05-20-gemini-for-science"]},
        {"id": "2026-05-21-ninety-day-pre-release-notifications",
         "title": "The White House briefs labs on FDA-style pre-release notification",
         "claim": "The White House is quietly briefing labs on an imminent executive order "
                  "pushing ninety-day pre-release notifications for frontier models, treating "
                  "new releases like drug submissions.",
         "domain": "policy", "actor": ["white-house"], "score": "90 days",
         "evidences": ["legislating-the-shift", "safety-pledges-recede"],
         "supersedes": [B + "developments/2026-05-05-an-executive-order-for-model-review"]},
        {"id": "2026-05-21-nvidia-posts-a-record-quarter-while-conceding-china",
         "title": "A chipmaker posts a record quarter while conceding a market",
         "claim": "Nvidia posted a record $81.6 billion quarter, up 85% year over year, even as "
                  "Jensen Huang acknowledged it has largely conceded the China AI chip market to "
                  "Huawei, while Seagate's chief executive conceded new factories would simply "
                  "take too long relative to demand.",
         "domain": "economics", "actor": ["nvidia", "huawei", "seagate"], "score": "$81.6B / +85%",
         "evidences": ["ai-as-the-economy", "silicon-curtain"],
         "supersedes": [B + "developments/2026-05-14-nvidia-crosses-55-trillion"]},
        {"id": "2026-05-21-paying-fifteen-billion-a-year-to-a-rivals-landlord",
         "title": "A lab pays its rival's owner $15 billion a year for compute",
         "claim": "Anthropic is now paying SpaceX $15 billion per year for compute and scaling "
                  "onto new capacity in Colossus 2 through June, while SpaceX's newly acquired "
                  "AI division bought another $2.8 billion of turbines, placing Anthropic in the "
                  "position of bankrolling its rival's landlord.",
         "domain": "economics", "actor": ["anthropic", "spacex", "xai"], "score": "$15B/yr",
         "evidences": ["compute-capital-stack", "coordination-tax"],
         "supersedes": [B + "developments/2026-05-20-a-twenty-five-billion-tpu-venture"]},
        {"id": "2026-05-21-a-city-bans-large-datacenters",
         "title": "A Missouri city votes to effectively ban large datacenters",
         "claim": "St. Charles City, Missouri voted to effectively ban large-scale data centers, "
                  "a reminder that the buildout still has to clear local zoning meetings.",
         "domain": "policy", "actor": ["st-charles"],
         "evidences": ["infrastructure-crowding-out", "regulatory-exit"],
         "supersedes": [B + "developments/2026-05-17-power-cut-to-49000-residents"]},
        {"id": "2026-05-21-a-total-addressable-market-of-us-gdp",
         "title": "A listing prospectus claims a market the size of US GDP",
         "claim": "SpaceX filed a listing prospectus claiming a $28.5 trillion total addressable "
                  "market, roughly the entire US GDP, spanning broadband, advertising, AI "
                  "infrastructure and an agent platform meant to emulate an entire AI-run "
                  "software company.",
         "domain": "economics", "actor": ["spacex"], "score": "$28.5T",
         "evidences": ["ai-as-the-economy", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-05-18-a-two-point-four-trillion-perpetual"]},
        {"id": "2026-05-21-the-orbital-debate-collapses-to-scheduling",
         "title": "A rival calls orbital datacenters realistic but the timeline ambitious",
         "claim": "Jeff Bezos agreed data centers in space are very realistic but called a two- "
                  "to three-year timeline a little ambitious, a sign the orbital-compute debate "
                  "has collapsed from physics to scheduling.",
         "domain": "space", "actor": ["blue-origin", "spacex"],
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-05-15-a-thousand-times-more-energy-than-we-generate"]},
        {"id": "2026-05-21-function-restored-to-donated-brains",
         "title": "A startup restores some function to brains from deceased donors",
         "claim": "Bexorg is restoring some functions to intact brains from deceased donors, "
                  "hoping to build a better drug development testbed for neurodegenerative "
                  "disease.",
         "domain": "biotech", "actor": ["bexorg"],
         "evidences": ["resurrection-and-time", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-17-one-time-car-t-controls-hiv"]},
        {"id": "2026-05-21-a-hundred-billion-in-philanthropy-becomes-liquid",
         "title": "Up to $100B of philanthropic stakes is about to become liquid",
         "claim": "A wave of $37 to $100 billion in philanthropic funding is about to become "
                  "liquid as one foundation's 26% stake and another's founders' giving pledges "
                  "mature, a six to seventeen percent boost to annual US philanthropy.",
         "domain": "economics", "actor": ["openai-foundation", "anthropic"], "score": "$37-100B",
         "evidences": ["compute-capital-stack", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-05-15-thirty-billion-at-nine-hundred"]},
        {"id": "2026-05-21-founders-offered-tokens-instead-of-cash",
         "title": "Founders are offered $2M in tokens instead of cash",
         "claim": "Sam Altman is offering every Y Combinator founder $2 million in OpenAI tokens "
                  "instead of cash, betting on what he calls tokenmaxxing startups, while the "
                  "company's top lobbyist pursued a reverse-federalism strategy shaping state "
                  "laws the industry can live with.",
         "domain": "economics", "actor": ["openai", "y-combinator"], "score": "$2M in tokens",
         "evidences": ["compute-as-compensation", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-05-14-gpu-hours-as-philanthropy"]},
        {"id": "2026-05-21-a-prize-winner-accused-on-publication",
         "title": "A prize-winning short story is accused of being machine-written on publication",
         "claim": "The Commonwealth short story prize winner was immediately accused of being "
                  "AI-generated upon publication, an ongoing referendum on whether human-only "
                  "literature is even verifiable, while Intuit cut 17% of its workforce and "
                  "Anthropic expected 130% revenue growth to $10.9 billion and its first "
                  "operating profit.",
         "domain": "society", "actor": ["commonwealth-prize", "intuit", "anthropic"],
         "score": "-17% / $10.9B",
         "evidences": ["agent-exclusion", "work-displaced"],
         "supersedes": [B + "developments/2026-05-15-a-monet-mistaken-for-ai-art"]},
    ],
}
