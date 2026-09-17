"""Issue 075 — 2026-03-13. A frozen memory comes back."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-13-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-13", "title": "Welcome to March 13, 2026", "url": URL,
        "thesis": "Memory survives being frozen solid, and neurons get racked in datacenters.",
        "body": """
# Welcome to March 13, 2026

German researchers achieved the first functional recovery of an adult mouse
hippocampus after vitrification — the first demonstration that memory can
survive being frozen solid. The corpus recorded ultrastructural preservation of
a rabbit brain in February; this is function, not just structure.

Cortical Labs is building biological data centers in Melbourne and Singapore,
powered by lab-grown human neurons on silicon.
""",
    },
    "organizations": [
        {"id": "stmicroelectronics", "type": "Organization", "title": "STMicroelectronics",
         "resource": "https://www.st.com/"},
        {"id": "motional", "type": "Organization", "title": "Motional",
         "resource": "https://motional.com/"},
        {"id": "beta-technologies", "type": "Organization", "title": "Beta Technologies",
         "resource": "https://www.beta.team/"},
        {"id": "met-museum", "type": "Organization", "title": "The Metropolitan Museum of Art",
         "resource": "https://www.metmuseum.org/"},
        {"id": "a16z", "type": "Organization", "title": "Andreessen Horowitz",
         "resource": "https://a16z.com/"},
    ],
    "developments": [
        {"id": "2026-03-13-memory-survives-vitrification",
         "title": "A frozen hippocampus recovers function",
         "claim": "German researchers achieved the first functional recovery of an adult mouse "
                  "hippocampus after cryopreservation by vitrification, the first demonstration "
                  "that memory can survive being frozen solid.",
         "domain": "biotech",
         "evidences": ["resurrection-and-time", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-07-rabbit-brain-vitrification"],
         "body": "February proved the structure survives. This proves the function does."},
        {"id": "2026-03-13-biological-datacenters",
         "title": "Data centers are built from lab-grown human neurons",
         "claim": "Cortical Labs is building the first biological data centers in Melbourne and "
                  "Singapore, powered by lab-grown human neurons on silicon, with Singapore set "
                  "to deploy up to a thousand units.",
         "domain": "compute", "actor": ["cortical-labs"], "score": "1,000 units",
         "evidences": ["hardware-grade-biology", "architecture-of-mind", "vertical-silicon"],
         "supersedes": [B + "developments/2026-02-28-neurons-learn-doom-in-a-week"]},
        {"id": "2026-03-13-alphaevolve-improves-ramsey-bounds",
         "title": "AlphaEvolve sets new lower bounds for five Ramsey numbers",
         "claim": "DeepMind used AlphaEvolve to establish new lower bounds for five classical "
                  "Ramsey numbers, an extremal combinatorics problem Erdős himself joked about "
                  "the difficulty of.",
         "domain": "science", "actor": ["google-deepmind"], "about": [B + "systems/alphaevolve"],
         "score": "5 Ramsey numbers",
         "evidences": ["automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-03-12-a-possible-open-problem-solution"]},
        {"id": "2026-03-13-palm-sized-42-tesla-magnets",
         "title": "Palm-sized coils reach 42 tesla on under a watt",
         "claim": "Swiss researchers demonstrated compact superconductor magnets reaching 42 "
                  "tesla with palm-sized coils drawing less than one watt.",
         "domain": "science", "score": "42 T / <1 W",
         "evidences": ["compiling-matter", "reasoning-price-deflation"]},
        {"id": "2026-03-13-meta-may-license-gemini",
         "title": "Meta discusses licensing a rival's model to power its own products",
         "claim": "Meta has reportedly discussed temporarily licensing Gemini to power its own "
                  "AI products after its in-house model was delayed to at least May, while Musk "
                  "expects xAI to surpass all competitors in coding by midyear after hiring two "
                  "senior Cursor leaders.",
         "domain": "models", "actor": ["meta", "google", "xai", "cursor"],
         "evidences": ["coordination-tax", "spiky-frontier"],
         "supersedes": [B + "developments/2026-03-10-microsoft-bundles-the-product-that-cost-it-220b"]},
        {"id": "2026-03-13-agents-will-outnumber-humans",
         "title": "A venture firm predicts agents outnumbering humans by orders of magnitude",
         "claim": "Andreessen Horowitz predicted agents will eventually outnumber humans by "
                  "orders of magnitude, with developers reporting that a coder is now more like "
                  "an architect than a construction worker, and Anthropic in talks with "
                  "Blackstone and others to form a venture selling Claude to portfolio "
                  "companies.",
         "domain": "economics", "actor": ["a16z", "anthropic", "blackstone"],
         "evidences": ["agent-society", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-03-09-half-of-britons-take-financial-advice-from-ai"]},
        {"id": "2026-03-13-lords-eject-hereditary-peers",
         "title": "Britain ejects hereditary peers after seven centuries",
         "claim": "Britain voted to eject hereditary aristocrats from the House of Lords after "
                  "700 years, while only half of Americans visited a cinema in 2025 and the Met "
                  "began publishing hundreds of high-resolution 3D models of iconic works.",
         "domain": "society", "actor": ["met-museum", "uk-govt"], "score": "700 years",
         "evidences": ["resurrection-and-time", "legislating-the-shift"]},
        {"id": "2026-03-13-humanoids-save-old-fabs",
         "title": "Humanoids are deployed to keep older chip fabs open",
         "claim": "STMicroelectronics unveiled plans to deploy over a hundred humanoid robots "
                  "for repetitive tasks in its older chip fabs to avoid plant closures, while "
                  "Motional relaunched robotaxis in Las Vegas and Beta Technologies partnered "
                  "in seven of eight FAA awards to fast-track flying taxis.",
         "domain": "robotics", "actor": ["stmicroelectronics", "motional", "beta-technologies"],
         "score": "100+ robots",
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-03-10-foundation-model-drives-an-excavator"]},
        {"id": "2026-03-13-humanoid-soldiers-delivered-to-ukraine",
         "title": "Armed humanoid soldiers are delivered for evaluation",
         "claim": "Phantom MK-1 humanoid soldiers brandishing firearms have been delivered to "
                  "Ukraine for evaluation.",
         "domain": "robotics", "actor": ["ukraine"],
         "evidences": ["autonomy-clock-speed", "physical-recursion"],
         "supersedes": [B + "developments/2026-03-10-directed-energy-confirmed-on-animals"]},
        {"id": "2026-03-13-smart-glasses-in-the-witness-box",
         "title": "A judge accuses a witness of being coached through smart glasses",
         "claim": "A UK High Court judge accused a man of wearing smart glasses to secretly "
                  "receive coaching while giving evidence in court.",
         "domain": "policy",
         "evidences": ["intimate-interface", "coordination-tax"],
         "body": "The oath was designed for a species with one brain at a time."},
        {"id": "2026-03-13-gut-brain-signal-routing",
         "title": "Enhancing gut-brain signaling reverses cognitive decline in mice",
         "claim": "Stanford found that enhancing gut-brain communication reversed cognitive "
                  "decline and improved memory formation in aging mice, reframing dementia as a "
                  "signal-routing problem, while China approved the world's first commercial "
                  "invasive brain-computer interface restoring hand movement.",
         "domain": "biotech", "actor": ["stanford", "china"],
         "evidences": ["hardware-grade-biology", "intimate-interface"],
         "supersedes": [B + "developments/2026-03-09-one-injection-heals-a-heart"]},
        {"id": "2026-03-13-factories-for-making-factories",
         "title": "A company builds a factory for manufacturing AI factories",
         "claim": "Crusoe announced a Spark Factory in Colorado for manufacturing modular AI "
                  "factories alongside edge zones for sovereign low-latency capacity, while "
                  "ByteDance is reportedly purchasing $2.5 billion in Nvidia Blackwell servers.",
         "domain": "compute", "actor": ["crusoe", "bytedance", "nvidia"], "score": "$2.5B",
         "evidences": ["physical-recursion", "silicon-curtain"],
         "supersedes": [B + "developments/2026-03-12-att-commits-250b"]},
        {"id": "2026-03-13-nuclear-reduction-a-strategic-mistake",
         "title": "Europe's Commission chief calls the nuclear drawdown a strategic mistake",
         "claim": "Europe's Commission chief admitted that reducing nuclear energy was a "
                  "strategic mistake.",
         "domain": "energy", "actor": ["european-union"],
         "evidences": ["burning-molecules-for-tokens", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-06-first-advanced-reactor-permit"]},
    ],
}
