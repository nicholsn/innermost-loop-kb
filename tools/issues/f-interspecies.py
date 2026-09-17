"""Feature — 2026-05-23. The first consumer-scale interspecies foundation model."""
URL = "https://theinnermostloop.substack.com/p/the-first-consumer-scale-interspecies"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-23", "slug": "feature-interspecies-foundation-model",
        "title": "The First Consumer-Scale Interspecies Foundation Model", "url": URL,
        "thesis": "AI progressed in the order things were written down.",
        "body": """
# The First Consumer-Scale Interspecies Foundation Model

Everything AI has learned came with a record already written. Text, code,
protein, images — humans had documented each domain and the machine only had to
read. Non-human cognition is the first frontier where no record exists, because
no other species wrote one.

Synthetic data cannot help: it interpolates distributions a model has already
seen, and no model has seen what another species means. The data have to be
measured into existence.
""",
    },
    "themes": [
        {"id": "the-unwritten-frontier", "type": "Theme",
         "title": "The first domain with no written record",
         "first_seen": "2026-05-23", "domain": "science",
         "body": "AI advanced in the order things were written down. Where no record "
                 "exists, synthetic data cannot substitute, because it only "
                 "interpolates what has already been seen. The corpus has to be "
                 "measured into existence by an instrument in the world."},
        {"id": "sensors-that-label-themselves", "type": "Theme",
         "title": "Multiple channels annotate one another",
         "first_seen": "2026-05-23", "domain": "science",
         "body": "When a camera frames the bowl, the motion channel logs the lunge "
                 "and the microphone the bark, three readings label one another with "
                 "no annotator in the loop. The labeling bottleneck dissolves into "
                 "the instrument design."},
    ],
    "organizations": [
        {"id": "sarama", "type": "Organization", "title": "Sarama",
         "body": "Interspecies foundation model lab, beginning with a dog collar."},
    ],
    "developments": [
        {"id": "2026-05-23-the-first-frontier-with-no-written-record",
         "title": "Non-human cognition is the first domain where the corpus must be created",
         "claim": "Sarama announced the first consumer-scale interspecies foundation model, "
                  "beginning with a dog collar, on the argument that non-human animal cognition "
                  "is the first frontier where the record does not exist because no other species "
                  "wrote one down, that meaning lives not in the signal but in what reliably "
                  "happens around it, and that synthetic data cannot help because no model has "
                  "seen what another species means.",
         "domain": "science", "actor": ["sarama"],
         "evidences": ["the-unwritten-frontier", "data-beyond-text", "biosphere-uplift"]},
        {"id": "2026-05-23-a-separate-model-of-each-animal",
         "title": "A universal dictionary fails because meaning is individual",
         "claim": "A universal bark dictionary fails for the same reason a universal human "
                  "dictionary would, since meaning is individual, so the approach builds a "
                  "separate model of each dog trained on that dog's own life, reaching the home "
                  "as an augmented-reality overlay and a first-person collar view.",
         "domain": "science", "actor": ["sarama"],
         "evidences": ["the-unwritten-frontier", "authoring-minds", "intimate-interface"],
         "supersedes": [B + "developments/2026-05-23-the-first-frontier-with-no-written-record"]},
        {"id": "2026-05-23-three-readings-labeling-one-another",
         "title": "Sensors label themselves with no annotator in the loop",
         "claim": "The collar carries a camera, microphone and motion sensors transmitting "
                  "feature vectors rather than raw audio or video, and the sensors label "
                  "themselves — when the camera frames the food bowl, the motion channel logs the "
                  "lunge and the microphone the bark, three readings labeling one another — "
                  "already the largest record of its kind and heading toward a million annotated "
                  "bark sequences.",
         "domain": "science", "actor": ["sarama"], "score": "1M sequences targeted",
         "evidences": ["sensors-that-label-themselves", "the-unwritten-frontier", "data-beyond-text"],
         "supersedes": [B + "developments/2026-05-23-a-separate-model-of-each-animal"]},
        {"id": "2026-05-23-a-model-catches-what-an-animal-evolved-to-hide",
         "title": "Continuous listening catches pain that an animal instinctively masks",
         "claim": "Dogs mask pain by instinct so illness goes unseen for weeks, and a model "
                  "watching continuously catches early what a dog evolved to hide, with the "
                  "collar reported at roughly 93% accuracy on emotion and intent and able to "
                  "identify individuals by voice.",
         "domain": "biotech", "actor": ["sarama"], "score": "~93% accuracy",
         "evidences": ["sensors-that-label-themselves", "biosphere-uplift", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-23-three-readings-labeling-one-another"],
         "body": "Figures are company-reported."},
        {"id": "2026-05-23-the-mind-that-already-solved-alignment-with-us",
         "title": "The animal on the other end co-evolved to read human intent",
         "claim": "The mind on the other end of the collar is the one intelligence that has "
                  "already solved alignment with us, co-evolved over tens of thousands of years "
                  "to read human emotion and intent more closely than any other animal, as law "
                  "shifts from property toward personhood with jurisdictions weighing a companion "
                  "animal's best interest.",
         "domain": "society", "actor": ["sarama", "nonhuman-rights"],
         "evidences": ["the-unwritten-frontier", "model-welfare", "agent-society"],
         "supersedes": [B + "developments/2026-05-23-a-model-catches-what-an-animal-evolved-to-hide"]},
    ],
}
