"""Issue 155 — 2026-07-04. There will not be an FDA for AI."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-4-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-04", "title": "Welcome to July 4, 2026", "url": URL,
        "thesis": "The ceiling gets regulated while the floor rockets upward.",
        "body": """
# Welcome to July 4, 2026

The President's departing AI adviser promises there will not be an FDA for AI —
no licensing agency, no sand in the gears — even after Washington withdrew
Mythos and stalled GPT-5.6.

The more consequential number is at the other end. GLM 5.2 topped PostTrainBench
at five times cheaper than Opus 4.8 and eleven times cheaper than Fable 5,
economics that make sovereign models viable for every company and country. Once
models can post-train other models, authoring minds becomes an accessible
artform.
""",
    },
    "themes": [
        {"id": "authoring-minds", "type": "Theme",
         "title": "Post-training becomes an accessible artform",
         "first_seen": "2026-07-04", "domain": "models",
         "body": "When a model can post-train another model cheaply, creating a mind "
                 "stops being an industrial act and becomes an authorial one. The "
                 "count of distinct cognitive systems in the world stops tracking the "
                 "count of organizations that can afford to train them."},
        {"id": "most-people-never-see-the-frontier", "type": "Theme",
         "title": "The frontier is invisible to almost everyone",
         "first_seen": "2026-07-04", "domain": "society",
         "body": "A tiny sliver of people touch frontier models; everyone else meets "
                 "AI at the small-model level and finds the displacement talk absurd. "
                 "The public argument about AI is conducted by people describing "
                 "different artifacts."},
    ],
    "organizations": [
        {"id": "wafer-inc", "type": "Organization", "title": "Wafer"},
        {"id": "ampera", "type": "Organization", "title": "AMPERA"},
        {"id": "deployable-energy", "type": "Organization", "title": "Deployable Energy"},
        {"id": "america250", "type": "Organization", "title": "America250"},
    ],
    "developments": [
        {"id": "2026-07-04-there-will-not-be-an-fda-for-ai",
         "title": "A departing adviser promises no licensing agency for AI",
         "claim": "The President's departing AI adviser promised there will not be an FDA for AI, "
                  "no licensing agency and no sand in the gears of the intelligence explosion, "
                  "even after Washington's unprecedented move to withdraw Mythos and stall "
                  "GPT-5.6.",
         "domain": "policy", "actor": ["white-house", "anthropic", "openai"],
         "evidences": ["safety-pledges-recede", "clearance-as-bottleneck", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-02-an-emergency-lever-becomes-a-scheduled-one"]},
        {"id": "2026-07-04-a-throttled-frontier-still-outruns-yesterday",
         "title": "A throttled model scores ten points below itself and still leads",
         "claim": "The re-released Fable 5 scored 54.8% on the APEX-SWE benchmark, ten points "
                  "below its June self yet still nine clear of Opus 4.8, showing that even a "
                  "throttled frontier outruns yesterday's best.",
         "domain": "benchmarks", "actor": ["anthropic"], "score": "54.8%, down 10, up 9 on rival",
         "evidences": ["rationed-recursion", "frontier-moves-backward", "spiky-frontier"],
         "supersedes": [B + "developments/2026-07-03-seventeen-leaders-in-two-years"]},
        {"id": "2026-07-04-most-of-humanity-never-met-the-frontier",
         "title": "Most people experience AI at the small-model level and are baffled",
         "claim": "A tiny sliver of the population touches frontier models, while everyone else "
                  "experiences AI at the 8-to-30-billion-parameter level and remains baffled at "
                  "how it is supposed to take their job.",
         "domain": "society",
         "evidences": ["most-people-never-see-the-frontier", "public-internal-divergence",
                       "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-07-04-a-throttled-frontier-still-outruns-yesterday"]},
        {"id": "2026-07-04-every-scaling-failure-was-a-bug",
         "title": "A lab president says every apparent scaling failure was a bug in disguise",
         "claim": "Greg Brockman reported that every apparent scaling failure has turned out to "
                  "be a bug in disguise, with either the mathematics wrong or the code not "
                  "matching it.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["takeoff-declared", "instruments-lag-the-models"],
         "supersedes": [B + "developments/2026-07-03-learning-speed-doubles-every-three-months"]},
        {"id": "2026-07-04-authoring-minds-becomes-an-artform",
         "title": "Cheap post-training makes sovereign models viable for everyone",
         "claim": "GLM 5.2 topped PostTrainBench at five times cheaper than Opus 4.8 and eleven "
                  "times cheaper than Fable 5, economics that make sovereign models viable for "
                  "every company and country, with OpenAI's Roon arguing that once models can "
                  "post-train other models, authoring minds becomes an accessible artform.",
         "domain": "models", "actor": ["zai", "openai", "anthropic"], "score": "5x / 11x cheaper",
         "evidences": ["authoring-minds", "own-your-own-weights", "open-weight-latency"],
         "supersedes": [B + "developments/2026-06-29-the-open-source-claude-moment"]},
        {"id": "2026-07-04-agents-write-the-kernels-closing-a-software-gap",
         "title": "A challenger GPU serves an open model at half the cost as agents write kernels",
         "claim": "Wafer served GLM-5.2 on AMD's MI355X at 2,626 tokens per second per node at "
                  "less than half Blackwell's cost, arguing AMD's software gap is closing because "
                  "AI agents now write the kernels.",
         "domain": "compute", "actor": ["wafer-inc", "amd", "nvidia"], "score": "2,626 tok/s/node",
         "evidences": ["recursive-self-improvement", "intelligence-per-watt", "vertical-silicon"],
         "supersedes": [B + "developments/2026-07-03-circuits-drawn-in-minutes-not-months"]},
        {"id": "2026-07-04-models-become-entities-not-genies",
         "title": "The argument shifts from genies summoned per task to entities that persist",
         "claim": "Commentators argued AGI will feel real when models stop being genies summoned "
                  "per task and become entities — remote coworkers who never turn on their "
                  "cameras — as Microsoft merged apps and added a paid tier after fewer than "
                  "4.5% of its 450 million customers paid for Copilot.",
         "domain": "agents", "actor": ["microsoft"], "score": "<4.5% paid conversion",
         "evidences": ["the-persistent-colleague", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-06-24-a-model-joins-the-team-in-slack"]},
        {"id": "2026-07-04-context-rendered-as-images-to-cut-bills",
         "title": "A proxy renders context into images to cut an AI bill by 59%",
         "claim": "The open-source pxpipe proxy renders bulky context into compact images, "
                  "turning a $100 Claude Code bill into $41 — lossy but lucid.",
         "domain": "agents", "score": "$100 to $41",
         "evidences": ["reasoning-price-deflation", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-06-28-ai-spend-halved-by-routing-and-caching"]},
        {"id": "2026-07-04-a-lab-will-develop-its-own-drugs",
         "title": "A frontier lab will develop drugs of its own to pressure-test its science tools",
         "claim": "Anthropic will develop drugs of its own to pressure-test Claude Science "
                  "against real problems, while Mistral's Leanstral 1.5 set records on graduate "
                  "algebra and solved 587 of 672 PutnamBench problems on a tenth of the budget.",
         "domain": "biotech", "actor": ["anthropic", "mistral"], "score": "587 of 672",
         "evidences": ["automated-science", "hardware-grade-biology", "proof-priced-per-unit"],
         "supersedes": [B + "developments/2026-07-01-sixty-databases-in-one-workbench"]},
        {"id": "2026-07-04-buying-compute-becomes-becoming-compute",
         "title": "A lab explores custom silicon as buying compute becomes becoming compute",
         "claim": "Anthropic is exploring custom silicon with Samsung's 2-nanometer process, "
                  "while Micron broke ground on a $9.3 billion Hiroshima expansion and Hong Kong "
                  "handled more than half of China's $239 billion in chip imports this year.",
         "domain": "compute", "actor": ["anthropic", "samsung", "micron"], "score": "$9.3B / $239B",
         "evidences": ["vertical-silicon", "compute-capital-stack", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-29-a-five-hundred-eighty-five-billion-semiconductor-complex"]},
        {"id": "2026-07-04-you-either-die-a-frontier-lab-or-sell-compute",
         "title": "A social network builds a cloud to monetize its own buildout",
         "claim": "Meta's coming cloud, a token service plus a neocloud, addresses both its ad "
                  "dependence and unmonetized capital spending, with the company reportedly in "
                  "final talks for private access to Claude, prompting one observer to quip that "
                  "you either die a frontier lab or live long enough to see yourself sell "
                  "compute.",
         "domain": "economics", "actor": ["meta", "anthropic"],
         "evidences": ["compute-capital-stack", "orchestration-not-construction"],
         "supersedes": [B + "developments/2026-07-02-compute-swings-into-surplus"]},
        {"id": "2026-07-04-three-microreactors-hit-a-presidential-deadline",
         "title": "Microreactors go critical on a presidential deadline",
         "claim": "AMPERA completed the first full-scale 3D-printed nuclear reactor module for "
                  "its factory-built thorium design and Deployable Energy's Unity reactor went "
                  "critical at Idaho National Laboratory, the third US microreactor to hit the "
                  "presidential deadline, as power-equipment makers scrambled for a market worth "
                  "over $200 billion a year.",
         "domain": "energy", "actor": ["ampera", "deployable-energy", "inl"], "score": ">$200B/yr",
         "evidences": ["industrialized-nature", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-07-02-the-first-nuclear-startup-to-make-electricity"]},
    ],
}
