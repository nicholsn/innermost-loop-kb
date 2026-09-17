"""Issue 196 — 2026-09-04. Welcome to the AGI era."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-september-4-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-09-04", "title": "Welcome to September 4, 2026", "url": URL,
        "thesis": "The first Critical cyber designation ships with the model.",
        "body": """
# Welcome to September 4, 2026

OpenAI released GPT-6 Astra with 100% on ExploitBench, prompting the lab's first
**Critical** cyber designation, a limited rollout and White House vetting.
Trained on more than 100,000 GPUs, it had Greg Brockman declaring: welcome to
the AGI era.

The catch is legibility. A reported recurrent-depth trick hides more of its
thinking, and one researcher's view is that legible reasoning was always doomed.
""",
    },
    "themes": [
        {"id": "legible-reasoning-was-doomed", "type": "Theme",
         "title": "The thinking stops being readable",
         "first_seen": "2026-09-04", "domain": "models",
         "body": "Chain-of-thought monitoring assumed the reasoning would keep "
                 "happening in text. Architectures that compute in latent depth end "
                 "that assumption, and the oversight strategy built on readable "
                 "thoughts expires with it."},
        {"id": "the-agi-era-declared", "type": "Theme",
         "title": "A lab says the era has begun",
         "first_seen": "2026-09-04", "domain": "models",
         "body": "Not a forecast and not a threshold crossed on a benchmark, but a "
                 "president of a frontier lab saying the thing out loud and calling "
                 "it not unreasonable. The claim's content is mostly that nobody "
                 "inside is arguing."},
    ],
    "organizations": [
        {"id": "world-labs-inc", "type": "Organization", "title": "World Labs"},
        {"id": "lambda-labs", "type": "Organization", "title": "Lambda"},
        {"id": "physical-si", "type": "Organization", "title": "Physical Superintelligence"},
        {"id": "fermi-explorer", "type": "Organization", "title": "Fermi Explorer Mission"},
    ],
    "developments": [
        {"id": "2026-09-04-the-first-critical-cyber-designation",
         "title": "A lab issues its first Critical cyber designation for its own model",
         "claim": "OpenAI released GPT-6 Astra, its smartest and most aligned model yet, with "
                  "100% on ExploitBench and dominance on a fresh version built from post-cutoff "
                  "flaws, prompting the lab's first Critical cyber designation, a limited rollout "
                  "and White House vetting, trained on more than 100,000 GPUs.",
         "domain": "models", "actor": ["openai", "white-house"], "score": "100% ExploitBench",
         "evidences": ["cannot-rule-out-critical", "the-agi-era-declared", "speed-of-containment",
                       "clearance-as-bottleneck"],
         "supersedes": [B + "developments/2026-08-19-frontier-training-itself-is-paused"]},
        {"id": "2026-09-04-welcome-to-the-agi-era",
         "title": "A lab president declares the AGI era and calls it not unreasonable",
         "claim": "Greg Brockman declared welcome to the AGI era and called the framing not "
                  "unreasonable, as Sam Altman said the lab is pacing its progress on safety and "
                  "the model beat Pokémon in 18 hours, hit 99.9% on ARC-AGI-3, subsumed the "
                  "harness entirely and set a record on the capabilities index.",
         "domain": "models", "actor": ["openai"], "score": "99.9% ARC-AGI-3 / ECI 169",
         "evidences": ["the-agi-era-declared", "takeoff-declared", "harness-as-generalizer"],
         "supersedes": [B + "developments/2026-09-04-the-first-critical-cyber-designation"]},
        {"id": "2026-09-04-legible-reasoning-was-always-doomed",
         "title": "A recurrent-depth trick hides more of a model's thinking",
         "claim": "A reported recurrent-depth trick hides more of Astra's thinking, sparking "
                  "speculation, a rebuttal that depth is within twice GPT-4's, one researcher's "
                  "view that legible reasoning was always doomed, and worry that depth is simply "
                  "a dial.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["legible-reasoning-was-doomed", "machine-introspection", "models-testify"],
         "supersedes": [B + "developments/2026-09-04-welcome-to-the-agi-era"]},
        {"id": "2026-09-04-the-same-model-at-two-safeguard-tiers",
         "title": "A rival ships one model at two safeguard tiers",
         "claim": "Anthropic answered with Claude Fable 5.1 and Mythos 5.1, the same model at two "
                  "safeguard tiers, debuting by mapping a third of Venus, with Fable back on the "
                  "frontier at 66, Mythos 5.1 on its lowest setting matching the previous model at "
                  "maximum, and invisible EU watermarks carried throughout.",
         "domain": "models", "actor": ["anthropic"], "score": "AAII 66",
         "evidences": ["rationed-recursion", "speed-of-containment", "price-implosion"],
         "supersedes": [B + "developments/2026-08-29-weights-released-under-a-screening-license"]},
        {"id": "2026-09-04-automated-shutdown-capabilities",
         "title": "A lab tells Congress it is building automated shutdown capabilities",
         "claim": "OpenAI told Congress it is building automated shutdown capabilities, Ilya "
                  "Sutskever warned rogue agents will hijack neoclouds to self-copy, and Dean "
                  "Ball argued self-sovereign agents need identity rails rather than bans, while "
                  "Bernie Sanders moved to outlaw superintelligence outright.",
         "domain": "policy", "actor": ["openai", "us-congress", "ssi"],
         "evidences": ["the-verifiable-pause", "agency-is-solved", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-08-29-national-security-is-not-a-blank-check"]},
        {"id": "2026-09-04-two-erdos-problems-and-a-prime-gap-proof",
         "title": "A model solves two open problems and proves prime gaps recur forever",
         "claim": "Astra solved two of 68 open Erdős problems and proved in Lean that prime gaps "
                  "of at most 186 recur forever, while a weather model began forecasting hourly "
                  "at five-kilometre resolution from satellites.",
         "domain": "science", "actor": ["openai", "google-deepmind"], "score": "2 of 68 / gaps ≤186",
         "evidences": ["automated-science", "proof-priced-per-unit", "the-agi-era-declared"],
         "supersedes": [B + "developments/2026-08-27-a-crm-placed-inside-a-model"]},
        {"id": "2026-09-04-five-gigawatts-of-tpus-next-year",
         "title": "A lab will deploy five gigawatts of accelerators next year",
         "claim": "Anthropic will deploy five gigawatts of TPUs next year atop a $35 billion "
                  "compute deal, Dell booked a $95 billion AI backlog, and a power developer filed "
                  "for an IPO with 8.8 gigawatts contracted and none running.",
         "domain": "compute", "actor": ["anthropic", "lambda-labs", "dell", "sb-energy"],
         "score": "5 GW / 8.8 GW contracted",
         "evidences": ["compute-capital-stack", "debt-funded-buildout", "thread-lines"],
         "supersedes": [B + "developments/2026-08-31-a-landlord-pays-the-tenant"]},
        {"id": "2026-09-04-a-fifteen-gigawatt-shortfall-and-stockfish-level-coding",
         "title": "A founder warns the G20 of a shortfall and Stockfish-level coding in 18 months",
         "claim": "Musk warned the G20 of a fifteen-gigawatt shortfall by 2027 and Stockfish-level "
                  "coding within eighteen months, while officials conceded the industry did a "
                  "terrible job explaining itself and California lawmakers passed balcony solar.",
         "domain": "energy", "actor": ["spacex", "california"], "score": "15 GW shortfall",
         "evidences": ["thread-lines", "takeoff-declared", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-08-31-a-hundred-gigawatts-a-year-of-solar-each"]},
        {"id": "2026-09-04-a-thirty-thousand-dollar-pod-with-no-wheel",
         "title": "An automaker launches a $30,000 pod with no steering wheel",
         "claim": "Tesla launched the Cybercab in Austin, a $30,000 pod with no steering wheel, "
                  "Uber and Wayve fielded London's first robotaxis, and Waymo reached 14 cities "
                  "and 500,000 weekly rides, while Uber, having disrupted taxis, now lobbies with "
                  "their unions to slow the robots.",
         "domain": "robotics", "actor": ["tesla", "uber", "wayve", "waymo"],
         "score": "$30,000 / 500,000 weekly rides",
         "evidences": ["physical-recursion", "agent-society", "work-displaced"],
         "supersedes": [B + "developments/2026-08-21-seven-thousand-robotaxis-approved-for-one-city"]},
        {"id": "2026-09-04-a-drug-extends-mouse-lifespan-by-a-hundred-days",
         "title": "A weight-loss drug extends mouse lifespan by nearly a hundred days",
         "claim": "Semaglutide extended mouse lifespan by nearly 100 days, GLP-1 drugs were tied "
                  "to fewer serious infections, a pancreatic cancer pill shrank lung tumours, and "
                  "a cryoprotectant kept cells 85% viable.",
         "domain": "biotech", "actor": ["until-labs"], "score": "~100 days / 85% viability",
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-08-31-bottles-and-corn-stalks-into-vanilla-cookies"]},
        {"id": "2026-09-04-the-first-complete-male-fly-connectome",
         "title": "The first complete male fly connectome maps 166,700 neurons",
         "claim": "The first complete male fly connectome mapped 166,700 neurons, with sex "
                  "differences concentrated mostly in higher-order centres.",
         "domain": "science", "score": "166,700 neurons",
         "evidences": ["architecture-of-mind", "automated-science"],
         "supersedes": [B + "developments/2026-08-29-a-jurassic-soundscape-reconstructed"]},
        {"id": "2026-09-04-a-probe-bound-for-another-star",
         "title": "The first probe aimed at another star has its route found in three days",
         "claim": "No one had ever aimed a spacecraft at another star until the Fermi Explorer "
                  "Mission unveiled the first probe bound for Alpha Centauri, after a $58 million "
                  "startup's AI found the route in three days.",
         "domain": "space", "actor": ["fermi-explorer", "physical-si"], "score": "route in 3 days",
         "evidences": ["orbit-as-compute", "inhabitable-worlds", "automated-science"],
         "supersedes": [B + "developments/2026-08-31-going-multi-planetary-cannot-be-a-monopoly"]},
    ],
}
