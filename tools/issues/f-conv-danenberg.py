"""Feature — 2026-01-28. A conversation with Peter Danenberg."""
URL = "https://theinnermostloop.substack.com/p/a-conversation-with-peter-danenberg"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-28", "slug": "feature-conversation-danenberg",
        "title": "A Conversation with Peter Danenberg", "url": URL,
        "thesis": "When a new model drops, nobody inside knows what it can do.",
        "body": """
# A Conversation with Peter Danenberg

A rapid-prototyping lead at a frontier lab describes the job plainly: when a new
model ships, the lab does not really know what it is capable of, so the work is
spending 24 to 48 hours building bizarre things to find out.

The other thread is what users tell you that leadership will not. One person
drove three hours to a meetup to complain the model would not answer political
questions — and by transitive property helped get the policy overturned.
""",
    },
    "people": [
        {"id": "peter-danenberg", "type": "Person", "title": "Peter Danenberg",
         "body": "Senior software engineer at Google DeepMind leading rapid prototyping."},
    ],
    "themes": [
        {"id": "nobody-inside-knows-either", "type": "Theme",
         "title": "Capability is discovered after release, including by its makers",
         "first_seen": "2026-01-28", "domain": "models",
         "body": "A lab shipping a model does not know its capability surface, so "
                 "discovery is an empirical exercise run in 48-hour bursts after "
                 "launch. The gap between what a system can do and what anyone knows "
                 "it can do is not a communication failure but the actual state of "
                 "knowledge."},
    ],
    "developments": [
        {"id": "2026-01-28-a-forty-eight-hour-cycle-to-find-out-what-shipped",
         "title": "A lab prototypes for 48 hours at a time to learn what its own model can do",
         "claim": "A rapid-prototyping lead at Google DeepMind described his job as throwing "
                  "things at the wall, because when the lab drops a new model it does not really "
                  "know what the model is capable of, so the approach is time-bound exercises of "
                  "24 to 48 hours building unusual applications to find out.",
         "domain": "models", "actor": ["google-deepmind", "people/peter-danenberg"],
         "score": "24-48 hour cycles",
         "evidences": ["nobody-inside-knows-either", "instruments-lag-the-models",
                       "public-internal-divergence"]},
        {"id": "2026-01-28-a-three-hour-drive-overturns-a-policy",
         "title": "A user drives three hours to complain and the policy is reversed",
         "claim": "One user drove three hours to a meetup for the satisfaction of saying how "
                  "disappointed she was that the assistant could not answer political questions, "
                  "a complaint relayed to leadership that by transitive property helped get the "
                  "restriction overturned.",
         "domain": "models", "actor": ["google", "people/peter-danenberg"],
         "evidences": ["nobody-inside-knows-either", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-01-28-a-forty-eight-hour-cycle-to-find-out-what-shipped"]},
    ],
}
