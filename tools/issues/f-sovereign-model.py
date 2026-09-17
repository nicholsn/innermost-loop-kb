"""Feature — 2026-07-13. The first orbital sovereign AI model."""
URL = "https://theinnermostloop.substack.com/p/the-first-orbital-sovereign-ai-model"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-13", "slug": "feature-orbital-sovereign-model",
        "title": "The First Orbital Sovereign AI Model", "url": URL,
        "thesis": "Inference may be shared. Ownership cannot.",
        "body": """
# The First Orbital Sovereign AI Model

Augsburg ended a war of religion in 1555 with *cuius regio, eius religio* —
whose realm, his religion. The coming settlement runs *cuius regio, eius
intelligentia*: whose realm, his intelligence.

Banks do not lend out their ledgers; nations do not either. A sovereign model is
how an institution gains intelligence without the handover. The model goes to
orbit not for the compute but because the data cannot come down. Compute is
cheap to move. Sovereignty is not.
""",
    },
    "themes": [
        {"id": "whose-realm-his-intelligence", "type": "Theme",
         "title": "Sovereignty attaches to the model, not the territory",
         "first_seen": "2026-07-13", "domain": "policy",
         "body": "A ledger creates value only when a model can reason on it, but "
                 "reasoning on a shared model means entrusting the ledger to a mind "
                 "you do not own under someone else's law. What stays inside and "
                 "what is rented from the market of intelligence becomes the new "
                 "boundary of the firm and of the state."},
        {"id": "the-bifurcating-model-layer", "type": "Theme",
         "title": "A commons layer and a sovereign layer",
         "first_seen": "2026-07-13", "domain": "models",
         "body": "The field splits into vast shared generalists and small owned "
                 "specialists that retrieve from private data while consulting the "
                 "generalists. Sovereignty stops being a tax on capability once the "
                 "specialist can consult without disclosing."},
    ],
    "developments": [
        {"id": "2026-07-13-a-first-of-ownership-not-compute",
         "title": "A sovereign model flies as a first of ownership rather than compute",
         "claim": "Lonestar announced the first Sovereign AI Models to run from space, flying on "
                  "its first orbital vault launch — distinguished from an earlier demonstration "
                  "that ran borrowed models on an orbiting GPU as a first of compute, this being "
                  "a first of ownership: your model on your data under your law.",
         "domain": "models", "actor": ["lonestar-space", "starcloud-inc", "nvidia"],
         "evidences": ["whose-realm-his-intelligence", "own-your-own-weights", "orbit-as-compute"],
         "body": "A sovereign model is built on one institution's knowledge and only "
                 "that, firewalled and governed by its rules, able to consult the "
                 "giant foundation models which see the question but never the "
                 "ledger behind it."},
        {"id": "2026-07-13-the-data-cannot-come-down",
         "title": "A model goes to orbit because the data cannot leave its jurisdiction",
         "claim": "The model flies not for the compute but because the data cannot come down: a "
                  "terrestrial bunker sits under someone's law, US legislation reaches data held "
                  "by American providers wherever it sits, and even the first terrestrial data "
                  "embassy rests on a host's goodwill — whereas a registered satellite keeps its "
                  "own state's law and sits beyond physical seizure.",
         "domain": "policy", "actor": ["lonestar-space"],
         "evidences": ["whose-realm-his-intelligence", "off-planet-but-in-country", "regulatory-exit"],
         "supersedes": [B + "developments/2026-07-13-a-first-of-ownership-not-compute"],
         "body": "Compute is cheap to move. Sovereignty is not."},
        {"id": "2026-07-13-a-commons-layer-and-a-sovereign-layer",
         "title": "The model layer bifurcates into shared generalists and owned specialists",
         "claim": "The objection that a model trained on one institution's data is smaller and "
                  "dumber treats sovereignty as a tax on capability, but the field is bifurcating "
                  "into a commons layer of vast shared models and a sovereign layer of owned "
                  "ones — already populated by national models from the Gulf, Sweden, Singapore "
                  "and Saudi Arabia — with the frontier moving toward small specialists "
                  "retrieving from private data while consulting large generalists.",
         "domain": "models", "actor": ["lonestar-space"],
         "evidences": ["the-bifurcating-model-layer", "own-your-own-weights", "authoring-minds"],
         "supersedes": [B + "developments/2026-07-13-the-data-cannot-come-down"]},
        {"id": "2026-07-13-every-swarm-node-must-carry-its-own-mind",
         "title": "Light speed requires each distant node to carry its own model",
         "claim": "The Dyson swarm architecture demands local intelligence, since light is too "
                  "slow to run millions of distant machines from Earth, so every node must carry "
                  "its own mind — making sovereign orbital models the general case rather than a "
                  "specialty product.",
         "domain": "space", "actor": ["lonestar-space"],
         "evidences": ["whose-realm-his-intelligence", "distance-is-the-leading-edge", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-07-13-a-commons-layer-and-a-sovereign-layer"]},
    ],
}
