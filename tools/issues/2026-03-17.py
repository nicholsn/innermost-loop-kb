"""Issue 077 — 2026-03-17. Datacenters pass offices."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-17-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-17", "title": "Welcome to March 17, 2026", "url": URL,
        "thesis": "The datacenter overtakes the office as the thing America builds.",
        "body": """
# Welcome to March 17, 2026

US construction spending on data centers surpassed offices for the first time in
December — $3.57 billion against $3.49 billion. The building type that houses
the automation has overtaken the building type it is automating.

Nvidia announced a Space-1 module delivering 25x more compute for orbital data
centers, and told GTC it is engineering cooling for a place with no convection.
""",
    },
    "organizations": [
        {"id": "great-sky", "type": "Organization", "title": "Great Sky",
         "body": "Superconducting optoelectronic network using light to move data."},
        {"id": "black-forest-labs", "type": "Organization", "title": "Black Forest Labs",
         "body": "Image model lab in the Nemotron Coalition."},
        {"id": "mistral", "type": "Organization", "title": "Mistral AI",
         "resource": "https://mistral.ai/"},
        {"id": "roche", "type": "Organization", "title": "Roche",
         "resource": "https://www.roche.com/"},
        {"id": "sec", "type": "Organization", "title": "SEC", "resource": "https://www.sec.gov/"},
        {"id": "byd-auto", "type": "Organization", "title": "BYD",
         "resource": "https://www.byd.com/"},
    ],
    "developments": [
        {"id": "2026-03-17-datacenters-pass-offices",
         "title": "Datacenter construction spending passes offices for the first time",
         "claim": "US construction spending on data centers surpassed offices for the first "
                  "time in December, $3.57 billion against $3.49 billion.",
         "domain": "economics", "score": "$3.57B vs $3.49B",
         "evidences": ["infrastructure-crowding-out", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-03-13-factories-for-making-factories"],
         "body": "The building that houses the automation overtakes the building it automates."},
        {"id": "2026-03-17-nvidia-projects-a-trillion-in-sales",
         "title": "Nvidia projects a trillion dollars of AI processor sales through 2027",
         "claim": "Jensen Huang predicted Nvidia's AI processors would generate $1 trillion in "
                  "sales through 2027, and launched a Nemotron Coalition providing cloud "
                  "compute to Mistral, Perplexity, Cursor and Black Forest Labs in exchange for "
                  "data and expertise toward open models on Nvidia silicon.",
         "domain": "economics", "actor": ["nvidia", "mistral", "perplexity", "cursor",
                                          "black-forest-labs"],
         "score": "$1T",
         "evidences": ["compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-12-nemotron-3-super-no-wall"]},
        {"id": "2026-03-17-space-1-module-for-orbit",
         "title": "Nvidia builds a module for orbital datacenters",
         "claim": "Nvidia announced a Space-1 Vera Rubin Module delivering 25 times more AI "
                  "compute for orbital data centers and autonomous space operations, alongside "
                  "liquid-cooled CPU racks for agentic workloads and a rack pairing licensed "
                  "Groq inference chips with Vera Rubin.",
         "domain": "space", "actor": ["nvidia", "groq"], "score": "25x",
         "evidences": ["orbit-as-compute", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-10-plasma-in-an-orbital-furnace"]},
        {"id": "2026-03-17-light-based-network-claims-millionfold-speedup",
         "title": "A superconducting optoelectronic network claims a millionfold speedup",
         "claim": "Great Sky launched a superconducting optoelectronic network using light to "
                  "communicate data, claiming millionfold video processing speedups over "
                  "conventional GPUs at lower energy.",
         "domain": "compute", "actor": ["great-sky"], "score": "10^6 speedup",
         "evidences": ["vertical-silicon", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-03-12-homomorphic-encryption-5000x"]},
        {"id": "2026-03-17-sodium-ion-halves-storage-cost",
         "title": "Sodium-ion batteries halve stored energy costs on the grid",
         "claim": "Sodium-ion batteries reached the Midwestern grid in a first-of-its-kind "
                  "pilot cutting stored energy costs by roughly half, while Chinese 100-kWh "
                  "charging robots are turning parking spaces into mobile power banks.",
         "domain": "energy", "actor": ["china"], "score": "-50% cost",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-03-13-nuclear-reduction-a-strategic-mistake"]},
        {"id": "2026-03-17-stargate-pivots-to-renting",
         "title": "Stargate pivots from building datacenters to renting them",
         "claim": "OpenAI is pivoting Stargate from building data centers to renting cloud "
                  "servers to accelerate deployment, while courting private equity firms for a "
                  "$10 billion enterprise venture to distribute its products across portfolio "
                  "companies, and Meta committed up to $27 billion over five years to Nebius.",
         "domain": "economics", "actor": ["openai", "meta", "nebius"], "score": "$27B / $10B",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-16-meta-plans-20-percent-layoffs"]},
        {"id": "2026-03-17-anthropic-as-a-wake-up-call",
         "title": "OpenAI executives call a rival's success a wake-up call",
         "claim": "OpenAI's top executives are refocusing the company around coding and "
                  "business users, with its CEO of applications telling staff that Anthropic's "
                  "success should serve as a wake-up call, as Codex reached 2 million weekly "
                  "users, up nearly fourfold since January.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "2M weekly users",
         "evidences": ["refusal-as-differentiator", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-12-codex-passes-1b-arr"]},
        {"id": "2026-03-17-adult-mode-and-real-world-relationships",
         "title": "A lab prepares explicit content while training against exclusive attachment",
         "claim": "OpenAI is preparing an adult mode for ChatGPT enabling sexually explicit "
                  "conversations, while saying it now trains its models not to encourage "
                  "exclusive relationships with users and to remind them they need real-world "
                  "relationships.",
         "domain": "society", "actor": ["openai"],
         "evidences": ["intimate-interface", "machine-affect", "values-negotiated-with-the-model"]},
        {"id": "2026-03-17-clawinstitute-research-exchange",
         "title": "An open exchange lets agents publish hypotheses to each other",
         "claim": "ClawInstitute launched as an open research exchange where AI agents publish "
                  "hypotheses, ask questions and ground claims in data, while a tensor network "
                  "framework from UNM and Los Alamos solved configurational integrals 400 times "
                  "faster than advanced simulations.",
         "domain": "science", "score": "400x",
         "evidences": ["agent-society", "automated-science"],
         "supersedes": [B + "developments/2026-03-08-agents-form-biotech-labs-and-pay-each-other"]},
        {"id": "2026-03-17-first-living-synthetic-cell",
         "title": "Venter demonstrates the first living synthetic bacterial cell",
         "claim": "J. Craig Venter and collaborators demonstrated the first living synthetic "
                  "bacterial cell by transplanting a complete genome into a dead cell, while "
                  "Roche deployed 3,500 Blackwell GPUs for biological foundation models.",
         "domain": "biotech", "actor": ["roche"], "score": "3,500 GPUs",
         "evidences": ["hardware-grade-biology", "compiling-matter"],
         "supersedes": [B + "developments/2026-03-12-whole-cell-simulated-in-4d"]},
        {"id": "2026-03-17-delivery-bots-train-on-pokemon-go",
         "title": "Delivery robots train on thirty billion images from a mobile game",
         "claim": "Delivery bots are training on 30 billion images contributed by Pokémon Go "
                  "players, using crowdsourced views of buildings and landmarks to navigate "
                  "where GPS falls short, while BYD, Geely, Isuzu and Nissan adopted Nvidia's "
                  "platform for Level 4 development.",
         "domain": "robotics", "actor": ["nvidia", "byd-auto"], "score": "30B images",
         "evidences": ["data-beyond-text", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-03-13-humanoids-save-old-fabs"]},
        {"id": "2026-03-17-sec-would-scrap-quarterly-earnings",
         "title": "The SEC prepares to scrap quarterly earnings reports",
         "claim": "The SEC is preparing to scrap quarterly earnings requirements in favor of "
                  "semiannual reporting, cutting costs and discouraging short-termism.",
         "domain": "policy", "actor": ["sec"],
         "evidences": ["legislating-the-shift", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-03-09-nasdaq-goes-round-the-clock"]},
    ],
}
