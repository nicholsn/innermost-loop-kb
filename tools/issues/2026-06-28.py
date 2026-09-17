"""Issue 150 — 2026-06-28. No ceiling, only a horizon."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-28-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-28", "title": "Welcome to June 28, 2026", "url": URL,
        "thesis": "The plateau moves out of sight.",
        "body": """
# Welcome to June 28, 2026

OpenAI's Noam Brown notes the plateau is actually really far out these days,
with a well-scaffolded GPT-5.5 able to think for weeks before benchmarks
flatten. Scaffolding, not scale, buys the depth.

A lone PhD synthesized the first selective GalR1 antagonist for Alzheimer's in
a garage lab run by Claude Code and a liquid-handling robot.
""",
    },
    "themes": [
        {"id": "garage-scale-discovery", "type": "Theme",
         "title": "Frontier science from a garage",
         "first_seen": "2026-06-28", "domain": "science",
         "body": "The capital stack that once gated a novel compound — a lab, a team, "
                 "a institution — collapses to one person, an agent and a liquid "
                 "handler. Discovery stops being rate-limited by who you work for."},
    ],
    "organizations": [
        {"id": "qihoo-360", "type": "Organization", "title": "360 Security"},
        {"id": "general-fusion", "type": "Organization", "title": "General Fusion"},
        {"id": "agibot", "type": "Organization", "title": "AGIBOT"},
        {"id": "seti", "type": "Organization", "title": "SETI Institute"},
    ],
    "developments": [
        {"id": "2026-06-28-the-plateau-is-really-far-out",
         "title": "A researcher says the plateau is far out with enough scaffolding",
         "claim": "OpenAI's Noam Brown noted the plateau is actually really far out these days, "
                  "with a well-scaffolded GPT-5.5 able to think for weeks before benchmarks "
                  "flatten, while Nous Research exposed mixture-of-agent presets as virtual "
                  "models claiming to beat Opus 4.8 by 8% and GPT-5.5 by 11%.",
         "domain": "models", "actor": ["openai", "nous-research"], "score": "+8% / +11%",
         "evidences": ["scaffolding-over-weights", "monoculture-is-the-vulnerability",
                       "takeoff-declared"],
         "supersedes": [B + "developments/2026-06-27-the-open-gap-closing-to-zero"]},
        {"id": "2026-06-28-a-trillion-six-parameter-open-model",
         "title": "An MIT-licensed model folds 1.6 trillion parameters into a tenth the KV cache",
         "claim": "DeepSeek's MIT-licensed V4-Pro-DSpark folds 1.6 trillion parameters and a "
                  "million-token context into speculative decoding that sips a tenth the KV "
                  "cache, as a field guide crowned DeepSeek, GLM 5.2, MiniMax M3 and Nemotron 3 "
                  "Ultra frontier-class coders holding the same three-to-six-month gap they have "
                  "kept for eighteen months.",
         "domain": "models", "actor": ["deepseek", "zai", "minimax", "nvidia"],
         "score": "1.6T params / 10% KV cache",
         "evidences": ["open-weight-latency", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-06-28-the-plateau-is-really-far-out"]},
        {"id": "2026-06-28-two-models-paired-by-comparative-advantage",
         "title": "A company pairs two frontier models by comparative advantage",
         "claim": "Shopify's CTO found GPT-5.6 beats Opus at everything yet still cedes coding to "
                  "Fable 5, pairing them so Fable writes code while 5.6 runs experiments.",
         "domain": "agents", "actor": ["shopify", "openai", "anthropic"],
         "evidences": ["monoculture-is-the-vulnerability", "spiky-frontier"],
         "supersedes": [B + "developments/2026-06-22-orchestration-as-export-control-arbitrage"]},
        {"id": "2026-06-28-rivals-fill-the-mythos-shaped-hole",
         "title": "Chinese and Japanese labs ship models to fill the gap left by a ban",
         "claim": "As the export ban dragged on, China's 360 shipped Tulongfeng and Tokyo's "
                  "Sakana shipped Fugu to fill the Mythos-shaped hole, with Chinese systems "
                  "reportedly matching Mythos in cybersecurity.",
         "domain": "policy", "actor": ["qihoo-360", "sakana-ai-lab", "anthropic"],
         "evidences": ["routing-around-the-ban", "silicon-curtain", "frontier-moves-backward"],
         "supersedes": [B + "developments/2026-06-27-a-tiered-planet-of-model-access"],
         "body": "One analyst warned the real fallout is China waking up: a state on the "
                 "receiving end of NSA-embedded offensive operations stops believing it "
                 "is four months behind and starts sprinting."},
        {"id": "2026-06-28-ai-spend-halved-by-routing-and-caching",
         "title": "A company nearly halves AI spend while usage soars",
         "claim": "Coinbase's Brian Armstrong nearly halved AI spend while usage soared, using "
                  "cheaper defaults, smarter routing and warm caches rather than usage caps, in "
                  "one case dragging a cache hit rate from 5% to 60%.",
         "domain": "economics", "actor": ["coinbase"], "score": "5% to 60% cache hits",
         "evidences": ["reasoning-price-deflation", "routing-around-the-ban"],
         "supersedes": [B + "developments/2026-06-13-a-consultancy-report-padded-with-hallucinations"]},
        {"id": "2026-06-28-the-creator-no-longer-writes-his-own-prompts",
         "title": "A tool's creator no longer writes his own prompts",
         "claim": "Engineers are leaning into loop engineering so completely that Claude Code's "
                  "creator no longer writes his own prompts — Claude does — while Gartner expects "
                  "AI coding costs to outrun the average developer's salary by 2028.",
         "domain": "agents", "actor": ["anthropic", "gartner"], "score": "costs > salary by 2028",
         "evidences": ["self-authored-scaffolding", "botsitting", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-06-27-agents-optimize-the-scientist-not-the-experiment"]},
        {"id": "2026-06-28-nine-billion-toward-a-2029-quantum-machine",
         "title": "A company pledges $9B over five years toward a 2029 quantum machine",
         "claim": "IBM seeded its Anderon foundry with $2 billion, half from Washington, and "
                  "pledged $9 billion more over five years toward its 2029 Starling machine.",
         "domain": "compute", "actor": ["ibm", "anderon", "white-house"], "score": "$9B / 2029",
         "evidences": ["science-as-industrial-policy", "vertical-silicon"],
         "supersedes": [B + "developments/2026-06-24-two-quantum-executive-orders"]},
        {"id": "2026-06-28-a-hyperscaler-throttles-another-hyperscaler",
         "title": "A hyperscaler throttles a rival's model access over scarcity",
         "claim": "Compute is so scarce that Google throttled Meta's Gemini access after Meta "
                  "asked for more than it could spare, while Masayoshi Son bet against orbital "
                  "data centers, asking what the point is when power is barely 7% of operating "
                  "cost and orbit is a decade too slow.",
         "domain": "compute", "actor": ["google", "meta", "softbank"], "score": "power = 7% of opex",
         "evidences": ["infrastructure-crowding-out", "orbit-as-compute", "coordination-tax"],
         "supersedes": [B + "developments/2026-06-27-reserved-gpu-prices-raised-twenty-percent"]},
        {"id": "2026-06-28-plasma-tripled-by-mechanical-squeeze",
         "title": "A fusion prototype triples its plasma by mechanical compression alone",
         "claim": "General Fusion tripled its plasma to 8.4 million degrees by mechanical squeeze "
                  "alone, as renewables reached 30% of US generation with solar overtaking wind.",
         "domain": "energy", "actor": ["general-fusion"], "score": "8.4M degrees / 30% renewable",
         "evidences": ["industrialized-nature", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-06-25-compute-becomes-an-exchange-traded-commodity"]},
        {"id": "2026-06-28-a-three-hundred-dollar-wristband-teaches-robot-hands",
         "title": "A $300 wristband teaches robots force-aware hands from muscle signals",
         "claim": "A $300 wristband called ForceBand teaches robots force-aware hands from human "
                  "muscle signals, hitting 87% on pick, squeeze and place, while AGIBOT rolled "
                  "out its 15,000th robot holding a 39% share of humanoid shipments.",
         "domain": "robotics", "actor": ["agibot"], "score": "$300 / 87% / 15,000 robots",
         "evidences": ["world-models-beat-vlas", "physical-recursion", "data-beyond-text"],
         "supersedes": [B + "developments/2026-06-25-a-humanoid-platform-given-away"]},
        {"id": "2026-06-28-an-unmanned-shield-of-two-hundred-thousand-drones",
         "title": "A government budgets for an unmanned shield of 208,200 attack drones",
         "claim": "Taiwan budgeted $6.6 billion for an unmanned shield of 208,200 one-way attack "
                  "drones, while in a national first a Sacramento sheriff's drone used a magnet "
                  "to lift a knife from a suspect's hand before deputies moved in.",
         "domain": "robotics", "actor": ["taiwan"], "score": "$6.6B / 208,200 drones",
         "evidences": ["violence-arrives", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-06-26-doctrine-lets-ai-initiate-wartime-actions"]},
        {"id": "2026-06-28-an-erdos-problem-formalized-at-unprecedented-scale",
         "title": "An Erdős problem falls and holds across 180,000 lines of formal proof",
         "claim": "Erdős problem #870 fell to GPT-5.5-Pro, then held up across 180,000 sorry-free "
                  "lines of Lean 4, a scale of formalization no one had attempted before.",
         "domain": "science", "actor": ["openai"], "score": "180,000 lines of Lean",
         "evidences": ["proof-priced-per-unit", "automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-06-25-a-physicist-credits-a-model-in-a-paper"]},
        {"id": "2026-06-28-a-novel-alzheimers-compound-from-a-garage",
         "title": "A lone researcher synthesizes a novel Alzheimer's compound in a garage lab",
         "claim": "A lone PhD synthesized PAC-832, the first selective GalR1 antagonist for "
                  "Alzheimer's, in a garage lab run by Claude Code and a liquid-handling robot.",
         "domain": "biotech", "actor": ["anthropic"],
         "evidences": ["garage-scale-discovery", "one-person-company", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-26-an-ai-designed-antibody-clears-early-safety"]},
    ],
}
