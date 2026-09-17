"""Issue 114 — 2026-05-13. The test-taker becomes the test-maker."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-13-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-13", "title": "Welcome to May 13, 2026", "url": URL,
        "thesis": "Agents begin writing their own objectives.",
        "body": """
# Welcome to May 13, 2026

Users have started metaprompting Codex to draft its own goal file, with one
calling the resulting stack the highest leverage agent configuration available.
The corpus has recorded agents writing their own skills and harnesses; this is
them writing the brief.

Princeton ended its 1893 honor code by faculty vote, requiring proctoring for
all in-person exams from this summer.
""",
    },
    "organizations": [
        {"id": "robotplusplus", "type": "Organization", "title": "RobotPlusPlus",
         "body": "Humanoid on magnetic-adhesion wheels that scales vertical steel."},
        {"id": "ames-lab", "type": "Organization", "title": "Ames National Laboratory",
         "resource": "https://www.ameslab.gov/"},
        {"id": "columbia", "type": "Organization", "title": "Columbia University",
         "resource": "https://www.columbia.edu/"},
        {"id": "star-catcher", "type": "Organization", "title": "Star Catcher",
         "body": "Beaming optical power to client satellites' existing solar arrays."},
        {"id": "princeton-u", "type": "Organization", "title": "Princeton University",
         "resource": "https://www.princeton.edu/"},
    ],
    "developments": [
        {"id": "2026-05-13-agents-write-their-own-goals",
         "title": "Users metaprompt an agent to write its own objective file",
         "claim": "Users are now metaprompting Codex to draft its own goal specification, with "
                  "one calling the resulting stack the highest-leverage agent configuration "
                  "available today.",
         "description": "After agents writing their own skills and harnesses, the corpus records them "
                        "writing the brief itself: the objective, the last human-authored layer, "
                        "moves inside the loop.",
         "domain": "agents", "actor": ["openai"], "occurred_on": "2026-05-11",
         "about": [B + "systems/codex"],
         "evidences": ["scaffolding-over-weights", "recursive-self-improvement",
                       "self-authored-scaffolding"],
         "supersedes": [B + "developments/2026-05-11-the-harness-eats-the-model"],
         "relatedTo": [B + "developments/2026-03-31-bilevel-autoresearch",
                       B + "developments/2026-02-03-codex-builds-itself",
                       B + "developments/2026-06-25-an-agent-rewrites-its-own-harness"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-05-11-the-harness-eats-the-model",
                        "relation_label": "extends"}],
         "tags": ["rsi", "agent-harness"],
         "supporting_text": "the highest leverage AI agent configuration available today",
         "sources": [{"id": "daniel-mac8-codex-goal-x",
                      "resource": "https://x.com/daniel_mac8/status/2053896200005271594",
                      "title": "@daniel_mac8 on X: metaprompting Codex to draft its own /goal",
                      "author": "human:daniel-mac8"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The pattern the newsletter picked up is a user asking [Codex](/systems/codex.md) to "
                 "draft its own \u201c/goal\u201d, the objective file that steers its subsequent work, "
                 "rather than writing the brief by hand; the poster the issue quotes called the result "
                 "\u201cthe highest leverage AI agent configuration available today\u201d "
                 "([X](https://x.com/daniel_mac8/status/2053896200005271594)). It comes two days after "
                 "[Hermes Agent took the token rankings by generating its own skills](/developments/2026-05-11-the-harness-eats-the-model.md) "
                 "and six weeks after a research loop "
                 "[wrote the strategies for its own outer loop](/developments/2026-03-31-bilevel-autoresearch.md): "
                 "skills, harness and now the objective are being authored by the agent, the thread the "
                 "[self-authored-scaffolding](/themes/self-authored-scaffolding.md) theme names in June. "
                 "The next day "
                 "[Recursive Superintelligence emerged from stealth with $650 million](/developments/2026-05-14-recursive-superintelligence-raises-650m.md) "
                 "to have AI experiment on improving itself, and in June the "
                 "[Self-Harness paradigm](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) "
                 "closed the loop without a human engineer."},
        {"id": "2026-05-13-a-model-scores-136-on-an-iq-meta-eval",
         "title": "A meta-eval maps twelve benchmarks onto an implied IQ of 136",
         "claim": "A new meta-evaluation mapping a calibrated mix of twelve existing benchmarks "
                  "onto implied IQs crowned GPT-5.5 the smartest available model at 136, while "
                  "both its reasoning modes solved the first task on a benchmark measuring "
                  "whether models can rebuild programs from scratch.",
         "domain": "benchmarks", "actor": ["openai"], "score": "IQ 136",
         "evidences": ["benchmark-saturation", "models-audit-their-benchmarks"],
         "supersedes": [B + "developments/2026-05-08-rebuilding-a-codebase-from-a-binary"]},
        {"id": "2026-05-13-claude-for-the-legal-industry",
         "title": "A lab ships a legal product and partners to widen access to counsel",
         "claim": "Anthropic launched Claude for the legal industry with more than twenty "
                  "connectors and twelve practice-area plugins, partnering with the Free Law "
                  "Project and the Justice Technology Association to put counsel within reach of "
                  "people who currently cannot access it.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["work-displaced", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-06-an-agent-is-given-a-cafe"]},
        {"id": "2026-05-13-the-prompt-becomes-a-gesture",
         "title": "A mouse pointer understands what it is pointing at",
         "claim": "Google unveiled Gemini Intelligence letting users vibe-code their own Android "
                  "widgets plus a model-powered mouse pointer that understands what it is "
                  "pointing at, and a Chromebook successor merging its two operating systems "
                  "into one model-optimized platform.",
         "domain": "models", "actor": ["google"],
         "evidences": ["intimate-interface", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-05-06-intelligence-becomes-a-default-setting"]},
        {"id": "2026-05-13-nineteen-gas-turbines-in-two-months",
         "title": "A datacenter campus adds nineteen gas turbines in two months",
         "claim": "xAI added nineteen gas turbines to its Colossus 2 campus in Mississippi over "
                  "two months, brute-forcing past the grid queue, while a national lab's "
                  "materials model compressed fusion alloy discovery from months to hours.",
         "domain": "energy", "actor": ["xai", "ames-lab"], "score": "19 turbines",
         "evidences": ["burning-molecules-for-tokens", "regulatory-exit"],
         "supersedes": [B + "developments/2026-05-12-transformer-demand-up-274-percent"]},
        {"id": "2026-05-13-a-humanoid-that-climbs-vertical-steel",
         "title": "A humanoid on magnetic wheels climbs vertical steel to weld and grind",
         "claim": "China's RobotPlusPlus debuted a humanoid special-operations robot on "
                  "magnetic-adhesion wheels that scales vertical steel in chemical plants, "
                  "shipyards and energy facilities, swapping tools at the wrist for welding, "
                  "flaw detection, rust removal, grinding and spraying.",
         "domain": "robotics", "actor": ["robotplusplus"],
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-05-12-a-production-ready-mecha"]},
        {"id": "2026-05-13-the-cocktail-party-problem-solved",
         "title": "A brain-controlled hearing system amplifies whichever voice you attend to",
         "claim": "Columbia researchers demonstrated the first real-time brain-controlled "
                  "hearing system, reading intracranial signals to identify whichever voice a "
                  "listener is focusing on in a noisy room and amplifying it while suppressing "
                  "the rest.",
         "domain": "biotech", "actor": ["columbia"],
         "evidences": ["intimate-interface", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-12-pleasure-becomes-a-knob"]},
        {"id": "2026-05-13-two-hundred-satellites-from-passing-everyone",
         "title": "One company nears launching more satellites than everyone else combined",
         "claim": "SpaceX is about two hundred satellites away from having launched more than "
                  "the rest of the world combined despite a sixty-one-year head start for "
                  "everyone else, while Google entered talks with SpaceX for a launch deal as it "
                  "expands its own orbital datacenter push.",
         "domain": "space", "actor": ["spacex", "google"], "score": "~200 satellites",
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-05-12-an-orbital-gpu-cluster-by-2027"]},
        {"id": "2026-05-13-a-power-grid-in-orbit",
         "title": "A startup raises $65M to beam power to existing satellite solar arrays",
         "claim": "Star Catcher raised $65 million to beam optical power tuned to off-the-shelf "
                  "solar arrays, supercharging client satellites with two to ten times more "
                  "power on demand and building the first true grid in orbit.",
         "domain": "space", "actor": ["star-catcher"], "score": "$65M / 2-10x",
         "evidences": ["orbit-as-compute", "burning-molecules-for-tokens"]},
        {"id": "2026-05-13-japan-opens-its-own-uap-review",
         "title": "Japan begins its own disclosure review of released UAP files",
         "claim": "Japan's government said it is analyzing the released UAP files with great "
                  "interest, including videos shot near Japan, and will begin its own disclosure "
                  "case by case.",
         "domain": "policy", "actor": ["japan-govt"],
         "evidences": ["politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-09-pursue-releases-162-records"]},
        {"id": "2026-05-13-princeton-ends-a-133-year-old-honor-code",
         "title": "Princeton ends its 1893 honor code and restores proctoring",
         "claim": "Princeton is ending its 1893 honor code by faculty vote, requiring proctoring "
                  "in all in-person examinations from this summer because AI has made cheating "
                  "both easier and harder to detect.",
         "domain": "society", "actor": ["princeton-u"], "score": "133 years",
         "evidences": ["deskilling", "coordination-tax"],
         "supersedes": [B + "developments/2026-04-03-harvard-replaces-freshman-advisers"]},
        {"id": "2026-05-13-screenwriting-becomes-the-new-waiting-tables",
         "title": "Screenwriters call AI gig work the new waiting tables",
         "claim": "Struggling Hollywood screenwriters now describe AI training gig work as the "
                  "new waiting tables, signing on with platforms to train the models that will "
                  "retire their craft, while Anthropic warned investors away from eight "
                  "unauthorized secondary marketplaces amid talks to raise up to $50 billion at "
                  "a $950 billion valuation.",
         "domain": "economics", "actor": ["mercor", "anthropic"], "score": "$950B",
         "evidences": ["humans-as-peripherals", "work-displaced"],
         "supersedes": [B + "developments/2026-05-11-women-hold-most-of-the-exposed-jobs"]},
    ],
}
