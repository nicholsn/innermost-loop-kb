"""Issue 025 — 2026-01-06. All software is about to be free."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-6-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-06", "title": "Welcome to January 6, 2026", "url": URL,
        "thesis": "Hardware scales while the software it runs becomes worthless.",
        "body": """
# Welcome to January 6, 2026

Two curves cross in this issue. Vera Rubin enters full production at 50
petaflops and a tenfold cut in inference cost; Musk agrees that all software is
about to be free. Capital pours into the substrate exactly as the thing it
produces stops being scarce.

Lego shipping a 2x4 brick with an ASIC and a mesh network in it is the other
half of the same story — compute becoming too cheap to meter, and therefore
appearing in children's toys.
""",
    },
    "organizations": [
        {"id": "amd", "type": "Organization", "title": "AMD", "resource": "https://www.amd.com/",
         "description": "American semiconductor company whose Instinct GPUs and ROCm software stack "
                        "are the principal challenger to Nvidia in AI training and inference "
                        "hardware.",
         "sameAs": ["http://www.wikidata.org/entity/Q128896"],
         "tags": ["chipmaker", "big-tech"],
         "body": "AMD designs CPUs, GPUs and the ROCm software stack, and in this corpus it is the "
                 "counterweight to Nvidia's hold on AI compute. It enters with the "
                 "[2-nm MI500 preview and Ryzen AI 400 launch](/developments/2026-01-06-amd-mi500-and-ryzen-ai-400.md) "
                 "at CES 2026 and its chief executive's forecast of "
                 "[five billion daily AI users](/developments/2026-01-06-veo-on-televisions.md), then "
                 "as the supplier in [Meta's 6 GW Instinct pact](/developments/2026-02-24-meta-amd-6gw-pact.md). "
                 "Its software gap is where it touches the recursive loop: "
                 "[ROCm improves 75-fold in fourteen days](/developments/2026-05-11-rocm-improves-75x-in-two-weeks.md) "
                 "and [agents write the kernels](/developments/2026-07-04-agents-write-the-kernels-closing-a-software-gap.md) "
                 "that let a challenger serve an open model on MI355X at half Blackwell's cost."},
        {"id": "lego", "type": "Organization", "title": "LEGO", "resource": "https://www.lego.com/",
         "body": "Shipped a programmable 2x4 brick with an on-board ASIC."},
        {"id": "qualcomm", "type": "Organization", "title": "Qualcomm",
         "resource": "https://www.qualcomm.com/"},
        {"id": "lg", "type": "Organization", "title": "LG", "resource": "https://www.lg.com/"},
        {"id": "mercedes-benz", "type": "Organization", "title": "Mercedes-Benz",
         "resource": "https://www.mercedes-benz.com/"},
        {"id": "lucid", "type": "Organization", "title": "Lucid Motors",
         "resource": "https://lucidmotors.com/"},
        {"id": "nuro", "type": "Organization", "title": "Nuro", "resource": "https://www.nuro.ai/"},
        {"id": "uber", "type": "Organization", "title": "Uber", "resource": "https://www.uber.com/"},
        {"id": "benchflow", "type": "Organization", "title": "BenchFlow",
         "body": "Jeff Dean-backed benchmark lab; published SkillsBench."},
        {"id": "donut-lab", "type": "Organization", "title": "Donut Lab",
         "body": "Solid-state battery charging in five minutes."},
        {"id": "bosch", "type": "Organization", "title": "Bosch",
         "resource": "https://www.bosch.com/"},
        {"id": "parcl", "type": "Organization", "title": "Parcl",
         "body": "Real estate prediction markets."},
    ],
    "hardware": [
        {"id": "vera-rubin", "type": "Hardware", "title": "Nvidia Vera Rubin",
         "description": "Nvidia's next-generation GPU platform, announced in full production in January "
                        "2026 at 50 petaflops of NVFP4 compute and a tenfold cut in inference cost.",
         "developed_by": [B + "organizations/nvidia"],
         "fabricated_by": [B + "organizations/nvidia"],
         "resource": "https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer",
         "sameAs": ["http://www.wikidata.org/entity/Q126888620"],
         "body": "50 petaflops of NVFP4 compute in full production; a tenfold reduction in inference cost. "
                 "Vera Rubin is [Nvidia](/organizations/nvidia.md)'s successor GPU platform, pairing Rubin "
                 "GPUs with Vera CPUs. It enters the corpus in the January 6, 2026 issue, when Nvidia "
                 "announced it in [full production](/developments/2026-01-06-vera-rubin-full-production.md) "
                 "and Musk said he would have the GPUs operating at scale within nine months "
                 "([Nvidia newsroom](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)). "
                 "It returns in August, when SpaceX's plan to fly Vera Rubin GPUs and Vera CPUs on Starmind "
                 "AI1 satellites is set beside a DeepMind executive's claim that "
                 "[recursive self-improvement justifies the capex](/developments/2026-08-04-recursive-self-improvement-justifies-the-capex.md)."},
        {"id": "lego-smart-brick", "type": "Hardware", "title": "LEGO Smart Brick",
         "fabricated_by": [B + "organizations/lego"],
         "body": "A standard 2x4 block containing a 4.1-mm ASIC and BrickNet mesh networking."},
    ],
    "benchmarks": [
        {"id": "skillsbench", "type": "Benchmark", "title": "SkillsBench",
         "published_by": [B + "organizations/benchflow"],
         "measures_capability": "audited agent performance on skilled tasks"},
    ],
    "developments": [
        {"id": "2026-01-06-vera-rubin-full-production",
         "title": "Vera Rubin enters production at 50 petaflops",
         "claim": "Nvidia's Vera Rubin platform entered full production delivering 50 petaflops "
                  "of NVFP4 compute and a tenfold reduction in inference cost, with Musk "
                  "expecting it at scale within nine months.",
         "domain": "compute", "actor": ["nvidia"], "about": [B + "hardware/vera-rubin"],
         "score": "50 PFLOPS, 10x cheaper inference",
         "evidences": ["reasoning-price-deflation", "vertical-silicon"]},
        {"id": "2026-01-06-dlss-45-five-frames",
         "title": "DLSS generates five frames for every one rendered",
         "claim": "Nvidia's DLSS 4.5 uses a second-generation transformer to generate five "
                  "frames per rendered frame, enabling path tracing above 240 FPS.",
         "domain": "models", "actor": ["nvidia"], "score": "5:1 frames",
         "evidences": ["reasoning-price-deflation"]},
        {"id": "2026-01-06-amd-mi500-and-ryzen-ai-400",
         "title": "AMD previews a 2-nm MI500 and ships edge silicon",
         "claim": "AMD previewed 2-nm MI500 GPUs for 2027 projecting a thousandfold AI "
                  "performance increase, and launched the Ryzen AI 400 series for the edge.",
         "domain": "compute", "actor": ["amd"], "score": "1000x by 2027",
         "evidences": ["vertical-silicon", "compute-capital-stack"]},
        {"id": "2026-01-06-intel-18a-core-ultra-3",
         "title": "Intel ships its first 18A consumer chips from US fabs",
         "claim": "Intel launched Core Ultra Series 3, its first chips built on the 18A process "
                  "and manufactured in the United States.",
         "domain": "compute", "actor": ["intel"],
         "evidences": ["silicon-curtain", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2025-12-30-samsung-texas-50k-wafers"]},
        {"id": "2026-01-06-lego-smart-brick",
         "title": "Lego puts an ASIC and a mesh network in a 2x4 brick",
         "claim": "Lego unveiled the Smart Brick, a standard 2x4 block containing a 4.1-mm ASIC "
                  "and BrickNet mesh networking, releasing programmable matter to children.",
         "domain": "compute", "actor": ["lego"], "about": [B + "hardware/lego-smart-brick"],
         "evidences": ["compiling-matter", "reasoning-price-deflation"],
         "body": "Compute cheap enough to appear in a toy is the clearest price signal in the "
                 "issue."},
        {"id": "2026-01-06-hyundai-30000-atlas-a-year",
         "title": "Hyundai plans 30,000 Atlas robots a year",
         "claim": "Hyundai plans to deploy 30,000 next-generation Atlas robots annually by "
                  "2028, running Google DeepMind's Gemini Robotics models.",
         "domain": "robotics", "actor": ["hyundai", "boston-dynamics", "google-deepmind"],
         "score": "30,000/yr by 2028",
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-01-04-atlas-enters-hyundai-plant"]},
        {"id": "2026-01-06-qualcomm-figure-dragonwing",
         "title": "Qualcomm puts Dragonwing silicon inside humanoids",
         "claim": "Qualcomm partnered with Figure to place Dragonwing IQ10 processors in its "
                  "next wave of humanoid robots.",
         "domain": "robotics", "actor": ["qualcomm", "figure"],
         "evidences": ["vertical-silicon", "physical-recursion"]},
        {"id": "2026-01-06-lg-cloid-zero-labor-home",
         "title": "LG aims a VLA home robot at the zero-labor home",
         "claim": "LG introduced CLOiD, a home robot built on vision-language-action models and "
                  "aimed at what it calls the zero-labor home.",
         "domain": "robotics", "actor": ["lg"], "evidences": ["work-displaced", "intimate-interface"]},
        {"id": "2026-01-06-nvidia-20pct-workforce-on-av",
         "title": "Nvidia puts a fifth of its workforce on autonomous driving",
         "claim": "Nvidia dedicated 20% of its workforce, some 7,000 people, to autonomous "
                  "vehicles and released the Alpamayo open reasoning models for driving edge "
                  "cases.",
         "domain": "robotics", "actor": ["nvidia"], "score": "7,000 people",
         "evidences": ["autonomy-clock-speed", "open-weight-latency"]},
        {"id": "2026-01-06-lucid-nuro-uber-fleet",
         "title": "Lucid, Nuro and Uber field a joint robotaxi fleet",
         "claim": "Lucid, Nuro and Uber unveiled a joint robotaxi fleet for the Bay Area, while "
                  "Mercedes-Benz began testing Nvidia's point-to-point Level 2 system.",
         "domain": "robotics", "actor": ["lucid", "nuro", "uber", "mercedes-benz"],
         "evidences": ["autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-03-london-waymo-baidu-head-to-head"]},
        {"id": "2026-01-06-all-software-about-to-be-free",
         "title": "Musk agrees all software is about to be free",
         "claim": "Elon Musk agreed that all software is about to be free, pointing at "
                  "imminent hyperdeflation in the sector.",
         "domain": "economics", "evidences": ["software-margin-collapse", "reasoning-price-deflation"]},
        {"id": "2026-01-06-vibe-coding-dies",
         "title": "Vibe coding dies because one-shotting works",
         "claim": "Engineers report that vibe coding is quietly dying because Claude Code can "
                  "one-shot two-month projects in minutes.",
         "domain": "agents", "actor": ["anthropic"], "about": [B + "systems/claude-code"],
         "evidences": ["engineer-as-supervisor", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-01-05-five-years-in-four-hours"]},
        {"id": "2026-01-06-edge-becomes-a-copilot-app",
         "title": "Microsoft rebuilds its browser as a Copilot app",
         "claim": "Microsoft is redesigning Edge to function as a Copilot application, "
                  "dissolving the browser into the agent.",
         "domain": "agents", "actor": ["microsoft"], "evidences": ["autonomous-commerce", "intimate-interface"]},
        {"id": "2026-01-06-skillsbench-audits-agents",
         "title": "SkillsBench audits agents more strictly",
         "claim": "Jeff Dean-backed BenchFlow introduced SkillsBench to audit agent performance "
                  "under stricter conditions.",
         "domain": "benchmarks", "actor": ["benchflow"], "about": [B + "benchmarks/skillsbench"],
         "evidences": ["benchmark-saturation"]},
        {"id": "2026-01-06-veo-on-televisions",
         "title": "Video generation arrives on the television",
         "claim": "Google's Veo video model is coming to TVs, letting viewers generate media on "
                  "demand, while AMD's CEO predicted 5 billion daily AI users within five years.",
         "domain": "models", "actor": ["google", "amd"], "about": [B + "systems/veo"],
         "score": "5B daily users", "evidences": ["intimate-interface"]},
        {"id": "2026-01-06-xai-five-gas-turbines",
         "title": "xAI buys five 380-MW gas turbines",
         "claim": "xAI purchased five 380-MW gas turbines to power a new cluster, while Crusoe "
                  "began hosting GB200s on Icelandic geothermal.",
         "domain": "energy", "actor": ["xai", "crusoe"], "score": "1.9 GW",
         "evidences": ["burning-molecules-for-tokens", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-04-meta-four-turbine-types"]},
        {"id": "2026-01-06-doe-27b-uranium-enrichment",
         "title": "The DOE puts $2.7B into domestic enrichment",
         "claim": "The Department of Energy awarded $2.7 billion to jumpstart domestic uranium "
                  "enrichment, as Foxconn reported revenue up 26.4% on AI demand.",
         "domain": "policy", "actor": ["doe", "foxconn"], "score": "$2.7B",
         "evidences": ["science-as-industrial-policy", "burning-molecules-for-tokens"]},
        {"id": "2026-01-06-five-minute-solid-state-battery",
         "title": "A solid-state battery charges in five minutes",
         "claim": "Donut Lab introduced a solid-state battery that charges in five minutes, "
                  "while CATL began commercial-scale sodium-ion deployment.",
         "domain": "energy", "actor": ["donut-lab", "catl"], "score": "5 minutes",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-01-05-tesla-semi-1-2mw-charging"]},
        {"id": "2026-01-06-crispr-nasal-spray-for-flu",
         "title": "A CRISPR nasal spray edits influenza in the lungs",
         "claim": "Australian researchers are developing a CRISPR Cas13 nasal spray that edits "
                  "influenza RNA directly in the lungs.",
         "domain": "biotech", "evidences": ["hardware-grade-biology"]},
        {"id": "2026-01-06-nasa-244b-lunar-fission",
         "title": "Congress funds lunar fission inside a $24.4B NASA budget",
         "claim": "Congress approved a $24.4 billion NASA budget including $250 million for "
                  "nuclear fission on the Moon.",
         "domain": "policy", "actor": ["nasa", "us-congress"], "score": "$24.4B / $250M",
         "evidences": ["inhabitable-worlds", "science-as-industrial-policy"]},
        {"id": "2026-01-06-bosch-29b-ai-13000-cuts",
         "title": "Bosch spends $2.9B on AI while cutting 13,000 jobs",
         "claim": "Bosch is investing $2.9 billion in AI while cutting 13,000 jobs, and Parcl "
                  "and Polymarket launched real estate prediction markets.",
         "domain": "economics", "actor": ["bosch", "parcl", "polymarket"], "score": "$2.9B / -13,000",
         "evidences": ["work-displaced", "autonomous-commerce"]},
    ],
}
