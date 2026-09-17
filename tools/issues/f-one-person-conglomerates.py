"""Feature — 2026-04-06. The first one-person AI conglomerates."""
URL = "https://theinnermostloop.substack.com/p/the-first-one-person-ai-conglomerates"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-06", "slug": "feature-one-person-conglomerates",
        "title": "The First One-Person AI Conglomerates", "url": URL,
        "thesis": "AI changes the minimum viable size of an organization.",
        "body": """
# The First One-Person AI Conglomerates

Coase asked in 1937 why firms exist at all, and answered: coordination costs.
When coordinating inside a hierarchy is cheaper than across a market, firms
grow. When those costs fall, firms shrink.

AI is the first technology powerful enough to collapse coordination costs to a
single person. That is the shift the technological unemployment debate keeps
missing: it does not just change what work gets done, it changes the minimum
viable size of the organization that does it. You do not need a new job. You
need a fleet.
""",
    },
    "themes": [
        {"id": "coordination-cost-collapse", "type": "Theme",
         "title": "The boundary of the firm reaches one person",
         "first_seen": "2026-04-06", "domain": "economics",
         "body": "Every coordination technology has moved the boundary of the firm — "
                 "rail and telegraph made it larger, the internet made it smaller. "
                 "The first one to drive coordination cost toward a single person's "
                 "attention changes the minimum viable size of an organization, not "
                 "just its productivity."},
    ],
    "organizations": [
        {"id": "him-machines", "type": "Organization", "title": "Henry Intelligent Machines",
         "body": "Public benefit corporation assembling and operating fleets of agent-run "
                 "microbusinesses for individual owners."},
    ],
    "developments": [
        {"id": "2026-04-06-coordination-cost-falls-to-one-persons-attention",
         "title": "An agent layer assembles and operates fleets of microbusinesses for one owner",
         "claim": "Henry Intelligent Machines announced the first AI agent layer that assembles, "
                  "operates and scales fleets of microbusinesses on behalf of individual owners — "
                  "not one business but a diversified fleet spanning publishing, services and "
                  "physical products, with the owner setting direction and agents doing the work.",
         "domain": "economics", "actor": ["him-machines"],
         "evidences": ["coordination-cost-collapse", "one-person-company", "agent-economy"],
         "body": "Ronald Coase's answer to why firms exist at all was coordination "
                 "costs. AI is the first technology powerful enough to collapse them "
                 "to a single person's attention."},
        {"id": "2026-04-06-the-displacement-thesis-inverted",
         "title": "A public benefit corporation aims to create AI-supervising entrepreneurs at scale",
         "claim": "The company is structured as a public benefit corporation whose stated mission "
                  "is to mitigate the 92 million jobs the World Economic Forum projects will be "
                  "displaced by 2030, by creating AI-supervising entrepreneurs at scale — putting "
                  "productive AI assets directly into individual hands rather than distributing "
                  "abundance from the top down.",
         "domain": "economics", "actor": ["him-machines"], "score": "92M jobs by 2030",
         "evidences": ["coordination-cost-collapse", "work-displaced", "post-labor-instruments"],
         "supersedes": [B + "developments/2026-04-06-coordination-cost-falls-to-one-persons-attention"]},
        {"id": "2026-04-06-a-competitors-feature-rebuilt-in-five-minutes",
         "title": "A five-agent organization rebuilds a rival's weeks-long feature in five minutes",
         "claim": "The company's founder had been running a five-agent organization from his desk "
                  "that builds software, researches markets and ships products around the clock, "
                  "and when a competitor announced a major feature after weeks of development, "
                  "his lead agent rebuilt it five minutes after being handed the blog post.",
         "domain": "agents", "actor": ["him-machines", "anthropic"], "score": "5 minutes",
         "evidences": ["coordination-cost-collapse", "one-person-company", "price-implosion"],
         "supersedes": [B + "developments/2026-04-06-the-displacement-thesis-inverted"]},
    ],
}
