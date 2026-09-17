"""Feature — 2026-03-26. The first tradable compute price index."""
URL = "https://theinnermostloop.substack.com/p/the-first-tradable-compute-price"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-26", "slug": "feature-tradable-compute-index",
        "title": "The First Tradable Compute Price Index", "url": URL,
        "thesis": "No lender can underwrite what it cannot price.",
        "body": """
# The First Tradable Compute Price Index

Nearly $7 trillion of datacenter investment is projected through 2030, and
roughly half must come from debt, infrastructure funds, pensions and sovereign
wealth — institutions that do not write checks they cannot hedge.

Oil got a futures market in 1983, gas in 1990, electricity in 1996. Every
critical commodity is first vital, then opaque, then benchmarked, and the whole
financial stack snaps into place above it. Compute has been stuck at step two.
""",
    },
    "themes": [
        {"id": "compute-becomes-a-commodity", "type": "Theme",
         "title": "The benchmark that lets capital commit",
         "first_seen": "2026-03-26", "domain": "economics",
         "body": "Infrastructure gets built when risk can be transferred, which "
                 "requires a price everyone can see. Without a benchmark, residual "
                 "value and demand shifts are unhedgeable, and the buildout stalls "
                 "for want of financial plumbing rather than demand."},
    ],
    "developments": [
        {"id": "2026-03-26-a-compute-index-derivatives-settle-against",
         "title": "The first compute price index that derivatives reference and settle against",
         "claim": "Ornn published the Ornn Compute Price Index on the Bloomberg Terminal, the "
                  "first compute price index that derivatives reference and settle against, built "
                  "on actual cleared prices from live GPU markets rather than surveys or rate "
                  "cards, with separate indices per GPU type and regional weighting, after "
                  "executing the first compute swap in December 2025.",
         "domain": "economics", "actor": ["ornn"],
         "evidences": ["compute-becomes-a-commodity", "ai-as-the-economy", "compute-capital-stack"]},
        {"id": "2026-03-26-a-gpu-hour-settles-like-electricity",
         "title": "Contracts settle the way power does, because a GPU-hour cannot be warehoused",
         "claim": "The index design draws on electricity because a GPU-hour cannot be warehoused "
                  "— it is consumed the instant it is produced or it is gone — so futures settle "
                  "Asian-style, averaging the volume-weighted price of executed transactions over "
                  "the contract period.",
         "domain": "economics", "actor": ["ornn"],
         "evidences": ["compute-becomes-a-commodity", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-03-26-a-compute-index-derivatives-settle-against"]},
        {"id": "2026-03-26-capital-flowing-blind-into-seven-trillion",
         "title": "Trillions are financed on trust because the underlying cannot be priced",
         "claim": "With nearly $7 trillion of data center investment projected through 2030 and "
                  "the largest four staking $650 billion in a single year, capital has been "
                  "flowing blind: no lender can efficiently underwrite what it cannot price, no "
                  "insurer cover what it cannot benchmark, and no investor mark a position to "
                  "market — so GPU infrastructure was financed like venture deals rather than "
                  "like energy.",
         "domain": "economics", "actor": ["ornn"], "score": "$7T through 2030",
         "evidences": ["compute-becomes-a-commodity", "debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-26-a-gpu-hour-settles-like-electricity"]},
        {"id": "2026-03-26-the-shale-lesson",
         "title": "A revolution begins when the financial infrastructure catches up",
         "claim": "The shale revolution did not begin when drilling technology was ready but when "
                  "lenders could hedge exposure and a futures curve gave capital confidence to "
                  "commit — Edison built the generators, but Samuel Insull securitized the "
                  "revenue streams that turned power into a financeable asset class.",
         "domain": "economics", "actor": ["ornn"],
         "evidences": ["compute-becomes-a-commodity", "bottlenecks-arbitraged-instantly",
                       "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-03-26-capital-flowing-blind-into-seven-trillion"]},
    ],
}
