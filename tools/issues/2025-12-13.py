"""Issue 003 — 2025-12-13. Autonomy gets a clock speed."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-13-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-13",
        "title": "Welcome to December 13, 2025",
        "url": URL,
        "thesis": "The clock speed of autonomy is accelerating.",
        "body": """
# Welcome to December 13, 2025

The third edition finds a better unit than accuracy: **how long a model can run
unsupervised**. Epoch AI puts Gemini 3 Pro at a 4.9-hour autonomous horizon, and
the extrapolated doubling time at roughly a month — which, if it holds, is what
makes annual roadmaps meaningless.

The second claim cuts against the first. Zoom's federated swarm of small open and
closed models beats the monolith it is assembled from. Capability stops being a
property of the best model and becomes a property of the arrangement — the same
move as issue 002's scaffolding argument, now at the level of the network.

Underneath, science is being *institutionalized* rather than merely automated:
new agency-funded lab structures, a national discovery platform, and a Fields
medallist describing himself as human-in-the-loop.

It closes on **the Solar System finally has a business model**.
""",
    },

    "themes": [
        {"id": "autonomy-clock-speed", "type": "Theme",
         "title": "Autonomy has a clock speed", "first_seen": "2025-12-13", "domain": "agents",
         "body": "The tracked quantity becomes how long a system runs unsupervised "
                 "before a human must intervene, and how fast that horizon doubles. "
                 "It converts capability into a rate, and a rate into a planning "
                 "horizon."},
        {"id": "network-over-node", "type": "Theme",
         "title": "The network beats the node", "first_seen": "2025-12-13", "domain": "agents",
         "body": "An orchestrated swarm of smaller models outscores the single best "
                 "model it contains. Capability becomes a property of the "
                 "arrangement rather than the checkpoint — the scaffolding argument "
                 "raised to the level of the network."},
        {"id": "silicon-curtain", "type": "Theme",
         "title": "A silicon curtain falls", "first_seen": "2025-12-13", "domain": "policy",
         "body": "Semiconductors stop being traded and start being aligned. Blocs "
                 "form around the whole stack, from minerals to logic, and subsidy "
                 "becomes the instrument of decoupling."},
        {"id": "science-as-industrial-policy", "type": "Theme",
         "title": "Science as industrial policy", "first_seen": "2025-12-13", "domain": "science",
         "body": "Discovery is not only automated but reorganized: new institutional "
                 "forms outside the university, funded as national infrastructure "
                 "and justified by productivity targets."},
        {"id": "hardware-grade-biology", "type": "Theme",
         "title": "Biology engineered past the constraints of life",
         "first_seen": "2025-12-13", "domain": "biotech",
         "body": "Designed proteins that hold structure at temperatures and forces "
                 "no organism tolerates. Biochemistry becomes a materials science "
                 "rather than a study of the living."},
    ],

    "people": [
        {"id": "terry-tao", "type": "Person", "title": "Terence Tao", "name": "Terence Tao",
         "resource": "https://terrytao.wordpress.com/",
         "body": "Mathematician. His account of solving an Erdős problem with machine "
                 "assistance is the issue's sharpest evidence that the unit of "
                 "discovery is shifting from the individual to the loop."},
    ],

    "organizations": [
        {"id": "zoom", "type": "Organization", "title": "Zoom",
         "resource": "https://zoom.us/", "body": "Deployed a federated multi-model swarm."},
        {"id": "nsf", "type": "Organization", "title": "National Science Foundation",
         "resource": "https://www.nsf.gov/", "body": "US federal science funder."},
        {"id": "doe", "type": "Organization", "title": "US Department of Energy",
         "resource": "https://www.energy.gov/",
         "body": "Funds national laboratories and, here, a national discovery platform."},
        {"id": "unitree", "type": "Organization", "title": "Unitree",
         "resource": "https://www.unitree.com/", "body": "Humanoid and quadruped robot maker."},
        {"id": "thinking-machines", "type": "Organization", "title": "Thinking Machines Lab",
         "resource": "https://thinkingmachines.ai/",
         "body": "Mira Murati's lab; ships Tinker for fine-tuning."},
        {"id": "youtube", "type": "Organization", "title": "YouTube",
         "resource": "https://www.youtube.com/", "body": "Creator platform; added stablecoin payouts."},
        {"id": "el-salvador", "type": "Organization", "title": "Government of El Salvador",
         "resource": "https://www.presidencia.gob.sv/",
         "body": "Partnered to put Grok tutoring in every public school."},
        {"id": "uatx", "type": "Organization", "title": "University of Austin (UATX)",
         "resource": "https://uaustin.org/", "body": "Building an applied engineering lab beside SpaceX."},
        {"id": "commonwealth-fusion", "type": "Organization", "title": "Commonwealth Fusion Systems",
         "resource": "https://cfs.energy/", "body": "Tokamak developer building a commercial demo plant."},
        {"id": "china", "type": "Organization", "title": "Government of China",
         "description": "The People's Republic of China's government as a policy actor: subsidising a decoupled chip industry and standing behind the corpus's Chinese hardware, robotics and energy items.",
         "resource": "https://english.www.gov.cn/",
         "sameAs": ["http://www.wikidata.org/entity/Q936190"],
         "tags": ["government", "state"],
         "body": "Countering export controls with domestic semiconductor subsidy. It enters the corpus with the "
                 "[$70 billion chip subsidy package](/developments/2025-12-13-china-70b-chip-subsidy.md), the same-day "
                 "counter to the US [Pax Silica Initiative](/developments/2025-12-13-pax-silica-initiative.md), followed by "
                 "a [Manhattan Project-style effort in Shenzhen to reverse-engineer EUV lithography](/developments/2025-12-18-shenzhen-euv-manhattan-project.md) "
                 "and a policy of [restricting domestic purchases to force reliance on local silicon](/developments/2026-01-14-h200-allowed-china-restricts.md). "
                 "In the recursive-self-improvement strand it is context rather than actor: the "
                 "[silicon curtain](/themes/silicon-curtain.md) that decides where the loop's compute can be built."},
        {"id": "japan", "type": "Organization", "title": "Government of Japan",
         "resource": "https://www.japan.go.jp/", "body": "Pax Silica partner."},
        {"id": "uae", "type": "Organization", "title": "Government of the UAE",
         "resource": "https://u.ae/", "body": "Pax Silica partner."},
    ],

    "systems": [
        {"id": "gemini-3-pro", "type": "AISystem", "title": "Gemini 3 Pro",
         "developed_by": [B + "organizations/google"], "modality": "text",
         "evaluated_on": [B + "benchmarks/autonomous-time-horizon",
                          B + "benchmarks/humanitys-last-exam"],
         "body": "Reported holding the state of the art autonomous time horizon."},
        {"id": "federated-ai", "type": "AISystem", "title": "Zoom Federated AI",
         "developed_by": [B + "organizations/zoom"], "modality": "model swarm",
         "evaluated_on": [B + "benchmarks/humanitys-last-exam"],
         "body": "A swarm of small open and closed models orchestrated together, "
                 "reported beating the best single model it contains."},
        {"id": "gemini-2-5-flash", "type": "AISystem", "title": "Gemini 2.5 Flash",
         "developed_by": [B + "organizations/google"], "modality": "speech",
         "body": "Updated with native audio for voice workflows."},
        {"id": "alphaevolve", "type": "AISystem", "title": "AlphaEvolve",
         "description": "DeepMind's Gemini-powered evolutionary coding agent, which pairs model-proposed program changes with automated evaluators to discover algorithms, bounds and training components.",
         "developed_by": [B + "organizations/google-deepmind"], "modality": "code",
         "resource": "https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/",
         "sameAs": ["http://www.wikidata.org/entity/Q134463401"],
         "tags": ["evolutionary-search", "research-agent"],
         "body": "Evolutionary search over algorithms and proofs: Gemini models propose changes to a program, "
                 "automated evaluators score them, and the strongest candidates seed the next generation "
                 "([DeepMind](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)). "
                 "In this corpus it first appears as Terence Tao's collaborator on an open "
                 "[Erdős problem](/developments/2025-12-13-tao-erdos-1026.md); it then "
                 "[discovers an activation function that triples ReLU](/developments/2026-02-08-alphaevolve-finds-new-activations.md), "
                 "the point at which the search loop turns on the components of the models that drive it, and "
                 "[establishes new lower bounds for five Ramsey numbers](/developments/2026-03-13-alphaevolve-improves-ramsey-bounds.md)."},
        {"id": "veo", "type": "AISystem", "title": "Veo",
         "developed_by": [B + "organizations/google-deepmind"], "modality": "video",
         "body": "Video generator repurposed as a simulator for evaluating robot policies."},
        {"id": "tinker", "type": "AISystem", "title": "Tinker",
         "developed_by": [B + "organizations/thinking-machines"], "modality": "fine-tuning",
         "body": "Lowers the cost of adapting existing weights — scaffolding sold as a product."},
    ],

    "benchmarks": [
        {"id": "autonomous-time-horizon", "type": "Benchmark", "title": "Autonomous time horizon",
         "published_by": [B + "organizations/epoch-ai"],
         "measures_capability": "how long a model works unsupervised before needing intervention",
         "body": "A duration rather than a score, which is why the corpus can read a "
                 "doubling time off it."},
        {"id": "humanitys-last-exam", "type": "Benchmark", "title": "Humanity's Last Exam",
         "measures_capability": "expert-level questions across many disciplines",
         "body": "Built to resist saturation by frontier models."},
    ],

    "facilities": [
        {"id": "cfs-demo-plant", "type": "Facility", "title": "Commonwealth Fusion demo plant",
         "operated_by": [B + "organizations/commonwealth-fusion"],
         "located_in": "near Boston, Massachusetts, USA", "capacity": "75% complete",
         "body": "Net-energy fusion moving from a physics problem to a construction schedule."},
        {"id": "american-science-security-platform", "type": "Facility",
         "title": "American Science and Security Platform",
         "operated_by": [B + "organizations/doe"], "located_in": "United States",
         "capacity": "$320M",
         "body": "An American Science Cloud plus a Transformational AI Models "
                 "Consortium, aimed at doubling national scientific productivity "
                 "within a decade."},
        {"id": "uatx-applied-engineering-lab", "type": "Facility",
         "title": "UATX Applied Engineering Lab",
         "operated_by": [B + "organizations/uatx"], "located_in": "Texas, USA",
         "body": "Sited next to SpaceX to feed talent straight into the hard-tech base."},
        {"id": "mars-ai-datacenter", "type": "Facility", "title": "Mars AI datacenter (planned)",
         "operated_by": [B + "organizations/blue-origin"], "located_in": "Mars",
         "body": "Announced for 2028. The furthest extension yet of the orbit-as-compute thread."},
    ],

    "developments": [
        {"id": "2025-12-13-autonomy-time-horizon-sota",
         "title": "Gemini 3 Pro reaches a 4.9-hour autonomous horizon",
         "claim": "Epoch AI extrapolates a state-of-the-art autonomous time horizon of 4.9 "
                  "hours for Gemini 3 Pro, with GPT-5.2 at 3.5 hours.",
         "domain": "agents", "actor": ["epoch-ai", "google"], "score": "4.9 h (GPT-5.2: 3.5 h)",
         "about": [B + "systems/gemini-3-pro", B + "benchmarks/autonomous-time-horizon"],
         "evidences": ["autonomy-clock-speed"]},
        {"id": "2025-12-13-autonomy-doubling-one-month",
         "title": "Autonomous capability is estimated to double monthly",
         "claim": "Some analysts estimate the doubling time for autonomous capability has "
                  "fallen to roughly one month, making annual roadmaps obsolete.",
         "domain": "agents", "actor": ["epoch-ai"], "score": "~1 month doubling",
         "evidences": ["autonomy-clock-speed", "reasoning-price-deflation"],
         "body": "A rate claim, and the reason the issue treats planning horizons rather "
                 "than capabilities as the thing under threat."},
        {"id": "2025-12-13-zoom-federated-swarm-hle",
         "title": "Zoom's federated swarm beats the monolith on Humanity's Last Exam",
         "claim": "Zoom deployed Federated AI, a swarm of small open and closed models that "
                  "scored 48.1% on Humanity's Last Exam, beating Gemini 3 Pro.",
         "domain": "agents", "actor": ["zoom"], "score": "48.1%",
         "about": [B + "systems/federated-ai", B + "benchmarks/humanitys-last-exam"],
         "evidences": ["network-over-node", "scaffolding-over-weights"],
         "body": "The arrangement outperforming its best component is the strongest form "
                 "of issue 002's scaffolding claim so far."},
        {"id": "2025-12-13-gemini-flash-native-audio",
         "title": "Gemini 2.5 Flash gains native audio",
         "claim": "Google updated Gemini 2.5 Flash with native audio so agents can handle "
                  "complex voice workflows.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/gemini-2-5-flash"],
         "evidences": ["intimate-interface"]},
        {"id": "2025-12-13-nsf-tech-labs",
         "title": "NSF launches Tech Labs as a new research institution",
         "claim": "The National Science Foundation launched Tech Labs, independent research "
                  "organizations aimed at technical bottlenecks universities cannot address.",
         "domain": "science", "actor": ["nsf"], "evidences": ["science-as-industrial-policy"]},
        {"id": "2025-12-13-doe-science-security-platform",
         "title": "DOE commits $320M to a national discovery platform",
         "claim": "The Department of Energy backed the American Science and Security Platform "
                  "with $320 million, combining an American Science Cloud and a "
                  "Transformational AI Models Consortium to double national scientific "
                  "productivity within a decade.",
         "domain": "science", "actor": ["doe"], "score": "$320M",
         "about": [B + "facilities/american-science-security-platform"],
         "evidences": ["science-as-industrial-policy", "automated-science"]},
        {"id": "2025-12-13-tao-erdos-1026",
         "title": "Terence Tao solves Erdős #1026 with machine assistance",
         "claim": "Terence Tao reported that he and collaborators solved Erdős problem #1026 "
                  "using AlphaEvolve combined with deep literature search.",
         "domain": "science", "actor": ["people/terry-tao", "google-deepmind"],
         "about": [B + "systems/alphaevolve"],
         "evidences": ["automated-science", "scaffolding-over-weights"],
         "body": "The issue's framing — the lone genius becoming human-in-the-loop — is a "
                 "claim about where mathematical credit now sits."},
        {"id": "2025-12-13-pax-silica-initiative",
         "title": "The US launches a Pax Silica Initiative",
         "claim": "The US launched a Pax Silica Initiative to secure the semiconductor stack "
                  "from minerals to logic, with allies including Japan and the UAE.",
         "domain": "policy", "actor": ["white-house", "japan", "uae"],
         "evidences": ["silicon-curtain", "vertical-silicon"]},
        {"id": "2025-12-13-china-70b-chip-subsidy",
         "title": "China answers with a $70B chip subsidy package",
         "claim": "China announced a $70 billion subsidy package to decouple its chip "
                  "industry from the West.",
         "domain": "policy", "actor": ["china"], "score": "$70 billion",
         "evidences": ["silicon-curtain"]},
        {"id": "2025-12-13-veo-evaluates-robot-policies",
         "title": "DeepMind uses Veo to evaluate robot policies",
         "claim": "DeepMind showed Veo can evaluate robotic policies, letting robots simulate "
                  "scenarios before acting.",
         "domain": "robotics", "actor": ["google-deepmind"], "about": [B + "systems/veo"],
         "evidences": ["inhabitable-worlds"],
         "body": "The world model from issue 002 turned into a test harness for embodiment."},
        {"id": "2025-12-13-unitree-humanoid-app-store",
         "title": "Unitree opens the first humanoid app store",
         "claim": "Unitree launched the first humanoid app store, making physical skills "
                  "distributable software.",
         "domain": "robotics", "actor": ["unitree"],
         "body": "Skills become a distribution problem rather than a research one."},
        {"id": "2025-12-13-tesla-grok-fsd-navigation",
         "title": "Tesla lets Grok drive FSD navigation",
         "claim": "Tesla's holiday update lets users ask Grok to handle Full Self-Driving "
                  "navigation.",
         "domain": "robotics", "actor": ["tesla", "xai"], "about": [B + "systems/grok"]},
        {"id": "2025-12-13-thermostable-designed-proteins",
         "title": "Designed proteins hold structure above 150°C",
         "claim": "Researchers used AI to design proteins that keep their structure above "
                  "150°C and resist extreme physical forces.",
         "domain": "biotech", "score": ">150°C", "evidences": ["hardware-grade-biology"]},
        {"id": "2025-12-13-rats-play-doom-vr",
         "title": "Rats play DOOM in a VR rig",
         "claim": "Hungarian researchers enabled rats to play DOOM in VR using a full "
                  "motion-tracking setup.",
         "domain": "biotech", "evidences": ["biosphere-uplift"],
         "body": "Read by the issue as a primitive uplift: a biological network wired "
                 "into a digital loop."},
        {"id": "2025-12-13-altman-enterprise-2026",
         "title": "OpenAI makes enterprise sales the 2026 priority",
         "claim": "Sam Altman confirmed enterprise sales are OpenAI's priority for 2026.",
         "domain": "economics", "actor": ["openai"], "evidences": ["compute-capital-stack"]},
        {"id": "2025-12-13-tinker-democratizes-finetuning",
         "title": "Thinking Machines releases Tinker for fine-tuning",
         "claim": "Mira Murati's Thinking Machines released Tinker to make fine-tuning widely "
                  "accessible.",
         "domain": "models", "actor": ["thinking-machines"], "about": [B + "systems/tinker"],
         "evidences": ["scaffolding-over-weights"]},
        {"id": "2025-12-13-youtube-stablecoin-payouts",
         "title": "YouTube lets creators cash out in stablecoins",
         "claim": "YouTube now allows creators to take payouts in stablecoins.",
         "domain": "economics", "actor": ["youtube"]},
        {"id": "2025-12-13-xai-el-salvador-tutoring",
         "title": "xAI puts Grok tutoring in every El Salvador public school",
         "claim": "xAI partnered with El Salvador to bring Grok-powered tutoring to every "
                  "public school student.",
         "domain": "society", "actor": ["xai", "el-salvador"], "about": [B + "systems/grok"],
         "evidences": ["intimate-interface"]},
        {"id": "2025-12-13-uatx-applied-engineering-lab",
         "title": "UATX builds an engineering lab next to SpaceX",
         "claim": "UATX is building an Applied Engineering Lab beside SpaceX to pipeline "
                  "talent into the hard-tech industrial base.",
         "domain": "society", "actor": ["uatx"],
         "about": [B + "facilities/uatx-applied-engineering-lab"],
         "evidences": ["science-as-industrial-policy"]},
        {"id": "2025-12-13-cfs-demo-75-percent",
         "title": "Commonwealth Fusion's demo plant is 75% complete",
         "claim": "Commonwealth Fusion Systems' commercial demonstration site near Boston is "
                  "75% complete.",
         "domain": "energy", "actor": ["commonwealth-fusion"], "score": "75% complete",
         "about": [B + "facilities/cfs-demo-plant"],
         "evidences": ["industrialized-nature"],
         "body": "Fusion described as a construction schedule rather than a physics result."},
        {"id": "2025-12-13-starlink-10000-satellites",
         "title": "Starlink heads for 10,000 satellites by February",
         "claim": "SpaceX is on track to have 10,000 Starlink satellites in orbit by February.",
         "domain": "space", "actor": ["spacex"], "score": "10,000 satellites",
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2025-12-11-starlink-100kw-compute"]},
        {"id": "2025-12-13-blue-origin-mars-datacenter",
         "title": "Blue Origin plans a Mars AI datacenter for 2028",
         "claim": "Blue Origin plans to deploy an AI data center to Mars in 2028.",
         "domain": "space", "actor": ["blue-origin"],
         "about": [B + "facilities/mars-ai-datacenter"],
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2025-12-11-blue-origin-space-datacenters"],
         "body": "Two days after forming a space-datacenter team, the stated target is "
                 "another planet."},
    ],
}
