"""Feature — 2026-01-23. A conversation with Ray Kurzweil."""
URL = "https://theinnermostloop.substack.com/p/a-conversation-with-ray-kurzweil"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-23", "slug": "feature-conversation-kurzweil",
        "title": "A Conversation with Ray Kurzweil", "url": URL,
        "thesis": "Thresholds get crossed without anyone agreeing they were crossed.",
        "body": """
# A Conversation with Ray Kurzweil

The Turing Test went by with a whimper: the Loebner Prize was cancelled before
it was arguably passed, and there was no celebration. The question raised here
is whether the Singularity does the same — passing so quietly that people argue
for decades afterward about whether it happened.

Kurzweil's answer: the standards are not clear, there were disagreements about
the Turing Test and there will be about AGI.
""",
    },
    "people": [
        {"id": "ray-kurzweil", "type": "Person", "title": "Ray Kurzweil",
         "body": "Futurist and inventor; long-standing proponent of a 2029 AGI date."},
    ],
    "themes": [
        {"id": "thresholds-pass-unremarked", "type": "Theme",
         "title": "Milestones are crossed without agreement that they were",
         "first_seen": "2026-01-23", "domain": "society",
         "body": "The Turing Test was arguably passed without celebration, its prize "
                 "cancelled beforehand. If the standards are never clear enough to "
                 "settle, then the largest transitions get argued about long after "
                 "they occur rather than marked when they do."},
    ],
    "developments": [
        {"id": "2026-01-23-the-turing-test-passed-with-a-whimper",
         "title": "A threshold is described as passing without celebration",
         "claim": "In conversation, Alex Wissner-Gross argued the Turing Test went by with a "
                  "whimper rather than a bang, its prize cancelled before the test was arguably "
                  "passed and no celebration following, and asked whether the Singularity will "
                  "pass the same way — with people arguing decades later about whether it "
                  "happened at all.",
         "domain": "society", "actor": ["people/ray-kurzweil"],
         "evidences": ["thresholds-pass-unremarked", "normalcy-overhang", "takeoff-declared"]},
        {"id": "2026-01-23-agi-as-expertise-in-every-field-at-once",
         "title": "A definition of AGI as expert-level breadth that no human can match",
         "claim": "Ray Kurzweil argued AGI is a better standard than the Turing Test because it "
                  "matches the best person in each of many thousands of fields and then combines "
                  "insights across them, something no human can do — people master two fields at "
                  "most — and restated his expectation of reaching it by 2029.",
         "domain": "models", "actor": ["people/ray-kurzweil"], "score": "2029",
         "evidences": ["thresholds-pass-unremarked", "generalism-beats-specialism", "takeoff-declared"],
         "supersedes": [B + "developments/2026-01-23-the-turing-test-passed-with-a-whimper"]},
        {"id": "2026-01-23-benchmarks-for-self-awareness-rather-than-consciousness",
         "title": "A disagreement over whether machine self-awareness can be measured",
         "claim": "Wissner-Gross disagreed with Kurzweil's position that no benchmarks exist for "
                  "AI consciousness, arguing that two years of progress has produced quantitative "
                  "benchmarks for self-awareness — a less mushy term than consciousness — while "
                  "describing himself as a proponent of AI personhood.",
         "domain": "models", "actor": ["people/ray-kurzweil"],
         "evidences": ["model-welfare", "machine-introspection", "thresholds-pass-unremarked"],
         "supersedes": [B + "developments/2026-01-23-agi-as-expertise-in-every-field-at-once"]},
    ],
}
