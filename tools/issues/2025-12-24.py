"""Issue 014 — 2025-12-24. The harness beats the model."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-24-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-24", "title": "Welcome to December 24, 2025", "url": URL,
        "thesis": "The curve is steepening into a wall.",
        "body": """
# Welcome to December 24, 2025

Poetiq's *harness* — not a new model — takes ARC-AGI-2 to 75% at under $8 a
problem, beating the previous state of the art by roughly 15% **without touching
the base weights**. The scaffolding thesis the corpus has tracked since issue 002
now produces the headline result outright.

The Epoch Capabilities Index supplies the mechanism: frontier improvement rates
nearly doubled after April 2024, on the shift to reasoning.
""",
    },
    "organizations": [
        {"id": "poetiq", "type": "Organization", "title": "Poetiq",
         "description": "AI startup that builds inference-time harnesses which lift frontier-model "
                        "scores without retraining, from 75% on ARC-AGI-2 to a self-optimizing Metasystem.",
         "resource": "https://poetiq.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q137132799"],
         "tags": ["startup"],
         "body": "Builds harnesses that raise base-model performance without retraining — "
                 "scaffolding around other labs' models rather than models of its own. In this "
                 "corpus its harness on GPT-5.2-xhigh "
                 "[took ARC-AGI-2 to 75% at under $8 a problem](/developments/2025-12-24-poetiq-harness-arc-agi-2.md) "
                 "without touching the base weights, it later "
                 "[orchestrated Gemini, GPT and Claude to 55% on Humanity's Last Exam](/developments/2026-02-11-poetiq-55pct-hle.md), "
                 "and in August it unveiled a "
                 "[self-optimizing Metasystem](/developments/2026-08-08-a-self-optimizing-optimizer.md) "
                 "that upgrades its own harnesses, prompts and code, arguing recursive "
                 "self-improvement is the fastest path to superintelligence."},
        {"id": "minimax", "type": "Organization", "title": "MiniMax",
         "description": "Chinese AI lab shipping the open-weight MiniMax M2 model line, from the "
                        "systems-language-tuned M2.1 to M2.7, which it said participates in its own evolution.",
         "resource": "https://www.minimax.io/",
         "sameAs": ["http://www.wikidata.org/entity/Q130263208"],
         "tags": ["startup", "open-source"],
         "body": "Chinese lab shipping open-weight models. In this corpus MiniMax releases "
                 "[M2.1](/systems/minimax-m2-1.md), "
                 "[tuned for Rust, Java and C++](/developments/2025-12-24-minimax-m2-1-systems-languages.md) "
                 "rather than Python alone, and three months later [M2.7](/systems/minimax-m2-7.md), "
                 "which it described as its first model "
                 "[deeply participating in its own evolution](/developments/2026-03-23-minimax-model-participates-in-its-own-evolution.md) "
                 "— the recursive-self-improvement claim arriving from the other side of the Pacific."},
        {"id": "boston-dynamics", "type": "Organization", "title": "Boston Dynamics",
         "resource": "https://bostondynamics.com/", "body": "Builds the Atlas humanoid."},
        {"id": "intel", "type": "Organization", "title": "Intel",
         "resource": "https://www.intel.com/", "body": "Fab and chip designer."},
        {"id": "databricks", "type": "Organization", "title": "Databricks",
         "resource": "https://www.databricks.com/", "body": "Data and AI platform."},
        {"id": "hugging-face", "type": "Organization", "title": "Hugging Face",
         "resource": "https://huggingface.co/", "body": "Model and dataset hub."},
    ],
    "systems": [
        {"id": "poetiq-harness", "type": "AISystem", "title": "Poetiq harness",
         "developed_by": [B + "organizations/poetiq"], "modality": "harness",
         "evaluated_on": [B + "benchmarks/arc-agi-2"]},
        {"id": "gemma-scope-2", "type": "AISystem", "title": "Gemma Scope 2",
         "developed_by": [B + "organizations/google-deepmind"], "modality": "interpretability",
         "body": "Sparse autoencoders on every layer, mapping the geography of machine thought."},
        {"id": "minimax-m2-1", "type": "AISystem", "title": "MiniMax M2.1",
         "description": "MiniMax's open-weight coding and agentic model of December 2025, tuned for "
                        "multi-language programming in Rust, Java and C++ rather than Python alone.",
         "resource": "https://www.minimax.io/news/minimax-m21",
         "developed_by": [B + "organizations/minimax"], "modality": "code",
         "tags": ["open-weight-model", "coding-agent"],
         "body": "MiniMax M2.1 is the December 2025 update to [MiniMax](/organizations/minimax.md)'s "
                 "open-weight M2 line, which the lab's release note pitches as built for real-world "
                 "complex tasks across many programming languages rather than Python alone "
                 "([release note](https://www.minimax.io/news/minimax-m21)). It enters the corpus "
                 "through its [systems-language release](/developments/2025-12-24-minimax-m2-1-systems-languages.md), "
                 "and four days later MiniMax [wired the same agentic model to a Vita Dynamics robot dog](/developments/2025-12-28-minimax-robot-dog-zero-shot.md) "
                 "with no prior physical-world training. Its successor "
                 "[M2.7](/systems/minimax-m2-7.md) is the model MiniMax later described as "
                 "[participating in its own evolution](/developments/2026-03-23-minimax-model-participates-in-its-own-evolution.md)."},
        {"id": "tesla-fsd", "type": "AISystem", "title": "Tesla FSD",
         "developed_by": [B + "organizations/tesla"], "modality": "driving"},
    ],
    "benchmarks": [
        {"id": "arc-agi-2", "type": "Benchmark", "title": "ARC-AGI-2",
         "description": "The ARC Prize Foundation's second abstraction-and-reasoning benchmark, whose "
                        "climb from harness-driven 75% to declared saturation the corpus uses to date "
                        "the end of fluid-intelligence tests as a ceiling.",
         "resource": "https://arcprize.org/arc-agi/2",
         "published_by": [B + "organizations/arc-prize"],
         "measures_capability": "fluid reasoning resistant to memorization",
         "tags": ["open-source"],
         "body": "ARC-AGI-2 is the second generation of the Abstraction and Reasoning Corpus published "
                 "by the [ARC Prize Foundation](/organizations/arc-prize.md): grid puzzles meant to "
                 "resist memorization and measure fluid reasoning, with public training and evaluation "
                 "sets on GitHub ([benchmark page](https://arcprize.org/arc-agi/2)). In this corpus it "
                 "is the benchmark that a harness, not a new model, first took to "
                 "[75% at under $8 a problem](/developments/2025-12-24-poetiq-harness-arc-agi-2.md); "
                 "two days later the foundation "
                 "[declared it saturated](/developments/2025-12-26-arc-declares-saturation.md), and by "
                 "February program synthesis had "
                 "[pushed it to 97.92%](/developments/2026-02-24-two-hours-of-video-in-a-million-tokens.md). "
                 "The successor is [ARC-AGI-3](/benchmarks/arc-agi-3.md)."},
        {"id": "epoch-capabilities-index", "type": "Benchmark", "title": "Epoch Capabilities Index",
         "description": "Epoch AI's composite index that places frontier models on a single capability "
                        "scale across benchmarks, the yardstick the corpus uses for the post-April-2024 "
                        "acceleration and later discontinuities.",
         "resource": "https://epoch.ai/eci",
         "published_by": [B + "organizations/epoch-ai"],
         "measures_capability": "aggregate rate of frontier capability improvement",
         "tags": ["open-source"],
         "body": "The Epoch Capabilities Index (ECI) is [Epoch AI](/organizations/epoch-ai.md)'s "
                 "composite measure that combines frontier models' scores across many benchmarks into "
                 "one capability scale, published with CC-BY data and a public repository "
                 "([index page](https://epoch.ai/eci)). The corpus first cites it for the finding that "
                 "[frontier improvement rates nearly doubled after April 2024](/developments/2025-12-24-epoch-capabilities-index-doubling.md) "
                 "on the shift to reasoning, and returns to it in April 2026 when Claude Mythos's "
                 "[benchmark sweep](/developments/2026-04-08-mythos-benchmark-sweep.md) registered as an "
                 "apparent upward discontinuity on the index."},
    ],
    "people": [
        {"id": "sholto-douglas", "type": "Person", "title": "Sholto Douglas", "name": "Sholto Douglas",
         "description": "Anthropic AI researcher whose forecast that continual learning would be "
                        "solved in 2026 the corpus tracks against later test-time-training results.",
         "resource": "https://x.com/_sholtodouglas",
         "sameAs": ["http://www.wikidata.org/entity/Q126287446"],
         "tags": ["researcher"],
         "body": "Sholto Douglas is an AI researcher at Anthropic. He enters the corpus through "
                 "No Priors' 2026 prediction episode, in which he "
                 "[predicts continual learning will be solved in 2026](/developments/2025-12-24-sholto-continual-learning-2026.md), "
                 "triggering the total automation of knowledge work — a forecast that Stanford's "
                 "[test-time-training result](/developments/2025-12-30-stanford-test-time-training.md) "
                 "began to cash out six days later."},
    ],
    "roles": [
        {"id": "sholto-douglas-anthropic-researcher", "type": "Role",
         "title": "Sholto Douglas, AI researcher at Anthropic",
         "roleName": "Researcher, RL scaling",
         "memberOf": [B + "organizations/anthropic"],
         "holder": [B + "people/sholto-douglas"],
         "description": "The position from which he predicted, on the No Priors podcast, that "
                        "continual learning would be solved in 2026.",
         "body": "The newsletter identifies him only as \"Anthropic's Sholto Douglas\"; his X "
                 "profile describes him as working on scaling RL at Anthropic, formerly DeepMind. "
                 "The role matters to the "
                 "corpus because the forecast comes from inside a frontier lab, four days after "
                 "another Anthropic researcher "
                 "[pivoted fully to automated alignment](/developments/2025-12-20-mcaleer-automated-alignment.md)."},
    ],
    "developments": [
        {"id": "2025-12-24-poetiq-harness-arc-agi-2",
         "title": "A harness takes ARC-AGI-2 to 75% without touching the model",
         "claim": "Poetiq's harness on GPT-5.2-xhigh reached 75% on ARC-AGI-2 at under $8 per "
                  "problem, beating the prior state of the art by about 15% with no "
                  "modification to the base model.",
         "domain": "benchmarks", "actor": ["poetiq", "openai"], "score": "75%, <$8/problem",
         "about": [B + "systems/poetiq-harness", B + "benchmarks/arc-agi-2"],
         "evidences": ["scaffolding-over-weights", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2025-12-13-zoom-federated-swarm-hle"],
         "body": "The scaffolding thesis producing the headline number, not a footnote."},
        {"id": "2025-12-24-epoch-capabilities-index-doubling",
         "title": "Frontier improvement rates nearly doubled after April 2024",
         "claim": "The Epoch Capabilities Index showed frontier model improvement rates nearly "
                  "doubled after April 2024, driven by the shift to reasoning.",
         "domain": "benchmarks", "actor": ["epoch-ai"], "score": "~2x rate",
         "about": [B + "benchmarks/epoch-capabilities-index"],
         "evidences": ["autonomy-clock-speed"]},
        {"id": "2025-12-24-gemma-scope-2-saes",
         "title": "Gemma Scope 2 puts sparse autoencoders on every layer",
         "claim": "DeepMind released Gemma Scope 2, placing sparse autoencoders on every layer "
                  "to map the internal geography of the model.",
         "domain": "models", "actor": ["google-deepmind"], "about": [B + "systems/gemma-scope-2"],
         "evidences": ["machine-introspection"],
         "supersedes": [B + "developments/2025-12-21-anthropic-activation-oracles"]},
        {"id": "2025-12-24-marlinspike-last-days-of-software",
         "title": "Moxie Marlinspike describes the last days of software development",
         "claim": "Signal founder Moxie Marlinspike described the novel sensation of living "
                  "through the last days of software development.",
         "domain": "society", "evidences": ["engineer-as-supervisor"]},
        {"id": "2025-12-24-sholto-continual-learning-2026",
         "title": "Anthropic's Sholto Douglas predicts continual learning solved in 2026",
         "claim": "Anthropic's Sholto Douglas predicted continual learning will be solved in "
                  "2026, triggering the total automation of knowledge work.",
         "description": "A frontier-lab insider puts a date on the missing ingredient and ties it "
                        "directly to the end of knowledge work, giving the corpus a forecast to "
                        "read later test-time-training results against.",
         "domain": "agents", "actor": ["people/sholto-douglas", "anthropic"],
         "score": "solved in 2026",
         "evidences": ["recursive-self-improvement"],
         "relatedTo": [B + "developments/2025-12-19-shazeer-5050-gemini-breakthrough",
                       B + "developments/2025-12-15-ai-2027-forecast-accuracy",
                       B + "developments/2025-12-20-mcaleer-automated-alignment"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2025-12-24-marlinspike-last-days-of-software",
                        "relation_label": "corroborates"}],
         "tags": ["forecast", "continual-learning", "labor", "rsi"],
         "supporting_text": "continual learning will be solved in 2026",
         "sources": [{"id": "no-priors-sholto-douglas-continual-learning",
                      "resource": "https://x.com/nopriorspod/status/2002120381709365257",
                      "title": "No Priors 2026 prediction episode",
                      "author": "org:no-priors"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "In No Priors' 2026 prediction episode "
                 "([announced on X](https://x.com/nopriorspod/status/2002120381709365257)), Anthropic's "
                 "[Sholto Douglas](/people/sholto-douglas.md) predicts that continual learning — "
                 "models that keep learning after deployment — will be solved in 2026, and that "
                 "solving it triggers the total automation of knowledge work. The newsletter "
                 "pairs it with Moxie Marlinspike's "
                 "[\"last days of software development\"](/developments/2025-12-24-marlinspike-last-days-of-software.md) "
                 "as the same sentiment from a builder and a researcher. In the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) strand it "
                 "follows Stephen McAleer's "
                 "[pivot to automated alignment](/developments/2025-12-20-mcaleer-automated-alignment.md) "
                 "and Noam Shazeer's "
                 "[even odds on Gemini making the next breakthrough](/developments/2025-12-19-shazeer-5050-gemini-breakthrough.md) "
                 "as the third lab-insider forecast in five days; six days later Stanford's "
                 "[test-time training](/developments/2025-12-30-stanford-test-time-training.md) "
                 "is the first result the corpus reads against it."},
        {"id": "2025-12-24-minimax-m2-1-systems-languages",
         "title": "MiniMax M2.1 targets Rust, Java and C++",
         "claim": "MiniMax released M2.1, an open-weight model optimized for Rust, Java and "
                  "C++ rather than Python alone.",
         "domain": "models", "actor": ["minimax"], "about": [B + "systems/minimax-m2-1"],
         "evidences": ["open-weight-latency"]},
        {"id": "2025-12-24-physical-turing-test-passed",
         "title": "NVIDIA's robotics director says FSD v14 passes the Physical Turing Test",
         "claim": "NVIDIA's director of robotics declared Tesla FSD v14 has crossed the "
                  "Physical Turing Test threshold.",
         "domain": "robotics", "actor": ["nvidia", "tesla"], "about": [B + "systems/tesla-fsd"],
         "evidences": ["physical-recursion"],
         "supersedes": [B + "developments/2025-12-22-tesla-fsd-power-outage"]},
        {"id": "2025-12-24-robotics-datasets-25x",
         "title": "Robotics datasets become the largest category on Hugging Face",
         "claim": "Robotics datasets on Hugging Face rose from rank 44 to first in three years, "
                  "growing 25x in the last twelve months.",
         "domain": "robotics", "actor": ["hugging-face"], "score": "25x in 12 months",
         "evidences": ["data-beyond-text"]},
        {"id": "2025-12-24-boston-dynamics-new-atlas",
         "title": "Boston Dynamics readies a new Atlas for CES 2026",
         "claim": "Boston Dynamics is preparing to unveil a new Atlas humanoid at CES 2026.",
         "domain": "robotics", "actor": ["boston-dynamics"]},
        {"id": "2025-12-24-white-house-robotic-shipyards",
         "title": "The White House calls for robotic factories to build warships",
         "claim": "The White House called for robotic factories to build Navy battleships.",
         "domain": "policy", "actor": ["white-house"],
         "evidences": ["physical-recursion", "politics-as-infrastructure"]},
        {"id": "2025-12-24-robotaxi-biowaste-fee",
         "title": "Tesla adds a $150 robotaxi cleaning fee",
         "claim": "Tesla introduced automated cleaning fees for robotaxis, charging $150 when "
                  "passengers leave biowaste behind.",
         "domain": "robotics", "actor": ["tesla"], "score": "$150",
         "body": "Autonomy meeting the part of the job nobody models."},
        {"id": "2025-12-24-billiards-turing-complete",
         "title": "Classical billiard systems are shown Turing complete",
         "claim": "Researchers found classical billiard systems are Turing complete, implying "
                  "ideal gases can perform computation in the right container.",
         "domain": "science", "evidences": ["compiling-matter"]},
        {"id": "2025-12-24-intel-18a-arizona",
         "title": "Intel enters high-volume 18A production in Arizona",
         "claim": "Intel began high-volume production of 18A, 2-nm class chips in Arizona.",
         "domain": "compute", "actor": ["intel"], "score": "18A / 2 nm class",
         "evidences": ["silicon-curtain"],
         "supersedes": [B + "developments/2025-12-21-tsmc-arizona-3nm-2027"]},
        {"id": "2025-12-24-china-15gw-solar-thermal",
         "title": "China plans 15 GW of solar thermal",
         "claim": "China is rolling out a roadmap for 15 gigawatts of solar thermal power.",
         "domain": "energy", "actor": ["china"], "score": "15 GW",
         "evidences": ["industrialized-nature"]},
        {"id": "2025-12-24-bitcoin-miners-retool-for-ai",
         "title": "Bitcoin mining ETF surges 90% as miners retool for AI",
         "claim": "The CoinShares Bitcoin Mining ETF rose 90% as miners repurposed their "
                  "thermodynamics for AI training.",
         "domain": "economics", "score": "+90%",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2025-12-19-anthropic-2-3gw-bitcoin-miners"]},
        {"id": "2025-12-24-bolivia-datacenters",
         "title": "Tesla, Amazon and Oracle invest in Bolivian datacenters",
         "claim": "Tesla, Amazon and Oracle are investing in Bolivian data centers, ending two "
                  "decades of socialist isolation.",
         "domain": "economics", "actor": ["tesla", "amazon", "oracle"],
         "evidences": ["capital-takes-the-plant"]},
        {"id": "2025-12-24-eu-datacenter-2-6b",
         "title": "$2.6B deployed for Frankfurt, Amsterdam and Paris datacenters",
         "claim": "A Canadian pension fund and Australia's Goodman Group are deploying $2.6 "
                  "billion for data center projects in Frankfurt, Amsterdam and Paris.",
         "domain": "economics", "score": "$2.6B",
         "evidences": ["capital-takes-the-plant"]},
        {"id": "2025-12-24-us-gdp-4-3-percent",
         "title": "US GDP growth hits 4.3% on AI investment",
         "claim": "US GDP growth reached 4.3%, driven by AI investment.",
         "domain": "economics", "score": "4.3%", "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-24-equity-research-15-minutes",
         "title": "Banks publish equity research 15 minutes after earnings calls",
         "claim": "Databricks reported banks using AI to issue equity research 15 minutes after "
                  "earnings calls.",
         "domain": "economics", "actor": ["databricks"], "score": "15 minutes",
         "evidences": ["autonomous-commerce"]},
    ],
}
