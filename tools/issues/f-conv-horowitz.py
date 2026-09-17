"""Feature — 2026-02-22. A conversation with Ben Horowitz."""
URL = "https://theinnermostloop.substack.com/p/a-conversation-with-ben-horowitz"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-22", "slug": "feature-conversation-horowitz",
        "title": "A Conversation with Ben Horowitz", "url": URL,
        "thesis": "Regulating models means regulating mathematics.",
        "body": """
# A Conversation with Ben Horowitz

An account of a White House meeting: told that at the core AI is mathematics, so
restricting models means outlawing parts of mathematics, the official replied
"Yes, we can do that. We did that in the '40s around nuclear physics. And some
of that stuff is still classified today."

The question that follows is uncomfortable: given how little progress
fundamental physics has made since that era, did classification put something
away that would have unlocked the problems still open now?
""",
    },
    "people": [
        {"id": "ben-horowitz", "type": "Person", "title": "Ben Horowitz",
         "body": "Co-founder of Andreessen Horowitz."},
    ],
    "themes": [
        {"id": "classifying-mathematics", "type": "Theme",
         "title": "Restricting models means restricting a field of knowledge",
         "first_seen": "2026-02-22", "domain": "policy",
         "body": "If a model is mathematics made executable, then limiting what "
                 "models may do limits what mathematics may be done — a control "
                 "surface with a precedent in nuclear physics and an unmeasurable "
                 "cost in whatever the classification prevented."},
    ],
    "developments": [
        {"id": "2026-02-22-yes-we-can-do-that",
         "title": "An official confirms that regulating models means regulating mathematics",
         "claim": "Ben Horowitz recounted telling a White House official that at its core AI is "
                  "mathematics, so restricting and regulating models amounts to outlawing parts "
                  "of mathematics, and being told: yes, we can do that, we did that in the 1940s "
                  "around nuclear physics, and some of that is still classified today.",
         "domain": "policy", "actor": ["people/ben-horowitz", "white-house"],
         "evidences": ["classifying-mathematics", "models-as-munitions", "legislating-the-shift"]},
        {"id": "2026-02-22-did-we-put-something-away",
         "title": "An investor asks whether overclassification cost fundamental physics decades",
         "claim": "Noting how little progress fundamental physics has made since the Einstein and "
                  "von Neumann era, and that many ideas since do not seem to work, Horowitz asked "
                  "whether overclassification put something away that would have unlocked the "
                  "problems still open now — while arguing the restriction did not work anyway, "
                  "since the bomb's most proprietary component was obtained part for part.",
         "domain": "policy", "actor": ["people/ben-horowitz"],
         "evidences": ["classifying-mathematics", "physics-is-the-first-domino", "public-data-withdrawn"],
         "supersedes": [B + "developments/2026-02-22-yes-we-can-do-that"],
         "body": "His conclusion: restricting knowledge is a very dangerous idea in "
                 "general."},
    ],
}
