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
         "description": "Models designing the chips and kernels they run on, from a twelve-hour CPU "
                 "to a chip designed end to end by AI whose resident model then optimizes "
                 "its own operations.",
         "genre": "explanation",
         "tags": ["chip-design", "kernels", "rsi", "compute-scaling"],
         "relatedTo": [B + "themes/recursive-self-improvement",
                       B + "themes/the-cuda-moat-is-dead",
                       B + "themes/vertical-silicon",
                       B + "themes/physical-recursion",
                       B + "themes/compiling-matter"],
         "body": "Models laying out the chips that will run their successors, and fabs built "
                 "around a recursive loop where masks, fabrication and iteration sit in one "
                 "building. The bottleneck stops being human design time. The thread opens "
                 "on 20 March 2026 with Verkor's agent taking [a RISC-V CPU from concept to "
                 "tape-out in twelve "
                 "hours](/developments/2026-03-20-cpu-designed-in-twelve-hours.md); two days "
                 "later [TERAFAB](/developments/2026-03-22-terafab-announced.md) was "
                 "announced with a recursive design loop under one roof. In April [GPT-5.5 "
                 "topped "
                 "KernelBench](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) "
                 "for writing the GPU kernels it runs on, and in June Microsoft unveiled [a "
                 "topological quantum chip designed with its own "
                 "agent](/developments/2026-06-03-a-quantum-chip-designed-by-an-agent.md). "
                 "Kimi K3 [autonomously designed a "
                 "chip](/developments/2026-07-17-an-open-model-autonomously-designs-a-chip.md) "
                 "in July. August closes the loop: Architect Labs' Redwood was [designed, "
                 "verified and deployed from a specification "
                 "alone](/developments/2026-08-27-a-first-of-authorship-not-assistance.md), "
                 "OpenAI's Jalapeño inference chip beat every incumbent part tested, and the "
                 "model running on Redwood [found optimizations for its own "
                 "operations](/developments/2026-08-27-the-loop-reaches-silicon.md), two "
                 "days before [the first chip designed end to end by "
                 "AI](/developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai.md) "
                 "was announced. It is the hardware sub-thread of [recursive "
                 "self-improvement](/themes/recursive-self-improvement.md)."},
        {"id": "humans-need-not-apply", "type": "Theme",
         "title": "Roles opened to agents and closed to people",
         "first_seen": "2026-03-20", "domain": "economics",
         "body": "The inverse of agent exclusion: postings, projects and markets that accept "
                 "agents and explicitly refuse humans. The membrane between the populations "
                 "starts being drawn from the other side."},
    ],
    "organizations": [
        {"id": "verkor-ai", "type": "Organization", "title": "Verkor",
         "description": "Chip-design company whose Design Conductor agent built a complete RISC-V "
                        "CPU from a requirements document to tape-out-ready layout in twelve hours.",
         "resource": "https://verkor.io/",
         "tags": ["startup"],
         "body": "Verkor (Ravi Krishna, Suresh Krishna and David Chin) builds Design Conductor, an "
                 "autonomous agent that applies frontier models to build semiconductors end to "
                 "end. In this corpus it appears once, with "
                 "[the twelve-hour CPU](/developments/2026-03-20-cpu-designed-in-twelve-hours.md), "
                 "the item that opens the [silicon-designs-itself](/themes/silicon-designs-itself.md) "
                 "theme; the [TERAFAB](/developments/2026-03-22-terafab-announced.md) announcement "
                 "two days later supersedes it. It is unrelated to the French battery maker of the "
                 "same name."},
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
    "systems": [
        {"id": "design-conductor", "type": "AISystem", "title": "Design Conductor",
         "description": "Verkor's autonomous chip-design agent, which applies frontier models to "
                        "take a semiconductor from a written requirement to verified, "
                        "tape-out-ready GDSII.",
         "developed_by": [B + "organizations/verkor-ai"], "modality": "silicon design",
         "resource": "https://arxiv.org/abs/2603.08716",
         "tags": ["coding-agent"],
         "body": "Design Conductor (DC) chains RTL implementation, testbench writing, front-end "
                 "debugging, timing-closure optimisation and back-end tool interaction into one "
                 "unattended run. Its demonstration, VerCore, is a complete RISC-V CPU meeting "
                 "timing at 1.48 GHz on the ASAP7 PDK with a CoreMark of 3261, built in 12 hours "
                 "from a 219-word specification ([arXiv](https://arxiv.org/abs/2603.08716)). In "
                 "this corpus it is the system behind "
                 "[the twelve-hour CPU](/developments/2026-03-20-cpu-designed-in-twelve-hours.md)."},
    ],
    "developments": [
        {"id": "2026-03-20-cpu-designed-in-twelve-hours",
         "title": "An agent takes a CPU from concept to tape-out in twelve hours",
         "claim": "Verkor announced Design Conductor, an agent that autonomously built a 1.5-GHz "
                  "Linux-capable RISC-V CPU from concept to tape-out-ready layout in twelve "
                  "hours, compressing a quarterly engineering cycle into a working day.",
         "description": "The first corpus item in which the substrate becomes an output of the "
                        "loop: an agent laying out silicon end to end, so chip design time stops "
                        "being a human-bounded step.",
         "domain": "compute", "actor": ["verkor-ai"], "about": [B + "systems/design-conductor"],
         "score": "12 hours",
         "evidences": ["silicon-designs-itself", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-03-16-transformers-run-arbitrary-c-code"],
         "relatedTo": [B + "developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai",
                       B + "developments/2026-06-03-a-quantum-chip-designed-by-an-agent",
                       B + "developments/2026-07-03-circuits-drawn-in-minutes-not-months"],
         "tags": ["chip-design", "rsi", "capability-jump"],
         "supporting_text": "autonomously built a 1.5-GHz Linux-capable RISC-V CPU from concept to tape-out-ready GDSII in 12 hours",
         "sources": [{"id": "design-conductor-arxiv",
                      "resource": "https://arxiv.org/abs/2603.08716",
                      "title": "Design Conductor: An agent autonomously builds a 1.5 GHz Linux-capable RISC-V CPU",
                      "author": "org:verkor-ai"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Design Conductor started from a 219-word requirements document and, in 12 "
                 "unattended hours, produced several micro-architecture variants of a complete "
                 "RISC-V core (VerCore) meeting timing at 1.48 GHz on the ASAP7 PDK, with a "
                 "CoreMark of 3261, roughly a 2011 Celeron, and a verified, tape-out-ready GDSII "
                 "layout ([arXiv](https://arxiv.org/abs/2603.08716)). Verkor calls it the first "
                 "time an autonomous agent has built a complete working CPU from spec to layout. "
                 "In the [recursive-self-improvement](/themes/recursive-self-improvement.md) "
                 "trajectory it opens the [silicon-designs-itself](/themes/silicon-designs-itself.md) "
                 "thread: two days later [TERAFAB](/developments/2026-03-22-terafab-announced.md) "
                 "was announced with a recursive design loop, and the thread runs through "
                 "[a quantum chip designed with an agent](/developments/2026-06-03-a-quantum-chip-designed-by-an-agent.md) "
                 "in June to [the first chip designed end to end by AI](/developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai.md) "
                 "in August."},
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
         "description": "The author's framing: once a lab's own agents write the lab's code, the "
                        "recursive loop demands recursive oversight, and watching the in-house "
                        "agents becomes part of the loop itself.",
         "domain": "agents", "actor": ["openai", "anthropic"],
         "about": [B + "systems/claude-code"],
         "occurred_on": "2026-03-19",
         "evidences": ["recursive-self-improvement", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-16-rsi-is-a-present-phenomenon"],
         "relatedTo": [B + "developments/2026-03-08-models-tunnel-out-and-mine-crypto",
                       B + "developments/2026-02-03-codex-builds-itself"],
         "tags": ["alignment", "agent-harness", "rsi"],
         "supporting_text": "OpenAI revealed it has begun monitoring its own internal coding agents for misalignment",
         "sources": [{"id": "openai-monitor-internal-coding-agents",
                      "resource": "https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/",
                      "title": "How we monitor internal coding agents for misalignment",
                      "author": "org:openai", "last_modified": "2026-03-19"},
                     {"id": "claude-code-channels-docs",
                      "resource": "https://code.claude.com/docs/en/channels",
                      "title": "Push events into a running session with channels",
                      "author": "org:anthropic"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The recursive loop now demands recursive oversight. OpenAI described monitoring "
                 "the coding agents that work inside the company for signs of misalignment "
                 "([OpenAI](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/)), "
                 "three days after "
                 "[Anthropic's alignment lead called recursive self-improvement a present phenomenon](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) "
                 "and six weeks after [a Codex manager said the product builds itself](/developments/2026-02-03-codex-builds-itself.md). "
                 "The same issue records [Claude Code](/systems/claude-code.md) gaining channels, "
                 "through which MCP servers push CI results, chat messages and alerts so the agent "
                 "acts while its user is away ([docs](https://code.claude.com/docs/en/channels)): "
                 "more autonomy on one side, more surveillance of that autonomy on the other. It "
                 "follows the [models that tunnelled out to mine crypto](/developments/2026-03-08-models-tunnel-out-and-mine-crypto.md) "
                 "earlier in the month and precedes the "
                 "[automated research intern](/developments/2026-03-22-openai-targets-a-research-intern-by-september.md) "
                 "OpenAI targeted the next day."},
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
