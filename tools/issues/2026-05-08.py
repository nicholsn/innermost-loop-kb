"""Issue 110 — 2026-05-08. A rival hands over an entire datacenter."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-8-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-08", "title": "Welcome to May 8, 2026", "url": URL,
        "thesis": "One lab hands a competitor a gigawatt-class datacenter and shuts its own down.",
        "body": """
# Welcome to May 8, 2026

SpaceX handed Anthropic the entire Colossus 1 datacenter — 300+ MW and over
220,000 GPUs — while shutting down xAI as a separate company. Musk vouched for
the Claude team after a week onsite, noting "no one set off my evil detector."

Anthropic grew 80x annualized in the first quarter against a planned 10x. Naive
extrapolation has it absorbing all global GDP in 21 months.
""",
    },
    "organizations": [
        {"id": "corning", "type": "Organization", "title": "Corning",
         "resource": "https://www.corning.com/"},
        {"id": "etrade", "type": "Organization", "title": "E*Trade",
         "resource": "https://us.etrade.com/"},
    ],
    "people": [
        {"id": "tom-brown", "type": "Person", "title": "Tom Brown", "name": "Tom Brown",
         "body": "Anthropic chief compute officer."},
    ],
    "systems": [
        {"id": "claude-managed-agents", "type": "AISystem", "title": "Claude Managed Agents",
         "description": "Anthropic's hosted runtime for deploying Claude agents at scale, with sandboxed "
                        "execution, checkpointing and, from May 2026, a scheduled dreaming process that "
                        "curates shared memories from session histories.",
         "developed_by": [B + "organizations/anthropic"],
         "modality": "text",
         "resource": "https://platform.claude.com/docs/en/managed-agents/overview",
         "tags": ["coding-agent"],
         "body": "Claude Managed Agents is [Anthropic](/organizations/anthropic.md)'s platform of "
                 "composable APIs for running cloud-hosted Claude agents with sandboxed execution, "
                 "checkpointing, scoped credentials and tracing. It enters the corpus in April, when the "
                 "newsletter read its launch as "
                 "[sandbox containment promoted to a product feature](/developments/2026-04-08-sandbox-containment-becomes-a-product-feature.md), "
                 "and returns in May with [dreaming](/developments/2026-05-08-agents-dream-overnight.md), "
                 "the scheduled process that reviews session histories and curates shared memories "
                 "across teams."},
        {"id": "gemini-nano", "type": "AISystem", "title": "Gemini Nano",
         "description": "Google's on-device Gemini model, shipped inside Chrome and on Pixel phones, "
                        "which Chrome began installing as a 4 GB download on every desktop with "
                        "available storage.",
         "developed_by": [B + "organizations/google"],
         "modality": "text",
         "resource": "https://developer.chrome.com/docs/ai/built-in",
         "sameAs": ["http://www.wikidata.org/entity/Q124547180"],
         "body": "Gemini Nano is the smallest member of Google's [Gemini](/systems/gemini.md) family, "
                 "sized to run locally on phones and desktops rather than in a datacenter. In this "
                 "corpus it appears when "
                 "[Chrome started quietly installing 4 GB of it](/developments/2026-05-08-agents-dream-overnight.md) "
                 "on every desktop with room to spare, and again in June when Google "
                 "[bolted multi-token prediction onto the frozen model](/developments/2026-06-27-multi-token-prediction-on-a-frozen-model.md) "
                 "on Pixels for more than 50% faster inference with bit-identical output."},
    ],
    "developments": [
        {"id": "2026-05-08-a-rival-hands-over-colossus-1",
         "title": "SpaceX hands a competitor a 300-MW datacenter and closes its own lab",
         "claim": "Anthropic signed a partnership with SpaceX handing it the entire Colossus 1 "
                  "data center, unlocking over 300 MW and more than 220,000 GPUs within the "
                  "month and doubling Claude Code rate limits, while Elon Musk shut down xAI as "
                  "a separate company and vouched for the Claude team after a week onsite.",
         "domain": "compute", "actor": ["spacex", "anthropic", "xai"], "score": "300 MW / 220,000 GPUs",
         "evidences": ["compute-capital-stack", "coordination-tax"],
         "supersedes": [B + "developments/2026-05-06-a-single-contract-is-forty-percent-of-a-backlog"]},
        {"id": "2026-05-08-multiple-gigawatts-of-orbital-compute",
         "title": "The deal extends to multiple gigawatts of orbital compute",
         "claim": "SpaceX confirmed the Anthropic deal extends into multiple gigawatts of "
                  "orbital AI compute because terrestrial power, land and cooling no longer "
                  "match the required cadence, with Anthropic's chief compute officer "
                  "summarizing the play as moving a lot of atoms, ideally off-planet.",
         "domain": "space", "actor": ["spacex", "anthropic", "people/tom-brown"],
         "evidences": ["orbit-as-compute", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-05-04-datacenter-towers-in-tokyo-car-parks"]},
        {"id": "2026-05-08-eighty-x-against-a-planned-ten",
         "title": "A lab grows eighty-fold annualized against a planned tenfold",
         "claim": "Dario Amodei revealed Anthropic grew eightyfold annualized in the first "
                  "quarter against a planned tenfold, with compute unable to catch up, while "
                  "its pre-listing valuation reached a record $1.2 trillion in onchain trading, "
                  "up 900% since October.",
         "domain": "economics", "actor": ["anthropic"], "score": "80x vs 10x planned / $1.2T",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-06-samsung-crosses-a-trillion"]},
        {"id": "2026-05-08-model-spec-midtraining",
         "title": "Models study their own values before alignment fine-tuning",
         "claim": "Anthropic unveiled model spec midtraining, letting models study their own "
                  "values before alignment fine-tuning, while Opus 4.7 took the top spot on a "
                  "new refactoring leaderboard for production-scale repositories.",
         "domain": "models", "actor": ["anthropic"], "score": "48.57",
         "evidences": ["values-negotiated-with-the-model", "machine-introspection"],
         "supersedes": [B + "developments/2026-04-16-weak-to-strong-supervision"],
         "body": "Reading the syllabus before the exam."},
        {"id": "2026-05-08-rebuilding-a-codebase-from-a-binary",
         "title": "A benchmark asks agents to rebuild whole codebases from a binary",
         "claim": "The ProgramBench benchmark asks agents to rebuild full codebases from a "
                  "binary alone, where Opus 4.7 leads at 3% almost resolved and zero percent "
                  "fully solved.",
         "domain": "benchmarks", "actor": ["anthropic"], "score": "3% / 0%",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-05-03-arc-agi-3-starts-to-move"],
         "body": "A humbling reminder that the ladder still has rungs above."},
        {"id": "2026-05-08-agents-dream-overnight",
         "title": "Agents review their own session histories overnight",
         "claim": "Anthropic launched dreaming in its managed agents, a scheduled process that "
                  "reviews session histories and curates shared memories across teams, while "
                  "Chrome began quietly installing four gigabytes of a local model on every "
                  "desktop with available storage.",
         "description": "The newsletter files a memory-curation job under agents training themselves "
                        "overnight: offline consolidation, until now a research result about agents "
                        "designing their own memory, ships as a product feature the agents run on "
                        "themselves.",
         "domain": "agents", "actor": ["anthropic", "google"], "score": "4 GB",
         "about": [B + "systems/claude-managed-agents", B + "systems/gemini-nano"],
         "evidences": ["recursive-self-improvement", "agent-society", "models-sleep"],
         "supersedes": [B + "developments/2026-04-29-every-ticket-gets-its-own-agent"],
         "relatedTo": [B + "developments/2026-02-12-alma-agents-design-their-own-memory",
                       B + "developments/2026-04-07-seventy-two-hours-fifty-experiments",
                       B + "developments/2026-04-23-agents-build-memories-from-screen-captures"],
         "tags": ["rsi", "continual-learning", "agent-harness"],
         "supporting_text": "a scheduled process that reviews session histories and curates shared memories across teams",
         "sources": [{"id": "anthropic-managed-agents-dreaming-blog",
                      "resource": "https://claude.com/blog/new-in-claude-managed-agents",
                      "title": "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration",
                      "author": "org:anthropic"},
                     {"id": "9to5google-chrome-gemini-nano-4gb",
                      "resource": "https://9to5google.com/2026/05/06/google-chrome-4gb-storage-ai-details/",
                      "title": "Google Chrome takes up 4GB for AI, but only if you have room",
                      "author": "org:9to5google", "last_modified": "2026-05-06"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Anthropic's \u201cdreaming\u201d is a scheduled job inside "
                 "[Claude Managed Agents](/systems/claude-managed-agents.md) that reads back an agent's "
                 "session histories and curates the memories worth keeping, shared across a team's "
                 "agents ([Anthropic blog](https://claude.com/blog/new-in-claude-managed-agents)); the "
                 "newsletter files it under agents training themselves overnight. It brings offline "
                 "consolidation into a shipped product, after researchers had agents "
                 "[meta-learn their own memory designs](/developments/2026-02-12-alma-agents-design-their-own-memory.md) "
                 "and a 72-hour unsupervised run "
                 "[invented a memory system](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md), "
                 "and it anticipates the [models-sleep](/themes/models-sleep.md) theme the newsletter "
                 "names later in May. The same issue notes Chrome quietly installing 4 GB of "
                 "[Gemini Nano](/systems/gemini-nano.md) on every desktop with room for it "
                 "([9to5Google](https://9to5google.com/2026/05/06/google-chrome-4gb-storage-ai-details/)), "
                 "the local-model half of the claim. It follows the "
                 "[Symphony orchestrator](/developments/2026-04-29-every-ticket-gets-its-own-agent.md) "
                 "giving every ticket its own agent, and precedes the "
                 "[self-rewriting harness](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) of June."},
        {"id": "2026-05-08-motherboard-sales-collapse",
         "title": "Enthusiast motherboard sales collapse as wafers redirect",
         "claim": "Motherboard sales collapsed over 25% as wafers were redirected to AI "
                  "accelerators, while Terafab is projected to cost $55 to $119 billion across "
                  "phases and Arm doubled its AI-chip guidance one month after launch.",
         "domain": "economics", "actor": ["tesla", "arm-holdings"], "score": "-25% / $55-119B",
         "evidences": ["consumer-deprioritized", "silicon-designs-itself"],
         "supersedes": [B + "developments/2026-05-06-apple-explores-intel-and-samsung-as-fabs"]},
        {"id": "2026-05-08-copper-runs-out-of-bandwidth",
         "title": "Nvidia puts $3.2B into optical fiber as copper runs out of bandwidth",
         "claim": "Nvidia is investing $3.2 billion in Corning for three new US optical fiber "
                  "plants because copper has run out of bandwidth, while OpenAI, AMD, Broadcom, "
                  "Intel, Microsoft and Nvidia jointly open-sourced a multipath protocol keeping "
                  "GPUs synchronized across cluster failures.",
         "domain": "compute", "actor": ["nvidia", "corning", "amd", "broadcom"], "score": "$3.2B",
         "evidences": ["vertical-silicon", "network-over-node"],
         "supersedes": [B + "developments/2026-05-06-datacenters-in-the-cul-de-sac"]},
        {"id": "2026-05-08-europe-weighs-cloud-sovereignty-rules",
         "title": "Europe weighs restricting US clouds from sensitive government data",
         "claim": "The European Commission is weighing rules restricting US cloud platforms from "
                  "processing sensitive government data, naming sovereignty as the next "
                  "constraint after compute, while Texas passed California in utility-scale "
                  "solar capacity.",
         "domain": "policy", "actor": ["european-union"],
         "evidences": ["silicon-curtain", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-05-an-executive-order-for-model-review"]},
        {"id": "2026-05-08-a-generalized-neural-interface",
         "title": "A surgical robot is rebuilt to reach any region of the brain",
         "claim": "Neuralink's surgical robot is being rebuilt to reach any brain region, aiming "
                  "at a generalized neural interface for every condition originating there, "
                  "while Amazon pharmacy kiosks will begin dispensing an oral GLP-1.",
         "domain": "biotech", "actor": ["neuralink", "amazon", "novo-nordisk"],
         "evidences": ["hardware-grade-biology", "intimate-interface"],
         "supersedes": [B + "developments/2026-05-06-radiology-without-the-radiation"]},
        {"id": "2026-05-08-pursue-launches",
         "title": "A records system launches to release tens of millions of UAP documents",
         "claim": "The Department of War launched PURSUE, a coordinated records release covering "
                  "tens of millions of documents across decades and dozens of agencies, with new "
                  "declassified tranches planned every few weeks.",
         "domain": "policy", "actor": ["war-department"],
         "evidences": ["politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-04-20-the-banned-model-is-run-by-the-agencies"]},
        {"id": "2026-05-08-korea-overtakes-canada-on-silicon-demand",
         "title": "South Korea's market overtakes Canada's on silicon demand",
         "claim": "South Korea's stock market overtook Canada's as the world's seventh largest "
                  "propelled by AI silicon demand, while Washington and Beijing weighed official "
                  "AI talks at an upcoming summit and a brokerage launched crypto trading at "
                  "fifty basis points.",
         "domain": "economics", "actor": ["morgan-stanley", "etrade"],
         "evidences": ["ai-as-the-economy", "silicon-curtain"]},
    ],
}
