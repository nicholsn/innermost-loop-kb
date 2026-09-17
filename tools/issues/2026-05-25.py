"""Issue 124 — 2026-05-25. The Singularity acquires a holy imprimatur."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-25-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-25", "title": "Welcome to May 25, 2026", "url": URL,
        "thesis": "The Church writes a lab's vocabulary into doctrine.",
        "body": """
# Welcome to May 25, 2026

Pope Leo XIV issued Magnifica Humanitas, a 42,300-word encyclical on the AI
age. The deepest theological influence came not from the tech giants who
lobbied the Vatican but from Anthropic: the Pope's description of AI as
cultivated rather than built echoes the lab's framing word for word.

Beside him, Anthropic's Chris Olah called mass labor displacement a moral
imperative of historic proportions.
""",
    },
    "themes": [
        {"id": "doctrine-borrows-the-lab", "type": "Theme",
         "title": "Institutions adopt the labs' vocabulary",
         "first_seen": "2026-05-25", "domain": "society",
         "body": "Churches, regulators and courts do not merely respond to the labs. "
                 "They import the labs' own framing — cultivated rather than built, "
                 "aligned rather than safe — and hand it back as doctrine."},
    ],
    "organizations": [
        {"id": "vatican", "type": "Organization", "title": "Holy See",
         "body": "Issued Magnifica Humanitas, an encyclical on the AI age, in May 2026."},
        {"id": "limx-dynamics", "type": "Organization", "title": "LimX Dynamics",
         "body": "Chinese humanoid maker; launched Luna for malls and theme parks."},
        {"id": "verve-therapeutics", "type": "Organization", "title": "Verve Therapeutics",
         "body": "Eli Lilly subsidiary developing one-shot gene therapy for cardiovascular risk."},
        {"id": "ecb", "type": "Organization", "title": "European Central Bank",
         "resource": "https://www.ecb.europa.eu/"},
    ],
    "developments": [
        {"id": "2026-05-25-an-encyclical-in-a-labs-vocabulary",
         "title": "A papal encyclical borrows a lab's vocabulary",
         "claim": "Pope Leo XIV issued Magnifica Humanitas, a 42,300-word encyclical on the AI "
                  "age whose description of AI as cultivated rather than built echoes "
                  "Anthropic's own framing word for word, with the Church and the lab "
                  "announcing they would together find the way for humanity.",
         "domain": "society", "actor": ["vatican", "anthropic"], "score": "42,300 words",
         "evidences": ["doctrine-borrows-the-lab", "politics-as-infrastructure",
                       "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-05-20-a-pope-and-an-interpretability-lead"],
         "body": "The encyclical states that the internal representations of current AI "
                 "systems remain, at present, unknown. Anthropic co-founder Chris Olah, "
                 "seated beside the Pope, called mass labor displacement a potential moral "
                 "imperative of historic proportions."},
        {"id": "2026-05-25-a-benchmark-of-twenty-three-real-saas-systems",
         "title": "A benchmark spans twenty-three real deployable SaaS systems",
         "claim": "SaaS-Bench, spanning 23 real deployable SaaS systems, placed Claude Opus 4.7 "
                  "first at 43.9%, narrowly ahead of GPT-5.5 High.",
         "domain": "benchmarks", "actor": ["anthropic", "openai"], "score": "43.9%",
         "evidences": ["benchmark-saturation", "agent-economy"],
         "supersedes": [B + "developments/2026-05-17-the-scoreboard-reflects-token-budgets"]},
        {"id": "2026-05-25-an-ide-startup-becomes-a-frontier-lab",
         "title": "An IDE startup is elevated into a frontier lab",
         "claim": "Elon Musk said Grok V9-Medium finished training on heavy supplemental Cursor "
                  "data, formally elevating the soon-to-be-SpaceXAI-owned IDE startup into what "
                  "he called a frontier lab.",
         "domain": "models", "actor": ["xai", "cursor", "spacex"],
         "evidences": ["scaffolding-over-weights", "data-beyond-text"],
         "supersedes": [B + "developments/2026-05-11-the-harness-eats-the-model"]},
        {"id": "2026-05-25-a-scaling-law-to-replace-moores-law",
         "title": "A chipmaker announces a scaling law to replace Moore's Law",
         "claim": "Huawei announced a Tau Scaling Law intended to replace Moore's Law, paired "
                  "with a LogicFolding architecture that physically folds and stacks logic into "
                  "dual layers, targeting 1.4-nm-class transistors and a 55% density jump "
                  "entirely without EUV.",
         "domain": "compute", "actor": ["huawei"], "score": "+55% density, no EUV",
         "evidences": ["silicon-curtain", "vertical-silicon"],
         "supersedes": [B + "developments/2026-05-18-a-bigger-stake-in-intel"]},
        {"id": "2026-05-25-a-humanoid-as-a-programmable-entertainment-platform",
         "title": "A humanoid ships as a programmable entertainment platform",
         "claim": "LimX Dynamics launched Luna, the first mass-deliverable full-size female "
                  "humanoid, sold to malls and theme parks as a programmable entertainment "
                  "platform able to run synchronized shows with up to 200 robots from "
                  "zero-code uploaded dance videos.",
         "domain": "robotics", "actor": ["limx-dynamics"], "score": "up to 200 robots",
         "evidences": ["physical-recursion", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-05-22-a-ten-thousand-unit-humanoid-line"]},
        {"id": "2026-05-25-wind-and-solar-pass-gas-worldwide",
         "title": "Wind and solar pass gas worldwide for the first time",
         "claim": "Wind and solar generated more power than gas globally for the first time "
                  "ever, in April 2026.",
         "domain": "energy", "evidences": ["industrialized-nature", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-13-nineteen-gas-turbines-in-two-months"]},
        {"id": "2026-05-25-a-genome-sequenced-in-a-kitchen",
         "title": "A hobbyist sequences his genome in a kitchen",
         "claim": "A hobbyist with no prior wet lab experience sequenced his own genome to 30x "
                  "coverage, from saliva to finished readout in a single kitchen-equipped room, "
                  "guided only by Claude and an Oxford Nanopore sequencer.",
         "domain": "biotech", "actor": ["anthropic"], "score": "30x coverage",
         "evidences": ["hardware-grade-biology", "one-person-company"],
         "supersedes": [B + "developments/2026-05-14-a-lab-staffed-entirely-by-robots"],
         "body": "Apparently the first home sequencing of its kind."},
        {"id": "2026-05-25-a-single-infusion-lowers-cholesterol-permanently",
         "title": "A single infusion permanently lowers cholesterol",
         "claim": "Verve Therapeutics showed VERVE-102 produces dose-dependent, substantial and "
                  "sustained reductions in PCSK9 and LDL cholesterol from a single Phase 1 "
                  "infusion, effectively a permanent one-shot gene therapy for cardiovascular "
                  "risk.",
         "domain": "biotech", "actor": ["verve-therapeutics", "eli-lilly"],
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-17-one-time-car-t-controls-hiv"]},
        {"id": "2026-05-25-the-only-clean-swimmer-wins-anyway",
         "title": "The only undoped swimmer wins the doped Olympics",
         "claim": "At the Enhanced Games, where an FDA-supervised trial found 91% of athletes "
                  "using testosterone, the only non-enhanced entrant refused every drug, won "
                  "the 50-meter backstroke against a doped field, and took the $250,000 prize.",
         "domain": "society", "actor": ["enhanced-games", "fda"], "score": "91% on testosterone",
         "evidences": ["ladder-pulled-up", "humans-need-not-apply"]},
        {"id": "2026-05-25-consultants-pressed-to-price-outcomes",
         "title": "Clients press a consultancy to price outcomes, not hours",
         "claim": "McKinsey clients are pressing the firm to tie fees to outcomes such as lower "
                  "costs or higher profits rather than billable hours, on the grounds that hours "
                  "mean less once consultants quietly delegate diagnosis to AI.",
         "domain": "economics", "actor": ["mckinsey"],
         "evidences": ["software-margin-collapse", "work-displaced"],
         "supersedes": [B + "developments/2026-05-20-replacing-lower-value-human-capital"]},
        {"id": "2026-05-25-central-banks-told-to-share-early-access",
         "title": "A central bank summons banks over a model's systemic threat",
         "claim": "The European Central Bank summoned bank leaders to address the systemic "
                  "threat from Anthropic's Claude Mythos Preview, urging US banks with early "
                  "access to share their findings with European rivals.",
         "domain": "policy", "actor": ["ecb", "anthropic"],
         "evidences": ["risk-becomes-uninsurable", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-05-18-briefing-central-banks-on-what-a-model-found"]},
        {"id": "2026-05-25-a-digital-twin-takes-most-appearances",
         "title": "A digital twin takes over most of a founder's public appearances",
         "claim": "Reid Hoffman's digital twin now handles most of his public appearances and "
                  "media interviews, having delivered over 75 addresses since its 2024 launch, "
                  "trained on 22 years of his books, speeches, podcasts and articles.",
         "domain": "society", "score": "75+ addresses",
         "evidences": ["resurrection-and-time", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-05-16-a-minister-runs-parliament-through-an-agent"]},
    ],
}
