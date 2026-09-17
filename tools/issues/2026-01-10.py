"""Issue 029 — 2026-01-10. Three Apollos and five Manhattans."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-10-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-10", "title": "Welcome to January 10, 2026", "url": URL,
        "thesis": "The buildout outgrows every historical comparison available.",
        "body": """
# Welcome to January 10, 2026

US AI infrastructure capex hit 1.9% of GDP in 2025 — more than three Apollos and
nearly five Manhattan Projects. The corpus has tracked this in gigawatts and
dollars; this is the first time it has a denominator.

The messy part is in the same issue: xAI was reportedly using Claude via Cursor
to build Grok until Anthropic cut off access. The frontier is close enough to
itself to be incestuous.
""",
    },
    "themes": [
        {"id": "regulatory-exit", "type": "Theme",
         "title": "Building outside the rules rather than changing them",
         "first_seen": "2026-01-10", "domain": "policy",
         "body": "Private grids outside utility regulation, company towns with their own "
                 "police, charter cities for unregulated compute, founders relocating ahead of "
                 "tax law. The response to friction is exit, not lobbying."},
    ],
    "organizations": [
        {"id": "elevenlabs", "type": "Organization", "title": "ElevenLabs",
         "resource": "https://elevenlabs.io/"},
        {"id": "sb-energy", "type": "Organization", "title": "SB Energy",
         "body": "SoftBank energy arm receiving $1B from OpenAI and SoftBank."},
        {"id": "d-wave", "type": "Organization", "title": "D-Wave",
         "resource": "https://www.dwavequantum.com/"},
        {"id": "arc-institute", "type": "Organization", "title": "Arc Institute",
         "resource": "https://arcinstitute.org/"},
        {"id": "boring-company", "type": "Organization", "title": "The Boring Company",
         "resource": "https://www.boringcompany.com/"},
    ],
    "people": [
        {"id": "jack-clark", "type": "Person", "title": "Jack Clark", "name": "Jack Clark",
         "description": "Anthropic co-founder and author of the Import AI newsletter whose January 2026 "
                        "remark put the lab on record seeing early signs of AI doing components of AI "
                        "research.",
         "resource": "https://jack-clark.net/",
         "sameAs": ["http://www.wikidata.org/entity/Q135111322"],
         "tags": ["founder"],
         "body": "Anthropic co-founder; confirmed early signs of AI improving AI research. Jack Clark "
                 "is a co-founder of [Anthropic](/organizations/anthropic.md) and writes the Import AI "
                 "newsletter. In this corpus he is the Anthropic voice in the "
                 "[early-signs statement](/developments/2026-01-10-clark-ai-doing-ai-research.md) of "
                 "January 10, 2026, reporting AI getting better at kernel development and autonomous "
                 "fine-tuning while assigning essentially zero likelihood to fully recursively "
                 "self-improving systems existing that month. The statement sits between OpenAI's "
                 "[eight-months-to-intern-researchers](/developments/2026-01-09-openai-eight-months-to-intern-researchers.md) "
                 "report and the [researchers-replaced-first](/developments/2026-01-24-researchers-replaced-first.md) "
                 "claim that superseded it."},
        {"id": "paul-graham", "type": "Person", "title": "Paul Graham", "name": "Paul Graham"},
    ],
    "roles": [
        {"id": "jack-clark-anthropic-co-founder", "type": "Role",
         "title": "Jack Clark, co-founder of Anthropic",
         "roleName": "Co-founder",
         "startDate": "2021",
         "memberOf": [B + "organizations/anthropic"],
         "holder": [B + "people/jack-clark"],
         "description": "The position in which he reported early signs of AI getting better at "
                        "components of AI research.",
         "body": "The newsletter identifies Jack Clark as an Anthropic co-founder when quoting his "
                 "January 2026 assessment "
                 "([development](/developments/2026-01-10-clark-ai-doing-ai-research.md)). Anthropic "
                 "was founded in 2021; the role is recorded from the newsletter's own attribution "
                 "rather than from a fuller biography."},
    ],
    "systems": [
        {"id": "axiomprover", "type": "AISystem", "title": "AxiomProver",
         "modality": "formal mathematics",
         "body": "Produced Lean proofs for all twelve Putnam 2025 problems."},
        {"id": "arc-stack", "type": "AISystem", "title": "Stack",
         "developed_by": [B + "organizations/arc-institute"], "modality": "single-cell",
         "body": "Virtual cell foundation model trained on 149 million cells; the first to show "
                 "in-context learning of biology."},
    ],
    "facilities": [
        {"id": "project-rainier", "type": "Facility", "title": "Project Rainier",
         "operated_by": [B + "organizations/anthropic"], "located_in": "Indiana, USA",
         "capacity": "750 MW, heading past 1 GW",
         "body": "The world's largest datacenter as of January 2026."},
    ],
    "developments": [
        {"id": "2026-01-10-capex-19pct-of-gdp",
         "title": "AI capex reaches 1.9% of US GDP",
         "claim": "US AI infrastructure capital expenditure reached 1.9% of GDP in 2025, more "
                  "than three times Apollo and nearly five times the Manhattan Project.",
         "domain": "economics", "score": "1.9% of GDP",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-01-09-atlanta-fed-doubles-forecast"]},
        {"id": "2026-01-10-clark-ai-doing-ai-research",
         "title": "Anthropic sees AI doing components of AI research",
         "claim": "Anthropic co-founder Jack Clark confirmed early signs of AI getting better at "
                  "components of AI research, from kernel development to autonomous fine-tuning.",
         "description": "A frontier-lab co-founder putting the loop on the record as an observed, "
                        "componentwise phenomenon inside a lab, naming the two layers, kernels and "
                        "fine-tuning, where the corpus's later items land.",
         "domain": "agents", "actor": ["anthropic", "people/jack-clark"],
         "occurred_on": "2026-01-09",
         "evidences": ["recursive-self-improvement"],
         "supersedes": [B + "developments/2026-01-09-openai-eight-months-to-intern-researchers"],
         "relatedTo": [B + "developments/2025-12-28-altman-self-improving-in-production",
                       B + "developments/2025-12-15-codex-babysits-own-training",
                       B + "developments/2026-01-27-amodei-country-of-geniuses-2027"],
         "tags": ["rsi", "ai-r-and-d", "kernels"],
         "supporting_text": "getting better at doing components of AI research",
         "sources": [{"id": "burry-ai-revolution-economy",
                      "resource": "https://post.substack.com/p/the-ai-revolution-is-here-will-the",
                      "title": "The AI revolution is here. Will the economy survive the transition?",
                      "author": "org:the-substack-post", "last_modified": "2026-01-09"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Writing in The Substack Post's January 9 exchange with Michael Burry "
                 "([source](https://post.substack.com/p/the-ai-revolution-is-here-will-the)), Clark "
                 "said Anthropic sees extremely early signs of AI getting better at components of AI "
                 "research, ranging from kernel development to autonomously fine-tuning open-weight "
                 "models, while assigning essentially zero likelihood to recursively self-improving "
                 "systems existing anywhere in January 2026. The newsletter reads the remark as "
                 "confirmation that the capex buildout is fueling a transition to "
                 "[recursive self-improvement](/themes/recursive-self-improvement.md); the caveat "
                 "belongs beside it. It runs in the issue after OpenAI's "
                 "[eight-months-to-intern-researchers](/developments/2026-01-09-openai-eight-months-to-intern-researchers.md) "
                 "report and two weeks after "
                 "[Altman's confirmation](/developments/2025-12-28-altman-self-improving-in-production.md) "
                 "of self-improving systems in production, and the two components Clark named are the "
                 "ones the storyline had already recorded in "
                 "[Codex babysitting its own training](/developments/2025-12-15-codex-babysits-own-training.md) "
                 "and later measures in "
                 "[a model writing the kernels it runs on](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md). "
                 "Anthropic's next entries in the storyline are "
                 "[Claude Code writing all of Claude Cowork](/developments/2026-01-13-claude-code-writes-cowork.md) "
                 "three days later and "
                 "[Amodei's remark](/developments/2026-01-27-amodei-country-of-geniuses-2027.md) on "
                 "January 27 that AI writes much of the lab's code."},
        {"id": "2026-01-10-xai-used-claude-to-build-grok",
         "title": "xAI reportedly used Claude to build Grok until cut off",
         "claim": "xAI was reportedly using Claude through Cursor to build Grok until Anthropic "
                  "revoked access.",
         "description": "The loop's messy side, in the newsletter's phrase the incestuous velocity of "
                        "the frontier: one lab's model inside a rival's development stack, and the "
                        "maker's answer being to cut the supply rather than compete on it.",
         "domain": "agents", "actor": ["xai", "anthropic"],
         "about": [B + "systems/claude", B + "systems/grok"],
         "occurred_on": "2026-01-07",
         "evidences": ["recursive-self-improvement", "coordination-tax", "no-neutral-infrastructure"],
         "relatedTo": [B + "developments/2026-01-10-grok-5-seven-trillion",
                       B + "developments/2026-01-11-x-timeline-rewrite-20pct",
                       B + "developments/2026-02-11-xai-cofounder-resigns-warning"],
         "tags": ["rsi", "ai-r-and-d"],
         "supporting_text": "using Claude via Cursor to build Grok",
         "sources": [{"id": "robison-xai-anthropic-cursor-cutoff",
                      "resource": "https://x.com/kyliebytes/status/2009686466746822731",
                      "title": "Kylie Robison on X: xAI staff used Anthropic's models through Cursor until Anthropic cut off access",
                      "author": "human:kylie-robison", "last_modified": "2026-01-09"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The frontier is now close enough to itself that labs build rivals with each "
                 "other's models. Kylie Robison's scoop of January 9 "
                 "([X](https://x.com/kyliebytes/status/2009686466746822731)) reported that xAI staff "
                 "had been using Anthropic's models internally through [Cursor](/organizations/cursor.md) "
                 "until Anthropic cut off the startup's access that week, a change xAI co-founder Tony "
                 "Wu relayed to staff by internal message on Wednesday, January 7. It is the corpus's "
                 "first instance of the "
                 "recursion crossing a lab boundary, [Claude](/systems/claude.md) in the loop that "
                 "builds [Grok](/systems/grok.md), and the first of a supplier withdrawing model access "
                 "from a competitor, the pattern the "
                 "[no-neutral-infrastructure](/themes/no-neutral-infrastructure.md) theme later names. "
                 "It lands in the same issue as "
                 "[Grok 5's seven trillion parameters](/developments/2026-01-10-grok-5-seven-trillion.md) "
                 "and a day before xAI's "
                 "[rewrite of the X timeline](/developments/2026-01-11-x-timeline-rewrite-20pct.md); an "
                 "[xAI co-founder's resignation warning](/developments/2026-02-11-xai-cofounder-resigns-warning.md) "
                 "of live loops within a year follows a month later."},
        {"id": "2026-01-10-grok-5-seven-trillion",
         "title": "Grok 5 is a seven-trillion-parameter model",
         "claim": "Jensen Huang revealed Grok 5 will have seven trillion parameters, while "
                  "DeepSeek V4 is launching with internal benchmarks reportedly beating Claude "
                  "and GPT at coding.",
         "domain": "models", "actor": ["xai", "nvidia", "deepseek"], "score": "7T parameters",
         "evidences": ["silicon-curtain", "spiky-frontier"],
         "supersedes": [B + "developments/2026-01-07-vercel-model-chess"]},
        {"id": "2026-01-10-axiomprover-12-of-12-putnam",
         "title": "A prover solves all twelve Putnam problems in Lean",
         "claim": "AxiomProver produced formal Lean proofs solving all twelve Putnam 2025 "
                  "competition problems nearly instantly.",
         "domain": "science", "about": [B + "systems/axiomprover"], "score": "12/12",
         "evidences": ["automated-science", "benchmark-saturation"],
         "supersedes": [B + "developments/2025-12-20-seed-prover-putnam"]},
        {"id": "2026-01-10-scribe-v2-fleurs",
         "title": "Speech-to-text reaches 95.7% on FLEURS",
         "claim": "ElevenLabs released Scribe v2 scoring 95.7% on FLEURS, while Google began "
                  "discouraging site owners from chunking content to feed Gemini instead of "
                  "human readers.",
         "domain": "models", "actor": ["elevenlabs", "google"], "score": "95.7%",
         "evidences": ["intimate-interface", "coordination-tax"]},
        {"id": "2026-01-10-project-rainier-750mw",
         "title": "Project Rainier becomes the world's largest datacenter",
         "claim": "Epoch AI identified Anthropic's Project Rainier in Indiana as the world's "
                  "largest data center at 750 MW and heading past a gigawatt.",
         "domain": "compute", "actor": ["anthropic", "epoch-ai"],
         "about": [B + "facilities/project-rainier"], "score": "750 MW",
         "evidences": ["compute-capital-stack", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-01-09-xai-macrohardrr"]},
        {"id": "2026-01-10-openai-softbank-sb-energy",
         "title": "OpenAI and SoftBank put $1B into SB Energy",
         "claim": "OpenAI and SoftBank are investing $1 billion in SB Energy for a US power "
                  "buildout.",
         "domain": "energy", "actor": ["openai", "softbank", "sb-energy"], "score": "$1B",
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-01-10-data-act-private-grids",
         "title": "The DATA Act would let datacenters build private grids",
         "claim": "Senator Cotton introduced the DATA Act, allowing data center owners to build "
                  "private power plants and grids outside public utility regulation.",
         "domain": "policy", "actor": ["us-congress"],
         "evidences": ["regulatory-exit", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-07-pjm-bring-your-own-power"]},
        {"id": "2026-01-10-dwave-acquires-quantum-circuits",
         "title": "D-Wave buys Quantum Circuits for $550M",
         "claim": "D-Wave is acquiring Quantum Circuits for $550 million to merge annealing and "
                  "gate-model quantum computing, as Intel confirmed 14A production for 2027 "
                  "with backside power delivery.",
         "domain": "compute", "actor": ["d-wave", "intel"], "score": "$550M",
         "evidences": ["vertical-silicon"]},
        {"id": "2026-01-10-graham-orbital-datacenters-inevitable",
         "title": "Paul Graham calls orbital datacenters inevitable",
         "claim": "Paul Graham declared orbital AI data centers inevitable and one of the "
                  "biggest engineering projects of the era, as the FCC approved doubling "
                  "Starlink Gen2 to 15,000 satellites.",
         "domain": "space", "actor": ["people/paul-graham", "spacex", "fcc"], "score": "15,000 satellites",
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-01-08-ark-100-launches-a-day"]},
        {"id": "2026-01-10-starbase-police-department",
         "title": "Starbase creates its own police department",
         "claim": "Starbase, Texas is standing up its own police department, a template for "
                  "company-town governance.",
         "domain": "policy", "actor": ["spacex"],
         "evidences": ["regulatory-exit", "politics-as-infrastructure"]},
        {"id": "2026-01-10-artemis-ii-february-6-941pm",
         "title": "Artemis II gets a launch time",
         "claim": "The Artemis II launch window opens February 6 at 9:41pm ET.",
         "domain": "space", "actor": ["nasa"], "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-01-03-artemis-ii-february-6"]},
        {"id": "2026-01-10-arc-stack-in-context-biology",
         "title": "A virtual cell model learns biology in context",
         "claim": "The Arc Institute unveiled Stack, a virtual cell foundation model trained on "
                  "149 million cells that simulates cellular responses to perturbations without "
                  "fine-tuning.",
         "domain": "biotech", "actor": ["arc-institute"], "about": [B + "systems/arc-stack"],
         "score": "149M cells",
         "evidences": ["hardware-grade-biology", "data-beyond-text", "automated-science"],
         "supersedes": [B + "developments/2026-01-08-universal-virtual-cell-model"],
         "body": "Few-shot learning arriving a second time, in wetware."},
        {"id": "2026-01-10-drugclip-10m-times-faster",
         "title": "DrugCLIP screens ten million times faster than docking",
         "claim": "Chinese researchers introduced DrugCLIP, a contrastive framework screening "
                  "molecules ten million times faster than traditional docking, as Eli Lilly "
                  "signed a biologics design deal with Chai Discovery.",
         "domain": "biotech", "actor": ["eli-lilly", "chai-discovery"], "score": "10^7 speedup",
         "evidences": ["automated-science", "discovery-as-process"]},
        {"id": "2026-01-10-vegas-loop-million-cubic-yards",
         "title": "The Vegas Loop pours a million cubic yards of concrete",
         "claim": "The Boring Company's Vegas Loop is using a million cubic yards of concrete to "
                  "stabilize its autonomous tunnel network, possibly the largest active US "
                  "infrastructure project.",
         "domain": "robotics", "actor": ["boring-company"], "score": "1M cubic yards",
         "evidences": ["physical-recursion", "autonomous-commerce"]},
        {"id": "2026-01-10-california-drought-free",
         "title": "California is drought-free for the first time in 25 years",
         "claim": "For the first time in 25 years not a single square mile of California is in "
                  "drought, even as Sergey Brin reportedly joins Larry Page in leaving the state "
                  "over retroactive wealth taxes.",
         "domain": "society", "evidences": ["regulatory-exit", "industrialized-nature"],
         "supersedes": [B + "developments/2026-01-08-page-leaves-california"]},
    ],
}
