"""Feature — 2026-03-14. A conversation with Mustafa Suleyman."""
URL = "https://theinnermostloop.substack.com/p/a-conversation-with-mustafa-suleyman"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-14", "slug": "feature-conversation-suleyman",
        "title": "A Conversation with Mustafa Suleyman", "url": URL,
        "thesis": "Measure the economy the way the economy measures itself: in dollars.",
        "body": """
# A Conversation with Mustafa Suleyman

The Modern Turing Test proposed a different kind of benchmark: rather than
academic tests, measure what a system can do in the economy — which model turns
$100,000 of starting capital into a million dollars.

Both participants note the older threshold passed without ceremony. There was no
Kasparov-Deep Blue moment for the Turing Test, because in a world of compounding
exponentials people desensitize to tenfold changes.
""",
    },
    "people": [
        {"id": "mustafa-suleyman", "type": "Person", "title": "Mustafa Suleyman",
         "body": "Chief executive of Microsoft AI; proposed the Modern Turing Test."},
    ],
    "themes": [
        {"id": "the-modern-turing-test", "type": "Theme",
         "title": "Benchmark capability in dollars, not in exams",
         "first_seen": "2026-03-14", "domain": "benchmarks",
         "body": "If the question is what a system can do in the workplace, the "
                 "measure should be the one the economy already uses. A model turning "
                 "seed capital into a tenfold return is a capability claim no "
                 "academic benchmark can substitute for."},
        {"id": "desensitized-to-tenfold", "type": "Theme",
         "title": "Compounding exponentials erase the sense of occasion",
         "first_seen": "2026-03-14", "domain": "society",
         "body": "In a field where order-of-magnitude changes arrive annually, each "
                 "one lands as routine. The absence of celebration around a passed "
                 "threshold is not denial but adaptation — and it means the record "
                 "of what happened has to be reconstructed after the fact."},
    ],
    "developments": [
        {"id": "2026-03-14-which-model-turns-a-hundred-thousand-into-a-million",
         "title": "A benchmark proposal measures capability in dollars rather than exams",
         "claim": "Mustafa Suleyman described the Modern Turing Test he proposed in 2022: rather "
                  "than academic benchmarks, measure what a system can do in the economy, since "
                  "we measure the economy in dollars and cents — asking which model would be "
                  "first to turn $100,000 of starting capital into a million.",
         "domain": "benchmarks", "actor": ["people/mustafa-suleyman", "microsoft"],
         "score": "$100,000 to $1M",
         "evidences": ["the-modern-turing-test", "targeting-systems-not-leaderboards",
                       "agent-economy"]},
        {"id": "2026-03-14-a-prediction-from-recognition-to-generation-to-action",
         "title": "A 2022 prediction traced the path from recognition to autonomous action",
         "claim": "The proposal rested on a simple prediction: if scaling laws continued with an "
                  "order of magnitude more compute each year, the field would move from "
                  "recognition through generation to perfect generation at every time step, which "
                  "in sequence produces assistive agentive actions resembling a knowledge worker, "
                  "project manager or founder.",
         "domain": "models", "actor": ["people/mustafa-suleyman"],
         "evidences": ["the-modern-turing-test", "agent-economy", "takeoff-declared"],
         "supersedes": [B + "developments/2026-03-14-which-model-turns-a-hundred-thousand-into-a-million"]},
        {"id": "2026-03-14-where-was-the-kasparov-moment",
         "title": "Two participants note a threshold passed with no ceremony at all",
         "claim": "Both participants observed that the Turing Test has been passed with no "
                  "AlphaGo moment and nobody celebrating — the relevant prize having wound down "
                  "beforehand — which Suleyman attributed to a world of compounding exponentials "
                  "where people become desensitized to tenfold changes, so much so that the "
                  "reaction to progress becomes asking why it has not happened yet.",
         "domain": "society", "actor": ["people/mustafa-suleyman"],
         "evidences": ["desensitized-to-tenfold", "thresholds-pass-unremarked", "normalcy-overhang"],
         "supersedes": [B + "developments/2026-03-14-a-prediction-from-recognition-to-generation-to-action"]},
    ],
}
