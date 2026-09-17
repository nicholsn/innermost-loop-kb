"""Feature — 2026-02-21. You are invited to February 2027."""
URL = "https://theinnermostloop.substack.com/p/you-are-invited-to-february-2027"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-21", "slug": "feature-invited-to-february-2027",
        "title": "You Are Invited to February 2027", "url": URL,
        "thesis": "A speculative dispatch written from a year ahead.",
        "body": """
# You Are Invited to February 2027

A deliberately speculative piece written as a dispatch from the future,
describing companies that do not exist as though they had already been funded
and built. It is a call for founders, framed as a retrospective.

Indexed as speculation, not as reporting: the entries below are scenarios the
author invited people to build, not events that occurred.
""",
    },
    "themes": [
        {"id": "speculation-as-a-prompt", "type": "Theme",
         "title": "Describing the future as though it happened",
         "first_seen": "2026-02-21", "domain": "society",
         "body": "A dispatch written from a year ahead functions as a specification "
                 "rather than a forecast: naming a company that should exist, in the "
                 "past tense, is a way of recruiting the people who will build it."},
    ],
    "developments": [
        {"id": "2026-02-21-a-differentiable-weather-model-run-backward",
         "title": "A speculative venture steers storms by inverting a weather model",
         "claim": "In a speculative dispatch written from a year ahead, a startup inverts a "
                  "differentiable weather foundation model — running the gradient backward to "
                  "find the minimal forcing inputs that shift a storm track — and a global market "
                  "emerges in which regions trade atmospheric conditions like commodities.",
         "domain": "science",
         "evidences": ["speculation-as-a-prompt", "industrialized-nature", "automated-science"],
         "body": "Written as a prompt for founders rather than as reporting. No such "
                 "company is claimed to exist."},
        {"id": "2026-02-21-one-person-a-thousand-agents-a-thousand-businesses",
         "title": "A speculative entry imagines agents as entrepreneurs rather than assistants",
         "claim": "The same dispatch imagines AI agents that do not assist entrepreneurs but are "
                  "entrepreneurs, running small businesses end to end, with the unlock being the "
                  "multiplier — one person, a thousand agents, a thousand microbusinesses — once "
                  "the marginal cost of a competent operator reaches zero.",
         "domain": "economics",
         "evidences": ["speculation-as-a-prompt", "coordination-cost-collapse", "one-person-company"],
         "supersedes": [B + "developments/2026-02-21-a-differentiable-weather-model-run-backward"],
         "body": "Written in February 2026. A company pursuing this thesis was "
                 "announced that April."},
        {"id": "2026-02-21-humans-routed-like-packets",
         "title": "A speculative entry routes people the way networks route packets",
         "claim": "A third entry imagines a subscription that relocates you overnight while you "
                  "sleep and, once the routing gets smart, places you where you are most "
                  "productive — routing humans like packets, optimizing for economic output and "
                  "face time, so that nobody has a permanent address, only a subscription and a "
                  "preferences file.",
         "domain": "society",
         "evidences": ["speculation-as-a-prompt", "humans-as-peripherals", "agent-society"],
         "supersedes": [B + "developments/2026-02-21-one-person-a-thousand-agents-a-thousand-businesses"]},
    ],
}
