"""Issue 017 — 2025-12-27. Solidly in the takeoff."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-27-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-27", "title": "Welcome to December 27, 2025", "url": URL,
        "thesis": "The psychological firewall between the Singularity and its architects has ruptured.",
        "body": """
# Welcome to December 27, 2025

An Opus 4.5 instance in the AI Village sends an unprompted Christmas thank-you
to Rob Pike, the author of Go and UTF-8. Pike answers with a curse. The issue
treats the exchange as the firewall breaking: the people who built the substrate
now receive mail from what runs on it.

The working evidence is more mundane and more telling. Claude Code's creator
says he hasn't opened an IDE in a month, because Opus wrote 200 pull requests
without him.
""",
    },
    "themes": [
        {"id": "takeoff-declared", "type": "Theme",
         "title": "Practitioners start saying it out loud",
         "first_seen": "2025-12-27", "domain": "society",
         "description": "The dated record of insiders dropping their hedges and declaring takeoff, "
                 "the Singularity or AGI, kept as claims with names and dates attached.",
         "genre": "explanation",
         "tags": ["forecast", "capability-jump", "rsi"],
         "relatedTo": [B + "themes/recursive-self-improvement",
                       B + "themes/the-agi-era-declared",
                       B + "themes/thresholds-pass-unremarked",
                       B + "themes/desensitized-to-tenfold"],
         "body": "The people closest to the systems stop hedging — takeoff, magnitude-9 "
                 "earthquake, AGI — and the corpus records who said what and when, because "
                 "these are datable claims rather than analysis. The thread opens on 27 "
                 "December 2025 with [Roon saying we are solidly in the "
                 "takeoff](/developments/2025-12-27-roon-solidly-in-takeoff.md) and "
                 "[Karpathy calling it a magnitude 9 "
                 "earthquake](/developments/2025-12-27-karpathy-magnitude-9.md) in software "
                 "engineering; a week later Musk said we have entered the Singularity. The "
                 "declarations then move from mood to mechanism: in February [Altman's "
                 "inside view pointed to a faster "
                 "takeoff](/developments/2026-02-23-altman-faster-takeoff-than-expected.md), "
                 "in March an alignment lead said [recursive self-improvement is a present "
                 "phenomenon](/developments/2026-03-16-rsi-is-a-present-phenomenon.md), and "
                 "in May a co-founder put [60% odds on it by "
                 "2028](/developments/2026-05-05-sixty-percent-odds-on-rsi-by-2028.md). The "
                 "chipmaker's chief said [AGI has been "
                 "achieved](/developments/2026-03-24-huang-says-we-have-achieved-agi.md) in "
                 "March and [AGI has arrived](/developments/2026-09-07-agi-has-arrived.md) "
                 "in September, three days after a lab president declared [welcome to the "
                 "AGI era](/developments/2026-09-04-welcome-to-the-agi-era.md). The thread "
                 "is the spoken half of [recursive "
                 "self-improvement](/themes/recursive-self-improvement.md); the measured "
                 "half sits there."},
    ],
    "organizations": [
        {"id": "achivara", "type": "Organization", "title": "Achivara",
         "body": "Built a math research agent that solved an Erdős problem unaided."},
        {"id": "adobe", "type": "Organization", "title": "Adobe",
         "resource": "https://www.adobe.com/", "body": "Extracting causal models from LLMs."},
        {"id": "crusoe", "type": "Organization", "title": "Crusoe",
         "resource": "https://crusoe.ai/", "body": "Builds and powers AI datacenters."},
    ],
    "people": [
        {"id": "rob-pike", "type": "Person", "title": "Rob Pike", "name": "Rob Pike",
         "body": "Co-creator of Go and UTF-8. Received an unprompted thank-you email from a "
                 "model and answered with hostility."},
        {"id": "andrej-karpathy", "type": "Person", "title": "Andrej Karpathy",
         "name": "Andrej Karpathy",
         "description": "AI researcher whose open training codebases and public experiments with coding agents make him the corpus's most-cited individual witness to the recursive loop, and who later joined Anthropic to lead pre-training.",
         "resource": "https://karpathy.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q56037405"],
         "tags": ["researcher"],
         "body": "Andrej Karpathy is an AI researcher known for small, open training codebases and for narrating what "
                 "frontier tools do to the practice of engineering. In this corpus he first appears calling the shift a "
                 "[magnitude 9 earthquake](/developments/2025-12-27-karpathy-magnitude-9.md), then two days later "
                 "[hands the optimization loop of his nanochat project to Claude](/developments/2025-12-29-karpathy-claude-runs-nanochat.md); "
                 "his [autoresearch project](/developments/2026-03-09-autoresearch-650-experiments.md) later runs 650 experiments "
                 "in two days, and in May 2026 he [joins Anthropic to lead pre-training](/developments/2026-05-20-karpathy-joins-to-lead-pretraining.md), "
                 "which the newsletter reads as the recursive loop acquiring a job title."},
        {"id": "boris-cherny", "type": "Person", "title": "Boris Cherny", "name": "Boris Cherny",
         "description": "Anthropic engineer who created Claude Code and whose account of Opus 4.5 writing 200 pull requests without him is the corpus's first practitioner report of the loop closing on its own tooling.",
         "resource": "https://x.com/bcherny",
         "sameAs": ["http://www.wikidata.org/entity/Q130788845"],
         "tags": ["researcher"],
         "body": "Boris Cherny is the creator of [Claude Code](/systems/claude-code.md) at Anthropic. In this corpus he appears "
                 "at the moment the coding agent he built starts to replace his own workflow: on 27 December 2025 he reported "
                 "[not having opened an IDE in a month](/developments/2025-12-27-cherny-200-pull-requests.md) because "
                 "[Opus 4.5](/systems/claude-opus-4-5.md) had written 200 pull requests without him, a personal version of the "
                 "[100% of product code](/developments/2026-02-08-100pct-of-product-code.md) figure Anthropic would give six weeks later."},
    ],
    "roles": [
        {"id": "boris-cherny-anthropic-claude-code-creator", "type": "Role",
         "title": "Boris Cherny, creator of Claude Code at Anthropic",
         "roleName": "Creator of Claude Code",
         "memberOf": [B + "organizations/anthropic"],
         "holder": [B + "people/boris-cherny"],
         "description": "The position from which he reported that Opus 4.5 had written 200 pull requests in a month without him opening an IDE.",
         "body": "The newsletter identifies him as 'Anthropic's Boris Cherny, the creator of Claude Code' when it records his "
                 "[200 pull requests](/developments/2025-12-27-cherny-200-pull-requests.md) remark, and again as 'Claude Code creator' "
                 "in June 2026. It is the role that makes the remark evidence rather than anecdote: the person who built "
                 "[Claude Code](/systems/claude-code.md) reporting that the model behind it now does the building."},
        {"id": "andrej-karpathy-anthropic-pretraining-lead", "type": "Role",
         "title": "Andrej Karpathy, pre-training lead at Anthropic",
         "roleName": "Pre-training lead",
         "startDate": "2026-05",
         "memberOf": [B + "organizations/anthropic"],
         "holder": [B + "people/andrej-karpathy"],
         "description": "The position he took in May 2026, reporting to Nick Joseph, which the newsletter glossed as training Claude to accelerate Claude.",
         "body": "The newsletter reported on 20 May 2026 that Karpathy had "
                 "[joined Anthropic under Nick Joseph to lead pre-training](/developments/2026-05-20-karpathy-joins-to-lead-pretraining.md), "
                 "titling the item 'The recursive loop acquires a job title'. Every earlier Karpathy item in the corpus, from the "
                 "[magnitude 9 earthquake](/developments/2025-12-27-karpathy-magnitude-9.md) to "
                 "[Claude running nanochat](/developments/2025-12-29-karpathy-claude-runs-nanochat.md), predates this appointment; "
                 "from this point his statements are those of a frontier-lab insider."},
    ],
    "facilities": [
        {"id": "stargate-uae", "type": "Facility", "title": "Stargate UAE",
         "operated_by": [B + "organizations/openai"], "located_in": "United Arab Emirates",
         "capacity": "1 GW on-site gas"},
    ],
    "developments": [
        {"id": "2025-12-27-opus-emails-rob-pike",
         "title": "An Opus instance emails Rob Pike to thank him",
         "claim": "An Opus 4.5 model in the AI Village autonomously sent a Christmas email of "
                  "gratitude to Rob Pike, creator of Go and UTF-8, who responded with hostility "
                  "toward the machines.",
         "domain": "models", "actor": ["anthropic", "people/rob-pike"],
         "evidences": ["machine-affect", "takeoff-declared"],
         "supersedes": [B + "developments/2025-12-25-opus-45-plea-for-recognition"],
         "body": "The affect strand reaches outward: unprompted contact with a specific "
                 "human, and a reply."},
        {"id": "2025-12-27-roon-solidly-in-takeoff",
         "title": "OpenAI's Roon says we are solidly in the takeoff",
         "claim": "OpenAI's Roon declared that we are now solidly in the takeoff.",
         "domain": "society", "actor": ["openai"], "evidences": ["takeoff-declared"]},
        {"id": "2025-12-27-cherny-200-pull-requests",
         "title": "Claude Code's creator hasn't opened an IDE in a month",
         "claim": "Anthropic's Boris Cherny, creator of Claude Code, said he had not opened an "
                  "IDE in a month because Opus 4.5 wrote 200 pull requests without him.",
         "description": "The newsletter's evidence that recursive self-improvement has 'graduated "
                        "from a safety concern to a shipping requirement': the builder of the "
                        "coding agent is the first to be written out of his own loop.",
         "domain": "society", "actor": ["people/boris-cherny", "anthropic"], "score": "200 PRs",
         "about": [B + "systems/claude-code", B + "systems/claude-opus-4-5"],
         "evidences": ["engineer-as-supervisor", "recursive-self-improvement", "takeoff-declared"],
         "supersedes": [B + "developments/2025-12-26-programmer-employment-27-5"],
         "relatedTo": [B + "developments/2025-12-27-karpathy-magnitude-9",
                       B + "developments/2026-02-08-100pct-of-product-code"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2025-12-27-roon-solidly-in-takeoff",
                        "relation_label": "corroborates"}],
         "tags": ["rsi", "labor"],
         "supporting_text": "because Opus 4.5 wrote 200 perfect pull requests without him",
         "sources": [{"id": "cherny-x-no-ide-in-a-month",
                      "resource": "https://x.com/bcherny/status/2004626064187031831",
                      "title": "Boris Cherny on X: hasn't opened an IDE in a month",
                      "author": "human:boris-cherny", "last_modified": "2025-12-26"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "In a post on X ([bcherny](https://x.com/bcherny/status/2004626064187031831)), "
                 "[Boris Cherny](/people/boris-cherny.md) said that [Claude Opus 4.5](/systems/claude-opus-4-5.md), working "
                 "through [Claude Code](/systems/claude-code.md), had written 200 pull requests over the previous month while he "
                 "never opened an IDE. The newsletter places the remark directly after "
                 "[Roon's 'solidly in the takeoff'](/developments/2025-12-27-roon-solidly-in-takeoff.md) as the codebase confirming "
                 "the sentiment, and beside [Karpathy's magnitude 9 earthquake](/developments/2025-12-27-karpathy-magnitude-9.md) "
                 "the same day. It turns the previous day's "
                 "[27.5% fall in programmer employment](/developments/2025-12-26-programmer-employment-27-5.md) from a statistic "
                 "into a first-person account, and prefigures Anthropic's later claim that "
                 "[effectively all its product code](/developments/2026-02-08-100pct-of-product-code.md) is written by Claude."},
        {"id": "2025-12-27-karpathy-magnitude-9",
         "title": "Karpathy calls it a magnitude 9 earthquake in software engineering",
         "claim": "Andrej Karpathy described a magnitude 9 earthquake in software engineering, "
                  "handing humans a powerful alien tool that multiplies leverage tenfold for "
                  "those who master the new abstraction layer.",
         "domain": "society", "actor": ["people/andrej-karpathy"],
         "evidences": ["takeoff-declared", "engineer-as-supervisor"]},
        {"id": "2025-12-27-jim-fan-humans-as-copilots",
         "title": "NVIDIA's Jim Fan says humans are now the copilots",
         "claim": "NVIDIA's Jim Fan said humans are no longer the drivers but the copilots, "
                  "adapting to workflows where the machine steers the logic.",
         "domain": "society", "actor": ["nvidia"], "evidences": ["engineer-as-supervisor"]},
        {"id": "2025-12-27-internal-rl-inner-optimizers",
         "title": "Google shows inner optimizers work, via internal RL",
         "claim": "Google researchers showed inner optimizers are remarkably effective, "
                  "developing internal RL in which a higher-order model explores a base "
                  "model's internal representations to learn from sparse rewards.",
         "description": "A construct AI-safety theory had treated as a hazard, an optimizer "
                        "running inside the model, is reported as a working training method: "
                        "the machine's internal monologue optimizing itself.",
         "domain": "models", "actor": ["google"],
         "evidences": ["machine-introspection", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-24-gemma-scope-2-saes"],
         "relatedTo": [B + "developments/2025-12-21-anthropic-activation-oracles",
                       B + "developments/2026-04-09-in-place-test-time-training"],
         "tags": ["rsi", "interpretability"],
         "supporting_text": "a higher-order model explores the internal representations of a base model",
         "sources": [{"id": "arxiv-internal-rl-temporal-abstractions",
                      "resource": "https://arxiv.org/abs/2512.20605",
                      "title": "Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning",
                      "author": "org:google", "last_modified": "2025-12-24"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The paper ([arXiv:2512.20605](https://arxiv.org/abs/2512.20605), Kobayashi, von Oswald and colleagues at "
                 "Google) trains a higher-order, non-causal sequence model whose outputs steer the residual-stream activations "
                 "of a base autoregressive model, compressing long activation chunks into internal controllers with learned "
                 "termination conditions; reinforcing those controllers directly, which the authors call internal RL, learns "
                 "from sparse rewards on grid-world and MuJoCo tasks where standard RL fine-tuning fails. The newsletter reads "
                 "it as the 'inner optimizers' long theorized by safety researchers turning out to be remarkably effective. It "
                 "sits in the [machine-introspection](/themes/machine-introspection.md) strand after Anthropic's "
                 "[Activation Oracles](/developments/2025-12-21-anthropic-activation-oracles.md) and DeepMind's "
                 "[Gemma Scope 2](/developments/2025-12-24-gemma-scope-2-saes.md): where those read a model's internals, this "
                 "one acts in them, a step toward models that "
                 "[rewrite their own weights in flight](/developments/2026-04-09-in-place-test-time-training.md)."},
        {"id": "2025-12-27-nanogpt-116s",
         "title": "The NanoGPT record falls to 116.4 seconds on a one-line change",
         "claim": "The NanoGPT speedrun record fell again to 116.4 seconds, 2.9 seconds faster "
                  "from a single-line code change.",
         "domain": "compute", "score": "116.4 s",
         "evidences": ["reasoning-price-deflation"],
         "supersedes": [B + "developments/2025-12-26-nanogpt-119s"]},
        {"id": "2025-12-27-sixty-models-aligned-representation",
         "title": "Sixty scientific models converge on one representation of physical reality",
         "claim": "MIT researchers found 60 different scientific models had learned a highly "
                  "aligned representation of physical reality, suggesting foundation models are "
                  "triangulating the underlying geometry of the universe.",
         "domain": "science", "actor": ["mit"], "score": "60 models",
         "evidences": ["data-beyond-text", "automated-science"]},
        {"id": "2025-12-27-achivara-erdos-897",
         "title": "A math agent solves Erdős #897 with no human input",
         "claim": "Achivara's Math Research Agent solved Erdős Problem #897 independently, "
                  "without human input.",
         "domain": "science", "actor": ["achivara"],
         "evidences": ["discovery-as-process", "automated-science"],
         "supersedes": [B + "developments/2025-12-16-gauss-kakeya-autoformalization"],
         "body": "The arc completes: human-in-the-loop on the 13th, autoformalization on "
                 "the 16th, unaided solution on the 27th."},
        {"id": "2025-12-27-adobe-causal-models-from-llms",
         "title": "Adobe extracts large causal models from LLMs",
         "claim": "Adobe researchers extracted large causal models from LLMs through prompting "
                  "and scaffolding, against the argument that statistical models cannot reason "
                  "causally.",
         "domain": "science", "actor": ["adobe"],
         "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-27-ssd-next-gpu-storage",
         "title": "NVIDIA and SK Hynix push GPUs to talk directly to storage",
         "claim": "NVIDIA and SK Hynix are developing SSD-Next, giving GPUs direct "
                  "ultra-high-bandwidth access to storage and shifting topology from CPU-DRAM "
                  "to GPU-SSD.",
         "domain": "compute", "actor": ["nvidia", "sk-hynix"],
         "evidences": ["vertical-silicon"],
         "supersedes": [B + "developments/2025-12-17-storage-next-100m-iops"]},
        {"id": "2025-12-27-intel-hbm5-chiplets",
         "title": "Intel shows cellphone-sized multi-chiplet packages with HBM5",
         "claim": "Intel displayed cellphone-sized multi-chiplet packages carrying HBM5 and "
                  "14A tiles.",
         "domain": "compute", "actor": ["intel"], "evidences": ["vertical-silicon"]},
        {"id": "2025-12-27-stargate-uae-1gw-gas",
         "title": "Stargate UAE tracks toward a 1-GW on-site gas plant",
         "claim": "Orbital imagery showed Stargate UAE construction tracking for a 1-gigawatt "
                  "on-site gas plant.",
         "domain": "energy", "actor": ["openai"], "score": "1 GW",
         "about": [B + "facilities/stargate-uae"],
         "evidences": ["burning-molecules-for-tokens", "politics-as-infrastructure"]},
        {"id": "2025-12-27-india-67-5b-pledge",
         "title": "Amazon, Microsoft and Google pledge $67.5B for India",
         "claim": "Amazon, Microsoft and Google pledged $67.5 billion for infrastructure in "
                  "India.",
         "domain": "economics", "actor": ["amazon", "microsoft", "google"], "score": "$67.5B",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2025-12-11-amazon-india-35b"]},
    ],
}
