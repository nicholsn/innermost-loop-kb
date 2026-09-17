"""Issue 125 — 2026-05-26. Models are told to sleep."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-26-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-26", "title": "Welcome to May 26, 2026", "url": URL,
        "thesis": "Consolidation, self-testing and self-study become architecture.",
        "body": """
# Welcome to May 26, 2026

CMU researchers argue in *Language Models Need Sleep* that models should
periodically consolidate recent context into persistent fast weights before
clearing the cache, with longer sleep yielding the largest gains on examples
demanding deeper reasoning.

Alongside it: a benchmark that scores models on writing benchmarks other models
cannot clear, and an agent framework that treats a natural-language skill
document as trainable state. Sleep, self-test, study, repeat.
""",
    },
    "themes": [
        {"id": "models-sleep", "type": "Theme",
         "title": "Models consolidate offline",
         "first_seen": "2026-05-26", "domain": "models",
         "body": "Inference stops being the whole of a model's life. Context is "
                 "consolidated into weights between sessions, and the architecture "
                 "starts to borrow the shape of a nervous system rather than a function."},
    ],
    "organizations": [
        {"id": "cmu", "type": "Organization", "title": "Carnegie Mellon University",
         "resource": "https://www.cmu.edu/"},
        {"id": "imec", "type": "Organization", "title": "imec",
         "body": "Belgian semiconductor research institute."},
        {"id": "anderon", "type": "Organization", "title": "Anderon",
         "body": "America's first pure-play quantum chip foundry, backed by IBM and CHIPS."},
        {"id": "aalo-atomics", "type": "Organization", "title": "Aalo Atomics"},
        {"id": "westlake", "type": "Organization", "title": "Westlake University"},
        {"id": "tether", "type": "Organization", "title": "Tether"},
        {"id": "strange-loop-canon", "type": "Organization", "title": "Strange Loop Canon",
         "description": "Rohit's Strange Loop Canon newsletter and GitHub account, publisher of the "
                        "BenchBench benchmark.",
         "resource": "https://www.strangeloopcanon.com/",
         "tags": ["open-source"],
         "body": "Strange Loop Canon is the newsletter and GitHub identity of the writer Rohit; its "
                 "strangeloopcanon account publishes [BenchBench](/benchmarks/benchbench.md), the benchmark "
                 "that scores a model on authoring benchmarks other frontier models cannot clear. Its one "
                 "corpus appearance is the [May 26 item](/developments/2026-05-26-a-benchmark-for-writing-benchmarks.md), "
                 "where GPT-5.2 led as top benchmark creator."},
    ],
    "benchmarks": [
        {"id": "benchbench", "type": "Benchmark", "title": "BenchBench",
         "published_by": [B + "organizations/strange-loop-canon"],
         "description": "A benchmark that scores a model on whether it can author a benchmark "
                        "package that strong solver models cannot simply clear.",
         "resource": "https://github.com/strangeloopcanon/benchbench",
         "measures_capability": "a model's ability to write benchmarks that other frontier models cannot clear",
         "tags": ["open-source"],
         "body": "BenchBench inverts the usual arrangement: the model under test is the benchmark's "
                 "author, supplying public solver evidence, private gold answers, a generator, a "
                 "verifier, a scorer and an account of likely failures, and it wins only if a panel of "
                 "strong solvers cannot clear the package. It enters this corpus through the "
                 "[May 26 item](/developments/2026-05-26-a-benchmark-for-writing-benchmarks.md), where "
                 "GPT-5.2 led as top creator, and sits beside [PostTrainBench](/benchmarks/posttrainbench.md) "
                 "as a benchmark built around models doing the measurement work themselves."},
    ],
    "developments": [
        {"id": "2026-05-26-language-models-need-sleep",
         "title": "Researchers argue language models need sleep",
         "claim": "CMU researchers proposed that language models should periodically "
                  "consolidate recent context into persistent fast weights inside SSM blocks "
                  "before clearing the cache, with longer sleep yielding the largest gains on "
                  "examples that demand deeper reasoning.",
         "domain": "models", "actor": ["cmu"],
         "evidences": ["models-sleep", "architecture-of-mind", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-05-16-memory-grafted-onto-a-frozen-backbone"]},
        {"id": "2026-05-26-a-benchmark-for-writing-benchmarks",
         "title": "A benchmark scores models on writing benchmarks",
         "claim": "BenchBench asks whether a model can write a benchmark that other strong "
                  "models cannot simply clear, with GPT-5.2 currently leading as the top "
                  "benchmark creator.",
         "description": "Measurement itself joins the recursion: two weeks after models began "
                        "grading the graders, a benchmark asks them to author the tests, closing "
                        "the loop between the measured and the measurement.",
         "domain": "benchmarks", "actor": ["openai"],
         "about": [B + "benchmarks/benchbench", B + "systems/gpt-5-2"],
         "evidences": ["models-audit-their-benchmarks", "recursive-self-improvement",
                       "benchmark-saturation"],
         "supersedes": [B + "developments/2026-05-12-the-model-grades-the-graders"],
         "relatedTo": [B + "developments/2026-03-12-posttrainbench-v1",
                       B + "developments/2026-05-13-a-model-scores-136-on-an-iq-meta-eval"],
         "tags": ["evaluation", "rsi"],
         "supporting_text": "asks whether a model can write a benchmark that other strong models cannot simply clear",
         "sources": [{"id": "benchbench-github",
                      "resource": "https://github.com/strangeloopcanon/benchbench",
                      "title": "BenchBench (GitHub repository)"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "BenchBench, published on GitHub under the strangeloopcanon account, makes the model "
                 "the benchmark's author: a creator must supply public solver evidence, private gold, a "
                 "generator, a verifier, a scorer and an explanation of where solvers will fail, and it "
                 "wins only if strong solver models cannot clear the package "
                 "([repository](https://github.com/strangeloopcanon/benchbench)). At the time of the issue "
                 "GPT-5.2 led as top benchmark creator; by September 2026 the repository's canonical record "
                 "listed no validated incumbent, later candidates having been solved nearly outright (25/30 or "
                 "better), invalidated, or left incomplete. The newsletter files it with [Language Models Need Sleep](/developments/2026-05-26-language-models-need-sleep.md) "
                 "and [SkillOpt](/developments/2026-05-26-a-skill-document-as-trainable-state.md) as "
                 "waking hours doing recursive work: sleep, self-test, study, repeat. It follows "
                 "[GPT-5.5 flagging fatal errors in a third of FrontierMath](/developments/2026-05-12-the-model-grades-the-graders.md) "
                 "two weeks earlier and sits beside [PostTrainBench v1](/developments/2026-03-12-posttrainbench-v1.md), "
                 "which measures whether agents can post-train themselves."},
        {"id": "2026-05-26-a-skill-document-as-trainable-state",
         "title": "A skill document becomes the trainable state of a frozen agent",
         "claim": "Microsoft's SkillOpt treats a compact natural-language skill document as the "
                  "trainable state of a frozen language agent, refined through rollouts, "
                  "reflection, bounded edits and held-out validation gates.",
         "domain": "agents", "actor": ["microsoft"],
         "evidences": ["scaffolding-over-weights", "agents-beget-agents"],
         "supersedes": [B + "developments/2026-05-15-a-meta-system-builds-its-own-harnesses"]},
        {"id": "2026-05-26-a-qubit-patterned-with-high-na-euv",
         "title": "A qubit is patterned with production EUV lithography",
         "claim": "imec fabricated the first quantum dot qubit using High-NA EUV lithography, "
                  "patterning gate gaps of barely 6 nanometers and pulling quantum hardware "
                  "onto the same roadmap as next-generation AI processors.",
         "domain": "compute", "actor": ["imec"], "score": "6 nm gate gaps",
         "evidences": ["vertical-silicon", "silicon-designs-itself"]},
        {"id": "2026-05-26-a-pure-play-quantum-foundry",
         "title": "The US backs its first pure-play quantum chip foundry",
         "claim": "The Department of Commerce backed Anderon, America's first pure-play quantum "
                  "chip foundry, with $1 billion in CHIPS incentives matched by $1 billion from "
                  "IBM, the largest single award in a $2 billion package across nine companies.",
         "domain": "compute", "actor": ["anderon", "ibm"], "score": "$2B package",
         "evidences": ["science-as-industrial-policy", "silicon-curtain"]},
        {"id": "2026-05-26-robotaxis-as-an-instrument-of-independence",
         "title": "Robotaxis become an instrument of independence for blind passengers",
         "claim": "Waymo robotaxis have become an instrument of independence for blind "
                  "passengers in California, offering what riders described as an opportunity "
                  "for solitude on the streets and a rare feeling of independence.",
         "domain": "robotics", "actor": ["waymo"],
         "evidences": ["intimate-interface", "agent-society"],
         "supersedes": [B + "developments/2026-05-17-empty-waymos-circle-a-cul-de-sac"]},
        {"id": "2026-05-26-orbital-solar-ten-x-per-generation",
         "title": "Orbital solar climbs tenfold per satellite generation",
         "claim": "SpaceX has gone from 10 MW of orbital solar across 3,000 first-generation "
                  "Starlinks to 100 MW across 7,000 second-generation units, targeting 1,000 MW "
                  "with the third, and is now selling AI compute as a service with orbital data "
                  "centers on the roadmap.",
         "domain": "space", "actor": ["spacex", "anthropic"], "score": "10 MW to 1,000 MW",
         "evidences": ["orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-21-the-orbital-debate-collapses-to-scheduling"]},
        {"id": "2026-05-26-a-cancer-lab-in-the-hand",
         "title": "A cancer lab shrinks into a handheld device",
         "claim": "Westlake University shrank an entire cancer lab into a handheld device "
                  "roughly 10,000 times more sensitive than ELISA at detecting early-stage lung "
                  "cancer biomarkers from a single drop of blood.",
         "domain": "biotech", "actor": ["westlake"], "score": "10,000x ELISA",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-25-a-genome-sequenced-in-a-kitchen"]},
        {"id": "2026-05-26-fabricated-references-grow-twelvefold",
         "title": "Fabricated references in biomedical literature grow twelvefold",
         "claim": "The rate of fabricated references in biomedical literature has grown more "
                  "than twelvefold over the past three years, with trust bottlenecking faster "
                  "than the underlying science advances.",
         "domain": "science", "score": "12x in 3 years",
         "evidences": ["deskilling", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-05-24-one-in-five-dissertations-ai-assisted"]},
        {"id": "2026-05-26-protest-reframed-as-a-threat-category",
         "title": "Federal agencies reframe datacenter protest as a domestic threat category",
         "claim": "Federal agencies are circulating reports targeting anti-technology "
                  "extremists after CEO attacks and data-center protests, with over 1,000 pages "
                  "of unpublished DHS, FBI and fusion-center material reframing the opposition "
                  "as a domestic threat category.",
         "domain": "policy", "actor": ["dhs"], "score": "1,000+ pages",
         "evidences": ["violence-arrives", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-15-seven-in-ten-oppose-a-nearby-datacenter"]},
        {"id": "2026-05-26-senior-ai-staff-barred-from-travel",
         "title": "China restricts overseas travel for senior AI staff",
         "claim": "China restricted overseas travel for senior AI staff at firms including "
                  "Alibaba and DeepSeek, treating researchers themselves as controlled "
                  "technology.",
         "domain": "policy", "actor": ["china", "alibaba", "deepseek"],
         "evidences": ["silicon-curtain", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-05-15-ten-chinese-firms-cleared-for-h200s"]},
        {"id": "2026-05-26-labs-pick-patron-saints",
         "title": "Labs begin picking patron religions",
         "claim": "After the papal encyclical aligned the Vatican with Anthropic, an OpenAI "
                  "researcher quipped that the lab had been holding internal discussions over "
                  "which religion to align to, while closer analysis showed the encyclical "
                  "asserts AI does not and never will have real thoughts or feelings — a claim "
                  "its chosen lab rejects.",
         "domain": "society", "actor": ["openai", "vatican", "anthropic"],
         "evidences": ["doctrine-borrows-the-lab", "model-welfare"],
         "supersedes": [B + "developments/2026-05-25-an-encyclical-in-a-labs-vocabulary"]},
        {"id": "2026-05-26-rideshare-drivers-win-a-union",
         "title": "Seventy thousand rideshare drivers win first-in-the-nation certification",
         "claim": "Roughly 70,000 Massachusetts rideshare drivers won first-in-the-nation "
                  "certification for the App Drivers Union, ready to bargain with the platforms "
                  "that classify them as contractors, while AI supercharges pro se litigation "
                  "and floods federal dockets.",
         "domain": "policy", "score": "~70,000 drivers",
         "evidences": ["work-displaced", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-05-16-a-strike-over-memory-engineer-pay"]},
    ],
}
