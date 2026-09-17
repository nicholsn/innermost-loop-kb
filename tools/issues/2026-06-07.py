"""Issue 133 — 2026-06-07. Everyone wants on the cap table."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-7-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-07", "title": "Welcome to June 7, 2026", "url": URL,
        "thesis": "The state, the left and the labs all reach for the same equity.",
        "body": """
# Welcome to June 7, 2026

The President says he is interested in the US government holding equity stakes
in leading AI labs. OpenAI is weighing donating equity to seed a Public Wealth
Fund. Sanders wants a bill transferring 50% of top labs' equity outright. When
the upside is this steep, everyone wants on the cap table.

Meanwhile the agents still get winded: SWE-Marathon strings twenty multi-hour
engineering tasks together and frontier models resolve under 19%.
""",
    },
    "organizations": [
        {"id": "adaption-labs", "type": "Organization", "title": "Adaption Labs"},
        {"id": "rochester", "type": "Organization", "title": "University of Rochester"},
        {"id": "sp-dow-jones", "type": "Organization", "title": "S&P Dow Jones Indices"},
    ],
    "developments": [
        {"id": "2026-06-07-everyone-wants-on-the-cap-table",
         "title": "The state and the left converge on taking lab equity",
         "claim": "The President said he is interested in the US government holding equity "
                  "stakes in leading AI labs, OpenAI is reportedly weighing donating equity to "
                  "seed a Public Wealth Fund, and Senator Sanders plans a bill transferring 50% "
                  "of top labs' equity to a public fund.",
         "domain": "policy", "actor": ["white-house", "openai", "us-congress"],
         "evidences": ["politics-as-infrastructure", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-05-washington-weighs-equity-in-the-labs"]},
        {"id": "2026-06-07-agents-lose-the-thread-over-hours",
         "title": "Frontier agents resolve under a fifth of a multi-hour task marathon",
         "claim": "The new SWE-Marathon benchmark strings together twenty multi-hour "
                  "engineering tasks, and even frontier models resolve under 19%, losing the "
                  "thread over hours.",
         "domain": "benchmarks", "score": "<19%",
         "evidences": ["benchmark-saturation", "autonomy-clock-speed", "spiky-frontier"],
         "supersedes": [B + "developments/2026-05-28-a-contamination-free-software-benchmark"],
         "body": "A counterweight to the 35-hour autonomous runs: duration is not the "
                 "same as coherence."},
        {"id": "2026-06-07-enterprises-route-by-difficulty",
         "title": "Enterprises start routing hard tasks to the frontier and easy ones elsewhere",
         "claim": "CFOs are reining in AI spending and enterprises are routing hard tasks to "
                  "frontier models and easy ones to cheaper rivals, threatening OpenAI's and "
                  "Anthropic's premium valuations, while Google supplies the cheap end with "
                  "quantization-aware Gemma 4 checkpoints under 1GB.",
         "domain": "economics", "actor": ["openai", "anthropic", "google"],
         "evidences": ["reasoning-price-deflation", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-06-03-a-company-caps-coding-tool-spend"]},
        {"id": "2026-06-07-a-specialist-clears-two-papers-in-lean",
         "title": "A specialist system autoformalizes two number-theory papers",
         "claim": "LeanMarathon autoformalizes research mathematics in Lean over hours-long "
                  "runs, clearing every target in two number-theory papers, while Adaption Labs "
                  "opened a $50,000 four-week challenge to release goal-adapted models openly.",
         "domain": "science", "actor": ["adaption-labs"], "score": "$50,000 prize",
         "evidences": ["automated-science", "generalism-beats-specialism", "proof-priced-per-unit"],
         "supersedes": [B + "developments/2026-06-03-the-leiden-declaration"]},
        {"id": "2026-06-07-a-general-model-matches-chemistry-tools",
         "title": "An untuned general model matches specialist chemistry software",
         "claim": "Anthropic's first chemistry white paper showed Claude Opus 4.7, untuned for "
                  "chemistry, matching ChemDraw and MestReNova at NMR prediction and working "
                  "backward to infer an unknown molecule's structure from its 1D NMR and "
                  "mass-spec data.",
         "domain": "science", "actor": ["anthropic"],
         "evidences": ["generalism-beats-specialism", "automated-science"],
         "supersedes": [B + "developments/2026-06-07-a-specialist-clears-two-papers-in-lean"]},
        {"id": "2026-06-07-cve-disclosures-spike-with-a-model-release",
         "title": "Critical CVE disclosures spike as a model preview lands",
         "claim": "Epoch AI now tracks CVEs from every reporting organization, with high- and "
                  "critical-severity disclosures spiking as the Claude Mythos Preview landed, "
                  "while OpenAI shipped an optional Lockdown Mode disabling Deep Research and "
                  "Agent Mode to blunt prompt injection.",
         "domain": "compute", "actor": ["epoch-ai", "openai", "anthropic"],
         "evidences": ["risk-becomes-uninsurable", "sandbox-escape"],
         "supersedes": [B + "developments/2026-05-29-five-billion-to-secure-the-open-source-supply-chain"]},
        {"id": "2026-06-07-a-rival-ends-up-powering-its-pursuer",
         "title": "A rival spends a year chasing a lab and ends up powering it",
         "claim": "Apollo and Blackstone closed a $35 billion private-credit package funding "
                  "Google TPUs for Anthropic to lease, while xAI spent a chaotic year chasing "
                  "Anthropic only to end up powering it through Colossus 1, and Google agreed "
                  "to pay SpaceX $920 million a month for roughly 110,000 GPUs at xAI's sites.",
         "domain": "economics", "actor": ["apollo-global", "blackstone", "google", "anthropic",
                                          "xai", "spacex"],
         "score": "$35B / $920M per month",
         "evidences": ["coordination-tax", "compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-06-03-the-tpu-debt-deal-prices"],
         "body": "One observer noted that with a single deal the SpaceX IPO went from "
                 "100x revenue to 50x revenue."},
        {"id": "2026-06-07-a-state-freezes-large-datacenter-permits",
         "title": "A state legislature passes a one-year datacenter permit freeze",
         "claim": "New York's legislature passed a one-year freeze on permits for data centers "
                  "above 20 MW, a first in the nation if the governor signs.",
         "domain": "policy", "actor": ["new-york-state"], "score": "20 MW threshold",
         "evidences": ["infrastructure-crowding-out", "regulatory-exit"],
         "supersedes": [B + "developments/2026-06-02-eighty-billion-in-equity-as-a-tax-break-dies"]},
        {"id": "2026-06-07-a-humanoid-loses-its-head-and-keeps-swinging",
         "title": "A humanoid loses its head mid-fight and keeps going",
         "claim": "Fight videos of China's T800 humanoid show one losing its head and continuing "
                  "to swing, a literal demonstration of graceful degradation.",
         "domain": "robotics", "actor": ["china"],
         "evidences": ["physical-recursion", "violence-arrives"],
         "supersedes": [B + "developments/2026-05-17-four-days-of-humanoids-until-failure"]},
        {"id": "2026-06-07-a-plasma-signature-five-years-early",
         "title": "A plasma signature flags lung cancer five years early",
         "claim": "Francis Crick Institute researchers used machine learning to find a "
                  "14-protein plasma signature flagging lung cancer five years early and "
                  "marking who benefits most from anti-IL-1β therapy.",
         "domain": "biotech", "actor": ["crick-institute"], "score": "5 years early",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-05-28-a-world-model-of-protein-biology"]},
        {"id": "2026-06-07-embryos-base-edited-without-crispr-damage",
         "title": "Human embryos are base-edited without CRISPR's chromosomal damage",
         "claim": "Columbia scientists base-edited LDL and fetal-hemoglobin genes in human "
                  "embryos without CRISPR's chromosomal damage, a step toward erasing inherited "
                  "disease before birth, while the White House backed a Utah pilot for AI "
                  "prescription refills and a path for autonomous AI doctors.",
         "domain": "biotech", "actor": ["columbia", "white-house"],
         "evidences": ["hardware-grade-biology", "compiling-matter"],
         "supersedes": [B + "developments/2026-06-05-a-genome-stitched-error-free-in-days"]},
        {"id": "2026-06-07-three-point-four-trillion-by-2040",
         "title": "A bank tells IPO investors one company's revenue could reach $3.4T",
         "claim": "Morgan Stanley told IPO investors SpaceX revenue could reach $3.4 trillion "
                  "by 2040, up from $18.67 billion, mostly on AI, while S&P Dow Jones refused "
                  "to fast-track it or waive profitability rules for unprofitable megacaps "
                  "OpenAI and Anthropic.",
         "domain": "economics", "actor": ["morgan-stanley", "spacex", "sp-dow-jones"],
         "score": "$3.4T by 2040",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-02-two-hundred-twenty-stranded-unicorns"]},
        {"id": "2026-06-07-banks-build-a-shared-tokenized-deposit-network",
         "title": "The big banks plan a shared tokenized-deposit network",
         "claim": "JPMorgan, Citi and peers are planning a shared tokenized-deposit network "
                  "with 24/7 settlement to fend off stablecoins, as Meta weighs a "
                  "multi-billion-dollar offering to fund AI spending of up to $145 billion this "
                  "year following Google's $85 billion share sale.",
         "domain": "economics", "actor": ["jpmorgan", "citigroup", "meta", "google"],
         "score": "$145B Meta capex",
         "evidences": ["debt-funded-buildout", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-07-a-rival-ends-up-powering-its-pursuer"]},
    ],
}
