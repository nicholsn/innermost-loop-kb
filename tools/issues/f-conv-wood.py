"""Feature — 2026-02-01. A conversation with Cathie Wood."""
URL = "https://theinnermostloop.substack.com/p/a-conversation-with-cathie-wood"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-01", "slug": "feature-conversation-wood",
        "title": "A Conversation with Cathie Wood", "url": URL,
        "thesis": "Delegating to agents looks like commerce to a national accountant.",
        "body": """
# A Conversation with Cathie Wood

The sharpest point in this conversation inverts the usual worry. Commentators
fret that hyper-deflation will reveal a gap between GDP growth and real wealth.
But as humanity subdivides its roles among agents, every interaction between
those subdivisions is *accretive* to GDP and looks like commerce.

So the statistics may explode in real terms while real wealth stays flat —
the opposite failure mode from the one people are bracing for.
""",
    },
    "people": [
        {"id": "cathie-wood", "type": "Person", "title": "Cathie Wood",
         "body": "Founder and chief executive of ARK Invest."},
    ],
    "themes": [
        {"id": "delegation-inflates-gdp", "type": "Theme",
         "title": "Subdividing work into agent transactions inflates the measure",
         "first_seen": "2026-02-01", "domain": "economics",
         "body": "Work done inside one person's head is invisible to national "
                 "accounts. Split across agents that transact with one another and "
                 "the same output becomes measured commerce — so the statistics can "
                 "rise sharply while real wealth does not move."},
    ],
    "developments": [
        {"id": "2026-02-01-agent-delegation-reads-as-commerce",
         "title": "An investor argues agent delegation inflates GDP rather than deflating it",
         "claim": "Against the common worry that hyper-deflation will expose a gap between GDP "
                  "growth and real wealth, Wissner-Gross put to Cathie Wood that as humanity "
                  "delegates more services to agents, the subdivision of human roles makes every "
                  "interaction between those subdivisions accretive to GDP and indistinguishable "
                  "from commerce — so the statistics could explode in real terms while real "
                  "wealth stays constant.",
         "domain": "economics", "actor": ["people/cathie-wood", "ark-invest"],
         "evidences": ["delegation-inflates-gdp", "post-labor-instruments", "dark-output"]},
        {"id": "2026-02-01-real-wealth-is-productivity-growth",
         "title": "An investor defines real wealth growth as technologically enabled productivity",
         "claim": "Asked to define real wealth growth rather than GDP growth, Wood tied it to "
                  "technologically enabled productivity gains rather than price-driven asset "
                  "appreciation, describing the 1980s and 1990s as only a foreshadowing — a "
                  "frustrating early period when technology appeared to hurt productivity, "
                  "followed by software and then the internet unlocking it.",
         "domain": "economics", "actor": ["people/cathie-wood"],
         "evidences": ["delegation-inflates-gdp", "ai-as-the-economy", "post-labor-instruments"],
         "supersedes": [B + "developments/2026-02-01-agent-delegation-reads-as-commerce"]},
    ],
}
