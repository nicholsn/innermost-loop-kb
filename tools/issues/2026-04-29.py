"""Issue 103 — 2026-04-29. A model trained only on the past."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-29-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-29", "title": "Welcome to April 29, 2026", "url": URL,
        "thesis": "The Singularity measured by how astonished the past would be.",
        "body": """
# Welcome to April 29, 2026

Alec Radford and colleagues launched Talkie, a 13B model trained only on
pre-1931 text, reportedly most astonished by the 1960s. The corpus opened on
December 14 with TimeCapsuleLLM and Victorian London. Four and a half months
later the same idea returns as a measuring instrument.

And GPT-5.5 topped KernelBench for writing GPU kernels — the model optimizing
the hardware that runs it.
""",
    },
    "organizations": [
        {"id": "true-anomaly", "type": "Organization", "title": "True Anomaly",
         "body": "Raised $650M for space interceptors."},
        {"id": "doudna-lab", "type": "Organization", "title": "Doudna Lab",
         "body": "Used a genomic foundation model to discover a pre-CRISPR targeting system."},
        {"id": "canada-govt", "type": "Organization", "title": "Government of Canada",
         "resource": "https://www.canada.ca/"},
    ],
    "systems": [
        {"id": "talkie", "type": "AISystem", "title": "Talkie",
         "modality": "text",
         "body": "A 13B model trained only on pre-1931 text, used as a measure of how "
                 "astonishing the present is."},
    ],
    "developments": [
        {"id": "2026-04-29-a-model-trained-only-on-the-past",
         "title": "A model trained only on pre-1931 text is used to measure the present",
         "claim": "Alec Radford and colleagues launched Talkie, a 13-billion-parameter model "
                  "trained only on pre-1931 text, which was reportedly especially astonished by "
                  "the events of the 1960s.",
         "domain": "models", "about": [B + "systems/talkie"],
         "evidences": ["resurrection-and-time", "architecture-of-mind"],
         "supersedes": [B + "developments/2025-12-14-timecapsule-llm-victorians"],
         "body": "The corpus opened on a model trained only on Victorian London. This is the "
                 "same idea returned as an instrument for measuring the present."},
        {"id": "2026-04-29-a-model-writes-the-kernels-that-run-it",
         "title": "A model tops the leaderboard for writing the GPU kernels it runs on",
         "claim": "GPT-5.5 topped KernelBench at 6.57% for writing GPU kernels, meaning the "
                  "model is now optimizing the hardware that runs it, while OpenAI's Codex lead "
                  "declared the product has achieved escape velocity and will keep improving "
                  "rapidly.",
         "domain": "models", "actor": ["openai"], "score": "6.57%",
         "evidences": ["recursive-self-improvement", "silicon-designs-itself"],
         "supersedes": [B + "developments/2026-04-27-openai-designs-phone-silicon"]},
        {"id": "2026-04-29-matharena-doubles-in-one-release",
         "title": "A fresh olympiad benchmark more than doubles in a single release",
         "claim": "GPT-5.5 scored a record 73.66% on fresh olympiad problems, more than "
                  "doubling its predecessor's 36.61% and repricing what counts as a hard "
                  "problem.",
         "domain": "benchmarks", "actor": ["openai"], "score": "36.61% → 73.66%",
         "evidences": ["benchmark-saturation", "automated-science"],
         "supersedes": [B + "developments/2026-04-27-a-23-year-old-cracks-an-erdos-problem-in-one-prompt"]},
        {"id": "2026-04-29-mathematicians-become-curators",
         "title": "A student says solutions arrive faster than he can process them",
         "claim": "An MIT senior reported that GPT-5.5 has been finding solutions quicker than "
                  "he can process them, with three full Erdős problem solutions already claimed "
                  "and more in the supervision queue, while observers noted the models are also "
                  "sweeping up neglected open problems and giving them proper statements.",
         "domain": "science", "actor": ["mit"], "score": "3 solutions queued",
         "evidences": ["automated-science", "cognitive-load-inverted"],
         "body": "Mathematicians as curators of synthetic genius."},
        {"id": "2026-04-29-every-ticket-gets-its-own-agent",
         "title": "An orchestrator gives every open ticket its own running agent",
         "claim": "OpenAI's Symphony orchestrator turns a project board into a control plane "
                  "where every open ticket gets its own continuously running agent, with humans "
                  "reduced to reviewing the diffs.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["agents-on-the-org-chart", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-04-23-agents-build-memories-from-screen-captures"]},
        {"id": "2026-04-29-a-classified-deal-for-any-lawful-purpose",
         "title": "Google signs a classified deal for any lawful government purpose",
         "claim": "Google signed a classified AI deal with the Pentagon for any lawful "
                  "government purpose, moving the fence around frontier intelligence closer to "
                  "the situation room.",
         "domain": "policy", "actor": ["google", "war-department"],
         "evidences": ["safety-pledges-recede", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-04-17-google-returns-to-the-pentagon"]},
        {"id": "2026-04-29-two-thirds-of-datacenters-head-for-farm-country",
         "title": "Two thirds of planned datacenters head for rural farmland",
         "claim": "Two-thirds of planned data centers are now headed for rural farm country "
                  "chasing cheap land and tax incentives, inverting the 87% urban concentration "
                  "of existing facilities.",
         "domain": "compute", "score": "67% rural vs 87% urban today",
         "evidences": ["infrastructure-crowding-out", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-04-27-we-have-never-retired-old-a100s"]},
        {"id": "2026-04-29-openai-misses-its-targets",
         "title": "OpenAI misses user and revenue targets as its cloud terms loosen",
         "claim": "OpenAI reportedly missed its user and revenue targets with its chief "
                  "financial officer voicing concern about funding future compute contracts, "
                  "while a revised Microsoft agreement lets it ship across any cloud and ends "
                  "the revenue share.",
         "domain": "economics", "actor": ["openai", "microsoft"],
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-27-the-prize-is-the-kitchen-not-the-recipe"]},
        {"id": "2026-04-29-humanoids-to-cross-drones-by-2033",
         "title": "Humanoid production is projected to cross drones around 2033",
         "claim": "Extrapolating from Epoch AI's analysis, humanoid production should cross "
                  "drones around 2033 and wheeled robots around 2034, putting the embodied "
                  "workforce on the same exponential as the disembodied one, while True Anomaly "
                  "raised $650 million for space interceptors.",
         "domain": "robotics", "actor": ["epoch-ai", "true-anomaly"], "score": "2033 / $650M",
         "evidences": ["physical-recursion", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-04-27-five-hundred-humanoids-on-high-voltage-work"]},
        {"id": "2026-04-29-a-targeting-system-older-than-crispr",
         "title": "A model finds a programmable DNA-targeting system that predates CRISPR",
         "claim": "The Doudna Lab used a genomic foundation model to discover a programmable "
                  "RNA-guided DNA-targeting system hidden inside bacteriophages that predates "
                  "CRISPR and operates on entirely different logic.",
         "domain": "biotech", "actor": ["doudna-lab"],
         "evidences": ["automated-science", "hardware-grade-biology", "discovery-as-process"],
         "supersedes": [B + "developments/2026-04-23-organ-networks-grown-in-animal-wombs"]},
        {"id": "2026-04-29-dead-internet-theory-confirmed",
         "title": "A third of websites created since 2022 turn out to be machine-generated",
         "claim": "A third of websites created since 2022 have turned out to be AI-generated, "
                  "confirming what had been called the dead internet theory.",
         "domain": "society", "score": "33% of new sites",
         "evidences": ["work-displaced", "coordination-tax"],
         "supersedes": [B + "developments/2026-04-23-keystrokes-captured-and-surveillance-pricing-banned"]},
        {"id": "2026-04-29-worst-month-of-tech-layoffs-in-two-years",
         "title": "Tech firms cut 45,800 jobs in the worst month in two years",
         "claim": "Technology firms cut 45,800 jobs in March, the worst month in two years, "
                  "with executives openly framing the layoffs as confidence in a post-human "
                  "future, while Meta prepared to unwind an acquisition after China blocked it "
                  "on national security grounds.",
         "domain": "economics", "actor": ["meta", "china"], "score": "45,800 jobs",
         "evidences": ["work-displaced", "silicon-curtain"],
         "supersedes": [B + "developments/2026-04-26-a-quarter-of-boys-prefer-the-chatbot"]},
        {"id": "2026-04-29-canada-opens-a-sovereign-wealth-fund",
         "title": "Canada announces its first sovereign wealth fund",
         "claim": "Canada's prime minister announced the country's first sovereign wealth fund "
                  "to finance energy, minerals, agriculture and infrastructure of national "
                  "interest, while the California billionaire tax headed to the November ballot.",
         "domain": "policy", "actor": ["canada-govt"],
         "evidences": ["science-as-industrial-policy", "regulatory-exit"],
         "supersedes": [B + "developments/2026-04-27-insurers-drop-ai-damages"]},
    ],
}
