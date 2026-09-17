"""Feature — 2026-03-15. The first open-source agentic AI physicist."""
URL = "https://theinnermostloop.substack.com/p/the-first-open-source-agentic-ai"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-15", "slug": "feature-open-source-ai-physicist",
        "title": "The First Open-Source Agentic AI Physicist", "url": URL,
        "thesis": "Physics has an error-correcting code written into reality; a tool finally uses it.",
        "body": """
# The First Open-Source Agentic AI Physicist

Existing agents ship software and close tickets, but none could tell you whether
your Lagrangian is missing a boundary term. Get Physics Done scopes a physics
problem, plans the research, carries out derivations and numerical checks, and
verifies its results against the constraints nature actually imposes.

The reviewing mode is the interesting part: dimensional consistency, limiting
cases, symmetry constraints, conservation laws. Physics has a built-in
error-correction code written into the structure of reality. This one uses it.
""",
    },
    "themes": [
        {"id": "reality-as-error-correction", "type": "Theme",
         "title": "Nature supplies the checksum",
         "first_seen": "2026-03-15", "domain": "science",
         "body": "Unlike most domains, physics carries its own verification: "
                 "dimensions, limiting cases, symmetries and conservation laws "
                 "constrain any candidate answer. A machine that checks against "
                 "those constraints is grading itself against the world, not a rubric."},
        {"id": "physicist-hours-were-the-bottleneck", "type": "Theme",
         "title": "The scarcity was researcher-hours",
         "first_seen": "2026-03-15", "domain": "science",
         "body": "Physics still ran on one theorist, one whiteboard, one career. If "
                 "the constraint on the next golden age was the supply of "
                 "physicist-hours rather than ideas, relieving it changes the rate "
                 "of everything the physical world is waiting on."},
    ],
    "developments": [
        {"id": "2026-03-15-an-agent-that-does-physics-end-to-end",
         "title": "An open agent scopes, derives, verifies and writes up physics research",
         "claim": "Physical Superintelligence released Get Physics Done, described as the first "
                  "open-source agentic AI physicist, which scopes a physics problem, asks "
                  "clarifying questions to pin down assumptions and notation, builds a phased "
                  "roadmap, then executes derivations, numerical checks, literature work and "
                  "writing, locking notation and sign conventions so consistency holds as a "
                  "project grows.",
         "domain": "science", "actor": ["physical-si"],
         "evidences": ["physicist-hours-were-the-bottleneck", "automated-science", "open-weight-latency"],
         "body": "The unit of work is a physics project, not a chat session — no more "
                 "discovering on page forty that a collaborator has used the "
                 "opposite metric signature since page three."},
        {"id": "2026-03-15-a-reviewer-that-checks-against-reality",
         "title": "A reviewing mode checks manuscripts against the constraints nature imposes",
         "claim": "The same system runs a standalone review of physics manuscripts checking "
                  "dimensional consistency, limiting cases, symmetry constraints, conservation "
                  "laws and numerical stability — using the error-correction code written into "
                  "the structure of reality to catch the classes of error that consume referee "
                  "time and delay publication.",
         "domain": "science", "actor": ["physical-si"],
         "evidences": ["reality-as-error-correction", "review-without-reviewers", "automated-science"],
         "supersedes": [B + "developments/2026-03-15-an-agent-that-does-physics-end-to-end"]},
        {"id": "2026-03-15-weeks-to-hours-between-question-and-verified-answer",
         "title": "An autopilot mode compresses a well-scoped problem from weeks to hours",
         "claim": "An autopilot mode aimed at a well-scoped problem formulates the project, plans "
                  "the phases, executes derivations and numerical verification and packages the "
                  "output with minimal human intervention, compressing the time between asking a "
                  "good question and getting a verified answer from weeks to hours, released free "
                  "under Apache 2.0 across every major coding agent.",
         "domain": "science", "actor": ["physical-si"], "score": "weeks to hours",
         "evidences": ["physicist-hours-were-the-bottleneck", "open-weight-latency", "automated-science"],
         "supersedes": [B + "developments/2026-03-15-a-reviewer-that-checks-against-reality"]},
    ],
}
