"""Issue 023 — 2026-01-04. Stack Overflow goes quiet."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-4-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-04", "title": "Welcome to January 4, 2026", "url": URL,
        "thesis": "The human developer era ends quietly, in a traffic chart.",
        "body": """
# Welcome to January 4, 2026

New questions on Stack Overflow have decayed to pre-launch levels. Nobody
announced the end of programmers asking programmers for help; the graph just
went flat. Musk says we are in the Singularity, which the corpus has now heard
from Roon, Eric Raymond, Yudkowsky and Altman inside three weeks.

The strangest item is the fog of war clearing through arbitrage: someone
vibe-coded a Pentagon pizza-order tracker, predicted a strike on Venezuela, and
made $80,000.
""",
    },
    "organizations": [
        {"id": "stackoverflow", "type": "Organization", "title": "Stack Overflow",
         "resource": "https://stackoverflow.com/", "body": "Programmer Q&A site; question volume "
                 "has decayed to pre-public levels."},
        {"id": "magicpath", "type": "Organization", "title": "MagicPath",
         "body": "Design tool startup; CEO scanned his DNA with Claude Code."},
        {"id": "cia", "type": "Organization", "title": "CIA",
         "resource": "https://www.cia.gov/"},
        {"id": "aerojet", "type": "Organization", "title": "Aerojet Rocketdyne",
         "body": "Proposing nuclear-electric propulsion for deep-space logistics."},
        {"id": "hyundai", "type": "Organization", "title": "Hyundai",
         "resource": "https://www.hyundai.com/", "body": "Owner of Boston Dynamics; deploying Atlas in Georgia."},
        {"id": "isa", "type": "Organization", "title": "International Seabed Authority",
         "resource": "https://www.isa.org.jm/", "body": "UN body finalizing deep-sea mining rules."},
    ],
    "people": [
        {"id": "danielle-fong", "type": "Person", "title": "Danielle Fong", "name": "Danielle Fong",
         "body": "Demonstrated an image model used as persistent visual memory."},
    ],
    "systems": [
        {"id": "seedfold", "type": "AISystem", "title": "SeedFold",
         "developed_by": [B + "organizations/bytedance"], "modality": "protein structure",
         "body": "Protein folding models leading FoldBench."},
    ],
    "benchmarks": [
        {"id": "foldbench", "type": "Benchmark", "title": "FoldBench",
         "measures_capability": "protein structure prediction accuracy"},
    ],
    "developments": [
        {"id": "2026-01-04-musk-enters-the-singularity",
         "title": "Musk says we have entered the Singularity",
         "claim": "Elon Musk stated that we have entered the Singularity.",
         "description": "The declarations stop coming only from researchers and reach the figure behind "
                        "xAI, SpaceX and Tesla, and the newsletter files it under a recursive "
                        "self-improvement phase it says has officially begun, with a flat Stack Overflow "
                        "traffic chart as the evidence behind the sentiment.",
         "domain": "society", "actor": ["people/elon-musk"],
         "evidences": ["takeoff-declared", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-28-esr-singularity-upon-us"],
         "relatedTo": [B + "developments/2026-01-04-stackoverflow-decays-to-prelaunch",
                       B + "developments/2025-12-27-roon-solidly-in-takeoff",
                       B + "developments/2025-12-28-yudkowsky-concludes-agi"],
         "tags": ["rsi"],
         "supporting_text": "we have entered the Singularity",
         "sources": [{"id": "musk-x-entered-the-singularity",
                      "resource": "https://x.com/elonmusk/status/2007738847397036143",
                      "title": "We have entered the Singularity", "author": "human:elonmusk",
                      "last_modified": "2026-01-04"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The fifth declaration in three weeks, after Roon, Raymond, Yudkowsky and Altman. Musk's "
                 "post is five words, 'We have entered the Singularity', in reply to @DavidSHolz on the "
                 "morning of 4 January 2026 ([X](https://x.com/elonmusk/status/2007738847397036143)); the "
                 "framing that this is the recursive self-improvement phase is the newsletter's own opening "
                 "line, which it backs with "
                 "[Stack Overflow question volume decaying to pre-launch levels](/developments/2026-01-04-stackoverflow-decays-to-prelaunch.md). "
                 "It overtakes [Eric Raymond's declaration](/developments/2025-12-28-esr-singularity-upon-us.md) "
                 "of a week earlier and sits beside [Roon's takeoff call](/developments/2025-12-27-roon-solidly-in-takeoff.md), "
                 "[Yudkowsky's AGI conclusion](/developments/2025-12-28-yudkowsky-concludes-agi.md) and "
                 "[Altman's confirmation of self-improving systems in production](/developments/2025-12-28-altman-self-improving-in-production.md); "
                 "a day later Musk [names 2026 the year of the Singularity](/developments/2026-01-05-musk-year-of-the-singularity.md)."},
        {"id": "2026-01-04-stackoverflow-decays-to-prelaunch",
         "title": "Stack Overflow question volume falls to pre-launch levels",
         "claim": "New questions on Stack Overflow decayed to volumes last seen before the site "
                  "went public, marking the end of programmers routinely asking other "
                  "programmers for help.",
         "domain": "economics", "actor": ["stackoverflow"],
         "evidences": ["work-displaced", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2025-12-30-resume-success-rate-04pct"],
         "body": "No announcement, just a flat graph."},
        {"id": "2026-01-04-rlm-two-orders-of-context",
         "title": "Recursive models handle contexts 100x their window",
         "claim": "Recursive Language Models are decomposing problems and calling themselves to "
                  "handle contexts two orders of magnitude larger than their context windows.",
         "description": "Long context stops being a property of the weights: a scaffold that lets the model "
                        "program over its own prompt beats both larger windows and existing agent "
                        "harnesses, which the newsletter reads as what replaces programmers asking "
                        "programmers for help.",
         "domain": "agents", "score": "two orders of magnitude",
         "about": [B + "systems/recursive-language-model"],
         "evidences": ["recursive-self-improvement", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-01-02-prime-intellect-rlm"],
         "relatedTo": [B + "developments/2025-12-30-stanford-test-time-training",
                       B + "developments/2026-03-16-million-token-windows-ship",
                       B + "developments/2026-02-12-alma-agents-design-their-own-memory"],
         "tags": ["agent-harness", "capability-jump"],
         "supporting_text": "to handle contexts two orders of magnitude larger than their windows",
         "sources": [{"id": "rlm-arxiv-paper",
                      "resource": "https://arxiv.org/abs/2512.24601v1",
                      "title": "Recursive Language Models", "author": "org:mit",
                      "last_modified": "2025-12-31"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The paper, by Alex L. Zhang, Tim Kraska and Omar Khattab of MIT CSAIL (arXiv 2512.24601, "
                 "31 December 2025), treats a long prompt as an external environment: the model examines it "
                 "from a Python REPL, decomposes it, and recursively calls itself over snippets. RLMs "
                 "process inputs up to two orders of magnitude beyond the context window, working at the "
                 "10M-plus-token scale, and across four long-context tasks improve GPT-5 by a median of 26% "
                 "over compaction, 130% over CodeAct with sub-calls and 13% over Claude Code at comparable "
                 "cost, while a post-trained RLM-Qwen3-8B beats its base model by 28.3% "
                 "([arXiv](https://arxiv.org/abs/2512.24601)). It supplies the measured result behind "
                 "[Prime Intellect's adoption of the RLM as the paradigm of 2026](/developments/2026-01-02-prime-intellect-rlm.md) "
                 "two days earlier, and stands as the scaffold-side answer to long context beside "
                 "Stanford's weight-side [end-to-end test-time training](/developments/2025-12-30-stanford-test-time-training.md), "
                 "months before [million-token windows ship](/developments/2026-03-16-million-token-windows-ship.md) "
                 "as a property of the model itself."},
        {"id": "2026-01-04-grok-business-tiers",
         "title": "xAI puts the Singularity on a seat licence",
         "claim": "xAI launched Grok Business and Enterprise tiers at $30 a seat.",
         "domain": "economics", "actor": ["xai"], "score": "$30/seat",
         "evidences": ["reasoning-price-deflation", "autonomous-commerce"]},
        {"id": "2026-01-04-claude-code-compresses-research",
         "title": "A three-month PhD project is replicated in twenty minutes",
         "claim": "Claude Code replicated a three-month PhD project in twenty minutes and "
                  "reproduced a year of Google's agent orchestrator work in an hour.",
         "domain": "agents", "actor": ["anthropic"], "about": [B + "systems/claude-code"],
         "score": "3 months → 20 minutes",
         "evidences": ["automated-science", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2025-12-27-cherny-200-pull-requests"]},
        {"id": "2026-01-04-dna-as-debugging",
         "title": "Genomics becomes a debugging task",
         "claim": "MagicPath's CEO used Claude Code to scan his raw DNA for health risks.",
         "domain": "biotech", "actor": ["magicpath"], "evidences": ["hardware-grade-biology"]},
        {"id": "2026-01-04-image-model-as-visual-memory",
         "title": "An image model is used as persistent visual memory",
         "claim": "Danielle Fong demonstrated Claude Code using Nano Banana as a persistent "
                  "visual memory store.",
         "domain": "agents", "actor": ["people/danielle-fong"],
         "evidences": ["scaffolding-over-weights", "data-beyond-text"]},
        {"id": "2026-01-04-gemini-2hop-latent-reasoning",
         "title": "Gemini 3 Pro reasons two hops without thinking out loud",
         "claim": "Gemini 3 Pro reached 60% accuracy on two-hop latent reasoning, chaining "
                  "inferences without chain-of-thought.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/gemini-3-pro"],
         "score": "60%", "evidences": ["machine-introspection", "architecture-of-mind"]},
        {"id": "2026-01-04-adversarial-poetry-jailbreak",
         "title": "Poetry is a universal jailbreak",
         "claim": "Italian researchers found that curated adversarial poetry bypasses safety "
                  "mechanisms across models, acting as a universal jailbreak.",
         "domain": "models", "evidences": ["machine-affect", "coordination-tax"],
         "body": "Too literary to censor."},
        {"id": "2026-01-04-training-clusters-visible-from-orbit",
         "title": "Training algorithms become visible from orbit",
         "claim": "Microsoft's new training clusters are distinguishable from space, with "
                  "different building architectures for GPU coherent training and CPU-based RL "
                  "environments.",
         "domain": "compute", "actor": ["microsoft"],
         "evidences": ["infrastructure-crowding-out", "physical-recursion"],
         "body": "The learning algorithm has a footprint."},
        {"id": "2026-01-04-meta-four-turbine-types",
         "title": "Meta powers a 200-MW cluster with four kinds of turbine",
         "claim": "Meta is running its 200-MW Ohio cluster on a bricolage of four different "
                  "turbine types.",
         "domain": "energy", "actor": ["meta"], "score": "200 MW",
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-01-04-stargate-uae-heat-derated",
         "title": "Desert heat derates Stargate UAE from 1.3 GW to 1 GW",
         "claim": "OpenAI's Stargate UAE was heat-derated from 1.3 GW to 1 GW because of desert "
                  "temperatures.",
         "domain": "compute", "actor": ["openai"], "score": "1.3 GW → 1 GW",
         "about": [B + "facilities/stargate-uae"],
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2025-12-27-stargate-uae-1gw-gas"],
         "body": "Thermodynamics as the binding constraint, not capital."},
        {"id": "2026-01-04-orbit-faster-than-ground",
         "title": "Orbital datacenters are argued to deploy faster than ground builds",
         "claim": "Former SpaceX engineers argued 1,000 Starship launches could place a "
                  "gigawatt of compute in orbit in about a month, against two years for "
                  "Stargate Abilene.",
         "domain": "space", "actor": ["spacex"], "score": "0.1 years vs 2 years",
         "evidences": ["orbit-as-compute", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2025-12-29-orbital-inference-1000x-cheaper"],
         "body": "The argument shifts from cost to schedule — the binding constraint on the "
                 "ground is now heat and time, not money."},
        {"id": "2026-01-04-aerojet-nuclear-electric",
         "title": "Aerojet proposes nuclear-electric deep-space logistics",
         "claim": "Aerojet Rocketdyne proposed nuclear-electric propulsion for deep-space "
                  "logistics.",
         "domain": "space", "actor": ["aerojet"], "evidences": ["inhabitable-worlds"]},
        {"id": "2026-01-04-maduro-capture-drone-cyber",
         "title": "A head of state is captured by drones and a blackout",
         "claim": "The capture of Venezuelan President Nicolás Maduro was orchestrated with CIA "
                  "stealth drones and cyberattacks that cut power to the capital.",
         "domain": "policy", "actor": ["cia"], "occurred_on": "2026-01-04",
         "evidences": ["autonomy-clock-speed", "politics-as-infrastructure"]},
        {"id": "2026-01-04-pentagon-pizza-arbitrage",
         "title": "A pizza-order bot predicts a military strike",
         "claim": "An anonymous coder claims to have built a bot tracking Pentagon pizza orders "
                  "that predicted the Venezuela strike and netted $80,000, while another trader "
                  "turned $30,000 into $436,000 on the news.",
         "domain": "economics", "score": "$30K → $436K",
         "evidences": ["autonomous-commerce", "coordination-tax"],
         "body": "The fog of war cleared by arbitrage."},
        {"id": "2026-01-04-grey-market-peptides",
         "title": "Silicon Valley runs on grey-market peptides",
         "claim": "Silicon Valley is increasingly using a grey market of Chinese peptides, "
                  "including oxytocin marketed as a treatment for autism.",
         "domain": "biotech", "evidences": ["hardware-grade-biology", "legislating-the-shift"]},
        {"id": "2026-01-04-alibaba-pancreatic-ct",
         "title": "Alibaba's AI finds pancreatic cancer in plain CTs",
         "claim": "Alibaba's model is detecting pancreatic cancer in non-contrast CT scans.",
         "domain": "biotech", "actor": ["alibaba"], "evidences": ["automated-science"]},
        {"id": "2026-01-04-seedfold-tops-foldbench",
         "title": "ByteDance takes the top spot on FoldBench",
         "claim": "ByteDance's SeedFold protein folding models took first place on FoldBench.",
         "domain": "benchmarks", "actor": ["bytedance"], "about": [B + "systems/seedfold"],
         "evidences": ["automated-science", "open-weight-latency"]},
        {"id": "2026-01-04-two-archetypes-of-persistence",
         "title": "Bacterial persistence splits into two archetypes",
         "claim": "Israeli researchers identified two distinct archetypes of bacterial "
                  "persistence, regulated and dysregulated.",
         "domain": "science", "evidences": ["discovery-as-process"]},
        {"id": "2026-01-04-atlas-enters-hyundai-plant",
         "title": "Atlas humanoids start work in a Hyundai plant",
         "claim": "Boston Dynamics' Atlas humanoids began working inside Hyundai's Georgia auto "
                  "plant.",
         "domain": "robotics", "actor": ["boston-dynamics", "hyundai"],
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2025-12-24-boston-dynamics-new-atlas"]},
        {"id": "2026-01-04-cybercabs-roam-austin",
         "title": "Cybercabs roam Austin as a solar supercharging oasis opens",
         "claim": "Tesla Cybercabs are operating in Austin while the world's largest "
                  "Supercharging site opened at Lost Hills with 164 stalls and a solar "
                  "microgrid.",
         "domain": "robotics", "actor": ["tesla"], "score": "164 stalls",
         "evidences": ["autonomous-commerce", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2025-12-15-unsupervised-robotaxis-austin"]},
        {"id": "2026-01-04-isa-deep-sea-mining-rules",
         "title": "The UN finalizes deep-sea mining rules across 31 contracts",
         "claim": "The International Seabed Authority is finalizing deep-sea mining rules, with "
                  "31 contracts issued for polymetallic nodules, cobalt crusts and sulfides.",
         "domain": "policy", "actor": ["isa"], "score": "31 contracts",
         "evidences": ["industrialized-nature", "legislating-the-shift"]},
        {"id": "2026-01-04-japan-quadruples-chip-budget",
         "title": "Japan quadruples its AI chip budget",
         "claim": "Japan is quadrupling its AI chip budget to ¥1.23 trillion.",
         "domain": "policy", "actor": ["japan-govt"], "score": "¥1.23T",
         "evidences": ["science-as-industrial-policy", "silicon-curtain"]},
        {"id": "2026-01-04-alaska-ai-judges",
         "title": "Alaska puts AI into probate court",
         "claim": "Alaska is deploying AI judges to help navigate probate court, while "
                  "California launched DROP to let citizens remove themselves from data brokers.",
         "domain": "policy", "evidences": ["politics-as-infrastructure", "legislating-the-shift"]},
    ],
}
