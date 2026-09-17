"""Issue 009 — 2025-12-19. The feedback loop tightens."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-19-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-19",
        "title": "Welcome to December 19, 2025",
        "url": URL,
        "thesis": "The feedback loop is tightening faster than we can measure.",
        "body": """
# Welcome to December 19, 2025

Noam Shazeer puts it at 50/50 that the next major breakthrough comes from Gemini
rather than a human researcher. Four days earlier the corpus recorded a model
watching its own training runs; this is the same claim stated as a probability.

The counterweight is friction. The Gemini 3 team now *rejects* performance gains
that exceed a complexity budget, protecting the throughput of 150 researchers
over isolated metrics — capability traded away deliberately.
""",
    },
    "themes": [
        {"id": "data-beyond-text", "type": "Theme",
         "title": "Grounding in physics, not web text", "first_seen": "2025-12-19",
         "domain": "science",
         "body": "The human-text corpus runs out, so the frontier turns to measurement: "
                 "scientific data at a scale that dwarfs the text internet, promising "
                 "models grounded in the non-negotiable rather than the web's guesses."},
    ],
    "organizations": [
        {"id": "dte-energy", "type": "Organization", "title": "DTE Energy",
         "resource": "https://www.dteenergy.com/", "body": "Michigan utility powering a Stargate site."},
        {"id": "samsung", "type": "Organization", "title": "Samsung",
         "resource": "https://www.samsung.com/", "body": "Memory and SoC manufacturer."},
        {"id": "tae-technologies", "type": "Organization", "title": "TAE Technologies",
         "resource": "https://tae.com/", "body": "Fusion developer."},
        {"id": "rocket-lab", "type": "Organization", "title": "Rocket Lab",
         "resource": "https://www.rocketlabusa.com/", "body": "Small-launch and satellite manufacturer."},
        {"id": "laude-institute", "type": "Organization", "title": "Laude Institute",
         "description": "San Francisco research nonprofit that co-hosts the Terminal-Bench "
                        "leaderboard with Stanford.",
         "resource": "https://www.laude.org/",
         "sameAs": ["http://www.wikidata.org/entity/Q137795953"],
         "tags": ["nonprofit", "research-lab"],
         "body": "The Laude Institute is a San Francisco research organization that, with Stanford "
                 "and Harbor, hosts [Terminal-Bench](/benchmarks/terminal-bench-2.md) "
                 "([tbench.ai](https://www.tbench.ai/)). In this corpus it appears only as a "
                 "publisher of that benchmark, the scoreboard on which "
                 "[GPT-5.2-Codex led at launch](/developments/2025-12-19-gpt52-codex-terminal-bench.md) "
                 "and on which a [record later fell in under thirty minutes](/developments/2026-02-06-record-falls-in-thirty-minutes.md)."},
    ],
    "people": [
        {"id": "noam-shazeer", "type": "Person", "title": "Noam Shazeer", "name": "Noam Shazeer",
         "description": "Transformer co-author and senior Google AI researcher who put even odds on "
                        "Gemini, not a human, making the next major breakthrough; poached by OpenAI "
                        "in June 2026.",
         "resource": "https://www.noamshazeer.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q30251943"],
         "tags": ["researcher"],
         "body": "Noam Shazeer is a co-author of \"Attention Is All You Need\" whom Google paid "
                 "$2.7 billion to reacquire in 2024. In this corpus he appears first as the Google "
                 "researcher who [put the odds at 50/50](/developments/2025-12-19-shazeer-5050-gemini-breakthrough.md) "
                 "that Gemini rather than a human generates the next breakthrough, the newsletter's "
                 "marker for the onset of recursive self-improvement. He returns in June 2026 when "
                 "[OpenAI poached him](/developments/2026-06-19-a-transformer-author-poached-back.md) "
                 "and Alphabet [lost $250 billion in a day](/developments/2026-06-24-a-quarter-trillion-lost-to-two-departures.md) "
                 "on his and John Jumper's departures."},
    ],
    "roles": [
        {"id": "noam-shazeer-google-ai-researcher", "type": "Role",
         "title": "Noam Shazeer, AI researcher at Google",
         "roleName": "AI researcher",
         "startDate": "2024",
         "memberOf": [B + "organizations/google"],
         "holder": [B + "people/noam-shazeer"],
         "description": "The Google position, held after the 2024 reacquisition, from which he put "
                        "even odds on Gemini making the next breakthrough.",
         "body": "Google paid $2.7 billion in 2024 to bring Shazeer back, and it was as Google's "
                 "researcher that he [put the odds at 50/50](/developments/2025-12-19-shazeer-5050-gemini-breakthrough.md) "
                 "that the next major breakthrough would be Gemini's rather than a human's. The "
                 "corpus records the position ending when "
                 "[OpenAI poached him](/developments/2026-06-19-a-transformer-author-poached-back.md) "
                 "in June 2026."},
        {"id": "noam-shazeer-openai-researcher", "type": "Role",
         "title": "Noam Shazeer, AI researcher at OpenAI",
         "roleName": "AI researcher",
         "startDate": "2026",
         "memberOf": [B + "organizations/openai"],
         "holder": [B + "people/noam-shazeer"],
         "description": "The move the corpus records in June 2026, when OpenAI reportedly poached "
                        "him two years after Google's $2.7 billion reacquisition.",
         "body": "OpenAI reportedly [poached Shazeer](/developments/2026-06-19-a-transformer-author-poached-back.md) "
                 "in June 2026, a jump he confirmed publicly; days later Alphabet "
                 "[lost $250 billion](/developments/2026-06-24-a-quarter-trillion-lost-to-two-departures.md) "
                 "in a day on his and John Jumper's defections."},
    ],
    "systems": [
        {"id": "gpt-5-2-codex", "type": "AISystem", "title": "GPT-5.2-Codex",
         "developed_by": [B + "organizations/openai"], "modality": "code",
         "evaluated_on": [B + "benchmarks/terminal-bench-2"]},
        {"id": "functiongemma", "type": "AISystem", "title": "FunctionGemma",
         "developed_by": [B + "organizations/google"], "modality": "function calling",
         "body": "A 270M model specialized for tool calls — intelligence pushed to the edge."},
        {"id": "genie", "type": "AISystem", "title": "Genie",
         "developed_by": [B + "organizations/google-deepmind"], "modality": "world model"},
        {"id": "sima", "type": "AISystem", "title": "SIMA",
         "developed_by": [B + "organizations/google-deepmind"], "modality": "embodied agent"},
    ],
    "benchmarks": [
        {"id": "terminal-bench-2", "type": "Benchmark", "title": "Terminal Bench 2.0",
         "measures_capability": "completing real tasks in a terminal",
         "description": "Agentic terminal-task benchmark whose record changed hands between "
                        "labs within half an hour and which a self-rewriting harness later "
                        "lifted by double digits.",
         "resource": "https://www.tbench.ai/",
         "published_by": [B + "organizations/stanford", B + "organizations/laude-institute"],
         "tags": ["coding-agent"],
         "body": "Terminal-Bench 2.0 scores agents on completing real tasks in a command-line "
                 "environment; it is hosted by Stanford, Harbor and the Laude Institute "
                 "([leaderboard](https://www.tbench.ai/)). It enters the corpus as the benchmark "
                 "[GPT-5.2-Codex topped](/developments/2025-12-19-gpt52-codex-terminal-bench.md) "
                 "on release, then becomes the clearest scoreboard for lab-versus-lab velocity when "
                 "Claude Opus 4.6's record [fell to GPT-5.3-Codex in under thirty minutes](/developments/2026-02-06-record-falls-in-thirty-minutes.md). "
                 "In June 2026 it is the yardstick on which an agent that "
                 "[rewrote its own scaffolding](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) "
                 "gained double digits with no human engineers involved."},
    ],
    "facilities": [
        {"id": "stargate-michigan", "type": "Facility", "title": "Stargate Michigan",
         "operated_by": [B + "organizations/oracle", B + "organizations/openai"],
         "located_in": "Michigan, USA", "capacity": "1.4 GW"},
        {"id": "genesis-mission", "type": "Facility", "title": "Genesis Mission",
         "operated_by": [B + "organizations/doe"], "located_in": "United States",
         "capacity": "~3,600 PB of scientific data",
         "body": "A corpus of measurement rather than text, estimated to dwarf the "
                 "text-based internet."},
    ],
    "developments": [
        {"id": "2025-12-19-shazeer-5050-gemini-breakthrough",
         "title": "Shazeer puts even odds on Gemini making the next breakthrough",
         "claim": "Google's Noam Shazeer put the odds at 50/50 that the next major AI "
                  "breakthrough will be generated by Gemini rather than a human researcher.",
         "description": "The newsletter's marker for the official onset of recursive "
                        "self-improvement: the loop stated as a probability by a Transformer "
                        "co-author inside Google rather than as an operational anecdote.",
         "domain": "agents", "actor": ["people/noam-shazeer", "google"], "score": "50/50",
         "about": [B + "systems/gemini"],
         "evidences": ["recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-15-codex-babysits-own-training"],
         "relatedTo": [B + "developments/2025-12-18-posttrainbench-models-training-models",
                       B + "developments/2025-12-19-gemini-complexity-budget",
                       B + "developments/2026-05-05-sixty-percent-odds-on-rsi-by-2028"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2025-12-19-deepmind-proto-agi-merge",
                        "relation_label": "corroborates"}],
         "tags": ["rsi", "forecast", "ai-r-and-d"],
         "supporting_text": "“50/50” that the next major AI breakthrough will be generated by Gemini",
         "sources": [{"id": "curran-shazeer-5050-post",
                      "resource": "https://x.com/andrewcurran_/status/2001766860791202073",
                      "title": "Andrew Curran on X: Noam Shazeer puts the odds at 50/50 that the "
                               "next major AI breakthrough comes from Gemini",
                      "author": "human:andrew-curran"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Asked where the next major AI breakthrough will come from, Google's Noam Shazeer "
                 "put it at even odds between [Gemini](/systems/gemini.md) and a human researcher, "
                 "in a remark relayed by Andrew Curran "
                 "([post](https://x.com/andrewcurran_/status/2001766860791202073)). The newsletter "
                 "calls it the official onset of recursive self-improvement: four days after "
                 "[Codex was reported watching its own training](/developments/2025-12-15-codex-babysits-own-training.md) "
                 "and a day after [PostTrainBench ranked models at training models](/developments/2025-12-18-posttrainbench-models-training-models.md), "
                 "the loop is stated as a probability by a co-author of the Transformer paper. The "
                 "same issue records DeepMind [assembling the pieces](/developments/2025-12-19-deepmind-proto-agi-merge.md) "
                 "for a proto-AGI and, as counterweight, the Gemini team "
                 "[declining gains that exceed a complexity budget](/developments/2025-12-19-gemini-complexity-budget.md). "
                 "The probability form recurs when Jack Clark "
                 "[puts recursive self-improvement at 60% by 2028](/developments/2026-05-05-sixty-percent-odds-on-rsi-by-2028.md); "
                 "Shazeer himself was [poached by OpenAI](/developments/2026-06-19-a-transformer-author-poached-back.md) "
                 "in June 2026."},
        {"id": "2025-12-19-deepmind-proto-agi-merge",
         "title": "DeepMind plans to converge its world models into a proto-AGI",
         "claim": "DeepMind plans to merge Nano Banana Pro with its Genie and SIMA world "
                  "models into a converged proto-AGI.",
         "domain": "models", "actor": ["google-deepmind"],
         "about": [B + "systems/genie", B + "systems/sima"],
         "evidences": ["inhabitable-worlds", "network-over-node"]},
        {"id": "2025-12-19-gemini-complexity-budget",
         "title": "The Gemini team rejects gains that exceed a complexity budget",
         "claim": "The Gemini 3 team said it now rejects performance gains that exceed a "
                  "complexity budget, prioritizing the cumulative velocity of 150 researchers "
                  "over isolated metrics.",
         "domain": "models", "actor": ["google"], "score": "150 researchers",
         "body": "Capability deliberately declined to protect throughput — the first time "
                 "the corpus records a lab trading accuracy away on purpose."},
        {"id": "2025-12-19-differentiable-retrieval-pretraining",
         "title": "Google works to make retrieval differentiable in pre-training",
         "claim": "Google is working to make retrieval fully differentiable within "
                  "pre-training, hardwiring the internet into the model itself.",
         "domain": "models", "actor": ["google"], "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-19-gpt52-codex-terminal-bench",
         "title": "GPT-5.2-Codex tops Terminal Bench 2.0 and automates the white-hat",
         "claim": "OpenAI released GPT-5.2-Codex, which leads Terminal Bench 2.0 and jumps "
                  "sharply on professional capture-the-flag cybersecurity challenges.",
         "domain": "agents", "actor": ["openai"],
         "about": [B + "systems/gpt-5-2-codex", B + "benchmarks/terminal-bench-2"],
         "evidences": ["autonomy-clock-speed"]},
        {"id": "2025-12-19-functiongemma-edge",
         "title": "FunctionGemma pushes tool use to the network edge",
         "claim": "Google released FunctionGemma, a 270M model fine-tuned for function calling, "
                  "with a recipe for further specialization.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/functiongemma"],
         "evidences": ["network-over-node"]},
        {"id": "2025-12-19-genesis-mission-3600-petabytes",
         "title": "The Genesis Mission could unlock 3,600 petabytes of scientific data",
         "claim": "Third-party analysis estimates the DOE's Genesis Mission could unlock 3,600 "
                  "petabytes of scientific training data, a corpus dwarfing the text internet.",
         "domain": "science", "actor": ["doe"], "score": "3,600 PB",
         "about": [B + "facilities/genesis-mission"],
         "evidences": ["data-beyond-text", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2025-12-13-doe-science-security-platform"]},
        {"id": "2025-12-19-datacenter-investment-61b",
         "title": "A record $61B flowed into datacenters this year",
         "claim": "A record $61 billion flowed into data centers during the year.",
         "domain": "economics", "score": "$61B",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out"]},
        {"id": "2025-12-19-speed-act-passes-house",
         "title": "The House passes the SPEED Act, cutting NEPA timelines to 150 days",
         "claim": "The House passed the SPEED Act, cutting NEPA litigation timelines from six "
                  "years to 150 days to fast-track AI infrastructure.",
         "domain": "policy", "actor": ["us-congress"], "score": "6 years to 150 days",
         "evidences": ["politics-as-infrastructure", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2025-12-17-speed-act-permitting"]},
        {"id": "2025-12-19-michigan-stargate-1-4gw",
         "title": "Michigan approves 1.4 GW for an Oracle and OpenAI Stargate site",
         "claim": "Michigan approved DTE Energy to power a 1.4-gigawatt Stargate facility for "
                  "Oracle and OpenAI.",
         "domain": "compute", "actor": ["dte-energy", "oracle", "openai"], "score": "1.4 GW",
         "about": [B + "facilities/stargate-michigan"],
         "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-19-anthropic-2-3gw-bitcoin-miners",
         "title": "Anthropic secures 2.3 GW from repurposed Bitcoin miners",
         "claim": "Anthropic secured 2.3 GW of capacity through Google-backed leases with "
                  "repurposed Bitcoin mining sites.",
         "domain": "energy", "actor": ["anthropic", "google"], "score": "2.3 GW",
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2025-12-19-samsung-exynos-2600-2nm",
         "title": "Samsung ships the first 2-nm gate-all-around phone SoC",
         "claim": "Samsung unveiled the Exynos 2600, the first 2-nm gate-all-around smartphone "
                  "system-on-chip.",
         "domain": "compute", "actor": ["samsung"], "score": "2 nm"},
        {"id": "2025-12-19-space-superiority-lunar-reactor",
         "title": "A White House order demands a lunar surface reactor by 2030",
         "claim": "A White House executive order on Ensuring American Space Superiority requires "
                  "deployment of space nuclear power and a lunar surface reactor by 2030.",
         "domain": "space", "actor": ["white-house"], "score": "by 2030",
         "evidences": ["orbit-as-compute", "politics-as-infrastructure"]},
        {"id": "2025-12-19-artemis-ii-months-away",
         "title": "Artemis II is months from a human lunar flyby",
         "claim": "NASA administrator Jared Isaacman confirmed Artemis II is months away from "
                  "a crewed lunar flyby.",
         "domain": "space", "actor": ["nasa"],
         "supersedes": [B + "developments/2025-12-18-isaacman-nasa-project-athena"]},
        {"id": "2025-12-19-supersonic-aviation-act",
         "title": "The House legalizes overland supersonic flight",
         "claim": "The House passed the Supersonic Aviation Modernization Act, legalizing "
                  "overland supersonic flight provided the boom does not reach the ground.",
         "domain": "policy", "actor": ["us-congress"], "evidences": ["legislating-the-shift"]},
        {"id": "2025-12-19-trump-media-tae-fusion",
         "title": "Trump Media merges with fusion firm TAE in a $6B deal",
         "claim": "Trump Media is merging with fusion company TAE Technologies in a $6 billion "
                  "deal to build a utility-scale plant.",
         "domain": "energy", "actor": ["tae-technologies"], "score": "$6B",
         "evidences": ["industrialized-nature"]},
        {"id": "2025-12-19-openai-100b-at-830b",
         "title": "OpenAI raises $100B at an $830B valuation",
         "claim": "OpenAI is raising $100 billion at an $830 billion valuation on $19 billion "
                  "of annualized revenue.",
         "domain": "economics", "actor": ["openai"], "score": "$100B at $830B, $19B ARR",
         "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-19-thinking-machines-50b",
         "title": "Thinking Machines discusses a $50B valuation",
         "claim": "Mira Murati's Thinking Machines is discussing a $50 billion valuation.",
         "domain": "economics", "actor": ["thinking-machines"], "score": "$50B"},
    ],
}
