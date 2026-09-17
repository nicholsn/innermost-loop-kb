"""Issue 156 — 2026-07-05. Intelligence bends back to face itself."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-5-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-05", "title": "Welcome to July 5, 2026", "url": URL,
        "thesis": "A mind should learn to model itself to predict its next token.",
        "body": """
# Welcome to July 5, 2026

Jürgen Schmidhuber argues that the one constant across training and rollouts is
the model itself, so a mind should learn to model itself in order to better
predict its next token. Self-knowledge as a scaling objective.

Meanwhile a hobbyist reverse-engineered a commercial router into a
~10,000-parameter conductor that beat every model on MMLU by handing each
question to the right specialist.
""",
    },
    "themes": [
        {"id": "self-modeling-as-objective", "type": "Theme",
         "title": "Modeling the self to predict the world",
         "first_seen": "2026-07-05", "domain": "models",
         "body": "The argument that self-representation is not a side effect of scale "
                 "but the efficient move: since the model is the only constant across "
                 "every context it will ever see, modeling itself is the highest-"
                 "leverage compression available."},
    ],
    "organizations": [
        {"id": "fab2", "type": "Organization", "title": "Fab2",
         "body": "Formerly Atomic Semi; a fab that builds fabs."},
        {"id": "eso", "type": "Organization", "title": "European Southern Observatory"},
        {"id": "loma-linda", "type": "Organization", "title": "Loma Linda University"},
        {"id": "us-treasury-dept", "type": "Organization", "title": "US Treasury"},
        {"id": "forge-prep", "type": "Organization", "title": "Forge Prep"},
    ],
    "developments": [
        {"id": "2026-07-05-a-mind-should-model-itself",
         "title": "A pioneer argues a model should learn to model itself",
         "claim": "Jürgen Schmidhuber argued that the one constant across training and rollouts "
                  "is the model itself, so a mind should learn to model itself in order to better "
                  "predict its next token.",
         "domain": "models",
         "evidences": ["self-modeling-as-objective", "machine-introspection", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-06-19-models-trained-to-describe-themselves-faithfully"]},
        {"id": "2026-07-05-a-ten-thousand-parameter-conductor-beats-every-model",
         "title": "A 10,000-parameter router beats every model by picking specialists",
         "claim": "A hobbyist reverse-engineered Sakana's Fugu into tinyrouter, a roughly "
                  "10,000-parameter conductor that beat every individual model on MMLU by handing "
                  "each question to the right specialist.",
         "domain": "models", "actor": ["sakana-ai-lab"], "score": "~10k parameters",
         "evidences": ["monoculture-is-the-vulnerability", "routing-around-the-ban",
                       "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-07-05-a-mind-should-model-itself"]},
        {"id": "2026-07-05-a-constitution-as-a-legible-compass",
         "title": "A rival credits scale, long-horizon RL and a constitution",
         "claim": "Google's Andy Coenen credited Fable's strength to three ingredients — sheer "
                  "scale, relentless long-horizon agentic reinforcement learning, and a "
                  "constitution that turns thousands of decisions into one legible compass — "
                  "while practitioners reported that letting the model exercise judgement beats "
                  "dictating rules and conserves tokens.",
         "domain": "models", "actor": ["google", "anthropic"],
         "evidences": ["values-negotiated-with-the-model", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-06-25-labs-hire-philosophers-to-write-constitutions"]},
        {"id": "2026-07-05-machine-research-taste-is-narrower-than-human",
         "title": "A framework finds machine research ideas cluster where humans roam",
         "claim": "A new framework measuring how far machine research ideas drift from human "
                  "taste found that language models cluster around bridge-and-synthesis gaps "
                  "while humans roam wider.",
         "domain": "science",
         "evidences": ["discovery-as-process", "understanding-as-the-scarce-good",
                       "generalism-beats-specialism"],
         "supersedes": [B + "developments/2026-07-02-math-risks-being-declared-solved"]},
        {"id": "2026-07-05-four-superconductors-from-twenty-eight-gpu-hours",
         "title": "A screen of 2.4 million crystals surfaces four verified superconductors",
         "claim": "Alibaba's Elements Claw screened 2.4 million crystals in 28 GPU-hours and "
                  "surfaced four verified superconductors.",
         "domain": "science", "actor": ["alibaba"], "score": "2.4M crystals / 28 GPU-hours",
         "evidences": ["automated-science", "compiling-matter", "proof-priced-per-unit"],
         "supersedes": [B + "developments/2026-07-03-a-tumor-attacked-in-both-compartments"]},
        {"id": "2026-07-05-accountability-as-the-only-value-left",
         "title": "A builder says sub-agent management left accountability as the only human value",
         "claim": "One builder declared that Fable managing sub-agents made hand-coding "
                  "worthless, leaving accountability as the only value left in human hands, as "
                  "Amazon wound down Mechanical Turk, the 2005 marketplace that survived by "
                  "labeling AI's training data.",
         "domain": "agents", "actor": ["anthropic", "amazon"],
         "evidences": ["engineer-as-supervisor", "work-displaced", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-07-04-models-become-entities-not-genies"],
         "body": "The marketplace built to supply human microtasks to machines closes "
                 "in the same week that machines are said to have absorbed the last "
                 "task worth doing."},
        {"id": "2026-07-05-a-fab-that-builds-fabs",
         "title": "A startup reorganizes itself as a fab that builds fabs",
         "claim": "Sam Zeloof renamed Atomic Semi to Fab2, a fab fab spanning an Austin chip "
                  "fab, a Lockhart fab fab and a San Francisco garage, all wired to a browser "
                  "design tool, while ETH Zurich floated a single trapped ion to map chip fields "
                  "in three dimensions down to 10 nanovolts per meter.",
         "domain": "compute", "actor": ["fab2", "eth-zurich"], "score": "10 nV/m",
         "evidences": ["garage-scale-discovery", "physical-recursion", "vertical-silicon"],
         "supersedes": [B + "developments/2026-07-04-buying-compute-becomes-becoming-compute"]},
        {"id": "2026-07-05-heads-of-state-court-ceos-personally",
         "title": "Heads of state personally court chip and cloud investment",
         "claim": "Macron and Modi personally courted chief executives, landing €75 billion from "
                  "SoftBank for France and a record $48 billion from Amazon for India.",
         "domain": "policy", "actor": ["softbank", "amazon"], "score": "€75B / $48B",
         "evidences": ["politics-as-infrastructure", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-07-01-exports-top-a-hundred-billion-in-a-month"]},
        {"id": "2026-07-05-a-cap-proposed-on-orbital-constellations",
         "title": "Astronomers urge a cap of 100,000 satellites",
         "claim": "An ESO study warned that 1.7 million proposed satellites, including orbital "
                  "data centers and sunlight mirrors, could blind astronomy, urging a cap of "
                  "100,000.",
         "domain": "space", "actor": ["eso"], "score": "1.7M proposed vs 100,000 cap",
         "evidences": ["orbit-as-compute", "infrastructure-crowding-out", "industrialized-nature"],
         "supersedes": [B + "developments/2026-07-02-the-largest-digital-camera-starts-its-survey"]},
        {"id": "2026-07-05-a-hundred-fifty-eight-alzheimers-drugs-in-trials",
         "title": "An annual pipeline report counts 158 Alzheimer's drugs across 192 trials",
         "claim": "An annual pipeline report counted 158 Alzheimer's drugs across 192 trials, "
                  "revealing a decade-long pivot from amyloid toward inflammation and immunity, "
                  "while a Loma Linda study linked a five-eggs-a-week diet to a 27% lower risk.",
         "domain": "biotech", "actor": ["loma-linda"], "score": "158 drugs / 192 trials",
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-07-03-the-us-death-rate-hits-a-record-low"]},
        {"id": "2026-07-05-a-name-returned-to-a-1780-grave",
         "title": "Triple-DNA forensics gives a name back to a Continental soldier",
         "claim": "Triple-DNA forensics gave a name back to a Continental soldier in a shallow "
                  "1780 grave, John Pumphrey, who enlisted at thirteen, while researchers found "
                  "the hobbits of Flores ate what the dragons left behind and never mastered "
                  "fire.",
         "domain": "science",
         "evidences": ["resurrection-and-time", "automated-science"],
         "supersedes": [B + "developments/2026-06-26-a-scroll-sealed-since-79-ad-is-read-end-to-end"]},
        {"id": "2026-07-05-every-child-seeded-with-a-thousand-dollar-stake",
         "title": "A treasury seeds every eligible child with a $1,000 market stake",
         "claim": "The Treasury launched 530A accounts, an early move toward universal basic "
                  "equity that seeds every eligible child with a $1,000 stake in capital markets "
                  "rather than a cash handout.",
         "domain": "economics", "actor": ["us-treasury-dept"], "score": "$1,000 per child",
         "evidences": ["ai-as-the-economy", "politics-as-infrastructure", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-07-02-a-five-percent-stake-floated-to-washington"]},
    ],
}
