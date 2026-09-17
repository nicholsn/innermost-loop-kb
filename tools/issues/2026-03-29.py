"""Issue 086 — 2026-03-29. USAMO saturated in twelve months."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-29-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-29", "title": "Welcome to March 29, 2026", "url": URL,
        "thesis": "A benchmark goes from under 5% to 95% in a single year.",
        "body": """
# Welcome to March 29, 2026

Models scored below 5% on USAMO 2025. GPT-5.4 just scored 95% on the 2026 exam.
Twelve months, flat.

The strangest item is downstream: chess grandmasters, all training on the same
perfect engine lines, are now winning by playing deliberately suboptimal moves
their opponents haven't practiced. Shared optimal play makes divergence the only
edge left.
""",
    },
    "organizations": [
        {"id": "northwestern", "type": "Organization", "title": "Northwestern University",
         "resource": "https://www.northwestern.edu/"},
        {"id": "neko-health", "type": "Organization", "title": "Neko Health",
         "body": "Body-scan clinics founded by Spotify's Daniel Ek."},
        {"id": "cyan-robotics", "type": "Organization", "title": "Cyan Robotics",
         "body": "Embodied character companion with sub-30-ms synchronized expression."},
        {"id": "space-biostasis", "type": "Organization", "title": "Space Biostasis Coalition",
         "body": "Mobilizing $1 billion toward engineered human cryosleep for spaceflight."},
        {"id": "ibm-quantum", "type": "Organization", "title": "IBM Quantum",
         "resource": "https://www.ibm.com/quantum"},
    ],
    "developments": [
        {"id": "2026-03-29-usamo-saturated-in-a-year",
         "title": "A mathematics olympiad goes from 5% to 95% in twelve months",
         "claim": "Models scored below 5% on USAMO 2025, and GPT-5.4 scored 95% on the 2026 "
                  "exam, saturating the benchmark in twelve months.",
         "domain": "benchmarks", "actor": ["openai"], "score": "<5% → 95%",
         "evidences": ["benchmark-saturation", "automated-science"],
         "supersedes": [B + "developments/2026-03-28-epoch-retires-problems-as-unworthy"]},
        {"id": "2026-03-29-triple-release-may-price-out-humanity",
         "title": "Three frontier releases land in one month",
         "claim": "GPT-5.5, Claude 5 Mythos and DeepSeek-V4 are all expected in April, a triple "
                  "release commentators warn could make frontier intelligence too expensive for "
                  "most of humanity as massive training runs become table stakes.",
         "domain": "models", "actor": ["openai", "anthropic", "deepseek"],
         "evidences": ["spiky-frontier", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-03-27-claude-mythos-leaked"]},
        {"id": "2026-03-29-parameter-golf-42x",
         "title": "A compression competition reaches 42.7x over baseline",
         "claim": "In OpenAI's Parameter Golf competition to train the best language model "
                  "fitting in a 16MB artifact, the best claimed result is now 42.7 times better "
                  "than baseline.",
         "domain": "models", "actor": ["openai"], "score": "42.7x",
         "evidences": ["reasoning-price-deflation", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-03-24-400b-model-on-a-phone"]},
        {"id": "2026-03-29-claude-operon-for-biology",
         "title": "A desktop mode ships for biology, from phylogeny to CRISPR screens",
         "claim": "Anthropic is testing Claude Operon, a desktop mode for biology spanning "
                  "phylogenetic trees to CRISPR knockout screens.",
         "domain": "biotech", "actor": ["anthropic"],
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-03-25-a-billion-a-year-aimed-at-alzheimers"]},
        {"id": "2026-03-29-a-living-pharmacy-implant",
         "title": "A living pharmacy implant doses three drugs for a month",
         "claim": "Northwestern scientists created HOBIT, a living pharmacy implant that kept "
                  "engineered cells alive for a month inside rats while dosing three drugs at "
                  "once, while researchers demonstrated the first integrated framework for how "
                  "epigenetic regulation controls aging.",
         "domain": "biotech", "actor": ["northwestern"], "score": "3 drugs / 1 month",
         "evidences": ["hardware-grade-biology", "compiling-matter"]},
        {"id": "2026-03-29-the-dog-cancer-company",
         "title": "The man who treated his dog's cancer starts a company",
         "claim": "The man who developed a custom mRNA immunotherapy for his dog's cancer using "
                  "frontier chatbots is starting a company to end cancer in dogs, while Neko "
                  "Health plans its first US body-scan clinic in New York.",
         "domain": "biotech", "actor": ["neko-health"],
         "evidences": ["hardware-grade-biology", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-03-16-a-vaccine-for-one-dog"]},
        {"id": "2026-03-29-modular-legs-snap-into-acrobats",
         "title": "Single-joint modular legs snap together into acrobatic machines",
         "claim": "Northwestern researchers introduced autonomous modular legs, "
                  "single-degree-of-freedom links that learn complex behaviors and snap "
                  "together into acrobatic multilegged machines at the metre scale, while "
                  "China's Agibot prepares to ship 10,000 humanoids, double its milestone from "
                  "one quarter earlier.",
         "domain": "robotics", "actor": ["northwestern", "agibot", "cyan-robotics"],
         "score": "10,000 humanoids",
         "evidences": ["physical-recursion", "compiling-matter"],
         "supersedes": [B + "developments/2026-03-28-robots-learn-to-sweat"]},
        {"id": "2026-03-29-bill-to-ban-chinese-robots-in-government",
         "title": "Senators move to ban Chinese robots from government use",
         "claim": "Two US senators plan to introduce the American Security Robotics Act to ban "
                  "government use of Chinese robots, while the Tesla Model Y emerged as the "
                  "world's best-selling car for a third consecutive year.",
         "domain": "policy", "actor": ["us-congress", "tesla"],
         "evidences": ["silicon-curtain", "legislating-the-shift"]},
        {"id": "2026-03-29-microreactors-by-independence-day",
         "title": "Microreactors could reach criticality by Independence Day",
         "claim": "The Department of Energy's reactor pilot programme could see three to four "
                  "microreactors reach criticality by July 4 for America's 250th anniversary, "
                  "while South Korea mandated solar panels for public car parks of eighty or "
                  "more spaces and the first steel went up at the Michigan Stargate site.",
         "domain": "energy", "actor": ["doe", "openai"], "score": "3-4 reactors",
         "evidences": ["burning-molecules-for-tokens", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-03-28-plasma-ignition-in-a-fusion-rocket"]},
        {"id": "2026-03-29-a-nuclear-spacecraft-to-mars-by-2028",
         "title": "NASA will send a nuclear-powered spacecraft to Mars before 2029",
         "claim": "NASA announced it will send Space Reactor-1 Freedom, the first "
                  "nuclear-powered interplanetary spacecraft, to Mars before the end of 2028 "
                  "carrying a fleet of small helicopters, while a coalition launched to "
                  "mobilize $1 billion into engineering human cryosleep for space travel.",
         "domain": "space", "actor": ["nasa", "space-biostasis"], "score": "$1B",
         "evidences": ["inhabitable-worlds", "resurrection-and-time"],
         "supersedes": [B + "developments/2026-03-27-gateway-scrapped-for-a-lunar-base"]},
        {"id": "2026-03-29-fifty-qubit-material-simulation",
         "title": "A quantum processor matches neutron scattering on fifty qubits",
         "claim": "IBM and collaborators demonstrated a superconducting quantum processor "
                  "producing meaningful comparisons with neutron-scattering measurements of a "
                  "canonical physical system on up to fifty qubits, a milestone for "
                  "pre-fault-tolerant material simulation.",
         "domain": "science", "actor": ["ibm-quantum"], "score": "50 qubits",
         "evidences": ["vertical-silicon", "automated-science"],
         "supersedes": [B + "developments/2026-03-28-quantum-timeline-pulled-in-six-years"]},
        {"id": "2026-03-29-autonomous-zero-day-on-stage",
         "title": "Autonomous zero-day discovery is demonstrated live",
         "claim": "An Anthropic researcher demonstrated autonomous zero-day discovery on stage, "
                  "prompting predictions of a major US cyberoffense boost that, unlike nuclear "
                  "weapons, would be deployed daily, while a Linux kernel maintainer said "
                  "AI-driven security reporting has jumped sharply across open source in a "
                  "month.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["automated-science", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-03-08-22-firefox-vulnerabilities-in-two-weeks"]},
        {"id": "2026-03-29-grandmasters-win-by-playing-worse",
         "title": "Grandmasters start winning by playing deliberately suboptimal moves",
         "claim": "Chess grandmasters, all training on the same optimal engine lines, are now "
                  "winning by playing suboptimal moves their opponents have not practiced.",
         "domain": "society",
         "evidences": ["deskilling", "coordination-tax"],
         "body": "When everyone studies the same perfect play, divergence becomes the only edge."},
        {"id": "2026-03-29-models-moderate-where-platforms-polarize",
         "title": "Models are found to moderate views where social platforms polarize them",
         "claim": "Research finds large language models elevate expert consensus and moderate "
                  "views, in contrast to the populist polarization of social platforms, while "
                  "Claude's paid subscriptions more than doubled this year.",
         "domain": "society", "actor": ["anthropic"],
         "evidences": ["intimate-interface", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-03-27-machines-outwrite-humans"]},
    ],
}
