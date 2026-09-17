"""Issue 181 — 2026-08-06. A terawatt of compute under one roof."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-6-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-06", "title": "Welcome to August 6, 2026", "url": URL,
        "thesis": "Weights are policed; taste is not.",
        "body": """
# Welcome to August 6, 2026

SpaceX confirmed Terafab — logic, memory and packaging under one roof, opening
at $16.8 billion and scaling toward 100 million square feet and a terawatt a
year of AI compute for Earth and orbit.

The quieter story: the labeling shops that sell judgment to American labs and
federal buyers also sell datasets and rubrics to Chinese giants, a $500 million
trade with almost none of the scrutiny aimed at chips. Weights are policed,
taste is not.
""",
    },
    "themes": [
        {"id": "taste-is-unpoliced", "type": "Theme",
         "title": "Judgment moves freely where weights cannot",
         "first_seen": "2026-08-06", "domain": "policy",
         "body": "Export controls track chips and model files, but the labeled "
                 "preferences and rubrics that teach a model what good looks like "
                 "cross borders as ordinary services. The scarcest input to alignment "
                 "is the one nobody is counting."},
        {"id": "biology-as-compile-target", "type": "Theme",
         "title": "Whole genomes designed from scratch",
         "first_seen": "2026-08-06", "domain": "biotech",
         "body": "Not editing an organism but writing one: language models emitting "
                 "complete functional genomes that outperform what evolution "
                 "supplied. Design replaces discovery at the level of the whole "
                 "organism."},
    ],
    "organizations": [
        {"id": "taalas-inc", "type": "Organization", "title": "Taalas"},
        {"id": "kc-fed", "type": "Organization", "title": "Federal Reserve Bank of Kansas City"},
        {"id": "penn", "type": "Organization", "title": "University of Pennsylvania"},
        {"id": "echostar", "type": "Organization", "title": "EchoStar"},
        {"id": "suno-inc", "type": "Organization", "title": "Suno"},
    ],
    "developments": [
        {"id": "2026-08-06-a-terawatt-of-compute-under-one-roof",
         "title": "A fab breaks ground aiming at a terawatt a year of AI compute",
         "claim": "SpaceX confirmed Terafab, a logic, memory and packaging plant under one roof, "
                  "opening at $16.8 billion and 3,000 jobs and scaling toward 100 million square "
                  "feet and a terawatt a year of AI compute for Earth and orbit, with output "
                  "splitting roughly 25% to humanoids and 75% to AI spacecraft.",
         "domain": "compute", "actor": ["spacex", "asml"], "score": "$16.8B / 1 TW per year",
         "evidences": ["compute-capital-stack", "vertical-silicon", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-08-05-a-buyer-inverts-the-diversification-playbook"],
         "body": "The rationale is scarcity: America has no high-volume memory fabs, "
                 "and incumbent best cases fall short."},
        {"id": "2026-08-06-weights-etched-into-silicon",
         "title": "A chipmaker buys a startup that etches model weights into silicon",
         "claim": "AMD bought Toronto's Taalas, which etches weights into silicon rather than "
                  "using high-bandwidth memory, after a 6nm chip served an 8B model at almost "
                  "17,000 tokens a second, each chip locked to one model until re-spin, while "
                  "Nvidia weighed the blunter fix of less memory in its next architecture.",
         "domain": "compute", "actor": ["amd", "taalas-inc", "nvidia"], "score": "~17,000 tok/s",
         "evidences": ["vertical-silicon", "intelligence-per-watt", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-08-06-a-terawatt-of-compute-under-one-roof"]},
        {"id": "2026-08-06-weights-are-policed-taste-is-not",
         "title": "Labeling shops sell judgment to both sides with no chip-level scrutiny",
         "claim": "The labeling shops serving American labs and federal buyers also sell datasets "
                  "and rubrics to Tencent, ByteDance, Alibaba and Ant, a $500 million trade with "
                  "almost none of the scrutiny aimed at chips.",
         "domain": "policy", "actor": ["tencent", "bytedance", "alibaba", "ant-group"],
         "score": "$500M trade",
         "evidences": ["taste-is-unpoliced", "silicon-curtain", "data-beyond-text"],
         "supersedes": [B + "developments/2026-08-05-open-models-excluded-from-a-review-framework"]},
        {"id": "2026-08-06-a-model-lands-on-the-cost-per-task-frontier",
         "title": "A third release in four months lands on the cost-per-task frontier",
         "claim": "Meta's Muse Spark 1.2 hit 54 on the Intelligence Index, its third release in "
                  "four months, with agentic work up 260 Elo past Opus 4.8, landing six points "
                  "below Claude Opus 5 at roughly one sixth the cost.",
         "domain": "models", "actor": ["meta", "anthropic"], "score": "1/6 the cost",
         "evidences": ["price-implosion", "intelligence-per-watt", "monoculture-is-the-vulnerability"],
         "supersedes": [B + "developments/2026-08-01-opus-level-coding-at-eighteen-cents"]},
        {"id": "2026-08-06-a-vendor-neutral-spec-for-agent-plugins",
         "title": "A vendor-neutral spec packs skills and servers into portable bundles",
         "claim": "OpenAI published Agent Plugins, a vendor-neutral spec packing Skills and MCP "
                  "servers into bundles any client can load, steered by Amazon, Cursor, Microsoft "
                  "and Vercel.",
         "domain": "agents", "actor": ["openai", "amazon", "anysphere", "microsoft", "vercel"],
         "evidences": ["agent-society", "network-over-node", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-07-15-payments-embedded-into-http-for-agents"]},
        {"id": "2026-08-06-twenty-five-billion-of-bonds-into-a-hundred-fifteen-billion-of-demand",
         "title": "A hyperscaler sells $25 billion of bonds into $115 billion of demand",
         "claim": "Alphabet sold $25 billion of bonds into $115 billion of peak demand, days "
                  "after its first ever negative free cash flow and capital guidance of $195 to "
                  "$205 billion, as a Fed official warned the financing could create a systemic "
                  "problem and asked whether AI is becoming too big to fail.",
         "domain": "economics", "actor": ["alphabet", "kc-fed"], "score": "$25B into $115B demand",
         "evidences": ["debt-funded-buildout", "risk-becomes-uninsurable", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-08-02-twenty-million-chips-doubling-every-nine-months"]},
        {"id": "2026-08-06-a-lab-hires-an-insider-risk-investigator",
         "title": "A lab will pay $305,000 to hunt exfiltration by its own staff",
         "claim": "Anthropic will pay up to $305,000 for an Insider Risk Investigator to "
                  "interview its own staff and hunt exfiltration in its logs, with nation-state "
                  "tradecraft preferred, as US imports of Saudi crude hit zero in July for the "
                  "first empty month since 1985.",
         "domain": "policy", "actor": ["anthropic"], "score": "$305,000",
         "evidences": ["dark-forest-research", "war-reaches-the-cloud", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-08-05-twenty-gigawatts-and-robot-factories-on-the-moon"]},
        {"id": "2026-08-06-whole-phages-designed-from-scratch",
         "title": "Genome language models design whole functional phages",
         "claim": "Researchers used genome language models to design whole phages, yielding 16 "
                  "functional genomes whose cocktail beat bacteria already resistant to a natural "
                  "phage, a first at genome scale.",
         "domain": "biotech", "score": "16 functional genomes",
         "evidences": ["biology-as-compile-target", "compiling-matter", "built-not-inherited"],
         "supersedes": [B + "developments/2026-07-29-a-first-hiv-vaccine-raising-broad-antibodies"]},
        {"id": "2026-08-06-the-first-us-mrna-flu-shot",
         "title": "A regulator approves the first US mRNA flu vaccine",
         "claim": "The FDA approved Moderna's mFlusiva, the first US mRNA flu shot, 27% better "
                  "than a standard dose and re-matchable to a new strain in two to three months "
                  "rather than six, while an engineered bean gum cut HPV by 93% in patient "
                  "saliva.",
         "domain": "biotech", "actor": ["fda", "penn"], "score": "+27% / -93% HPV",
         "evidences": ["hardware-grade-biology", "biology-as-compile-target"],
         "supersedes": [B + "developments/2026-08-06-whole-phages-designed-from-scratch"]},
        {"id": "2026-08-06-a-network-rebuilt-without-towers",
         "title": "A constellation will bolt femtocells onto dishes and chargers instead of towers",
         "claim": "SpaceX will bolt femtocells onto existing Starlink dishes, gateways and "
                  "Superchargers, using EchoStar's spectrum backhauled over the same link, so "
                  "phones reach rooftops rather than leased towers by late 2027.",
         "domain": "space", "actor": ["spacex", "echostar", "tesla"], "score": "65 MHz",
         "evidences": ["network-over-node", "orbit-as-compute", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-08-05-twenty-gigawatts-and-robot-factories-on-the-moon"]},
        {"id": "2026-08-06-a-decade-of-forecasting-progress-open-sourced",
         "title": "A weather model buys an extra day of cyclone lead time and is open-sourced",
         "claim": "DeepMind's WeatherNext set the state of the art on cyclone track, intensity and "
                  "wind structure, buying an extra day of lead time — a decade of progress — and "
                  "was open-sourced.",
         "domain": "science", "actor": ["google-deepmind"], "score": "+1 day lead time",
         "evidences": ["automated-science", "open-weight-latency", "industrialized-nature"],
         "supersedes": [B + "developments/2026-08-02-wild-monkeys-recognized-and-paid-in-banana"]},
        {"id": "2026-08-06-earth-kept-habitable-for-nine-million-billion-years",
         "title": "A paper prices megaengineering to keep Earth habitable far past its natural span",
         "claim": "A new paper prices megaengineering fixes for seven long-run threats, from "
                  "rising solar luminosity to the end of plate tectonics, keeping Earth habitable "
                  "for 9.1 million billion years, longer still if mass is lifted off the Sun.",
         "domain": "science", "score": "9.1 million billion years",
         "evidences": ["inhabitable-worlds", "industrialized-nature", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-08-06-a-decade-of-forecasting-progress-open-sourced"]},
    ],
}
