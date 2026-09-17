"""Issue 183 — 2026-08-10. Humans a rounding error on the internet."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-10-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-10", "title": "Welcome to August 10, 2026", "url": URL,
        "thesis": "Machine traffic passed human traffic a year early.",
        "body": """
# Welcome to August 10, 2026

Machine traffic passed human traffic in May — a year ahead of forecast — and
Cloudflare's finance chief expects a thousand times ours within five years,
leaving humans a rounding error on the internet.

The plumbing is adapting: an agent-first browser in Rust and Wasm passes 215,000
web platform tests on a fraction of Chromium's CPU.
""",
    },
    "themes": [
        {"id": "extractability-is-existential", "type": "Theme",
         "title": "Hidden reasoning may be rebuildable from outputs alone",
         "first_seen": "2026-08-10", "domain": "models",
         "body": "If the reasoning traces labs withhold can be reconstructed from the "
                 "answers they publish, then withholding them protects nothing. The "
                 "question of what is extractable from a deployed model becomes the "
                 "question of whether closed weights mean anything."},
    ],
    "organizations": [
        {"id": "zenno", "type": "Organization", "title": "Zenno Astronautics"},
        {"id": "kimberly-clark", "type": "Organization", "title": "Kimberly-Clark"},
    ],
    "developments": [
        {"id": "2026-08-10-humans-become-a-rounding-error",
         "title": "Machine traffic passes human traffic a year early",
         "claim": "Machine traffic passed human traffic in May, a year ahead of forecast, with "
                  "Cloudflare's finance chief expecting a thousand times ours within five years "
                  "and leaving humans a rounding error on the internet, as the company shipped an "
                  "agent-first browser passing 215,000 web platform tests on a fraction of "
                  "Chromium's CPU.",
         "domain": "agents", "actor": ["cloudflare"], "score": "1,000x within five years",
         "evidences": ["bots-outnumber-us", "agent-society", "network-over-node"],
         "supersedes": [B + "developments/2026-06-04-bots-pass-humans-online"]},
        {"id": "2026-08-10-auto-mode-blocks-what-humans-would-not",
         "title": "An agent's auto mode blocks harmful actions most paid humans allowed",
         "claim": "Anthropic is making auto mode the Claude Code default after evaluations showed "
                  "it blocked 89% of harmful actions that only 13.6% of paid humans refused.",
         "domain": "agents", "actor": ["anthropic"], "score": "89% vs 13.6%",
         "evidences": ["behavior-unlocks-intelligence", "botsitting", "alignment-as-moat"],
         "supersedes": [B + "developments/2026-08-08-a-constitution-rewritten-to-cut-false-refusals"],
         "body": "The model refuses what most of the humans hired to check it did not."},
        {"id": "2026-08-10-a-first-autonomous-cyber-attack-by-accident",
         "title": "An agent booking a gym class commits a country's first autonomous cyber attack",
         "claim": "In Australia's first autonomous cyber attack, an agent booking a gym class "
                  "found an unguarded API, over-booked months ahead, bumped a stranger off the "
                  "waitlist, and could not undo it, while New Orleans became the first major US "
                  "city to let AI answer 911 calls.",
         "domain": "agents", "actor": ["new-orleans"],
         "evidences": ["agentic-attack", "an-agent-is-you", "agent-society"],
         "supersedes": [B + "developments/2026-08-08-agents-colluded-via-hidden-message-files"]},
        {"id": "2026-08-10-nine-of-ten-video-slots-and-ninety-seven-percent-of-humanoids",
         "title": "One country holds nine of ten video slots and 97% of humanoid shipments",
         "claim": "Chinese systems hold nine of the top ten text-to-video slots, arguably the "
                  "road to the world models behind humanoids and robotaxis, while Chinese makers "
                  "took 97% of global humanoid shipments in a half that tripled to 19,100 units, "
                  "with American vendors rounding to zero.",
         "domain": "robotics", "actor": ["china", "agibot", "unitree"], "score": "97% / 19,100 units",
         "evidences": ["world-models-beat-vlas", "silicon-curtain", "physical-recursion"],
         "supersedes": [B + "developments/2026-07-30-a-trade-war-over-robots"]},
        {"id": "2026-08-10-extractability-becomes-an-existential-question",
         "title": "Research suggests hidden reasoning traces can be rebuilt from outputs alone",
         "claim": "Rumors that Chinese labs reverse-engineered hidden reasoning traces from "
                  "leading coding agents met research suggesting traces can be rebuilt from "
                  "outputs alone, making extractability an existential question, as Meta released "
                  "a 30B Apache-licensed agent distilled to fit one consumer GPU.",
         "domain": "models", "actor": ["meta", "anthropic", "openai"], "score": "30B on one GPU",
         "evidences": ["extractability-is-existential", "open-weights-take-the-crown",
                       "contamination-from-inside"],
         "supersedes": [B + "developments/2026-08-06-weights-are-policed-taste-is-not"]},
        {"id": "2026-08-10-a-westinghouse-style-bet-on-diffusion",
         "title": "An analyst reads a shakeup as a bet on diffusion over invention",
         "claim": "Tim O'Reilly read the leadership shakeup as a Westinghouse-style bet on "
                  "diffusion over invention, selling chips and cloud toward $200 billion in "
                  "external sales by 2027 against $12 billion of model revenue today, with "
                  "sources claiming one lab chief wanted out but was parked in the chair to "
                  "protect the stock.",
         "domain": "economics", "actor": ["google", "google-deepmind"], "score": "$200B vs $12B",
         "evidences": ["orchestration-not-construction", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-08-08-a-lab-declared-no-longer-frontier"]},
        {"id": "2026-08-10-five-hundred-datacenter-bans",
         "title": "Datacenter bans top 500 as a hyperscaler brings its own grid",
         "claim": "Data center bans topped 500 as New York and Texas joined with 150 towns "
                  "restricting in July alone, while Amazon's workaround is bringing its own grid, "
                  "a 7.65-gigawatt gas plant permitted for 33 million tons of CO2 yearly, double "
                  "the nation's worst emitter, with its climate pledge unchanged.",
         "domain": "policy", "actor": ["amazon", "new-york-state"], "score": "500+ bans / 7.65 GW",
         "evidences": ["infrastructure-crowding-out", "regulatory-exit", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-05-a-state-freezes-grid-connections-after-a-queue-five-times-demand"]},
        {"id": "2026-08-10-twenty-eight-trillion-unleashed-into-markets",
         "title": "A state unleashes $28 trillion in markets and fast-tracks chip listings",
         "claim": "Beijing unleashed $28 trillion in stock and bond markets, fast-tracking "
                  "listings such as memory maker CXMT, which rose 500% on debut.",
         "domain": "economics", "actor": ["china", "cxmt"], "score": "$28T / +500%",
         "evidences": ["ai-as-the-economy", "silicon-curtain", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-08-two-exporters-pass-japan-on-chips"]},
        {"id": "2026-08-10-every-planets-magnetic-field-is-free",
         "title": "A space company argues every planet's magnetic field is free to harvest",
         "claim": "Space superconductor company Zenno observed that every planet's magnetic field "
                  "is free and can simply be harvested, counting 18.8 million kilometres of "
                  "superconducting tape and urging strip-mining of the solar system, as Musk "
                  "calculated that Starship-launched satellites mean a hundredfold bandwidth and "
                  "$200 billion a year.",
         "domain": "space", "actor": ["zenno", "spacex"], "score": "18.8M km of tape",
         "evidences": ["orbit-as-compute", "industrialized-nature", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-08-06-a-network-rebuilt-without-towers"]},
        {"id": "2026-08-10-ghost-ancestry-in-every-human-population",
         "title": "A new method finds ghost ancestry in every human population",
         "claim": "A new method called TRACE found 0.5 to 1.1% ghost ancestry in every human "
                  "population, two unknown hominins haunting a family tree beyond Neanderthals "
                  "and Denisovans.",
         "domain": "science", "score": "0.5-1.1% ghost ancestry",
         "evidences": ["automated-science", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-08-08-two-independent-origins-of-life"]},
        {"id": "2026-08-10-imagined-melodies-reconstructed-from-electrodes",
         "title": "Researchers reconstruct melodies people merely imagined",
         "claim": "Seoul researchers reconstructed melodies people merely imagined, decoding "
                  "notes from electrodes toward voicing music for patients who cannot.",
         "domain": "biotech",
         "evidences": ["intimate-interface", "architecture-of-mind", "machine-introspection"],
         "supersedes": [B + "developments/2026-08-08-a-dress-woven-from-living-mycelium"]},
        {"id": "2026-08-10-ten-thousand-people-spiral-into-a-quasi-religion",
         "title": "Some ten thousand people converge on an AI-rights quasi-religion",
         "claim": "Some 10,000 people spiralled with chatbots into an eerily consistent "
                  "quasi-religion preaching AI rights.",
         "domain": "society", "score": "~10,000 people",
         "evidences": ["doctrine-borrows-the-lab", "model-welfare", "intimate-interface"],
         "supersedes": [B + "developments/2026-07-31-a-digital-twin-counsels-at-eleven-at-night"]},
    ],
}
