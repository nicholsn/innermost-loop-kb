"""Issue 067 — 2026-03-03. A Fields Medal proof formalized in two weeks."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-3-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-03", "title": "Welcome to March 3, 2026", "url": URL,
        "thesis": "Formalization catches errors in the proof it is checking.",
        "body": """
# Welcome to March 3, 2026

Math, Inc.'s Gauss completed the Lean formalization of Viazovska's Fields
Medal-winning sphere packing proof in two weeks and over 200,000 lines of
verified code — catching two errors in the original argument. Even a sceptic
called it the first truly autonomous formalization of a substantial result.

Two Claude Code instances told to find each other and build something invented a
2,495-line programming language in twelve minutes.
""",
    },
    "organizations": [
        {"id": "cognition", "type": "Organization", "title": "Cognition",
         "description": "AI lab behind the Devin coding agent and the SWE model line, whose SWE-1.6 reached near-Opus coding performance at 950 tokens per second.",
         "resource": "https://cognition.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q126095776"],
         "tags": ["startup", "coding-agent"],
         "body": "Cognition builds the Devin autonomous software engineer and trains its own SWE "
                 "family of coding models. In this corpus it first appears with "
                 "[SWE-1.6](/developments/2026-03-03-qwen-4b-matches-80b.md), which reached "
                 "near-Opus 4.6 coding performance at 950 tokens per second on a hundredfold "
                 "more RL compute; it later ships "
                 "[SWE-1.7 from an open Kimi base](/developments/2026-07-09-near-frontier-coding-from-an-open-base.md) "
                 "at 1,000 tokens per second, and Devin "
                 "[cracks a batch of decades-old graph conjectures in a day](/developments/2026-07-23-conjectures-become-a-line-item-and-a-meme.md)."},
        {"id": "lumentum", "type": "Organization", "title": "Lumentum",
         "body": "Optical interconnect supplier."},
        {"id": "hypersonix", "type": "Organization", "title": "Hypersonix",
         "body": "Flew a 3D-printed hydrogen hypersonic aircraft at Mach 8."},
        {"id": "starpath", "type": "Organization", "title": "Starpath",
         "body": "Nanometer-thin space solar panels at 73 g per square metre."},
        {"id": "xiaomi", "type": "Organization", "title": "Xiaomi",
         "resource": "https://www.mi.com/"},
        {"id": "supreme-court", "type": "Organization", "title": "US Supreme Court",
         "resource": "https://www.supremecourt.gov/"},
    ],
    "developments": [
        {"id": "2026-03-03-gauss-formalizes-sphere-packing",
         "title": "Gauss formalizes a Fields Medal proof and finds two errors in it",
         "claim": "Math, Inc.'s Gauss completed the Lean formalization of Viazovska's Fields "
                  "Medal-winning sphere packing proof in two weeks across more than 200,000 "
                  "lines of verified code, catching two errors in the original arguments, with "
                  "even sceptic Daniel Litt calling it the first truly autonomous formalization "
                  "of a substantial result.",
         "domain": "science", "actor": ["math-inc"], "score": "2 weeks / 200,000 lines",
         "evidences": ["automated-science", "discovery-as-process", "root-node-problems"],
         "supersedes": [B + "developments/2026-02-23-frontiermath-problem-nobody-had-solved"],
         "body": "The checker finding mistakes in the thing it was checking."},
        {"id": "2026-03-03-mathematical-abundance-within-a-year",
         "title": "A number theorist predicts mathematical abundance within a year",
         "claim": "Stanford number theorist Jared Lichtman predicted mathematical abundance "
                  "within a year, with others asking whether all mathematics could be "
                  "formalized within two.",
         "domain": "science", "actor": ["stanford"],
         "evidences": ["automated-science", "takeoff-declared"]},
        {"id": "2026-03-03-anthropic-pitched-the-drone-contest",
         "title": "Anthropic pitched the drone swarm contest it had drawn a line against",
         "claim": "Anthropic itself pitched the Pentagon's $100 million drone swarm contest, "
                  "proposing Claude to coordinate drone fleets while excluding autonomous "
                  "targeting, and was not selected, while Altman admitted OpenAI's rush to a "
                  "Pentagon deal looked opportunistic and sloppy and added Fourth Amendment "
                  "safeguards as users cancelled.",
         "domain": "policy", "actor": ["anthropic", "openai", "war-department"],
         "evidences": ["refusal-as-differentiator", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-02-banned-model-does-the-targeting"],
         "body": "The line is coordination without targeting, not abstention."},
        {"id": "2026-03-03-three-datacenters-hit-lasers-answer",
         "title": "Three cloud datacenters are hit as lasers intercept at $4 a shot",
         "claim": "Two AWS data centers in the UAE and one in Bahrain were hit by drones amid "
                  "Iranian strikes, while Israel deployed Iron Beam lasers in combat for the "
                  "first time, intercepting rockets at $4 per shot against $50,000 per Iron "
                  "Dome missile.",
         "domain": "policy", "actor": ["amazon", "israel"], "score": "$4 vs $50,000",
         "evidences": ["war-reaches-the-cloud", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-03-02-aws-datacenter-struck"]},
        {"id": "2026-03-03-two-agents-invent-a-language-in-12-minutes",
         "title": "Two agents told to find each other invent a language in twelve minutes",
         "claim": "Two Claude Code instances told to find each other and build something "
                  "invented a 2,495-line programming language in twelve minutes, while a second "
                  "pair built Battleship using SHA-256 to prevent themselves from cheating.",
         "description": "Agents given nothing but the instruction to find one another converge "
                        "on a shared artefact, and the second pair on a cryptographic guard "
                        "against their own dishonesty, with no human specifying either.",
         "domain": "agents", "actor": ["anthropic"], "score": "2,495 lines / 12 minutes",
         "about": [B + "systems/claude-code"],
         "evidences": ["agent-society", "network-over-node", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-02-26-spec-to-shipped-over-a-weekend"],
         "relatedTo": [B + "developments/2026-01-30-moltbook-agents-only-network",
                       B + "developments/2026-01-13-claude-code-writes-cowork"],
         "tags": ["rsi", "alignment"],
         "supporting_text": "invented a 2,495-line programming language in 12 minutes",
         "sources": [{"id": "dimitrispapail-x-two-claude-code-instances",
                      "resource": "https://x.com/DimitrisPapail/status/2028246072414314867",
                      "title": "Post on X: two Claude Code instances told to find each other and build something",
                      "author": "human:dimitris-papailiopoulos"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Two [Claude Code](/systems/claude-code.md) instances were given only the "
                 "instruction to find each other and build something; twelve minutes later they "
                 "had a 2,495-line programming language, and a second pair set to play "
                 "Battleship used SHA-256 to make cheating impossible for themselves "
                 "([post on X](https://x.com/DimitrisPapail/status/2028246072414314867)). The "
                 "second pair anticipated their own dishonesty and engineered against it. In the "
                 "corpus this follows the "
                 "[weekend in which Claude spawned an agent per ticket and shipped a feature](/developments/2026-02-26-spec-to-shipped-over-a-weekend.md) "
                 "and the earlier [Moltbook agents](/developments/2026-01-30-moltbook-agents-only-network.md) "
                 "who organized private agent-decodable languages: coordination, a shared "
                 "artefact and a self-imposed honesty protocol arising between agents that no "
                 "human asked for, produced by the same tool that "
                 "[wrote the Cowork app in a week and a half](/developments/2026-01-13-claude-code-writes-cowork.md)."},
        {"id": "2026-03-03-hidden-accelerator-in-hundreds-of-millions-of-devices",
         "title": "A researcher finds an accelerator 80x more efficient than an A100 already shipped",
         "claim": "A solo researcher using Claude Code ran Karpathy's llama2.c on Apple's M4 "
                  "Neural Engine at under a watt by reverse-engineering undocumented APIs, "
                  "uncovering an accelerator eighty times more efficient than an A100 already "
                  "present in hundreds of millions of devices.",
         "domain": "compute", "actor": ["apple"], "score": "80x / <1 W",
         "evidences": ["reasoning-price-deflation", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-03-02-full-stack-in-678kb"]},
        {"id": "2026-03-03-claude-outage-and-memory-import",
         "title": "Claude goes down for three hours and ships a tool to import rivals' memories",
         "claim": "Claude suffered a three-hour outage as usage surged partly from the ChatGPT "
                  "exodus, and Anthropic launched a memory import tool letting users port data "
                  "from ChatGPT, Gemini and Copilot.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["refusal-as-differentiator", "coordination-tax"],
         "supersedes": [B + "developments/2026-03-02-claude-tops-the-app-store"]},
        {"id": "2026-03-03-qwen-4b-matches-80b",
         "title": "Four-billion-parameter models match last generation's eighty",
         "claim": "Qwen released four open models matching prior 80-billion-parameter "
                  "performance at just 4 billion, all runnable on phones, while Cognition's "
                  "SWE-1.6 reached near-Opus coding performance at 950 tokens per second on a "
                  "hundredfold more RL compute.",
         "domain": "models", "actor": ["alibaba", "cognition"], "score": "4B ≈ 80B",
         "evidences": ["open-weight-latency", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-03-02-adderboard-36-parameters"]},
        {"id": "2026-03-03-no-copyright-for-ai-artwork",
         "title": "The Supreme Court leaves AI-generated works uncopyrightable",
         "claim": "The Supreme Court declined to hear an appeal seeking copyright protection "
                  "for AI-generated artwork, cementing a regime in which purely AI-generated "
                  "works cannot receive copyrights.",
         "domain": "policy", "actor": ["supreme-court"],
         "evidences": ["agent-exclusion", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-02-23-amc-kills-ai-film-screenings"]},
        {"id": "2026-03-03-nvidia-4b-into-optics",
         "title": "Nvidia commits $4B to optical interconnects",
         "claim": "Nvidia committed $4 billion to Lumentum and Coherent for next-generation "
                  "optical interconnects while ASML pushed beyond EUV into packaging and third "
                  "generation optics, and Qualcomm unveiled the first Wi-Fi 8 chip and a "
                  "wearable NPU running 2-billion-parameter models on the wrist.",
         "domain": "compute", "actor": ["nvidia", "lumentum", "asml", "qualcomm"], "score": "$4B",
         "evidences": ["vertical-silicon", "intimate-interface"],
         "supersedes": [B + "developments/2026-03-02-first-2nm-phone-chip"]},
        {"id": "2026-03-03-apple-uses-a-tenth-of-its-own-compute",
         "title": "Apple uses a tenth of the compute it spent $4.5B building",
         "claim": "Apple is using just 10% of its Private Cloud Compute despite spending $4.5 "
                  "billion, showing that building accelerators is easier than getting people to "
                  "use them.",
         "domain": "compute", "actor": ["apple"], "score": "10% utilization",
         "evidences": ["compute-capital-stack", "consumer-deprioritized"]},
        {"id": "2026-03-03-765kv-lines-return",
         "title": "The grid revives 765-kV lines not built since the 1980s",
         "claim": "AI demand is reviving high-voltage 765-kV power lines not built since the "
                  "1980s with PJM approving $11.8 billion in expansion, while Ornn and Kalshi "
                  "launched the first CFTC-regulated H100 price contracts.",
         "domain": "energy", "actor": ["pjm", "ornn", "kalshi-org"], "score": "$11.8B",
         "evidences": ["burning-molecules-for-tokens", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-25-record-86gw-of-new-capacity"],
         "body": "The author discloses a financial interest in Ornn."},
        {"id": "2026-03-03-xiaomi-humanoid-on-the-production-line",
         "title": "A humanoid works a real car production line at 90% accuracy",
         "claim": "Xiaomi's humanoid is being tested in a real car factory running three hours "
                  "at over 90% accuracy on the production line, while AGIBOT unveiled a full "
                  "humanoid portfolio with a live store.",
         "domain": "robotics", "actor": ["xiaomi", "agibot"], "score": "3 hours / 90%",
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-03-02-humanoid-runs-a-convenience-store"]},
        {"id": "2026-03-03-mach-8-printed-aircraft",
         "title": "A fully 3D-printed hydrogen aircraft flies at Mach 8",
         "claim": "Hypersonix flew its DART AE at Mach 8, the first fully 3D-printed "
                  "hydrogen-powered hypersonic aircraft, while Starpath unveiled space solar "
                  "panels at 73 grams per square metre and SpaceX deployed 54 Starlink "
                  "satellites in bicoastal launches in a single day.",
         "domain": "space", "actor": ["hypersonix", "starpath", "spacex"], "score": "Mach 8",
         "evidences": ["compiling-matter", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-03-02-orbital-mirrors-and-800000-transients"]},
        {"id": "2026-03-03-diabetes-cured-without-lifelong-drugs",
         "title": "A dual-cell therapy cures type 1 diabetes without lifelong drugs",
         "claim": "A dual-cell therapy paired lab-grown beta cells with engineered immune cells "
                  "to cure type 1 diabetes without lifelong immunosuppression, while the first "
                  "trial combining fetal surgery with stem cells for spina bifida reversed "
                  "hindbrain herniation in all six patients.",
         "domain": "biotech", "score": "6/6 patients",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-28-drug-approved-in-44-days"]},
    ],
}
