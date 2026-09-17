"""Feature — 2026-02-15. Physical Superintelligence."""
URL = "https://theinnermostloop.substack.com/p/physical-superintelligence"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-15", "slug": "feature-physical-superintelligence",
        "title": "Physical Superintelligence", "url": URL,
        "thesis": "Physics is the first domino, and every other science waits on it.",
        "body": """
# Physical Superintelligence

The last golden age of physics gave us transistors, nuclear energy and lasers.
A new company is organized around one mission: new physics, at scale — an AI
system that reasons like a theorist, validates like a computational physicist,
tests like an experimentalist, and discovers what none of them could alone.

The framing is a shaped charge: focus superintelligence through a single hard
positive-sum target and the spillover industrializes the whole domain.
""",
    },
    "themes": [
        {"id": "physics-is-the-first-domino", "type": "Theme",
         "title": "Every downstream science waits on physics",
         "first_seen": "2026-02-15", "domain": "science",
         "body": "The solution wavefront begins with mathematics and code, then "
                 "cascades through physics into chemistry, materials, biology and "
                 "planetary systems. The domains are not independent, so "
                 "accelerating the foundation moves everything downstream."},
        {"id": "the-shaped-charge-model", "type": "Theme",
         "title": "Focus superintelligence through one hard target",
         "first_seen": "2026-02-15", "domain": "science",
         "body": "Rather than spreading capability thinly across every problem, aim "
                 "the full force at a single hard positive-sum target and let the "
                 "spillover industrialize the surrounding domain."},
    ],
    "developments": [
        {"id": "2026-02-15-a-vertically-integrated-factory-for-new-physics",
         "title": "A company organizes around producing new physics at scale",
         "claim": "Physical Superintelligence PBC is building what it believes is the first "
                  "vertically integrated factory for physical superintelligence, an AI system "
                  "that reasons like a theorist, validates like a computational physicist, tests "
                  "like an experimentalist, and drives breakthroughs through to commercial "
                  "deployment, organized as a public benefit corporation around the single "
                  "mission of new physics at scale.",
         "domain": "science", "actor": ["physical-si"],
         "evidences": ["physics-is-the-first-domino", "the-shaped-charge-model", "automated-science"],
         "body": "Structured as a public benefit corporation in part because the "
                 "breakthroughs ahead may change both what we understand reality to "
                 "be and what we can build with it."},
        {"id": "2026-02-15-the-shaped-charge-aimed-at-physics",
         "title": "A framework argues countless discoveries are bottlenecked on physics",
         "claim": "The Solve Everything framework maps a solution wavefront beginning with "
                  "mathematics and code then cascading through physics, chemistry, materials, "
                  "biology and planetary systems, arguing that countless discoveries across every "
                  "physical science are bottlenecked on physics breakthroughs no single human "
                  "mind can reach alone — every downstream domino waiting on the first to fall.",
         "domain": "science", "actor": ["physical-si"],
         "evidences": ["physics-is-the-first-domino", "the-shaped-charge-model", "root-node-problems"],
         "supersedes": [B + "developments/2026-02-15-a-vertically-integrated-factory-for-new-physics"]},
    ],
}
