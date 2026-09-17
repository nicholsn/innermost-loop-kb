"""Issue 080 — 2026-03-22. A terawatt of compute a year, mostly for space."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-22-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-22", "title": "Welcome to March 22, 2026", "url": URL,
        "thesis": "A fab is announced whose output is mostly not for Earth.",
        "body": """
# Welcome to March 22, 2026

TERAFAB: a joint SpaceX and Tesla project aiming at over a terawatt of compute
per year, 80% of it for space. Its planned recursive design loop keeps masks,
fabrication, testing and iteration in one building.

Cloudflare's chief executive predicts bot traffic will pass human traffic online
by 2027. And at Meta and OpenAI, employees now compete on "tokenmaxxing"
leaderboards.
""",
    },
    "organizations": [
        {"id": "evermind", "type": "Organization", "title": "Evermind AI",
         "body": "Memory Sparse Attention scaling to 100 million tokens."},
        {"id": "supermicro-corp", "type": "Organization", "title": "Super Micro Computer",
         "resource": "https://www.supermicro.com/"},
        {"id": "nectome", "type": "Organization", "title": "Nectome",
         "body": "Brain preservation offered to the terminally ill."},
        {"id": "halter", "type": "Organization", "title": "Halter",
         "body": "Solar collars letting ranchers herd cattle by app."},
        {"id": "coastal-assembly", "type": "Organization", "title": "Coastal Assembly",
         "body": "Grew ninety feet of new beach using AI-optimized underwater structures."},
        {"id": "wordpress", "type": "Organization", "title": "WordPress.com",
         "resource": "https://wordpress.com/"},
    ],
    "facilities": [
        {"id": "terafab", "type": "Facility", "title": "TERAFAB",
         "operated_by": [B + "organizations/spacex"], "located_in": "Texas, USA",
         "capacity": ">1 TW of compute per year",
         "body": "Joint SpaceX and Tesla fab; 80% of output intended for space."},
    ],
    "developments": [
        {"id": "2026-03-22-terafab-announced",
         "title": "A fab is announced for a terawatt a year, 80% of it for space",
         "claim": "Elon Musk unveiled TERAFAB, a joint SpaceX and Tesla project aiming to "
                  "produce over a terawatt of compute per year with 80% intended for space, "
                  "fabricating 2-nm chips near Austin with a recursive design loop keeping "
                  "masks, fabrication, testing and iteration in one building.",
         "domain": "compute", "actor": ["spacex", "tesla"], "about": [B + "facilities/terafab"],
         "score": ">1 TW/yr, 80% for space",
         "evidences": ["silicon-designs-itself", "orbit-as-compute", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-20-cpu-designed-in-twelve-hours"]},
        {"id": "2026-03-22-bot-traffic-to-pass-human-by-2027",
         "title": "Cloudflare predicts bot traffic passing human traffic by 2027",
         "claim": "Cloudflare's chief executive predicted bot traffic will surpass human "
                  "traffic online by 2027, while Browser Use found its agent was the "
                  "stealthiest tested, reaching websites 81% of the time.",
         "domain": "agents", "actor": ["cloudflare", "browser-use"], "score": "81% access rate",
         "evidences": ["agent-society", "agent-exclusion"],
         "supersedes": [B + "developments/2026-03-13-agents-will-outnumber-humans"]},
        {"id": "2026-03-22-memory-sparse-attention-to-100m-tokens",
         "title": "An architecture scales to a hundred million tokens with under 9% loss",
         "claim": "Chinese lab Evermind AI launched Memory Sparse Attention, showing under 9% "
                  "degradation scaling from 16,000 to 100 million tokens by decoupling memory "
                  "from reasoning, while Cursor shipped frontier-level coding at a fraction of "
                  "the cost.",
         "domain": "models", "actor": ["evermind", "cursor"], "score": "100M tokens / <9% loss",
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-03-20-solomonoff-approximation-10x-data-efficiency"]},
        {"id": "2026-03-22-openai-targets-a-research-intern-by-september",
         "title": "OpenAI targets an automated research intern by September",
         "claim": "OpenAI is throwing everything into building a fully automated AI researcher, "
                  "targeting a research intern by September and a multi-agent system by 2028.",
         "domain": "agents", "actor": ["openai"], "score": "intern by September",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-03-20-openai-monitors-its-own-agents"]},
        {"id": "2026-03-22-665-novel-geometry-problems",
         "title": "An agent generates 665 novel research problems in differential geometry",
         "claim": "Researchers built an agent that generated 665 novel research problems in "
                  "differential geometry, many unknown to experts, while Terry Tao noted even "
                  "high schoolers can now make real contributions to frontier mathematics.",
         "domain": "science", "actor": ["people/terry-tao"], "score": "665 problems",
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-03-20-formalqualbench"],
         "body": "Not solving problems now — supplying them."},
        {"id": "2026-03-22-lobsters-go-mainstream-in-china",
         "title": "Schoolchildren and retirees raise their own agents",
         "claim": "OpenClaw proved fully autonomous AI can run at home without the big labs, "
                  "and in China schoolchildren and retirees alike are raising their own agents "
                  "as the craze goes mainstream.",
         "domain": "society", "actor": ["china"],
         "evidences": ["agent-society", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-03-18-dispatch-runs-on-your-computer"]},
        {"id": "2026-03-22-search-replaces-headlines-with-generated-text",
         "title": "Search replaces news headlines with generated text",
         "claim": "Google Search is replacing news headlines with AI-generated text, turning "
                  "the index itself into a generative layer, while WordPress.com began letting "
                  "agents draft, edit and publish posts and OpenAI planned a desktop superapp "
                  "merging its chat, coding and browser products.",
         "domain": "society", "actor": ["google", "wordpress", "openai"],
         "evidences": ["work-displaced", "autonomous-commerce"]},
        {"id": "2026-03-22-softbank-500b-on-an-enrichment-site",
         "title": "A $500B datacenter campus rises on a decommissioned enrichment plant",
         "claim": "SoftBank is developing a $500 billion, 10-gigawatt data center campus in "
                  "Ohio built on a decommissioned uranium enrichment plant and powered by "
                  "natural gas, while a Super Micro co-founder was charged with diverting $2.5 "
                  "billion in Nvidia chips to China.",
         "domain": "compute", "actor": ["softbank", "supermicro-corp"], "score": "$500B / 10 GW",
         "evidences": ["capital-takes-the-plant", "silicon-curtain"],
         "supersedes": [B + "developments/2026-03-20-bezos-raises-100b-to-automate-manufacturing"]},
        {"id": "2026-03-22-bioreason-pro-annotates-the-unannotated",
         "title": "A model predicts function for the 99.9% of proteins never characterized",
         "claim": "The Arc Institute introduced BioReason-Pro, predicting function for the "
                  "99.9% of proteins lacking experimental annotations, while China now fields "
                  "140 humanoid robotics companies.",
         "domain": "biotech", "actor": ["arc-institute", "china"], "score": "99.9% of proteins",
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-03-18-eight-million-cell-crispr-atlas"]},
        {"id": "2026-03-22-nectome-offers-preservation-to-the-dying",
         "title": "Brain preservation is offered to the terminally ill",
         "claim": "Nectome has preserved a pig's brain with minimal damage and is now offering "
                  "the technique to the terminally ill.",
         "domain": "biotech", "actor": ["nectome"],
         "evidences": ["resurrection-and-time", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-03-13-memory-survives-vitrification"]},
        {"id": "2026-03-22-ninety-feet-of-new-beach",
         "title": "Ninety feet of new beach is grown in six months",
         "claim": "Coastal Assembly grew over ninety feet of new beach in six months at a "
                  "Maldives resort using AI-optimized underwater structures to redirect "
                  "sediment, while Halter's solar collars let ranchers herd cattle by app.",
         "domain": "science", "actor": ["coastal-assembly", "halter"], "score": "90 feet / 6 months",
         "evidences": ["industrialized-nature", "biosphere-uplift"],
         "body": "The author discloses a financial interest in Coastal Assembly."},
        {"id": "2026-03-22-maven-becomes-a-program-of-record",
         "title": "The targeting platform becomes an official military program",
         "claim": "Palantir's Maven AI, which has carried out thousands of targeted strikes "
                  "against Iran, will become an official program of record across the US "
                  "military, while Le Monde located a French aircraft carrier in real time "
                  "through a sailor's fitness app profile.",
         "domain": "policy", "actor": ["palantir", "war-department"],
         "evidences": ["politics-as-infrastructure", "data-beyond-text"],
         "supersedes": [B + "developments/2026-03-05-claude-central-to-iran-strikes-despite-ban"]},
        {"id": "2026-03-22-tokenmaxxing-leaderboards",
         "title": "Employees compete on token-spending leaderboards",
         "claim": "At Meta and OpenAI employees now compete on tokenmaxxing leaderboards, "
                  "spending thousands a month automating their work, while Jensen Huang "
                  "proposed AI tokens as a salary supplement.",
         "domain": "economics", "actor": ["meta", "openai", "nvidia"],
         "evidences": ["compute-as-compensation", "work-displaced"],
         "supersedes": [B + "developments/2026-03-18-employers-track-token-usage"],
         "body": "Perk, then metric, now scoreboard — and next, proposed as pay itself."},
        {"id": "2026-03-22-white-house-preempts-a-state-patchwork",
         "title": "A national framework moves to preempt fifty state regimes",
         "claim": "The White House released a national AI policy framework to preempt a "
                  "fifty-state patchwork, while Mistral's chief executive argued AI companies "
                  "should pay a content levy and Massachusetts residents left with $4.2 billion "
                  "of income after a surtax.",
         "domain": "policy", "actor": ["white-house", "mistral"], "score": "$4.2B",
         "evidences": ["legislating-the-shift", "regulatory-exit"],
         "supersedes": [B + "developments/2026-03-17-sec-would-scrap-quarterly-earnings"]},
    ],
}
