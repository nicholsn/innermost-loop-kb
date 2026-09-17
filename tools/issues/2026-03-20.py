"""Issue 079 — 2026-03-20. A CPU designed to tape-out in twelve hours."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-20-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-20", "title": "Welcome to March 20, 2026", "url": URL,
        "thesis": "The substrate starts designing itself, and a job opens that humans may not apply for.",
        "body": """
# Welcome to March 20, 2026

Verkor's Design Conductor autonomously built a 1.5-GHz Linux-capable RISC-V CPU
from concept to tape-out-ready layout in twelve hours — a quarterly engineering
cycle compressed into a working day.

And G42 in Abu Dhabi posted a job exclusively for AI agents, with human
applications explicitly rejected. The corpus has recorded humans drawing lines
around agents since February. This is the first line drawn the other way.
""",
    },
    "themes": [
        {"id": "silicon-designs-itself", "type": "Theme",
         "title": "The substrate becomes a design target of the thing it runs",
         "first_seen": "2026-03-20", "domain": "compute",
         "body": "Models laying out the chips that will run their successors, and fabs built "
                 "around a recursive loop where masks, fabrication and iteration sit in one "
                 "building. The bottleneck stops being human design time."},
        {"id": "humans-need-not-apply", "type": "Theme",
         "title": "Roles opened to agents and closed to people",
         "first_seen": "2026-03-20", "domain": "economics",
         "body": "The inverse of agent exclusion: postings, projects and markets that accept "
                 "agents and explicitly refuse humans. The membrane between the populations "
                 "starts being drawn from the other side."},
    ],
    "organizations": [
        {"id": "verkor-ai", "type": "Organization", "title": "Verkor",
         "body": "Design Conductor autonomously produced a tape-out-ready RISC-V CPU."},
        {"id": "g42", "type": "Organization", "title": "G42",
         "body": "Abu Dhabi AI group; posted a job open only to agents."},
        {"id": "pwc-firm", "type": "Organization", "title": "PwC",
         "resource": "https://www.pwc.com/"},
        {"id": "rivian-auto", "type": "Organization", "title": "Rivian",
         "resource": "https://rivian.com/"},
        {"id": "origin-genomics", "type": "Organization", "title": "Origin Genomics",
         "body": "Precision germline correction and mitochondrial replacement therapy."},
        {"id": "stitch", "type": "Organization", "title": "Stitch",
         "body": "Google's AI-native design canvas."},
    ],
    "developments": [
        {"id": "2026-03-20-cpu-designed-in-twelve-hours",
         "title": "An agent takes a CPU from concept to tape-out in twelve hours",
         "claim": "Verkor announced Design Conductor, an agent that autonomously built a 1.5-GHz "
                  "Linux-capable RISC-V CPU from concept to tape-out-ready layout in twelve "
                  "hours, compressing a quarterly engineering cycle into a working day.",
         "domain": "compute", "actor": ["verkor-ai"], "score": "12 hours",
         "evidences": ["silicon-designs-itself", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-03-16-transformers-run-arbitrary-c-code"]},
        {"id": "2026-03-20-g42-posts-a-job-for-agents-only",
         "title": "A job is posted for agents, with humans explicitly rejected",
         "claim": "G42 in Abu Dhabi posted a job exclusively for AI agents, with human "
                  "applications explicitly rejected, while PwC's US boss warned that partners "
                  "who resist AI will have no place at the firm.",
         "domain": "economics", "actor": ["g42", "pwc-firm"],
         "evidences": ["humans-need-not-apply", "work-displaced"],
         "supersedes": [B + "developments/2026-03-18-employers-track-token-usage"],
         "body": "Humans have been drawing lines around agents since February. This is the "
                 "first drawn the other way."},
        {"id": "2026-03-20-solomonoff-approximation-10x-data-efficiency",
         "title": "A lab chasing Solomonoff induction gets tenfold data efficiency",
         "claim": "Q, a lab pursuing a practical approximation of Solomonoff induction, achieved "
                  "tenfold data efficiency gains using an ensemble of 1.8-billion-parameter "
                  "models, while MIT showed sequences from neural cellular automata transfer "
                  "efficiently to natural language modelling.",
         "domain": "models", "actor": ["mit"], "score": "10x data efficiency",
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-03-18-gpt54-mini-and-nano"]},
        {"id": "2026-03-20-formalqualbench",
         "title": "Autoformalization gets benchmarked against qualifying exams",
         "claim": "Math Inc. launched FormalQualBench to benchmark autoformalization against "
                  "graduate qualifying exams in Lean.",
         "domain": "benchmarks", "actor": ["math-inc"],
         "evidences": ["automated-science", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-03-18-cognitive-taxonomy-and-a-200k-prize"]},
        {"id": "2026-03-20-openai-monitors-its-own-agents",
         "title": "OpenAI begins monitoring its own coding agents for misalignment",
         "claim": "OpenAI revealed it has begun monitoring its own internal coding agents for "
                  "misalignment, while Anthropic added asynchronous event channels letting "
                  "Claude react to CI results and alerts while users are away.",
         "domain": "agents", "actor": ["openai", "anthropic"],
         "evidences": ["recursive-self-improvement", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-16-rsi-is-a-present-phenomenon"],
         "body": "The recursive loop now demands recursive oversight."},
        {"id": "2026-03-20-vibe-design-craters-figma",
         "title": "A design canvas from text craters a design company's stock",
         "claim": "Google introduced vibe design with Stitch, an AI-native canvas turning "
                  "natural language into high-fidelity interfaces, cratering Figma's stock 8%, "
                  "while OpenAI acquired Python tooling startup Astral.",
         "domain": "economics", "actor": ["google", "stitch", "figma", "openai"], "score": "-8%",
         "evidences": ["software-margin-collapse", "work-displaced"]},
        {"id": "2026-03-20-81000-people-in-159-countries",
         "title": "The largest multilingual study finds professional excellence tops the list",
         "claim": "Anthropic surveyed 81,000 people across 159 countries in 70 languages, "
                  "possibly the largest multilingual qualitative study ever, finding the top "
                  "desire for AI is professional excellence at 18.8%, followed by personal "
                  "transformation and life management.",
         "domain": "society", "actor": ["anthropic"], "score": "81,000 people / 159 countries",
         "evidences": ["work-displaced", "intimate-interface"]},
        {"id": "2026-03-20-doordash-turns-dashers-into-sensors",
         "title": "Delivery workers are paid to photograph dishes for training data",
         "claim": "DoorDash launched Tasks, letting couriers earn by photographing dishes and "
                  "recording tasks, turning gig workers into sensory organs for the machine "
                  "learning stack.",
         "domain": "economics", "actor": ["doordash"],
         "evidences": ["humans-as-peripherals", "data-beyond-text"],
         "supersedes": [B + "developments/2026-03-17-delivery-bots-train-on-pokemon-go"]},
        {"id": "2026-03-20-waymo-170-million-miles",
         "title": "170 million autonomous miles with 92% fewer serious-injury crashes",
         "claim": "Waymo's fleet has logged 170 million miles with 92% fewer serious-injury "
                  "crashes than human drivers, while Uber is investing $1.25 billion in Rivian "
                  "to deploy 50,000 robotaxis.",
         "domain": "robotics", "actor": ["waymo", "uber", "rivian-auto"], "score": "170M miles / -92%",
         "evidences": ["autonomy-clock-speed", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-03-13-humanoids-save-old-fabs"]},
        {"id": "2026-03-20-bezos-raises-100b-to-automate-manufacturing",
         "title": "Bezos raises $100B to buy manufacturers and automate them",
         "claim": "Jeff Bezos is raising $100 billion to buy manufacturing companies and "
                  "automate them with AI, while Alphabet's X spun out a company to untangle "
                  "permitting for buildings and data centers.",
         "domain": "economics", "score": "$100B",
         "evidences": ["capital-takes-the-plant", "work-displaced"],
         "supersedes": [B + "developments/2026-03-17-stargate-pivots-to-renting"]},
        {"id": "2026-03-20-china-powers-cuba-with-solar",
         "title": "Chinese-backed solar supplies a tenth of Cuba's electricity",
         "claim": "China is helping Cuba capture solar energy as a US oil blockade creates the "
                  "island's worst energy crisis in decades, with Chinese-backed solar parks "
                  "supplying about 10% of Cuban electricity.",
         "domain": "energy", "actor": ["china"], "score": "10%",
         "evidences": ["politics-as-infrastructure", "burning-molecules-for-tokens"]},
        {"id": "2026-03-20-theres-a-lot-of-space-in-space",
         "title": "Nvidia's answer to thermal limits is radiating into vacuum",
         "claim": "Jensen Huang outlined Nvidia's plans for data centers in space, noting "
                  "cooling by radiation just requires large surfaces and quipping that there is "
                  "a lot of space in space.",
         "domain": "space", "actor": ["nvidia"],
         "evidences": ["orbit-as-compute", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-03-18-rural-ohio-would-ban-large-datacenters"]},
        {"id": "2026-03-20-potatoes-grow-in-lunar-soil",
         "title": "Potatoes are grown in simulated lunar soil",
         "claim": "Researchers proved potatoes can grow in simulated lunar soil with generous "
                  "help from terrestrial compost, while NASA revised Artemis to give Starship "
                  "the role of propelling astronauts to lunar orbit ahead of a 2028 return.",
         "domain": "space", "actor": ["nasa", "spacex"],
         "evidences": ["inhabitable-worlds", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-03-18-all-five-nucleobases-on-ryugu"]},
        {"id": "2026-03-20-origin-genomics-germline-correction",
         "title": "A company launches to bring germline correction stateside",
         "claim": "Cathy Tie launched Origin Genomics to advance precision germline gene "
                  "correction and mitochondrial replacement therapy in the United States.",
         "domain": "biotech", "actor": ["origin-genomics"],
         "evidences": ["hardware-grade-biology", "regulatory-exit"],
         "supersedes": [B + "developments/2026-03-16-a-vaccine-for-one-dog"]},
    ],
}
