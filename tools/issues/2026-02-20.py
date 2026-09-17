"""Issue 059 — 2026-02-20. Disclosure forced by the curve."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-20-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-20", "title": "Welcome to February 20, 2026", "url": URL,
        "thesis": "The UAP file opens, and the stated reason is the AI curve.",
        "body": """
# Welcome to February 20, 2026

The White House directed the Secretary of War and other agencies to begin
releasing government files on extraterrestrial life. The reasoning circulating
alongside it is the striking part: disclosure was "forced on us because of the
AI curve," on the theory that building superintelligence is risky to any
non-human intelligence with access to Earth.

Meanwhile RentAHuman passes 500,000 people signed up, and businesses replace
freelancers at $1 of human labor per $0.03 of AI spend.
""",
    },
    "organizations": [
        {"id": "bafta", "type": "Organization", "title": "BAFTA",
         "resource": "https://www.bafta.org/"},
        {"id": "type-one-energy", "type": "Organization", "title": "Type One Energy",
         "body": "Stellarator developer targeting a prototype by 2029."},
        {"id": "research-revival", "type": "Organization", "title": "Research Revival",
         "body": "Funds recovery of neglected and buried research."},
        {"id": "california", "type": "Organization", "title": "State of California"},
        {"id": "odni", "type": "Organization", "title": "ODNI",
         "resource": "https://www.dni.gov/"},
    ],
    "systems": [
        {"id": "gemini-3-1-pro", "type": "AISystem", "title": "Gemini 3.1 Pro",
         "developed_by": [B + "organizations/google"], "modality": "text"},
    ],
    "developments": [
        {"id": "2026-02-20-uap-disclosure-directive",
         "title": "The White House orders release of extraterrestrial files",
         "claim": "The White House directed the Secretary of War and other agencies to begin "
                  "releasing government files on extraterrestrial life and UAPs, after scolding "
                  "former President Obama for discussing classified information.",
         "domain": "policy", "actor": ["white-house"],
         "evidences": ["politics-as-infrastructure", "legislating-the-shift"]},
        {"id": "2026-02-20-disclosure-forced-by-the-ai-curve",
         "title": "Disclosure is framed as forced by the AI curve",
         "claim": "Commentators argued disclosure was forced by the AI curve, on the reasoning "
                  "that developing superintelligence is potentially risky to any non-human "
                  "intelligence with access to Earth.",
         "domain": "society",
         "evidences": ["takeoff-declared", "politics-as-infrastructure"],
         "body": "The first item in the corpus where the capability curve is offered as the "
                 "cause of a government disclosure decision."},
        {"id": "2026-02-20-gemini-31-pro-leads-the-index",
         "title": "Gemini 3.1 Pro takes the index lead at half the evaluation cost",
         "claim": "Google launched Gemini 3.1 Pro with 44.4% on Humanity's Last Exam without "
                  "tools, 77.1% on ARC-AGI-2 and 94.3% on GPQA Diamond, which Artificial "
                  "Analysis ranked the new Intelligence Index leader at less than half the "
                  "evaluation cost of Opus 4.6 or GPT-5.2.",
         "domain": "benchmarks", "actor": ["google", "artificial-analysis"],
         "about": [B + "systems/gemini-3-1-pro"], "score": "44.4% HLE / 77.1% ARC-AGI-2",
         "evidences": ["benchmark-saturation", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-02-18-sonnet-46-beats-opus"]},
        {"id": "2026-02-20-rentahuman-500000-signups",
         "title": "Half a million people sign up to work for agents",
         "claim": "RentAHuman now has 500,000 people signed up to take physical tasks from AI "
                  "agents, while OpenAI's Codex lead predicted today's coding agents will look "
                  "funny within ten weeks.",
         "domain": "economics", "actor": ["rentahuman", "openai"], "score": "500,000 people",
         "evidences": ["humans-as-peripherals", "agent-economy"],
         "supersedes": [B + "developments/2026-02-13-waymo-pays-humans-to-close-doors"]},
        {"id": "2026-02-20-one-dollar-of-labor-for-three-cents",
         "title": "Freelancers are replaced at three cents on the dollar",
         "claim": "Research found businesses replacing Upwork and Fiverr freelancers with AI at "
                  "a rate of one dollar of human labor for three cents of AI spending.",
         "domain": "economics", "score": "$1 → $0.03",
         "evidences": ["work-displaced", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-02-08-agent-outearns-minimum-wage"],
         "body": "The substitution ratio, stated directly."},
        {"id": "2026-02-20-multi-evolve-tenfold-protein-gains",
         "title": "One round of ML guidance gives tenfold gains in directed evolution",
         "claim": "The Arc Institute's MULTI-evolve framework achieved tenfold improvements in "
                  "protein directed evolution with a single round of machine learning guidance.",
         "domain": "biotech", "actor": ["arc-institute"], "score": "10x",
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-19-all-disease-in-ten-to-twenty-years"]},
        {"id": "2026-02-20-taiwan-imports-pass-china",
         "title": "US imports from Taiwan pass China for the first time since 1992",
         "claim": "The AI boom pushed US imports from Taiwan past those from China for the first "
                  "time since 1992, running on semiconductors, while Amazon dethroned Walmart as "
                  "the world's largest company by revenue on datacenter growth.",
         "domain": "economics", "actor": ["amazon"],
         "evidences": ["silicon-curtain", "compute-capital-stack"]},
        {"id": "2026-02-20-gpus-as-loan-collateral",
         "title": "AI chips are used as loan collateral",
         "claim": "AMD is backstopping a $300 million loan to Crusoe using AI chips as "
                  "collateral, the first known example of AMD GPUs as a financial instrument.",
         "domain": "economics", "actor": ["amd", "crusoe"], "score": "$300M",
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-02-19-openai-closes-100b-at-830b"]},
        {"id": "2026-02-20-shadow-grid-of-gas-plants",
         "title": "A shadow grid of off-grid gas plants forms around datacenters",
         "claim": "Data centers are spawning a shadow grid of off-grid natural gas plants "
                  "because solar and wind variability is unmanageable without backup, with "
                  "SoftBank forming a consortium for a $33 billion 9.2-GW plant on the "
                  "Ohio-Kentucky border that would be the largest in the US.",
         "domain": "energy", "actor": ["softbank"], "score": "9.2 GW / $33B",
         "evidences": ["burning-molecules-for-tokens", "regulatory-exit"],
         "supersedes": [B + "developments/2026-02-18-ormat-geothermal-for-google"]},
        {"id": "2026-02-20-bafta-names-human-achievement",
         "title": "BAFTA makes human achievement a guiding principle",
         "claim": "BAFTA introduced human achievement as a guiding principle for its awards, "
                  "the first major cinematic institution to formally distinguish carbon-based "
                  "creativity.",
         "domain": "society", "actor": ["bafta"],
         "evidences": ["agent-exclusion", "work-displaced"],
         "supersedes": [B + "developments/2026-02-17-free-for-humans-ten-for-agents"]},
        {"id": "2026-02-20-anthropic-may-pass-openai-revenue",
         "title": "Epoch projects Anthropic passing OpenAI's revenue by mid-2026",
         "claim": "Epoch AI projects Anthropic, growing tenfold a year, may surpass OpenAI's "
                  "revenue by mid-2026, while Nvidia is close to finalizing a $30 billion "
                  "investment in OpenAI.",
         "domain": "economics", "actor": ["epoch-ai", "anthropic", "openai", "nvidia"],
         "score": "$30B",
         "evidences": ["compute-capital-stack"]},
        {"id": "2026-02-20-europe-cannot-restructure",
         "title": "Restructuring costs 62 months of salary in Spain against 7 in the US",
         "claim": "Corporate restructuring costs 62 months of salary per employee in Spain "
                  "against seven in the US, a rigidity offered as explanation for why Europe "
                  "struggles to build into the new economy.",
         "domain": "economics", "score": "62 vs 7 months",
         "evidences": ["work-displaced", "coordination-tax"]},
        {"id": "2026-02-20-3d-printers-must-block-firearms",
         "title": "California would require 3D printers to block firearm manufacture",
         "claim": "California introduced a bill requiring all 3D printers sold in the state to "
                  "be certified with firearm blocking technology, an early sign of regulation "
                  "grappling with decentralized manufacturing.",
         "domain": "policy", "actor": ["california"],
         "evidences": ["compiling-matter", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-01-27-hassabis-18-months-to-humanoids"]},
        {"id": "2026-02-20-chickens-show-bouba-kiki",
         "title": "Newborn chickens show the bouba-kiki effect",
         "claim": "Newborn chickens were found to exhibit the bouba-kiki effect, associating "
                  "round shapes with round sounds, suggesting cross-modal abstraction predates "
                  "language.",
         "domain": "science",
         "evidences": ["biosphere-uplift", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-02-07-bonobos-identify-pretend-objects"],
         "body": "The circle of minds worth taking seriously widens from the egg as well as "
                 "from the server rack."},
    ],
}
