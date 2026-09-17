"""Issue 028 — 2026-01-09. Growth without hiring."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-9-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-09", "title": "Welcome to January 9, 2026", "url": URL,
        "thesis": "The expansion arrives, and it is jobless.",
        "body": """
# Welcome to January 9, 2026

The Atlanta Fed doubles its Q4 forecast from 2.7% to 5.4%. Productivity rises
4.9% while hours worked stay flat. Firms are scaling silicon instead of
headcount, and the macro data finally shows it.

The counterweight is the strangest item in the batch: removing rote work has
left humans with nothing but high-intensity decisions, and CEOs report their
staff are mentally finished by Friday. The micro-breaks were load-bearing.
""",
    },
    "themes": [
        {"id": "growth-without-hiring", "type": "Theme",
         "title": "Output rises while headcount does not",
         "first_seen": "2026-01-09", "domain": "economics",
         "body": "GDP and productivity climb with hours worked flat. The expansion is real and "
                 "the jobs do not follow, breaking the link between growth and employment that "
                 "every post-war policy assumes."},
        {"id": "cognitive-load-inverted", "type": "Theme",
         "title": "Automating the boring parts removes the rest",
         "first_seen": "2026-01-09", "domain": "society",
         "body": "Rote work was also recovery time. Strip it out and what remains is unbroken "
                 "high-intensity judgment, which humans cannot sustain across a week."},
    ],
    "organizations": [
        {"id": "atlanta-fed", "type": "Organization", "title": "Federal Reserve Bank of Atlanta",
         "resource": "https://www.atlantafed.org/"},
        {"id": "vistra", "type": "Organization", "title": "Vistra",
         "resource": "https://www.vistracorp.com/"},
        {"id": "terrapower", "type": "Organization", "title": "TerraPower",
         "resource": "https://www.terrapower.com/"},
        {"id": "oklo", "type": "Organization", "title": "Oklo", "resource": "https://oklo.com/"},
        {"id": "lambda", "type": "Organization", "title": "Lambda",
         "resource": "https://lambda.ai/", "body": "GPU cloud renting Nvidia capacity."},
        {"id": "paypal", "type": "Organization", "title": "PayPal",
         "resource": "https://www.paypal.com/"},
        {"id": "stripe", "type": "Organization", "title": "Stripe",
         "resource": "https://stripe.com/"},
        {"id": "schmidt-sciences", "type": "Organization", "title": "Schmidt Sciences",
         "resource": "https://www.schmidtsciences.org/"},
        {"id": "fcc", "type": "Organization", "title": "FCC", "resource": "https://www.fcc.gov/"},
        {"id": "illinois", "type": "Organization", "title": "State of Illinois",
         "resource": "https://illinois.gov/"},
    ],
    "facilities": [
        {"id": "macrohardrr", "type": "Facility", "title": "MACROHARDRR",
         "operated_by": [B + "organizations/xai"], "located_in": "Mississippi, USA",
         "capacity": "$20B investment",
         "body": "xAI's Mississippi datacenter, the largest investment in state history."},
        {"id": "micron-new-york-megafab", "type": "Facility", "title": "Micron New York megafab",
         "operated_by": [B + "organizations/micron"], "located_in": "New York, USA",
         "capacity": "$100B"},
    ],
    "developments": [
        {"id": "2026-01-09-15m-h100-equivalents",
         "title": "Earth passes 15 million H100-equivalents",
         "claim": "Epoch AI estimated humanity's total AI compute has passed 15 million "
                  "H100-equivalents, putting Earth's AI processing density at 10^-14 MIPS per "
                  "milligram.",
         "domain": "compute", "actor": ["epoch-ai"], "score": "15M H100e",
         "evidences": ["compute-capital-stack", "orbit-as-compute"],
         "body": "A planetary quantity, stated as a density — the framing the newsletter uses "
                 "to point at the Solar System as the next denominator."},
        {"id": "2026-01-09-atlanta-fed-doubles-forecast",
         "title": "The Atlanta Fed doubles its growth forecast",
         "claim": "The Atlanta Fed doubled its Q4 2025 GDP forecast from 2.7% to 5.4%.",
         "domain": "economics", "actor": ["atlanta-fed"], "score": "2.7% → 5.4%",
         "evidences": ["growth-without-hiring", "compute-capital-stack"]},
        {"id": "2026-01-09-productivity-up-hours-flat",
         "title": "Productivity jumps 4.9% with hours worked flat",
         "claim": "Labor productivity rose 4.9% while hours worked stayed flat, indicating "
                  "firms are scaling silicon rather than headcount.",
         "domain": "economics", "score": "+4.9% productivity, 0% hours",
         "evidences": ["growth-without-hiring", "work-displaced"],
         "supersedes": [B + "developments/2026-01-08-keynesian-demand-collapse-warning"],
         "body": "The warning of a demand collapse and the evidence for it land a day apart."},
        {"id": "2026-01-09-xai-macrohardrr",
         "title": "xAI puts $20B into a Mississippi datacenter",
         "claim": "xAI is investing $20 billion in a Mississippi data center called MACROHARDRR, "
                  "the largest investment in state history, while building Colossus 3 faster "
                  "than Colossus 1's 122-day record.",
         "domain": "compute", "actor": ["xai"], "about": [B + "facilities/macrohardrr"],
         "score": "$20B", "evidences": ["compute-capital-stack", "capital-takes-the-plant"]},
        {"id": "2026-01-09-meta-66gw-nuclear",
         "title": "Meta contracts 6.6 GW of nuclear",
         "claim": "Meta signed agreements for 6.6 GW of nuclear energy with Vistra, TerraPower "
                  "and Oklo through 2035, as Illinois lifted its moratorium on new construction.",
         "domain": "energy", "actor": ["meta", "vistra", "terrapower", "oklo", "illinois"],
         "score": "6.6 GW",
         "evidences": ["burning-molecules-for-tokens", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-01-06-xai-five-gas-turbines"]},
        {"id": "2026-01-09-micron-100b-megafab",
         "title": "Micron breaks ground on a $100B megafab",
         "claim": "Micron broke ground on a $100 billion megafab in New York as Intel began "
                  "shipping sub-2-nm 18A products, returning leading-edge lithography to the US.",
         "domain": "compute", "actor": ["micron", "intel"],
         "about": [B + "facilities/micron-new-york-megafab"], "score": "$100B",
         "evidences": ["silicon-curtain", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-01-06-intel-18a-core-ultra-3"]},
        {"id": "2026-01-09-openai-eight-months-to-intern-researchers",
         "title": "OpenAI is reportedly eight months from intern-level researchers",
         "claim": "OpenAI is reportedly at most eight months away from AI researchers at intern "
                  "level.",
         "description": "The newsletter's flat statement that recursive self-improvement is "
                        "imminent gets its first calendar date: a lab's own horizon for "
                        "automating the junior end of its research staff.",
         "domain": "agents", "actor": ["openai"], "score": "≤8 months",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2025-12-28-altman-self-improving-in-production"],
         "relatedTo": [B + "people/sam-altman",
                       B + "developments/2026-03-22-openai-targets-a-research-intern-by-september",
                       B + "developments/2026-09-07-three-agent-workdays-per-human-workday"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-01-09-tao-calls-erdos-728-a-milestone",
                        "relation_label": "corroborates"}],
         "tags": ["rsi", "ai-r-and-d", "forecast"],
         "supporting_text": "OpenAI is reportedly at most [8 months away]",
         "sources": [{"id": "techcrunch-altman-legitimate-ai-researcher-2028",
                      "resource": "https://techcrunch.com/2025/10/28/sam-altman-says-openai-will-have-a-legitimate-ai-researcher-by-2028/",
                      "title": "Sam Altman says OpenAI will have a 'legitimate AI researcher' by 2028",
                      "author": "org:techcrunch", "last_modified": "2025-10-28"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The figure traces to Sam Altman's livestream of 28 October 2025, where he said "
                 "OpenAI was tracking toward an intern-level research assistant by September 2026 "
                 "and a fully automated \"legitimate AI researcher\" by 2028 "
                 "([TechCrunch](https://techcrunch.com/2025/10/28/sam-altman-says-openai-will-have-a-legitimate-ai-researcher-by-2028/)); "
                 "counted from this issue, September is eight months out. It is the first dated "
                 "internal timeline for an automated researcher in the corpus, following "
                 "[Altman's confirmation](/developments/2025-12-28-altman-self-improving-in-production.md) "
                 "that self-improving systems already run in production, and the newsletter pairs it "
                 "with [Tao's \"milestone\" verdict](/developments/2026-01-09-tao-calls-erdos-728-a-milestone.md) "
                 "as evidence the capability is already here. OpenAI restated the "
                 "[September intern target](/developments/2026-03-22-openai-targets-a-research-intern-by-september.md) "
                 "in March and in September reported the intern "
                 "[delivering 3.1 agent-workdays per human workday](/developments/2026-09-07-three-agent-workdays-per-human-workday.md), "
                 "closing the loop this item opened under "
                 "[recursive self-improvement](/themes/recursive-self-improvement.md)."},
        {"id": "2026-01-09-tao-calls-erdos-728-a-milestone",
         "title": "Tao calls the Erdős #728 solution a milestone",
         "claim": "Terry Tao called the AI solution to Erdős problem #728 a milestone, noting "
                  "the model rapidly rewrote its own mathematical expositions.",
         "domain": "science", "actor": ["people/terry-tao"],
         "evidences": ["automated-science", "machine-introspection"],
         "supersedes": [B + "developments/2026-01-08-math-inc-autoformalizes-tao"]},
        {"id": "2026-01-09-agents-create-4x-more-databases",
         "title": "Agents create four times more databases than humans",
         "claim": "AI agents on Databricks are now creating four times as many databases as "
                  "humans, taking over the administration of stored data.",
         "domain": "agents", "actor": ["databricks"], "score": "4x",
         "evidences": ["autonomous-commerce", "work-displaced"]},
        {"id": "2026-01-09-amazon-more-robots-than-employees",
         "title": "Amazon is on track for more robots than employees",
         "claim": "ARK Invest noted Amazon is on track to have more robots than human employees "
                  "within a few years, with global humanoid shipments projected at 2.6 million "
                  "by 2035 and xAI telling investors Grok will power Tesla's Optimus fleet.",
         "domain": "robotics", "actor": ["ark-invest", "amazon", "xai", "tesla"],
         "score": "2.6M humanoids by 2035",
         "evidences": ["work-displaced", "physical-recursion"],
         "supersedes": [B + "developments/2026-01-06-hyundai-30000-atlas-a-year"]},
        {"id": "2026-01-09-lambda-350m-raise",
         "title": "Lambda raises $350M to rent GPUs",
         "claim": "Lambda is raising another $350 million to rent Nvidia chips to the highest "
                  "bidder.",
         "domain": "economics", "actor": ["lambda"], "score": "$350M",
         "evidences": ["compute-capital-stack"]},
        {"id": "2026-01-09-copilot-checkout",
         "title": "Checkout moves inside the chat window",
         "claim": "Microsoft launched Copilot Checkout with PayPal and Stripe embedded directly "
                  "in AI chat, while Google replaced the inbox list with a Gemini summary view.",
         "domain": "economics", "actor": ["microsoft", "paypal", "stripe", "google"],
         "evidences": ["autonomous-commerce", "intimate-interface"],
         "supersedes": [B + "developments/2026-01-06-edge-becomes-a-copilot-app"]},
        {"id": "2026-01-09-stablecoin-volume-33t",
         "title": "Stablecoin volume reaches $33 trillion",
         "claim": "Stablecoin volume hit $33 trillion in 2025, marking the mass digitization of "
                  "the dollar.",
         "domain": "economics", "score": "$33T",
         "evidences": ["autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-05-pwc-pitches-stablecoins"]},
        {"id": "2026-01-09-private-telescope-larger-than-hubble",
         "title": "A private telescope larger than Hubble is funded",
         "claim": "Schmidt Sciences is funding a private space telescope larger than Hubble, "
                  "decoupling astronomy from government budgets.",
         "domain": "space", "actor": ["schmidt-sciences"],
         "evidences": ["science-as-industrial-policy", "capital-takes-the-plant"]},
        {"id": "2026-01-09-openai-for-healthcare",
         "title": "OpenAI launches a healthcare arm with hospital systems",
         "claim": "OpenAI launched OpenAI for Healthcare with major hospital systems to ground "
                  "medical models in clinical reality.",
         "domain": "society", "actor": ["openai"],
         "evidences": ["intimate-interface", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-01-08-chatgpt-health-emr"]},
        {"id": "2026-01-09-photonic-octopus-skin",
         "title": "Synthetic skin changes color and texture like an octopus",
         "claim": "Stanford researchers created the first synthetic octopus-like photonic skin "
                  "that changes both color and texture, as the FCC authorized high-power 6 GHz "
                  "outdoor Wi-Fi for AR geofencing.",
         "domain": "science", "actor": ["stanford", "fcc"],
         "evidences": ["compiling-matter", "biosphere-uplift"]},
        {"id": "2026-01-09-gifted-word-learner-dogs",
         "title": "Some dogs learn words like toddlers",
         "claim": "Austrian researchers found some dogs are gifted word learners with "
                  "sociocognitive skills parallel to eighteen-month-old humans.",
         "domain": "science", "evidences": ["biosphere-uplift", "architecture-of-mind"]},
        {"id": "2026-01-09-cognitive-burnout",
         "title": "Productivity rises 20% and staff are finished by Friday",
         "claim": "CEOs report productivity up 20% alongside employee cognitive burnout, "
                  "because removing rote work stripped out the micro-breaks that made a week "
                  "sustainable.",
         "domain": "society", "score": "+20% productivity",
         "evidences": ["cognitive-load-inverted", "work-displaced", "growth-without-hiring"],
         "body": "The first item in the corpus to name a cost of automation borne by the people "
                 "who kept their jobs."},
    ],
}
