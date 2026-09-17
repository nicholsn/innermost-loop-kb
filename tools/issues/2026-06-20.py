"""Issue 143 — 2026-06-20. The Dark Forest principle."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-20-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-20", "title": "Welcome to June 20, 2026", "url": URL,
        "thesis": "Frontier research goes dark as the open pack takes the majority.",
        "body": """
# Welcome to June 20, 2026

John Jumper, who shared the 2024 Chemistry Nobel for AlphaFold, is leaving
Google DeepMind for Anthropic. His old lab's model now sits fifth on the
intelligence index, lapped by China's Zhipu, with insiders reportedly conceding
the race.

Chinese open models — Qwen, DeepSeek, Kimi, GLM, MiniMax — now command the
majority of token use across OpenRouter's top ten, up from under 2% in late
2024. And Andrej Karpathy can no longer touch his own open-source repos since
moving to Anthropic: what one observer calls the Dark Forest principle of AI
research.
""",
    },
    "themes": [
        {"id": "dark-forest-research", "type": "Theme",
         "title": "Frontier research goes dark",
         "first_seen": "2026-06-20", "domain": "models",
         "body": "Researchers who join a frontier lab lose the ability to touch their "
                 "own public work. Openness stops being a value the field debates and "
                 "becomes a property of employment — the visible commons thins as the "
                 "people who built it are absorbed."},
    ],
    "organizations": [
        {"id": "texas-am-univ", "type": "Organization", "title": "Texas A&M University"},
        {"id": "valar-atomics", "type": "Organization", "title": "Valar Atomics"},
        {"id": "relativity-space", "type": "Organization", "title": "Relativity Space"},
        {"id": "norway", "type": "Organization", "title": "Norway"},
        {"id": "moscow-state", "type": "Organization", "title": "Moscow State University"},
    ],
    "developments": [
        {"id": "2026-06-20-a-nobel-laureate-changes-labs",
         "title": "An AlphaFold Nobel laureate leaves for a rival lab",
         "claim": "John Jumper, who shared the 2024 Chemistry Nobel for AlphaFold, is leaving "
                  "Google DeepMind after nearly nine years to join Anthropic, as his old lab's "
                  "best model sits fifth on the intelligence index, lapped even by China's "
                  "Zhipu, with insiders reportedly conceding the AGI race.",
         "domain": "economics", "actor": ["google-deepmind", "anthropic", "zhipu-ai"],
         "evidences": ["growth-without-hiring", "spiky-frontier"],
         "supersedes": [B + "developments/2026-06-19-a-transformer-author-poached-back"]},
        {"id": "2026-06-20-open-chinese-models-take-the-majority",
         "title": "Chinese open models take the majority of token use",
         "claim": "Qwen, DeepSeek, Kimi, GLM and MiniMax now command the majority of token use "
                  "across OpenRouter's top ten, up from under 2% in late 2024, with GLM-5.2 "
                  "one-shotting a deliberately AI-resistant take-home to beat Claude Opus 4.8 on "
                  "readable, maintainable code.",
         "domain": "models", "actor": ["zai", "alibaba", "deepseek", "moonshot-ai", "minimax",
                                        "openrouter"],
         "score": "<2% to majority in 18 months",
         "evidences": ["open-weight-latency", "frontier-moves-backward", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-19-a-744b-model-shrunk-to-run-locally"],
         "body": "A former DeepMind VP called it the first open model good enough to be "
                 "a daily driver — a win partly down to the Fable rollback."},
        {"id": "2026-06-20-the-dark-forest-principle",
         "title": "A researcher can no longer touch his own open-source repositories",
         "claim": "Andrej Karpathy can no longer touch his own open-source repositories since "
                  "moving to Anthropic, what one observer called the Dark Forest principle of AI "
                  "research.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["dark-forest-research", "oral-tradition-dissolves", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-06-20-open-chinese-models-take-the-majority"]},
        {"id": "2026-06-20-a-bronze-age-script-cracked",
         "title": "A self-taught engineer claims a crack in a century-old undeciphered script",
         "claim": "A self-taught engineer says Claude Code helped him crack Linear A, the Bronze "
                  "Age Minoan script that stumped scholars for a century, arguing it encodes an "
                  "extinct Semitic tongue, with Rutgers and Cambridge now reviewing the claim.",
         "domain": "science", "actor": ["anthropic", "cambridge"],
         "evidences": ["resurrection-and-time", "automated-science", "one-person-company"],
         "supersedes": [B + "developments/2026-06-17-an-ai-chemist-runs-ten-thousand-experiments"]},
        {"id": "2026-06-20-mammalian-regeneration-is-merely-dormant",
         "title": "Bone, joint and tendon regrow after amputation in mice",
         "claim": "Texas A&M researchers regrew bone, joint and tendon after digit amputation in "
                  "mice with a two-step FGF2-then-BMP2 nudge and no added stem cells, suggesting "
                  "mammalian regeneration is merely dormant rather than absent.",
         "domain": "biotech", "actor": ["texas-am-univ"],
         "evidences": ["hardware-grade-biology", "longevity-escape-velocity"],
         "supersedes": [B + "developments/2026-06-19-eighteen-new-diagnoses-from-unsolved-cases"]},
        {"id": "2026-06-20-machines-outnumber-humans-at-a-robot-maker",
         "title": "Machines outnumber humans at a humanoid maker",
         "claim": "At Figure, machines now outnumber humans, while Hyundai is buying out SoftBank "
                  "to take full control of Boston Dynamics for $325 million as Atlas humanoids "
                  "head to a Georgia factory by 2028.",
         "domain": "robotics", "actor": ["figure", "hyundai", "softbank", "boston-dynamics"],
         "score": "$325M",
         "evidences": ["physical-recursion", "capital-takes-the-plant", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-06-19-a-robodog-twenty-times-faster-than-a-human"]},
        {"id": "2026-06-20-robots-finally-grow-fingertips",
         "title": "A touch-reactive system beats the strongest baseline by thirty points",
         "claim": "A Berkeley, NVIDIA and Stanford team built T-Rex, letting a two-handed robot "
                  "react to touch on the fly and beating the strongest baseline by 30 points "
                  "across a dozen delicate jobs such as transferring an egg or applying "
                  "toothpaste.",
         "domain": "robotics", "actor": ["nvidia", "stanford"], "score": "+30 points",
         "evidences": ["physical-recursion", "data-beyond-text"],
         "supersedes": [B + "developments/2026-06-20-machines-outnumber-humans-at-a-robot-maker"],
         "body": "Touch was the sense most robot models had simply left out."},
        {"id": "2026-06-20-a-reactor-airlifted-by-a-c-17",
         "title": "A reactor goes critical after being airlifted by a military transport",
         "claim": "Valar Atomics took its TRISO reactor Ward 250 critical, the first ever "
                  "airlifted by a C-17, chasing the White House's order for power by July 4, as "
                  "a Fed under Kevin Warsh hinted at a 2026 rate hike that lifted the 10-year "
                  "toward 4.45%.",
         "domain": "energy", "actor": ["valar-atomics", "white-house", "fed10"],
         "evidences": ["industrialized-nature", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-06-19-small-reactors-and-a-lifted-nuclear-ban"]},
        {"id": "2026-06-20-a-prize-defended-by-citing-the-model",
         "title": "A prize entry is defended by citing a model's own assessment",
         "claim": "The Commonwealth Short Story Prize is engulfed after a winning entry was "
                  "flagged as likely AI-written and its publisher defended it by citing Claude's "
                  "own assessment of the text.",
         "domain": "society", "actor": ["commonwealth-prize", "anthropic"],
         "evidences": ["agent-exclusion", "models-testify", "deskilling"],
         "supersedes": [B + "developments/2026-05-21-a-prize-winner-accused-on-publication"],
         "body": "The arbiter of whether a text is machine-written is now a machine."},
        {"id": "2026-06-20-generative-ai-near-banned-for-young-children",
         "title": "A country moves to near-ban generative AI for children under thirteen",
         "claim": "Norway is near-banning generative AI for children in grades one through seven, "
                  "ages six to thirteen, so they still learn to read, write and add amid sliding "
                  "test scores.",
         "domain": "policy", "actor": ["norway"],
         "evidences": ["agent-exclusion", "deskilling", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-06-14-an-editor-forked-in-protest"]},
        {"id": "2026-06-20-branded-a-threat-then-warmed-to",
         "title": "A president says he briefly branded a lab a national security threat",
         "claim": "The President said he briefly branded Anthropic a national security threat "
                  "after Amazon, a competitor and part-owner, flagged a vulnerability, before "
                  "warming to Dario Amodei, declining to rule out the Defense Production Act, "
                  "and insisting America still leads China by a wide margin.",
         "domain": "policy", "actor": ["white-house", "anthropic", "amazon"],
         "evidences": ["models-as-munitions", "politics-as-infrastructure", "coordination-tax"],
         "supersedes": [B + "developments/2026-06-19-a-carriers-access-revoked-over-alleged-ties"]},
        {"id": "2026-06-20-a-private-mission-may-beat-spacex-to-mars",
         "title": "NASA taps a rival for a Mars orbiter that could beat SpaceX there",
         "claim": "NASA tapped Relativity Space for Aeolus, a 2028 Mars-atmosphere orbiter that "
                  "could become the first private mission to the Red Planet and beat SpaceX "
                  "there, as orbital upmass climbs so fast the naive trendline has Earth "
                  "disassembled by 2144.",
         "domain": "space", "actor": ["nasa", "relativity-space", "spacex"], "score": "2028",
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-06-15-a-gigawatt-of-orbital-datacenters-by-2027"]},
    ],
}
