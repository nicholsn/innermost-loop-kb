"""Feature — 2026-06-18. The first early-stage ticker symbol."""
URL = "https://theinnermostloop.substack.com/p/the-first-early-stage-ticker-symbol"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-18", "slug": "feature-early-stage-ticker",
        "title": "The First Early-Stage Ticker Symbol", "url": URL,
        "thesis": "A company that assumes it will be acquired thinks like a feature.",
        "body": """
# The First Early-Stage Ticker Symbol

The IPO was how technological progress became shared prosperity. That tradition
eroded: compliance burden rose, the shareholder threshold that forced companies
public was raised, and mega-rounds let startups reach $100 billion valuations
without listing.

This year's landmark listings illustrate the problem rather than solving it. One
grew from $30 billion to $1.77 trillion entirely behind closed doors.
""",
    },
    "themes": [
        {"id": "the-public-market-withdrawal", "type": "Theme",
         "title": "The growth phase happens in private",
         "first_seen": "2026-06-18", "domain": "economics",
         "body": "When the most consequential companies of a generation compound "
                 "privately from tens of billions to trillions, retail investors miss "
                 "the growth phase entirely — and startups aim lower, because a "
                 "company that assumes it will be acquired thinks like a feature "
                 "rather than an institution."},
    ],
    "developments": [
        {"id": "2026-06-18-a-ticker-reserved-as-a-declaration-of-intent",
         "title": "A company reserves an exchange ticker years before any listing",
         "claim": "Ornn reserved the ticker $ORNN on the New York Stock Exchange in what is "
                  "described as the first time a company has reserved a ticker on a major "
                  "exchange not as a step toward an imminent listing but as a long-term "
                  "declaration of intent to become a public company.",
         "domain": "economics", "actor": ["ornn", "nyse"],
         "evidences": ["the-public-market-withdrawal", "ai-as-the-economy",
                       "targeting-systems-not-leaderboards"]},
        {"id": "2026-06-18-thirty-billion-to-one-point-eight-trillion-in-private",
         "title": "A company compounds from $30 billion to $1.77 trillion behind closed doors",
         "claim": "This year's landmark listings, whose combined valuation runs north of $4.5 "
                  "trillion, illustrate the problem rather than solving it, since one of them "
                  "grew from $30 billion to $1.77 trillion entirely behind closed doors, leaving "
                  "retail investors to miss the growth phase of the most consequential companies "
                  "of their lifetime.",
         "domain": "economics", "actor": ["spacex", "openai", "anthropic"],
         "score": "$30B to $1.77T private",
         "evidences": ["the-public-market-withdrawal", "ai-as-the-economy", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-06-18-a-ticker-reserved-as-a-declaration-of-intent"]},
        {"id": "2026-06-18-a-counter-signal-to-stay-private-longer",
         "title": "An early-stage ticker is framed as a counter-signal to staying private",
         "claim": "If the dominant signal in venture for the past decade has been to stay private "
                  "longer, an early-stage company reserving a ticker on a major exchange "
                  "introduces a counter-signal backed by the most recognizable brand in global "
                  "finance, with the exchange anticipating further reservations for additional "
                  "early-stage companies.",
         "domain": "economics", "actor": ["ornn", "nyse", "sec"],
         "evidences": ["the-public-market-withdrawal", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-18-thirty-billion-to-one-point-eight-trillion-in-private"]},
    ],
}
