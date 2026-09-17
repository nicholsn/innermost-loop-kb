"""Feature — 2026-03-07. The first multi-behavior whole-brain emulation."""
URL = "https://theinnermostloop.substack.com/p/the-first-multi-behavior-brain-upload"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-07", "slug": "feature-multi-behavior-brain-upload",
        "title": "The First Multi-Behavior Brain Upload", "url": URL,
        "thesis": "A copy of a biological brain drives a simulated body through multiple behaviors.",
        "body": """
# The First Multi-Behavior Brain Upload

A connectome-derived emulation of the entire adult fruit fly brain — 125,000
neurons, 50 million synapses — was coupled to a physics-simulated body, closing
the sensorimotor loop for the first time in a whole-brain emulation.

Prior work modelled brains without bodies or animated bodies without brains.
This is neither an animation nor a reinforcement-learning policy imitating
biology: it is a copy of a brain, wired from electron microscopy, making a body
move.
""",
    },
    "themes": [
        {"id": "emulation-closes-the-loop", "type": "Theme",
         "title": "A copied brain acts on a world",
         "first_seen": "2026-03-07", "domain": "biotech",
         "body": "Whole-brain emulation stops being a static map and becomes a "
                 "controller: sensory input in, connectome dynamics through, motor "
                 "output to a body that obeys physics. The remaining question for "
                 "larger brains becomes scale rather than kind."},
    ],
    "organizations": [
        {"id": "eon-systems", "type": "Organization", "title": "Eon Systems",
         "body": "Building connectome-derived whole-brain emulations, targeting a mouse brain."},
        {"id": "flywire", "type": "Organization", "title": "FlyWire",
         "body": "The fruit fly connectome project underlying the emulation."},
    ],
    "developments": [
        {"id": "2026-03-07-a-copied-brain-drives-a-simulated-body",
         "title": "A whole-brain emulation drives a physics-simulated body through multiple behaviors",
         "claim": "Eon Systems demonstrated what it believes is the first embodiment of a "
                  "whole-brain emulation producing multiple behaviors, integrating a "
                  "connectome-derived emulation of the adult fruit fly brain with a "
                  "physics-simulated body so that sensory input flows in, activity propagates "
                  "through the complete connectome, and motor commands drive a body that obeys "
                  "physics.",
         "domain": "biotech", "actor": ["eon-systems", "flywire"],
         "evidences": ["emulation-closes-the-loop", "architecture-of-mind", "resurrection-and-time"],
         "body": "Neither an animation nor a reinforcement-learning policy imitating "
                 "biology: a copy of a brain, wired neuron to neuron from electron "
                 "microscopy, making a body move."},
        {"id": "2026-03-07-a-hundred-twenty-five-thousand-neurons-at-ninety-five-percent",
         "title": "A whole-brain computational model predicted motor behavior at 95% accuracy",
         "claim": "The underlying model covers the entire adult Drosophila brain with more than "
                  "125,000 neurons and 50 million synaptic connections, built from a connectome "
                  "plus machine-learning predictions of neurotransmitter identity, and predicted "
                  "motor behavior at 95% accuracy — but was disembodied, with motor outputs that "
                  "had nowhere to go.",
         "domain": "biotech", "actor": ["eon-systems"], "score": "125,000 neurons / 95%",
         "evidences": ["emulation-closes-the-loop", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-03-07-a-copied-brain-drives-a-simulated-body"]},
        {"id": "2026-03-07-a-mouse-brain-is-five-hundred-sixty-times-larger",
         "title": "The stated next target is a brain 560 times larger",
         "claim": "Eon's stated mission is the world's largest connectome and highest-fidelity "
                  "brain emulation, targeting a complete digital emulation of a mouse brain at "
                  "roughly 70 million neurons — 560 times the fly's count — combining expansion "
                  "microscopy with tens of thousands of hours of calcium and voltage imaging.",
         "domain": "biotech", "actor": ["eon-systems"], "score": "70M neurons / 560x",
         "evidences": ["emulation-closes-the-loop", "hardware-grade-biology", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-03-07-a-hundred-twenty-five-thousand-neurons-at-ninety-five-percent"]},
    ],
}
