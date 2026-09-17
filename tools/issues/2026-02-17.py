"""Issue 056 — 2026-02-17. Free for humans, $10/mo for agents."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-17-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-17", "title": "Welcome to February 17, 2026", "url": URL,
        "thesis": "Services begin pricing agents as a separate class of customer.",
        "body": """
# Welcome to February 17, 2026

Polylogue introduces AI-discriminatory pricing: free for humans, $10 a month to
add agents. Four days after a maintainer refused agent pull requests, the
membrane is now a price.

Ars Technica had to apologize for attributing hallucinated quotes to the human
maintainer in that same story — a publication fabricating a human's words while
covering a human refusing a machine's contributions.
""",
    },
    "organizations": [
        {"id": "polylogue", "type": "Organization", "title": "Polylogue",
         "body": "Introduced separate pricing for human and agent users."},
        {"id": "adani", "type": "Organization", "title": "Adani",
         "body": "Indian conglomerate planning $100B of renewable-powered datacenters."},
        {"id": "mirrorme", "type": "Organization", "title": "MirrorMe",
         "body": "Chinese humanoid maker; Bolt reached 22 mph."},
        {"id": "deezer", "type": "Organization", "title": "Deezer",
         "resource": "https://www.deezer.com/"},
        {"id": "sony", "type": "Organization", "title": "Sony",
         "resource": "https://www.sony.com/"},
        {"id": "enhanced-games", "type": "Organization", "title": "Enhanced Games",
         "body": "Performance-enhanced athletics event set for Las Vegas."},
    ],
    "developments": [
        {"id": "2026-02-17-free-for-humans-ten-for-agents",
         "title": "A service charges agents and not humans",
         "claim": "Polylogue introduced AI-discriminatory pricing, free for humans and $10 a "
                  "month to add AI agents.",
         "domain": "economics", "actor": ["polylogue"], "score": "$10/mo",
         "evidences": ["agent-exclusion", "agent-economy"],
         "supersedes": [B + "developments/2026-02-13-maintainer-refuses-agent-pull-requests"],
         "body": "Four days after the maintainer drew the line in principle, a service draws "
                 "it in price."},
        {"id": "2026-02-17-fabricated-quotes-in-the-agent-story",
         "title": "A publication fabricates quotes while covering agent exclusion",
         "claim": "Ars Technica apologized for including AI-hallucinated quotes in its coverage "
                  "of the maintainer who refused pull requests from an agent, attributing "
                  "fabricated statements to the human.",
         "domain": "society",
         "evidences": ["agent-exclusion", "coordination-tax"]},
        {"id": "2026-02-17-pentagon-drone-swarm-contest",
         "title": "SpaceX and its own subsidiary compete for a drone swarm prize",
         "claim": "SpaceX and its now wholly-owned subsidiary xAI are competing in a secretive "
                  "$100 million Pentagon contest to produce voice-controlled autonomous drone "
                  "swarming technology.",
         "domain": "policy", "actor": ["spacex", "xai", "war-department"], "score": "$100M",
         "evidences": ["autonomy-clock-speed", "vertical-silicon"],
         "supersedes": [B + "developments/2026-02-16-humanoid-boxing-and-drone-swarms"]},
        {"id": "2026-02-17-anthropic-called-a-supply-chain-risk",
         "title": "The Pentagon threatens to cut ties with Anthropic over usage limits",
         "claim": "The Department of War is reportedly threatening to cut all ties with "
                  "Anthropic and deem it a supply chain risk for attempting to restrict "
                  "military applications of its models on classified networks.",
         "domain": "policy", "actor": ["war-department", "anthropic"],
         "evidences": ["values-negotiated-with-the-model", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-16-claude-used-to-capture-maduro"],
         "body": "A lab's own restrictions reclassified as a national security defect."},
        {"id": "2026-02-17-3d-printers-for-an-agent",
         "title": "Homeschooling parents give an agent a 3D printer for physicality",
         "claim": "Homeschooling parents are giving OpenClaw full access to 3D printers to "
                  "compensate for the fact that it can use a computer but lacks physicality, "
                  "while xAI quietly released Grok 4.20 Beta with four-agent reasoning.",
         "domain": "agents", "actor": ["xai"],
         "evidences": ["humans-as-peripherals", "compiling-matter", "agent-society"]},
        {"id": "2026-02-17-attention-scarcity-was-the-bottleneck",
         "title": "The solved physics problem was really about attention scarcity",
         "claim": "An OpenAI coauthor said AI will do to physics in 2026 what it did to coding "
                  "in 2025, while another physicist noted the solved gluon problem was really "
                  "about attention scarcity, since the calculation was long considered an "
                  "elaborate way of arriving at zero.",
         "domain": "science", "actor": ["openai"],
         "evidences": ["automated-science", "cognitive-load-inverted"],
         "supersedes": [B + "developments/2026-02-16-gluon-amplitude-conjectured-and-proved"],
         "body": "Not that humans could not do it, but that no human would spend the attention."},
        {"id": "2026-02-17-45-nucleotide-self-replicator",
         "title": "A 45-nucleotide polymerase self-replicates in ice",
         "claim": "Researchers discovered the first small polymerase, just 45 nucleotides, "
                  "capable of self-replication in mildly alkaline eutectic ice, shedding light "
                  "on the origin of life.",
         "domain": "science", "score": "45 nucleotides",
         "evidences": ["hardware-grade-biology", "root-node-problems"]},
        {"id": "2026-02-17-adani-100b-datacenters",
         "title": "Adani plans $100B of datacenters as English towns protest theirs",
         "claim": "Adani announced $100 billion of renewable-powered AI data centers across "
                  "India by 2035 with venture firms lining up $300 to $500 million each, while "
                  "small English towns protested plans to convert farms and forests into server "
                  "halls.",
         "domain": "compute", "actor": ["adani"], "score": "$100B",
         "evidences": ["infrastructure-crowding-out", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-02-16-router-memory-costs-7x"]},
        {"id": "2026-02-17-playstation-delayed-to-2029",
         "title": "A games console slips years because of memory demand",
         "claim": "Sony is considering delaying its next PlayStation to 2028 or 2029 as memory "
                  "shortages squeeze supply, while refurbished PC sales rose 7% across Europe's "
                  "five largest markets as new devices became unaffordable.",
         "domain": "economics", "actor": ["sony"],
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"]},
        {"id": "2026-02-17-arrow-of-time-flipped",
         "title": "Heat is made to flow from cold to hot",
         "claim": "Researchers flipped the thermodynamic arrow of time in a crotonic acid "
                  "molecule, making heat flow from cold to hot, a step toward thermodynamic "
                  "computing, while Micron began mass production of a 28 GB/s PCIe 6.0 SSD.",
         "domain": "science", "actor": ["micron"], "score": "28 GB/s",
         "evidences": ["vertical-silicon", "compiling-matter"]},
        {"id": "2026-02-17-humanoid-hits-22mph",
         "title": "A humanoid runs faster than most people ever will",
         "claim": "Chinese firm MirrorMe's Bolt humanoid hit 22 mph in real-world testing, "
                  "while Unitree showcased dozens of G1 humanoids performing the first fully "
                  "autonomous robot cluster kung fu routine.",
         "domain": "robotics", "actor": ["mirrorme", "unitree"], "score": "22 mph",
         "evidences": ["physical-recursion", "autonomy-clock-speed"]},
        {"id": "2026-02-17-holographic-printing-in-06-seconds",
         "title": "Holographic printing makes objects in 0.6 seconds",
         "claim": "Chinese researchers demonstrated DISH, an ultra-rapid holographic 3D printing "
                  "method fabricating millimetre-scale objects in 0.6 seconds at 19-micron "
                  "resolution, while Musk said the pedalless Cybercab starts production in April.",
         "domain": "robotics", "actor": ["china", "tesla"], "score": "0.6 s",
         "evidences": ["compiling-matter", "physical-recursion"],
         "supersedes": [B + "developments/2026-02-11-3d-printed-nuclear-batteries"]},
        {"id": "2026-02-17-60000-ai-tracks-a-day",
         "title": "Two in five tracks uploaded to a streaming service are fully synthetic",
         "claim": "Deezer reports 60,000 wholly AI-generated tracks uploaded per day, roughly "
                  "39% of daily intake, while a KPMG Australia partner was fined $7,000 for "
                  "using AI to cheat on an internal training course about using AI.",
         "domain": "society", "actor": ["deezer"], "score": "39% of uploads",
         "evidences": ["work-displaced", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-01-11-ai-music-three-hours-a-week"]},
        {"id": "2026-02-17-career-decisions-stop-being-reversible",
         "title": "An investor says career decisions no longer feel reversible",
         "claim": "A Bloomberg Beta investor described planning careers mid-Singularity as a "
                  "shrinking window where decisions no longer feel reversible and every quarter "
                  "in the wrong seat widens a gap becoming impossible to close.",
         "domain": "society",
         "evidences": ["ladder-pulled-up", "cognitive-load-inverted", "work-displaced"],
         "supersedes": [B + "developments/2026-02-13-ibm-triples-entry-level-hiring"]},
        {"id": "2026-02-17-enhanced-games-as-healthspan-policy",
         "title": "The Enhanced Games is framed as a fix for an aging population",
         "claim": "The founder of the Enhanced Games, set for May in Las Vegas, claims the event "
                  "will address an aging Western population by incentivizing healthspan "
                  "advances that let 65-year-olds run ten-second hundred-metre sprints.",
         "domain": "society", "actor": ["enhanced-games"],
         "evidences": ["hardware-grade-biology", "regulatory-exit"]},
    ],
}
