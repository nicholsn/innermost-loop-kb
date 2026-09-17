"""Feature — 2026-06-16. The first frontier AI token price index."""
URL = "https://theinnermostloop.substack.com/p/the-first-frontier-ai-token-price"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-16", "slug": "feature-token-price-index",
        "title": "The First Frontier AI Token Price Index", "url": URL,
        "thesis": "A posted price is a declaration; a transacted price is a discovery.",
        "body": """
# The First Frontier AI Token Price Index

Oil producers fixed the barrel at 42 gallons in 1866; until then no two
contracts matched. The token is already the AI economy's barrel. What the market
lacked was the price.

No buyer pays the rate card. Caching, the input/output split, provider routing
and model mix mean the posted price and the realized cost have never been the
same number. In oil that gap was political. In AI it is structural.
""",
    },
    "themes": [
        {"id": "the-posted-price-is-not-the-paid-price", "type": "Theme",
         "title": "What a token costs is not what a rate card says",
         "first_seen": "2026-06-16", "domain": "economics",
         "body": "Rate cards are public and nobody pays them. The gap between the "
                 "declared price and the transacted one is where caching, routing "
                 "and model mix live — and it is the only place the real cost curve "
                 "of intelligence can be read."},
    ],
    "developments": [
        {"id": "2026-06-16-a-token-index-built-from-paid-inference",
         "title": "The first token benchmark built from transactions rather than rate cards",
         "claim": "Ornn launched the Ornn Token Price Indices, the first benchmark to price "
                  "frontier-lab tokens from real transactions rather than posted rate cards, with "
                  "separate daily indices for the two leading labs, weighting every model by "
                  "transacted volume into a single dollars-per-million-tokens figure built from "
                  "executed, paid inference.",
         "domain": "economics", "actor": ["ornn", "anthropic", "openai"],
         "evidences": ["the-posted-price-is-not-the-paid-price", "compute-becomes-a-commodity",
                       "price-implosion"],
         "body": "Because every input is paid inference at hundreds of billions to "
                 "trillions of tokens a day, the number is the market itself rather "
                 "than a survey of it."},
        {"id": "2026-06-16-a-unit-value-index-lets-the-mix-in",
         "title": "A unit-value index inverts three centuries of index design",
         "claim": "Where classical index design fixes a basket to isolate pure price, a "
                  "unit-value index does the reverse and lets the live mix into the number, so it "
                  "moves with what the market actually pays — total dollars over total tokens "
                  "bought.",
         "domain": "economics", "actor": ["ornn"],
         "evidences": ["the-posted-price-is-not-the-paid-price", "compute-becomes-a-commodity"],
         "supersedes": [B + "developments/2026-06-16-a-token-index-built-from-paid-inference"]},
        {"id": "2026-06-16-the-real-deflation-is-the-gap",
         "title": "Pricing input and output together exposes the real deflation",
         "claim": "One index prices the input to the AI economy and the other the output, and "
                  "together they read both sides of the cost curve: with cost per unit of a given "
                  "level of intelligence reportedly falling about fortyfold a year, a token price "
                  "holds up as buyers climb to the frontier and slips only as the frontier "
                  "commoditizes — and the gap between the two is the real deflation, the half no "
                  "rate card or capability headline can show.",
         "domain": "economics", "actor": ["ornn", "openai"], "score": "~40x a year",
         "evidences": ["price-implosion", "the-posted-price-is-not-the-paid-price",
                       "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-06-16-a-unit-value-index-lets-the-mix-in"]},
        {"id": "2026-06-16-a-labs-most-guarded-number",
         "title": "A volume-weighted index exposes how traffic splits across a lab's models",
         "claim": "Because the index is volume-weighted from transacted traffic, it carries "
                  "something nobody outside a lab can see — how a provider's traffic actually "
                  "splits across its models, and how fast a new release wins that traffic once it "
                  "ships — normally a lab's most guarded number and the demand signal itself.",
         "domain": "economics", "actor": ["ornn"],
         "evidences": ["the-posted-price-is-not-the-paid-price", "public-internal-divergence",
                       "compute-becomes-a-commodity"],
         "supersedes": [B + "developments/2026-06-16-the-real-deflation-is-the-gap"]},
    ],
}
