"""Features — the six recorded conversations, Dec 2025 to Mar 2026."""
B = "https://nicholsn.github.io/innermost-loop-kb/"

# Each conversation is its own issue; this spec carries the shared people and
# themes and the Werner interview, with the rest emitted from sibling specs.
URL = "https://theinnermostloop.substack.com/p/a-conversation-with-john-werner"
SPEC = {
    "issue": {
        "date": "2026-02-04", "slug": "feature-conversation-werner",
        "title": "A Conversation with John Werner", "url": URL,
        "thesis": "The Singularity was an optical illusion, and we are in the foothills.",
        "body": """
# A Conversation with John Werner

A field report from the largest AI conference in the world. The most spoken
language in the hallways was Mandarin: American frontier labs have gone dark at
the top academic venues, leaving a vacuum that Chinese labs are visibly filling.

And a reframing worth keeping: a mountain looks like a point from a distance,
but up close there are foothills and a smooth gradient. The Singularity was an
optical illusion in the same way — and we are already in it.
""",
    },
    "people": [
        {"id": "john-werner", "type": "Person", "title": "John Werner",
         "body": "Founder of Imagination in Action; managing director at Link Ventures."},
    ],
    "themes": [
        {"id": "the-foothills-illusion", "type": "Theme",
         "title": "A threshold that is a gradient up close",
         "first_seen": "2026-02-04", "domain": "society",
         "body": "A mountain looks like a single point from far away and resolves into "
                 "foothills as you approach. If the Singularity has the same shape, "
                 "there is no moment to mark — only the recognition, late, that you "
                 "have been climbing for a while."},
        {"id": "the-labs-go-dark-at-conferences", "type": "Theme",
         "title": "A publication vacuum at the top venues",
         "first_seen": "2026-02-04", "domain": "models",
         "body": "When the leading labs stop publishing at academic conferences, the "
                 "record of the field stops reflecting the frontier — and whoever "
                 "keeps publishing inherits the appearance of leadership and the "
                 "pipeline of students that follows it."},
    ],
    "developments": [
        {"id": "2026-02-04-the-most-spoken-language-in-the-hallways",
         "title": "American labs go dark at the top conference and rivals fill the vacuum",
         "claim": "At the largest AI conference in the world, the most spoken language in the "
                  "hallways was Mandarin, with American frontier labs having largely gone dark at "
                  "top academic venues and Chinese labs visibly filling the vacuum — one firm "
                  "presenting more than 130 papers including a best paper award.",
         "domain": "models", "actor": ["alibaba"], "score": "130+ papers",
         "evidences": ["the-labs-go-dark-at-conferences", "dark-forest-research", "silicon-curtain"]},
        {"id": "2026-02-04-a-century-becomes-a-few-years",
         "title": "A philanthropy's disease timeline compresses from a century to a few years",
         "claim": "A major philanthropy founded with a mandate to cure all disease within a "
                  "century now describes the same goal in terms of a few years, with humanoid "
                  "robots widely perceived at the conference as the obvious next thing after "
                  "agents.",
         "domain": "biotech", "actor": ["czi"], "score": "a century to a few years",
         "evidences": ["longevity-escape-velocity", "takeoff-declared", "physical-recursion"],
         "supersedes": [B + "developments/2026-02-04-the-most-spoken-language-in-the-hallways"]},
        {"id": "2026-02-04-the-singularity-was-an-optical-illusion",
         "title": "A threshold is reframed as a gradient already underway",
         "claim": "Wissner-Gross argued the Singularity was an optical illusion in the sense that "
                  "a mountain appears as a point or vertical line from a distance but resolves "
                  "into foothills and a smooth gradient up close — and that by that reading we "
                  "are at least in the foothills already.",
         "domain": "society", "actor": ["people/john-werner"],
         "evidences": ["the-foothills-illusion", "normalcy-overhang", "thresholds-pass-unremarked"],
         "supersedes": [B + "developments/2026-02-04-a-century-becomes-a-few-years"]},
    ],
}
