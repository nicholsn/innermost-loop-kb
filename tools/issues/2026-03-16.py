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
         "body": "Anthropic alignment lead."},
        {"id": "jared-kaplan", "type": "Person", "title": "Jared Kaplan", "name": "Jared Kaplan",
         "body": "Anthropic chief science officer."},
    ],
    "developments": [
        {"id": "2026-03-16-rsi-is-a-present-phenomenon",
         "title": "An alignment lead says recursive self-improvement is already happening",
         "claim": "Between 70 and 90 percent of the code behind future Anthropic models is now "
                  "written by Claude, chief science officer Jared Kaplan believes fully "
                  "automated AI research is less than a year away, and alignment lead Evan "
                  "Hubinger said recursive self-improvement is not a future phenomenon but a "
                  "present one.",
         "domain": "agents", "actor": ["anthropic", "people/evan-hubinger", "people/jared-kaplan"],
         "score": "70-90% of code",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2026-03-12-posttrainbench-v1"]},
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
         "domain": "models", "actor": ["anthropic", "openai"], "score": "1M tokens",
         "evidences": ["recursive-self-improvement", "architecture-of-mind"]},
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
