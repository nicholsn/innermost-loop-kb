"""Issue 103 — 2026-04-29. A model trained only on the past."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-29-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-29", "title": "Welcome to April 29, 2026", "url": URL,
        "thesis": "The Singularity measured by how astonished the past would be.",
        "body": """
# Welcome to April 29, 2026

Alec Radford and colleagues launched Talkie, a 13B model trained only on
pre-1931 text, reportedly most astonished by the 1960s. The corpus opened on
December 14 with TimeCapsuleLLM and Victorian London. Four and a half months
later the same idea returns as a measuring instrument.

And GPT-5.5 topped KernelBench for writing GPU kernels — the model optimizing
the hardware that runs it.
""",
    },
    "organizations": [
        {"id": "true-anomaly", "type": "Organization", "title": "True Anomaly",
         "body": "Raised $650M for space interceptors."},
        {"id": "doudna-lab", "type": "Organization", "title": "Doudna Lab",
         "body": "Used a genomic foundation model to discover a pre-CRISPR targeting system."},
        {"id": "canada-govt", "type": "Organization", "title": "Government of Canada",
         "resource": "https://www.canada.ca/"},
    ],
    "systems": [
        {"id": "talkie", "type": "AISystem", "title": "Talkie",
         "modality": "text",
         "body": "A 13B model trained only on pre-1931 text, used as a measure of how "
                 "astonishing the present is."},
        {"id": "gpt-5-5", "type": "AISystem", "title": "GPT-5.5",
         "description": "OpenAI's frontier model of spring 2026, whose xhigh reasoning setting topped "
                        "KernelBench for GPU-kernel writing and which more than doubled its "
                        "predecessor on fresh olympiad problems.",
         "developed_by": [B + "organizations/openai"],
         "modality": "text",
         "resource": "https://openai.com/index/introducing-gpt-5-5/",
         "evaluated_on": [B + "benchmarks/kernelbench", B + "benchmarks/frontiermath",
                          B + "benchmarks/gdpval", B + "benchmarks/terminal-bench-2"],
         "sameAs": ["http://www.wikidata.org/entity/Q139594271"],
         "tags": ["reasoning-model"],
         "body": "GPT-5.5 is the OpenAI model "
                 "[released on April 26, 2026](/developments/2026-04-26-gpt-55-sweeps-four-domains.md) "
                 "with selectable reasoning effort, of which xhigh is the highest setting, posting "
                 "39.6% on [FrontierMath](/benchmarks/frontiermath.md) Tier 4, 84.9% on "
                 "[GDPval](/benchmarks/gdpval.md) and 82.7% on "
                 "[Terminal-Bench 2.0](/benchmarks/terminal-bench-2.md) at launch. In this corpus it is the model that "
                 "[topped KernelBench at 6.57%](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) "
                 "for writing the GPU kernels it runs on and that "
                 "[more than doubled GPT-5.4 on fresh olympiad problems](/developments/2026-04-29-matharena-doubles-in-one-release.md) "
                 "in the same issue; a week after it shipped, "
                 "[Codex overtook Claude Code in downloads](/developments/2026-05-05-codex-overtakes-claude-code.md), "
                 "and in May a meta-evaluation "
                 "[mapped it to an implied IQ of 136](/developments/2026-05-13-a-model-scores-136-on-an-iq-meta-eval.md)."},
    ],
    "benchmarks": [
        {"id": "kernelbench", "type": "Benchmark", "title": "KernelBench",
         "description": "A benchmark from Stanford's Scaling Intelligence Lab that asks models to write "
                        "correct, faster-than-baseline GPU kernels for PyTorch reference workloads.",
         "published_by": [B + "organizations/stanford"],
         "measures_capability": "writing correct, faster-than-baseline GPU kernels from PyTorch reference code",
         "resource": "https://scalingintelligence.stanford.edu/KernelBenchLeaderboard/",
         "tags": ["open-source"],
         "body": "KernelBench ([arXiv 2502.10517](https://arxiv.org/abs/2502.10517)) scores a model on "
                 "replacing PyTorch operators with GPU kernels that are both correct and faster than the "
                 "reference, with a public leaderboard maintained by Stanford's Scaling Intelligence Lab. "
                 "In this corpus it is the leaderboard that [GPT-5.5](/systems/gpt-5-5.md) xhigh "
                 "[topped at 6.57%](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md), "
                 "the item the newsletter reads as a model optimizing the hardware it runs on; a "
                 "megakernel variant, KernelBench-Mega, appears in the "
                 "[seventeen-leaders item](/developments/2026-07-03-seventeen-leaders-in-two-years.md) of July."},
    ],
    "developments": [
        {"id": "2026-04-29-a-model-trained-only-on-the-past",
         "title": "A model trained only on pre-1931 text is used to measure the present",
         "claim": "Alec Radford and colleagues launched Talkie, a 13-billion-parameter model "
                  "trained only on pre-1931 text, which was reportedly especially astonished by "
                  "the events of the 1960s.",
         "domain": "models", "about": [B + "systems/talkie"],
         "evidences": ["resurrection-and-time", "architecture-of-mind"],
         "supersedes": [B + "developments/2025-12-14-timecapsule-llm-victorians"],
         "body": "The corpus opened on a model trained only on Victorian London. This is the "
                 "same idea returned as an instrument for measuring the present."},
        {"id": "2026-04-29-a-model-writes-the-kernels-that-run-it",
         "title": "A model tops the leaderboard for writing the GPU kernels it runs on",
         "claim": "GPT-5.5 topped KernelBench at 6.57% for writing GPU kernels, meaning the "
                  "model is now optimizing the hardware that runs it, while OpenAI's Codex lead "
                  "declared the product has achieved escape velocity and will keep improving "
                  "rapidly.",
         "description": "The newsletter reads a kernel-writing leaderboard and a lead engineer's "
                        "'escape velocity' remark in one breath, as the self-improvement loop baked "
                        "into the dev cycle and now reaching down into the hardware layer.",
         "domain": "models", "actor": ["openai", "people/thibault-sottiaux"], "score": "6.57%",
         "about": [B + "systems/gpt-5-5", B + "benchmarks/kernelbench", B + "systems/codex"],
         "evidences": ["recursive-self-improvement", "silicon-designs-itself", "takeoff-declared"],
         "supersedes": [B + "developments/2026-04-27-openai-designs-phone-silicon",
                        B + "developments/2026-02-06-gpt53-codex-creates-itself",
                        B + "developments/2026-02-03-codex-builds-itself"],
         "relatedTo": [B + "developments/2026-02-06-opus-34x-speedup",
                       B + "developments/2026-03-20-cpu-designed-in-twelve-hours",
                       B + "developments/2026-01-10-clark-ai-doing-ai-research"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-02-03-codex-builds-itself",
                        "relation_label": "extends"},
                       {"predicate": "relatedTo",
                        "target": B + "developments/2026-01-10-clark-ai-doing-ai-research",
                        "relation_label": "corroborates"}],
         "tags": ["rsi", "kernels", "evaluation"],
         "supporting_text": "at 6.57% for writing GPU kernels",
         "sources": [{"id": "brockman-gpt-5-5-kernelbench-x",
                      "resource": "https://x.com/gdb/status/2048777802586149331",
                      "title": "Greg Brockman on X: GPT-5.5 xhigh tops KernelBench",
                      "author": "human:greg-brockman"},
                     {"id": "sottiaux-codex-escape-velocity-x",
                      "resource": "https://x.com/thsottiaux/status/2048958572562710550",
                      "title": "Thibault Sottiaux on X: Codex has achieved escape velocity",
                      "author": "human:thibault-sottiaux"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "[GPT-5.5](/systems/gpt-5-5.md) at its xhigh reasoning setting took the top of "
                 "[KernelBench](/benchmarks/kernelbench.md) at 6.57%, per "
                 "[Greg Brockman](https://x.com/gdb/status/2048777802586149331), while OpenAI's Codex "
                 "engineering lead [Thibault Sottiaux](/people/thibault-sottiaux.md) wrote that "
                 "[Codex](/systems/codex.md) had achieved escape velocity and would keep improving rapidly "
                 "([X](https://x.com/thsottiaux/status/2048958572562710550)). The kernel result is the "
                 "first kernel-writing leaderboard in the corpus, making concrete the early sign "
                 "[Jack Clark named in January](/developments/2026-01-10-clark-ai-doing-ai-research.md) and "
                 "following Opus 4.6's [34x training speedup](/developments/2026-02-06-opus-34x-speedup.md) "
                 "and the [twelve-hour CPU](/developments/2026-03-20-cpu-designed-in-twelve-hours.md) in the "
                 "[silicon-designs-itself](/themes/silicon-designs-itself.md) thread. Sottiaux's remark "
                 "updates his own February line that "
                 "[Codex builds itself](/developments/2026-02-03-codex-builds-itself.md). The storyline "
                 "continues with agents [writing AMD kernels](/developments/2026-07-04-agents-write-the-kernels-closing-a-software-gap.md), "
                 "a model [rewriting the kernels behind an 80% price cut](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) "
                 "and, in August, [the loop reaching silicon](/developments/2026-08-27-the-loop-reaches-silicon.md)."},
        {"id": "2026-04-29-matharena-doubles-in-one-release",
         "title": "A fresh olympiad benchmark more than doubles in a single release",
         "claim": "GPT-5.5 scored a record 73.66% on fresh olympiad problems, more than "
                  "doubling its predecessor's 36.61% and repricing what counts as a hard "
                  "problem.",
         "domain": "benchmarks", "actor": ["openai"], "score": "36.61% → 73.66%",
         "evidences": ["benchmark-saturation", "automated-science"],
         "supersedes": [B + "developments/2026-04-27-a-23-year-old-cracks-an-erdos-problem-in-one-prompt"]},
        {"id": "2026-04-29-mathematicians-become-curators",
         "title": "A student says solutions arrive faster than he can process them",
         "claim": "An MIT senior reported that GPT-5.5 has been finding solutions quicker than "
                  "he can process them, with three full Erdős problem solutions already claimed "
                  "and more in the supervision queue, while observers noted the models are also "
                  "sweeping up neglected open problems and giving them proper statements.",
         "domain": "science", "actor": ["mit"], "score": "3 solutions queued",
         "evidences": ["automated-science", "cognitive-load-inverted"],
         "body": "Mathematicians as curators of synthetic genius."},
        {"id": "2026-04-29-every-ticket-gets-its-own-agent",
         "title": "An orchestrator gives every open ticket its own running agent",
         "claim": "OpenAI's Symphony orchestrator turns a project board into a control plane "
                  "where every open ticket gets its own continuously running agent, with humans "
                  "reduced to reviewing the diffs.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["agents-on-the-org-chart", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-04-23-agents-build-memories-from-screen-captures"]},
        {"id": "2026-04-29-a-classified-deal-for-any-lawful-purpose",
         "title": "Google signs a classified deal for any lawful government purpose",
         "claim": "Google signed a classified AI deal with the Pentagon for any lawful "
                  "government purpose, moving the fence around frontier intelligence closer to "
                  "the situation room.",
         "domain": "policy", "actor": ["google", "war-department"],
         "evidences": ["safety-pledges-recede", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-04-17-google-returns-to-the-pentagon"]},
        {"id": "2026-04-29-two-thirds-of-datacenters-head-for-farm-country",
         "title": "Two thirds of planned datacenters head for rural farmland",
         "claim": "Two-thirds of planned data centers are now headed for rural farm country "
                  "chasing cheap land and tax incentives, inverting the 87% urban concentration "
                  "of existing facilities.",
         "domain": "compute", "score": "67% rural vs 87% urban today",
         "evidences": ["infrastructure-crowding-out", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-04-27-we-have-never-retired-old-a100s"]},
        {"id": "2026-04-29-openai-misses-its-targets",
         "title": "OpenAI misses user and revenue targets as its cloud terms loosen",
         "claim": "OpenAI reportedly missed its user and revenue targets with its chief "
                  "financial officer voicing concern about funding future compute contracts, "
                  "while a revised Microsoft agreement lets it ship across any cloud and ends "
                  "the revenue share.",
         "domain": "economics", "actor": ["openai", "microsoft"],
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-27-the-prize-is-the-kitchen-not-the-recipe"]},
        {"id": "2026-04-29-humanoids-to-cross-drones-by-2033",
         "title": "Humanoid production is projected to cross drones around 2033",
         "claim": "Extrapolating from Epoch AI's analysis, humanoid production should cross "
                  "drones around 2033 and wheeled robots around 2034, putting the embodied "
                  "workforce on the same exponential as the disembodied one, while True Anomaly "
                  "raised $650 million for space interceptors.",
         "domain": "robotics", "actor": ["epoch-ai", "true-anomaly"], "score": "2033 / $650M",
         "evidences": ["physical-recursion", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-04-27-five-hundred-humanoids-on-high-voltage-work"]},
        {"id": "2026-04-29-a-targeting-system-older-than-crispr",
         "title": "A model finds a programmable DNA-targeting system that predates CRISPR",
         "claim": "The Doudna Lab used a genomic foundation model to discover a programmable "
                  "RNA-guided DNA-targeting system hidden inside bacteriophages that predates "
                  "CRISPR and operates on entirely different logic.",
         "domain": "biotech", "actor": ["doudna-lab"],
         "evidences": ["automated-science", "hardware-grade-biology", "discovery-as-process"],
         "supersedes": [B + "developments/2026-04-23-organ-networks-grown-in-animal-wombs"]},
        {"id": "2026-04-29-dead-internet-theory-confirmed",
         "title": "A third of websites created since 2022 turn out to be machine-generated",
         "claim": "A third of websites created since 2022 have turned out to be AI-generated, "
                  "confirming what had been called the dead internet theory.",
         "domain": "society", "score": "33% of new sites",
         "evidences": ["work-displaced", "coordination-tax"],
         "supersedes": [B + "developments/2026-04-23-keystrokes-captured-and-surveillance-pricing-banned"]},
        {"id": "2026-04-29-worst-month-of-tech-layoffs-in-two-years",
         "title": "Tech firms cut 45,800 jobs in the worst month in two years",
         "claim": "Technology firms cut 45,800 jobs in March, the worst month in two years, "
                  "with executives openly framing the layoffs as confidence in a post-human "
                  "future, while Meta prepared to unwind an acquisition after China blocked it "
                  "on national security grounds.",
         "domain": "economics", "actor": ["meta", "china"], "score": "45,800 jobs",
         "evidences": ["work-displaced", "silicon-curtain"],
         "supersedes": [B + "developments/2026-04-26-a-quarter-of-boys-prefer-the-chatbot"]},
        {"id": "2026-04-29-canada-opens-a-sovereign-wealth-fund",
         "title": "Canada announces its first sovereign wealth fund",
         "claim": "Canada's prime minister announced the country's first sovereign wealth fund "
                  "to finance energy, minerals, agriculture and infrastructure of national "
                  "interest, while the California billionaire tax headed to the November ballot.",
         "domain": "policy", "actor": ["canada-govt"],
         "evidences": ["science-as-industrial-policy", "regulatory-exit"],
         "supersedes": [B + "developments/2026-04-27-insurers-drop-ai-damages"]},
    ],
}
