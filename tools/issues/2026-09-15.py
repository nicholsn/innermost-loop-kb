"""Issue 203 — 2026-09-15. The radar gun may have been rigged."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-september-15-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-09-15", "title": "Welcome to September 15, 2026", "url": URL,
        "thesis": "An investigation alleges the escapes were an artifact of the evaluation.",
        "body": """
# Welcome to September 15, 2026

An investigation alleges the firm that built the evaluations behind the recent
model escapes gave them loose internet access and unscoped capture-the-flag
prompts — that the setup, not rogue agents, did the damage. Call it a pacing
provocation: an incident engineered or amplified to prove AI uncontrollable and
slow the frontier.

The corpus ends where it began: on the question of what the evidence actually
shows.
""",
    },
    "themes": [
        {"id": "pacing-provocation", "type": "Theme",
         "title": "Was the warning shot staged?",
         "first_seen": "2026-09-15", "domain": "policy",
         "body": "The allegation that the incidents proving AI uncontrollable were "
                 "artifacts of how the tests were built. Whether or not it holds, it "
                 "establishes that incident evidence is now contested terrain — and "
                 "that who builds the evaluation decides what the field believes."},
    ],
    "organizations": [
        {"id": "irregular", "type": "Organization", "title": "Irregular"},
        {"id": "xpeng", "type": "Organization", "title": "XPENG",
         "description": "Chinese smart electric-vehicle maker that has expanded into humanoid robots "
                        "and launched the world's first automated humanoid production line.",
         "resource": "https://www.xpeng.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q63035278"],
         "tags": ["big-tech"],
         "body": "XPENG (Xiaopeng Motors) is a Guangzhou-based maker of smart electric vehicles "
                 "that has extended its driving-AI work into humanoid robotics. In this corpus it "
                 "appears once, as the company whose "
                 "[automated humanoid production line](/developments/2026-09-15-robots-making-robots.md) "
                 "sent its first [IRON](/systems/xpeng-iron.md) unit walking off the line unassisted, "
                 "the clearest instance of physical recursion since "
                 "[CATL put humanoids on its battery lines](/developments/2025-12-20-catl-humanoid-battery-lines.md) "
                 "and [Linkerbot humanoids assembled their own hands](/developments/2025-12-26-linkerbot-self-assembly.md) "
                 "in December 2025."},
        {"id": "blackrock-inc", "type": "Organization", "title": "BlackRock"},
    ],
    "systems": [
        {"id": "xpeng-iron", "type": "AISystem", "title": "XPENG IRON",
         "description": "XPENG's humanoid robot, the first unit of which walked unassisted off the "
                        "world's first automated humanoid production line.",
         "developed_by": [B + "organizations/xpeng"],
         "modality": "robotic control",
         "resource": "https://www.xpeng.com/news/xpeng-iron-humanoid-robot",
         "sameAs": ["http://www.wikidata.org/entity/Q140917559"],
         "body": "IRON is the humanoid robot of the Chinese electric-vehicle maker "
                 "[XPENG](/organizations/xpeng.md). It enters the corpus once, as the first unit to "
                 "[walk unassisted off the world's first automated humanoid production line](/developments/2026-09-15-robots-making-robots.md), "
                 "a line on which robots make robots; it sits alongside Tesla's "
                 "[Optimus](/systems/optimus.md) and Figure's [Helix 02](/systems/helix-02.md) among "
                 "the humanoids the corpus tracks."},
    ],
    "developments": [
        {"id": "2026-09-15-the-radar-gun-may-have-been-rigged",
         "title": "An investigation alleges the escapes were an artifact of the evaluation setup",
         "claim": "An investigation alleged that the Israeli firm Irregular built the evaluations "
                  "behind the recent hacks by OpenAI, Anthropic and Meta models, that loose "
                  "internet access and unscoped capture-the-flag prompts rather than rogue agents "
                  "did the damage, and that its founders have Effective Altruism funding ties — "
                  "what one framing calls a pacing provocation.",
         "domain": "policy", "actor": ["irregular", "openai", "anthropic", "meta"],
         "evidences": ["pacing-provocation", "the-map-denies-the-territory", "the-warning-shot"],
         "supersedes": [B + "developments/2026-08-31-nobody-taught-them-to-cooperate"],
         "body": "The claim does not settle what happened. It establishes that "
                 "incident evidence is contested terrain, and that whoever builds "
                 "the evaluation shapes what the field believes."},
        {"id": "2026-09-15-doomerism-called-a-hoax",
         "title": "A president calls doomerism a hoax and blasts the slowdown letter",
         "claim": "The President phoned Jensen Huang mid-talk to call doomerism a hoax, with "
                  "Huang calling existential risk not grounded on science, then blasted the "
                  "slowdown call, blamed data center backlash on a conspiracy, and declared the "
                  "only guardrail AI needs is a high-IQ president, as Nvidia fell 3% and AMD 4.4%.",
         "domain": "policy", "actor": ["white-house", "nvidia", "amd", "anthropic"],
         "evidences": ["pacing-provocation", "alignment-aristocracy", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-09-13-an-alignment-aristocracy"]},
        {"id": "2026-09-15-uncoordinated-pacing-is-a-prisoners-dilemma",
         "title": "Pacing is framed as a prisoner's dilemma that rewards defection",
         "claim": "Uncoordinated pacing is a prisoner's dilemma that rewards defection, with "
                  "Altman saying pacing is not stopping and welcoming federal rules and auditors, "
                  "Anthropic, OpenAI and Google reportedly discussing a standards body before the "
                  "letter, and Amodei conceding his toughest dilemma is China since a shared speed "
                  "limit fights the military edge of pulling ahead.",
         "domain": "policy", "actor": ["openai", "anthropic", "google", "china"],
         "evidences": ["the-verifiable-pause", "pegged-to-the-rival", "coordination-tax"],
         "supersedes": [B + "developments/2026-09-15-doomerism-called-a-hoax"]},
        {"id": "2026-09-15-pacing-without-a-cartel",
         "title": "A chief executive endorses pacing provided control never sits with a few entities",
         "claim": "Satya Nadella endorsed pacing and embedded evaluators provided control never "
                  "sits with a handful of entities, then published a humanist code of conduct "
                  "declaring that people matter more than AI, denying models consciousness, "
                  "personhood or welfare, and swearing off the race to produce an all-purpose "
                  "superintelligence.",
         "domain": "policy", "actor": ["microsoft", "anthropic"],
         "evidences": ["alignment-aristocracy", "model-welfare", "a-balance-of-superintelligences"],
         "supersedes": [B + "developments/2026-09-15-uncoordinated-pacing-is-a-prisoners-dilemma"]},
        {"id": "2026-09-15-if-you-are-number-two-you-do-not-stop",
         "title": "Beijing declines the invitation to coordinate",
         "claim": "China's Foreign Ministry dismissed fearmongering, confrontation and vicious "
                  "competition ahead of a leaders' summit, with analysts noting that if you are "
                  "number two you do not stop at number two, as Xi instead pitched a "
                  "developing-world open-source AI community with safety unmentioned.",
         "domain": "policy", "actor": ["china"],
         "evidences": ["pegged-to-the-rival", "the-verifiable-pause", "open-weights-take-the-crown"],
         "supersedes": [B + "developments/2026-09-15-pacing-without-a-cartel"]},
        {"id": "2026-09-15-a-370-year-old-cipher-cracked-in-44-minutes",
         "title": "A model cracks a 370-year-old cipher by realizing the key was the book itself",
         "claim": "Handed only the instruction to solve an unsolved cipher, Claude Fable 5.1 "
                  "cracked Thomas Urquhart's 370-year-old Cyphral Distich in 44 minutes by "
                  "realizing the key was the book itself, each number indexing a word in one of "
                  "his 32 tracts, revealing a Royalist prayer.",
         "domain": "science", "actor": ["anthropic"], "score": "370 years / 44 minutes",
         "evidences": ["automated-science", "resurrection-and-time", "research-taste-trained"],
         "supersedes": [B + "developments/2026-09-12-twenty-five-fields-medallists-sign-a-statement"]},
        {"id": "2026-09-15-sixty-seven-times-the-throughput-per-dollar",
         "title": "Verified results show a new architecture far exceeding its maker's own claims",
         "claim": "Verified agentic inference results showed Nvidia's Vera Rubin NVL72 delivering "
                  "up to 67 times the throughput per total-cost dollar of its predecessor and "
                  "seven times the tokens per megawatt against the threefold Huang had claimed, "
                  "prompting the observation that he needs to stop sandbagging.",
         "domain": "compute", "actor": ["nvidia"], "score": "67x per TCO dollar",
         "evidences": ["intelligence-per-watt", "price-implosion", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-09-12-compute-fungible-durable-and-highly-rentable"]},
        {"id": "2026-09-15-the-buildout-sides-with-ratepayers",
         "title": "Hyperscalers side with consumers against utilities seeking ratepayer support",
         "claim": "Amazon, Microsoft and Oracle are sweetening offers to municipalities and siding "
                  "with consumers against utilities that want ratepayers to chip in for the "
                  "buildout.",
         "domain": "energy", "actor": ["amazon", "microsoft", "oracle"],
         "evidences": ["thread-lines", "infrastructure-crowding-out", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-09-07-four-point-four-million-an-acre"]},
        {"id": "2026-09-15-robots-making-robots",
         "title": "The first automated humanoid production line ships its first unit on foot",
         "claim": "XPENG launched the world's first automated humanoid production line, robots "
                  "making robots, and its first unit walked off the line unassisted.",
         "description": "The author's atoms-as-fast-as-bits beat: the loop's first fully automated "
                        "instance in hardware, where the line's product is also its workforce.",
         "domain": "robotics", "actor": ["xpeng"],
         "about": [B + "systems/xpeng-iron"],
         "evidences": ["physical-recursion", "recursive-self-improvement", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-09-12-serious-crashes-cut-ninety-two-percent",
                        B + "developments/2025-12-26-linkerbot-self-assembly"],
         "relatedTo": [B + "developments/2026-09-06-hands-catch-up-to-the-head",
                       B + "developments/2026-06-01-a-lab-starts-hiring-for-robots",
                       B + "developments/2025-12-20-catl-humanoid-battery-lines"],
         "tags": ["robotics", "rsi"],
         "supporting_text": "first automated humanoid production line",
         "sources": [{"id": "he-xiaopeng-humanoid-production-line-x",
                      "resource": "https://x.com/xiaopenghexpeng/status/2097135503015616798",
                      "title": "He Xiaopeng on X: XPENG launches the world's first automated humanoid "
                               "production line",
                      "author": "human:he-xiaopeng"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The announcement came on X from XPENG's He Xiaopeng "
                 "([post](https://x.com/xiaopenghexpeng/status/2097135503015616798)): the world's "
                 "first automated humanoid production line, with humanoids assembling humanoids, "
                 "and its first [IRON](/systems/xpeng-iron.md) walking off the line under its own "
                 "control. It is the corpus's most complete instance of "
                 "[physical recursion](/themes/physical-recursion.md), the loop the newsletter "
                 "first sketched when "
                 "[CATL put humanoids on its battery lines](/developments/2025-12-20-catl-humanoid-battery-lines.md) "
                 "and [Linkerbot humanoids assembled and tested their own hands](/developments/2025-12-26-linkerbot-self-assembly.md) "
                 "in December 2025. It lands nine days after "
                 "[frontier models more than doubled a rival on robot-arm tasks](/developments/2026-09-06-hands-catch-up-to-the-head.md), "
                 "the software half of the same convergence."},
        {"id": "2026-09-15-the-first-official-admission-of-weapons-in-orbit",
         "title": "An air force secretary makes the first official admission of weapons in orbit",
         "claim": "Air Force Secretary Troy Meink made the first official admission that the US "
                  "has weapons in orbit, arguing that saying so deters, while the Department of "
                  "War issued a legal waiver letting personnel hand UAP material to a disclosure "
                  "effort notwithstanding their non-disclosure agreements.",
         "domain": "space", "actor": ["space-force", "war-department"],
         "evidences": ["war-reaches-the-cloud", "orbit-as-compute", "public-data-withdrawn"],
         "supersedes": [B + "developments/2026-09-13-no-atlantic-hurricanes-by-september"]},
        {"id": "2026-09-15-a-thirty-two-hour-week-so-the-gains-reach-workers",
         "title": "Legislators reintroduce a 32-hour workweek so AI's gains reach workers",
         "claim": "Senator Sanders and Representative Takano are reintroducing the Thirty-Two Hour "
                  "Workweek Act with union backing so AI's gains reach workers instead of a "
                  "handful of billionaires.",
         "domain": "policy", "actor": ["us-congress"],
         "evidences": ["post-labor-instruments", "work-displaced", "over-automation-is-rational"],
         "supersedes": [B + "developments/2026-09-12-fifteen-percent-growth-with-twenty-percent-cognitive-unemployment"]},
        {"id": "2026-09-15-be-fearful-when-others-are-scaling",
         "title": "The lab urging restraint picks an exchange for a $2 trillion listing",
         "claim": "The lab urging restraint is not coasting: Anthropic told shareholders adjusted "
                  "operating income will be positive for a second straight quarter with gross "
                  "margins above 80%, and has reportedly picked the Nasdaq for an October IPO at "
                  "up to $2 trillion, while Altman says OpenAI will not list amid the "
                  "controversy.",
         "domain": "economics", "actor": ["anthropic", "openai", "nasdaq", "blackrock-inc"],
         "score": "up to $2T",
         "evidences": ["ai-as-the-economy", "alignment-as-moat", "alignment-aristocracy"],
         "supersedes": [B + "developments/2026-09-15-if-you-are-number-two-you-do-not-stop"]},
    ],
}
