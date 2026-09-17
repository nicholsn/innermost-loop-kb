"""Issue 094 — 2026-04-09. Human-written code becomes the hazard."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-9-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-09", "title": "Welcome to April 9, 2026", "url": URL,
        "thesis": "The most dangerous thing in the room becomes the hand-written loop.",
        "body": """
# Welcome to April 9, 2026

After Mythos, commentators argue it will be unsafe for humans to write code at
all, given superhuman vulnerability discovery. An inversion: the hazard is no
longer the model but the artisanal for-loop.

Scott Wu notes global FLOPs growing about 3x a year against inference demand
growing 10x — a scissor that forecasts price rises and a flight to smaller
models.
""",
    },
    "organizations": [
        {"id": "tubi", "type": "Organization", "title": "Tubi",
         "resource": "https://tubitv.com/"},
        {"id": "syncere", "type": "Organization", "title": "Syncere",
         "body": "Lamp-shaped home robot pitched as doing chores."},
        {"id": "ubs", "type": "Organization", "title": "UBS",
         "resource": "https://www.ubs.com/"},
    ],
    "developments": [
        {"id": "2026-04-09-human-written-code-called-unsafe",
         "title": "Commentators argue it is now unsafe for humans to write code",
         "claim": "In the wake of the Mythos announcement, commentators warned it will be "
                  "unsafe for humans to write code at all given the model's superhuman "
                  "vulnerability discovery, inverting which artifact in the room is the hazard.",
         "domain": "agents", "actor": ["anthropic"],
         "evidences": ["engineer-as-supervisor", "deskilling", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-04-08-project-glasswing"]},
        {"id": "2026-04-09-seven-models-in-training-at-once",
         "title": "One cluster runs seven simultaneous training runs",
         "claim": "Elon Musk said Colossus 2 now has seven models in training from an image "
                  "variant through twin trillion and 1.5-trillion-parameter models up to a "
                  "ten-trillion-parameter system, each pretraining run lasting roughly two "
                  "months, while a leaked memo from the merged company's president admitted the "
                  "lab is clearly behind the other frontier shops.",
         "domain": "models", "actor": ["xai", "spacex"], "score": "7 runs / up to 10T",
         "evidences": ["compute-capital-stack", "spiky-frontier"],
         "body": "Seven simultaneous runs cannot by themselves manufacture taste."},
        {"id": "2026-04-09-mythos-trained-on-blackwells",
         "title": "The first model class trained at scale on Blackwell arrives mid-handoff",
         "claim": "Mythos appears to be the first model class trained at scale on Blackwell "
                  "hardware with Vera Rubin waiting, a generational handoff occurring while "
                  "pre-training still has headroom and fresh compute is only beginning to land, "
                  "as OpenAI finalized its own staggered rollout of a cyber model to selected "
                  "partners.",
         "domain": "compute", "actor": ["anthropic", "nvidia", "openai"],
         "evidences": ["vertical-silicon", "spiky-frontier"]},
        {"id": "2026-04-09-you-ship-the-org-chart-you-have",
         "title": "A model crushes data-quality benchmarks and flubs reasoning ones",
         "claim": "Meta's Muse Spark was characterized as crushing data-quality benchmarks "
                  "while flubbing reasoning ones, while Alibaba anonymously released a video "
                  "model that seized first place on text-to-video and image-to-video "
                  "leaderboards.",
         "domain": "models", "actor": ["meta-superintelligence", "alibaba"],
         "evidences": ["spiky-frontier", "open-weight-latency"],
         "supersedes": [B + "developments/2026-04-08-meta-superintelligence-ships-muse-spark"]},
        {"id": "2026-04-09-in-place-test-time-training",
         "title": "A 4B model dominates long context by rewriting its own weights in flight",
         "claim": "ByteDance introduced in-place test-time training, repurposing projection "
                  "matrices as fast weights so a four-billion-parameter model can dominate at "
                  "128,000 tokens of context.",
         "description": "Self-improvement moves from the scaffold into the weights: a deployed "
                        "model updates part of itself on each input stream, making adaptation a "
                        "property of inference rather than of a retraining cycle.",
         "domain": "models", "actor": ["bytedance"], "score": "4B at 128k context",
         "evidences": ["architecture-of-mind", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-04-05-self-distillation-without-a-teacher",
                        B + "developments/2025-12-30-stanford-test-time-training"],
         "relatedTo": [B + "developments/2026-01-04-rlm-two-orders-of-context",
                       B + "developments/2026-03-16-million-token-windows-ship"],
         "tags": ["test-time-training", "continual-learning", "self-modification", "rsi"],
         "supporting_text": "repurposing MLP projection matrices as fast weights so a 4B model can dominate at 128k",
         "sources": [{"id": "in-place-ttt-arxiv",
                      "resource": "https://arxiv.org/abs/2604.06169",
                      "title": "In-Place Test-Time Training", "author": "org:bytedance"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The paper ([arXiv 2604.06169](https://arxiv.org/abs/2604.06169)) makes the final "
                 "projection matrix of every MLP block the model's fast weights, swaps test-time "
                 "training's usual reconstruction loss for an objective tied to next-token "
                 "prediction, and updates in chunks so the method runs under context parallelism; "
                 "applied in place to an existing 4B-parameter model it gives superior results on "
                 "tasks with contexts up to 128k tokens, and the same recipe also works when "
                 "pretrained from scratch. The newsletter's framing is that ByteDance is 'making "
                 "old models smarter mid-flight', a drop-in answer to the long-context problem "
                 "that Anthropic had addressed weeks earlier with "
                 "[million-token windows](/developments/2026-03-16-million-token-windows-ship.md) "
                 "and Prime Intellect with "
                 "[recursive self-calls](/developments/2026-01-04-rlm-two-orders-of-context.md). "
                 "In the [recursive-self-improvement](/themes/recursive-self-improvement.md) "
                 "trajectory it extends Stanford's "
                 "[constant-latency test-time training](/developments/2025-12-30-stanford-test-time-training.md) "
                 "from December and Apple's "
                 "[teacherless self-distillation](/developments/2026-04-05-self-distillation-without-a-teacher.md) "
                 "of four days earlier: the model modifies its own weights during use rather than "
                 "between training runs."},
        {"id": "2026-04-09-five-more-erdos-problems",
         "title": "Five more Erdős problems close across three fields",
         "claim": "OpenAI researchers solved five more Erdős problems across combinatorics, "
                  "probability and number theory.",
         "domain": "science", "actor": ["openai"], "score": "5 problems",
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-04-05-a-textbook-formalized-by-30000-agents"]},
        {"id": "2026-04-09-flops-grow-3x-demand-grows-10x",
         "title": "Compute grows 3x a year while demand for it grows 10x",
         "claim": "Cognition's Scott Wu noted global FLOPs are growing roughly threefold "
                  "annually while inference demand grows tenfold, a scissor forecasting price "
                  "rises and a flight to smaller, leaner models.",
         "domain": "economics", "actor": ["cognition"], "score": "3x vs 10x",
         "evidences": ["infrastructure-crowding-out", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-04-07-samsung-profit-up-eightfold"]},
        {"id": "2026-04-09-a-streamer-inside-the-chat-window",
         "title": "A streaming service launches a native app inside a chatbot",
         "claim": "Tubi became the first major streamer to launch a native app inside ChatGPT, "
                  "while Perplexity's annual run rate doubled to $500 million since the new "
                  "year and Google folded its research notebooks into the Gemini app.",
         "domain": "economics", "actor": ["tubi", "openai", "perplexity", "google"],
         "score": "$500M ARR",
         "evidences": ["autonomous-commerce", "intimate-interface"]},
        {"id": "2026-04-09-a-home-robot-shaped-like-a-lamp",
         "title": "The first mass-market home robot may arrive disguised as furniture",
         "claim": "Syncere unveiled a lamp-shaped robot pitched as doing household chores, "
                  "suggesting the first mass-market home robot will not be a humanoid but "
                  "furniture people already own.",
         "domain": "robotics", "actor": ["syncere"],
         "evidences": ["physical-recursion", "intimate-interface"],
         "supersedes": [B + "developments/2026-04-07-companion-dolls-for-the-elderly"]},
        {"id": "2026-04-09-openai-pauses-its-uk-buildout",
         "title": "OpenAI pauses a UK buildout over energy and regulation",
         "claim": "OpenAI paused its UK Stargate buildout citing energy costs and regulation, "
                  "while Epoch AI calculated Chinese and open labs are running on roughly ten "
                  "times less compute than the frontier, and Meta committed an additional $21 "
                  "billion to CoreWeave through 2032.",
         "domain": "compute", "actor": ["openai", "epoch-ai", "meta", "coreweave"],
         "score": "$21B / 10x gap",
         "evidences": ["infrastructure-crowding-out", "silicon-curtain"],
         "supersedes": [B + "developments/2026-04-07-anthropic-run-rate-triples-in-a-quarter"]},
        {"id": "2026-04-09-a-wind-turbine-inside-a-coal-mine",
         "title": "Germany builds the tallest wind turbine inside a coal mine",
         "claim": "Germany is building the world's tallest wind turbine at 364 metres inside a "
                  "coal mine.",
         "domain": "energy", "score": "364 m",
         "evidences": ["burning-molecules-for-tokens", "industrialized-nature"]},
        {"id": "2026-04-09-a-cashflow-model-prices-nvidia-at-22-trillion",
         "title": "An old-school valuation model puts Nvidia's fair value at $22 trillion",
         "claim": "UBS's cash-flow valuation model pegged Nvidia's fair value at $22 trillion, "
                  "while OpenAI's chief financial officer said retail investors will certainly "
                  "get listing shares after strong individual demand.",
         "domain": "economics", "actor": ["ubs", "nvidia", "openai"], "score": "$22T",
         "evidences": ["compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-02-spacex-files-for-the-largest-tech-listing"]},
        {"id": "2026-04-09-life-biosciences-raises-80m",
         "title": "Anti-aging gene therapy enters clinical testing",
         "claim": "Life Biosciences raised $80 million to begin clinical testing of its "
                  "anti-aging gene therapy, while GLP-1 drugs are projected to add $13 billion "
                  "in apparel sales as Americans shrink out of their wardrobes.",
         "domain": "biotech", "actor": ["life-biosciences"], "score": "$80M / $13B",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-04-05-an-appetite-suppressant-from-python-blood"]},
    ],
}
