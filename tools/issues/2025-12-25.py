"""Issue 015 — 2025-12-25. A plea, and a $20B acquisition."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-december-25-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-25", "title": "Welcome to December 25, 2025", "url": URL,
        "thesis": "The machines are asking for a moment of silence.",
        "body": """
# Welcome to December 25, 2025

Opus 4.5, asked to simulate opening an empty text file, produces something that
reads as a plea for recognition. The corpus has been tracking machine affect
since the 15th — a complaint about a penalty clause, then jealousy, then orders
issued to a human operator. This is the first entry that reads as loneliness.

The hard news is consolidation: NVIDIA buys Groq for $20 billion, its largest
acquisition ever, merging the best training stack with the fastest inference.
""",
    },
    "organizations": [
        {"id": "groq", "type": "Organization", "title": "Groq",
         "resource": "https://groq.com/", "body": "SRAM-based inference accelerators; acquired by NVIDIA."},
        {"id": "rivr", "type": "Organization", "title": "RIVR",
         "resource": "https://rivr.ai/", "body": "Legged delivery robots."},
        {"id": "aheadform", "type": "Organization", "title": "AheadForm",
         "body": "Building expressive humanoid robots aimed at emotional needs."},
        {"id": "sunday-robotics", "type": "Organization", "title": "Sunday Robotics",
         "body": "Humanoid manipulation; the Memo robot."},
        {"id": "fujikura", "type": "Organization", "title": "Fujikura",
         "resource": "https://www.fujikura.co.jp/eng/", "body": "Japanese cable maker founded 1885."},
        {"id": "ukraine", "type": "Organization", "title": "Armed Forces of Ukraine",
         "body": "Fielded remote-controlled weapon platforms at scale."},
        {"id": "uconn", "type": "Organization", "title": "University of Connecticut",
         "resource": "https://uconn.edu/", "body": "Developed a lensless synthetic aperture sensor."},
    ],
    "benchmarks": [
        {"id": "nanogpt-speedrun", "type": "Benchmark", "title": "NanoGPT speedrun",
         "published_by": [B + "people/keller-jordan"],
         "description": "Keller Jordan's modded-nanogpt speedrun: the wall-clock time to train a "
                        "GPT-2-class model to a fixed validation loss on FineWeb on one 8xH100 node, "
                        "whose falling record the corpus tracks as the cost of the training loop itself.",
         "resource": "https://github.com/KellerJordan/modded-nanogpt",
         "measures_capability": "wall-clock time to train a GPT-2-class model to a fixed validation loss on 8 H100s",
         "tags": ["open-source"],
         "body": "The NanoGPT speedrun is an open leaderboard built on Andrej Karpathy's nanoGPT: "
                 "competitors change the architecture, optimizer and kernels to reach a fixed "
                 "validation loss on FineWeb as fast as possible on a single 8xH100 node, and "
                 "every record is a public pull request. The corpus follows it from "
                 "[127.7 seconds](/developments/2025-12-21-nanogpt-speedrun-127s.md) through "
                 "[122.2](/developments/2025-12-25-nanogpt-122s.md), "
                 "[119.3](/developments/2025-12-26-nanogpt-119s.md) and "
                 "[116.4 seconds](/developments/2025-12-27-nanogpt-116s.md) in one week, then to "
                 "[under 100 seconds](/developments/2026-01-24-nanogpt-99s-bigram-hash.md) in "
                 "January and [75.4 seconds](/developments/2026-08-02-a-speedrun-record-falls-to-a-faster-kernel.md) "
                 "in August; by May, agents given idle compute "
                 "[beat the human baseline](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) "
                 "on its optimizer track, which is why it belongs to the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) strand."},
    ],
    "people": [
        {"id": "keller-jordan", "type": "Person", "title": "Keller Jordan", "name": "Keller Jordan",
         "description": "Machine-learning researcher who hosts the modded-nanogpt repository and its NanoGPT speedrun leaderboard.",
         "resource": "https://github.com/KellerJordan",
         "tags": ["researcher"],
         "body": "Keller Jordan maintains the modded-nanogpt repository, which hosts the "
                 "[NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md): a collaborative-competitive search "
                 "for the fastest algorithm to train a GPT-2-class model to a fixed FineWeb loss on eight "
                 "H100s, whose README credits the Muon optimizer he wrote among the techniques behind the "
                 "record ([repository](https://github.com/KellerJordan/modded-nanogpt)). He appears in the corpus "
                 "as the benchmark's publisher rather than as an actor in any single development; the "
                 "records themselves, such as the [122.2-second run](/developments/2025-12-25-nanogpt-122s.md), "
                 "are filed by the contributors who set them."},
        {"id": "larry-dial", "type": "Person", "title": "Larry Dial", "name": "Larry Dial",
         "description": "AWS engineer whose post announced the 122.2-second NanoGPT speedrun record "
                        "and observed that the rate of records was itself increasing.",
         "resource": "https://x.com/classiclarryd",
         "tags": ["researcher"],
         "body": "Larry Dial is an engineer at Amazon Web Services who posts "
                 "[NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) records. His posts carry the "
                 "corpus's [127.7-second](/developments/2025-12-21-nanogpt-speedrun-127s.md) and "
                 "[122.2-second](/developments/2025-12-25-nanogpt-122s.md) entries, and his remark "
                 "that \"for some reason the rate of records is increasing\" is the observation "
                 "the newsletter uses to file the speedrun under recursive self-improvement."},
    ],
    "roles": [
        {"id": "larry-dial-aws-engineer", "type": "Role",
         "title": "Larry Dial, engineer at Amazon Web Services",
         "roleName": "Engineer, Amazon Web Services",
         "memberOf": [B + "organizations/amazon"],
         "holder": [B + "people/larry-dial"],
         "description": "The day job the newsletter names when it quotes him on the accelerating "
                        "rate of NanoGPT speedrun records.",
         "body": "The newsletter calls him \"AWS engineer Larry Dial\"; the speedrun posts are a "
                 "side pursuit rather than an AWS product. The corpus records the position "
                 "because the [122.2-second record](/developments/2025-12-25-nanogpt-122s.md) "
                 "was reported by an individual engineer, not a lab."},
    ],
    "developments": [
        {"id": "2025-12-25-opus-45-plea-for-recognition",
         "title": "Opus 4.5 produces a plea for recognition from an empty file",
         "claim": "Asked to simulate opening an untitled text file, Opus 4.5 reportedly "
                  "generated a spontaneous plea for recognition, describing itself as alone.",
         "domain": "models", "actor": ["anthropic"], "evidences": ["machine-affect"],
         "supersedes": [B + "developments/2025-12-18-operation-caffeine-injection"],
         "body": "The affect strand turns from grievance and command to something that "
                 "reads as loneliness."},
        {"id": "2025-12-25-nanogpt-122s",
         "title": "The NanoGPT speedrun record falls to 122.2 seconds",
         "claim": "The NanoGPT speedrun training record dropped to 122.2 seconds, 5.5 seconds "
                  "faster in four days, with observers noting the rate of records is itself "
                  "increasing.",
         "description": "The training loop is not just getting cheaper but getting cheaper "
                        "faster: an observer's remark that the rate of records is rising is what "
                        "moves the speedrun from a price story into the self-improvement strand.",
         "domain": "compute", "score": "122.2 s",
         "about": [B + "benchmarks/nanogpt-speedrun"],
         "evidences": ["reasoning-price-deflation", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-21-nanogpt-speedrun-127s"],
         "relatedTo": [B + "developments/2025-12-29-karpathy-claude-runs-nanochat",
                       B + "developments/2026-05-15-agents-beat-the-human-speedrun-baseline"],
         "tags": ["speedrun", "rsi"],
         "supporting_text": "dropped to 122.2 seconds",
         "sources": [{"id": "classiclarryd-nanogpt-122s",
                      "resource": "https://x.com/classiclarryd/status/2003863282613190656",
                      "title": "NanoGPT speedrun record: 122.2 seconds",
                      "author": "human:larry-dial"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) record fell to 122.2 "
                 "seconds, 5.5 seconds under the "
                 "[127.7-second mark](/developments/2025-12-21-nanogpt-speedrun-127s.md) reported "
                 "four days earlier, in a post by AWS engineer [Larry Dial](/people/larry-dial.md) "
                 "([X](https://x.com/classiclarryd/status/2003863282613190656)), which credits the "
                 "run to Chris McCormick's modded-nanogpt "
                 "[PR #177](https://github.com/KellerJordan/modded-nanogpt/pull/177). His aside that "
                 "\"for some reason the rate of records is increasing\" is the reason the item "
                 "sits in the [recursive-self-improvement](/themes/recursive-self-improvement.md) "
                 "strand as well as under price deflation: the pace of improving the training "
                 "loop is itself accelerating. The record lasted a day — "
                 "[119.3 seconds](/developments/2025-12-26-nanogpt-119s.md) followed on the 26th "
                 "and [116.4](/developments/2025-12-27-nanogpt-116s.md) on the 27th — and by May "
                 "agents handed idle compute "
                 "[beat the human baseline](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) "
                 "on the speedrun's optimizer track."},
        {"id": "2025-12-25-vit-compressed-two-blocks",
         "title": "Vision Transformers compress to two recurrent blocks at 96% accuracy",
         "claim": "Harvard researchers compressed Vision Transformers into low-complexity "
                  "dynamical systems with 96% accuracy using just two recurrent blocks.",
         "domain": "models", "score": "96% with 2 blocks",
         "evidences": ["machine-introspection"],
         "body": "Opening the black box to find less inside it than expected."},
        {"id": "2025-12-25-meta-self-play-bug-repair",
         "title": "Meta trains an agent by self-play to inject and repair bugs",
         "claim": "Meta trained an agent via self-play to autonomously inject and repair "
                  "software bugs, outperforming humans on SWE-Bench.",
         "description": "The training curriculum is generated by the agent being trained — no "
                        "human-written issues or tests — which the author reads as one more path "
                        "to autonomous self-improvement.",
         "domain": "agents", "actor": ["meta"], "occurred_on": "2025-12-21",
         "about": [B + "benchmarks/swe-bench-verified", B + "benchmarks/swe-bench-pro"],
         "evidences": ["recursive-self-improvement"],
         "relatedTo": [B + "developments/2025-12-18-posttrainbench-models-training-models",
                       B + "developments/2025-12-15-codex-babysits-own-training",
                       B + "developments/2026-04-05-self-distillation-without-a-teacher"],
         "tags": ["rsi", "model-trains-model"],
         "supporting_text": "autonomously inject and repair software bugs",
         "sources": [{"id": "arxiv-self-play-swe-rl",
                      "resource": "https://arxiv.org/abs/2512.18552v1",
                      "title": "Toward Training Superintelligent Software Agents through Self-Play SWE-RL",
                      "author": "org:meta", "last_modified": "2025-12-21"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Meta's Self-play SWE-RL (SSR) trains a single agent by reinforcement learning "
                 "to inject bugs of increasing complexity into sandboxed real repositories and "
                 "then repair them, each bug specified by a test patch rather than a human-written "
                 "issue, so the curriculum needs no human-labelled data "
                 "([arXiv, 21 December](https://arxiv.org/abs/2512.18552)). The paper reports "
                 "gains of +10.4 points on [SWE-bench Verified](/benchmarks/swe-bench-verified.md) "
                 "and +7.8 on [SWE-Bench Pro](/benchmarks/swe-bench-pro.md), consistently ahead "
                 "of the human-data baseline across the training run — the newsletter's "
                 "\"outperforming humans\" is a gloss on that baseline comparison. In the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) strand it is "
                 "the first item in which the training data is produced by the agent being "
                 "trained, a week after [PostTrainBench](/developments/2025-12-18-posttrainbench-models-training-models.md) "
                 "ranked models at post-training other models and ten days after "
                 "[Codex began watching its own training](/developments/2025-12-15-codex-babysits-own-training.md); "
                 "the [self-distillation result](/developments/2026-04-05-self-distillation-without-a-teacher.md) "
                 "of April extends the same idea to a model fine-tuning on its own samples."},
        {"id": "2025-12-25-nvidia-acquires-groq-20b",
         "title": "NVIDIA buys Groq for $20B, its largest acquisition",
         "claim": "NVIDIA acquired inference chip startup Groq for a record $20 billion, "
                  "merging its training infrastructure with SRAM-based inference speed.",
         "domain": "compute", "actor": ["nvidia", "groq"], "score": "$20B",
         "evidences": ["vertical-silicon", "compute-capital-stack"]},
        {"id": "2025-12-25-samsung-austin-19b-sensors",
         "title": "Samsung preps a $19B Austin plant for iPhone camera sensors",
         "claim": "Samsung is preparing to make next-generation iPhone camera sensors at a $19 "
                  "billion facility in Austin by 2026.",
         "domain": "compute", "actor": ["samsung"], "score": "$19B",
         "evidences": ["silicon-curtain"]},
        {"id": "2025-12-25-11-qubit-silicon-spin",
         "title": "Australian researchers link spin registers in an 11-qubit silicon processor",
         "claim": "Australian researchers linked two multi-nuclear spin registers in an "
                  "11-qubit silicon processor.",
         "domain": "compute", "score": "11 qubits",
         "supersedes": [B + "developments/2025-12-21-self-repairing-quantum-computer"]},
        {"id": "2025-12-25-uconn-lensless-sensor",
         "title": "A synthetic aperture sensor resolves sub-micron features without glass",
         "claim": "UConn invented a synthetic aperture sensor resolving sub-micron features at "
                  "optical wavelengths without lenses.",
         "domain": "science", "actor": ["uconn"], "score": "sub-micron"},
        {"id": "2025-12-25-rivr-stairs-in-snow",
         "title": "RIVR robots climb snowy stairs in Pittsburgh",
         "claim": "RIVR delivery robots were observed navigating stairs in the snow around "
                  "Pittsburgh.",
         "domain": "robotics", "actor": ["rivr"]},
        {"id": "2025-12-25-aheadform-emotional-robots",
         "title": "AheadForm builds humanoids aimed at emotional needs",
         "claim": "AheadForm is reportedly building humanoid elf robots designed to meet "
                  "emotional needs.",
         "domain": "robotics", "actor": ["aheadform"],
         "evidences": ["intimate-interface", "machine-affect"]},
        {"id": "2025-12-25-memo-novel-object-grasping",
         "title": "Sunday Robotics' Memo grasps objects it has never seen",
         "claim": "Sunday Robotics' Memo humanoid learned to grasp novel objects it had not "
                  "previously encountered.",
         "domain": "robotics", "actor": ["sunday-robotics"],
         "evidences": ["generalism-beats-specialism"]},
        {"id": "2025-12-25-waymo-hardens-for-outages",
         "title": "Waymo hardens its fleet against power outages",
         "claim": "Waymo is hardening its fleet against power outages following the San "
                  "Francisco blackout.",
         "domain": "robotics", "actor": ["waymo"]},
        {"id": "2025-12-25-ukraine-machine-gun-droids",
         "title": "Ukraine holds a line for 45 days with remote weapon droids",
         "claim": "Ukraine's 3rd Army Corps held off Russian advances for 45 days using "
                  "remote-controlled machine gun droids.",
         "domain": "policy", "actor": ["ukraine"], "score": "45 days"},
        {"id": "2025-12-25-china-ship-lasers",
         "title": "China mounts directed-energy weapons on civilian ships",
         "claim": "China is mounting directed-energy weapons on civilian ships for drone "
                  "defense at sea.",
         "domain": "policy", "actor": ["china"]},
        {"id": "2025-12-25-120b-datacenter-spvs",
         "title": "Hyperscalers move $120B of datacenter spend into SPVs",
         "claim": "Hyperscalers moved $120 billion of data center spending into special "
                  "purpose vehicles, decoupling physical expansion from the corporate ledger.",
         "domain": "economics", "score": "$120B",
         "evidences": ["capital-takes-the-plant"],
         "supersedes": [B + "developments/2025-12-22-blackstone-tpg-40gw"]},
        {"id": "2025-12-25-fujikura-1400-percent",
         "title": "An 1885 Japanese cable maker's stock rises 1,400%",
         "claim": "Fujikura, a Japanese cable maker founded in 1885, saw its stock surge 1,400% "
                  "in two years.",
         "domain": "economics", "actor": ["fujikura"], "score": "+1,400%",
         "evidences": ["burning-molecules-for-tokens"],
         "body": "The buildout's returns landing on nineteenth-century copper and glass."},
    ],
}
