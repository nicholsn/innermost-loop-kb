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
         "body": "Builds harnesses that raise base-model performance without retraining."},
        {"id": "minimax", "type": "Organization", "title": "MiniMax",
         "resource": "https://www.minimax.io/", "body": "Chinese lab shipping open-weight models."},
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
         "developed_by": [B + "organizations/minimax"], "modality": "code",
         "body": "Open-weight and tuned for Rust, Java and C++ rather than Python alone."},
        {"id": "tesla-fsd", "type": "AISystem", "title": "Tesla FSD",
         "developed_by": [B + "organizations/tesla"], "modality": "driving"},
    ],
    "benchmarks": [
        {"id": "arc-agi-2", "type": "Benchmark", "title": "ARC-AGI-2",
         "measures_capability": "fluid reasoning resistant to memorization"},
        {"id": "epoch-capabilities-index", "type": "Benchmark", "title": "Epoch Capabilities Index",
         "published_by": [B + "organizations/epoch-ai"],
         "measures_capability": "aggregate rate of frontier capability improvement"},
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
                  "2026, triggering broad automation of knowledge work.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["recursive-self-improvement"]},
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
