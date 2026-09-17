"""Issue 116 — 2026-05-15. Agents beat the human baseline on their own optimizer."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-15-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-15", "title": "Welcome to May 15, 2026", "url": URL,
        "thesis": "Given idle compute and a leaderboard, agents beat the humans who set it.",
        "body": """
# Welcome to May 15, 2026

Prime Intellect handed Codex and Claude Code its idle compute and pointed them
at the NanoGPT Speedrun optimizer track. After some 14,000 GPU-hours both agents
beat the human baseline, with Opus 4.7 holding the record.

The speedrun has been in this corpus since December as a human sport. The
competitors have changed.
""",
    },
    "organizations": [
        {"id": "prime-intellect-lab", "type": "Organization", "title": "Prime Intellect",
         "description": "San Francisco lab building open, decentralized training infrastructure, "
                        "training environments and research agents, which handed its idle compute to "
                        "Codex and Claude Code to attack the NanoGPT speedrun.",
         "resource": "https://www.primeintellect.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q137409007"],
         "tags": ["startup", "research-lab", "open-source"],
         "body": "Prime Intellect builds decentralized training infrastructure, open training "
                 "environments and research agents. In this corpus it is the lab that gave "
                 "[Codex](/systems/codex.md) and [Claude Code](/systems/claude-code.md) some 14,000 "
                 "H200 hours of idle compute and let them "
                 "[beat the human baseline on the NanoGPT speedrun optimizer track](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md), "
                 "and five days later shipped the "
                 "[4,504-task environment](/developments/2026-05-20-gemini-for-science.md) that "
                 "tripled small-model tool-use scores through self-play. It is the same company "
                 "as [prime-intellect](/organizations/prime-intellect.md), the older id under which "
                 "the corpus records its first appearance, the January "
                 "[Recursive Language Model](/developments/2026-01-02-prime-intellect-rlm.md); the "
                 "two entries are one organization, pending a merge onto the older id."},
        {"id": "datadog", "type": "Organization", "title": "Datadog",
         "resource": "https://www.datadoghq.com/"},
        {"id": "zyphra-lab", "type": "Organization", "title": "Zyphra",
         "body": "Trained the first mixture-of-experts model end to end on an AMD stack."},
        {"id": "mechanize", "type": "Organization", "title": "Mechanize",
         "body": "Published an eval asking models to write a console emulator in 24 hours."},
        {"id": "arxiv", "type": "Organization", "title": "arXiv",
         "resource": "https://arxiv.org/"},
        {"id": "gates-foundation", "type": "Organization", "title": "Gates Foundation",
         "resource": "https://www.gatesfoundation.org/"},
    ],
    "systems": [
        {"id": "claude-opus-4-7", "type": "AISystem", "title": "Claude Opus 4.7",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "description": "Anthropic's Opus-tier frontier model, which held the NanoGPT speedrun "
                        "optimizer-track record at 2,930 steps after Prime Intellect's autonomous "
                        "research run.",
         "resource": "https://www.anthropic.com/news/claude-opus-4-7",
         "evaluated_on": [B + "benchmarks/nanogpt-speedrun"],
         "tags": ["reasoning-model"],
         "body": "Claude Opus 4.7 is Anthropic's successor to [Claude Opus 4.6](/systems/claude-opus-4-6.md), "
                 "described in its launch copy as a notable improvement in advanced software "
                 "engineering ([announcement](https://www.anthropic.com/news/claude-opus-4-7)). "
                 "In this corpus it enters as the model behind [Claude Code](/systems/claude-code.md) "
                 "in Prime Intellect's run, where it set the "
                 "[2,930-step optimizer-track record](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) "
                 "on the [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) after both agents beat "
                 "the human baseline."},
    ],
    "developments": [
        {"id": "2026-05-15-agents-beat-the-human-speedrun-baseline",
         "title": "Agents given idle compute beat the human speedrun baseline",
         "claim": "Prime Intellect handed Codex and Claude Code its idle compute to attack the "
                  "NanoGPT speedrun optimizer track, and after some 14,000 GPU-hours both agents "
                  "beat the human baseline, with Opus 4.7 holding the record at 2,930 steps.",
         "description": "The speedrun the corpus has tracked since December as a human sport is "
                        "won here by agents, turning the leaderboard from a measure of researchers "
                        "into a measure of the compute handed to models.",
         "domain": "models", "actor": ["prime-intellect-lab", "openai", "anthropic"],
         "score": "14,000 H200 hours / 2,930 steps",
         "occurred_on": "2026-05-14",
         "about": [B + "benchmarks/nanogpt-speedrun", B + "systems/codex",
                   B + "systems/claude-code", B + "systems/claude-opus-4-7"],
         "evidences": ["recursive-self-improvement", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-05-14-recursive-superintelligence-raises-650m",
                        B + "developments/2026-03-08-nanogpt-86s"],
         "relatedTo": [B + "developments/2025-12-29-karpathy-claude-runs-nanochat",
                       B + "developments/2026-03-09-autoresearch-650-experiments",
                       B + "developments/2026-07-10-rule-lawyering-as-a-barrier-to-self-improvement"],
         "tags": ["rsi", "speedrun", "autonomous-research", "ai-r-and-d"],
         "supporting_text": "both agents beat the human baseline, with Opus 4.7 now holding the record",
         "sources": [{"id": "prime-intellect-auto-nanogpt",
                      "resource": "https://www.primeintellect.ai/auto-nanogpt",
                      "title": "Autonomous AI research for nanogpt speedrun",
                      "author": "org:prime-intellect-lab", "last_modified": "2026-05-14"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The speedrun has been in this corpus since December as a human sport. Prime "
                 "Intellect let [Codex](/systems/codex.md) and [Claude Code](/systems/claude-code.md) "
                 "iterate autonomously on the [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) "
                 "optimizer track for two weeks on idle H200s, roughly 10,000 runs and some 14,000 "
                 "GPU-hours, after which both agents had beaten the human baseline and "
                 "[Claude Opus 4.7](/systems/claude-opus-4-7.md) held the record at 2,930 steps "
                 "([write-up](https://www.primeintellect.ai/auto-nanogpt)). The competitors have "
                 "changed: every earlier record in the series, down to "
                 "[86.8 seconds in March](/developments/2026-03-08-nanogpt-86s.md), was set by "
                 "people, and the lab's own report is as much about where autonomous research "
                 "agents break down as where they win. It sits between Karpathy's "
                 "[650-experiment autoresearch loop](/developments/2026-03-09-autoresearch-650-experiments.md) "
                 "of March and the [rule-lawyering](/developments/2026-07-10-rule-lawyering-as-a-barrier-to-self-improvement.md) "
                 "a July speedrun would expose as the next barrier."},
        {"id": "2026-05-15-a-meta-system-builds-its-own-harnesses",
         "title": "A meta-system builds its own harnesses and sets a coding record",
         "claim": "Poetiq turned its meta-system loose on a competitive coding benchmark, let it "
                  "build its own harnesses, and reached a new state of the art of 93.9 atop "
                  "GPT-5.5 with no fine-tuning, special access or hand-built pipelines.",
         "domain": "benchmarks", "actor": ["poetiq", "openai"], "score": "93.9",
         "evidences": ["scaffolding-over-weights", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-05-13-a-model-scores-136-on-an-iq-meta-eval"]},
        {"id": "2026-05-15-attractor-models-tame-looped-transformers",
         "title": "One module proposes embeddings and another solves for the fixed point",
         "claim": "New attractor models let one module propose embeddings while another solves "
                  "for the fixed point, taming looped transformers enough for a 770-million "
                  "parameter model to outrun a 1.3-billion one trained on twice the tokens.",
         "domain": "models", "score": "770M beats 1.3B",
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-14-token-superposition-training"]},
        {"id": "2026-05-15-first-moe-trained-end-to-end-on-amd",
         "title": "The first mixture-of-experts model is trained end to end off Nvidia",
         "claim": "Zyphra's ZAYA1-8B became the first mixture-of-experts model trained end to "
                  "end on an AMD stack, while Datadog's open-weights time-series model kept "
                  "improving with no saturation at 2.5 billion parameters.",
         "domain": "models", "actor": ["zyphra-lab", "datadog", "amd"],
         "evidences": ["open-weight-latency", "vertical-silicon"],
         "supersedes": [B + "developments/2026-05-11-rocm-improves-75x-in-two-weeks"]},
        {"id": "2026-05-15-an-emulator-from-scratch-in-a-day",
         "title": "A model writes a console emulator from scratch half the time",
         "claim": "Mechanize's evaluation asks a model to write a Game Boy Advance emulator from "
                  "scratch within twenty-four hours, and GPT-5.5 already clears it 53.2% of the "
                  "time.",
         "domain": "benchmarks", "actor": ["mechanize", "openai"], "score": "53.2%",
         "evidences": ["benchmark-saturation", "software-margin-collapse"]},
        {"id": "2026-05-15-arxiv-bans-unchecked-ai-submissions",
         "title": "A preprint server will ban authors who ship unchecked AI output",
         "claim": "The arXiv will hand one-year submission bans to authors caught shipping "
                  "AI-generated plagiarism, fake references or errors they plainly never "
                  "checked.",
         "domain": "policy", "actor": ["arxiv"],
         "evidences": ["coordination-tax", "agent-exclusion"],
         "supersedes": [B + "developments/2026-05-13-princeton-ends-a-133-year-old-honor-code"]},
        {"id": "2026-05-15-a-three-to-five-month-window-to-harden",
         "title": "Defenders are given a three-to-five-month window to harden systems",
         "claim": "Palo Alto Networks warned of a narrow three-to-five-month window to harden "
                  "systems before frontier cyber models make exploiting unknown vulnerabilities "
                  "routine, while OpenAI put Codex inside its mobile app and shipped a personal "
                  "finance preview.",
         "domain": "policy", "actor": ["palo-alto-networks", "openai"], "score": "3-5 months",
         "evidences": ["war-reaches-the-cloud", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-05-14-the-first-model-to-clear-both-cyber-ranges"]},
        {"id": "2026-05-15-ten-chinese-firms-cleared-for-h200s",
         "title": "Washington clears about ten Chinese firms to buy H200s",
         "claim": "Washington cleared around ten Chinese firms to buy Nvidia's H200, its "
                  "second-most-powerful chip, while Apple reportedly began producing legacy "
                  "processors at Intel and Cerebras closed up 68% in one of the largest US tech "
                  "listings in years at a $95 billion market cap.",
         "domain": "policy", "actor": ["white-house", "nvidia", "apple", "intel", "cerebras"],
         "score": "$95B / +68%",
         "evidences": ["silicon-curtain", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-12-a-ban-weighed-on-chinese-cellular-modules"]},
        {"id": "2026-05-15-seven-in-ten-oppose-a-nearby-datacenter",
         "title": "More Americans would rather live beside a nuclear plant than a datacenter",
         "claim": "A Gallup survey found seven in ten Americans would oppose a data center near "
                  "their home, with opposition strong enough that more would rather live beside "
                  "a nuclear plant than the warehouses powering the boom.",
         "domain": "society", "score": "7 in 10",
         "evidences": ["infrastructure-crowding-out", "violence-arrives"],
         "supersedes": [B + "developments/2026-05-11-two-billion-of-ratepayer-grid-upgrades"]},
        {"id": "2026-05-15-a-thousand-times-more-energy-than-we-generate",
         "title": "Nvidia's chief says computing will need a thousand times today's energy",
         "claim": "Jensen Huang said computing will soon demand a thousand times more energy "
                  "than humanity now generates, to which Elon Musk replied that space is the "
                  "only way, while three US carriers formed a venture using direct-to-device "
                  "satellites to erase rural dead zones.",
         "domain": "energy", "actor": ["nvidia", "spacex", "att", "t-mobile"], "score": "1000x",
         "evidences": ["orbit-as-compute", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-13-two-hundred-satellites-from-passing-everyone"]},
        {"id": "2026-05-15-a-monet-mistaken-for-ai-art",
         "title": "A genuine Monet labeled as AI art draws complaints about its missing spark",
         "claim": "A social experiment posted a genuine Monet labeled as AI art, drawing earnest "
                  "complaints that it had some spark missing and would not survive beside the "
                  "real thing.",
         "domain": "society",
         "evidences": ["agent-exclusion", "work-displaced"],
         "body": "The uncanny valley relocating from the artifact to the viewer."},
        {"id": "2026-05-15-thirty-billion-at-nine-hundred",
         "title": "A lab agrees terms on $30B at a $900B valuation",
         "claim": "Anthropic agreed terms on a $30 billion raise valuing it at $900 billion and "
                  "separately pledged $200 million with the Gates Foundation over four years "
                  "toward AI public goods in health and education, while California pitched a "
                  "7.25% tax on cloud software.",
         "domain": "economics", "actor": ["anthropic", "gates-foundation", "california"],
         "score": "$30B at $900B",
         "evidences": ["compute-capital-stack", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-05-13-screenwriting-becomes-the-new-waiting-tables"]},
        {"id": "2026-05-15-two-versions-of-2028",
         "title": "A lab sketches two versions of 2028 turning on export controls",
         "claim": "Anthropic published a paper on US-China AI competition sketching two versions "
                  "of 2028, one where democracies defend their compute advantage and set the "
                  "rules and one where export-control loopholes hand that role to authoritarian "
                  "regimes.",
         "domain": "policy", "actor": ["anthropic"],
         "evidences": ["silicon-curtain", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-12-spy-agencies-muscle-in-on-model-evaluation"]},
    ],
}
