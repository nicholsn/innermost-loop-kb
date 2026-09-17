"""Feature — 2026-03-01. A conversation with Frazer Anderson."""
URL = "https://theinnermostloop.substack.com/p/a-conversation-with-frazer-anderson"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-01", "slug": "feature-conversation-anderson",
        "title": "A Conversation with Frazer Anderson", "url": URL,
        "thesis": "Realpolitik becomes realspacepolitik, which adds a dimension.",
        "body": """
# A Conversation with Frazer Anderson

Two clichés first: GPUs are the new oil, and the world is dividing into spheres
with independent tech stacks. Then the less obvious claim — the Dyson Swarm is
happening, there is too much momentum behind diverting intelligence
infrastructure to orbit, and so the realpolitik of compute becomes
*realspacepolitik*.

Which adds literally a whole new dimension to it.
""",
    },
    "people": [
        {"id": "frazer-anderson", "type": "Person", "title": "Frazer Anderson",
         "body": "Managing director at Link Ventures."},
    ],
    "themes": [
        {"id": "realspacepolitik", "type": "Theme",
         "title": "Compute geopolitics acquires an altitude axis",
         "first_seen": "2026-03-01", "domain": "space",
         "body": "If the physical layer of intelligence moves to orbit, the "
                 "competition between spheres of influence stops being about "
                 "territory on a surface and gains a vertical dimension that no "
                 "existing framework of borders addresses."},
        {"id": "gpu-diplomacy", "type": "Theme",
         "title": "Statecraft conducted in compute",
         "first_seen": "2026-03-01", "domain": "policy",
         "body": "Compute is not evenly distributed across the Earth's surface, so "
                 "allocating it becomes an instrument of foreign policy in the way "
                 "energy and arms once were."},
    ],
    "developments": [
        {"id": "2026-03-01-gpu-diplomacy-becomes-a-portfolio",
         "title": "A State Department official is described as working on GPU diplomacy",
         "claim": "Wissner-Gross described a conversation with a US Under Secretary of State "
                  "working on what he called GPU diplomacy, in an era when compute is very much "
                  "not evenly distributed around the Earth's surface.",
         "domain": "policy", "actor": ["state-department", "people/frazer-anderson"],
         "evidences": ["gpu-diplomacy", "silicon-curtain", "politics-as-infrastructure"]},
        {"id": "2026-03-01-realpolitik-becomes-realspacepolitik",
         "title": "Compute geopolitics is projected to acquire a vertical dimension",
         "claim": "Setting aside the clichés that GPUs are the new oil and the world is dividing "
                  "into spheres with independent tech stacks, Wissner-Gross argued the Dyson "
                  "Swarm is going to happen — there is too much momentum behind diverting "
                  "intelligence infrastructure to space — so realpolitik becomes "
                  "realspacepolitik, adding literally a whole new dimension.",
         "domain": "space", "actor": ["people/frazer-anderson"],
         "evidences": ["realspacepolitik", "orbit-as-compute", "gpu-diplomacy"],
         "supersedes": [B + "developments/2026-03-01-gpu-diplomacy-becomes-a-portfolio"]},
    ],
}
