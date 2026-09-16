"""Issue 004 — 2025-12-14. The buildout becomes geological."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-14-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-14",
        "title": "Welcome to December 14, 2025",
        "url": URL,
        "thesis": "The AI infrastructure buildout is becoming geological.",
        "body": """
# Welcome to December 14, 2025

Infrastructure at a scale that starts displacing other infrastructure: China
fusing its datacenters into one machine over a national optical backbone, US
private datacenter construction crowding out municipal projects, Europe buying
back in with fab subsidy.

The other half is stranger. MIT compiles speech into furniture and DARPA proposes
a compiler for nucleic acids — matter as a build target. The issue ends on the
Cosmist note it will return to: a model trained only on Victorian London as a
first step toward conquering time rather than space.
""",
    },

    "themes": [
        {"id": "infrastructure-crowding-out", "type": "Theme",
         "title": "Compute crowds out other infrastructure",
         "first_seen": "2025-12-14", "domain": "compute",
         "body": "The buildout stops being additive. Labor, materials and memory "
                 "flow to datacenters and away from everything else that needed them."},
        {"id": "compiling-matter", "type": "Theme", "title": "Matter as a compile target",
         "first_seen": "2025-12-14", "domain": "science",
         "body": "Fabrication reframed as compilation: an instruction at one end, "
                 "a physical or biological artifact at the other, with no craft in between."},
        {"id": "resurrection-and-time", "type": "Theme",
         "title": "Conquering time, not just space", "first_seen": "2025-12-14",
         "domain": "society",
         "body": "The Cosmist thread. Models trained to reconstitute vanished "
                 "worldviews, and the ambition — stated outright in this issue — of "
                 "resurrecting the dead."},
    ],

    "organizations": [
        {"id": "european-commission", "type": "Organization", "title": "European Commission",
         "resource": "https://commission.europa.eu/", "body": "Approved state aid for new EU fabs."},
        {"id": "mit", "type": "Organization", "title": "MIT",
         "resource": "https://www.mit.edu/", "body": "Demonstrated speech-to-reality fabrication."},
        {"id": "darpa", "type": "Organization", "title": "DARPA",
         "resource": "https://www.darpa.mil/", "body": "US defense research agency."},
        {"id": "atomic-canyon", "type": "Organization", "title": "Atomic Canyon",
         "resource": "https://atomiccanyon.com/", "body": "Nuclear-specific AI for plant licensing and operations."},
        {"id": "netflix", "type": "Organization", "title": "Netflix",
         "resource": "https://www.netflix.com/", "body": "Streaming incumbent moving into physical venues."},
        {"id": "cisco", "type": "Organization", "title": "Cisco",
         "resource": "https://www.cisco.com/", "body": "Networking incumbent; a dot-com era marker."},
    ],

    "systems": [
        {"id": "gemini-live-speech", "type": "AISystem", "title": "Gemini live speech-to-speech",
         "developed_by": [B + "organizations/google"], "modality": "speech",
         "body": "Translation that carries nuance rather than words, shipped in Google Translate."},
        {"id": "timecapsule-llm", "type": "AISystem", "title": "TimeCapsuleLLM",
         "modality": "text",
         "body": "Trained only on 1800-1875 London texts, to reconstitute a vanished worldview."},
    ],

    "facilities": [
        {"id": "china-optical-backbone", "type": "Facility", "title": "China national optical backbone",
         "operated_by": [B + "organizations/china"], "located_in": "China",
         "body": "Fuses scattered datacenters into what is described as a single national "
                 "AI supercomputer."},
        {"id": "diablo-canyon", "type": "Facility", "title": "Diablo Canyon nuclear plant",
         "located_in": "California, USA",
         "body": "Targeted to stay operational to 2030 to serve AI load."},
    ],

    "developments": [
        {"id": "2025-12-14-china-optical-backbone",
         "title": "China fuses its datacenters into one machine",
         "claim": "China activated a nationwide optical backbone that unifies scattered "
                  "data centers into a single national AI supercomputer.",
         "domain": "compute", "actor": ["china"],
         "about": [B + "facilities/china-optical-backbone"],
         "evidences": ["compute-capital-stack", "silicon-curtain"]},
        {"id": "2025-12-14-us-datacenter-construction-41b",
         "title": "US datacenter construction hits $41B annualized and displaces public works",
         "claim": "US private data center construction reached an annualized $41 billion, "
                  "absorbing enough labor and material to displace municipal infrastructure "
                  "projects.",
         "domain": "compute", "score": "$41B annualized",
         "evidences": ["infrastructure-crowding-out", "compute-capital-stack"]},
        {"id": "2025-12-14-eu-fab-aid",
         "title": "Europe approves €623M for two first-of-a-kind fabs",
         "claim": "The European Commission approved €623 million in aid for two "
                  "first-of-a-kind semiconductor fabs in Germany.",
         "domain": "policy", "actor": ["european-commission"], "score": "€623M",
         "evidences": ["silicon-curtain"]},
        {"id": "2025-12-14-google-translate-speech-nuance",
         "title": "Google Translate gains nuance-preserving speech-to-speech",
         "claim": "Google Translate began beta testing Gemini live speech-to-speech that "
                  "carries the nuance of human speech rather than only the words.",
         "domain": "models", "actor": ["google"], "about": [B + "systems/gemini-live-speech"],
         "evidences": ["intimate-interface"]},
        {"id": "2025-12-14-kindle-queryable-books",
         "title": "Amazon makes Kindle books interrogable",
         "claim": "Amazon added an AI layer to Kindle letting readers question a book "
                  "directly about plot and characters without leaving the page.",
         "domain": "society", "actor": ["amazon"], "evidences": ["intimate-interface"],
         "body": "Text stops being static and becomes a queryable database."},
        {"id": "2025-12-14-mit-speech-to-reality",
         "title": "MIT compiles spoken commands into furniture",
         "claim": "MIT researchers demonstrated a speech-to-reality system directing a "
                  "robotic arm to build furniture in five minutes.",
         "domain": "robotics", "actor": ["mit"], "score": "5 minutes",
         "evidences": ["compiling-matter"]},
        {"id": "2025-12-14-darpa-generative-optogenetics",
         "title": "DARPA proposes a nucleic acid compiler driven by light",
         "claim": "DARPA launched Generative Optogenetics, aiming at a nucleic acid compiler "
                  "that uses light to write DNA and RNA inside living cells.",
         "domain": "biotech", "actor": ["darpa"],
         "evidences": ["compiling-matter", "hardware-grade-biology"]},
        {"id": "2025-12-14-atomic-canyon-diablo-canyon",
         "title": "Nuclear-specific models are trained to keep Diablo Canyon running",
         "claim": "Atomic Canyon is using the Frontier supercomputer to train nuclear-specific "
                  "models, aiming to keep California's Diablo Canyon operational to 2030 to "
                  "serve AI load.",
         "domain": "energy", "actor": ["atomic-canyon"],
         "about": [B + "facilities/diablo-canyon"],
         "evidences": ["industrialized-nature", "infrastructure-crowding-out"]},
        {"id": "2025-12-14-fda-plausible-mechanism",
         "title": "FDA proposes approving personalized medicine without randomized trials",
         "claim": "The FDA proposed a plausible mechanism pathway to approve personalized "
                  "medicines without randomized controlled trials.",
         "domain": "policy", "actor": ["fda"], "evidences": ["legislating-the-shift"],
         "body": "Regulatory evidence shifting from statistics to mechanism — an "
                 "acknowledgement that n=1 medicine needs a different standard."},
        {"id": "2025-12-14-cisco-passes-dotcom-peak",
         "title": "Cisco passes its dot-com peak after 26 years",
         "claim": "Cisco stock surpassed its dot-com bubble peak after 26 years.",
         "domain": "economics", "actor": ["cisco"], "score": "26 years",
         "evidences": ["compute-capital-stack"],
         "body": "Offered as a lagging indicator: the physical internet finally catching "
                 "up with the expectations of 2000."},
        {"id": "2025-12-14-netflix-theme-parks",
         "title": "Netflix opens theme parks in dead department stores",
         "claim": "Netflix is opening theme parks in repurposed department stores.",
         "domain": "society", "actor": ["netflix"]},
        {"id": "2025-12-14-chatgpt-business-formation",
         "title": "ChatGPT's release is linked to a 6% rise in new business formation",
         "claim": "Research found the release of ChatGPT caused a 6% jump in new business "
                  "formation.",
         "domain": "economics", "actor": ["openai"], "score": "+6%",
         "about": [B + "systems/chatgpt"]},
        {"id": "2025-12-14-musk-aging-reversal-mrna",
         "title": "Musk predicts aging stopped and reversed via synthetic mRNA",
         "claim": "Elon Musk predicted aging will be stopped and reversed using synthetic mRNA.",
         "domain": "biotech", "evidences": ["hardware-grade-biology"]},
        {"id": "2025-12-14-reproductive-drive-lifespan",
         "title": "Suppressing reproductive drive is linked to longer life across mammals",
         "claim": "A study suggested suppressing the reproductive drive extends lifespan "
                  "across mammalian species.",
         "domain": "biotech", "evidences": ["hardware-grade-biology"]},
        {"id": "2025-12-14-timecapsule-llm-victorians",
         "title": "TimeCapsuleLLM trains only on Victorian London",
         "claim": "The TimeCapsuleLLM project is training models exclusively on 1800-1875 "
                  "London texts to reconstruct the Victorian worldview.",
         "domain": "models", "about": [B + "systems/timecapsule-llm"],
         "evidences": ["resurrection-and-time"],
         "body": "The issue reads this as a first step toward the Cosmist ambition it "
                 "closes on."},
    ],
}
