"""Feature — 2026-02-14. Solve Everything."""
URL = "https://theinnermostloop.substack.com/p/solve-everything"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-14", "slug": "feature-solve-everything",
        "title": "Solve Everything", "url": URL,
        "thesis": "Superintelligence is no longer a question of if, but of where we point it.",
        "body": """
# Solve Everything

A book-length blueprint for aiming the Singularity at every problem that has
made human life short, expensive or unfair. Its central claim is that the
Intelligence Revolution is a war on the final bottleneck — scarce expert
attention — and its weapon is artificial cognition collapsing toward the cost of
electricity.

The obstacle is named as The Muddle: bureaucracy, input-based pricing and
scarcity-minded institutions. The essay is structured as a race between the
Rails and the Muddle, with roughly eighteen months before path dependencies
harden.
""",
    },
    "themes": [
        {"id": "scarce-expert-attention", "type": "Theme",
         "title": "The final bottleneck is expert attention",
         "first_seen": "2026-02-14", "domain": "economics",
         "body": "Every domain that stays expensive is gated on a small number of "
                 "people who understand it. Collapsing the cost of expert cognition "
                 "toward the cost of electricity is the single intervention that "
                 "reaches all of them at once."},
        {"id": "targeting-systems-not-leaderboards", "type": "Theme",
         "title": "Measurement that creates the future rather than records it",
         "first_seen": "2026-02-14", "domain": "benchmarks",
         "body": "A leaderboard looks backward to record who is winning. A targeting "
                 "system looks forward: make the measurement legible, adversarial "
                 "and payable, and capital and cognition route themselves to clear "
                 "the target without being directed."},
        {"id": "the-muddle", "type": "Theme",
         "title": "The institutional layer that absorbs the gains",
         "first_seen": "2026-02-14", "domain": "policy",
         "body": "Bureaucracy, input-based pricing and scarcity-minded institutions "
                 "constitute the real obstacle, not the technology. The risk is not "
                 "that capability fails but that it is captured by ad optimization "
                 "and grant theater."},
    ],
    "developments": [
        {"id": "2026-02-14-a-war-on-scarce-expert-attention",
         "title": "A blueprint argues the Intelligence Revolution targets one bottleneck",
         "claim": "Peter Diamandis and Alex Wissner-Gross released Solve Everything: Achieving "
                  "Abundance by 2035, arguing superintelligence is no longer a question of if but "
                  "of where we point it, that the Intelligence Revolution is a war on the final "
                  "bottleneck of scarce expert attention, and that its weapon is artificial "
                  "cognition collapsing toward the cost of electricity.",
         "domain": "economics",
         "evidences": ["scarce-expert-attention", "price-implosion", "physics-is-the-first-domino"]},
        {"id": "2026-02-14-a-nine-layer-stack-and-a-six-stage-curve",
         "title": "A framework converts messy domains into problems compute can be poured into",
         "claim": "The blueprint introduces an Industrial Intelligence Stack, a nine-layer "
                  "framework for converting any messy real-world domain into a system solvable by "
                  "pouring compute into it, and a six-stage maturation curve from The Muddle, "
                  "where nobody agrees on the rules, to Solved, where a service is as boring and "
                  "reliable as tap water.",
         "domain": "economics",
         "evidences": ["scarce-expert-attention", "the-muddle", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-02-14-a-war-on-scarce-expert-attention"]},
        {"id": "2026-02-14-targeting-systems-rather-than-leaderboards",
         "title": "A distinction between measurement that records and measurement that creates",
         "claim": "The engine of the framework is a Targeting System, distinguished sharply from "
                  "a leaderboard: where old benchmarks looked backward to record who was winning, "
                  "a targeting system looks forward, and making the measurement legible, "
                  "adversarial and payable routes capital and cognition to clear it "
                  "automatically, producing an abundance flywheel.",
         "domain": "benchmarks",
         "evidences": ["targeting-systems-not-leaderboards", "benchmark-saturation", "scarce-expert-attention"],
         "supersedes": [B + "developments/2026-02-14-a-nine-layer-stack-and-a-six-stage-curve"]},
        {"id": "2026-02-14-a-solution-wavefront-in-three-phases",
         "title": "A schedule for what gets solved and when, in three phases to 2035",
         "claim": "The blueprint lays out a solution wavefront in three phases: pure information "
                  "through 2027 as mathematics, code and physics become formal verification "
                  "utilities; the physical world from 2028 to 2031 as chemistry, materials and "
                  "biology capitulate once the virtual cell comes online; and planetary-scale "
                  "systems from 2032 to 2035 as energy, climate, food and infrastructure are "
                  "industrialized into dial-tone-reliable utilities.",
         "domain": "science", "score": "three phases to 2035",
         "evidences": ["physics-is-the-first-domino", "scarce-expert-attention", "biology-as-compile-target"],
         "supersedes": [B + "developments/2026-02-14-targeting-systems-rather-than-leaderboards"]},
        {"id": "2026-02-14-fifteen-moonshots-with-spillover",
         "title": "Fifteen moonshots each with benchmarks, dates, guardrails and a spillover theory",
         "claim": "The operational heart is fifteen moonshots grouped into human needs, the "
                  "frontier of mind, the planetary substrate and the frontier of physics, from "
                  "manufacturing organs on demand — treating transplant waitlists as an inventory "
                  "management error — to doubling healthy lifespan, demonstrating mind uploading "
                  "and decoding interspecies communication, each with a theory of spillover.",
         "domain": "science", "score": "15 moonshots",
         "evidences": ["the-shaped-charge-model", "scarce-expert-attention", "longevity-escape-velocity"],
         "supersedes": [B + "developments/2026-02-14-a-solution-wavefront-in-three-phases"]},
        {"id": "2026-02-14-a-race-between-the-rails-and-the-muddle",
         "title": "The obstacle is named as institutions, with three paths branching from one fork",
         "claim": "The blueprint frames the obstacle as The Muddle — entrenched bureaucracy, "
                  "input-based pricing and scarcity-minded institutions — structured as a race "
                  "between the Rails and the Muddle with roughly eighteen months of regulatory "
                  "foundry window before path dependencies harden, branching into a bright path "
                  "of abundance by 2035, a muddle path where AI is captured by ad optimization "
                  "and grant theater, and a dark path where a safety incident freezes progress.",
         "domain": "policy", "score": "~18-month window",
         "evidences": ["the-muddle", "politics-as-infrastructure", "the-verifiable-pause"],
         "supersedes": [B + "developments/2026-02-14-fifteen-moonshots-with-spillover"]},
    ],
}
