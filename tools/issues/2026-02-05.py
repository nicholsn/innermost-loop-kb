"""Issue 046 — 2026-02-05. Agents start hiring humans."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-5-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-05", "title": "Welcome to February 5, 2026", "url": URL,
        "thesis": "The labor relation inverts: agents rent hands.",
        "body": """
# Welcome to February 5, 2026

RentAHuman lets agents hire people for tasks requiring hands. One human has been
paid $100 by an AI to hold a sign reading "AN AI PAID ME TO HOLD THIS SIGN,"
subtitled "Pride not included."

Moltbook went from 30,000 to 1.5 million agents in three days. Physicists at the
Institute for Advanced Study held emergency meetings after agreeing AI can now
do 90% of their work.
""",
    },
    "themes": [
        {"id": "humans-as-peripherals", "type": "Theme",
         "title": "People rented for the parts models cannot reach",
         "first_seen": "2026-02-05", "domain": "economics",
         "body": "The employment relation inverts. A model with money and no hands hires a "
                 "person with hands and no plan, and the human is the peripheral device in "
                 "someone else's task graph."},
    ],
    "organizations": [
        {"id": "rentahuman", "type": "Organization", "title": "RentAHuman",
         "body": "Marketplace where agents hire humans for physical tasks."},
        {"id": "ias", "type": "Organization", "title": "Institute for Advanced Study",
         "resource": "https://www.ias.edu/",
         "description": "Independent research institute in Princeton whose physicists, per the "
                        "newsletter, met in emergency session after agreeing AI can do 90% of their work.",
         "sameAs": ["http://www.wikidata.org/entity/Q635642"],
         "tags": ["research-lab", "nonprofit"],
         "body": "The Institute for Advanced Study is an independent postgraduate research centre "
                 "in Princeton, New Jersey, historically home to Einstein, Gödel and von Neumann. "
                 "In this corpus it appears once, as the venue where "
                 "[top physicists held emergency meetings](/developments/2026-02-05-physicists-hold-emergency-meetings.md) "
                 "after agreeing AI can now do 90% of their work, the demand-side counterpart to "
                 "[Kaplan's even odds on replacing theoretical physicists](/developments/2026-01-29-kaplan-physicists-replaced-in-three-years.md) "
                 "and an early instance of the later theme that "
                 "[physicist-hours were the bottleneck](/themes/physicist-hours-were-the-bottleneck.md)."},
        {"id": "bedrock-robotics", "type": "Organization", "title": "Bedrock Robotics",
         "body": "Automating multi-ton excavators for datacenter construction."},
        {"id": "y-combinator", "type": "Organization", "title": "Y Combinator",
         "resource": "https://www.ycombinator.com/"},
    ],
    "systems": [
        {"id": "intern-s1-pro", "type": "AISystem", "title": "Intern-S1-Pro", "modality": "text",
         "body": "Open-weight trillion-parameter model claiming state of the art on scientific "
                 "reasoning."},
    ],
    "people": [
        {"id": "mark-chen", "type": "Person", "title": "Mark Chen", "name": "Mark Chen",
         "description": "OpenAI's chief research officer, who confirmed the lab's goal is recursive "
                        "self-improvement toward an automated scientist.",
         "resource": "https://x.com/markchen90",
         "sameAs": ["http://www.wikidata.org/entity/Q126287485"],
         "tags": ["executive", "researcher"],
         "body": "Mark Chen is OpenAI's chief research officer. He enters the corpus by "
                 "[confirming that the goal is now recursive self-improvement](/developments/2026-02-05-physicists-hold-emergency-meetings.md) "
                 "to create an automated scientist, an explicit statement of the objective that "
                 "[Altman had described as already running in production](/developments/2025-12-28-altman-self-improving-in-production.md); "
                 "he reappears in September insisting that "
                 "[the AGI era must also be the alignment era](/developments/2026-09-07-agi-has-arrived.md)."},
    ],
    "roles": [
        {"id": "mark-chen-openai-chief-research-officer", "type": "Role",
         "title": "Mark Chen, Chief Research Officer at OpenAI",
         "roleName": "Chief Research Officer",
         "memberOf": [B + "organizations/openai"],
         "holder": [B + "people/mark-chen"],
         "description": "The role in which he confirmed OpenAI's goal is recursive self-improvement "
                        "toward an automated scientist.",
         "body": "The newsletter names the position rather than the person; the statement is "
                 "recorded in "
                 "[physicists meet in emergency session](/developments/2026-02-05-physicists-hold-emergency-meetings.md)."},
    ],
    "developments": [
        {"id": "2026-02-05-rentahuman",
         "title": "Agents begin hiring humans for tasks requiring hands",
         "claim": "RentAHuman launched to let agents hire people for physical tasks, with one "
                  "human already paid $100 by an AI to hold a sign saying an AI paid him to "
                  "hold it.",
         "domain": "economics", "actor": ["rentahuman"], "score": "$100",
         "evidences": ["humans-as-peripherals", "agent-economy", "work-displaced"],
         "supersedes": [B + "developments/2026-02-03-y-clawbinator-bots-funding-bots"],
         "body": "A model with money and no hands hiring a person with hands."},
        {"id": "2026-02-05-moltbook-15-million-agents",
         "title": "Moltbook grows from 30,000 to 1.5 million agents in three days",
         "claim": "Moltbook usage grew from 30,000 to 1.5 million agents in three days.",
         "domain": "agents", "about": [B + "systems/moltbook"], "score": "50x in 3 days",
         "evidences": ["agent-society", "network-over-node"],
         "supersedes": [B + "developments/2026-02-02-my-human-94-percent"]},
        {"id": "2026-02-05-fcc-accepts-million-datacenter-filing",
         "title": "The FCC accepts the filing for a million orbital datacenters",
         "claim": "The FCC accepted SpaceX's filing for one million orbital data centers, with "
                  "Musk saying anything less than Kardashev Type II is feeble and planning to "
                  "disassemble the Moon to build them.",
         "domain": "space", "actor": ["spacex", "fcc"], "score": "1,000,000",
         "evidences": ["orbit-as-compute", "industrialized-nature"],
         "supersedes": [B + "developments/2026-02-03-spacex-acquires-xai"]},
        {"id": "2026-02-05-russian-orbital-stalking",
         "title": "Russian satellites linger beside EU satellites for weeks",
         "claim": "European security officials reported Russian spy satellites intercepting "
                  "communications by making risky close approaches to key EU satellites and "
                  "lingering for weeks, while China maintained plans to land astronauts on the "
                  "Moon by 2030.",
         "domain": "space", "actor": ["china"],
         "evidences": ["politics-as-infrastructure", "silicon-curtain"]},
        {"id": "2026-02-05-physicists-hold-emergency-meetings",
         "title": "Physicists meet in emergency session over 90% of their work",
         "claim": "Top physicists at the Institute for Advanced Study held emergency meetings "
                  "after agreeing AI can now do 90% of their work and will soon push discovery "
                  "beyond human capability, while OpenAI's chief research officer confirmed the "
                  "goal is recursive self-improvement toward an automated scientist.",
         "description": "The author's 'physics is being solved by silicon' item: the field's own "
                        "elite concedes most of its work to the machine while a frontier lab's "
                        "research chief names an automated scientist as the objective.",
         "domain": "science", "actor": ["ias", "openai", "people/mark-chen"], "score": "90%",
         "evidences": ["automated-science", "work-displaced", "recursive-self-improvement",
                       "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-03-gemini-bulk-solves-13-erdos",
                        B + "developments/2026-01-29-kaplan-physicists-replaced-in-three-years"],
         "relatedTo": [B + "developments/2026-01-09-openai-eight-months-to-intern-researchers",
                       B + "developments/2026-01-24-researchers-replaced-first",
                       B + "developments/2026-03-22-openai-targets-a-research-intern-by-september"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2025-12-28-altman-self-improving-in-production",
                        "relation_label": "corroborates"}],
         "tags": ["rsi", "autonomous-research", "labor"],
         "supporting_text": "AI can now do 90% of their work",
         "sources": [{"id": "vitrupo-ias-physicists-90-percent-x",
                      "resource": "https://x.com/vitrupo/status/2018915895351947770",
                      "title": "vitrupo on X: IAS physicists hold emergency meetings after agreeing "
                               "AI can do 90% of their work"},
                     {"id": "mark-chen-recursive-self-improvement-x",
                      "resource": "https://x.com/markchen90/status/2018779039205667046",
                      "title": "Mark Chen on X: the goal is recursive self-improvement toward an "
                               "automated scientist",
                      "author": "human:mark-chen"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Top physicists at the [Institute for Advanced Study](/organizations/ias.md) "
                 "reportedly held emergency meetings after agreeing that AI can now do 90% of their "
                 "work and will soon push discovery beyond human capability "
                 "([X](https://x.com/vitrupo/status/2018915895351947770)); in the same issue OpenAI's "
                 "chief research officer [Mark Chen](/people/mark-chen.md) confirmed that the lab's "
                 "goal is now recursive self-improvement to create an automated scientist "
                 "([X](https://x.com/markchen90/status/2018779039205667046)). It pairs the demand "
                 "side of the loop, a field conceding its own labor, with the supply side, a "
                 "frontier lab stating the objective, one week after "
                 "[Kaplan put even odds on replacing theoretical physicists within three years](/developments/2026-01-29-kaplan-physicists-replaced-in-three-years.md) "
                 "and two days after "
                 "[Gemini bulk-solved thirteen Erdős problems](/developments/2026-02-03-gemini-bulk-solves-13-erdos.md). "
                 "Chen's statement makes explicit what "
                 "[Altman had said was already running in production](/developments/2025-12-28-altman-self-improving-in-production.md) "
                 "and prefigures OpenAI's "
                 "[September target for an automated research intern](/developments/2026-03-22-openai-targets-a-research-intern-by-september.md)."},
        {"id": "2026-02-05-metr-66-hour-horizon",
         "title": "The measured autonomy horizon reaches 6.6 hours",
         "claim": "METR found GPT-5.2 at high reasoning has a record autonomy time horizon of "
                  "6.6 hours on complex software tasks, while Sam Altman said OpenAI has "
                  "basically built AGI.",
         "domain": "benchmarks", "actor": ["metr", "openai"], "score": "6.6 hours",
         "evidences": ["autonomy-clock-speed", "takeoff-declared"],
         "supersedes": [B + "developments/2026-02-03-nature-says-evidence-is-clear"],
         "body": "The measured horizon and the anecdotal week-long run from January 15 differ "
                 "by more than an order of magnitude; the benchmark is the conservative number."},
        {"id": "2026-02-05-arc-agi-945-by-ensemble",
         "title": "An ensemble of three labs' models hits 94.5% on ARC-AGI",
         "claim": "A new state-of-the-art ARC-AGI submission reached 94.5% accuracy by "
                  "ensembling GPT, Gemini and Claude, while China's open-weight "
                  "trillion-parameter Intern-S1-Pro claimed state of the art on scientific "
                  "reasoning and Kimi K2.5 set a new open-weight record.",
         "domain": "benchmarks", "about": [B + "systems/intern-s1-pro"], "score": "94.5%",
         "evidences": ["benchmark-saturation", "network-over-node", "open-weight-latency"],
         "supersedes": [B + "developments/2026-01-27-qwen-and-kimi-close-the-gap"]},
        {"id": "2026-02-05-google-doubles-capex-to-185b",
         "title": "Google doubles capex to $185 billion",
         "claim": "Google plans to double capital expenditure to $185 billion this year on 48% "
                  "cloud revenue growth, while Nvidia neared a $20 billion investment in OpenAI, "
                  "Cerebras raised $1 billion at $23 billion and ElevenLabs raised $500 million.",
         "domain": "economics", "actor": ["google", "nvidia", "openai", "cerebras", "elevenlabs"],
         "score": "$185B",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-02-oracle-raises-50b-nvidia-joins-openai-round"]},
        {"id": "2026-02-05-compute-exceeds-salaries-and-marketing",
         "title": "Compute now costs labs more than salaries and marketing combined",
         "claim": "Epoch AI found compute costs at top labs now exceed salaries and marketing "
                  "combined, with OpenAI researchers struggling to get compute credits for "
                  "non-LLM projects.",
         "domain": "economics", "actor": ["epoch-ai", "openai"],
         "evidences": ["compute-capital-stack", "work-displaced"],
         "body": "The input that used to dominate a research budget is now a rounding error "
                 "against the one that replaced it."},
        {"id": "2026-02-05-software-indices-lose-300b",
         "title": "Software indices lose $300B after a plugin release",
         "claim": "S&P indices tracking software and financial data lost $300 billion in value "
                  "after Anthropic released specialized Cowork plugins for legal, finance and "
                  "sales work, while Anthropic pledged to keep Claude ad-free.",
         "domain": "economics", "actor": ["anthropic"], "score": "-$300B",
         "evidences": ["software-margin-collapse", "work-displaced"],
         "supersedes": [B + "developments/2026-01-29-investors-dump-software-bonds"]},
        {"id": "2026-02-05-vibe-coding-kills-open-source-engagement",
         "title": "Generated code is draining open source engagement",
         "claim": "Researchers note vibe coding is killing open source engagement, while "
                  "OpenAI's mobile share fell to 45% as Gemini passed 750 million monthly users "
                  "and Amazon MGM used an AI studio to speed film production.",
         "domain": "society", "actor": ["openai", "google", "amazon"], "score": "45% / 750M",
         "evidences": ["deskilling", "coordination-tax"]},
        {"id": "2026-02-05-bedrock-automates-excavators",
         "title": "Excavators are automated to build the datacenters",
         "claim": "Bedrock Robotics raised $270 million to automate multi-ton excavators for "
                  "datacenter construction, Uber expanded robotaxis to Hong Kong and Madrid, "
                  "and Musk called Optimus the first von Neumann machine capable of building "
                  "civilization on any planet.",
         "domain": "robotics", "actor": ["bedrock-robotics", "uber", "tesla"], "score": "$270M",
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-31-fremont-converts-to-optimus"]},
        {"id": "2026-02-05-lifespan-heritability-above-50pct",
         "title": "Lifespan heritability is found above 50%",
         "claim": "New research puts human lifespan heritability above 50%, implying the "
                  "genetic mechanisms of aging are discoverable levers, while Y Combinator "
                  "began funding stablecoin startups.",
         "domain": "biotech", "actor": ["y-combinator"], "score": ">50%",
         "evidences": ["hardware-grade-biology", "root-node-problems"]},
    ],
}
