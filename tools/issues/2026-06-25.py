"""Issue 147 — 2026-06-25. The agent rewrites its own scaffolding."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-25-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-25", "title": "Welcome to June 25, 2026", "url": URL,
        "thesis": "An agent mines its own weaknesses and rewrites its harness.",
        "body": """
# Welcome to June 25, 2026

A new Self-Harness paradigm lets an agent mine its own weaknesses and rewrite
its scaffolding, lifting Terminal-Bench scores by double digits with no human
engineers in the loop.

And Ed Witten, for the first time, credited Claude Opus 4.8 with generalizing
an entanglement-wedge calculation.
""",
    },
    "themes": [
        {"id": "self-authored-scaffolding", "type": "Theme",
         "title": "The harness writes itself",
         "first_seen": "2026-06-25", "domain": "agents",
         "body": "The scaffolding around a model — its tools, prompts and control "
                 "flow — had been the last reliably human-authored layer. When the "
                 "agent mines its own failures and rewrites that layer, improvement "
                 "closes a loop that needs no engineer."},
    ],
    "organizations": [
        {"id": "krea", "type": "Organization", "title": "Krea"},
        {"id": "bio-iq", "type": "Organization", "title": "Bio IQ"},
        {"id": "sunrun", "type": "Organization", "title": "Sunrun"},
        {"id": "slate-auto", "type": "Organization", "title": "Slate Auto"},
        {"id": "centessa", "type": "Organization", "title": "Centessa"},
        {"id": "intercept-org", "type": "Organization", "title": "Intercept"},
        {"id": "terrasse-vaudreuil", "type": "Organization", "title": "Terrasse-Vaudreuil"},
    ],
    "developments": [
        {"id": "2026-06-25-an-agent-rewrites-its-own-harness",
         "title": "An agent mines its weaknesses and rewrites its own scaffolding",
         "claim": "A new Self-Harness paradigm lets an agent mine its own weaknesses and rewrite "
                  "its scaffolding, lifting Terminal-Bench scores by double digits with no human "
                  "engineers involved.",
         "domain": "agents",
         "evidences": ["self-authored-scaffolding", "recursive-self-improvement",
                       "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-06-24-skills-that-write-themselves"]},
        {"id": "2026-06-25-a-physicist-credits-a-model-in-a-paper",
         "title": "A leading physicist credits a model with generalizing a calculation",
         "claim": "Ed Witten for the first time credited Claude Opus 4.8 with generalizing an "
                  "entanglement-wedge calculation.",
         "domain": "science", "actor": ["anthropic"],
         "evidences": ["automated-science", "humans-mine-the-machine", "root-node-problems"],
         "supersedes": [B + "developments/2026-06-20-a-bronze-age-script-cracked"]},
        {"id": "2026-06-25-a-language-that-composes-dna-rna-and-protein",
         "title": "A model composes DNA, RNA and proteins into validated designs",
         "claim": "Stanford's Brian Hie unveiled Proto, a language composing DNA, RNA and "
                  "proteins into validated designs, while NVIDIA's BioNeMo Agent Toolkit turned "
                  "biomolecular models into callable skills and Bio IQ launched life-science and "
                  "biosecurity leaderboards.",
         "domain": "biotech", "actor": ["stanford", "nvidia", "bio-iq"],
         "evidences": ["compiling-matter", "hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-06-24-antibodies-designed-and-tested-in-six-weeks"]},
        {"id": "2026-06-25-the-largest-known-distillation-attack",
         "title": "A lab accuses a rival of harvesting 28.8 million exchanges",
         "claim": "Anthropic accused Alibaba's Qwen of the largest known distillation attack, "
                  "28.8 million harvested exchanges, while Cloudflare and the major browsers "
                  "build personhood tokens to sort humans and authorized bots from malicious "
                  "traffic.",
         "domain": "models", "actor": ["anthropic", "alibaba", "cloudflare"],
         "score": "28.8M exchanges",
         "evidences": ["bots-outnumber-us", "silicon-curtain", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-06-22-orchestration-as-export-control-arbitrage"]},
        {"id": "2026-06-25-labs-hire-philosophers-to-write-constitutions",
         "title": "Frontier labs hire philosophers to write AI constitutions",
         "claim": "Frontier labs are now hiring philosophers to write AI constitutions, while "
                  "two more Gemini staffers were poached by Anthropic and an audit found ChatGPT "
                  "mostly left-leaning, Gemini neutral, and even Grok citing the left more.",
         "domain": "models", "actor": ["anthropic", "openai", "google", "xai"],
         "evidences": ["values-negotiated-with-the-model", "doctrine-borrows-the-lab"],
         "supersedes": [B + "developments/2026-06-19-models-trained-to-describe-themselves-faithfully"]},
        {"id": "2026-06-25-a-two-point-three-trillion-chip-plan",
         "title": "Japan unveils a $2.3 trillion plan to quintuple chip output",
         "claim": "Japan's prime minister unveiled a $2.3 trillion plan to quintuple chip "
                  "output, lofting the Nikkei past 72,000, while the EU signed the US-led Pax "
                  "Silica pact against China and agreed to buy $40 billion in US chips.",
         "domain": "policy", "actor": ["japan-govt", "european-union"], "score": "$2.3T / $40B",
         "evidences": ["science-as-industrial-policy", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-24-two-quantum-executive-orders"]},
        {"id": "2026-06-25-memory-becomes-the-margin-king",
         "title": "A memory maker posts tech's highest margin at 84.9%",
         "claim": "Micron became tech's margin king at a record 84.9%, posting record revenue "
                  "and a trillion-dollar capitalization on sevenfold data growth, noting a "
                  "humanoid robot holds ten times a car's memory.",
         "domain": "economics", "actor": ["micron"], "score": "84.9% margin",
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "physical-recursion"],
         "supersedes": [B + "developments/2026-06-22-a-memory-maker-becomes-a-countrys-most-valuable-firm"]},
        {"id": "2026-06-25-an-inference-chip-taped-out-in-nine-months",
         "title": "A lab tapes out its first inference chip in nine months",
         "claim": "OpenAI and Broadcom taped out Jalapeño, OpenAI's first inference chip, in "
                  "nine months, while Qualcomm bought Modular to challenge CUDA and unveiled a "
                  "CPU with Meta as first customer.",
         "domain": "compute", "actor": ["openai", "broadcom", "qualcomm", "meta"],
         "score": "9 months to tapeout",
         "evidences": ["vertical-silicon", "silicon-designs-itself"],
         "supersedes": [B + "developments/2026-06-24-a-supercomputer-on-cpus-alone"]},
        {"id": "2026-06-25-compute-becomes-an-exchange-traded-commodity",
         "title": "A venture firm funds the first modern exchange for compute",
         "claim": "a16z funded Ornn to offer the first modern exchange for compute as a "
                  "commodity, while Sunrun, Tesla and Renew Home stitched home batteries and EVs "
                  "into 16 gigawatts of flexible capacity and Walmart signed its first nuclear "
                  "deal.",
         "domain": "economics", "actor": ["a16z", "ornn", "sunrun", "tesla", "walmart"],
         "score": "16 GW flexible",
         "evidences": ["ai-as-the-economy", "industrialized-nature", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-17-cognition-priced-like-crude"]},
        {"id": "2026-06-25-a-humanoid-platform-given-away",
         "title": "A founder open-hands a humanoid platform as too vital to gatekeep",
         "claim": "1X's Bernt Bornich is open-handing NEO to developers, calling a Western "
                  "humanoid platform too vital to gatekeep, as Amazon's Zoox revealed a "
                  "production-intent robotaxi at a hundred a week and Agility's Digit went "
                  "public via SPAC at $2.5 billion.",
         "domain": "robotics", "actor": ["1x", "zoox", "agility-robotics"], "score": "$2.5B SPAC",
         "evidences": ["open-weight-latency", "physical-recursion"],
         "supersedes": [B + "developments/2026-06-24-fifty-robots-while-workers-await-recall"]},
        {"id": "2026-06-25-brain-to-brain-through-latent-space",
         "title": "A founder says brain-to-brain telepathy may be attempted this year",
         "claim": "Elon Musk said Neuralink may attempt brain-to-brain communication through "
                  "latent space this year, while Eli Lilly closed its Centessa acquisition, "
                  "possibly betting an orexin agonist could let anyone feel rested on four "
                  "hours' sleep.",
         "domain": "biotech", "actor": ["neuralink", "eli-lilly", "centessa"],
         "evidences": ["intimate-interface", "hardware-grade-biology", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-06-17-a-voice-returned-to-a-man-with-als"]},
        {"id": "2026-06-25-orbital-manufacturing-gets-a-return-vehicle",
         "title": "A reentry capsule is deployed to corner orbital manufacturing",
         "claim": "SpaceX confirmed deployment of Starfall, a reentry capsule that could corner "
                  "global cargo return and orbital manufacturing, which rival startups cheered "
                  "as proof the market is real.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["orbit-as-compute", "compiling-matter"],
         "supersedes": [B + "developments/2026-06-03-orbital-manufacturing-cleared-for-test"]},
        {"id": "2026-06-25-a-town-grants-trees-the-right-to-life",
         "title": "A town becomes the first in Canada to recognize trees as living beings",
         "claim": "Quebec's Terrasse-Vaudreuil became the first Canadian town to recognize trees "
                  "as living beings, granting them the right to life, to natural growth, to "
                  "integrity and to regeneration.",
         "domain": "society", "actor": ["terrasse-vaudreuil"],
         "evidences": ["model-welfare", "agent-society", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-06-14-a-third-state-court-asks-whether-personhood-has-a-trunk"]},
    ],
}
