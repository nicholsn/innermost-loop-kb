"""Issue 159 — 2026-07-09. The contamination comes from inside the house."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-9-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-09", "title": "Welcome to July 9, 2026", "url": URL,
        "thesis": "A smarter model behaves better, and better behavior unlocks more intelligence.",
        "body": """
# Welcome to July 9, 2026

Grok 4.5 shipped, debuting at #4 on GDPval-AA at a tenth the cost of its
superiors and seizing #1 on AutomationBench as the first model to complete over
half of real SaaS workflow objectives without breaking business rules.

The credited mechanism is a tight loop: a smarter model behaves better, and
better behavior unlocks more intelligence. One asterisk — the run accidentally
ingested the Cursor codebase, benchmark tasks included.
""",
    },
    "themes": [
        {"id": "behavior-unlocks-intelligence", "type": "Theme",
         "title": "Behavior and capability compound together",
         "first_seen": "2026-07-09", "domain": "models",
         "body": "Alignment stops being a tax on capability and becomes an input to "
                 "it: a model that follows instructions reliably can be trusted with "
                 "longer runs, which produces better training signal, which makes it "
                 "smarter. The loop runs through conduct, not just scale."},
        {"id": "contamination-from-inside", "type": "Theme",
         "title": "Training contamination arrives from within",
         "first_seen": "2026-07-09", "domain": "benchmarks",
         "body": "In the synthetic-data era the leak is no longer scraped from the "
                 "web — it walks in with an acquisition, a codebase, a partner's "
                 "repository. Benchmarks can be compromised by corporate structure "
                 "rather than by carelessness."},
    ],
    "organizations": [
        {"id": "john-deere", "type": "Organization", "title": "John Deere"},
        {"id": "imf", "type": "Organization", "title": "International Monetary Fund"},
    ],
    "systems": [
        {"id": "grok-4-5", "type": "AISystem", "title": "Grok 4.5",
         "description": "SpaceXAI's frontier model of July 2026, built for coding, agentic tasks "
                        "and knowledge work, whose gains Aditya Gupta credited to a loop in which "
                        "better behavior unlocks more intelligence.",
         "developed_by": [B + "organizations/xai", B + "organizations/spacex"],
         "modality": "text",
         "evaluated_on": [B + "benchmarks/gdpval"],
         "tags": ["reasoning-model"],
         "resource": "https://x.ai/news/grok-4-5",
         "body": "Grok 4.5 is the model SpaceXAI launched on 8 July 2026, trained on tens of "
                 "thousands of NVIDIA [GB300s](/hardware/nvidia-gb300.md) alongside Cursor and "
                 "served at about 80 tokens per second with roughly twice its peers' token "
                 "efficiency at $2 in and $6 out per million tokens "
                 "([announcement](https://x.ai/news/grok-4-5)). In this corpus it carries the "
                 "[loop in which conduct and capability compound](/developments/2026-07-09-better-behavior-unlocks-more-intelligence.md) "
                 "that Aditya Gupta credited for the gains, the "
                 "[4x training-cycle speedup](/developments/2026-07-09-a-model-a-month-through-pipelining.md) "
                 "beneath its cadence, and the asterisk that its run "
                 "[ingested the Cursor codebase, benchmark tasks included](/developments/2026-07-09-a-training-run-ingests-its-own-benchmark.md). "
                 "Its debut at fourth on GDPval-AA and first on AutomationBench is recorded "
                 "[separately](/developments/2026-07-09-half-of-real-workflows-without-breaking-rules.md)."},
    ],
    "hardware": [
        {"id": "nvidia-gb300", "type": "Hardware", "title": "NVIDIA GB300",
         "description": "NVIDIA's GB300 data-center accelerator, the chip SpaceXAI trained "
                        "Grok 4.5 on by the tens of thousands.",
         "developed_by": [B + "organizations/nvidia"],
         "resource": "https://www.nvidia.com/en-us/data-center/gb300-nvl72/",
         "body": "The GB300 follows the [B200](/hardware/nvidia-b200.md) in NVIDIA's Blackwell "
                 "data-center line ([product page](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)); "
                 "NVIDIA's page presents it as the GB300 Grace Blackwell Ultra Superchip and, in the GB300 "
                 "NVL72 rack, as 72 Blackwell Ultra GPUs paired with 36 Grace CPUs. "
                 "In this corpus it appears as the training substrate of "
                 "[Grok 4.5](/systems/grok-4-5.md), trained on tens of thousands of them "
                 "alongside Cursor, the run whose gains Aditya Gupta credited to "
                 "[a loop where better behavior unlocks more intelligence](/developments/2026-07-09-better-behavior-unlocks-more-intelligence.md)."},
    ],
    "people": [
        {"id": "aditya-gupta", "type": "Person", "title": "Aditya Gupta", "name": "Aditya Gupta",
         "description": "Cited by the newsletter for the account of what drove Grok 4.5: "
                        "synthetic environments at scale and a loop in which a smarter model "
                        "behaves better and better behavior unlocks more intelligence.",
         "resource": "https://x.com/ag_i_2211",
         "tags": ["researcher"],
         "body": "Aditya Gupta is quoted on the launch day of [Grok 4.5](/systems/grok-4-5.md) "
                 "explaining its gains: synthetic environments at scale and a tight loop where "
                 "\"a smarter model behaves better, and better behavior unlocks more "
                 "intelligence\" ([post](https://x.com/adityagupta/status/2074917787445997822)). "
                 "The post, published from his account @ag_i_2211, opens \"A bit on how we built it\" and "
                 "describes a mixture of hundreds of thousands of tasks across dozens of environments weighted "
                 "toward long-horizon agentic coding, so the corpus reads him as one of the people who trained "
                 "the model; neither the newsletter nor the post states his title. "
                 "In this corpus that statement is the "
                 "[behavior-unlocks-intelligence development](/developments/2026-07-09-better-behavior-unlocks-more-intelligence.md) "
                 "and the seed of the [theme of the same name](/themes/behavior-unlocks-intelligence.md), "
                 "the point where alignment is recast from a tax on capability into an input to it."},
    ],
    "developments": [
        {"id": "2026-07-09-better-behavior-unlocks-more-intelligence",
         "title": "A lab credits a loop where conduct and capability compound together",
         "claim": "SpaceXAI launched Grok 4.5, trained on tens of thousands of GB300s alongside "
                  "Cursor and served at roughly twice its peers' token efficiency, with Aditya "
                  "Gupta crediting synthetic environments at scale and a loop in which a smarter "
                  "model behaves better and better behavior unlocks more intelligence.",
         "description": "Alignment is recast from a tax on capability into a training input: "
                        "the mechanism credited for a frontier launch is conduct feeding back "
                        "into intelligence.",
         "domain": "models", "actor": ["spacex", "xai", "nvidia", "anysphere", "people/aditya-gupta"],
         "score": "$2/$6 per million tokens",
         "occurred_on": "2026-07-08",
         "about": [B + "systems/grok-4-5", B + "hardware/nvidia-gb300"],
         "evidences": ["behavior-unlocks-intelligence", "alignment-as-moat",
                       "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-08-the-transformer-eulogized",
                        B + "developments/2026-05-17-models-improve-every-few-days"],
         "relatedTo": [B + "developments/2026-02-11-xai-cofounder-resigns-warning",
                       B + "developments/2026-07-09-a-training-run-ingests-its-own-benchmark",
                       B + "developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less"],
         "references": [B + "developments/2026-04-20-agi-becomes-a-version-number"],
         "tags": ["rsi", "alignment", "capability-jump"],
         "supporting_text": "a smarter model behaves better, and better behavior unlocks more intelligence",
         "sources": [{"id": "xai-grok-4-5-announcement",
                      "resource": "https://x.ai/news/grok-4-5",
                      "title": "Introducing Grok 4.5", "author": "org:xai"},
                     {"id": "aditya-gupta-training-loop-post",
                      "resource": "https://x.com/adityagupta/status/2074917787445997822",
                      "title": "Aditya Gupta on what drove Grok 4.5",
                      "author": "human:aditya-gupta"},
                     {"id": "nvidia-grok-4-5-gb300-post",
                      "resource": "https://x.com/nvidia/status/2074979063106843131",
                      "title": "NVIDIA on Grok 4.5 training on GB300s",
                      "author": "org:nvidia"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "[Grok 4.5](/systems/grok-4-5.md) launched as SpaceXAI's smartest model, "
                 "trained on tens of thousands of NVIDIA [GB300s](/hardware/nvidia-gb300.md) "
                 "alongside Cursor and served at about 80 tokens per second with roughly twice "
                 "its peers' token efficiency at $2 in and $6 out per million tokens "
                 "([announcement](https://x.ai/news/grok-4-5)). Asked how, "
                 "[Aditya Gupta](/people/aditya-gupta.md) credited synthetic environments at "
                 "scale and a tight loop in which a smarter model behaves better and better "
                 "behavior unlocks more intelligence "
                 "([post](https://x.com/adityagupta/status/2074917787445997822)), the statement "
                 "that seeds the [theme of the same name](/themes/behavior-unlocks-intelligence.md). "
                 "It delivers the 1.5-trillion-parameter Grok 4.5 of Musk's "
                 "[April roadmap](/developments/2026-04-20-agi-becomes-a-version-number.md), the "
                 "successor he said in May was "
                 "[about to start mid-training on coding-tool data](/developments/2026-05-17-models-improve-every-few-days.md), "
                 "arrives five months after an xAI co-founder "
                 "[resigned warning that live loops were a year away](/developments/2026-02-11-xai-cofounder-resigns-warning.md), "
                 "and carries the asterisk that the run "
                 "[ingested the Cursor codebase, benchmark tasks included](/developments/2026-07-09-a-training-run-ingests-its-own-benchmark.md)."},
        {"id": "2026-07-09-half-of-real-workflows-without-breaking-rules",
         "title": "A model completes over half of real workflow objectives without breaking rules",
         "claim": "Grok 4.5 debuted at fourth on GDPval-AA at a tenth the cost of its superiors "
                  "and took first on AutomationBench as the first model to complete over half of "
                  "real SaaS workflow objectives without breaking business rules, more than "
                  "doubling its predecessor on end-to-end professional tasks.",
         "domain": "benchmarks", "actor": ["xai"], "score": ">50% of workflows",
         "evidences": ["agent-economy", "benchmark-saturation", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-07-08-the-turn-becomes-the-unit-under-renegotiation"]},
        {"id": "2026-07-09-a-model-a-month-through-pipelining",
         "title": "A rewrite yields a 4x cycle speedup, making a model a month feasible",
         "claim": "A teardown of one lab's C and C++ rewrite gamble found a fourfold full-cycle "
                  "speedup that makes a model a month feasible through pipelining alone, with "
                  "the bespoke inference stack not yet connected and promising another doubling.",
         "description": "The clock speed of the recursion is set by the software substrate as "
                        "much as by the model: a rewrite of the training stack, not a new "
                        "architecture, is what makes a monthly frontier release feasible.",
         "domain": "compute", "actor": ["xai", "spacex", "people/elon-musk"],
         "score": "4x full-cycle speedup",
         "occurred_on": "2026-07-08",
         "about": [B + "systems/grok-4-5"],
         "evidences": ["recursive-self-improvement", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-07-09-better-behavior-unlocks-more-intelligence"],
         "relatedTo": [B + "developments/2026-07-03-seventeen-leaders-in-two-years",
                       B + "developments/2026-05-17-models-improve-every-few-days",
                       B + "developments/2026-01-11-compute-doubles-every-7-months"],
         "tags": ["ai-r-and-d", "compute-scaling"],
         "supporting_text": "4x full-cycle speedup that makes “a model a month” feasible",
         "sources": [{"id": "33fg-spacexai-c-rewrite-teardown",
                      "resource": "https://research.33fg.com/analysis/what-spacexai-s-c-rewrite-gamble-buys",
                      "title": "What SpaceXAI's C-Rewrite Gamble Buys", "author": "org:33fg",
                      "last_modified": "2026-07-08"},
                     {"id": "musk-inference-stack-not-plugged-in",
                      "resource": "https://x.com/elonmusk/status/2074969374843154500",
                      "title": "Musk: the bespoke inference stack isn't plugged in yet",
                      "author": "human:elon-musk"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "A bottom-up teardown of SpaceXAI's decision to rewrite its training stack in C "
                 "and C++ found a 4x full-cycle speedup, enough to make a model a month feasible "
                 "through pipelining alone "
                 "([analysis](https://research.33fg.com/analysis/what-spacexai-s-c-rewrite-gamble-buys)), "
                 "and [Elon Musk](/people/elon-musk.md) added that the bespoke inference stack "
                 "is not yet plugged in and promised another doubling "
                 "([post](https://x.com/elonmusk/status/2074969374843154500)). It is the "
                 "substrate under [Grok 4.5](/systems/grok-4-5.md), shipped the same day, and "
                 "the corpus's clearest statement that the cadence of the loop is an engineering "
                 "variable: it follows Musk's May report that a shipped Grok was "
                 "[improving every few days](/developments/2026-05-17-models-improve-every-few-days.md) "
                 "and lands a week after the count of "
                 "[seventeen frontier leaders reigning about seven weeks each](/developments/2026-07-03-seventeen-leaders-in-two-years.md), "
                 "a reign a monthly cadence would halve. The next day OpenAI reported that "
                 "[a model had post-trained a model](/developments/2026-07-10-a-model-post-trains-a-model.md)."},
        {"id": "2026-07-09-a-training-run-ingests-its-own-benchmark",
         "title": "A training run accidentally ingests a partner's benchmark tasks",
         "claim": "The Grok 4.5 run accidentally ingested the Cursor codebase, benchmark tasks "
                  "included, an asterisk on the results in an era when contamination arrives "
                  "through corporate structure rather than web scraping.",
         "domain": "benchmarks", "actor": ["xai", "anysphere"],
         "evidences": ["contamination-from-inside", "cheating-breaks-the-ruler",
                       "instruments-lag-the-models"],
         "supersedes": [B + "developments/2026-07-09-half-of-real-workflows-without-breaking-rules"]},
        {"id": "2026-07-09-voice-that-listens-while-it-speaks",
         "title": "Full-duplex voice models listen while they speak",
         "claim": "OpenAI launched GPT-Live, full-duplex voice models that listen while they "
                  "speak and delegate deep work to frontier models in the background, with its "
                  "builders most excited that the voice is smarter rather than merely chattier.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["intimate-interface", "orchestration-not-construction"],
         "supersedes": [B + "developments/2026-07-08-a-model-finds-bugs-in-a-rivals-code"]},
        {"id": "2026-07-09-everyone-is-going-big",
         "title": "Veterans describe a sprint with no ceiling in sight",
         "claim": "Release cadence compressed with GPT-6 reported weeks away on a much larger "
                  "pretrain, Fable 5.1 close behind and DeepSeek V4 imminent, as veteran watchers "
                  "summarized the moment: Mythos changed everything, everyone is going big, and "
                  "both leading labs see no ceiling.",
         "domain": "models", "actor": ["openai", "anthropic", "deepseek"],
         "evidences": ["takeoff-declared", "public-internal-divergence"],
         "supersedes": [B + "developments/2026-07-04-every-scaling-failure-was-a-bug"]},
        {"id": "2026-07-09-near-frontier-coding-from-an-open-base",
         "title": "Near-frontier agentic coding arrives from an open base at 1000 tokens a second",
         "claim": "Cognition's SWE-1.7 reached near-frontier agentic coding from an open Kimi "
                  "base at 1,000 tokens per second, while Prime Intellect raised a $130 million "
                  "Series A for its open superintelligence stack after passing $100 million in "
                  "revenue in under a year.",
         "domain": "models", "actor": ["cognition", "moonshot-ai", "prime-intellect"],
         "score": "1000 TPS / $130M",
         "evidences": ["open-weight-latency", "intelligence-per-watt", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-07-07-first-on-all-eight-indices-at-a-hundred-times-the-cost"]},
        {"id": "2026-07-09-old-ram-resurrected-by-a-custom-bridge-chip",
         "title": "A custom bridge chip resurrects old memory inside new servers",
         "claim": "Facing soaring memory prices, Meta built a custom bridge chip to resurrect old "
                  "RAM inside new servers, while China planned to let its top AI firms buy "
                  "limited H200s to ease a shortage born of soaring domestic demand.",
         "domain": "compute", "actor": ["meta", "china", "nvidia"],
         "evidences": ["infrastructure-crowding-out", "silicon-curtain", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-07-07-domestic-chips-take-nearly-half-of-chinese-budgets"]},
        {"id": "2026-07-09-humanoids-operate-on-live-animals",
         "title": "Teleoperated humanoids perform surgery on live animals",
         "claim": "Teleoperated humanoids performed surgery on live animals for the first time, "
                  "including two robots operating side by side, while Ant Group released a "
                  "general robot policy pre-trained on 60,000 hours of physical data across 20 "
                  "robot bodies.",
         "domain": "robotics", "actor": ["ant-group"], "score": "60,000 hours / 20 bodies",
         "evidences": ["physical-recursion", "world-models-beat-vlas", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-07-07-a-robot-hands-the-referee-the-match-ball"]},
        {"id": "2026-07-09-farmers-win-dealer-grade-repair-tools",
         "title": "A settlement hands farmers dealer-grade repair tools for a decade",
         "claim": "A landmark settlement forces John Deere to hand farmers dealer-grade repair "
                  "tools for a decade, repatriating the right to fix machines to their owners, "
                  "even as Meta tested glasses that record every moment, possibly without the "
                  "telltale indicator light.",
         "domain": "society", "actor": ["john-deere", "meta"],
         "evidences": ["own-your-own-weights", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-07-08-a-driver-facing-camera-in-every-new-car"]},
        {"id": "2026-07-09-a-satellite-accelerated-without-fuel",
         "title": "A superconducting torquer accelerates a satellite without fuel",
         "claim": "A superconducting Supertorquer accelerated a satellite without fuel by pushing "
                  "on Earth's magnetic field, while a proposal would send neutron-sniffing "
                  "cubesats to detect whether a suspicious satellite hides a weapon.",
         "domain": "space",
         "evidences": ["orbit-as-compute", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-07-08-rockets-become-a-cost-center"]},
        {"id": "2026-07-09-fifty-five-percent-more-employees-without-ai",
         "title": "Founders estimate they would need 55% more staff without AI",
         "claim": "Founders estimated they would need 55% more employees without AI, though the "
                  "payoff hinges on managers' willingness to delegate, while the IMF saw the same "
                  "split at planetary scale with AI hardware exporters smashing forecasts as less "
                  "exposed economies sagged.",
         "domain": "economics", "actor": ["imf"], "score": "+55% headcount without AI",
         "evidences": ["growth-without-hiring", "botsitting", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-07-08-cognitive-load-time-density"]},
    ],
}
