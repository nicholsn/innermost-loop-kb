"""Issue 089 — 2026-04-02. Artemis II flies, and Outlook fails in orbit."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-2-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-02", "title": "Welcome to April 2, 2026", "url": URL,
        "thesis": "Humans return toward the Moon while the buildout warms the ground beneath it.",
        "body": """
# Welcome to April 2, 2026

Artemis II launched, the closest crewed approach to the Moon since Apollo, and
was photographed mid-flight from a passenger plane. Seven hours in, the
commander's Outlook inbox failed.

Underneath, a finding the corpus has been circling: land surface temperatures
rise about 2°C after a data center begins operating, producing local
microclimates researchers call the data heat island effect.
""",
    },
    "organizations": [
        {"id": "arcee-ai", "type": "Organization", "title": "Arcee AI",
         "body": "Released Trinity-Large-Thinking under a permissive licence."},
        {"id": "ikea", "type": "Organization", "title": "IKEA",
         "resource": "https://www.ikea.com/"},
        {"id": "globalstar", "type": "Organization", "title": "Globalstar",
         "resource": "https://www.globalstar.com/"},
        {"id": "r3-bio", "type": "Organization", "title": "R3 Bio",
         "body": "Pitching nonsentient organ sacks as an alternative to animal testing."},
        {"id": "paradigm-vc", "type": "Organization", "title": "Paradigm",
         "resource": "https://www.paradigm.xyz/"},
        {"id": "dol", "type": "Organization", "title": "US Department of Labor",
         "resource": "https://www.dol.gov/"},
    ],
    "developments": [
        {"id": "2026-04-02-artemis-ii-launches",
         "title": "Artemis II launches and Outlook fails seven hours in",
         "claim": "NASA's Artemis II launched from Kennedy Space Center on the closest crewed "
                  "approach to the Moon since Apollo, was photographed mid-flight from a "
                  "passenger plane, and seven hours in the commander's Outlook inbox failed.",
         "domain": "space", "actor": ["nasa"],
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-04-01-spacex-commands-97-percent-of-us-launches"]},
        {"id": "2026-04-02-spacex-files-for-the-largest-tech-listing",
         "title": "SpaceX files confidentially for the largest technology listing ever",
         "claim": "SpaceX filed confidentially for an IPO seeking a valuation above $1.75 "
                  "trillion, the largest technology listing ever, while Amazon entered talks to "
                  "acquire satellite telecom Globalstar to build its own low-orbit "
                  "constellation.",
         "domain": "economics", "actor": ["spacex", "amazon", "globalstar"], "score": "$1.75T",
         "evidences": ["compute-capital-stack", "orbit-as-compute"]},
        {"id": "2026-04-02-clone-terry-tao-a-thousand-times",
         "title": "The near-term framing shifts from superintelligence to replication",
         "claim": "Dwarkesh Patel framed the near-term implication not as superintelligence but "
                  "as replication, imagining a thousand copies of a leading mathematician each "
                  "given millions in inference and pointed at separate Millennium Prize "
                  "Problems for a hundred subjective years, while Arcee released the strongest "
                  "open model outside China at 76.3% on GPQA-D.",
         "domain": "models", "actor": ["arcee-ai"], "score": "76.3%",
         "evidences": ["automated-science", "open-weight-latency"],
         "supersedes": [B + "developments/2026-04-01-one-bit-models-ship"]},
        {"id": "2026-04-02-ikea-turns-agent-failures-into-a-consultancy",
         "title": "A retailer turns its agent's failures into a $1.2B consultancy",
         "claim": "IKEA built a customer service agent that handled requests at 57% approval, "
                  "found the 43% of failures were all people asking for design advice, launched "
                  "a consultancy to serve them and made $1.2 billion in year one, while Meta "
                  "released a model for designing concrete mixes.",
         "domain": "economics", "actor": ["ikea", "meta"], "score": "57% / $1.2B",
         "evidences": ["work-displaced", "autonomous-commerce"],
         "body": "The residue the machine could not handle turned out to be the business."},
        {"id": "2026-04-02-chinese-gpus-take-41-percent-at-home",
         "title": "Chinese accelerators take 41% of their home market",
         "claim": "Chinese GPU makers have captured nearly 41% of China's AI accelerator server "
                  "market, eroding Nvidia's once-dominant position, while Intel paid $14.2 "
                  "billion to buy back half of its Ireland plant.",
         "domain": "compute", "actor": ["china", "nvidia", "intel"], "score": "41% / $14.2B",
         "evidences": ["silicon-curtain", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-18-h200s-approved-for-china"]},
        {"id": "2026-04-02-data-heat-island-effect",
         "title": "Land temperatures rise 2°C after a datacenter opens",
         "claim": "Researchers found land surface temperatures rise 2°C on average after a data "
                  "center begins operations, inducing local microclimate zones they call the "
                  "data heat island effect.",
         "domain": "science", "score": "+2°C",
         "evidences": ["infrastructure-crowding-out", "industrialized-nature"],
         "supersedes": [B + "developments/2026-03-31-robots-assemble-gpu-racks"],
         "body": "The first measured environmental footprint of the buildout at ground level."},
        {"id": "2026-04-02-a-car-yields-to-a-delivery-robot",
         "title": "A self-driving car stops for a delivery robot",
         "claim": "Tesla FSD was recorded stopping so a small delivery robot could cross the "
                  "street, an early instance of traffic negotiation between two autonomous "
                  "systems.",
         "domain": "robotics", "actor": ["tesla"],
         "evidences": ["agent-society", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-04-01-robotaxis-sometimes-driven-by-humans"]},
        {"id": "2026-04-02-organ-sacks-and-replaceable-radiologists",
         "title": "A startup pitches nonsentient organ sacks as a testing substrate",
         "claim": "R3 Bio emerged from stealth pitching nonsentient monkey organ sacks as an "
                  "alternative to animal testing, while the chief executive of America's "
                  "largest public hospital system said he is prepared to replace radiologists "
                  "with AI once regulation allows.",
         "domain": "biotech", "actor": ["r3-bio"],
         "evidences": ["hardware-grade-biology", "work-displaced"],
         "supersedes": [B + "developments/2026-03-31-lilly-insilico-275b"]},
        {"id": "2026-04-02-shors-algorithm-at-ten-thousand-qubits",
         "title": "Shor's algorithm is shown viable at ten thousand qubits",
         "claim": "Preskill and collaborators showed Shor's algorithm can run at "
                  "cryptographically relevant scales with as few as 10,000 reconfigurable "
                  "atomic qubits, putting an expiration date on current encryption.",
         "domain": "compute", "score": "10,000 qubits",
         "evidences": ["vertical-silicon", "coordination-tax"],
         "supersedes": [B + "developments/2026-04-01-half-a-million-qubits-to-break-bitcoin"]},
        {"id": "2026-04-02-lab-diamonds-take-61-percent-of-rings",
         "title": "Lab diamonds fall 80% and take most of the ring market",
         "claim": "Lab-grown diamonds have fallen 80% in five years to under $1,000 for two "
                  "carats and now account for 61% of engagement rings, while the Labor "
                  "Department proposed opening retirement plans to crypto and private equity.",
         "domain": "economics", "actor": ["dol"], "score": "-80% / 61%",
         "evidences": ["compiling-matter", "autonomous-commerce"]},
        {"id": "2026-04-02-oracle-cuts-30000-globally",
         "title": "Oracle cuts 30,000 in a global AI restructuring",
         "claim": "Oracle cut 10,000 jobs in India as part of a global AI restructuring "
                  "affecting 30,000 employees, while OpenAI shares fell on secondary markets as "
                  "investors pivoted toward Anthropic and Paradigm began building a prediction "
                  "markets trading terminal.",
         "domain": "economics", "actor": ["oracle", "openai", "anthropic", "paradigm-vc"],
         "score": "30,000 jobs",
         "evidences": ["work-displaced", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-04-01-four-companies-take-64-percent-of-vc"]},
        {"id": "2026-04-02-europe-urges-citizens-to-drive-less",
         "title": "Europe urges citizens to stay home amid an energy crisis",
         "claim": "The European Commission is urging citizens to work from home and drive less "
                  "amid a prolonged energy crisis stemming from the Gulf conflict.",
         "domain": "energy", "actor": ["european-union"],
         "evidences": ["war-reaches-the-cloud", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-04-01-iran-seizes-starlink-terminals"]},
    ],
}
