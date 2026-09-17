"""Feature — 2026-03-21. The first AI-grown land."""
URL = "https://theinnermostloop.substack.com/p/the-first-ai-grown-land"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-21", "slug": "feature-ai-grown-land",
        "title": "The First AI-Grown Land", "url": URL,
        "thesis": "Land was the bull case for scarcity surviving the Singularity.",
        "body": """
# The First AI-Grown Land

Humans have made land since antiquity — the Dutch poldered, Boston filled its
Back Bay, Dubai dredged the Palm — but every method was expensive enough that
land stayed effectively scarce. Roughly 600,000 acres of artificial land since
2000, about the size of Luxembourg, for tens of billions a year. And the ocean
takes it back.

AI-optimized porous structures grew more than 90 feet of new beach in six
months, not by pumping sand but by telling the ocean where to deposit it.
""",
    },
    "themes": [
        {"id": "land-stops-being-fixed", "type": "Theme",
         "title": "The last asset priced on fixed supply",
         "first_seen": "2026-03-21", "domain": "economics",
         "body": "Trillions of dollars of coastal property are priced on the "
                 "assumption that land supply cannot grow. If sediment can be "
                 "directed rather than dredged, that assumption becomes a liability "
                 "and island nations facing sea-level rise become land producers "
                 "rather than land losers."},
    ],
    "organizations": [
        {"id": "coastal-assembly", "type": "Organization", "title": "Coastal Assembly",
         "body": "Grows land by designing structures that redirect ocean sediment."},
    ],
    "developments": [
        {"id": "2026-03-21-the-ocean-becomes-the-construction-crew",
         "title": "Engineered structures grow 90 feet of beach in six months",
         "claim": "Coastal Assembly completed a field study in which AI-optimized underwater "
                  "structures grew more than 90 feet of new beach in six months, not by pumping "
                  "sand or pouring concrete but by programming the ocean to deposit it, with a "
                  "separate study growing an entirely new island by over 800 cubic metres.",
         "domain": "science", "actor": ["coastal-assembly"], "score": "90 feet in six months",
         "evidences": ["land-stops-being-fixed", "compiling-matter", "industrialized-nature"],
         "body": "For centuries coastal engineering fought the ocean with static "
                 "barriers. This inverts it: porous structures dissipate storm energy "
                 "while letting calm-weather currents carry sediment inward, so sand "
                 "accumulates but does not leave."},
        {"id": "2026-03-21-the-more-land-it-grows-the-better-it-gets",
         "title": "An intelligence layer reads coastlines from space and compounds on its results",
         "claim": "Above the structures sits an intelligence layer that reads satellite imagery, "
                  "decomposes years of shoreline history into predictive models and determines "
                  "where to place structures to redirect sediment, with coordinated swarms of "
                  "autonomous vessels executing deployment and every new site feeding ground "
                  "truth back — so the more land it grows, the better it gets at growing land.",
         "domain": "science", "actor": ["coastal-assembly"],
         "evidences": ["land-stops-being-fixed", "recursive-self-improvement", "physical-recursion"],
         "supersedes": [B + "developments/2026-03-21-the-ocean-becomes-the-construction-crew"]},
        {"id": "2026-03-21-land-was-the-bull-case-for-scarcity",
         "title": "The last domain assumed immune to technological deflation",
         "claim": "Land had been the bull case for scarcity surviving the Singularity — "
                  "physical, tangible and load-bearing, with prime coastal acreage worth $10 "
                  "million an acre or more and trillions of dollars of property priced on the "
                  "assumption that supply is fixed.",
         "domain": "economics", "actor": ["coastal-assembly"], "score": "$10M+ per acre",
         "evidences": ["land-stops-being-fixed", "price-implosion", "scarce-expert-attention"],
         "supersedes": [B + "developments/2026-03-21-the-more-land-it-grows-the-better-it-gets"]},
    ],
}
