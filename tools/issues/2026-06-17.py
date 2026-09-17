"""Issue 141 — 2026-06-17. The Singularity speaks Mandarin."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-17-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-17", "title": "Welcome to June 17, 2026", "url": URL,
        "thesis": "The leading open model is Chinese, and the frontier model is unavailable.",
        "body": """
# Welcome to June 17, 2026

GLM-5.2 took first on Design Arena, leapfrogging a "now unavailable" Claude
Fable 5 — a phrase doing real geopolitical work. Anthropic's consolation was
Epoch's Capabilities Index, where Fable 5 beat GPT-5.5 Pro by a point, its
first lead in a year, and reaches almost no one.

An AI chemist ran 10,080 experiments in a robotic lab and taught itself the
trick that made a stubborn reaction work.
""",
    },
    "organizations": [
        {"id": "molecule-one", "type": "Organization", "title": "Molecule.one"},
        {"id": "chainguard", "type": "Organization", "title": "Chainguard"},
        {"id": "sandboxaq", "type": "Organization", "title": "SandboxAQ"},
        {"id": "kazakhstan", "type": "Organization", "title": "Kazakhstan"},
        {"id": "anysphere", "type": "Organization", "title": "Anysphere",
         "body": "Maker of Cursor; acquired by SpaceX for $60B."},
        {"id": "uc-davis", "type": "Organization", "title": "UC Davis"},
        {"id": "anssi", "type": "Organization", "title": "ANSSI",
         "body": "France's national cybersecurity agency."},
    ],
    "developments": [
        {"id": "2026-06-17-the-leading-open-model-is-chinese",
         "title": "A Chinese open model takes the lead while the frontier sits unavailable",
         "claim": "Z.ai's GLM-5.2 packs 744 billion parameters into MIT-licensed million-token "
                  "weights and was crowned the leading open model at 51 by Artificial Analysis, "
                  "also taking first on Design Arena at 1360 Elo, leapfrogging a now-unavailable "
                  "Claude Fable 5.",
         "domain": "models", "actor": ["zai", "artificial-analysis"], "score": "744B params / 51 AAII",
         "evidences": ["open-weight-latency", "frontier-moves-backward", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-14-radical-openness-answers-within-hours"]},
        {"id": "2026-06-17-an-ai-chemist-runs-ten-thousand-experiments",
         "title": "A near-autonomous AI chemist runs 10,080 experiments and finds the trick",
         "claim": "OpenAI and Molecule.one set a near-autonomous AI chemist loose in a robotic "
                  "lab where, across 10,080 experiments, it taught itself the trick that made a "
                  "stubborn but useful reaction work, lifting its yield.",
         "domain": "science", "actor": ["openai", "molecule-one"], "score": "10,080 experiments",
         "evidences": ["automated-science", "discovery-as-process", "compiling-matter"],
         "supersedes": [B + "developments/2026-06-12-a-beam-a-hundred-million-times-brighter-than-the-sun"]},
        {"id": "2026-06-17-humans-plan-and-the-model-executes",
         "title": "A study of 400,000 sessions splits planning from execution",
         "claim": "Anthropic's analysis of 400,000 Claude Code sessions found humans owning 70% "
                  "of planning and Claude 80% of execution, with domain expertise beating coding "
                  "background and debugging time halving over seven months.",
         "domain": "agents", "actor": ["anthropic"], "score": "70% planning / 80% execution",
         "evidences": ["engineer-as-supervisor", "botsitting", "deskilling"],
         "supersedes": [B + "developments/2026-06-15-eleven-hours-saved-and-six-spent-botsitting"]},
        {"id": "2026-06-17-cognition-priced-like-crude",
         "title": "Token price indices appear for the major labs",
         "claim": "Ornn launched token price indices for OpenAI and Anthropic and Microsoft "
                  "began offering a cheap DeepSeek tier inside Copilot Cowork, pricing cognition "
                  "by the token the way commodities are priced by the barrel.",
         "domain": "economics", "actor": ["ornn", "microsoft", "openai", "anthropic", "deepseek"],
         "evidences": ["reasoning-price-deflation", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-12-nations-co-train-one-shared-model"]},
        {"id": "2026-06-17-two-thousand-flaws-patched-pre-disclosure",
         "title": "A coalition patches 2,000 flaws before disclosure",
         "claim": "Chainguard's Athena coalition, drawing on Anthropic's Glasswing and OpenAI's "
                  "Daybreak, patched 2,000 flaws ahead of public disclosure.",
         "domain": "compute", "actor": ["chainguard", "anthropic", "openai"], "score": "2,000 flaws",
         "evidences": ["risk-becomes-uninsurable", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-06-12-malware-hides-behind-safety-refusals"]},
        {"id": "2026-06-17-fifty-nine-percent-of-a-platform-is-slop",
         "title": "A majority of one platform's content is machine-generated",
         "claim": "59% of TikTok content is AI-generated slop, triple YouTube's share, and a "
                  "leading forensics expert said deepfakes have him going blind, while France "
                  "swapped Palantir for domestic software and a Mistral assistant.",
         "domain": "society", "actor": ["mistral", "palantir"], "score": "59% of TikTok",
         "evidences": ["bots-outnumber-us", "agent-exclusion", "regulatory-exit"],
         "supersedes": [B + "developments/2026-06-04-answer-engine-optimization-poisons-a-forum"]},
        {"id": "2026-06-17-capex-tops-cash-flow",
         "title": "Hyperscaler capex is forecast to exceed cash flow",
         "claim": "Epoch warned hyperscaler capital expenditure will top cash flow by the third "
                  "quarter, as Kazakhstan signed a $10 billion data center deal for 100,000 GPUs "
                  "and Microsoft borrowed AWS capacity to keep a GitHub straining under 14 "
                  "billion AI commits alive.",
         "domain": "economics", "actor": ["epoch-ai", "kazakhstan", "microsoft", "amazon"],
         "score": "$10B / 14B AI commits",
         "evidences": ["debt-funded-buildout", "compute-capital-stack", "coordination-tax"],
         "supersedes": [B + "developments/2026-06-15-two-and-a-half-years-for-a-transformer"]},
        {"id": "2026-06-17-unpermitted-turbines-called-vital",
         "title": "Unpermitted turbines are called vital because the model serves the military",
         "claim": "The Justice Department called xAI's unpermitted Memphis turbines vital "
                  "because Grok serves the military, just as Washington let its data-center "
                  "oversight law lapse.",
         "domain": "policy", "actor": ["xai", "white-house"],
         "evidences": ["politics-as-infrastructure", "regulatory-exit", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-06-13-seventy-five-projects-blocked-in-a-quarter"]},
        {"id": "2026-06-17-the-first-license-to-build-a-fusion-plant",
         "title": "A company wins the first license to build a fusion plant",
         "claim": "Helion won the first license ever issued to build a fusion power plant, while "
                  "American battery output continued to climb steeply.",
         "domain": "energy", "actor": ["helion"],
         "evidences": ["industrialized-nature", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-06-13-a-crewed-aircraft-on-solid-state-batteries"]},
        {"id": "2026-06-17-the-largest-startup-buyout-ever",
         "title": "A rocket company buys an IDE maker for $60B",
         "claim": "SpaceX's post-IPO surge carried it past Amazon and briefly Microsoft in "
                  "market value, after which it bought Cursor-maker Anysphere for $60 billion, "
                  "the largest startup buyout ever.",
         "domain": "economics", "actor": ["spacex", "anysphere"], "score": "$60B",
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2026-06-13-the-first-trillionaire"]},
        {"id": "2026-06-17-a-voice-returned-to-a-man-with-als",
         "title": "A brain interface returns a man's voice",
         "claim": "A UC Davis brain interface gave a man with ALS his voice back, while Stanford "
                  "researchers dated the biological age of 40 cell types and found aged "
                  "astrocytes triple Alzheimer's risk in APOE4 carriers.",
         "domain": "biotech", "actor": ["uc-davis", "stanford"],
         "evidences": ["intimate-interface", "longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-13-chromatin-shredded-in-p53-mutant-cancers"]},
        {"id": "2026-06-17-lab-chiefs-join-heads-of-state",
         "title": "AI chiefs join heads of state to propose walling off a rival",
         "claim": "At a closed G7 lunch in Évian, Amodei and Hassabis pushed a US-led coalition "
                  "walling China off from frontier compute, the first time AI chiefs joined "
                  "heads of state on risk, sovereignty and child safety.",
         "domain": "policy", "actor": ["anthropic", "google-deepmind"],
         "evidences": ["politics-as-infrastructure", "silicon-curtain", "models-as-munitions"],
         "supersedes": [B + "developments/2026-06-15-a-lab-sends-staff-to-unwind-an-export-ban"]},
        {"id": "2026-06-17-quantum-safe-crypto-required",
         "title": "A national agency moves to require quantum-safe cryptography",
         "claim": "France's ANSSI moved to require quantum-safe cryptography against harvest "
                  "now, decrypt later attacks, as a preprint argued a qubit could crack "
                  "NP-complete problems if gravity stays classical — which its authors take as "
                  "proof it cannot.",
         "domain": "compute", "actor": ["anssi"],
         "evidences": ["risk-becomes-uninsurable", "root-node-problems"],
         "supersedes": [B + "developments/2026-06-03-a-quantum-chip-designed-by-an-agent"]},
    ],
}
