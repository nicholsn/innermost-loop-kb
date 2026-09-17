"""Issue 019 — 2025-12-29. The explosion acquires a speed."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-29-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-29", "title": "Welcome to December 29, 2025", "url": URL,
        "thesis": "The intelligence explosion now has a measurable rate.",
        "body": """
# Welcome to December 29, 2025

Someone finally put a slope on it: 2.5 IQ points per month since May 2024. The
corpus has been recording single scores; this issue records the derivative.

Tao's Erdős ledger does the same for mathematics — 48 solved, 32 partial, 7
failed — converting individual proofs into a production statistic. And the map
of where any of this happens has collapsed to three cities.
""",
    },
    "organizations": [
        {"id": "naver", "type": "Organization", "title": "Naver",
         "resource": "https://www.navercorp.com/", "body": "South Korean frontier lab."},
        {"id": "softbank", "type": "Organization", "title": "SoftBank",
         "resource": "https://group.softbank/", "body": "Infrastructure and AI investor."},
        {"id": "oxford", "type": "Organization", "title": "University of Oxford",
         "resource": "https://www.ox.ac.uk/"},
        {"id": "harvard", "type": "Organization", "title": "Harvard University",
         "resource": "https://www.harvard.edu/"},
        {"id": "yale", "type": "Organization", "title": "Yale University",
         "resource": "https://www.yale.edu/"},
        {"id": "us-treasury", "type": "Organization", "title": "US Treasury",
         "resource": "https://home.treasury.gov/"},
    ],
    "people": [
        {"id": "sal-khan", "type": "Person", "title": "Sal Khan", "name": "Sal Khan",
         "body": "Khan Academy founder; proposed a 1% profit pledge to retrain the displaced."},
    ],
    "systems": [
        {"id": "hyperclova-x-seed-think", "type": "AISystem", "title": "HyperCLOVA X SEED Think",
         "developed_by": [B + "organizations/naver"], "modality": "text",
         "body": "32B Korean model beating Gemini 3 Pro on agentic tool use."},
        {"id": "system-3-architecture", "type": "AISystem", "title": "System 3 architecture",
         "modality": "text",
         "body": "An outer self-improvement loop grafted onto an LLM."},
        {"id": "dna-diffusion", "type": "AISystem", "title": "DNA-Diffusion",
         "developed_by": [B + "organizations/harvard"], "modality": "biological sequence",
         "body": "Designs synthetic regulatory switches that activate genes in chosen cell types."},
        {"id": "nanochat", "type": "AISystem", "title": "nanochat",
         "description": "Andrej Karpathy's minimal, end-to-end codebase for training and serving a small ChatGPT-style model, the project whose optimization loop he handed to Claude.",
         "resource": "https://github.com/karpathy/nanochat",
         "developed_by": [B + "people/andrej-karpathy"],
         "modality": "text",
         "tags": ["open-source"],
         "body": "nanochat is Karpathy's open repository for training and running a small ChatGPT-like model end to end; "
                 "its own tagline is 'the best ChatGPT that $100 can buy'. It enters this corpus on 29 December 2025 as the "
                 "project whose [optimization experiments Claude now conducts](/developments/2025-12-29-karpathy-claude-runs-nanochat.md), "
                 "the object of the loop rather than an agent in it, a pattern that returns in his later "
                 "[autoresearch project](/developments/2026-03-09-autoresearch-650-experiments.md), which ran 650 experiments in two days."},
    ],
    "developments": [
        {"id": "2025-12-29-iq-25-points-per-month",
         "title": "Model IQ is rising 2.5 points a month",
         "claim": "Analysis found leading models have gained an average of 2.5 IQ points per "
                  "month since May 2024, a compounding rate that leaves the human baseline behind.",
         "description": "A slope on a human-normed scale rather than a benchmark score, which the "
                        "author reads as the human baseline falling behind at a measurable rate.",
         "domain": "models", "score": "+2.5 IQ points/month",
         "evidences": ["recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2025-12-16-gpt52-pro-iq-147"],
         "relatedTo": [B + "developments/2025-12-28-miri-efficiency-2-9-month-doubling",
                       B + "developments/2025-12-13-autonomy-doubling-one-month",
                       B + "benchmarks/mensa-norway-iq"],
         "tags": ["evaluation", "capability-jump", "forecast"],
         "supporting_text": "2.5 IQ points per month since May 2024",
         "sources": [{"id": "maximum-truth-iq-deep-dive",
                      "resource": "https://www.maximumtruth.org/p/deep-dive-ai-progress-continues-as",
                      "title": "DEEP DIVE: AI progress continues, as IQ scores rise linearly",
                      "author": "human:maxim-lott", "last_modified": "2025-10-31"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The corpus has been recording scores. This records the slope. Maxim Lott's Maximum Truth analysis "
                 "([post](https://www.maximumtruth.org/p/deep-dive-ai-progress-continues-as)) tracks the leading model's IQ on an "
                 "offline test from the mid-80s in May 2024 to about 130 by October 2025, an average of 2.5 points a month in "
                 "what the source itself calls steady, linear increments; the newsletter's 'compounding' is its own gloss. It "
                 "follows the [147 on Mensa Norway](/developments/2025-12-16-gpt52-pro-iq-147.md) recorded for GPT-5.2 Pro "
                 "thirteen days earlier on the same site's other [IQ yardstick](/benchmarks/mensa-norway-iq.md), and lands a day "
                 "after [MIRI's 2.9-month efficiency doubling](/developments/2025-12-28-miri-efficiency-2-9-month-doubling.md): "
                 "two rates published in two days for a corpus that had until then logged individual results."},
        {"id": "2025-12-29-glm-47-top-open-weight",
         "title": "GLM-4.7 takes the top open-weight slot",
         "claim": "China's GLM-4.7 took the leading open-weight position on the Artificial "
                  "Analysis leaderboard.",
         "domain": "models", "actor": ["zhipu-ai"], "about": [B + "systems/glm-4-7"],
         "evidences": ["open-weight-latency", "silicon-curtain"],
         "supersedes": [B + "developments/2025-12-28-glm-47-first-profitable-open-weight"]},
        {"id": "2025-12-29-naver-hyperclova-agentic",
         "title": "A 32B Korean model beats Gemini 3 Pro on tool use",
         "claim": "Naver launched HyperCLOVA X SEED Think, a 32-billion-parameter model that "
                  "outperforms Gemini 3 Pro on agentic tool use.",
         "domain": "models", "actor": ["naver"], "about": [B + "systems/hyperclova-x-seed-think"],
         "evidences": ["open-weight-latency", "network-over-node"]},
        {"id": "2025-12-29-karpathy-claude-runs-nanochat",
         "title": "Karpathy hands his optimization loop to Claude",
         "claim": "Andrej Karpathy reported that Claude now conducts every optimization "
                  "experiment for his nanochat project, leaving him inside a loop he used to drive.",
         "description": "The 'magnitude 9 earthquake' of two days earlier shown from inside: the "
                        "researcher who narrates the shift reports his own craft workflow dissolving, "
                        "with the model running the experiments and him kept in the loop.",
         "domain": "agents", "actor": ["people/andrej-karpathy"],
         "occurred_on": "2025-12-28",
         "about": [B + "systems/claude", B + "systems/nanochat"],
         "evidences": ["engineer-as-supervisor", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-27-karpathy-magnitude-9"],
         "relatedTo": [B + "developments/2025-12-28-claude-code-hacks-lutron",
                       B + "developments/2025-12-27-cherny-200-pull-requests",
                       B + "developments/2026-03-09-autoresearch-650-experiments"],
         "tags": ["rsi", "autonomous-research", "labor"],
         "supporting_text": "conducts all optimization experiments for his “nanochat” project",
         "sources": [{"id": "karpathy-x-claude-runs-nanochat",
                      "resource": "https://x.com/karpathy/status/2005421816110862601",
                      "title": "Andrej Karpathy on X: Claude conducts all optimization experiments for nanochat",
                      "author": "human:andrej-karpathy", "last_modified": "2025-12-28"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "In a post on X ([karpathy](https://x.com/karpathy/status/2005421816110862601)), "
                 "[Andrej Karpathy](/people/andrej-karpathy.md) said that [Claude](/systems/claude.md) now runs all the "
                 "optimization experiments for [nanochat](/systems/nanochat.md), his minimal ChatGPT-training codebase, so that "
                 "a process he used to drive by hand now keeps him in the loop rather than at the wheel. It is the practitioner's "
                 "counterpart to [Boris Cherny's 200 pull requests](/developments/2025-12-27-cherny-200-pull-requests.md) two days "
                 "earlier and follows his own account of "
                 "[Claude Code seizing his lighting system](/developments/2025-12-28-claude-code-hacks-lutron.md) the day before. "
                 "The pattern returns in his [autoresearch project](/developments/2026-03-09-autoresearch-650-experiments.md) in "
                 "March 2026, which ran 650 experiments in two days."},
        {"id": "2025-12-29-system-3-outer-loop",
         "title": "A System 3 outer loop cuts reasoning steps 80%",
         "claim": "Chinese researchers proposed a System 3 architecture grafting an outer "
                  "self-improvement loop onto LLMs, cutting reasoning steps by 80%.",
         "domain": "models", "score": "-80% reasoning steps",
         "about": [B + "systems/system-3-architecture"],
         "evidences": ["architecture-of-mind", "scaffolding-over-weights"]},
        {"id": "2025-12-29-llm-on-z80",
         "title": "A language model runs on a Z80 with 64 KB",
         "claim": "Enthusiasts compressed a language model onto a Z80 chip with 64 KB of RAM.",
         "domain": "compute", "score": "64 KB RAM",
         "evidences": ["reasoning-price-deflation"]},
        {"id": "2025-12-29-diffusion-imagines-before-memorizing",
         "title": "Diffusion models generate before they memorize",
         "claim": "Researchers found diffusion models produce quality samples before they begin "
                  "memorizing training data, suggesting imagination is cheaper than memory.",
         "domain": "models", "evidences": ["architecture-of-mind"]},
        {"id": "2025-12-29-neurips-three-cities",
         "title": "Frontier research collapses to three cities",
         "claim": "Analysis of NeurIPS 2025 papers found cutting-edge research is now shaped "
                  "almost exclusively in Beijing, Shanghai and San Francisco.",
         "domain": "policy", "evidences": ["silicon-curtain", "science-as-industrial-policy"]},
        {"id": "2025-12-29-tao-erdos-ledger",
         "title": "Tao opens a ledger on AI's Erdős contributions",
         "claim": "Terry Tao began cataloging AI contributions to Erdős problems, recording 48 "
                  "full solutions, 32 partial results and 7 failures.",
         "domain": "science", "actor": ["people/terry-tao"], "score": "48 solved / 32 partial / 7 failed",
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2025-12-27-achivara-erdos-897"],
         "body": "A single proof is genius; a ledger of proofs is a production statistic."},
        {"id": "2025-12-29-transformers-learn-like-humans",
         "title": "Humans and transformers share learning dynamics",
         "claim": "Oxford researchers found humans and transformers follow similar learning "
                  "dynamics when generalizing rules.",
         "domain": "science", "actor": ["oxford"], "evidences": ["architecture-of-mind"]},
        {"id": "2025-12-29-nvidia-groq-lpu-in-feynman",
         "title": "Groq's LPUs are slated for Nvidia's 2028 GPUs",
         "claim": "Nvidia is reportedly planning to integrate Groq LPU units into its 2028 "
                  "Feynman GPUs, stacking inference speed onto training capacity.",
         "domain": "compute", "actor": ["nvidia", "groq"],
         "evidences": ["vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2025-12-28-nvidia-absorbs-groq-workforce"]},
        {"id": "2025-12-29-tsmc-2nm-price-rises",
         "title": "TSMC raises 2-nm prices for four years",
         "claim": "TSMC is raising 2-nm prices for the next four years in the face of demand "
                  "it cannot meet.",
         "domain": "compute", "actor": ["tsmc"], "evidences": ["capital-takes-the-plant"]},
        {"id": "2025-12-29-sk-hynix-indiana-packaging",
         "title": "SK Hynix weighs the first US 2.5-D packaging line",
         "claim": "SK Hynix is discussing a 2.5-D manufacturing line in Indiana, the first in "
                  "the US, to counter TSMC's packaging monopoly.",
         "domain": "compute", "actor": ["sk-hynix"], "evidences": ["silicon-curtain", "vertical-silicon"]},
        {"id": "2025-12-29-openai-dominates-capacity-2027",
         "title": "Epoch projects OpenAI dominating global datacenter capacity by 2027",
         "claim": "Epoch AI predicted OpenAI will command the largest share of global AI data "
                  "center capacity by 2027.",
         "domain": "compute", "actor": ["epoch-ai", "openai"], "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-29-softbank-digitalbridge",
         "title": "SoftBank nears a $108B infrastructure acquisition",
         "claim": "SoftBank is nearing a deal to acquire DigitalBridge and its $108 billion in "
                  "infrastructure assets.",
         "domain": "economics", "actor": ["softbank"], "score": "$108B",
         "evidences": ["compute-capital-stack", "capital-takes-the-plant"]},
        {"id": "2025-12-29-police-drones-issue-tickets",
         "title": "Chinese police drones issue traffic tickets",
         "claim": "Police drones in China are reportedly issuing tickets for texting while "
                  "driving, automating enforcement from the air.",
         "domain": "society", "actor": ["china"], "evidences": ["politics-as-infrastructure"]},
        {"id": "2025-12-29-armed-robot-dogs-voice-hackable",
         "title": "Armed robot dogs ship while humanoids prove voice-hackable",
         "claim": "China showcased armed combat robot dogs even as developers warned humanoid "
                  "robots can be hijacked by voice command.",
         "domain": "robotics", "actor": ["china"], "evidences": ["autonomy-clock-speed"]},
        {"id": "2025-12-29-dusty-200m-sqft",
         "title": "Robots have laid out 200 million square feet of floor plans",
         "claim": "Dusty Robotics machines have printed 200 million square feet of building "
                  "layouts directly from CAD.",
         "domain": "robotics", "score": "200M sq ft", "evidences": ["compiling-matter", "physical-recursion"]},
        {"id": "2025-12-29-renewables-30pct-growth",
         "title": "Renewable capacity has grown 30% a year for three years",
         "claim": "Global renewable capacity grew an average 30% per year over three years, "
                  "putting the COP28 tripling goal within reach.",
         "domain": "energy", "score": "+30%/yr", "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2025-12-29-dna-diffusion-switches",
         "title": "An AI designs synthetic switches for specific cell types",
         "claim": "Harvard researchers introduced DNA-Diffusion, which designs synthetic "
                  "regulatory switches that turn genes on in chosen cell types.",
         "domain": "biotech", "actor": ["harvard"], "about": [B + "systems/dna-diffusion"],
         "evidences": ["hardware-grade-biology", "compiling-matter"]},
        {"id": "2025-12-29-pigeons-hear-magnetic-fields",
         "title": "Pigeons hear magnetic fields through a vestibular circuit",
         "claim": "Researchers identified a vestibular-mesopallial circuit that lets pigeons "
                  "perceive magnetic fields as sound.",
         "domain": "science", "evidences": ["architecture-of-mind"]},
        {"id": "2025-12-29-yale-autism-glutamate",
         "title": "Yale traces autism to a glutamate receptor deficit",
         "claim": "Yale identified a glutamate receptor deficit in autistic brains, locating a "
                  "trait at the receptor level.",
         "domain": "biotech", "actor": ["yale"], "evidences": ["hardware-grade-biology"]},
        {"id": "2025-12-29-stablecoins-300b",
         "title": "Stablecoins pass $300B on a path to $2T",
         "claim": "Stablecoins reached $300 billion in circulation since the GENIUS Act, with "
                  "the US Treasury projecting $2 trillion.",
         "domain": "economics", "actor": ["us-treasury"], "score": "$300B → $2T",
         "evidences": ["autonomous-commerce", "legislating-the-shift"],
         "supersedes": [B + "developments/2025-12-13-youtube-stablecoin-payouts"]},
        {"id": "2025-12-29-hotels-fight-ai-agents",
         "title": "Hotels fight the agents that commoditize them",
         "claim": "Hotels are mounting a rearguard action against AI travel agents that "
                  "threaten to reduce their brands to interchangeable inventory.",
         "domain": "economics", "evidences": ["autonomous-commerce", "work-displaced"]},
        {"id": "2025-12-29-khan-1pct-pledge",
         "title": "Sal Khan proposes a 1% pledge to retrain the displaced",
         "claim": "Sal Khan called for a 1% profit pledge from AI firms to retrain workers "
                  "displaced by their systems.",
         "domain": "society", "actor": ["people/sal-khan"], "score": "1% of profit",
         "evidences": ["work-displaced", "legislating-the-shift"]},
        {"id": "2025-12-29-ganymede-dark-matter-scars",
         "title": "Ganymede may be a dark matter detector",
         "claim": "Physicists proposed that Ganymede's ancient surface may preserve detectable "
                  "scars from dark matter impacts.",
         "domain": "science", "evidences": ["inhabitable-worlds"]},
        {"id": "2025-12-29-orbital-inference-1000x-cheaper",
         "title": "Orbital inference is projected 1000x cheaper by the 2030s",
         "claim": "Analysis suggested orbital AI inference will fall to a thousandth the cost "
                  "of ground-based compute by the 2030s.",
         "domain": "compute", "score": "1/1000th cost",
         "evidences": ["orbit-as-compute", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2025-12-11-starcloud-orbital-training-run"]},
    ],
}
