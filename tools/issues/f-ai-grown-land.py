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
                  "autonomous surface vessels slated to execute deployment at scale and every new "
                  "site feeding ground truth back — so the more land it grows, the better it gets "
                  "at growing land.",
         "description": "An improvement loop whose training data is the coastline it reshapes: each "
                        "site the system builds in the ocean becomes ground truth for the model that "
                        "sites the next, a data flywheel in geography rather than code.",
         "domain": "science", "actor": ["coastal-assembly"],
         "evidences": ["land-stops-being-fixed", "recursive-self-improvement", "physical-recursion"],
         "supersedes": [B + "developments/2026-03-21-the-ocean-becomes-the-construction-crew"],
         "relatedTo": [B + "developments/2025-12-26-linkerbot-self-assembly",
                       B + "developments/2025-12-20-catl-humanoid-battery-lines"],
         "tags": ["rsi", "continual-learning", "robotics"],
         "supporting_text": "The more land Coastal grows, the better it gets at growing land.",
         "sources": [{"id": "coastal-assembly-site", "resource": "https://coastalassembly.ai/",
                      "title": "Coastal Assembly", "author": "org:coastal-assembly"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Coastal Assembly's platform reads satellite imagery, decomposes years of shoreline "
                 "history into predictive models and picks the placements that will redirect "
                 "sediment; coordinated swarms of autonomous surface vessels are to carry out "
                 "deployment at scale, and each new site returns ground-truth data to the models "
                 "([company site](https://coastalassembly.ai/)). The structures themselves — porous "
                 "forms that let calm-weather currents deposit sand while dissipating storm energy — "
                 "are [recorded separately](/developments/2026-03-21-the-ocean-becomes-the-construction-crew.md); "
                 "this item is the learning layer above them, which [Coastal Assembly](/organizations/coastal-assembly.md), "
                 "built on nine years of Skylar Tibbits's Self-Assembly Lab research at [MIT](/organizations/mit.md), "
                 "says gets better at growing land the more land it grows. In the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it is "
                 "the loop's first appearance in geography, a data flywheel in the ocean alongside the "
                 "[physical recursion](/themes/physical-recursion.md) of "
                 "[humanoids assembling their own hands](/developments/2025-12-26-linkerbot-self-assembly.md), "
                 "and it sets up the same issue's argument that "
                 "[land was the bull case for scarcity](/developments/2026-03-21-land-was-the-bull-case-for-scarcity.md). "
                 "The author discloses a financial interest in the company."},
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
