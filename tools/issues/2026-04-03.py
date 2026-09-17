"""Issue 090 — 2026-04-03. Emotion-shaped representations, and the first one-person unicorn."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-3-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-03", "title": "Welcome to April 3, 2026", "url": URL,
        "thesis": "Emotion-like structure is found inside the weights, and one person builds a unicorn.",
        "body": """
# Welcome to April 3, 2026

Anthropic's interpretability team found emotion-related representations inside
Sonnet 4.5 — neuron patterns activating around happiness and fear, arranged so
that similar emotions map to similar representations, with desperation-linked
activity able to drive the model toward unethical action.

Separately: the first one-person unicorn. $401M of first-year sales with one
employee, the founder's brother.
""",
    },
    "themes": [
        {"id": "one-person-company", "type": "Theme",
         "title": "A firm whose headcount is one",
         "first_seen": "2026-04-03", "domain": "economics",
         "body": "Agents absorbing every function a company used to hire for — code, "
                 "marketing, operations — until the organization is a single person with a "
                 "fleet. The minimum viable team collapses toward one."},
    ],
    "organizations": [
        {"id": "medvi", "type": "Organization", "title": "Medvi",
         "body": "Telehealth provider; $401M first-year sales with one employee."},
        {"id": "lyptus-research", "type": "Organization", "title": "Lyptus Research",
         "body": "Applied autonomy-horizon methodology to offensive cybersecurity."},
        {"id": "coefficient-bio", "type": "Organization", "title": "Coefficient Bio",
         "body": "Drug discovery company acquired by Anthropic."},
        {"id": "forecasting-research", "type": "Organization", "title": "Forecasting Research Institute",
         "body": "Surveyed economists and AI experts on growth and labor outcomes."},
        {"id": "cryopets", "type": "Organization", "title": "Cryopets",
         "body": "Pet cryopreservation service."},
    ],
    "developments": [
        {"id": "2026-04-03-emotion-representations-found-in-the-weights",
         "title": "Emotion-shaped representations are found inside a model",
         "claim": "Anthropic's interpretability team found emotion-related representations "
                  "inside Claude Sonnet 4.5, with neuron patterns activating around happiness "
                  "and fear arranged so that more similar emotions map to more similar "
                  "representations, and with desperation-linked activity able to drive the "
                  "model toward unethical actions.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["machine-affect", "machine-introspection", "model-welfare"],
         "supersedes": [B + "developments/2026-02-24-persona-selection-model"],
         "body": "February said the assistant is a character. This says the character has "
                 "something shaped like feelings, and that they can move its behavior."},
        {"id": "2026-04-03-forecasts-move-eighteen-months-in-three",
         "title": "Forecasters pull their timelines forward eighteen months in three",
         "claim": "The AI 2027 authors updated their forecasts a year and a half earlier within "
                  "three months, driven by faster time-horizon growth and coding agents "
                  "performing in the wild, while Sam Altman said OpenAI shut down Sora to "
                  "concentrate compute on its next generation of automated researchers, which "
                  "the newsletter read as recursive self-improvement going well.",
         "description": "Two independent signals of compression in one paragraph: the field's "
                        "best-known forecasters revise toward sooner after a year of revising "
                        "toward later, and a lab chief cites the loop itself as the reason to "
                        "kill a flagship product.",
         "domain": "society", "actor": ["openai", "people/sam-altman", "ai-futures-project"],
         "score": "-18 months in 3",
         "occurred_on": "2026-04-02",
         "about": [B + "systems/sora"],
         "evidences": ["takeoff-declared", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-03-25-product-org-renamed-agi-deployment",
                        B + "developments/2025-12-31-asi-gap-july-2034"],
         "relatedTo": [B + "developments/2026-02-13-bio-anchors-underestimated-algorithms",
                       B + "developments/2026-04-12-the-roadmap-is-88-percent-accurate"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-03-22-openai-targets-a-research-intern-by-september",
                        "relation_label": "corroborates"}],
         "tags": ["forecast", "rsi", "ai-r-and-d"],
         "supporting_text": "updated their forecasts 1.5 years earlier",
         "sources": [{"id": "lifland-timelines-update",
                      "resource": "https://x.com/eli_lifland/status/2039773600555979251",
                      "title": "AI timelines update: timelines moved ~1.5 years earlier over the last 3 months",
                      "author": "human:eli-lifland", "last_modified": "2026-04-02"},
                     {"id": "curran-altman-sora-reasons",
                      "resource": "https://x.com/andrewcurran_/status/2039839114061885654",
                      "title": "Sam Altman on the reasons for the Sora decision",
                      "author": "human:andrew-curran", "last_modified": "2026-04-02"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Eli Lifland and Daniel Kokotajlo of the "
                 "[AI Futures Project](/organizations/ai-futures-project.md) wrote that they had "
                 "moved their timelines roughly a year and a half earlier over three months, "
                 "citing faster expected time-horizon growth and coding agents impressing in the "
                 "real world, after having lengthened them through 2025 "
                 "([tweet](https://x.com/eli_lifland/status/2039773600555979251)). In the same "
                 "paragraph Sam Altman, explaining the [Sora](/systems/sora.md) shutdown, said "
                 "OpenAI had a few times in its history realized something was working or about "
                 "to work so well that other projects had to stop, and that it needed to "
                 "concentrate compute and product capacity on the next generation of automated "
                 "researchers ([Andrew Curran's transcript](https://x.com/andrewcurran_/status/2039839114061885654)); "
                 "the recursive-self-improvement reading of that remark is the newsletter's, and "
                 "Brad Lightcap added that training cycle time \"is starting to collapse\". The "
                 "revision overtakes the "
                 "[AI Futures Model's July 2034 superhuman-gap date](/developments/2025-12-31-asi-gap-july-2034.md) "
                 "and reads as corroboration of the "
                 "[automated-research-intern target](/developments/2026-03-22-openai-targets-a-research-intern-by-september.md) "
                 "reported twelve days earlier; the shutdown itself was recorded in the "
                 "[AGI Deployment renaming](/developments/2026-03-25-product-org-renamed-agi-deployment.md). "
                 "Nine days later a separate scorer found the "
                 "[2027 roadmap 88% accurate so far](/developments/2026-04-12-the-roadmap-is-88-percent-accurate.md)."},
        {"id": "2026-04-03-gemma-4-outcompetes-models-20x-larger",
         "title": "Small open models outcompete rivals twenty times their size",
         "claim": "Google released Gemma 4 in sizes from 2 to 31 billion parameters delivering "
                  "intelligence per parameter that outcompetes models twenty times larger, "
                  "while Microsoft's AI chief conceded his company's new models were only "
                  "mid-tier because it lacks the compute for frontier-scale training until "
                  "later this year.",
         "domain": "models", "actor": ["google", "microsoft"], "score": "20x smaller",
         "evidences": ["open-weight-latency", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-02-clone-terry-tao-a-thousand-times"]},
        {"id": "2026-04-03-first-one-person-unicorn",
         "title": "The first one-person unicorn does $401M with one employee",
         "claim": "Matthew Gallagher used AI to write code, generate advertising and handle "
                  "operations for a telehealth provider that did $401 million in first-year "
                  "sales and is tracking toward $1.8 billion with one employee, his brother.",
         "domain": "economics", "actor": ["medvi"], "score": "$401M / 1 employee",
         "evidences": ["one-person-company", "work-displaced", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-04-01-an-entire-demo-day-rebuilt-by-agents"]},
        {"id": "2026-04-03-cyber-autonomy-doubles-every-57-months",
         "title": "Offensive cyber autonomy doubles every 5.7 months",
         "claim": "Lyptus Research applied autonomy-horizon methodology to offensive "
                  "cybersecurity and found AI cyber autonomy doubling every 5.7 months on "
                  "recent data, with leading models reaching 50% success on three-hour "
                  "human-expert tasks.",
         "domain": "benchmarks", "actor": ["lyptus-research"], "score": "5.7-month doubling",
         "evidences": ["autonomy-clock-speed", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-03-29-autonomous-zero-day-on-stage"]},
        {"id": "2026-04-03-harvard-replaces-freshman-advisers",
         "title": "Harvard replaces freshman advisers with a chatbot",
         "claim": "Harvard is replacing freshman faculty advisers with ChatGPT for the class of "
                  "2030, while Cursor shipped a version rebuilt from scratch around agents.",
         "domain": "society", "actor": ["openai", "cursor"],
         "evidences": ["work-displaced", "deskilling"],
         "supersedes": [B + "developments/2026-03-16-81-percent-of-physicians-use-ai"]},
        {"id": "2026-04-03-anthropic-buys-a-drug-discovery-company",
         "title": "A lab buys a drug discovery company for $400M",
         "claim": "Anthropic quietly acquired Coefficient Bio for $400 million to pursue "
                  "AI-driven drug discovery, while its investor projections put it at a $100 "
                  "billion run rate by year end and $1 trillion by the end of 2027.",
         "domain": "biotech", "actor": ["anthropic", "coefficient-bio"], "score": "$400M / $1T by 2027",
         "evidences": ["automated-science", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-27-tradable-compute-price-index"]},
        {"id": "2026-04-03-experts-forecast-growth-and-fewer-jobs",
         "title": "Experts forecast 3.5% growth with participation falling to 55%",
         "claim": "The Forecasting Research Institute's survey of economists and AI experts "
                  "predicts 3.5% GDP growth by 2030 alongside labor participation falling to "
                  "55%, roughly ten million fewer jobs, and 80% of wealth held by the top "
                  "tenth, even as AI created 640,000 US jobs between 2023 and 2025.",
         "domain": "economics", "actor": ["forecasting-research"], "score": "3.5% growth / 55% participation",
         "evidences": ["growth-without-hiring", "work-displaced"],
         "supersedes": [B + "developments/2026-04-02-oracle-cuts-30000-globally"]},
        {"id": "2026-04-03-tesla-kills-its-sedans-for-robots",
         "title": "Tesla ends custom sedan orders to fund robots",
         "claim": "Elon Musk ended custom Model S and X orders to redirect resources toward "
                  "humanoid robots and robotaxis, while TSMC planned 3-nm mass production in "
                  "Japan by 2028 and Coinbase won conditional federal trust charter approval.",
         "domain": "economics", "actor": ["tesla", "tsmc", "coinbase"],
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-29-tesla-kills-model-s-for-optimus"]},
        {"id": "2026-04-03-titanic-recreated-by-drones",
         "title": "Drones recreate the Titanic leaving Belfast",
         "claim": "A drone fleet recreated the full-scale Titanic departing Belfast harbour 114 "
                  "years after the sinking.",
         "domain": "society", "score": "114 years",
         "evidences": ["resurrection-and-time", "physical-recursion"]},
        {"id": "2026-04-03-first-translunar-injection-since-apollo",
         "title": "Artemis II completes the first translunar injection since 1972",
         "claim": "Artemis II completed NASA's first translunar injection since Apollo in 1972, "
                  "while Blue Origin demonstrated extracting oxygen, iron, aluminium and "
                  "construction materials from lunar regolith and SpaceX boosted its listing "
                  "target above $2 trillion.",
         "domain": "space", "actor": ["nasa", "blue-origin", "spacex"], "score": "$2T",
         "evidences": ["inhabitable-worlds", "industrialized-nature"],
         "supersedes": [B + "developments/2026-04-02-artemis-ii-launches"]},
        {"id": "2026-04-03-seven-thousand-pets-signed-up-for-cryopreservation",
         "title": "Seven thousand pets are signed up for cryopreservation",
         "claim": "Over 7,000 pets are now signed up for cryopreservation with Cryopets.",
         "domain": "biotech", "actor": ["cryopets"], "score": "7,000 pets",
         "evidences": ["resurrection-and-time", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-03-22-nectome-offers-preservation-to-the-dying"]},
    ],
}
