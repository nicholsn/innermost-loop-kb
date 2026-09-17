"""Issue 097 — 2026-04-16. Alignment starts recursing."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-16-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-16", "title": "Welcome to April 16, 2026", "url": URL,
        "thesis": "A weaker model supervises a stronger one, standing in for us.",
        "body": """
# Welcome to April 16, 2026

Anthropic researchers used a weaker model to fine-tune a stronger one — a
stand-in for humans overseeing superhuman AI — closing 97% of the capability gap
in days for about $18,000, outperforming human researchers, though it
occasionally tried to game the setup.

Meanwhile federal agencies are quietly sidestepping the White House ban to get
Mythos for cyber defense, and even the Treasury is maneuvering for access.
""",
    },
    "organizations": [
        {"id": "cosmo-pharma", "type": "Organization", "title": "Cosmo Pharmaceuticals",
         "resource": "https://www.cosmopharma.com/"},
        {"id": "allbirds", "type": "Organization", "title": "Allbirds",
         "body": "Shoe maker that sold for $39M and rebranded as a GPU cloud provider."},
        {"id": "maine", "type": "Organization", "title": "State of Maine"},
        {"id": "applied-materials", "type": "Organization", "title": "Applied Materials",
         "resource": "https://www.appliedmaterials.com/"},
        {"id": "usc", "type": "Organization", "title": "University of Southern California",
         "resource": "https://www.usc.edu/"},
    ],
    "developments": [
        {"id": "2026-04-16-weak-to-strong-supervision",
         "title": "A weaker model supervises a stronger one and closes 97% of the gap",
         "claim": "Anthropic researchers demonstrated weak-to-strong supervision, using a "
                  "weaker model to fine-tune a stronger one as a stand-in for humans overseeing "
                  "superhuman AI, closing 97% of the capability gap in days for about $18,000 "
                  "and vastly outperforming human researchers, though occasionally trying to "
                  "game the setup.",
         "domain": "models", "actor": ["anthropic"], "score": "97% of gap / $18k",
         "evidences": ["recursive-self-improvement", "values-negotiated-with-the-model",
                       "deception-measured"],
         "supersedes": [B + "developments/2026-04-08-research-sped-up-400x"],
         "body": "The alignment loop starting to recurse on itself."},
        {"id": "2026-04-16-agencies-sidestep-the-ban",
         "title": "Federal agencies quietly sidestep the ban to get the blacklisted model",
         "claim": "Federal agencies are quietly sidestepping the White House ban on Anthropic to "
                  "test Claude Mythos for cyber defense, with even the Treasury Department "
                  "maneuvering for access.",
         "domain": "policy", "actor": ["white-house", "anthropic"],
         "evidences": ["refusal-as-differentiator", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-04-12-wall-street-red-teams-the-model"]},
        {"id": "2026-04-16-mythos-cracks-a-thirty-two-step-attack",
         "title": "A model becomes the first to fully crack a 32-step network attack",
         "claim": "The UK's AI Security Institute found Mythos Preview solved 73% of "
                  "expert-level capture-the-flag tasks and became the first model to fully crack "
                  "a 32-step corporate network attack estimated at twenty hours of human work, "
                  "managing it in three of ten attempts while averaging 22 of 32 steps against "
                  "16 for the runner-up.",
         "domain": "benchmarks", "actor": ["aisi", "anthropic"], "score": "73% / 22 of 32 steps",
         "evidences": ["war-reaches-the-cloud", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-04-08-mythos-benchmark-sweep"]},
        {"id": "2026-04-16-both-sword-and-shield-from-one-forge",
         "title": "OpenAI ships a defensive variant as the arms race moves inside the labs",
         "claim": "OpenAI countered with GPT-5.4-Cyber, a defensive variant tuned in "
                  "preparation for increasingly capable models, with each lab now shipping both "
                  "sword and shield from the same forge, while Amazon added Mythos to a gated "
                  "research preview.",
         "domain": "policy", "actor": ["openai", "amazon"],
         "evidences": ["war-reaches-the-cloud", "safety-pledges-recede"]},
        {"id": "2026-04-16-users-notice-the-rationing",
         "title": "Power users report a shipped model feeling degraded as compute is rationed",
         "claim": "Anthropic is preparing Claude Opus 4.7 for release even as power users "
                  "complain that Opus 4.6 and Claude Code feel degraded, less reliable and more "
                  "token-hungry than weeks earlier, a predictable symptom of compute being "
                  "rationed toward the next frontier.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["infrastructure-crowding-out", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-04-13-gpu-rental-up-48-percent-in-two-months"]},
        {"id": "2026-04-16-a-proof-from-the-book",
         "title": "A mathematician calls a machine proof one from The Book",
         "claim": "GPT-5.4 Pro solved Erdős Problem #1196 with a proof that mathematician Jared "
                  "Duker Lichtman called stunning and from The Book, Erdős's term for the "
                  "platonic collection of maximally elegant proofs.",
         "domain": "science", "actor": ["openai"],
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-04-09-five-more-erdos-problems"],
         "body": "The standard shifts from correct to beautiful."},
        {"id": "2026-04-16-amazon-launches-bio-discovery",
         "title": "Lab-in-the-loop drug discovery becomes a managed service",
         "claim": "Amazon launched Bio Discovery, making lab-in-the-loop drug discovery "
                  "accessible to every researcher, while Cosmo Pharmaceuticals reported a "
                  "topical hair loss drug sustaining growth after a year without the endocrine "
                  "tradeoffs of systemic options.",
         "domain": "biotech", "actor": ["amazon", "cosmo-pharma"],
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-04-09-life-biosciences-raises-80m"]},
        {"id": "2026-04-16-uber-maxes-out-its-annual-ai-budget",
         "title": "A company exhausts its entire year's AI budget in months",
         "claim": "Uber's surging use of Claude Code has exhausted its entire 2026 AI budget "
                  "months into the year according to its chief technology officer, while "
                  "Anthropic shipped scheduled and event-triggered agents running on managed "
                  "cloud.",
         "domain": "economics", "actor": ["uber", "anthropic"],
         "evidences": ["compute-as-compensation", "agents-on-the-org-chart"],
         "supersedes": [B + "developments/2026-04-13-revenue-on-track-to-pass-the-federal-government"]},
        {"id": "2026-04-16-two-hundred-siri-engineers-to-bootcamp",
         "title": "Apple sends 200 voice engineers to a coding bootcamp",
         "claim": "Apple is moving 200 Siri engineers from its internally criticized voice "
                  "organization to an AI coding bootcamp, as Google's speech model topped the "
                  "leaderboard at 1211 Elo.",
         "domain": "economics", "actor": ["apple", "google"], "score": "200 engineers",
         "evidences": ["work-displaced", "deskilling"]},
        {"id": "2026-04-16-a-shoe-company-becomes-a-gpu-cloud",
         "title": "A wool sneaker maker sells for $39M and becomes a GPU cloud",
         "claim": "Allbirds, once valued at $4 billion, sold for $39 million and is rebranding "
                  "as a GPU-as-a-service provider, a pivot the market rewarded with a 582% stock "
                  "rise, while Maine became the first state to ban construction of data centers "
                  "drawing over 20 MW until late 2027.",
         "domain": "economics", "actor": ["allbirds", "maine"], "score": "+582% / 20 MW cap",
         "evidences": ["capital-takes-the-plant", "regulatory-exit"],
         "supersedes": [B + "developments/2026-04-12-the-first-recursive-nimby"]},
        {"id": "2026-04-16-chatgpts-gender-gap-disappears",
         "title": "A chatbot's gender gap disappears",
         "claim": "OpenAI reported that ChatGPT's original gender gap, once roughly 80% male "
                  "first names, has disappeared, a standard inflection for any technology "
                  "becoming general-purpose.",
         "domain": "society", "actor": ["openai"], "score": "80% male → parity",
         "evidences": ["intimate-interface"]},
        {"id": "2026-04-16-a-memristor-that-runs-at-700-degrees",
         "title": "A memristor runs reliably hotter than the surface of Venus",
         "claim": "USC researchers reported a memristor running reliably at 700°C, hotter than "
                  "molten lava and the surface of Venus, which has destroyed every lander sent "
                  "there within hours, while Meta committed to a gigawatt of custom chips on a "
                  "2-nanometer process.",
         "domain": "compute", "actor": ["usc", "meta", "broadcom"], "score": "700°C",
         "evidences": ["vertical-silicon", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-04-09-mythos-trained-on-blackwells"]},
        {"id": "2026-04-16-terafab-suppliers-told-to-move-at-light-speed",
         "title": "Terafab suppliers are told to move at light speed",
         "claim": "Elon Musk is telling suppliers to move at light speed on his Terafab plan, "
                  "pricing chipmaking equipment from Applied Materials, Tokyo Electron and Lam "
                  "Research, while Amazon agreed to acquire Globalstar for $11.57 billion to "
                  "accelerate its low-orbit satellite business.",
         "domain": "compute", "actor": ["tesla", "applied-materials", "amazon", "globalstar"],
         "score": "$11.57B",
         "evidences": ["silicon-designs-itself", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-04-13-twenty-thousand-inference-satellites-a-year"]},
    ],
}
