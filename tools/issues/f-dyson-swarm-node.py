"""Feature — 2026-06-30. The first Dyson swarm node."""
URL = "https://theinnermostloop.substack.com/p/the-first-dyson-swarm-node"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-30", "slug": "feature-first-dyson-swarm-node",
        "title": "The First Dyson Swarm Node", "url": URL,
        "thesis": "The swarm's leading edge is one number: how far from Earth the compute runs.",
        "body": """
# The First Dyson Swarm Node

A Dyson swarm in the AI age is made of data centers — sun-powered compute that
makes inert matter think. It is assembled one node at a time, outward from home,
and its leading edge is defined by a single number: how far from Earth the
compute actually runs.

By that measure the leading builder is on the Moon, 300,000 kilometers out,
while everyone else is a few hundred kilometers up.
""",
    },
    "themes": [
        {"id": "distance-is-the-leading-edge", "type": "Theme",
         "title": "The swarm is measured by how far the compute runs",
         "first_seen": "2026-06-30", "domain": "space",
         "body": "Orbital compute in low Earth orbit races toward commodity pricing. "
                 "Distance is what cannot be commoditized: the premium, sovereign "
                 "tier belongs to whoever operates furthest out, and scarcity at "
                 "that range confers pricing power."},
        {"id": "if-it-isnt-thinking-it-isnt-working", "type": "Theme",
         "title": "Idle matter is the deepest waste",
         "first_seen": "2026-06-30", "domain": "space",
         "body": "A solar system of matter and energy computing nothing is the "
                 "largest unexploited resource there is. A Dyson swarm is the "
                 "mechanism by which dead mass and sunlight are made to think."},
    ],
    "organizations": [
        {"id": "lonestar-space", "type": "Organization", "title": "Lonestar Space",
         "body": "Operates compute, storage and bandwidth on the lunar surface."},
        {"id": "intuitive-machines", "type": "Organization", "title": "Intuitive Machines"},
        {"id": "sidus-space", "type": "Organization", "title": "Sidus Space"},
    ],
    "developments": [
        {"id": "2026-06-30-the-only-compute-beyond-low-earth-orbit",
         "title": "One company operates the full stack at lunar distance while rivals stay in LEO",
         "claim": "While the contenders for orbital compute all operate a few hundred kilometres "
                  "up, Lonestar Space runs compute, storage and bandwidth on the lunar surface "
                  "300,000 kilometres from Earth — the only one beyond low Earth orbit, let alone "
                  "on the Moon.",
         "domain": "space", "actor": ["lonestar-space", "spacex", "starcloud-inc"],
         "score": "300,000 km",
         "evidences": ["distance-is-the-leading-edge", "orbit-as-compute", "if-it-isnt-thinking-it-isnt-working"]},
        {"id": "2026-06-30-the-only-commercial-payload-that-worked",
         "title": "A lunar data center kept working after its lander tipped over",
         "claim": "In February 2024 the company flew the first software-defined data center to "
                  "the lunar surface and was the only commercial payload that worked even after "
                  "the lander tipped over, transmitting founding documents up for storage and "
                  "back down — the first disaster-recovery data moved to and from the Moon.",
         "domain": "space", "actor": ["lonestar-space", "intuitive-machines"],
         "evidences": ["distance-is-the-leading-edge", "orbit-as-compute", "public-data-withdrawn"],
         "supersedes": [B + "developments/2026-06-30-the-only-compute-beyond-low-earth-orbit"]},
        {"id": "2026-06-30-eight-terabytes-and-a-risc-v-flight-chip",
         "title": "A follow-on carries the first solid-state drives and first RISC-V chip to the Moon",
         "claim": "A 2025 follow-on carried the first solid-state drives to the Moon at eight "
                  "terabytes — nearly seven million times the storage of all nine Apollo missions "
                  "combined — plus the first RISC-V flight chip worth roughly twenty thousand "
                  "Apollo guidance computers, running continuously through thirty-nine lunar "
                  "orbits and holding disaster-recovery data for eight governments.",
         "domain": "space", "actor": ["lonestar-space"], "score": "8 TB / 39 orbits",
         "evidences": ["distance-is-the-leading-edge", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-06-30-the-only-commercial-payload-that-worked"]},
        {"id": "2026-06-30-a-hundred-twenty-million-for-an-l1-constellation",
         "title": "A $120 million agreement funds a constellation at a Lagrange point",
         "claim": "The company holds a $120 million agreement to build an L1 constellation, with "
                  "eight government customers and prior payloads sold out, holding the premium "
                  "sovereign tier uncontested at its distance while compute in low Earth orbit "
                  "races toward commodity pricing.",
         "domain": "space", "actor": ["lonestar-space", "sidus-space"], "score": "$120M",
         "evidences": ["distance-is-the-leading-edge", "orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-30-eight-terabytes-and-a-risc-v-flight-chip"],
         "body": "Figures are company-reported and unverified."},
    ],
}
