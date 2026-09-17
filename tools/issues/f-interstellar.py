"""Feature — 2026-09-02. The first spacecraft aimed at another star."""
URL = "https://theinnermostloop.substack.com/p/the-first-interstellar-spacecraft"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-09-02", "slug": "feature-interstellar-spacecraft",
        "title": "The First Interstellar Spacecraft to Alpha Centauri", "url": URL,
        "thesis": "In seven decades nobody had aimed a spacecraft at a specific star.",
        "body": """
# The First Interstellar Spacecraft to Alpha Centauri

Both Voyagers carried a golden record, but neither was aimed at a star. In seven
decades no one has ever pointed a spacecraft at a specific star.

The Fermi Explorer Mission announced the first interstellar spacecraft built to
launch now, on existing ion propulsion, toward Alpha Centauri. The cruise takes
roughly 80,000 years. That number is not a flaw in the plan. It is the plan.
""",
    },
    "themes": [
        {"id": "a-spacetime-capsule", "type": "Theme",
         "title": "A payload addressed to the deep future",
         "first_seen": "2026-09-02", "domain": "space",
         "body": "An 80,000-year cruise changes what a payload is for. Less a message "
                 "in a bottle for aliens than a retrievable snapshot of who we are "
                 "now, placed beyond the reach of any catastrophe on Earth."},
        {"id": "hedging-the-fermi-paradox", "type": "Theme",
         "title": "One launch hedges every explanation at once",
         "first_seen": "2026-09-02", "domain": "space",
         "body": "If we are first, someone must begin seeding intelligence outward. "
                 "If a filter lies ahead, this is the window. If we are fenced in, "
                 "reaching the bars is how the keeper notices. Three explanations, "
                 "one action."},
    ],
    "organizations": [
        {"id": "starcloud-inc", "type": "Organization", "title": "Starcloud"},
    ],
    "developments": [
        {"id": "2026-09-02-the-first-spacecraft-aimed-at-a-star",
         "title": "A mission announces the first spacecraft aimed at a specific star",
         "claim": "The Fermi Explorer Mission announced the first interstellar spacecraft built "
                  "to launch now on existing propulsion, on a trajectory toward Alpha Centauri "
                  "just over four light-years away, with a partner startup establishing that "
                  "existing propulsion, trajectory and power can carry a craft that far — the "
                  "first time in seven decades anyone has pointed a spacecraft at a specific star.",
         "domain": "space", "actor": ["fermi-explorer", "physical-si", "starcloud-inc"],
         "score": "4.2 light-years",
         "evidences": ["hedging-the-fermi-paradox", "inhabitable-worlds", "orbit-as-compute"],
         "body": "Earlier proposals aimed at Alpha Centauri on paper but await "
                 "propulsion nobody has built. This one is expected to launch within "
                 "a few years on ion thrusters of a kind already flown."},
        {"id": "2026-09-02-eighty-thousand-years-is-the-plan",
         "title": "An 80,000-year cruise reframes the payload as a spacetime capsule",
         "claim": "At the speeds available the cruise takes roughly 80,000 years, which reframes "
                  "the payload: addressed as plausibly to ourselves or to descendants who "
                  "retrieve it before arrival, a retrievable snapshot placed beyond the reach of "
                  "any catastrophe on Earth, with the mission opening the payload to public "
                  "contributions.",
         "domain": "space", "actor": ["fermi-explorer"], "score": "~80,000 years",
         "evidences": ["a-spacetime-capsule", "resurrection-and-time", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-09-02-the-first-spacecraft-aimed-at-a-star"]},
        {"id": "2026-09-02-one-launch-hedges-every-fermi-answer",
         "title": "Three explanations of the Fermi paradox imply the same action",
         "claim": "If humanity is simply first, the burden of seeding intelligence outward falls "
                  "to us and every replicating lineage begins with one craft that cannot yet "
                  "replicate; if a Great Filter lies ahead, this is the narrow window; and if we "
                  "are inside a quarantine, visibly reaching the bars is how a caged animal gets "
                  "noticed — first, filtered or fenced in, the move is identical.",
         "domain": "space", "actor": ["fermi-explorer"],
         "evidences": ["hedging-the-fermi-paradox", "inhabitable-worlds", "a-spacetime-capsule"],
         "supersedes": [B + "developments/2026-09-02-eighty-thousand-years-is-the-plan"]},
    ],
}
