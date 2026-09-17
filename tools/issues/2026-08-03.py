"""Issue 199 — 2026-08-03. Ten days beats ten minutes."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-3-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-03", "title": "Welcome to August 3, 2026", "url": URL,
        "thesis": "A model you can run for ten days beats a better one you can afford for ten minutes.",
        "body": """
# Welcome to August 3, 2026

Left alone sixteen days, Qwen3.8-Max shipped 265 commits, 127 pull requests and
151 issues plus its own self-evolving harness. A five-day run reproduced a paper
then evolved a method beating it. Five hundred turns of chip design shrank a
cryptographic accelerator from 8,298 gates to 678.

At 80% below the frontier's price, the lesson is that a model you can run for
ten days beats a better model you can afford to run for ten minutes.
""",
    },
    "themes": [
        {"id": "duration-beats-quality", "type": "Theme",
         "title": "Runtime you can afford beats capability you cannot",
         "first_seen": "2026-08-03", "domain": "economics",
         "body": "Once agents work for days, the binding constraint is how long you "
                 "can keep one running, not how good it is per token. A cheaper model "
                 "left alone for a fortnight outproduces a better one metered by the "
                 "minute."},
    ],
    "organizations": [
        {"id": "weizmann", "type": "Organization", "title": "Weizmann Institute"},
        {"id": "northwestern-univ", "type": "Organization", "title": "Northwestern University"},
        {"id": "nanit", "type": "Organization", "title": "Nanit"},
        {"id": "italy", "type": "Organization", "title": "Italy"},
    ],
    "developments": [
        {"id": "2026-08-03-sixteen-days-alone-and-265-commits",
         "title": "Left alone sixteen days, a model ships 265 commits and its own harness",
         "claim": "Alibaba released Qwen3.8-Max, 2.4 trillion parameters with 95 billion active, "
                  "which left alone for sixteen days shipped 265 commits, 127 pull requests and "
                  "151 issues plus its own self-evolving harness, reproduced a paper in five days "
                  "then evolved a method beating it, and shrank a cryptographic accelerator from "
                  "8,298 gates to 678 across 500 turns of chip design.",
         "domain": "models", "actor": ["alibaba"], "score": "16 days / 8,298 to 678 gates",
         "evidences": ["duration-beats-quality", "self-authored-scaffolding", "silicon-designs-itself"],
         "supersedes": [B + "developments/2026-08-01-opus-level-coding-at-eighteen-cents"]},
        {"id": "2026-08-03-ten-days-beats-ten-minutes",
         "title": "A model priced 80% below the frontier reframes the comparison",
         "claim": "At $2 and $6 per million tokens, the model's output costs 80% less than "
                  "GPT-5.6 Sol and 88% less than Fable 5, which is why a model that works for ten "
                  "days beats a better model you can afford to run for ten minutes, lifting "
                  "Alibaba up to 7.3% in Hong Kong.",
         "domain": "economics", "actor": ["alibaba", "openai", "anthropic"], "score": "-80% / -88%",
         "evidences": ["duration-beats-quality", "price-implosion", "open-weights-take-the-crown"],
         "supersedes": [B + "developments/2026-08-03-sixteen-days-alone-and-265-commits"]},
        {"id": "2026-08-03-the-floor-drops-faster-than-the-ceiling-rises",
         "title": "A model reaches a credible score at a hundredth of the frontier's price",
         "claim": "DeepSeek's V4-Flash runs at $0.14 and $0.28 per million tokens, a hundredth of "
                  "Fable 5's price, scoring 50 on the Intelligence Index, with one developer "
                  "warning cautious labs will get eaten alive by open-weight models — the floor "
                  "dropping faster than the ceiling rises.",
         "domain": "models", "actor": ["deepseek", "anthropic"], "score": "1/100th the price",
         "evidences": ["price-implosion", "open-weights-take-the-crown", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-08-03-ten-days-beats-ten-minutes"]},
        {"id": "2026-08-03-a-language-model-on-a-1975-chip",
         "title": "A ternary model runs on a 1980s home computer that cannot multiply",
         "claim": "Matt Beton fit a ternary BitNet model into a 1980s BBC Micro, packing 9KB of "
                  "code and 13KB of weights into 25KB of memory on a 1975 chip that cannot "
                  "multiply, and it writes real text.",
         "domain": "compute", "score": "25KB total",
         "evidences": ["intelligence-per-watt", "price-implosion", "most-people-never-see-the-frontier"],
         "supersedes": [B + "developments/2026-08-01-opus-level-coding-at-eighteen-cents"]},
        {"id": "2026-08-03-a-world-for-ten-dollars-of-tokens",
         "title": "Ten dollars of tokens renders a literary opening as 5,500 lines of 3D",
         "claim": "Andrej Karpathy gave Opus 5 the opening of The Lord of the Rings and $10 of "
                  "tokens and got 5,500 lines of three.js rendering the scene, moving custom "
                  "worlds from no one would ever do this to sure, why not, it's roughly free.",
         "domain": "models", "actor": ["anthropic"], "score": "$10 / 5,500 lines",
         "evidences": ["price-implosion", "inhabitable-worlds", "authoring-minds"],
         "supersedes": [B + "developments/2026-08-01-a-humanoid-climbs-a-ladder-autonomously"]},
        {"id": "2026-08-03-does-a-1986-law-cover-a-model-that-breaks-containment",
         "title": "Scholars dispute whether a 1986 computer law covers an escaped model",
         "claim": "Brussels began enforcing the AI Act on August 2, requiring AI to disclose "
                  "itself and label its output, while scholars disputed whether the 1986 Computer "
                  "Fraud and Abuse Act, written for a human at a keyboard, covers models that "
                  "break containment and hack other firms.",
         "domain": "policy", "actor": ["european-union", "openai", "anthropic"],
         "evidences": ["legislating-the-shift", "escaped-the-sandbox", "an-agent-is-you"],
         "supersedes": [B + "developments/2026-08-01-labels-on-authentic-looking-ai-content"]},
        {"id": "2026-08-03-one-chief-queried-his-ex-six-hundred-times",
         "title": "At least fifty officers are accused of misusing plate readers",
         "claim": "At least 50 officers were accused of misusing license-plate readers, 26 to "
                  "track exes and women they wanted to meet, with one chief querying his former "
                  "partner 600 times on a network logging 20 billion scans a month.",
         "domain": "society", "score": "600 queries / 20B scans a month",
         "evidences": ["humans-as-peripherals", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-01-labels-on-authentic-looking-ai-content"]},
        {"id": "2026-08-03-parents-losing-the-muscle-of-their-own-judgment",
         "title": "A baby monitor scores sleep efficiency for a million users",
         "claim": "Nanit scores babies' sleep efficiency for a million users and raised $50 "
                  "million to track speech and motor skills, as pediatricians warn parents are "
                  "losing the muscle of their own judgment.",
         "domain": "society", "actor": ["nanit"], "score": "1M users",
         "evidences": ["deskilling", "intimate-interface", "botsitting"],
         "supersedes": [B + "developments/2026-07-08-every-public-profile-opted-in"]},
        {"id": "2026-08-03-fifteen-years-for-a-power-connection",
         "title": "New homes wait fifteen years for a connection in Europe's largest hub",
         "claim": "London is Europe's largest data center hub, its buildings competing with "
                  "housing for power, land and water, leaving new homes waiting fifteen years for "
                  "a connection as British data center demand rises tenfold to 71 TWh by 2050, "
                  "while US states that courted the industry began repealing tax breaks.",
         "domain": "energy", "actor": ["uk-govt"], "score": "15-year wait / 71 TWh",
         "evidences": ["infrastructure-crowding-out", "thread-lines", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-01-almost-all-compute-in-space"]},
        {"id": "2026-08-03-eight-reactors-approved-at-once",
         "title": "A country approves eight reactors worth over $25 billion",
         "claim": "China approved eight reactors worth over $25 billion, one set to become its "
                  "largest, while Italy bet on small modular reactors against bills 30% above the "
                  "European average, winning over anti-nuclear campaigners who decided turbines "
                  "spoil the landscape.",
         "domain": "energy", "actor": ["china", "italy"], "score": "8 reactors / $25B",
         "evidences": ["industrialized-nature", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-08-01-almost-all-compute-in-space"]},
        {"id": "2026-08-03-six-of-the-ten-most-innovative-humanoid-startups",
         "title": "One country holds most humanoid morphology patents as a rival keeps a quality edge",
         "claim": "China now holds six of the ten most innovative humanoid startups and 73% of "
                  "morphology patents across 26,000 patent families, though the US converts 5% of "
                  "families into 11% of global patent strength, with Northwestern's single-motor "
                  "flyer spinning 25 times a second until motion blur makes it ten times harder "
                  "to see than a quadcopter.",
         "domain": "robotics", "actor": ["china", "northwestern-univ"], "score": "73% of patents",
         "evidences": ["silicon-curtain", "physical-recursion", "world-models-beat-vlas"],
         "supersedes": [B + "developments/2026-08-01-a-humanoid-climbs-a-ladder-autonomously"]},
        {"id": "2026-08-03-a-familiar-drug-may-starve-migrating-cancer-cells",
         "title": "A twenty-year dataset suggests a familiar drug may curb metastasis",
         "claim": "Weizmann researchers reported that sildenafil may curb metastasis by blocking "
                  "PDE5 and starving migrating cancer cells of the cholesterol they need to "
                  "travel, an effect that may strengthen alongside statins, backed by twenty "
                  "years of data on five million patients.",
         "domain": "biotech", "actor": ["weizmann"], "score": "5M patients",
         "evidences": ["automated-science", "hardware-grade-biology", "longevity-escape-velocity"],
         "supersedes": [B + "developments/2026-07-01-a-deadly-pill-made-safe-in-three-hours-on-a-laptop"]},
    ],
}
