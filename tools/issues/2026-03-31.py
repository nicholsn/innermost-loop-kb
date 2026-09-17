"""Issue 087 — 2026-03-31. Institutions as workarounds for insufficient intelligence."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-31-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-31", "title": "Welcome to March 31, 2026", "url": URL,
        "thesis": "Research agents get an outer loop that writes their own search strategies.",
        "body": """
# Welcome to March 31, 2026

Bilevel Autoresearch wraps an inner research loop inside an outer one that
generates new search strategies as Python code at runtime — both loops powered
by the same model, with no stronger model required. The recursion no longer
needs a smarter supervisor.

The line of the issue is an aside: the economy is discovering that most of its
institutions were workarounds for insufficient intelligence.
""",
    },
    "organizations": [
        {"id": "skild-ai", "type": "Organization", "title": "Skild AI",
         "body": "Robotic brain demonstrated assembling GPU racks."},
        {"id": "whoop", "type": "Organization", "title": "Whoop",
         "resource": "https://www.whoop.com/"},
        {"id": "aes", "type": "Organization", "title": "AES",
         "resource": "https://www.aes.com/"},
        {"id": "innovation-council", "type": "Organization", "title": "Innovation Council Action",
         "body": "Pro-AI political operation entering the midterms."},
        {"id": "university-of-michigan", "type": "Organization", "title": "University of Michigan",
         "resource": "https://umich.edu/"},
    ],
    "systems": [
        {"id": "bilevel-autoresearch", "type": "AISystem", "title": "Bilevel Autoresearch",
         "description": "A two-level autoresearch framework in which an outer loop reads the "
                        "inner hyperparameter-search loop's code and traces and injects new "
                        "Python search mechanisms at runtime, both loops running on the same "
                        "model.",
         "modality": "research agent",
         "resource": "https://arxiv.org/abs/2603.23420",
         "tags": ["research-agent"],
         "body": "Bilevel Autoresearch, by independent researchers Yaonan Qu and Meng Lu "
                 "([arXiv](https://arxiv.org/abs/2603.23420)), treats Karpathy's autoresearch "
                 "loop as itself a research target: the inner loop proposes and tests changes to "
                 "a GPT pretraining run, while the outer loop diagnoses the inner loop's search "
                 "behavior and writes new mechanisms drawn from bandits, combinatorial "
                 "optimization and design of experiments. On Karpathy's GPT pretraining "
                 "benchmark the outer loop reports a 5x improvement over the inner loop alone "
                 "(-0.045 vs -0.009 val_bpb) with no stronger meta-level model. It enters the "
                 "corpus in [the March 31 development](/developments/2026-03-31-bilevel-autoresearch.md) "
                 "as the point where the recursion stops needing a smarter supervisor, and is the "
                 "immediate predecessor of Apple's "
                 "[self-distillation result](/developments/2026-04-05-self-distillation-without-a-teacher.md)."},
        {"id": "aira2", "type": "AISystem", "title": "AIRA2",
         "description": "Meta's second-generation AI research agent, which attacks three "
                        "structural bottlenecks in research agents with an asynchronous "
                        "multi-GPU worker pool, a hidden consistent evaluation protocol and "
                        "interactively debugging ReAct agents.",
         "developed_by": [B + "organizations/meta"],
         "modality": "research agent",
         "resource": "https://arxiv.org/abs/2603.26499",
         "tags": ["research-agent"],
         "body": "AIRA2 ([arXiv](https://arxiv.org/abs/2603.26499)) is Meta's follow-on "
                 "research agent, built around fixes for three bottlenecks the field had "
                 "identified: synchronous single-GPU execution, a generalization gap in which "
                 "validation-based selection overfits over long search horizons, and the ceiling "
                 "imposed by fixed single-turn operators. It reports an 81.5% mean percentile "
                 "rank on MLE-bench-30 at 24 hours (83.1% at 72) against a 72.7% baseline, "
                 "exceeds human state of the art on 6 of 20 AIRS-Bench tasks, and its ablations "
                 "attribute earlier reports of overfitting to evaluation noise. In this corpus it "
                 "shares [the March 31 development](/developments/2026-03-31-bilevel-autoresearch.md) "
                 "with Bilevel Autoresearch and follows Meta's "
                 "[hyperagents](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md) "
                 "of the previous week."},
    ],
    "developments": [
        {"id": "2026-03-31-bilevel-autoresearch",
         "title": "A research loop writes the strategies for its own outer loop",
         "claim": "Bilevel Autoresearch wraps an inner research loop inside an outer one that "
                  "generates new search strategies as Python code at runtime, with both loops "
                  "powered by the same model and no stronger model required, while Meta's AIRA2 "
                  "cracked three structural bottlenecks in research agents.",
         "description": "The outer loop that a human used to be, reading the inner loop's "
                        "code, finding its bottleneck and writing the fix, is handed to the "
                        "same model, so the recursion no longer needs a smarter supervisor.",
         "domain": "agents", "actor": ["meta"],
         "about": [B + "systems/bilevel-autoresearch", B + "systems/aira2"],
         "evidences": ["recursive-self-improvement", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-03-29-autonomous-zero-day-on-stage",
                        B + "developments/2026-03-24-hyperagents-edit-their-own-mechanism",
                        B + "developments/2026-03-09-autoresearch-650-experiments"],
         "relatedTo": [B + "developments/2026-03-31-harnesses-become-editable-artifacts",
                       B + "developments/2026-02-12-alma-agents-design-their-own-memory",
                       B + "people/andrej-karpathy"],
         "tags": ["rsi", "autonomous-research", "self-modification", "agent-harness"],
         "supporting_text": "generates new search strategies as Python code at runtime",
         "sources": [{"id": "bilevel-autoresearch-arxiv",
                      "resource": "https://arxiv.org/abs/2603.23420",
                      "title": "Bilevel Autoresearch: Meta-Autoresearching Itself",
                      "author": "human:yaonan-qu", "last_modified": "2026-03-24"},
                     {"id": "aira2-arxiv",
                      "resource": "https://arxiv.org/abs/2603.26499",
                      "title": "AIRA2: Overcoming Bottlenecks in AI Research Agents",
                      "author": "org:meta", "last_modified": "2026-03-27"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The recursion stops needing a smarter supervisor. "
                 "[Bilevel Autoresearch](/systems/bilevel-autoresearch.md) (Qu and Lu, "
                 "[arXiv](https://arxiv.org/abs/2603.23420)) nests two loops: the inner one is "
                 "the hyperparameter-search loop Karpathy popularized as autoresearch, and the "
                 "outer one reads the inner loop's code and traces, identifies bottlenecks and "
                 "injects new Python search mechanisms at runtime; on Karpathy's GPT pretraining "
                 "benchmark the outer loop reports a 5x improvement over the inner loop alone "
                 "(-0.045 vs -0.009 val_bpb), instantiating mechanisms from bandits, "
                 "combinatorial optimization and design of experiments that no human specified. "
                 "Both loops use the same model, which is the point: the gain comes from the "
                 "architecture rather than a stronger supervisor. Meta's [AIRA2](/systems/aira2.md) "
                 "([arXiv](https://arxiv.org/abs/2603.26499)) attacks the other side of the "
                 "problem, replacing synchronous single-GPU execution with an asynchronous "
                 "multi-GPU worker pool, adding a hidden consistent evaluation protocol to close "
                 "the generalization gap and using ReAct agents that debug interactively, and "
                 "reaches an 81.5% mean percentile rank on MLE-bench-30 at 24 hours against a "
                 "72.7% baseline. The pair extend Meta's "
                 "[hyperagents](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md) "
                 "of the previous week and Karpathy's "
                 "[650-experiment autoresearch run](/developments/2026-03-09-autoresearch-650-experiments.md), "
                 "and are overtaken within days by Apple's "
                 "[self-distillation result](/developments/2026-04-05-self-distillation-without-a-teacher.md), "
                 "which removes the search loop entirely."},
        {"id": "2026-03-31-harnesses-become-editable-artifacts",
         "title": "Agent control logic becomes a portable natural-language object",
         "claim": "Natural-Language Agent Harnesses externalize agent control logic as portable "
                  "editable natural-language artifacts, making the harness itself a first-class "
                  "programmable object, while WR-Arena began benchmarking world models on "
                  "action fidelity and long-horizon forecasting.",
         "domain": "agents",
         "evidences": ["scaffolding-over-weights", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-03-27-scaffolding-beats-weights-at-a-ninth-the-cost"]},
        {"id": "2026-03-31-reading-papers-improves-the-agent",
         "title": "Giving an agent research papers improves its results",
         "claim": "A controlled experiment confirmed that giving an autoresearch agent access "
                  "to computer science papers during hyperparameter search improved results by "
                  "3.2%.",
         "description": "The author reads it as the payoff of the optimizer-optimizing agents "
                        "in the same paragraph: an autonomous researcher gets measurably better "
                        "simply by being allowed to read the literature, so the agents are "
                        "getting hungrier for input.",
         "domain": "agents", "score": "+3.2%",
         "occurred_on": "2026-03-27",
         "about": [B + "systems/claude-code"],
         "evidences": ["recursive-self-improvement", "automated-science"],
         "supersedes": [B + "developments/2026-03-09-autoresearch-650-experiments"],
         "relatedTo": [B + "people/andrej-karpathy"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-03-31-bilevel-autoresearch",
                        "relation_label": "corroborates"}],
         "tags": ["autonomous-research", "ai-r-and-d", "agent-harness"],
         "supporting_text": "access to CS papers during hyperparameter search improved results by 3.2%",
         "sources": [{"id": "reddit-autoresearch-papers-experiment",
                      "resource": "https://www.reddit.com/r/MachineLearning/comments/1s5jpgz/r_controlled_experiment_giving_an_llm_agent/",
                      "title": "[R] Controlled experiment: giving an LLM agent access to CS papers during automated hyperparameter search improves results by 3.2%",
                      "author": "human:kalpitdixit", "last_modified": "2026-03-27"},
                     {"id": "paper-lantern-autoresearch-writeup",
                      "resource": "https://www.paperlantern.ai/blog/auto-research-case-study",
                      "title": "Paper Lantern improves Autoresearch",
                      "author": "org:paper-lantern", "last_modified": "2026-03-26"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The experiment, posted to r/MachineLearning on 27 March by u/kalpitdixit "
                 "([thread](https://www.reddit.com/r/MachineLearning/comments/1s5jpgz/r_controlled_experiment_giving_an_llm_agent/)), "
                 "compared an autoresearch-style hyperparameter-search agent with and without "
                 "access to computer-science papers and reported a 3.2% improvement for the arm "
                 "that could read; the newsletter's framing is that the agents are getting "
                 "hungrier for input. It is a small number attached to a large question, whether "
                 "autonomous researchers benefit from the literature the way human ones do, and "
                 "it sits between Karpathy's "
                 "[650-experiment autoresearch run](/developments/2026-03-09-autoresearch-650-experiments.md) "
                 "and the same issue's [Bilevel Autoresearch](/developments/2026-03-31-bilevel-autoresearch.md), "
                 "which improves the loop by rewriting its search mechanism rather than feeding "
                 "it papers. The setup was two identical runs of Karpathy's autoresearch "
                 "framework, a [Claude Code](/systems/claude-code.md) agent optimizing a roughly "
                 "7M-parameter GPT-2 on TinyStories on an M4 Pro for 100 experiments per arm from "
                 "the same seed configuration, with the only variable an MCP server (Paper "
                 "Lantern) doing full-text search over more than two million CS papers; at the "
                 "two-hour mark the arm without papers stood at a val_bpb of 0.4624 and the arm "
                 "with papers at 0.4475, a 3.2% gap still widening, after considering 520 papers, "
                 "citing 100 and trying 25 paper-sourced techniques including AdaGC, the sqrt "
                 "batch-scaling rule, the REX schedule and WSD cooldown "
                 "([full writeup](https://www.paperlantern.ai/blog/auto-research-case-study)). "
                 "The author's own limitation is a single run per condition on a tiny model, so "
                 "the figure is suggestive rather than settled."},
        {"id": "2026-03-31-qwen-retreats-from-open-source",
         "title": "Alibaba's newest omni-modal model ships closed",
         "claim": "Alibaba's Qwen3.5-Omni processes text, more than ten hours of audio, images "
                  "and video but only through a proprietary API, marking a quiet Chinese "
                  "retreat from open source.",
         "domain": "models", "actor": ["alibaba"],
         "evidences": ["open-weight-latency", "silicon-curtain"],
         "supersedes": [B + "developments/2026-03-03-qwen-4b-matches-80b"]},
        {"id": "2026-03-31-lilly-insilico-275b",
         "title": "A pharma giant pays $2.75B for AI-developed drugs",
         "claim": "Eli Lilly struck a $2.75 billion deal with Insilico to bring AI-developed "
                  "drugs to global markets, while the University of Michigan built a bismuth "
                  "selenide memristor combining long-term retention with analog tuning.",
         "domain": "biotech", "actor": ["eli-lilly", "insilico", "university-of-michigan"],
         "score": "$2.75B",
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-03-29-claude-operon-for-biology"]},
        {"id": "2026-03-31-a-qr-code-smaller-than-a-bacterium",
         "title": "A QR code is made smaller than most bacteria",
         "claim": "Scientists created a microscopic QR code smaller than most bacteria, visible "
                  "only under an electron microscope and certified as a world record.",
         "domain": "science",
         "evidences": ["compiling-matter", "data-beyond-text"]},
        {"id": "2026-03-31-mistral-raises-debt-and-signs-the-army",
         "title": "A European lab raises debt and signs its national army",
         "claim": "Mistral raised $830 million in debut debt financing to build Nvidia-powered "
                  "data centers across Europe, and the French army reportedly signed a "
                  "three-year contract with Mistral to fine-tune models on defense data.",
         "domain": "economics", "actor": ["mistral"], "score": "$830M",
         "evidences": ["debt-funded-buildout", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-28-google-finances-a-campus-for-a-rival"]},
        {"id": "2026-03-31-starcloud-unicorn-for-orbital-datacenters",
         "title": "An orbital datacenter startup reaches unicorn status",
         "claim": "Starcloud raised $170 million at a $1.1 billion valuation to build data "
                  "centers in space, among the fastest startups to reach unicorn status after "
                  "Y Combinator, while China launched the first ultra-large deep-sea floating "
                  "research island in Shanghai.",
         "domain": "space", "actor": ["starcloud", "china"], "score": "$170M at $1.1B",
         "evidences": ["orbit-as-compute", "industrialized-nature"],
         "supersedes": [B + "developments/2026-03-23-blue-origin-asks-for-51600-satellites"]},
        {"id": "2026-03-31-robots-assemble-gpu-racks",
         "title": "A robotic brain assembles GPU racks",
         "claim": "Skild AI demonstrated its robotic brain assembling GPU racks with high "
                  "precision, heralding robotically assembled data centers, while a Maximo "
                  "robot installed 100 MW of solar at a single complex.",
         "domain": "robotics", "actor": ["skild-ai", "aes"], "score": "100 MW",
         "evidences": ["physical-recursion", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-03-29-modular-legs-snap-into-acrobats"],
         "body": "Robots building the racks that will run the models that direct the robots."},
        {"id": "2026-03-31-security-dogs-patrol-atlanta",
         "title": "Robotic security dogs patrol city streets",
         "claim": "Robotic security dogs now patrol Atlanta streets as residents take crime "
                  "prevention into their own hands, while Mark Cuban predicted humanoid robots "
                  "will not be needed beyond the next decade as robots merge into their "
                  "environments.",
         "domain": "robotics",
         "evidences": ["politics-as-infrastructure", "physical-recursion"]},
        {"id": "2026-03-31-ios-app-releases-up-55-percent",
         "title": "App releases jump 55% since agentic coding went mainstream",
         "claim": "US iOS app releases grew 54.8% year over year in January, the highest rate in "
                  "four years, since agentic coding went mainstream, while OpenAI introduced a "
                  "Codex plugin for Claude Code letting users invoke one tool from inside the "
                  "other.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "+54.8%",
         "evidences": ["software-margin-collapse", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-03-28-nobody-hand-writes-code-any-more"]},
        {"id": "2026-03-31-eyewear-banned-from-courts",
         "title": "A court system bans all AI-integrated eyewear",
         "claim": "Philadelphia courts banned all smart and AI-integrated eyewear to prevent "
                  "witness and juror intimidation, while Whoop raised $575 million at a $10.1 "
                  "billion valuation after reaching a billion in annual revenue.",
         "domain": "policy", "actor": ["whoop"], "score": "$10.1B",
         "evidences": ["agent-exclusion", "intimate-interface"],
         "supersedes": [B + "developments/2026-03-13-smart-glasses-in-the-witness-box"]},
        {"id": "2026-03-31-institutions-as-workarounds",
         "title": "A pro-AI operation enters the midterms with $100M",
         "claim": "Innovation Council Action is entering the midterms with over $100 million to "
                  "push AI deregulation with the White House's blessing, while Rivian won a "
                  "years-long battle enabling direct electric vehicle sales in Washington state.",
         "domain": "policy", "actor": ["innovation-council", "rivian-auto", "white-house"],
         "score": "$100M",
         "evidences": ["legislating-the-shift", "regulatory-exit"],
         "supersedes": [B + "developments/2026-03-27-datacenter-moratorium-act"]},
        {"id": "2026-03-31-midjourney-traffic-falls-60-percent",
         "title": "A capability dissolves into foundation models and traffic falls 60%",
         "claim": "Midjourney's monthly traffic has fallen 60% since its 2023 peak as image "
                  "generation dissolves into foundation models as a feature, while Amazon is "
                  "building forty to fifty delivery hubs a year toward covering every US ZIP "
                  "code within four years.",
         "domain": "economics", "actor": ["midjourney", "amazon"], "score": "-60%",
         "evidences": ["software-margin-collapse", "autonomous-commerce"]},
    ],
}
