"""Feature — 2026-07-06. The first commercial orbital data embassy."""
URL = "https://theinnermostloop.substack.com/p/the-first-commercial-orbital-data"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-06", "slug": "feature-orbital-data-embassy",
        "title": "The First Commercial Orbital Data Embassy", "url": URL,
        "thesis": "Redundancy is not independence. To win independence you have to leave.",
        "body": """
# The First Commercial Orbital Data Embassy

An embassy is often called foreign soil, but it isn't: its premises are
inviolable while the ground stays the host's. It was always a legal fiction — a
nation's law running where the nation is not.

In orbit that fiction becomes fact. A satellite keeps the jurisdiction of the
state that registered it, so an orbital embassy holds a nation's law beyond the
reach of any court, seizure or earthquake. Off planet, but in country.
""",
    },
    "themes": [
        {"id": "off-planet-but-in-country", "type": "Theme",
         "title": "Jurisdiction without territory",
         "first_seen": "2026-07-06", "domain": "policy",
         "body": "A terrestrial embassy, however well defended, sits inside the "
                 "jurisdiction it is exempt from. Registration law makes orbit the "
                 "only ground where the host is the registry state — the Westphalian "
                 "weld between law and land, remade."},
        {"id": "redundancy-is-not-independence", "type": "Theme",
         "title": "Every terrestrial backup shares Earth's fate",
         "first_seen": "2026-07-06", "domain": "policy",
         "body": "The safest vault on Earth is still on Earth. Copies distributed "
                 "across a single planet hedge local failure and nothing larger, and "
                 "the archives built as failsafes have already been breached by war "
                 "and weather."},
    ],
    "developments": [
        {"id": "2026-07-06-a-legal-fiction-becomes-physical-fact",
         "title": "An orbital data platform makes an embassy's legal fiction into fact",
         "claim": "Lonestar Space will take its sovereign data architecture into Earth orbit in "
                  "April 2027 as the world's first commercially operational space-based sovereign "
                  "data platform, with immutable records under cryptographic key escrow — because "
                  "under the Outer Space Treaty and Registration Convention a satellite stays "
                  "under the jurisdiction of the state that registered it.",
         "domain": "policy", "actor": ["lonestar-space"],
         "evidences": ["off-planet-but-in-country", "orbit-as-compute", "regulatory-exit"],
         "body": "A data center sells computation. A data embassy sells the law that "
                 "governs it."},
        {"id": "2026-07-06-the-safest-vault-on-earth-is-still-on-earth",
         "title": "The archives built as failsafes have already been breached",
         "claim": "Estonia answered a 2007 cyberattack by creating the first data embassy in 2017 "
                  "— full copies of its registries abroad but governed by its own law under "
                  "treaty — while the Svalbard seed vault, the closest thing to a sovereign "
                  "archive on Earth, saw its first withdrawal forced by war in 2015 and its "
                  "entrance flooded by a heat spike in 2016.",
         "domain": "policy",
         "evidences": ["redundancy-is-not-independence", "off-planet-but-in-country",
                       "a-library-is-a-verb"],
         "supersedes": [B + "developments/2026-07-06-a-legal-fiction-becomes-physical-fact"]},
        {"id": "2026-07-06-neither-a-time-capsule-nor-an-air-gap",
         "title": "Prior orbital archives were capsules or vaults, never embassies",
         "claim": "Earlier efforts reached for space as a vault rather than an embassy — a lunar "
                  "library seeded since 2019 as a time capsule rather than sovereign custody, and "
                  "an orbital-storage venture that sold an air-gapped vault beyond reach but "
                  "never flew — whereas an embassy carries a nation's own law upward, retrievable "
                  "and in force, on hardware the nation still controls.",
         "domain": "space", "actor": ["lonestar-space"],
         "evidences": ["off-planet-but-in-country", "a-library-is-a-verb", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-07-06-the-safest-vault-on-earth-is-still-on-earth"]},
        {"id": "2026-07-06-long-term-memory-for-planetary-computation",
         "title": "An orbital archive is framed as long-term memory for planetary-scale computation",
         "claim": "The Singularity runs on civilization's accumulated memory — the training corpus "
                  "its models learn from and the records its institutions depend on — and that "
                  "memory has no safe home on a single planet, making an orbital data embassy "
                  "long-term memory for planetary-scale computation, a monument of information "
                  "that may outlast the stone ones.",
         "domain": "space", "actor": ["lonestar-space"],
         "evidences": ["redundancy-is-not-independence", "the-corpus-consumed", "a-spacetime-capsule"],
         "supersedes": [B + "developments/2026-07-06-neither-a-time-capsule-nor-an-air-gap"]},
    ],
}
