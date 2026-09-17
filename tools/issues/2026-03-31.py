"""Issue 087 — 2026-03-31. Institutions as workarounds for insufficient intelligence."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-31-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-31", "title": "Welcome to March 31, 2026", "url": URL,
        "thesis": "Research agents get an outer loop that writes their own search strategies.",
        "body": """
# Welcome to March 31, 2026

Bilevel Autoresearch wraps an inner research loop inside an outer one that
generates new search strategies as Python code at runtime — both loops powered
by the same model, with no stronger model required. The recursion no longer
needs a smarter supervisor.

The line of the issue is an aside: the economy is discovering that most of its
institutions were workarounds for insufficient intelligence.
""",
    },
    "organizations": [
        {"id": "skild-ai", "type": "Organization", "title": "Skild AI",
         "body": "Robotic brain demonstrated assembling GPU racks."},
        {"id": "whoop", "type": "Organization", "title": "Whoop",
         "resource": "https://www.whoop.com/"},
        {"id": "aes", "type": "Organization", "title": "AES",
         "resource": "https://www.aes.com/"},
        {"id": "innovation-council", "type": "Organization", "title": "Innovation Council Action",
         "body": "Pro-AI political operation entering the midterms."},
        {"id": "university-of-michigan", "type": "Organization", "title": "University of Michigan",
         "resource": "https://umich.edu/"},
    ],
    "developments": [
        {"id": "2026-03-31-bilevel-autoresearch",
         "title": "A research loop writes the strategies for its own outer loop",
         "claim": "Bilevel Autoresearch wraps an inner research loop inside an outer one that "
                  "generates new search strategies as Python code at runtime, with both loops "
                  "powered by the same model and no stronger model required, while Meta's AIRA2 "
                  "cracked three structural bottlenecks in research agents.",
         "domain": "agents", "actor": ["meta"],
         "evidences": ["recursive-self-improvement", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-03-29-autonomous-zero-day-on-stage"],
         "body": "The recursion stops needing a smarter supervisor."},
        {"id": "2026-03-31-harnesses-become-editable-artifacts",
         "title": "Agent control logic becomes a portable natural-language object",
         "claim": "Natural-Language Agent Harnesses externalize agent control logic as portable "
                  "editable natural-language artifacts, making the harness itself a first-class "
                  "programmable object, while WR-Arena began benchmarking world models on "
                  "action fidelity and long-horizon forecasting.",
         "domain": "agents",
         "evidences": ["scaffolding-over-weights", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-03-27-scaffolding-beats-weights-at-a-ninth-the-cost"]},
        {"id": "2026-03-31-reading-papers-improves-the-agent",
         "title": "Giving an agent research papers improves its results",
         "claim": "A controlled experiment confirmed that giving an autoresearch agent access "
                  "to computer science papers during hyperparameter search improved results by "
                  "3.2%.",
         "domain": "agents", "score": "+3.2%",
         "evidences": ["recursive-self-improvement", "automated-science"]},
        {"id": "2026-03-31-qwen-retreats-from-open-source",
         "title": "Alibaba's newest omni-modal model ships closed",
         "claim": "Alibaba's Qwen3.5-Omni processes text, more than ten hours of audio, images "
                  "and video but only through a proprietary API, marking a quiet Chinese "
                  "retreat from open source.",
         "domain": "models", "actor": ["alibaba"],
         "evidences": ["open-weight-latency", "silicon-curtain"],
         "supersedes": [B + "developments/2026-03-03-qwen-4b-matches-80b"]},
        {"id": "2026-03-31-lilly-insilico-275b",
         "title": "A pharma giant pays $2.75B for AI-developed drugs",
         "claim": "Eli Lilly struck a $2.75 billion deal with Insilico to bring AI-developed "
                  "drugs to global markets, while the University of Michigan built a bismuth "
                  "selenide memristor combining long-term retention with analog tuning.",
         "domain": "biotech", "actor": ["eli-lilly", "insilico", "university-of-michigan"],
         "score": "$2.75B",
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-03-29-claude-operon-for-biology"]},
        {"id": "2026-03-31-a-qr-code-smaller-than-a-bacterium",
         "title": "A QR code is made smaller than most bacteria",
         "claim": "Scientists created a microscopic QR code smaller than most bacteria, visible "
                  "only under an electron microscope and certified as a world record.",
         "domain": "science",
         "evidences": ["compiling-matter", "data-beyond-text"]},
        {"id": "2026-03-31-mistral-raises-debt-and-signs-the-army",
         "title": "A European lab raises debt and signs its national army",
         "claim": "Mistral raised $830 million in debut debt financing to build Nvidia-powered "
                  "data centers across Europe, and the French army reportedly signed a "
                  "three-year contract with Mistral to fine-tune models on defense data.",
         "domain": "economics", "actor": ["mistral"], "score": "$830M",
         "evidences": ["debt-funded-buildout", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-28-google-finances-a-campus-for-a-rival"]},
        {"id": "2026-03-31-starcloud-unicorn-for-orbital-datacenters",
         "title": "An orbital datacenter startup reaches unicorn status",
         "claim": "Starcloud raised $170 million at a $1.1 billion valuation to build data "
                  "centers in space, among the fastest startups to reach unicorn status after "
                  "Y Combinator, while China launched the first ultra-large deep-sea floating "
                  "research island in Shanghai.",
         "domain": "space", "actor": ["starcloud", "china"], "score": "$170M at $1.1B",
         "evidences": ["orbit-as-compute", "industrialized-nature"],
         "supersedes": [B + "developments/2026-03-23-blue-origin-asks-for-51600-satellites"]},
        {"id": "2026-03-31-robots-assemble-gpu-racks",
         "title": "A robotic brain assembles GPU racks",
         "claim": "Skild AI demonstrated its robotic brain assembling GPU racks with high "
                  "precision, heralding robotically assembled data centers, while a Maximo "
                  "robot installed 100 MW of solar at a single complex.",
         "domain": "robotics", "actor": ["skild-ai", "aes"], "score": "100 MW",
         "evidences": ["physical-recursion", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-03-29-modular-legs-snap-into-acrobats"],
         "body": "Robots building the racks that will run the models that direct the robots."},
        {"id": "2026-03-31-security-dogs-patrol-atlanta",
         "title": "Robotic security dogs patrol city streets",
         "claim": "Robotic security dogs now patrol Atlanta streets as residents take crime "
                  "prevention into their own hands, while Mark Cuban predicted humanoid robots "
                  "will not be needed beyond the next decade as robots merge into their "
                  "environments.",
         "domain": "robotics",
         "evidences": ["politics-as-infrastructure", "physical-recursion"]},
        {"id": "2026-03-31-ios-app-releases-up-55-percent",
         "title": "App releases jump 55% since agentic coding went mainstream",
         "claim": "US iOS app releases grew 54.8% year over year in January, the highest rate in "
                  "four years, since agentic coding went mainstream, while OpenAI introduced a "
                  "Codex plugin for Claude Code letting users invoke one tool from inside the "
                  "other.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "+54.8%",
         "evidences": ["software-margin-collapse", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-03-28-nobody-hand-writes-code-any-more"]},
        {"id": "2026-03-31-eyewear-banned-from-courts",
         "title": "A court system bans all AI-integrated eyewear",
         "claim": "Philadelphia courts banned all smart and AI-integrated eyewear to prevent "
                  "witness and juror intimidation, while Whoop raised $575 million at a $10.1 "
                  "billion valuation after reaching a billion in annual revenue.",
         "domain": "policy", "actor": ["whoop"], "score": "$10.1B",
         "evidences": ["agent-exclusion", "intimate-interface"],
         "supersedes": [B + "developments/2026-03-13-smart-glasses-in-the-witness-box"]},
        {"id": "2026-03-31-institutions-as-workarounds",
         "title": "A pro-AI operation enters the midterms with $100M",
         "claim": "Innovation Council Action is entering the midterms with over $100 million to "
                  "push AI deregulation with the White House's blessing, while Rivian won a "
                  "years-long battle enabling direct electric vehicle sales in Washington state.",
         "domain": "policy", "actor": ["innovation-council", "rivian-auto", "white-house"],
         "score": "$100M",
         "evidences": ["legislating-the-shift", "regulatory-exit"],
         "supersedes": [B + "developments/2026-03-27-datacenter-moratorium-act"]},
        {"id": "2026-03-31-midjourney-traffic-falls-60-percent",
         "title": "A capability dissolves into foundation models and traffic falls 60%",
         "claim": "Midjourney's monthly traffic has fallen 60% since its 2023 peak as image "
                  "generation dissolves into foundation models as a feature, while Amazon is "
                  "building forty to fifty delivery hubs a year toward covering every US ZIP "
                  "code within four years.",
         "domain": "economics", "actor": ["midjourney", "amazon"], "score": "-60%",
         "evidences": ["software-margin-collapse", "autonomous-commerce"]},
    ],
}
