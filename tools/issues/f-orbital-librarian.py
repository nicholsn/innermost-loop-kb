"""Feature — 2026-07-27. The first orbital librarian."""
URL = "https://theinnermostloop.substack.com/p/the-first-orbital-librarian"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-27", "slug": "feature-first-orbital-librarian",
        "title": "The First Orbital Librarian", "url": URL,
        "thesis": "Libraries do not burn. They are abandoned.",
        "body": """
# The First Orbital Librarian

The Library of Alexandria did not die by fire. A scroll in use lives a century
or two, so a great library was never a building — it was a payroll, scribes
recopying the collection faster than the reeds rotted. When the stipends
stopped, the scrolls died of deferred maintenance.

Storage is a noun. A library is a verb. An autonomous agent will fly as a
standing curator, and Alexandria's fate does not transfer: curation that was
labor becomes capital, its stipend sunlight, its copies lossless.
""",
    },
    "themes": [
        {"id": "a-library-is-a-verb", "type": "Theme",
         "title": "Curation, not storage, is the survival technology",
         "first_seen": "2026-07-27", "domain": "society",
         "body": "Vaults preserve bits; only a librarian preserves meaning. Every "
                 "archive that died, died of deferred curation rather than "
                 "catastrophe — and every write-once vault repeats the mistake at "
                 "greater expense."},
    ],
    "developments": [
        {"id": "2026-07-27-libraries-are-abandoned-not-burned",
         "title": "The archive problem is diagnosed as deferred curation, not catastrophe",
         "claim": "The Library of Alexandria likely lost warehoused scrolls to a dockside fire "
                  "but ran for centuries afterward; what killed it was that a scroll in use lives "
                  "a century or two, so the library was a payroll of scribes recopying faster "
                  "than the reeds rotted, and when the stipends stopped the scrolls died of "
                  "deferred maintenance — even the 120-scroll catalog of everything faded "
                  "uncopied, so we lost the list of the books as well as the books.",
         "domain": "society",
         "evidences": ["a-library-is-a-verb", "the-corpus-consumed", "resurrection-and-time"],
         "body": "The modern version is already visible: 38% of the 2013 web is gone "
                 "and half the URLs in Supreme Court opinions point at nothing."},
        {"id": "2026-07-27-an-autonomous-agent-stationed-beside-the-archive",
         "title": "An open agent framework will fly as a standing orbital curator",
         "claim": "Lonestar announced that the open-source Hermes agent framework will fly on its "
                  "orbital vault as the first orbital librarian, an autonomous agent whose "
                  "standing job is curating a sovereign knowledge collection without end — "
                  "organizing collections, maintaining semantic indexes, resolving conflicting "
                  "records and building the retrieval plans from which a customer-selected model "
                  "reasons, sealed inside the owner's data boundary.",
         "domain": "space", "actor": ["lonestar-space", "nous-research"],
         "evidences": ["a-library-is-a-verb", "orbit-as-compute", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-07-27-libraries-are-abandoned-not-burned"],
         "body": "Earlier orbital AI flew as pilot, scientist, companion and oracle. "
                 "Never as a librarian."},
        {"id": "2026-07-27-orbit-is-the-posting-physics-favors",
         "title": "Latency makes orbit the right posting for an archivist rather than an oracle",
         "claim": "Orbit looks like the worst posting for an agent until the job is specified: "
                  "oracles need milliseconds, archivists work between the questions, so pass "
                  "after pass the agent curates while the vacuum serves as the reading-room door, "
                  "with each instance serving one trust domain under one owner's keys and no "
                  "state shared between customers.",
         "domain": "space", "actor": ["lonestar-space"],
         "evidences": ["a-library-is-a-verb", "orbit-as-compute", "distance-is-the-leading-edge"],
         "supersedes": [B + "developments/2026-07-27-an-autonomous-agent-stationed-beside-the-archive"]},
        {"id": "2026-07-27-curation-becomes-capital-rather-than-labor",
         "title": "An autonomous scribe changes the economics that killed every earlier library",
         "claim": "Alexandria's fate does not transfer because the library starved when curation, "
                  "being labor, lost its patrons — whereas an autonomous scribe is capital, its "
                  "stipend sunlight and its copies lossless, so that replacing a satellite is a "
                  "launch where replacing a literature took a renaissance.",
         "domain": "society", "actor": ["lonestar-space"],
         "evidences": ["a-library-is-a-verb", "work-displaced", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-07-27-orbit-is-the-posting-physics-favors"]},
    ],
}
