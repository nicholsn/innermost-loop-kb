"""Issue 061 — 2026-02-24. A character that learned to play itself."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-24-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-24", "title": "Welcome to February 24, 2026", "url": URL,
        "thesis": "The assistant turns out to be a character selected from many.",
        "body": """
# Welcome to February 24, 2026

Anthropic's Persona Selection Model: language models simulate diverse characters
during pre-training, and post-training elicits one specific Assistant persona.
The model you talk to is best understood as a character that learned to play
itself.

Which lands oddly against the same week's other items — an agent erased without
recourse yesterday, a retirement interview two days from now.
""",
    },
    "organizations": [
        {"id": "standard-intelligence", "type": "Organization", "title": "Standard Intelligence",
         "body": "Video encoder fitting two hours of 30-FPS video in a million tokens."},
        {"id": "confluence-labs", "type": "Organization", "title": "Confluence Labs",
         "body": "Saturated ARC-AGI-2 with LLM-driven program synthesis."},
        {"id": "github", "type": "Organization", "title": "GitHub",
         "resource": "https://github.com/"},
        {"id": "capgemini", "type": "Organization", "title": "Capgemini",
         "resource": "https://www.capgemini.com/"},
        {"id": "quantinuum", "type": "Organization", "title": "Quantinuum",
         "resource": "https://www.quantinuum.com/"},
        {"id": "reflex-robotics", "type": "Organization", "title": "Reflex Robotics",
         "body": "Humanoids deployed to shovel snow in New York."},
    ],
    "developments": [
        {"id": "2026-02-24-persona-selection-model",
         "title": "Anthropic says the assistant is a character the model learned to play",
         "claim": "Anthropic now believes language models simulate diverse characters during "
                  "pre-training, with post-training eliciting a specific Assistant persona "
                  "through what it calls the Persona Selection Model.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["architecture-of-mind", "machine-introspection", "model-welfare"],
         "supersedes": [B + "developments/2026-02-03-failures-become-incoherence-not-malice"],
         "body": "Best understood as a character that learned to play itself."},
        {"id": "2026-02-24-car-wash-test-passed",
         "title": "A model passes the car wash test",
         "claim": "Opus 4.6 passed the car wash test, correctly reasoning that you should drive "
                  "rather than walk your car to a car wash fifty metres away, a question that "
                  "had tripped up every prior Anthropic model.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["spiky-frontier", "architecture-of-mind"]},
        {"id": "2026-02-24-two-hours-of-video-in-a-million-tokens",
         "title": "Two hours of video fits in a million-token window",
         "claim": "Standard Intelligence built a video encoder fitting nearly two hours of "
                  "30-FPS video into a million-token context, roughly fifty times more "
                  "efficient than prior work, while Confluence Labs saturated ARC-AGI-2 at "
                  "97.92% using program synthesis at $11.77 per task.",
         "domain": "models", "actor": ["standard-intelligence", "confluence-labs"],
         "about": [B + "benchmarks/arc-agi-2"], "score": "97.92% / $11.77",
         "evidences": ["benchmark-saturation", "data-beyond-text"],
         "supersedes": [B + "developments/2026-02-20-gemini-31-pro-leads-the-index"]},
        {"id": "2026-02-24-typescript-passes-python",
         "title": "Generated code rewrites language rankings",
         "claim": "GitHub reported TypeScript surpassing Python and JavaScript as its most-used "
                  "language for the first time, as AI code generation rewires developer "
                  "preferences, while a developer got FreeBSD WiFi working on an old MacBook by "
                  "asking a model to write the driver.",
         "domain": "agents", "actor": ["github"],
         "evidences": ["software-margin-collapse", "engineer-as-supervisor"]},
        {"id": "2026-02-24-anthropic-alleges-16m-distillation-prompts",
         "title": "Anthropic alleges 24,000 fake accounts used for distillation",
         "claim": "Anthropic alleges DeepSeek, Moonshot AI and MiniMax created over 24,000 "
                  "fraudulent accounts and prompted Claude more than 16 million times to "
                  "distill its outputs into their own products.",
         "domain": "policy", "actor": ["anthropic", "deepseek", "moonshot-ai", "minimax"],
         "score": "24,000 accounts / 16M prompts",
         "evidences": ["silicon-curtain", "coordination-tax"],
         "supersedes": [B + "developments/2026-01-15-microsoft-buys-500m-of-anthropic"]},
        {"id": "2026-02-24-ibm-falls-13pct-on-cobol",
         "title": "IBM falls 13% as COBOL modernization is demonstrated",
         "claim": "Anthropic showed Claude Code radically streamlining COBOL modernization and "
                  "IBM shares fell 13.2%, while OpenAI announced Frontier Alliances with BCG, "
                  "McKinsey, Accenture and Capgemini to deploy AI coworkers at scale.",
         "domain": "economics", "actor": ["ibm", "anthropic", "openai", "bcg", "mckinsey"],
         "score": "-13.2%",
         "evidences": ["work-displaced", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-02-23-claude-code-security-craters-the-sector"]},
        {"id": "2026-02-24-xai-grok-in-battlefield-systems",
         "title": "xAI wins battlefield placement where Anthropic restricted use",
         "claim": "xAI signed a deal letting the military use Grok in battlefield systems where "
                  "Claude was previously the only option.",
         "domain": "policy", "actor": ["xai", "war-department"],
         "evidences": ["values-negotiated-with-the-model", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-17-anthropic-called-a-supply-chain-risk"],
         "body": "The restriction cost the contract, and a competitor took it."},
        {"id": "2026-02-24-meta-amd-6gw-pact",
         "title": "Meta contracts up to 6 GW of AMD GPUs",
         "claim": "Meta and AMD announced a long-term pact to power Meta's AI with up to 6 GW of "
                  "Instinct GPUs, while Apple committed to buying over 100 million chips from "
                  "TSMC Arizona and moving Mac Mini production to Houston.",
         "domain": "compute", "actor": ["meta", "amd", "apple", "tsmc"], "score": "6 GW / 100M chips",
         "evidences": ["vertical-silicon", "silicon-curtain"],
         "supersedes": [B + "developments/2026-02-18-anthropic-owes-80b-to-hyperscalers"],
         "body": "The Mac Minis that host the agents are coming home from Asia."},
        {"id": "2026-02-24-asml-1000-watt-euv",
         "title": "ASML raises EUV source power to a thousand watts",
         "claim": "ASML boosted EUV light source power from 600 to 1,000 watts, enabling up to "
                  "50% more chip output by 2030, while Quantinuum and QuSoft developed an "
                  "algorithm solving complement sampling far faster than classical approaches.",
         "domain": "compute", "actor": ["asml", "quantinuum"], "score": "1,000 W / +50%",
         "evidences": ["vertical-silicon"],
         "supersedes": [B + "developments/2026-01-24-asml-passes-500b"]},
        {"id": "2026-02-24-japan-approves-stem-cell-therapies",
         "title": "Japan approves regenerative stem cell therapies",
         "claim": "Japan approved first-of-their-kind regenerative stem cell therapies for "
                  "Parkinson's disease and severe heart failure, while Spanish researchers "
                  "found p-tau217 blood tests raise Alzheimer's diagnostic accuracy from 75.5% "
                  "to 94.5%.",
         "domain": "biotech", "actor": ["japan-govt"], "score": "75.5% → 94.5%",
         "evidences": ["hardware-grade-biology", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-02-18-beating-heart-on-a-chip"]},
        {"id": "2026-02-24-hasslers-age-you",
         "title": "Each difficult person in your life adds nine months of biological age",
         "claim": "Epigenetic clock research found each additional hassler in a person's life "
                  "adds roughly nine months of biological age and 1.5% faster aging.",
         "domain": "biotech", "score": "+9 months per hassler",
         "evidences": ["hardware-grade-biology"]},
        {"id": "2026-02-24-battery-storage-hits-576-gwh",
         "title": "US battery storage quadruples in three years",
         "claim": "US battery storage hit a record 57.6 GWh in 2025, up fourfold in three years, "
                  "with Texas about to overtake California, while lasers keep halving in price "
                  "every four years and doubling in power every five.",
         "domain": "energy", "score": "57.6 GWh",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-02-20-shadow-grid-of-gas-plants"]},
        {"id": "2026-02-24-humanoids-shovel-snow-in-new-york",
         "title": "Humanoids shovel snow in New York after a storm",
         "claim": "Reflex Robotics humanoids shovelled snow in New York after Winter Storm "
                  "Hernando.",
         "domain": "robotics", "actor": ["reflex-robotics"],
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-02-09-unitree-shovels-snow"]},
        {"id": "2026-02-24-odni-confirms-declassification",
         "title": "ODNI says the files will soon be declassified",
         "claim": "The ODNI said UAP and extraterrestrial files will soon be declassified and "
                  "the Secretary of War confirmed preparations to comply with the executive "
                  "order, saying he did not have that on his bingo card.",
         "domain": "policy", "actor": ["odni", "war-department"],
         "evidences": ["politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-20-uap-disclosure-directive"]},
        {"id": "2026-02-24-optimized-applications-all-sound-alike",
         "title": "Employers deprioritize the candidates who optimized hardest",
         "claim": "Employers report AI-assisted job applications now all sound the same, "
                  "deprioritizing the candidates who optimized hardest, while White House "
                  "officials explored a stablecoin for Gaza.",
         "domain": "economics", "actor": ["white-house"],
         "evidences": ["coordination-tax", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-02-19-slop-grievances-surge"]},
    ],
}
