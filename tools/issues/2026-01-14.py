"""Issue 033 — 2026-01-14. The AMS president proves a theorem with help."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-14-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-14", "title": "Welcome to January 14, 2026", "url": URL,
        "thesis": "Mathematics accepts insights it could not have reached alone.",
        "body": """
# Welcome to January 14, 2026

Ravi Vakil, president of the American Mathematical Society, proved a new result
in algebraic geometry with Gemini Deep Think and says he is unsure he could have
reached the insights alone. Harmonic, with $295 million, announces it is going
after the Riemann Hypothesis and the Millennium problems.

The other end of the same week: 244,851 tech jobs cut globally in 2025, and
Tesla ending one-time FSD purchases in favor of a monthly rental.
""",
    },
    "organizations": [
        {"id": "atoms", "type": "Organization", "title": "Atoms",
         "body": "Autonomous AI team that builds and scales real businesses."},
        {"id": "salesforce", "type": "Organization", "title": "Salesforce",
         "description": "Enterprise CRM company and owner of Slack that the corpus tracks shipping an "
                        "employee agent, then placing its whole CRM inside Claude.",
         "resource": "https://www.salesforce.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q941127"],
         "tags": ["big-tech"],
         "body": "Salesforce is the enterprise CRM company that owns Slack. In this corpus it enters by "
                 "[releasing Slackbot as an out-of-the-box employee agent](/developments/2026-01-14-atoms-autonomous-business-team.md) "
                 "([announcement](https://investor.salesforce.com/news/news-details/2026/Salesforce-Announces-the-General-Availability-of-Slackbot--Your-Personal-Agent-for-Work/default.aspx)), "
                 "and ten days later is the incumbent whose "
                 "[$350k contract a customer swapped for generated software](/developments/2026-01-24-350k-salesforce-contract-terminated.md). "
                 "By August it ships [Slack Code](/systems/slack-code.md) as a workplace for coding agents and "
                 "[puts its whole CRM inside Claude](/developments/2026-08-27-a-crm-placed-inside-a-model.md), "
                 "billed by consumption."},
        {"id": "essilorluxottica", "type": "Organization", "title": "EssilorLuxottica",
         "resource": "https://www.essilorluxottica.com/"},
        {"id": "overview-energy", "type": "Organization", "title": "Overview Energy",
         "body": "Beamed power from aircraft to ground by near-infrared laser."},
        {"id": "caterpillar", "type": "Organization", "title": "Caterpillar",
         "resource": "https://www.caterpillar.com/"},
        {"id": "etched", "type": "Organization", "title": "Etched",
         "resource": "https://www.etched.com/", "body": "Transformer-specific ASIC startup."},
        {"id": "filics", "type": "Organization", "title": "Filics",
         "body": "German startup replacing forklifts with swarming pallet robots."},
        {"id": "hhs", "type": "Organization", "title": "US Department of Health and Human Services",
         "resource": "https://www.hhs.gov/"},
        {"id": "eu-frontier-ai", "type": "Organization", "title": "European Frontier AI Initiative",
         "body": "Sovereign European frontier lab; first 30 researchers recruited."},
    ],
    "people": [
        {"id": "ravi-vakil", "type": "Person", "title": "Ravi Vakil", "name": "Ravi Vakil",
         "body": "President of the American Mathematical Society; proved a new algebraic "
                 "geometry result with Gemini Deep Think."},
    ],
    "systems": [
        {"id": "confer", "type": "AISystem", "title": "Confer", "modality": "text",
         "body": "Moxie Marlinspike's open-source assistant, cryptographically verifiable as "
                 "unreadable by anyone but the user."},
        {"id": "medgemma-1-5", "type": "AISystem", "title": "MedGemma 1.5",
         "developed_by": [B + "organizations/google"], "modality": "medical imaging"},
        {"id": "glm-image", "type": "AISystem", "title": "GLM-Image",
         "developed_by": [B + "organizations/zhipu-ai"], "modality": "image",
         "body": "Reportedly the first multimodal foundation model trained entirely on Huawei chips."},
    ],
    "developments": [
        {"id": "2026-01-14-vakil-proves-with-deep-think",
         "title": "The AMS president proves a result he is unsure he could reach alone",
         "claim": "Ravi Vakil, president of the American Mathematical Society, used Gemini Deep "
                  "Think to prove a new result in algebraic geometry, saying the model produced "
                  "insights he is unsure he could have reached alone.",
         "domain": "science", "actor": ["people/ravi-vakil", "google"],
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-01-13-tao-learned-from-aristotle"]},
        {"id": "2026-01-14-harmonic-targets-millennium-problems",
         "title": "Harmonic aims $295M at the Millennium problems",
         "claim": "Harmonic, holding $295 million, announced plans to solve the Riemann "
                  "Hypothesis, the Hodge Conjecture and the Millennium Prize problems.",
         "domain": "science", "actor": ["harmonic"], "score": "$295M",
         "evidences": ["root-node-problems", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-01-10-axiomprover-12-of-12-putnam"]},
        {"id": "2026-01-14-atoms-autonomous-business-team",
         "title": "An AI team builds and scales real businesses",
         "claim": "A startup called Atoms launched an autonomous AI team that builds, launches "
                  "and scales real businesses, while Salesforce released Slackbot as an "
                  "out-of-the-box employee agent.",
         "domain": "agents", "actor": ["atoms", "salesforce"],
         "evidences": ["agents-on-the-org-chart", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-13-mckinsey-employs-20000-agents"]},
        {"id": "2026-01-14-confer-verifiable-privacy",
         "title": "Signal's creator ships a verifiably private assistant",
         "claim": "Moxie Marlinspike launched Confer, an open-source AI assistant that is "
                  "cryptographically verifiable as unreadable by anyone but its user.",
         "domain": "agents", "about": [B + "systems/confer"],
         "evidences": ["intimate-interface", "coordination-tax"],
         "supersedes": [B + "developments/2025-12-24-marlinspike-last-days-of-software"]},
        {"id": "2026-01-14-billion-images-in-53-days",
         "title": "One model generates a billion images in 53 days",
         "claim": "Google said Nano Banana Pro generated a billion images in its first 53 days "
                  "and upgraded Veo 3.1 for identity consistency across video, while Meta and "
                  "EssilorLuxottica doubled smart glasses production to 20 million units a year.",
         "domain": "models", "actor": ["google", "meta", "essilorluxottica"],
         "about": [B + "systems/nano-banana-pro"], "score": "1B images / 53 days",
         "evidences": ["intimate-interface", "work-displaced"],
         "supersedes": [B + "developments/2026-01-07-meta-pauses-ray-ban-display"]},
        {"id": "2026-01-14-laser-power-beaming",
         "title": "Power is beamed from an aircraft by laser",
         "claim": "Overview Energy emerged from stealth after beaming power from an aircraft to "
                  "a ground receiver by near-infrared laser, planning orbital transmission by "
                  "2028, as NASA and the DOE partnered on a lunar fission reactor by 2030.",
         "domain": "energy", "actor": ["overview-energy", "nasa", "doe"],
         "evidences": ["orbit-as-compute", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-01-12-twilight-dawn-dusk-orbit"]},
        {"id": "2026-01-14-microsoft-570-energy-hires",
         "title": "Microsoft hires 570 energy specialists and offers to pay its way",
         "claim": "Microsoft has hired 570 energy specialists since 2022 and pledged to pay its "
                  "own way, asking utilities to set rates covering datacenter costs without "
                  "raising consumer bills.",
         "domain": "energy", "actor": ["microsoft"], "score": "570 hires",
         "evidences": ["burning-molecules-for-tokens", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-13-pjm-48pct-annual-demand-growth"]},
        {"id": "2026-01-14-caterpillar-300b-as-ai-play",
         "title": "A tractor company becomes a $300B AI play",
         "claim": "Caterpillar crossed a $300 billion valuation as a secondary AI play on "
                  "backup power generation.",
         "domain": "economics", "actor": ["caterpillar"], "score": "$300B",
         "evidences": ["compute-capital-stack", "capital-takes-the-plant"]},
        {"id": "2026-01-14-h200-allowed-china-restricts",
         "title": "The US allows H200 sales as China forbids buying them",
         "claim": "The US will allow Nvidia to sell H200 chips to China while China restricts "
                  "domestic purchases to force reliance on local silicon, and Zhipu released "
                  "GLM-Image, reportedly the first multimodal model fully trained on Huawei "
                  "chips.",
         "domain": "policy", "actor": ["nvidia", "china", "zhipu-ai"],
         "about": [B + "systems/glm-image"],
         "evidences": ["silicon-curtain", "open-weight-latency"],
         "supersedes": [B + "developments/2026-01-13-taiwan-deal-five-more-fabs"],
         "body": "Export control from both directions at once, each side restricting the same "
                 "trade for opposite reasons."},
        {"id": "2026-01-14-etched-500m-cerebras-22b",
         "title": "Specialty silicon raises against the GPU monopoly",
         "claim": "Etched has raised $500 million to compete with Nvidia while Cerebras eyes a "
                  "$22 billion valuation ahead of its IPO on wafer-scale compute.",
         "domain": "compute", "actor": ["etched", "cerebras"], "score": "$500M / $22B",
         "evidences": ["vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2025-12-20-cerebras-ipo-q2-2026"]},
        {"id": "2026-01-14-fsd-becomes-a-rental",
         "title": "Full Self-Driving becomes a monthly rental",
         "claim": "Tesla will stop selling Full Self-Driving as a one-time purchase next month, "
                  "moving entirely to monthly subscription, while Filics replaced forklifts with "
                  "omnidirectional pallet robots.",
         "domain": "economics", "actor": ["tesla", "filics"],
         "about": [B + "systems/tesla-fsd"],
         "evidences": ["autonomous-commerce", "software-margin-collapse"],
         "body": "Autonomy metered rather than owned."},
        {"id": "2026-01-14-hhs-autonomous-prescribing",
         "title": "HHS wants autonomous prescribing agents approved in two years",
         "claim": "The Department of Health and Human Services reportedly hopes to have the FDA "
                  "approve autonomous prescribing agents within two years, as Google released "
                  "the open-weight MedGemma 1.5 and the FDA moved to Bayesian statistics for "
                  "clinical trials.",
         "domain": "policy", "actor": ["hhs", "fda", "google"],
         "about": [B + "systems/medgemma-1-5"],
         "evidences": ["legislating-the-shift", "automated-science"],
         "supersedes": [B + "developments/2026-01-07-utah-ai-prescription-renewals"]},
        {"id": "2026-01-14-244851-tech-jobs-cut",
         "title": "244,851 tech jobs were cut in 2025",
         "claim": "RationalFX calculated that 244,851 tech jobs were cut globally in 2025 as "
                  "firms restructured around AI-driven productivity, while the European "
                  "Frontier AI Initiative recruited its first thirty researchers.",
         "domain": "economics", "actor": ["eu-frontier-ai"], "score": "244,851",
         "evidences": ["work-displaced", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-01-09-productivity-up-hours-flat"],
         "body": "The count behind the flat-hours statistic."},
    ],
}
