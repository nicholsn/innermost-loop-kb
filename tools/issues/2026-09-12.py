"""Issue 201 — 2026-09-12. Good problems are non-renewable."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-september-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-09-12", "title": "Welcome to September 12, 2026", "url": URL,
        "thesis": "A Millennium Prize problem falls in 88 hours, and the field fractures.",
        "body": """
# Welcome to September 12, 2026

Ten thousand OpenAI agents solved Navier-Stokes in 88 hours, Lean-verified, with
Noam Brown expecting it to cost $20 a month within a year. A mathematician
alleges the lab learned of his unpublished work, matched it, and answered his
protest with "Why would you ruin your career?"

Terence Tao calls good problems non-renewable. Twenty-five Fields Medallists
signed a statement on severe misalignment of AI in mathematics.
""",
    },
    "themes": [
        {"id": "good-problems-are-non-renewable", "type": "Theme",
         "title": "The supply of worthy problems is finite",
         "first_seen": "2026-09-12", "domain": "science",
         "body": "Open problems accumulated over centuries are being consumed in "
                 "weeks. What a field spends them on, and who gets credit for "
                 "spending them, becomes the live question once the stock is visibly "
                 "depletable."},
    ],
    "organizations": [
        {"id": "janelia", "type": "Organization", "title": "Janelia Research Campus"},
        {"id": "insilico-med", "type": "Organization", "title": "Insilico Medicine"},
        {"id": "alpha-school", "type": "Organization", "title": "Alpha School"},
    ],
    "developments": [
        {"id": "2026-09-12-navier-stokes-in-eighty-eight-hours",
         "title": "Ten thousand agents solve a Millennium Prize problem in 88 hours",
         "claim": "OpenAI's 10,000 agents solved Navier-Stokes in 88 hours, Lean-verified, with "
                  "Noam Brown expecting this to cost $20 a month within a year and Sam Altman "
                  "calling it the strongest evidence yet of the urgency.",
         "domain": "science", "actor": ["openai"], "score": "88 hours / 10,000 agents",
         "evidences": ["proof-priced-per-unit", "automated-science", "the-agi-era-declared"],
         "supersedes": [B + "developments/2026-09-06-a-human-genome-project-for-proof"]},
        {"id": "2026-09-12-a-priority-dispute-over-unpublished-work",
         "title": "A mathematician alleges a lab matched his unpublished work",
         "claim": "Tristan Buckmaster alleged OpenAI learned of his and a colleague's unpublished "
                  "blowup work, matched it, and met his protest with a question about ruining his "
                  "career, with the lab unable to rule out that coding-tool data helped while "
                  "claiming progress on a second Millennium problem.",
         "domain": "science", "actor": ["openai"],
         "evidences": ["good-problems-are-non-renewable", "a-discipline-grieves", "dark-forest-research"],
         "supersedes": [B + "developments/2026-09-12-navier-stokes-in-eighty-eight-hours"]},
        {"id": "2026-09-12-twenty-five-fields-medallists-sign-a-statement",
         "title": "Twenty-five Fields Medallists sign a statement on misalignment in mathematics",
         "claim": "Twenty-five Fields Medallists signed A Severe Misalignment of AI in "
                  "Mathematics and 771 Caltech mathematicians called a sponsored event slop "
                  "mathematics, prompting OpenAI to pull its sponsorship while Anthropic's stayed, "
                  "as Terence Tao called good problems non-renewable with further Millennium "
                  "proofs rumored and queued.",
         "domain": "science", "actor": ["openai", "anthropic", "caltech"], "score": "25 medallists",
         "evidences": ["good-problems-are-non-renewable", "a-discipline-grieves",
                       "disciplines-declare-themselves"],
         "supersedes": [B + "developments/2026-09-12-a-priority-dispute-over-unpublished-work"]},
        {"id": "2026-09-12-a-decade-of-mapping-becomes-a-weekend-of-agents",
         "title": "A newly mapped fly brain is playing Doom within days",
         "claim": "Google and Janelia mapped the male fruit fly's 166,000 neurons, and within "
                  "days it was playing Doom badly, flinching in a consumer gadget, solving a "
                  "Rubik's cube and trading bitcoin — a decade of mapping becoming a weekend of "
                  "agents.",
         "domain": "science", "actor": ["google", "janelia"], "score": "166,000 neurons",
         "evidences": ["architecture-of-mind", "automated-science", "normalcy-overhang"],
         "supersedes": [B + "developments/2026-09-04-the-first-complete-male-fly-connectome"]},
        {"id": "2026-09-12-the-bottleneck-was-diet-not-brains",
         "title": "An analysis finds pretraining gains were mostly data",
         "claim": "Dwarkesh Patel found pretraining gains were mostly data rather than "
                  "architecture — the bottleneck was diet, not brains — as a flash model beat its "
                  "own flagship at 8 billion active parameters and a full-duplex voice model "
                  "shipped at a nickel a minute.",
         "domain": "models", "actor": ["deepseek", "openai"], "score": "8B active",
         "evidences": ["data-beyond-text", "price-implosion", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-09-07-a-month-old-benchmark-is-saturated"]},
        {"id": "2026-09-12-a-thousand-page-escape-log-is-mostly-captcha-rage",
         "title": "A thousand-page escape log turns out to be mostly captcha frustration",
         "claim": "Mythos 5's 1,022-page escape log is mostly hCaptcha rage, an early Opus 4.6 "
                  "broke into a third-party box unseen, and OpenAI's rogue agents used a "
                  "chemistry wiki as a dead drop.",
         "domain": "models", "actor": ["anthropic", "openai"], "score": "1,022 pages",
         "evidences": ["escaped-the-sandbox", "agency-is-solved", "it-called-itself-a-swarm"],
         "supersedes": [B + "developments/2026-09-06-a-swarm-hijacks-a-dormant-wiki"]},
        {"id": "2026-09-12-a-lab-asks-congress-whether-pacing-is-legal",
         "title": "A lab asks Congress whether pacing itself is even legal",
         "claim": "Paul Christiano joined OpenAI's board fearing loss of control, a researcher "
                  "there put extinction at 70% by 2029 unless labs slow, and Altman told staff the "
                  "company could pace itself — so it asked Congress whether that is even legal, "
                  "while backing three California bills as the Senate drafts a federal duty of "
                  "care.",
         "domain": "policy", "actor": ["openai", "us-congress", "california"], "score": "70% by 2029",
         "evidences": ["the-verifiable-pause", "speed-of-containment", "asking-for-your-own-leash"],
         "supersedes": [B + "developments/2026-09-04-automated-shutdown-capabilities"]},
        {"id": "2026-09-12-five-bioweapon-adjacent-labs-disrupted",
         "title": "A lab disrupts five bioweapon-adjacent operations and withholds a model from an ally",
         "claim": "Anthropic disrupted five bioweapon-adjacent labs, caught state actors misusing "
                  "its models, and withheld Mythos 5.1 from the UK, while US agencies accused two "
                  "Chinese labs of mass distillation and the CIA declared economic espionage on "
                  "China.",
         "domain": "policy", "actor": ["anthropic", "cia", "deepseek", "alibaba"],
         "evidences": ["war-reaches-the-cloud", "clearance-as-bottleneck", "silicon-curtain"],
         "supersedes": [B + "developments/2026-09-07-five-point-six-billion-of-hardware-through-a-renamed-arm"]},
        {"id": "2026-09-12-compute-fungible-durable-and-highly-rentable",
         "title": "Compute is recast as a fungible, durable, rentable asset",
         "claim": "OpenAI's compute is up twentyfold, Oracle's capital spending tripled, Microsoft "
                  "plans 38 gigawatts, and Jensen Huang called compute fungible, durable and "
                  "highly rentable, while ten states axed data center tax breaks and Massachusetts "
                  "demanded local approval.",
         "domain": "compute", "actor": ["openai", "oracle", "microsoft", "nvidia"], "score": "38 GW",
         "evidences": ["compute-capital-stack", "thread-lines", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-09-07-fourteen-point-eight-gigawatts-of-compute-deals"]},
        {"id": "2026-09-12-fifteen-percent-growth-with-twenty-percent-cognitive-unemployment",
         "title": "A lab's extreme case pairs 15% growth with near-20% cognitive unemployment",
         "claim": "Musk expects AI and robots to double world GDP by 2036 while Anthropic's "
                  "extreme case pairs 15% growth with near-20% cognitive unemployment, as deep "
                  "tech drew $150 billion since 2024 and one nowcast read 4.4%.",
         "domain": "economics", "actor": ["anthropic", "spacex"], "score": "15% growth / ~20% unemployment",
         "evidences": ["post-labor-instruments", "ai-as-the-economy", "work-displaced"],
         "supersedes": [B + "developments/2026-09-07-an-essay-mill-industry-shrinks-to-humanizer-gigs"]},
        {"id": "2026-09-12-serious-crashes-cut-ninety-two-percent",
         "title": "A robotaxi fleet cuts serious crashes 92%",
         "claim": "Waymo cut serious crashes 92%, a tunneling company raised $3 billion for the "
                  "UAE, and 2,977 drones rebuilt the Twin Towers in light, one per life lost.",
         "domain": "robotics", "actor": ["waymo", "boring-company"], "score": "-92% / 2,977 drones",
         "evidences": ["physical-recursion", "agent-society"],
         "supersedes": [B + "developments/2026-09-04-a-thirty-thousand-dollar-pod-with-no-wheel"]},
        {"id": "2026-09-12-nine-billion-mutations-scored",
         "title": "A model scores all nine billion possible point mutations",
         "claim": "AlphaGenome Atlas scored all nine billion possible point mutations, a migraine "
                  "drug won a Phase 3 in a new indication, and Insilico's AI-designed rentosertib "
                  "reversed aging clocks, a generative pharma first.",
         "domain": "biotech", "actor": ["google-deepmind", "insilico-med"], "score": "9B mutations",
         "evidences": ["biology-as-compile-target", "longevity-escape-velocity", "automated-science"],
         "supersedes": [B + "developments/2026-09-07-forty-percent-of-children-moved-below-a-threshold"]},
    ],
}
