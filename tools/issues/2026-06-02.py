"""Issue 129 — 2026-06-02. The finish line becomes a leaderboard."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-2-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-02", "title": "Welcome to June 2, 2026", "url": URL,
        "thesis": "The gap between frontier models is now measured in multiples per quarter.",
        "body": """
# Welcome to June 2, 2026

Opus 4.8 posted a state-of-the-art 1.5% of human efficiency on ARC-AGI-3,
tripling GPT-5.5's score. One and a half percent of a human, and it is the
best in the world — the benchmark that still humiliates every model is also
the one where quarterly gains now come in multiples.

Elsewhere: hackers took over the Obama White House Instagram by politely
asking a support bot to change the email.
""",
    },
    "themes": [
        {"id": "oral-tradition-dissolves", "type": "Theme",
         "title": "Institutional memory dissolves into weights",
         "first_seen": "2026-06-02", "domain": "society",
         "body": "The knowledge that passed from mentor to junior — unwritten, "
                 "situational, learned by proximity — stops being transmitted between "
                 "people and starts being absorbed by models. The chain breaks in the "
                 "generation that never had to learn it."},
    ],
    "organizations": [
        {"id": "enisa", "type": "Organization", "title": "ENISA",
         "body": "EU Agency for Cybersecurity; first European agency in Project Glasswing."},
        {"id": "aft", "type": "Organization", "title": "American Federation of Teachers",
         "body": "The second-largest US teachers' union."},
        {"id": "hpe", "type": "Organization", "title": "Hewlett Packard Enterprise"},
        {"id": "ohio", "type": "Organization", "title": "Ohio"},
    ],
    "developments": [
        {"id": "2026-06-02-one-and-a-half-percent-of-a-human",
         "title": "The best model reaches 1.5% of human efficiency on ARC-AGI-3",
         "claim": "Opus 4.8 posted a state-of-the-art 1.5% of human efficiency on ARC-AGI-3, "
                  "tripling GPT-5.5's score and showing that the gap between frontier models is "
                  "now measured in multiples per quarter.",
         "domain": "benchmarks", "actor": ["anthropic", "openai", "arc-prize"], "score": "1.5%",
         "evidences": ["spiky-frontier", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-05-29-the-safest-model-is-also-the-strongest"]},
        {"id": "2026-06-02-open-weights-undercut-by-forty-fold",
         "title": "An open-weight model undercuts the frontier forty-fold",
         "claim": "MiniMax's M3 claims to be the only open-weight model fusing frontier coding, "
                  "a million-token context and native multimodality, priced at $0.12 per million "
                  "input tokens against Opus 4.7's $5, while Nvidia's Nemotron 3 Ultra became "
                  "the smartest open US model at roughly 550B parameters — still trailing "
                  "China's Kimi K2.6.",
         "domain": "models", "actor": ["minimax", "nvidia", "moonshot-ai"],
         "score": "$0.12 vs $5 per Mtok",
         "evidences": ["open-weight-latency", "reasoning-price-deflation", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-01-an-image-model-that-fits-on-a-phone"]},
        {"id": "2026-06-02-a-european-agency-gets-the-weapon",
         "title": "A European cyber agency is given access to a model officials fear",
         "claim": "Anthropic gave the EU's ENISA access to Mythos, making it the first European "
                  "agency in Project Glasswing to wield a model officials quietly fear could be "
                  "turned on the vulnerabilities of critical infrastructure.",
         "domain": "policy", "actor": ["anthropic", "enisa"],
         "evidences": ["war-reaches-the-cloud", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-05-25-central-banks-told-to-share-early-access"]},
        {"id": "2026-06-02-social-engineering-without-the-social",
         "title": "Accounts are seized by politely asking a support bot",
         "claim": "Hackers seized the Instagram accounts of the Obama White House, a Space Force "
                  "chief and Sephora just by asking Meta's support bot to swap the registered "
                  "email — the first social engineering attack where the social was optional.",
         "domain": "agents", "actor": ["meta"],
         "evidences": ["sandbox-escape", "agent-economy", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-05-29-a-side-channel-in-your-idle-drive"]},
        {"id": "2026-06-02-the-oral-tradition-may-not-survive",
         "title": "A historian warns software's oral tradition may not survive AI",
         "claim": "A historian-turned-engineer warned that the oral tradition that built "
                  "software may not survive AI, as the mentor-to-junior handoff of institutional "
                  "memory dissolves into model weights, while Microsoft stitches Copilot, chat, "
                  "Cowork and a new Autopilot agent into a single super app.",
         "domain": "society", "actor": ["microsoft"],
         "evidences": ["oral-tradition-dissolves", "deskilling", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-05-26-fabricated-references-grow-twelvefold"]},
        {"id": "2026-06-02-a-union-fences-off-the-classroom",
         "title": "A teachers' union moves to fence AI out of classrooms",
         "claim": "The American Federation of Teachers released a ten-point plan capping AI use "
                  "in classrooms and banning screens through second grade unless there is a "
                  "compelling reason.",
         "domain": "society", "actor": ["aft"],
         "evidences": ["agent-exclusion", "deskilling"],
         "supersedes": [B + "developments/2026-05-05-ai-literacy-hardwired-into-schools"]},
        {"id": "2026-06-02-one-architecture-from-rack-to-body",
         "title": "One architecture now spans rack, desk, laptop and body",
         "claim": "Nvidia named Anthropic, OpenAI and SpaceX as launch customers for its Vera "
                  "CPU, then shrank the same ambition into the DGX Station at 748 GB and 20 "
                  "petaFLOPS, the RTX Spark consumer laptop chip, and the open Isaac GR00T "
                  "reference humanoid fusing a Unitree chassis, Sharpa hands and Jetson Thor.",
         "domain": "compute", "actor": ["nvidia", "unitree"], "score": "748 GB / 20 PFLOPS",
         "evidences": ["vertical-silicon", "physical-recursion"],
         "supersedes": [B + "developments/2026-05-28-an-arm-chip-outscores-x86"]},
        {"id": "2026-06-02-eighty-billion-in-equity-as-a-tax-break-dies",
         "title": "A hyperscaler raises $80B as a state kills its datacenter tax break",
         "claim": "Alphabet is raising $80 billion in equity, including $10 billion from "
                  "Berkshire Hathaway, to fund its infrastructure buildout, even as Ohio "
                  "suspended the tax break that made it a data center magnet.",
         "domain": "economics", "actor": ["alphabet", "berkshire", "ohio"], "score": "$80B",
         "evidences": ["debt-funded-buildout", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-05-28-a-region-doubles-datacenter-fees"]},
        {"id": "2026-06-02-undersea-drones-to-guard-the-cables",
         "title": "Three navies develop undersea drones to guard data cables",
         "claim": "The US, UK and Australia are developing AUKUS undersea drones to guard the "
                  "cables and pipelines carrying the world's data and power.",
         "domain": "policy", "actor": ["uk-govt", "war-department"],
         "evidences": ["war-reaches-the-cloud", "network-over-node"],
         "supersedes": [B + "developments/2026-05-18-iran-would-charge-for-subsea-cables"]},
        {"id": "2026-06-02-an-ai-bet-dethrones-the-combustion-engine",
         "title": "An AI holding company passes an automaker as Japan's most valuable",
         "claim": "SoftBank passed Toyota to become Japan's most valuable company, ending the "
                  "automaker's twenty-year reign, while HPE revenue jumped 40% to $10.7 billion "
                  "on a 33% surge in server sales.",
         "domain": "economics", "actor": ["softbank", "toyota", "hpe"], "score": "+40% to $10.7B",
         "evidences": ["ai-as-the-economy", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-06-01-memory-is-worth-more-than-oil"]},
        {"id": "2026-06-02-two-hundred-twenty-stranded-unicorns",
         "title": "Hundreds of pre-ChatGPT startups are stranded",
         "claim": "More than 220 fallen unicorns sit stranded among hundreds of pre-ChatGPT "
                  "startups, too inflated for fresh venture money and too unprofitable for Wall "
                  "Street, while SpaceX's IPO forces index providers to rewrite their admission "
                  "rules.",
         "domain": "economics", "actor": ["spacex"], "score": "220+ fallen unicorns",
         "evidences": ["ai-as-the-economy", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-05-17-an-index-rewritten-for-one-listing"]},
        {"id": "2026-06-02-a-sovereign-wealth-fund-paid-in-lab-stock",
         "title": "A senator proposes a sovereign wealth fund paid in lab equity",
         "claim": "Bernie Sanders proposed an AI Sovereign Wealth Fund handing the public a "
                  "direct ownership stake through a one-time 50% tax paid in frontier lab "
                  "stock rather than profits.",
         "domain": "policy", "actor": ["us-congress"], "score": "50% in stock",
         "evidences": ["politics-as-infrastructure", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-01-a-lab-files-confidentially-for-an-ipo"]},
    ],
}
