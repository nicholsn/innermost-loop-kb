"""Feature — 2026-03-19. The first American professional robotics sports league."""
URL = "https://theinnermostloop.substack.com/p/the-first-american-professional-robotics"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-19", "slug": "feature-robotics-sports-league",
        "title": "The First American Professional Robotics Sports League", "url": URL,
        "thesis": "Industrial strategy disguised as entertainment.",
        "body": """
# The First American Professional Robotics Sports League

Five hundred robots from sixteen countries competed at a former Olympic venue in
Beijing, and the half-marathon runner-up's manufacturer reportedly took over
2,000 commercial orders in the months that followed. These were public testbeds
that compressed the path from prototype to product — industrial strategy
disguised as entertainment.

The US builds the most advanced robots on Earth and then hides them at trade
shows.
""",
    },
    "themes": [
        {"id": "sport-as-benchmark-infrastructure", "type": "Theme",
         "title": "A league is benchmarking infrastructure with an audience",
         "first_seen": "2026-03-19", "domain": "robotics",
         "body": "You cannot solve what you cannot benchmark. Rules, seasons and "
                 "standings make capability legible to a public, and the events that "
                 "look like spectacle function as the shared evaluation a field "
                 "otherwise lacks."},
    ],
    "organizations": [
        {"id": "prorl", "type": "Organization", "title": "Professional Robotics League",
         "body": "Public benefit corporation staging robotics sports events in the US."},
    ],
    "developments": [
        {"id": "2026-03-19-sports-events-as-industrial-strategy",
         "title": "A state uses robot sports to compress prototype to product",
         "claim": "China staged the World Humanoid Robot Games with 500 robots from 16 countries "
                  "at a former Olympic venue, months after the first humanoid half-marathon, with "
                  "the runner-up's manufacturer reportedly receiving over 2,000 commercial orders "
                  "in the months that followed — public testbeds compressing the path from "
                  "prototype to product.",
         "domain": "robotics", "actor": ["china"], "score": "500 robots / 2,000 orders",
         "evidences": ["sport-as-benchmark-infrastructure", "physical-recursion",
                       "science-as-industrial-policy"]},
        {"id": "2026-03-19-the-first-american-professional-robotics-event",
         "title": "The first professional robotics sports event in American history",
         "claim": "The Professional Robotics League will stage its founding Combine on marathon "
                  "weekend in Boston, with humanoid robots sprinting a 50-metre dash on a "
                  "spectator-lined course, the first professional robotics sports event in "
                  "American history, growing toward a full 10-to-12 event season in 2027 with "
                  "standings and team rivalries.",
         "domain": "robotics", "actor": ["prorl"], "score": "50-metre dash",
         "evidences": ["sport-as-benchmark-infrastructure", "physical-recursion"],
         "supersedes": [B + "developments/2026-03-19-sports-events-as-industrial-strategy"]},
        {"id": "2026-03-19-speed-fills-the-stadium-manipulation-proves-the-work",
         "title": "Competition categories expand from speed toward commercially valuable tasks",
         "claim": "The league's categories expand from speed toward commercially valuable tasks — "
                  "the dexterous, task-oriented performance that maps to warehouses, hospitals "
                  "and homes — on the logic that speed gets people into the stadium while "
                  "manipulation and precision challenges show which robots can actually do useful "
                  "work, with a survey finding one in three US sports fans already interested.",
         "domain": "robotics", "actor": ["prorl"], "score": "1 in 3 fans",
         "evidences": ["sport-as-benchmark-infrastructure", "targeting-systems-not-leaderboards",
                       "work-displaced"],
         "supersedes": [B + "developments/2026-03-19-the-first-american-professional-robotics-event"]},
    ],
}
