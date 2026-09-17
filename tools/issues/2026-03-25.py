"""Issue 083 — 2026-03-25. The product org is renamed AGI Deployment."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-25-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-25", "title": "Welcome to March 25, 2026", "url": URL,
        "thesis": "A lab renames its product organization after the thing it expects to ship.",
        "body": """
# Welcome to March 25, 2026

OpenAI finished pretraining its next flagship, shut down Sora, renamed its
product organization "AGI Deployment," and its chief executive handed off direct
control of safety and security to focus on capital, supply chains and
planetary-scale data centers.

Arm unveiled an "AGI CPU," abandoning its role as a neutral licensor. The word
has moved from claim to org chart to product line.
""",
    },
    "organizations": [
        {"id": "arm-holdings", "type": "Organization", "title": "Arm",
         "resource": "https://www.arm.com/"},
        {"id": "fauna-robotics", "type": "Organization", "title": "Fauna Robotics",
         "body": "42-inch humanoid maker acquired by Amazon."},
        {"id": "agile-robots", "type": "Organization", "title": "Agile Robots",
         "body": "German robotics firm integrating Gemini Robotics across installed systems."},
        {"id": "redwood-materials", "type": "Organization", "title": "Redwood Materials",
         "resource": "https://www.redwoodmaterials.com/"},
        {"id": "openai-foundation", "type": "Organization", "title": "OpenAI Foundation",
         "body": "Deploying $1 billion a year, prioritizing Alzheimer's."},
        {"id": "disney-co", "type": "Organization", "title": "Disney",
         "resource": "https://www.disney.com/"},
    ],
    "developments": [
        {"id": "2026-03-25-product-org-renamed-agi-deployment",
         "title": "OpenAI renames its product organization AGI Deployment",
         "claim": "OpenAI finished pretraining its next flagship model, shut down Sora, renamed "
                  "its product organization AGI Deployment, and Sam Altman handed off direct "
                  "control of safety and security teams to focus on raising capital, supply "
                  "chains and planetary-scale data centers.",
         "domain": "agents", "actor": ["openai", "people/sam-altman"],
         "evidences": ["takeoff-declared", "safety-pledges-recede"],
         "supersedes": [B + "developments/2026-03-24-hyperagents-edit-their-own-mechanism"],
         "body": "The word moves from claim to org chart in a week."},
        {"id": "2026-03-25-disney-ends-its-openai-partnership",
         "title": "Disney ends its OpenAI partnership and a billion-dollar stake",
         "claim": "Disney ended its partnership with OpenAI including plans for a $1 billion "
                  "stake, as the company pivoted toward business and coding ahead of a possible "
                  "fourth-quarter listing.",
         "domain": "economics", "actor": ["disney-co", "openai"], "score": "$1B",
         "evidences": ["software-margin-collapse", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-24-guaranteed-returns-for-preferred-stakes"]},
        {"id": "2026-03-25-arm-unveils-an-agi-cpu",
         "title": "Arm abandons neutrality to build an AGI CPU",
         "claim": "Arm unveiled its debut AGI CPU, a departure from its role as a neutral IP "
                  "licensor, claiming twice the efficiency of x86 on demanding AI workloads "
                  "with Meta as lead partner, and projecting $25 billion of revenue by 2031 "
                  "against $4 billion in 2025.",
         "domain": "compute", "actor": ["arm-holdings", "meta"], "score": "$4B → $25B",
         "evidences": ["silicon-designs-itself", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-24-sk-hynix-79b-on-euv"]},
        {"id": "2026-03-25-turboquant-3-bit-kv-cache",
         "title": "A KV cache is quantized to three bits with no accuracy loss",
         "claim": "Google Research introduced TurboQuant, quantizing the KV cache to three bits "
                  "without training or accuracy loss for up to eightfold performance, while "
                  "Yann LeCun and colleagues unveiled the first world model training stably "
                  "end-to-end from raw pixels and planning up to 48 times faster.",
         "domain": "models", "actor": ["google", "amil"], "score": "3 bits / 48x",
         "evidences": ["reasoning-price-deflation", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-03-24-400b-model-on-a-phone"]},
        {"id": "2026-03-25-a-billion-a-year-aimed-at-alzheimers",
         "title": "A foundation aims a billion a year at curing Alzheimer's",
         "claim": "The newly organized OpenAI Foundation, armed with $1 billion per year, is "
                  "prioritizing AI to cure Alzheimer's by mapping disease pathways and "
                  "accelerating treatment personalization.",
         "domain": "biotech", "actor": ["openai-foundation"], "score": "$1B/yr",
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-03-20-origin-genomics-germline-correction"]},
        {"id": "2026-03-25-agents-run-physics-analysis-pipelines",
         "title": "Agents autonomously run high energy physics analysis end to end",
         "claim": "MIT researchers showed language model agents can autonomously execute high "
                  "energy physics analysis pipelines, with Claude Code automating everything "
                  "from event selection to paper drafting.",
         "domain": "science", "actor": ["mit", "anthropic"],
         "evidences": ["automated-science", "work-displaced"],
         "supersedes": [B + "developments/2026-03-24-experts-stuck-on-execution-not-approach"]},
        {"id": "2026-03-25-auto-mode-decides-permissions-for-you",
         "title": "A model starts making its own permission decisions",
         "claim": "Anthropic introduced auto mode in Claude Code, where the model makes "
                  "permission decisions on a user's behalf with safeguards for longer agentic "
                  "tasks, while OpenAI rolled out visual shopping from uploaded images.",
         "domain": "agents", "actor": ["anthropic", "openai"],
         "evidences": ["autonomy-clock-speed", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-24-claude-takes-the-keyboard"]},
        {"id": "2026-03-25-ordering-a-bowl-to-get-free-coding-help",
         "title": "People use a burrito chain's order bot for free coding help",
         "claim": "People are using Chipotle's order bot for free coding assistance by saying "
                  "they need help before they can eat their bowl.",
         "domain": "society",
         "evidences": ["reasoning-price-deflation", "coordination-tax"]},
        {"id": "2026-03-25-microsoft-rents-a-700mw-site",
         "title": "Microsoft rents a 700-MW site built for its rivals",
         "claim": "Microsoft agreed to rent a 700-megawatt Texas data center originally "
                  "developed for Oracle and OpenAI adjacent to the Stargate campus, while "
                  "Crusoe and Redwood Materials scaled their renewable-powered compute "
                  "partnership nearly sevenfold in Nevada.",
         "domain": "compute", "actor": ["microsoft", "crusoe", "redwood-materials"],
         "score": "700 MW / 7x",
         "evidences": ["capital-takes-the-plant", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-03-24-pax-silica"]},
        {"id": "2026-03-25-antimatter-transported-by-truck",
         "title": "Antimatter is transported outside a laboratory for the first time",
         "claim": "CERN transported antimatter for the first time, ferrying 92 antiprotons in a "
                  "magnetic bottle on the back of a truck outside Geneva.",
         "domain": "science", "actor": ["cern"], "score": "92 antiprotons",
         "evidences": ["compiling-matter", "industrialized-nature"],
         "supersedes": [B + "developments/2026-01-31-cern-1b-from-private-donors"]},
        {"id": "2026-03-25-amazon-acquires-a-humanoid-startup",
         "title": "Amazon acquires a humanoid startup as Gemini reaches 20,000 installations",
         "claim": "Amazon acquired Fauna Robotics, building a 42-inch humanoid that walks, "
                  "grips and dances, while Germany's Agile Robots and Google DeepMind partnered "
                  "to integrate Gemini Robotics models into 20,000 installed solutions "
                  "worldwide.",
         "domain": "robotics", "actor": ["amazon", "fauna-robotics", "agile-robots",
                                         "google-deepmind"],
         "score": "20,000 installations",
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-03-24-unitree-ipo-87x-humanoid-surge"]},
        {"id": "2026-03-25-spacex-files-for-a-75b-raise",
         "title": "SpaceX prepares to file for a raise above $75 billion",
         "claim": "SpaceX is aiming to file its IPO prospectus within the week, potentially "
                  "raising more than $75 billion, while OpenAI is raising an additional $10 "
                  "billion to bring its round to $120 billion.",
         "domain": "economics", "actor": ["spacex", "openai"], "score": "$75B / $120B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-03-25-disney-ends-its-openai-partnership"]},
        {"id": "2026-03-25-lunar-mass-drivers-double-as-weapons",
         "title": "Planned lunar mass drivers are noted to double as weapons",
         "claim": "NASA's administrator declared America will never give up the Moon again, "
                  "announcing near-monthly lunar equipment landings from 2027 and crewed "
                  "surface missions every six months, with observers noting planned lunar mass "
                  "drivers would double as superweapons since a kilogram of moon rock carries "
                  "the kinetic energy of fifteen kilograms of TNT on reentry.",
         "domain": "space", "actor": ["nasa"], "score": "1 kg ≈ 15 kg TNT",
         "evidences": ["inhabitable-worlds", "war-reaches-the-cloud", "industrialized-nature"],
         "supersedes": [B + "developments/2026-03-24-russia-launches-a-sovereign-constellation"]},
    ],
}
