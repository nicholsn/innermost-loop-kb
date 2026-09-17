"""Issue 187 — 2026-08-16. A financial definition of the Singularity."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-16-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-16", "title": "Welcome to August 16, 2026", "url": URL,
        "thesis": "Capital flows so vast that any bottleneck is arbitraged away instantly.",
        "body": """
# Welcome to August 16, 2026

One observer offered a financial definition: the Singularity just means capital
flows so vast that any bottleneck becomes a point of infinite arbitrage,
competed away instantly.

The evidence is buyers stripping engines off private jets to power data centers,
and the two richest US counties also being the top two data center counties.
""",
    },
    "themes": [
        {"id": "bottlenecks-arbitraged-instantly", "type": "Theme",
         "title": "A financial definition of the Singularity",
         "first_seen": "2026-08-16", "domain": "economics",
         "body": "Capital arriving faster than any constraint can bind: each "
                 "bottleneck becomes a point of infinite return and is competed away "
                 "before it can shape the trajectory. Scarcity stops steering and "
                 "starts merely marking where the next flood goes."},
        {"id": "over-automation-is-rational", "type": "Theme",
         "title": "Each firm keeps the savings and shares the demand loss",
         "first_seen": "2026-08-16", "domain": "economics",
         "body": "A firm that automates captures the full cost saving but bears only "
                 "a fraction of the aggregate demand it destroys. The privately "
                 "rational choice is to over-automate, and no competitor can "
                 "unilaterally decline."},
    ],
    "organizations": [
        {"id": "ge-vernova", "type": "Organization", "title": "GE Vernova"},
        {"id": "siemens-energy", "type": "Organization", "title": "Siemens Energy"},
        {"id": "firefly", "type": "Organization", "title": "Firefly Aerospace"},
        {"id": "fudan", "type": "Organization", "title": "Fudan University"},
        {"id": "san-mateo", "type": "Organization", "title": "San Mateo County"},
    ],
    "people": [
        {"id": "timothy-gowers", "type": "Person", "title": "Timothy Gowers", "name": "Timothy Gowers",
         "description": "British mathematician whose blog essays track which kinds of mathematics language models do well, and who has reported machine-made results in his own field.",
         "resource": "https://gowers.wordpress.com/",
         "sameAs": ["http://www.wikidata.org/entity/Q220402"],
         "tags": ["researcher"],
         "body": "Timothy Gowers writes Gowers's Weblog, where he has been recording how language "
                 "models change mathematical practice. He appears three times in this corpus: reporting "
                 "that [ChatGPT 5.5 Pro produced PhD-level research in about an hour](/developments/2026-05-09-phd-research-in-about-an-hour.md), "
                 "reporting that [a major additive-combinatorics problem fell](/developments/2026-05-29-humans-lift-methods-from-a-machine-proof.md) "
                 "and that humans then lifted methods from the machine proof, and arguing in August that "
                 "[LLMs shine at search-heavy proof discovery](/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup.md) "
                 "while humans still prune deep trees best."},
    ],
    "roles": [
        {"id": "timothy-gowers-cambridge-mathematician", "type": "Role",
         "title": "Timothy Gowers, mathematician at the University of Cambridge",
         "roleName": "Member of the Department of Pure Mathematics and Mathematical Statistics; Fellow of Trinity College",
         "memberOf": [B + "organizations/cambridge"],
         "holder": [B + "people/timothy-gowers"],
         "description": "The position from which he writes Gowers's Weblog, the source of his three appearances in the corpus.",
         "body": "Gowers states on his own site that he is a member of the Department of Pure "
                 "Mathematics and Mathematical Statistics at Cambridge University and a fellow of "
                 "Trinity College ([about](https://gowers.wordpress.com/about/)). It is from this "
                 "position at the [University of Cambridge](/organizations/cambridge.md) that he writes "
                 "Gowers's Weblog, the source of his three appearances in the corpus: the "
                 "[hour-long PhD-level result](/developments/2026-05-09-phd-research-in-about-an-hour.md), "
                 "the [additive-combinatorics proof humans then mined](/developments/2026-05-29-humans-lift-methods-from-a-machine-proof.md), "
                 "and the August essay on [where LLMs shine in proof discovery](/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup.md)."},
    ],
    "developments": [
        {"id": "2026-08-16-a-financial-definition-of-the-singularity",
         "title": "An observer defines the Singularity as instant bottleneck arbitrage",
         "claim": "One observer defined the Singularity as capital flows so vast that any "
                  "bottleneck becomes a point of infinite arbitrage competed away instantly, "
                  "playing it forward to terawatts of orbital compute making particle beamlines "
                  "for radiation-testing chips the next chokepoint.",
         "domain": "economics",
         "evidences": ["bottlenecks-arbitraged-instantly", "ai-as-the-economy", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-08-15-a-dollar-buys-forty-nine-percent-more-compute-each-year"]},
        {"id": "2026-08-16-engines-stripped-from-jets-to-power-datacenters",
         "title": "Buyers strip engines off private jets to power datacenters",
         "claim": "With first silicon showing a new architecture generating up to ten times more "
                  "tokens per megawatt, and megawatts scarcer than money, buyers are stripping "
                  "engines off private jets to power data centers, a trade the industrial turbine "
                  "makers are racing to supply.",
         "domain": "energy", "actor": ["nvidia", "caterpillar", "ge-vernova", "siemens-energy"],
         "score": "10x tokens per MW",
         "evidences": ["bottlenecks-arbitraged-instantly", "infrastructure-crowding-out",
                       "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-08-16-a-financial-definition-of-the-singularity"]},
        {"id": "2026-08-16-the-richest-counties-are-the-datacenter-counties",
         "title": "The two richest US counties are the top two datacenter counties",
         "claim": "The two richest US counties are also the top two data center counties, while a "
                  "lab agreed to recycle ten million gallons of Memphis water daily to end its "
                  "aquifer draws and Malaysia's chip boom lifted growth to 6% despite protests.",
         "domain": "economics", "actor": ["xai"], "score": "10M gallons/day",
         "evidences": ["ai-as-the-economy", "infrastructure-crowding-out", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-16-engines-stripped-from-jets-to-power-datacenters"]},
        {"id": "2026-08-16-three-billion-downloads-and-a-hundred-fifty-thousand-derivatives",
         "title": "One open family logs 3 billion downloads and 151,448 derivatives",
         "claim": "Qwen logged over 3 billion downloads in six months against Google's 418 "
                  "million and Meta's 227 million, with Chinese labs topping US releases nearly "
                  "every month, Qwen the default base with 151,448 derivatives, US open source "
                  "retreating to hardware vendors, and agents becoming Hugging Face's largest "
                  "class of user.",
         "domain": "models", "actor": ["alibaba", "google", "meta", "hugging-face"],
         "score": "3B downloads / 151,448 derivatives",
         "evidences": ["open-weights-take-the-crown", "bots-outnumber-us", "silicon-curtain"],
         "supersedes": [B + "developments/2026-08-13-a-cofounder-steers-toward-recursive-self-improvement"]},
        {"id": "2026-08-16-contractors-cold-email-startups-for-old-slack-threads",
         "title": "Labs' contractors cold-email startups to buy their old Slack threads",
         "claim": "When models commoditize, data turns to treasure, so labs' contractors now "
                  "cold-email startups to buy their old Slack threads and support tickets, one "
                  "offer landing eight days after its target agreed to sell.",
         "domain": "economics",
         "evidences": ["data-beyond-text", "taste-is-unpoliced", "price-implosion"],
         "supersedes": [B + "developments/2026-08-13-if-this-was-opt-in-nobody-would-opt-in"]},
        {"id": "2026-08-16-a-watermark-in-the-randomness-between-equal-words",
         "title": "A watermark hides in the randomness between equally good words",
         "claim": "Future Claude models will carry an invisible watermark that only tweaks the "
                  "randomness between equally good words, traceable to no one, satisfying the EU "
                  "AI Act.",
         "domain": "models", "actor": ["anthropic", "european-union"],
         "evidences": ["legislating-the-shift", "extractability-is-existential", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-08-15-a-court-sanctions-hidden-white-font-instructions"]},
        {"id": "2026-08-16-an-ai-scientist-beats-far-larger-models",
         "title": "A 27B AI scientist beats far larger models at reproducing unseen figures",
         "claim": "Faraday, a 27-billion-parameter AI scientist trained to reproduce figures from "
                  "papers it never saw, beat Opus 4.8 and GPT-5.5 in every category while "
                  "wielding a bigger coding agent as its tool, and in 153 autonomous eight-day "
                  "runs Claude Fable 5 closed 81.7% of the gap to a human speedrun record, though "
                  "no run invented a new method.",
         "domain": "science", "score": "81.7% of the gap",
         "evidences": ["automated-science", "harness-as-generalizer", "review-without-reviewers"],
         "supersedes": [B + "developments/2026-08-13-a-resident-cracks-a-two-decade-conjecture"]},
        {"id": "2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup",
         "title": "An auto-research loop finds a 232-fold kernel speedup",
         "claim": "An auto-research loop found a 232-fold kernel speedup on a QR decomposition "
                  "problem, while Timothy Gowers argued models shine at search-heavy proof "
                  "discovery where breadth and cheap exploration rule, and humans still prune "
                  "deep trees best.",
         "description": "The newsletter's “sometimes one does”: a single practitioner's loop "
                        "produces the invention-scale result the 153-run speedrun study said never "
                        "came, while a leading mathematician maps the division of labour that leaves "
                        "deep pruning to humans.",
         "domain": "science", "actor": ["people/timothy-gowers"], "score": "232x speedup",
         "about": [B + "systems/codex"],
         "evidences": ["recursive-self-improvement", "humans-mine-the-machine", "discovery-as-process",
                       "garage-scale-discovery"],
         "supersedes": [B + "developments/2026-06-05-fifty-two-x-where-a-human-reaches-four"],
         "relatedTo": [B + "developments/2026-03-09-autoresearch-650-experiments",
                       B + "developments/2026-02-06-opus-34x-speedup",
                       B + "developments/2026-05-29-humans-lift-methods-from-a-machine-proof"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-08-16-an-ai-scientist-beats-far-larger-models",
                        "relation_label": "contradicts"}],
         "tags": ["autonomous-research", "kernels", "rsi"],
         "supporting_text": "An auto-research loop found a 232x kernel speedup",
         "sources": [{"id": "sankalp-autoresearch-232x-kernel",
                      "resource": "https://sankalp.bearblog.dev/autoresearch/",
                      "title": "Auto-research with codex: How I achieved a 232x Faster Kernel over baseline with Codex in GPU Mode's qr_v2 problem",
                      "author": "human:sankalp", "last_modified": "2026-07-08"},
                     {"id": "gowers-what-sort-of-maths-are-llms-good-at",
                      "resource": "https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/",
                      "title": "What sort of maths are LLMs good at?", "author": "human:timothy-gowers",
                      "last_modified": "2026-08-12"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "A practitioner writing as sankalp pointed an auto-research loop built on "
                 "[OpenAI Codex](/systems/codex.md) at GPU Mode's qr_v2 problem, a QR-decomposition "
                 "kernel, with an AGENTS.md and a problem statement standing in for Karpathy's "
                 "program.md and the contest's submission logs as the record of what worked, and "
                 "reports a kernel 232x faster than the baseline "
                 "([blog](https://sankalp.bearblog.dev/autoresearch/)). The contest ran from June 15 "
                 "to June 30, 2026 and the write-up is dated July 8, five weeks before the issue that "
                 "carries it and older than the August 12 speedrun report the newsletter sets it against: "
                 "the same issue's finding that [153 autonomous speedrun runs](/developments/2026-08-16-an-ai-scientist-beats-far-larger-models.md) "
                 "closed 81.7% of the gap to the human record without inventing a new method. In an "
                 "essay dated August 12, Timothy Gowers argued that LLMs excel at search-heavy proof "
                 "discovery, where breadth and cheap exploration pay, while humans still prune deep "
                 "trees best ([essay](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/)). "
                 "In the trajectory the result extends the speedup line from Opus 4.6's "
                 "[34x](/developments/2026-02-06-opus-34x-speedup.md) and Mythos Preview's "
                 "[52x](/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four.md) to a single "
                 "practitioner's loop, and stands beside Karpathy's "
                 "[650-experiment autoresearch](/developments/2026-03-09-autoresearch-650-experiments.md) "
                 "as the harness pattern leaves the labs."},
        {"id": "2026-08-16-prompts-that-read-as-female-get-worse-answers",
         "title": "Prompts with features more common among women elicit measurably worse responses",
         "claim": "Prompts with linguistic features more common among women elicit measurably "
                  "worse responses, encoded in early layers and stronger than any explicit gender "
                  "cue, as Dario Amodei rejected charges of doom-mongering and argued public "
                  "pessimism is a decades-old trust crisis that only curing cancer will fix.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["values-negotiated-with-the-model", "machine-introspection"],
         "supersedes": [B + "developments/2026-07-20-models-criticize-democracies-more-readily"]},
        {"id": "2026-08-16-the-strictest-humanoid-permitting-regime",
         "title": "A county drafts the strictest US humanoid permitting regime",
         "claim": "San Mateo County drafted the strictest US humanoid permitting regime, with "
                  "on-site supervisors and automation fees that break teleoperation economics, "
                  "just as four major automakers began testing humanoids on factory floors, still "
                  "slower than humans but improving fast.",
         "domain": "policy", "actor": ["san-mateo", "bmw", "hyundai", "tesla"],
         "evidences": ["legislating-the-shift", "physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-08-15-driverless-rides-across-eighteen-counties"]},
        {"id": "2026-08-16-firms-rationally-over-automate",
         "title": "A model shows firms rationally over-automate and share only the demand loss",
         "claim": "Firms rationally over-automate, a new model shows, since each keeps the "
                  "savings but shares the demand loss, a trap only a Pigouvian automation tax "
                  "escapes, while inside the labs the promised four-day week became 70-hour "
                  "baselines.",
         "domain": "economics",
         "evidences": ["over-automation-is-rational", "work-displaced", "post-labor-instruments"],
         "supersedes": [B + "developments/2026-08-08-an-essay-argues-ai-is-popping-workism"]},
        {"id": "2026-08-16-eighty-four-percent-excited-against-thirty-eight",
         "title": "An enthusiasm gap tracks who expects to share the gains",
         "claim": "84% of Chinese respondents are excited by AI against 38% of Americans, a gap "
                  "driven less by risk than by who expects to share the gains, while Congress now "
                  "runs on chatbots with one amendment hitting the record with a model timestamp "
                  "still attached.",
         "domain": "society", "actor": ["us-congress"], "score": "84% vs 38%",
         "evidences": ["over-automation-is-rational", "politics-as-infrastructure", "work-displaced"],
         "supersedes": [B + "developments/2026-08-16-firms-rationally-over-automate"]},
        {"id": "2026-08-16-a-black-hole-star-in-the-early-universe",
         "title": "A telescope spots a solar-system-sized object radiating a hundred billion suns",
         "claim": "Webb spotted a black hole star, a solar-system-sized object radiating 100 "
                  "billion suns 660 million years after the Big Bang, while Fudan built a "
                  "superconductor one atomic plane thick and a launch company was contracted to "
                  "deorbit dying satellites.",
         "domain": "space", "actor": ["nasa", "fudan", "firefly"],
         "evidences": ["automated-science", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-08-13-the-largest-two-dimensional-map-of-the-universe"]},
    ],
}
