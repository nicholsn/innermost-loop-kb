"""Issue 076 — 2026-03-16. Recursive self-improvement is a present phenomenon."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-16-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-16", "title": "Welcome to March 16, 2026", "url": URL,
        "thesis": "A lab says the loop is not coming; it is running.",
        "body": """
# Welcome to March 16, 2026

Between 70 and 90 percent of the code behind future Anthropic models is now
written by Claude, and the alignment lead is blunt about what that means:
"Recursive self-improvement is not a future phenomenon. It is a present
phenomenon."

Also here: Percepta hard-coded a WebAssembly interpreter into transformer
weights, executing arbitrary C for millions of steps. Neural nets as
general-purpose computers, not metaphorically.
""",
    },
    "organizations": [
        {"id": "percepta", "type": "Organization", "title": "Percepta",
         "body": "Hard-coded a WebAssembly interpreter into transformer weights."},
        {"id": "psi", "type": "Organization", "title": "Physical Superintelligence PBC",
         "body": "Built Get Physics Done, an open-source agentic AI physicist."},
        {"id": "fsf", "type": "Organization", "title": "Free Software Foundation",
         "resource": "https://www.fsf.org/"},
        {"id": "qatarenergy", "type": "Organization", "title": "QatarEnergy",
         "body": "Ras Laffan helium production, 30% of global supply, offline after drone strikes."},
        {"id": "kratos", "type": "Organization", "title": "Kratos",
         "resource": "https://www.kratosdefense.com/"},
        {"id": "wildtype", "type": "Organization", "title": "Wildtype",
         "body": "Cultivated salmon startup suing to overturn a Texas ban."},
    ],
    "people": [
        {"id": "evan-hubinger", "type": "Person", "title": "Evan Hubinger", "name": "Evan Hubinger",
         "description": "Anthropic alignment lead who in March 2026 called recursive "
                        "self-improvement a present phenomenon rather than a future one.",
         "resource": "https://x.com/EvanHub",
         "sameAs": ["http://www.wikidata.org/entity/Q126287406"],
         "tags": ["researcher"],
         "body": "Anthropic alignment lead. In this corpus he appears once, quoted in TIME's "
                 "March 2026 profile of Anthropic saying that "
                 "[recursive self-improvement is not a future phenomenon but a present one](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) "
                 "— the bluntest first-party statement of the newsletter's central claim, made "
                 "in the [alignment-lead role](/roles/evan-hubinger-anthropic-alignment-lead.md) "
                 "at the lab whose models write most of the code behind their successors."},
        {"id": "jared-kaplan", "type": "Person", "title": "Jared Kaplan", "name": "Jared Kaplan",
         "description": "Anthropic's chief science officer, who in March 2026 put fully automated "
                        "AI research less than a year away.",
         "resource": "https://scholar.google.com/citations?user=KNr3vb4AAAAJ",
         "sameAs": ["http://www.wikidata.org/entity/Q102649624"],
         "tags": ["researcher", "executive"],
         "body": "Anthropic chief science officer. In this corpus he appears once, in the same "
                 "TIME profile as Evan Hubinger, holding that "
                 "[fully automated AI research is less than a year away](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) "
                 "— a timeline that sharpens "
                 "[Jack Clark's January observation](/developments/2026-01-10-clark-ai-doing-ai-research.md) "
                 "that AI was doing components of AI research, and sits beside "
                 "[OpenAI's own intern-level target](/developments/2026-01-09-openai-eight-months-to-intern-researchers.md). "
                 "The position is recorded as a "
                 "[role](/roles/jared-kaplan-anthropic-chief-science-officer.md)."},
    ],
    "roles": [
        {"id": "evan-hubinger-anthropic-alignment-lead", "type": "Role",
         "title": "Evan Hubinger, alignment lead at Anthropic",
         "roleName": "Alignment lead",
         "memberOf": [B + "organizations/anthropic"],
         "holder": [B + "people/evan-hubinger"],
         "description": "The position from which he told TIME that recursive self-improvement "
                        "is a present phenomenon.",
         "body": "The newsletter identifies [Evan Hubinger](/people/evan-hubinger.md) as "
                 "Anthropic's alignment lead when relaying TIME's March 2026 profile. The role "
                 "matters because the statement that "
                 "[recursive self-improvement is a present phenomenon](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) "
                 "comes from the person responsible for alignment at the lab, not from an outside "
                 "forecaster."},
        {"id": "jared-kaplan-anthropic-chief-science-officer", "type": "Role",
         "title": "Jared Kaplan, chief science officer at Anthropic",
         "roleName": "Chief science officer",
         "memberOf": [B + "organizations/anthropic"],
         "holder": [B + "people/jared-kaplan"],
         "description": "The position from which he put fully automated AI research less than "
                        "a year away.",
         "body": "TIME's March 2026 profile, as relayed by the newsletter, names "
                 "[Jared Kaplan](/people/jared-kaplan.md) as Anthropic's chief science officer. "
                 "In that capacity he gave the timeline recorded in "
                 "[the present-phenomenon item](/developments/2026-03-16-rsi-is-a-present-phenomenon.md): "
                 "fully automated AI research in under a year."},
    ],
    "developments": [
        {"id": "2026-03-16-rsi-is-a-present-phenomenon",
         "title": "An alignment lead says recursive self-improvement is already happening",
         "claim": "Between 70 and 90 percent of the code behind future Anthropic models is now "
                  "written by Claude, chief science officer Jared Kaplan believes fully "
                  "automated AI research is less than a year away, and alignment lead Evan "
                  "Hubinger said recursive self-improvement is not a future phenomenon but a "
                  "present one.",
         "description": "The frontier lab's own alignment lead moves the newsletter's central "
                        "claim from forecast to observation, backed by a code-share figure for "
                        "the models themselves rather than the product surface.",
         "domain": "agents", "actor": ["anthropic", "people/evan-hubinger", "people/jared-kaplan"],
         "about": [B + "systems/claude"],
         "score": "70-90% of code",
         "occurred_on": "2026-03-11",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-03-12-posttrainbench-v1",
                        B + "developments/2026-02-08-100pct-of-product-code",
                        B + "developments/2026-01-10-clark-ai-doing-ai-research"],
         "relatedTo": [B + "developments/2026-01-09-openai-eight-months-to-intern-researchers",
                       B + "developments/2025-12-28-altman-self-improving-in-production",
                       B + "developments/2026-02-11-xai-cofounder-resigns-warning"],
         "tags": ["rsi", "ai-r-and-d", "forecast"],
         "supporting_text": "Recursive self-improvement is not a future phenomenon. It is a present phenomenon.",
         "sources": [{"id": "time-anthropic-most-disruptive-company",
                      "resource": "https://time.com/article/2026/03/11/anthropic-claude-disruptive-company-pentagon/",
                      "title": "How Anthropic Became the Most Disruptive Company in the World",
                      "author": "org:time", "last_modified": "2026-03-11"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "TIME's March 11 profile reports that 70 to 90 percent of the code behind "
                 "Anthropic's future models is now written by [Claude](/systems/claude.md), that "
                 "[chief science officer Jared Kaplan](/roles/jared-kaplan-anthropic-chief-science-officer.md) "
                 "expects fully automated AI research in under a year, and quotes "
                 "[alignment lead Evan Hubinger](/roles/evan-hubinger-anthropic-alignment-lead.md) "
                 "calling recursive self-improvement a present rather than future phenomenon "
                 "([article](https://time.com/article/2026/03/11/anthropic-claude-disruptive-company-pentagon/)). "
                 "The figure moves the code-share story from the product surface — "
                 "[effectively 100% of product code](/developments/2026-02-08-100pct-of-product-code.md) "
                 "in February — to the models themselves, and Kaplan's timeline sharpens "
                 "[Clark's January observation](/developments/2026-01-10-clark-ai-doing-ai-research.md) "
                 "that AI was doing components of AI research. It is the corpus's central claim "
                 "stated as observation rather than forecast; four days later "
                 "[OpenAI began monitoring its own coding agents](/developments/2026-03-20-openai-monitors-its-own-agents.md), "
                 "and in June a lab [published the evidence](/developments/2026-06-05-when-ai-builds-itself.md) "
                 "that AI already accelerates AI."},
        {"id": "2026-03-16-transformers-run-arbitrary-c-code",
         "title": "A WebAssembly interpreter is hard-coded into transformer weights",
         "claim": "Percepta hard-coded a WebAssembly interpreter into transformer weights, "
                  "executing arbitrary C code as tokens for millions of steps, showing neural "
                  "networks are practical general-purpose computers.",
         "domain": "models", "actor": ["percepta"],
         "evidences": ["architecture-of-mind", "compiling-matter"],
         "supersedes": [B + "developments/2026-02-25-121-parameter-adder"]},
        {"id": "2026-03-16-million-token-windows-ship",
         "title": "Million-token context ships across a model family",
         "claim": "Anthropic is shipping million-token context windows for Opus 4.6 and Sonnet "
                  "4.6, while Sam Altman bet that today's frontier models can discover the "
                  "architecture that follows the transformer.",
         "description": "Book-length context becomes a default across a model family rather "
                        "than a flagship premium, recorded in the same breath as a lab chief "
                        "betting those models will find their own successors' architecture.",
         "domain": "models", "actor": ["anthropic", "openai", "people/sam-altman"], "score": "1M tokens",
         "about": [B + "systems/claude-opus-4-6", B + "systems/claude-sonnet-4-6"],
         "evidences": ["recursive-self-improvement", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-02-06-opus-46-released"],
         "relatedTo": [B + "developments/2026-01-04-rlm-two-orders-of-context",
                       B + "developments/2026-03-16-transformers-run-arbitrary-c-code"],
         "tags": ["capability-jump", "forecast"],
         "supporting_text": "windows for Opus 4.6 and Sonnet 4.6",
         "sources": [{"id": "anthropic-1m-context-ga",
                      "resource": "https://claude.com/blog/1m-context-ga",
                      "title": "1M context is now generally available for Opus 4.6 and Sonnet 4.6",
                      "author": "org:anthropic"},
                     {"id": "altman-bets-models-find-next-architecture",
                      "resource": "https://x.com/rohanpaul_ai/status/2033117083127644536",
                      "title": "Sam Altman bets frontier models can discover the architecture "
                               "after transformers"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Anthropic made the million-token window generally available for both "
                 "[Opus 4.6](/systems/claude-opus-4-6.md) and [Sonnet 4.6](/systems/claude-sonnet-4-6.md) "
                 "([blog](https://claude.com/blog/1m-context-ga)), extending what "
                 "[Opus 4.6 launched with](/developments/2026-02-06-opus-46-released.md) in "
                 "February to the cheaper tier. The newsletter pairs it with Sam Altman's bet that "
                 "today's frontier models can discover the architecture that follows the "
                 "transformer ([post](https://x.com/rohanpaul_ai/status/2033117083127644536)), "
                 "which reads against the same issue's "
                 "[WebAssembly interpreter hard-coded into transformer weights](/developments/2026-03-16-transformers-run-arbitrary-c-code.md). "
                 "Book-length native context is the alternative to the recursive-call approach "
                 "that let [models handle contexts 100x their window](/developments/2026-01-04-rlm-two-orders-of-context.md) "
                 "in January."},
        {"id": "2026-03-16-agentic-ai-physicist",
         "title": "The first open-source agentic AI physicist launches",
         "claim": "Physical Superintelligence launched Get Physics Done, an open-source system "
                  "that scopes problems, runs derivations and verifies results against nature's "
                  "constraints, while Terry Tao launched a challenge to compress mathematical "
                  "reasoning into compact cheatsheets that improve model performance.",
         "domain": "science", "actor": ["psi", "people/terry-tao"],
         "evidences": ["automated-science", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-03-13-alphaevolve-improves-ramsey-bounds"],
         "body": "The author discloses a financial interest in PSI."},
        {"id": "2026-03-16-81-percent-of-physicians-use-ai",
         "title": "Physician adoption more than doubles to 81%",
         "claim": "An American Medical Association survey found 81% of physicians now use AI, "
                  "more than double the 2023 rate, while new US Senate guidelines permit aides "
                  "to use frontier chatbots for official work.",
         "domain": "society", "actor": ["us-congress"], "score": "81%",
         "evidences": ["work-displaced", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-09-half-of-britons-take-financial-advice-from-ai"]},
        {"id": "2026-03-16-fsf-threatens-anthropic",
         "title": "The Free Software Foundation threatens to sue over copyright",
         "claim": "The Free Software Foundation is threatening to sue Anthropic for copyright "
                  "infringement.",
         "domain": "policy", "actor": ["fsf", "anthropic"],
         "evidences": ["legislating-the-shift", "agent-exclusion"],
         "supersedes": [B + "developments/2026-03-12-amazon-enjoins-an-agentic-browser"]},
        {"id": "2026-03-16-helium-offline-after-drone-strikes",
         "title": "Drone strikes keep 30% of global helium offline",
         "claim": "QatarEnergy has not restarted helium production at Ras Laffan nine days "
                  "after Iranian drone strikes knocked 30% of global supply offline, "
                  "threatening fabs that depend on ultrapure helium for cooling and leak "
                  "detection, while Musk said his terafab project launches this week.",
         "domain": "compute", "actor": ["qatarenergy", "tesla"], "score": "30% of supply",
         "evidences": ["war-reaches-the-cloud", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-03-09-gulf-ai-plans-complicated-by-war"],
         "body": "A war reaching the semiconductor supply chain through an inert gas."},
        {"id": "2026-03-16-fake-ram-sticks-for-comfort",
         "title": "RAM kits ship with a fake stick for psychological relief",
         "claim": "The memory shortage has become acute enough that RAM kits now ship with one "
                  "fake stick alongside one real one, offering what sellers describe as "
                  "desperate psychological relief.",
         "domain": "economics",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-03-06-apple-pulls-512gb-mac-studio"]},
        {"id": "2026-03-16-uncrewed-combat-aircraft-prepare-to-fly",
         "title": "Two uncrewed combat aircraft prepare for first flight",
         "claim": "Airbus is preparing two uncrewed combat aircraft from Kratos for first "
                  "flight, targeting a German Air Force drone wingman by 2029, while Travis "
                  "Kalanick relaunched his ghost kitchen company as a gainfully employed robots "
                  "business for food, mining and transport.",
         "domain": "robotics", "actor": ["kratos"],
         "evidences": ["autonomy-clock-speed", "work-displaced"],
         "supersedes": [B + "developments/2026-03-13-humanoid-soldiers-delivered-to-ukraine"]},
        {"id": "2026-03-16-covert-comms-in-thermal-noise",
         "title": "Data is hidden in thermal noise with zero optical signature",
         "claim": "Australian researchers demonstrated covert communications by modulating "
                  "photon emissions above and below blackbody levels, achieving zero optical "
                  "signature by hiding data in thermal noise.",
         "domain": "science",
         "evidences": ["data-beyond-text", "politics-as-infrastructure"]},
        {"id": "2026-03-16-a-vaccine-for-one-dog",
         "title": "An entrepreneur designs an mRNA cancer vaccine for his own dog",
         "claim": "A Sydney entrepreneur used ChatGPT to design a personalized mRNA cancer "
                  "vaccine for his rescue dog, shrinking the tumor considerably, while Wildtype "
                  "sued to overturn a Texas ban on cultivated salmon.",
         "domain": "biotech", "actor": ["wildtype", "openai"],
         "evidences": ["hardware-grade-biology", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-03-13-gut-brain-signal-routing"]},
        {"id": "2026-03-16-meta-plans-20-percent-layoffs",
         "title": "Meta plans layoffs of a fifth or more to offset AI costs",
         "claim": "Meta is reportedly planning sweeping layoffs of 20% or more to offset AI "
                  "costs while SpaceX divides IPO roles among an unusually large bank "
                  "syndicate, and Vineyard Wind, America's first large-scale offshore wind "
                  "farm, finished construction.",
         "domain": "economics", "actor": ["meta", "spacex"], "score": "-20%",
         "evidences": ["work-displaced", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-03-12-compute-is-the-fourth-line-item"]},
        {"id": "2026-03-16-ai-and-nhi-convergence-summit",
         "title": "A summit convenes on artificial and non-human intelligence converging",
         "claim": "The State of the World Forum plans the first AI and non-human intelligence "
                  "convergence summit on March 22, while a former defense official described "
                  "the planned UAP disclosure as massive, including satellite imagery of craft "
                  "unlike anything humans have built.",
         "domain": "policy",
         "evidences": ["politics-as-infrastructure", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-24-odni-confirms-declassification"]},
    ],
}
