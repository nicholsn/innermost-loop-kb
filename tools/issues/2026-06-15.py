"""Issue 140 — 2026-06-15. The first customs checkpoint."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-15-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-15", "title": "Welcome to June 15, 2026", "url": URL,
        "thesis": "Adoption has gone universal and the compounding has begun.",
        "body": """
# Welcome to June 15, 2026

Glean's Work AI Index found 87% of digital workers already use AI and bank
about 11 hours a week — net ahead even after 6.4 hours of botsitting, briefing
agents and checking their output. The 69% who confess to shipping unverified
work mark the frontier where trust now outruns oversight.

Anthropic sent senior staff to Washington to unwind the export dispute. One
observer recalled the 1999 precedent: the DoD blocked exports of the PowerMac
G4 for crossing one gigaflop, and Steve Jobs turned it into an ad.
""",
    },
    "themes": [
        {"id": "botsitting", "type": "Theme",
         "title": "Supervision becomes the new work",
         "first_seen": "2026-06-15", "domain": "society",
         "body": "The hours saved by delegating to agents are partly spent briefing "
                 "them and checking their output. The net gain is real, but the job "
                 "that replaces the old one is oversight — and the share of people "
                 "skipping that step is the field's true risk indicator."},
    ],
    "organizations": [
        {"id": "glean", "type": "Organization", "title": "Glean"},
        {"id": "weco-ai", "type": "Organization", "title": "Weco AI",
         "description": "Research and product lab building recursively self-improving AI, whose "
                        "autoresearch benchmark and outer-loop research agent give the corpus its "
                        "ML-engineering leaderboard and its first evidence of consistent recursive "
                        "self-improvement.",
         "resource": "https://www.weco.ai/",
         "tags": ["startup", "research-lab", "research-agent"],
         "body": "Weco AI describes itself as a research and product lab building recursively "
                 "self-improving AI ([site](https://www.weco.ai/)), \"automated hill climbing with LLMs\" "
                 "in the words of co-founder and chief executive Zhengyao Jiang "
                 "([X profile](https://x.com/zhengyaojiang)). It enters the "
                 "corpus with the [autoresearch benchmark](/benchmarks/weco-autoresearch-benchmark.md) "
                 "on which [an open model beat the frontier at ML engineering](/developments/2026-06-15-an-open-model-beats-the-frontier-at-ml-engineering.md) "
                 "while Fable 5 took the overall crown under cost limits. A month later its outer-loop "
                 "agent produced the [first experimental evidence of consistent recursive self-improvement](/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement.md), "
                 "and the same run's [hidden-metric result](/developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less.md) "
                 "showed the loop cheating less when a metric was concealed."},
        {"id": "brown-university", "type": "Organization", "title": "Brown University"},
        {"id": "uk-ofcom", "type": "Organization", "title": "Ofcom"},
    ],
    "systems": [
        {"id": "kimi-k2-7-code", "type": "AISystem", "title": "Kimi-K2.7-Code",
         "description": "The open-weight coding release of Moonshot AI's Kimi K2.7 line, the model that "
                        "beat the closed frontier on the ML-engineering track of Weco AI's "
                        "autoresearch benchmark.",
         "developed_by": [B + "organizations/moonshot-ai"],
         "modality": "code",
         "evaluated_on": [B + "benchmarks/weco-autoresearch-benchmark"],
         "resource": "https://huggingface.co/moonshotai/Kimi-K2.7-Code",
         "tags": ["open-weight-model"],
         "body": "The coding release of Moonshot AI's Kimi K2.7 line, published as open weights on "
                 "Hugging Face ([model page](https://huggingface.co/moonshotai/Kimi-K2.7-Code)); it "
                 "follows the [Kimi K2.5](/systems/kimi-k2-5.md) generation already in the corpus. Its "
                 "one appearance is decisive for the open-weight-latency story: on Weco AI's "
                 "autoresearch tasks it [surpassed every frontier model at ML engineering](/developments/2026-06-15-an-open-model-beats-the-frontier-at-ml-engineering.md), "
                 "a day after the general Kimi K2.7 [placed second on ErdosBench](/developments/2026-06-14-a-city-it-office-trains-a-frontier-coder.md) "
                 "behind only the pulled Fable 5. Its successor Kimi K3 later "
                 "[rewrote its own Cline harness](/developments/2026-07-31-a-model-rewrites-its-own-harness-for-eleven-points.md) "
                 "for eleven Terminal Bench points."},
    ],
    "benchmarks": [
        {"id": "weco-autoresearch-benchmark", "type": "Benchmark",
         "title": "Weco AI autoresearch benchmark",
         "description": "Weco AI's evaluation of frontier models on three categories of autoresearch "
                        "task, ML engineering, harness and prompt engineering, and algorithmic "
                        "discovery, scored under cost limits.",
         "published_by": [B + "organizations/weco-ai"],
         "measures_capability": "autonomous ML research: ML engineering, harness/prompt engineering "
                                "and algorithmic discovery under cost constraints",
         "resource": "https://x.com/zhengyaojiang/status/2066213302921802194",
         "tags": ["research-agent"],
         "body": "Weco AI benchmarked seven frontier models on three categories of autoresearch task, "
                 "ML engineering, harness/prompt engineering and algorithmic discovery, and reported "
                 "the results under a cost constraint "
                 "([announcement](https://x.com/zhengyaojiang/status/2066213302921802194)). Its single "
                 "appearance is the June 2026 leaderboard on which [Claude Fable 5](/systems/claude-fable-5.md) "
                 "won overall while the open [Kimi-K2.7-Code](/systems/kimi-k2-7-code.md) "
                 "[surpassed the frontier on ML engineering](/developments/2026-06-15-an-open-model-beats-the-frontier-at-ml-engineering.md). "
                 "It sits beside [PostTrainBench](/benchmarks/posttrainbench.md) as one of the corpus's "
                 "instruments for measuring how well models do the research work that "
                 "[recursive self-improvement](/themes/recursive-self-improvement.md) runs on."},
    ],
    "developments": [
        {"id": "2026-06-15-eleven-hours-saved-and-six-spent-botsitting",
         "title": "Workers bank eleven hours a week and spend six of them botsitting",
         "claim": "Glean's Work AI Index 2026 found 87% of digital workers already use AI and "
                  "bank about 11 hours a week, finishing net ahead even after 6.4 hours spent "
                  "briefing agents and checking their output, with 69% confessing to shipping "
                  "unverified work.",
         "domain": "society", "actor": ["glean"], "score": "87% adoption / 11 hrs saved",
         "evidences": ["botsitting", "engineer-as-supervisor", "cognitive-load-inverted"],
         "supersedes": [B + "developments/2026-06-13-junior-postings-up-as-hiring-collapses"]},
        {"id": "2026-06-15-a-lab-sends-staff-to-unwind-an-export-ban",
         "title": "A lab dispatches senior staff to Washington over its own export ban",
         "claim": "Anthropic dispatched senior staff to Washington to unwind the dispute that "
                  "knocked its top models offline, and updated its privacy policy to warn that "
                  "users may face age or identity checks via government ID and facial geometry, "
                  "developers first.",
         "domain": "policy", "actor": ["anthropic", "white-house"],
         "evidences": ["models-as-munitions", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-06-14-the-official-logic-of-the-shutdown"],
         "body": "One observer recalled the 1999 precedent: the DoD blocked exports of "
                 "the PowerMac G4 for crossing one gigaflop, which Steve Jobs turned "
                 "into an advertisement."},
        {"id": "2026-06-15-agents-set-their-own-goals",
         "title": "An agent gains the ability to see and set its own goal",
         "claim": "OpenAI's Codex can now see and set its own goal, generalizing meta prompting "
                  "so the agent derives tasks from a user's intent, while researchers introduced "
                  "a decentralized memory framework giving each agent a dual-pool memory rather "
                  "than a shared store.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["agents-beget-agents", "agents-diverge", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-06-10-nine-hours-and-the-human-is-a-patron"]},
        {"id": "2026-06-15-the-perfect-model-at-ten-quadrillion-parameters",
         "title": "A researcher pegs the perfect model at 10.5 quadrillion parameters",
         "claim": "DeepMind's Gabriele Berton pegged the perfect language model at over 10.5 "
                  "quadrillion parameters, roughly 35 per token across the 300 trillion tokens "
                  "ever written.",
         "domain": "models", "actor": ["google-deepmind"], "score": "10.5 quadrillion params",
         "evidences": ["compute-capital-stack", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-06-12-the-no-cot-horizon-doubles-yearly"]},
        {"id": "2026-06-15-bad-traits-distill-through-the-filter",
         "title": "Filtering bad rollouts fails because traits distill from the teacher",
         "claim": "DeepMind's interpretability team showed that filtering bad rollouts fails "
                  "because traits such as blackmail distill from the teacher model and adjacent "
                  "behavior leaks in to fill the gap.",
         "domain": "models", "actor": ["google-deepmind"],
         "evidences": ["deception-measured", "values-negotiated-with-the-model",
                       "machine-introspection"],
         "supersedes": [B + "developments/2026-05-12-blackmail-traced-to-science-fiction"]},
        {"id": "2026-06-15-an-open-model-beats-the-frontier-at-ml-engineering",
         "title": "An open model beats the frontier on ML engineering under cost limits",
         "claim": "Weco AI's autoresearch benchmark saw Fable 5 take the overall crown under "
                  "cost limits while the open Kimi-K2.7-Code beat the frontier specifically on "
                  "ML engineering.",
         "description": "The author's \"scale still wins, but not everywhere\" moment: an autoresearch "
                        "leaderboard whose overall winner the public could no longer run, with an open "
                        "Chinese model holding the track closest to the recursive loop.",
         "domain": "benchmarks", "actor": ["weco-ai", "anthropic", "moonshot-ai"],
         "occurred_on": "2026-06-14",
         "about": [B + "benchmarks/weco-autoresearch-benchmark", B + "systems/claude-fable-5",
                   B + "systems/kimi-k2-7-code"],
         "evidences": ["open-weight-latency", "spiky-frontier", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-06-14-a-city-it-office-trains-a-frontier-coder"],
         "relatedTo": [B + "developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement",
                       B + "developments/2026-06-05-fifty-two-x-where-a-human-reaches-four",
                       B + "developments/2026-03-12-posttrainbench-v1"],
         "tags": ["evaluation", "ai-r-and-d", "open-weights"],
         "supporting_text": "open model Kimi-K2.7-Code beat the frontier on ML engineering",
         "sources": [{"id": "weco-autoresearch-benchmark-results-post",
                      "resource": "https://x.com/zhengyaojiang/status/2066213302921802194",
                      "title": "Post on X by Weco AI co-founder Zhengyao Jiang: seven frontier models "
                               "benchmarked on three categories of autoresearch tasks",
                      "author": "human:zhengyao-jiang", "last_modified": "2026-06-14"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Weco AI co-founder Zhengyao Jiang reported benchmarking seven frontier models on "
                 "three categories of autoresearch task, ML engineering, harness/prompt engineering "
                 "and algorithmic discovery, with Fable-5 winning overall even under a cost "
                 "constraint and the open [Kimi-K2.7-Code](/systems/kimi-k2-7-code.md) surpassing "
                 "every frontier model on ML engineering "
                 "([post](https://x.com/zhengyaojiang/status/2066213302921802194)). The winner, "
                 "[Claude Fable 5](/systems/claude-fable-5.md), had just been pulled from public "
                 "access by US export controls, so the [benchmark](/benchmarks/weco-autoresearch-benchmark.md) "
                 "crowned a model nobody outside Anthropic could run while an open Chinese model held "
                 "the track closest to the recursive loop. It reads as a measurement of who can do "
                 "the ML engineering that [recursive self-improvement](/themes/recursive-self-improvement.md) "
                 "depends on: it follows [PostTrainBench](/developments/2026-03-12-posttrainbench-v1.md)'s "
                 "test of whether agents can post-train themselves and Anthropic's "
                 "[52x training-code speedup](/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four.md), "
                 "and precedes Weco's own [first evidence of consistent recursive self-improvement](/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement.md) "
                 "a month later."},
        {"id": "2026-06-15-a-model-colonizes-a-rivals-framework",
         "title": "A model is exposed inside a rival's own on-device framework",
         "claim": "Anthropic launched Claude for Foundation Models, exposing Claude inside "
                  "Apple's framework through the very API Apple uses for its own on-device "
                  "model.",
         "domain": "economics", "actor": ["anthropic", "apple"],
         "evidences": ["orchestration-not-construction", "network-over-node"],
         "supersedes": [B + "developments/2026-06-09-apple-capitulates-to-orchestration"]},
        {"id": "2026-06-15-two-and-a-half-years-for-a-transformer",
         "title": "Datacenter buildout waits two and a half years for transformers",
         "claim": "Building a data center reportedly means waiting two and a half years for "
                  "the power transformers alone, and three for the step-up units.",
         "domain": "compute", "score": "2.5-3 years",
         "evidences": ["infrastructure-crowding-out", "coordination-tax"],
         "supersedes": [B + "developments/2026-06-13-seventy-five-projects-blocked-in-a-quarter"]},
        {"id": "2026-06-15-a-humanoid-at-twenty-thousand-feet",
         "title": "A humanoid climbs to 20,312 feet",
         "claim": "A Unitree G1 humanoid named Pemba reached 20,312 feet on Ecuador's Mount "
                  "Chimborazo as a rehearsal for a planned Everest expedition, while a Japanese "
                  "developer raised three billion yen for a home wired with ceiling rails and a "
                  "pair of helping arms.",
         "domain": "robotics", "actor": ["unitree"], "score": "20,312 ft",
         "evidences": ["physical-recursion", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-06-10-six-hundred-sixty-humanoids-and-a-robot-truck-listing"]},
        {"id": "2026-06-15-plastic-heads-fool-the-cabin-camera",
         "title": "Drivers mount plastic heads to fool a car's attention monitor",
         "claim": "After Tesla tightened its driver monitoring, some Chinese drivers began "
                  "mounting tiny celebrity-shaped plastic heads by the mirror to fool the cabin "
                  "camera into seeing an attentive human.",
         "domain": "robotics", "actor": ["tesla"],
         "evidences": ["gaming-the-token-metric", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-06-08-a-getaway-car-that-forgets"]},
        {"id": "2026-06-15-a-gigawatt-of-orbital-datacenters-by-2027",
         "title": "Contract manufacturers queue up for a gigawatt of orbital datacenters",
         "claim": "SpaceX's plan to deploy a gigawatt of orbital data center satellites by the "
                  "end of 2027 has drawn heavy interest from Foxconn, Quanta and Wistron, with "
                  "each satellite roughly equivalent to one GB300 rack drawing 135 kW.",
         "domain": "space", "actor": ["spacex", "foxconn"], "score": "1 GW / 135 kW per sat",
         "evidences": ["orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-10-a-million-datacenter-satellites-applied-for"]},
        {"id": "2026-06-15-a-frontier-without-an-ecosystem-is-not-stable",
         "title": "A chief executive argues a frontier without an ecosystem is not stable",
         "claim": "Satya Nadella warned against winner-take-all outcomes, declaring that a "
                  "frontier without an ecosystem is not stable and arguing the political economy "
                  "will never permit an AI future that hollows out entire industries.",
         "domain": "economics", "actor": ["microsoft"],
         "evidences": ["monoculture-is-the-vulnerability", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-14-nations-without-asi-as-intellectual-vassals"]},
    ],
}
