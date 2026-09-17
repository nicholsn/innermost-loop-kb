"""Issue 200 — 2026-08-04. Source code becomes assembly."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-4-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-04", "title": "Welcome to August 4, 2026", "url": URL,
        "thesis": "The difficulty of building software is trending to zero.",
        "body": """
# Welcome to August 4, 2026

Elon Musk argues source code is on the verge of becoming like assembly, with AI
emitting the binary directly. One founder notes SaaS multiples fell from 18x
revenue to 3.4x because the difficulty of building software is trending to zero,
leaving distribution as the one asset a model cannot clone.

And a proctoring AI lost to a test-taking AI: 58,000 university applicants must
sit their entrance exam again.
""",
    },
    "themes": [
        {"id": "source-code-becomes-assembly", "type": "Theme",
         "title": "The layer humans read stops being the layer that matters",
         "first_seen": "2026-08-04", "domain": "models",
         "body": "Assembly did not disappear; it stopped being where the work "
                 "happened. If models emit working systems directly, source code "
                 "becomes an intermediate representation humans consult rather than "
                 "the artifact they author."},
        {"id": "the-proctor-loses-to-the-taker", "type": "Theme",
         "title": "Detection loses to generation at institutional scale",
         "first_seen": "2026-08-04", "domain": "society",
         "body": "An exam scored by AI and taken with AI resolves in favour of the "
                 "taker. When the result is implausible enough to void, the "
                 "institution learns that its assessment technology has been "
                 "outclassed — and has no replacement ready."},
    ],
    "organizations": [
        {"id": "asari-ai", "type": "Organization", "title": "Asari AI",
         "description": "Startup building self-improving co-inventor agents that design and optimize high-performance infrastructure, whose rebuild of the inference stack serving two open models is the corpus's first agent-driven result at the serving layer.",
         "resource": "https://asari.ai/",
         "tags": ["startup", "research-agent"],
         "body": "Asari AI builds what it calls [co-inventors](/systems/asari-co-inventor.md): self-improving agents that "
                 "design and optimize high-performance infrastructure ([site](https://asari.ai/)). In this corpus it "
                 "appears once, when those agents "
                 "[rebuilt the inference stack](/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on.md) "
                 "serving [DeepSeek v4 Pro](/systems/deepseek-v4-pro.md) and [GLM 5.2](/systems/glm-5-2.md) on "
                 "[B200s](/hardware/nvidia-b200.md), lifting throughput and interactivity by up to 16%: the loop "
                 "applied to the serving layer rather than to training or to individual kernels."},
        {"id": "intology", "type": "Organization", "title": "Intology",
         "description": "Startup whose Locus agent post-trains models unsupervised and leads PostTrainBench, the corpus's benchmark for a model's skill at training other models.",
         "resource": "https://intology.ai/",
         "tags": ["startup", "research-agent"],
         "body": "Intology builds autonomous research agents; its [Locus](/systems/locus.md) agent post-trains language "
                 "models without human supervision. In this corpus it appears when Locus "
                 "[took the lead on PostTrainBench](/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on.md) "
                 "in ten H100-hours and beat human tuners on the harder variant, overtaking the "
                 "[Sol post-trains Luna](/developments/2026-07-10-a-model-post-trains-a-model.md) result that had made "
                 "[PostTrainBench](/benchmarks/posttrainbench.md) the yardstick for a model training a model."},
        {"id": "volta", "type": "Organization", "title": "Volta"},
        {"id": "unam", "type": "Organization", "title": "UNAM"},
        {"id": "mariana-minerals", "type": "Organization", "title": "Mariana Minerals"},
    ],
    "systems": [
        {"id": "asari-co-inventor", "type": "AISystem", "title": "Asari co-inventor agents",
         "developed_by": [B + "organizations/asari-ai"], "modality": "research agent",
         "description": "Asari AI's self-improving agents for designing and optimizing high-performance infrastructure, which rebuilt the vLLM inference stack serving two open models on B200s.",
         "resource": "https://asari.ai/blog/inference-optimization",
         "tags": ["research-agent"],
         "body": "Asari AI calls its agents co-inventors: self-improving systems that design and optimize "
                 "high-performance infrastructure through a rigorous improvement process. In this corpus they appear "
                 "once, [rebuilding the inference stack](/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on.md) "
                 "for [DeepSeek v4 Pro](/systems/deepseek-v4-pro.md) and [GLM 5.2](/systems/glm-5-2.md) on "
                 "[NVIDIA B200s](/hardware/nvidia-b200.md) running vLLM, lifting throughput and interactivity by up to "
                 "16% while preserving model behaviour through distribution-level correctness checks "
                 "([Asari blog](https://asari.ai/blog/inference-optimization))."},
        {"id": "deepseek-v4-pro", "type": "AISystem", "title": "DeepSeek v4 Pro",
         "developed_by": [B + "organizations/deepseek"], "modality": "text",
         "description": "DeepSeek's open-weight flagship of mid-2026, one of the two large open-source LLMs whose B200 serving stack Asari's agents rebuilt.",
         "resource": "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro",
         "tags": ["open-weight-model"],
         "body": "DeepSeek v4 Pro is the larger variant of [DeepSeek](/organizations/deepseek.md)'s fourth-generation "
                 "open-weight model family. In this corpus it appears as one of the two open models whose full "
                 "inference stack Asari AI's co-inventor agents "
                 "[rebuilt on B200s](/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on.md) for up "
                 "to 16% more throughput and interactivity, the serving layer entering the loop after kernels and "
                 "harnesses."},
        {"id": "locus", "type": "AISystem", "title": "Locus",
         "developed_by": [B + "organizations/intology"], "modality": "research agent",
         "evaluated_on": [B + "benchmarks/posttrainbench"],
         "description": "Intology's autonomous research agent, which post-trains language models unsupervised and leads PostTrainBench.",
         "resource": "https://intology.ai/blog/scaling-automated-post-training",
         "tags": ["research-agent"],
         "body": "Locus is [Intology](/organizations/intology.md)'s autonomous research agent for post-training. In this "
                 "corpus it [leads PostTrainBench](/developments/2026-08-04-agents-rebuild-the-inference-stack-they-run-on.md) "
                 "after post-training models unsupervised in ten H100-hours and beating human tuners on the harder "
                 "variant ([Intology blog](https://intology.ai/blog/scaling-automated-post-training)), overtaking the "
                 "[Sol post-trains Luna](/developments/2026-07-10-a-model-post-trains-a-model.md) result on "
                 "[PostTrainBench](/benchmarks/posttrainbench.md) and continuing the "
                 "[model-trains-a-model](/themes/a-model-trains-a-model.md) line that began when the benchmark "
                 "[first ranked models at post-training](/developments/2025-12-18-posttrainbench-models-training-models.md)."},
    ],
    "developments": [
        {"id": "2026-08-04-agents-rebuild-the-inference-stack-they-run-on",
         "title": "Self-improving agents rebuild the inference stack serving two open models",
         "claim": "Asari AI's self-improving co-inventor agents rebuilt the inference stack for "
                  "two open models on B200s, lifting throughput and interactivity up to 16%, "
                  "while Intology's Locus agent led PostTrainBench by post-training models "
                  "unsupervised in ten H100-hours and beating human tuners on the harder variant.",
         "description": "The Singularity filing its own optimization tickets: the loop reaches the serving layer, "
                        "the last piece of infrastructure between a model and its users, and the post-training "
                        "pipeline in the same week.",
         "domain": "agents", "actor": ["asari-ai", "intology"], "score": "up to 16%",
         "evidences": ["recursive-self-improvement", "a-model-trains-a-model", "optimizing-its-own-invoice"],
         "about": [B + "systems/asari-co-inventor", B + "systems/deepseek-v4-pro", B + "systems/glm-5-2",
                   B + "hardware/nvidia-b200", B + "systems/locus", B + "benchmarks/posttrainbench"],
         "supersedes": [B + "developments/2026-08-03-sixteen-days-alone-and-265-commits",
                        B + "developments/2026-07-10-a-model-post-trains-a-model",
                        B + "developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price"],
         "relatedTo": [B + "developments/2026-04-29-a-model-writes-the-kernels-that-run-it",
                       B + "developments/2026-07-04-agents-write-the-kernels-closing-a-software-gap",
                       B + "developments/2026-03-12-posttrainbench-v1"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-07-10-a-model-post-trains-a-model",
                        "relation_label": "extends"}],
         "tags": ["rsi", "kernels", "model-trains-model", "autonomous-research"],
         "supporting_text": "DeepSeek v4 Pro and GLM 5.2 on B200s, lifting throughput and interactivity up to 16%",
         "sources": [{"id": "asari-inference-optimization-blog",
                      "resource": "https://asari.ai/blog/inference-optimization",
                      "title": "Speeding up end-to-end inference with self-improving agents",
                      "author": "org:asari-ai", "last_modified": "2026-07-28"},
                     {"id": "intology-scaling-automated-post-training",
                      "resource": "https://intology.ai/blog/scaling-automated-post-training",
                      "title": "Scaling Automated Post-Training", "author": "org:intology",
                      "last_modified": "2026-08-03"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Asari AI's [co-inventor agents](/systems/asari-co-inventor.md) optimized the full vLLM serving stack "
                 "for [DeepSeek v4 Pro](/systems/deepseek-v4-pro.md) and [GLM 5.2](/systems/glm-5-2.md) on "
                 "[NVIDIA B200s](/hardware/nvidia-b200.md), improving throughput and interactivity by up to 16% across "
                 "concurrency levels while preserving model behaviour through distribution-level correctness checks "
                 "([Asari blog](https://asari.ai/blog/inference-optimization)). In the same issue Intology's "
                 "[Locus](/systems/locus.md) took the top of [PostTrainBench](/benchmarks/posttrainbench.md) by "
                 "post-training models unsupervised in ten H100-hours and beating human tuners on the harder variant "
                 "([Intology blog](https://intology.ai/blog/scaling-automated-post-training)), overtaking the "
                 "[Sol post-trains Luna](/developments/2026-07-10-a-model-post-trains-a-model.md) result of July. "
                 "Together they extend the loop from "
                 "[production kernels](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) and "
                 "[self-evolving harnesses](/developments/2026-08-03-sixteen-days-alone-and-265-commits.md) to the "
                 "serving stack and the post-training pipeline, two more of the layers between a model and its own "
                 "next version; four days later Poetiq's "
                 "[self-optimizing optimizer](/developments/2026-08-08-a-self-optimizing-optimizer.md) makes the same "
                 "claim for the harness layer."},
        {"id": "2026-08-04-rebuilding-whole-projects-from-scratch",
         "title": "A benchmark tests rebuilding whole projects from scratch and passing every test",
         "claim": "On MirrorCode, which tests whether agents can rebuild whole software projects "
                  "from scratch and pass every test, Claude Fable 5 solves 64% to GPT-5.6 Sol's "
                  "20%.",
         "domain": "benchmarks", "actor": ["anthropic", "openai"], "score": "64% vs 20%",
         "evidences": ["benchmark-saturation", "source-code-becomes-assembly", "spiky-frontier"],
         "supersedes": [B + "developments/2026-08-03-the-floor-drops-faster-than-the-ceiling-rises"]},
        {"id": "2026-08-04-source-code-on-the-verge-of-becoming-assembly",
         "title": "A founder says source code is on the verge of becoming like assembly",
         "claim": "Elon Musk argued source code is on the verge of becoming like assembly with AI "
                  "emitting the binary directly, while one founder noted SaaS multiples fell from "
                  "18 times revenue to 3.4 because the difficulty of building software is "
                  "trending to zero, leaving distribution as the one asset a model cannot clone.",
         "domain": "economics", "score": "18x to 3.4x revenue",
         "evidences": ["source-code-becomes-assembly", "software-margin-collapse", "price-implosion"],
         "supersedes": [B + "developments/2026-08-03-ten-days-beats-ten-minutes"]},
        {"id": "2026-08-04-the-next-generation-needs-more-than-your-laptop",
         "title": "A coding lead says today's harness will look primitive within months",
         "claim": "OpenAI's Codex lead called the tool a good harness that will seem primitive in "
                  "two to three months, since the next generation of models needs more than your "
                  "laptop.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["harness-as-generalizer", "autonomy-clock-speed", "duration-beats-quality"],
         "supersedes": [B + "developments/2026-08-04-source-code-on-the-verge-of-becoming-assembly"]},
        {"id": "2026-08-04-arxiv-math-spikes-while-budgets-flatline",
         "title": "Mathematics uploads spike while budgets flatline, and 312 problems are resolved",
         "claim": "Mathematics uploads to arXiv are spiking while budgets flatlined, the clearest "
                  "signal of AI influence, with one tracker showing 427 problems tracked and 312 "
                  "resolved, 205 in July alone, up 193% over June and a third checked in Lean.",
         "domain": "science", "actor": ["arxiv"], "score": "312 of 427 / +193%",
         "evidences": ["automated-science", "proof-priced-per-unit", "the-genome-project-for-proof"],
         "supersedes": [B + "developments/2026-08-03-a-world-for-ten-dollars-of-tokens"]},
        {"id": "2026-08-04-a-hundred-fold-activity-gain-in-five-cycles",
         "title": "A hybrid model plus robotic experiments yields hundred-fold enzyme gains",
         "claim": "Tianjin's REAP pairs a hybrid-loss model with robotic experiments for a "
                  "57-fold activity gain in cytochrome P450 BM3 in five cycles and 104-fold in "
                  "Sortase A.",
         "domain": "biotech", "score": "57x and 104x",
         "evidences": ["biology-as-compile-target", "automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-08-03-a-familiar-drug-may-starve-migrating-cancer-cells"]},
        {"id": "2026-08-04-feedback-that-never-leaves-the-skull",
         "title": "A headstage runs models on-device so feedback never leaves the skull",
         "claim": "Science Corp's SciFi headstage, from $2,048, moves 2.5 gigabits per second "
                  "across thousands of channels with on-device models, so feedback never leaves "
                  "the skull.",
         "domain": "biotech", "actor": ["science-corp"], "score": "2.5 Gbps / $2,048",
         "evidences": ["intimate-interface", "architecture-of-mind", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-08-04-a-hundred-fold-activity-gain-in-five-cycles"]},
        {"id": "2026-08-04-a-hundred-fifty-billion-of-chips-routed-to-one-lab",
         "title": "A financing program routes $150 billion of chips to a single lab",
         "claim": "Google built one of history's largest financing programs to route $150 billion "
                  "of chips to Anthropic, which separately signed a $10 billion deal for 133 "
                  "megawatts of hydropowered capacity in Norway, while Caterpillar posted record "
                  "$20.5 billion sales with datacenter power generation up 29%.",
         "domain": "economics", "actor": ["google", "anthropic", "volta", "caterpillar"],
         "score": "$150B / $10B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-08-03-fifteen-years-for-a-power-connection"]},
        {"id": "2026-08-04-recursive-self-improvement-justifies-the-capex",
         "title": "A strategy chief says recursive self-improvement is what justifies the spending",
         "claim": "DeepMind's chief strategy officer said what justifies this capital spending is "
                  "recursive self-improvement, AI building better AI, as SpaceX partnered with "
                  "Nvidia to fly datacenter-class compute on satellites and prepaid a Texas county "
                  "$10 million on a fab deal that could reach $119 billion.",
         "description": "An insider gives the newsletter's own thesis as the financial rationale for the buildout: "
                        "the chips, the satellites and the fab are a bet that AI building better AI will pay for "
                        "them.",
         "domain": "compute", "actor": ["google-deepmind", "spacex", "nvidia"], "score": "$119B",
         "evidences": ["recursive-self-improvement", "orbit-as-compute", "compute-capital-stack"],
         "about": [B + "hardware/vera-rubin", B + "facilities/terafab"],
         "supersedes": [B + "developments/2026-07-19-we-want-k2-to-help-build-k3"],
         "relatedTo": [B + "developments/2026-08-04-a-hundred-fifty-billion-of-chips-routed-to-one-lab",
                       B + "developments/2026-06-12-recursion-could-delay-an-ipo",
                       B + "developments/2026-08-01-almost-all-compute-in-space",
                       B + "developments/2026-08-05-a-buyer-inverts-the-diversification-playbook"],
         "tags": ["rsi", "compute-scaling", "funding"],
         "supporting_text": "what justifies this capex is recursive self-improvement, AI building better AI",
         "sources": [{"id": "the-information-deepmind-capex-rsi",
                      "resource": "https://www.theinformation.com/newsletters/ai-agenda/google-deepmind-exec-says-unprecedented-capex-actually-bet-rsi",
                      "title": "Google DeepMind Exec Says Unprecedented Capex Is Actually a Bet On 'RSI'",
                      "author": "org:the-information"},
                     {"id": "spacex-nvidia-starmind-post",
                      "resource": "https://x.com/SpaceX/status/2084723854534951218",
                      "title": "SpaceX on flying Nvidia Rubin GPUs and Vera CPUs on Starmind AI1 satellites",
                      "author": "org:spacex"},
                     {"id": "terafab-grimes-county-prepayment-post",
                      "resource": "https://x.com/cb_doge/status/2084628645721616722",
                      "title": "SpaceX prepays Grimes County $10 million on the Terafab deal"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Speaking to The Information, DeepMind's chief strategy officer said what justifies the unprecedented "
                 "capital spending is recursive self-improvement, AI building better AI "
                 "([The Information](https://www.theinformation.com/newsletters/ai-agenda/google-deepmind-exec-says-unprecedented-capex-actually-bet-rsi)). "
                 "The newsletter sets the remark beside the hardware it is meant to pay for: SpaceX partnering with "
                 "Nvidia to fly [Vera Rubin](/hardware/vera-rubin.md) GPUs and Vera CPUs on Starmind AI1 satellites as "
                 "datacenter-class space compute, and prepaying Grimes County $10 million on a "
                 "[Terafab](/facilities/terafab.md) deal that could reach $119 billion. It is the first time in the "
                 "corpus that a frontier-lab insider gives the loop as the financial rationale for the buildout, after "
                 "[Altman warned it could delay an IPO](/developments/2026-06-12-recursion-could-delay-an-ipo.md) and "
                 "[Moonshot stated it as a roadmap](/developments/2026-07-19-we-want-k2-to-help-build-k3.md); nine "
                 "days later Sergey Brin is reported "
                 "[steering Google's own resources the same way](/developments/2026-08-13-a-cofounder-steers-toward-recursive-self-improvement.md)."},
        {"id": "2026-08-04-competitiveness-chosen-over-containment",
         "title": "Officials reverse on sanctions against open-source rivals after lobbying",
         "claim": "Officials weighed sanctions and blacklists against open-source Chinese labs "
                  "then reversed after Jensen Huang lobbied against restrictions two frontier "
                  "labs wanted, picking competitiveness over containment, while lab staffers "
                  "reviewed a finished voluntary evaluation framework still undisclosed because "
                  "unclassified does not mean broadcast to everyone.",
         "domain": "policy", "actor": ["white-house", "nvidia", "openai", "anthropic"],
         "evidences": ["pegged-to-the-rival", "clearance-as-bottleneck", "safety-pledges-recede"],
         "supersedes": [B + "developments/2026-08-03-does-a-1986-law-cover-a-model-that-breaks-containment"]},
        {"id": "2026-08-04-the-proctoring-ai-lost-to-the-test-taking-ai",
         "title": "Fifty-eight thousand applicants must resit an exam the proctor could not police",
         "claim": "UNAM, Mexico's largest university, ran its first remote entrance exam and got "
                  "scores so implausible that 58,000 applicants must sit it again, the proctoring "
                  "AI having lost to the test-taking AI.",
         "domain": "society", "actor": ["unam"], "score": "58,000 applicants",
         "evidences": ["the-proctor-loses-to-the-taker", "cheating-breaks-the-ruler", "deskilling"],
         "supersedes": [B + "developments/2026-08-03-parents-losing-the-muscle-of-their-own-judgment"]},
        {"id": "2026-08-04-a-mine-restarted-in-four-months-on-autonomous-software",
         "title": "An idled copper mine restarts in four months on autonomous software",
         "claim": "Mariana Minerals raised $310 million after restarting an idled Utah copper "
                  "mine in four months on autonomous software, since electrified intelligence "
                  "eats metal, as stablecoins reached $300 billion and the IMF warned failures "
                  "can propagate faster than supervisors can respond.",
         "domain": "economics", "actor": ["mariana-minerals", "imf"], "score": "$310M / 4 months",
         "evidences": ["physical-recursion", "ai-as-the-economy", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-08-03-eight-reactors-approved-at-once"]},
    ],
}
