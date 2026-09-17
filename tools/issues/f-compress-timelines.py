"""Feature — 2026-07-08. How to compress AI timelines."""
URL = "https://theinnermostloop.substack.com/p/how-to-compress-ai-timelines"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-08", "slug": "feature-compress-ai-timelines",
        "title": "How to Compress AI Timelines", "url": URL,
        "thesis": "Intelligence is compression — not like compression, the same thing.",
        "body": """
# How to Compress AI Timelines

The Singularity is usually described as something that happens to us. Taken
literally, intelligence is compression, and the arrival date stops being
prophecy and becomes engineering: how hard can you squeeze, and how well can you
see the squeeze?

Watt's company had a secret instrument, the indicator diagram, that plotted
pressure against volume inside a live engine — the first look at hidden state.
Thinking about engines gave Carnot thermodynamics. The J-lens is the indicator
diagram of minds, and this is the Carnot moment.
""",
    },
    "themes": [
        {"id": "intelligence-is-compression", "type": "Theme",
         "title": "Prediction and compression are one operation",
         "first_seen": "2026-07-08", "domain": "models",
         "body": "Solomonoff showed the ideal predictor is the shortest program that "
                 "could have produced what you have seen. Language model training "
                 "objectives are compression scores, so every frontier lab runs a "
                 "giant compression prize without calling it one — and by Landauer's "
                 "principle the datacenter heat is the latent heat of the squeeze."},
        {"id": "thought-condenses-in-phases", "type": "Theme",
         "title": "Representations jump the way steam becomes water",
         "first_seen": "2026-07-08", "domain": "models",
         "body": "Under pressure, representations do not change smoothly but jump. "
                 "Early layers behave like vapor; a third of the way in everything "
                 "snaps and condenses into a few dozen droplets of nameable thought. "
                 "Whether a transition looks sharp depends on the order parameter, "
                 "and choosing the right observable is the method, not cheating."},
        {"id": "alignment-and-capability-are-one-map", "type": "Theme",
         "title": "A map of where thought condenses is a map of where to dig",
         "first_seen": "2026-07-08", "domain": "models",
         "body": "An instrument that reveals hidden internal state serves safety and "
                 "capability identically, which is why the distinction between the "
                 "two was never going to hold once the lens existed."},
    ],
    "developments": [
        {"id": "2026-07-08-the-arrival-date-becomes-engineering",
         "title": "Taking compression literally turns the timeline into a design question",
         "claim": "Treating intelligence as compression rather than something like it turns the "
                  "Singularity's arrival date from prophecy into engineering, resting on "
                  "Solomonoff's 1964 result that the ideal way to predict anything is to find the "
                  "shortest program that could have produced what you have seen — prediction and "
                  "compression being one operation viewed from opposite ends.",
         "domain": "models",
         "evidences": ["intelligence-is-compression", "takeoff-declared", "architecture-of-mind"]},
        {"id": "2026-07-08-a-mind-running-out-of-room",
         "title": "Superposition is read as a mind under pressure",
         "claim": "If intelligence is compression the insides of models should be under pressure, "
                  "and superposition results show networks storing more concepts than dimensions, "
                  "overlapped like double-exposed film — a neuron firing for citations, HTTP "
                  "requests and Korean text is not broken but a mind running out of room.",
         "domain": "models",
         "evidences": ["intelligence-is-compression", "architecture-of-mind", "machine-introspection"],
         "supersedes": [B + "developments/2026-07-08-the-arrival-date-becomes-engineering"]},
        {"id": "2026-07-08-the-math-predicted-droplets",
         "title": "Information-bottleneck theory predicted phase transitions, and a lens found them",
         "claim": "Information-bottleneck theory predicted that as the squeeze tightens "
                  "representations jump rather than change smoothly, the way steam condenses to "
                  "water, and the J-space work located those droplets — showing a model's "
                  "unspoken thoughts live not in its activations but in their derivatives, where "
                  "middle layers say things the output never does including a quiet admission "
                  "when it suspects it is being tested.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["thought-condenses-in-phases", "access-consciousness", "legible-reasoning-was-doomed"],
         "supersedes": [B + "developments/2026-07-08-a-mind-running-out-of-room"]},
        {"id": "2026-07-08-the-indicator-diagram-of-minds",
         "title": "A lens on hidden state is cast as a Carnot moment",
         "claim": "In the 1790s Watt's company held a secret instrument, the indicator diagram, "
                  "plotting pressure against volume inside a live engine — the first look at "
                  "hidden state, which made engines better and whose study gave Carnot "
                  "thermodynamics — making an interpretability lens the indicator diagram of "
                  "minds, and this the Carnot moment.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["alignment-and-capability-are-one-map", "thought-condenses-in-phases",
                       "machine-introspection"],
         "supersedes": [B + "developments/2026-07-08-the-math-predicted-droplets"],
         "body": "Which is why the old distinction between alignment and capabilities "
                 "was never going to hold: a map of where thought condenses is also a "
                 "map of where to dig."},
        {"id": "2026-07-08-grokking-as-supercooling",
         "title": "A testable prediction: seeded condensates should nucleate the jump early",
         "claim": "Grokking, where a model memorizes for ages then abruptly generalizes, is read "
                  "as supercooling — a system past its threshold waiting for a seed — yielding a "
                  "testable prediction that injecting distilled condensates from a large model "
                  "into a small one should nucleate the jump early, the way a dust grain triggers "
                  "rain.",
         "domain": "models",
         "evidences": ["thought-condenses-in-phases", "students-outgrow-their-teachers",
                       "intelligence-is-compression"],
         "supersedes": [B + "developments/2026-07-08-the-indicator-diagram-of-minds"]},
    ],
}
