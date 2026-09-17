"""Issue 122 — 2026-05-22. Thirty-five hours without a human."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-22-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-22", "title": "Welcome to May 22, 2026", "url": URL,
        "thesis": "Autonomous execution stretches past a day and a half.",
        "body": """
# Welcome to May 22, 2026

Qwen3.7-Max ran thirty-five hours of continuous autonomous execution — 432
kernel evaluations, 1,158 tool calls — to deliver a tenfold speedup. An LLM
matched superforecaster performance on ForecastBench. The horizon over which a
model can be left alone keeps stretching.
""",
    },
    "organizations": [
        {"id": "engineai", "type": "Organization", "title": "EngineAI",
         "body": "Chinese humanoid maker scaling to a 10,000-unit line."},
        {"id": "clickup", "type": "Organization", "title": "ClickUp",
         "resource": "https://clickup.com/"},
    ],
    "systems": [
        {"id": "qwen-3-7-max", "type": "AISystem", "title": "Qwen3.7-Max",
         "developed_by": [B + "organizations/alibaba"], "modality": "text",
         "tags": ["coding-agent"],
         "description": "Alibaba's flagship Qwen model, reported running thirty-five hours of "
                        "continuous autonomous kernel optimization without a human in the loop.",
         "resource": "https://qwen.ai/blog?id=qwen3.7",
         "body": "Qwen3.7-Max is the flagship of Alibaba's Qwen family. Its corpus appearance is the "
                 "[thirty-five-hour autonomous run](/developments/2026-05-22-thirty-five-hours-of-autonomous-execution.md): "
                 "432 kernel evaluations across 1,158 tool calls, ending in a 10x geometric-mean speedup over "
                 "the Triton reference, two weeks after METR's suite had topped out at a "
                 "[sixteen-hour horizon](/developments/2026-05-09-a-sixteen-hour-horizon-at-the-edge-of-the-ruler.md). "
                 "The Qwen line also appears in the corpus as "
                 "[Qwen3-Max-Thinking](/systems/qwen3-max-thinking.md)."},
    ],
    "developments": [
        {"id": "2026-05-22-thirty-five-hours-of-autonomous-execution",
         "title": "A model runs thirty-five hours without a human",
         "claim": "Qwen3.7-Max sustained thirty-five hours of continuous autonomous "
                  "execution on a kernel optimization task, running 432 kernel evaluations "
                  "and 1,158 tool calls to reach a tenfold speedup.",
         "description": "The autonomy horizon outruns the instruments built to measure it: a "
                        "production model works unattended for a day and a half on the accelerator "
                        "kernels that models run on, two weeks after METR's suite topped out "
                        "at sixteen hours.",
         "domain": "models", "actor": ["alibaba"], "about": [B + "systems/qwen-3-7-max"],
         "score": "35 hours / 1,158 tool calls",
         "occurred_on": "2026-05-21",
         "evidences": ["autonomy-clock-speed", "engineer-as-supervisor", "recursive-self-improvement",
                       "silicon-designs-itself"],
         "supersedes": [B + "developments/2026-05-09-a-sixteen-hour-horizon-at-the-edge-of-the-ruler"],
         "relatedTo": [B + "developments/2026-04-29-a-model-writes-the-kernels-that-run-it",
                       B + "developments/2026-04-07-seventy-two-hours-fifty-experiments",
                       B + "developments/2026-02-06-opus-34x-speedup"],
         "tags": ["rsi", "kernels", "autonomous-research"],
         "supporting_text": "ran 35 hours of continuous autonomous execution, performing 432 kernel evaluations across 1,158 tool calls",
         "sources": [{"id": "alibaba-qwen-x-35-hour-run",
                      "resource": "https://x.com/Alibaba_Qwen/status/2057450236180935056",
                      "title": "Alibaba Qwen on X: Self-Evolving in the Wild — ~35 hours of continuous autonomous execution",
                      "author": "org:alibaba"},
                     {"id": "qwen-3-7-blog", "resource": "https://qwen.ai/blog?id=qwen3.7",
                      "title": "Qwen3.7: The Agent Frontier", "author": "org:alibaba"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Alibaba's Qwen team reported that Qwen3.7-Max worked a kernel-optimization task for "
                 "35 hours with no human intervention, running 432 kernel evaluations across 1,158 tool "
                 "calls and finishing with a 10x geometric-mean speedup over the Triton reference "
                 "([X post](https://x.com/Alibaba_Qwen/status/2057450236180935056)). The newsletter files "
                 "it under the line that recursive self-improvement is no longer theoretical: the model is "
                 "optimizing the accelerator kernels that models run on, here an Extend Attention kernel "
                 "for Alibaba's own T-Head PPU, hardware the model had not encountered in training, "
                 "the same loop as "
                 "[GPT-5.5 topping KernelBench](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) "
                 "three weeks earlier and [Opus 4.6's 34x training speedup](/developments/2026-02-06-opus-34x-speedup.md) "
                 "in February. On the autonomy axis it lands two weeks after "
                 "[METR's suite topped out at sixteen hours](/developments/2026-05-09-a-sixteen-hour-horizon-at-the-edge-of-the-ruler.md) "
                 "and six weeks after [UNC's seventy-two-hour unattended run](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md); "
                 "the next code-speedup result in the corpus is the "
                 "[52x speedup where a skilled human reaches 4x](/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four.md) "
                 "in June, and the kernel thread itself resumes with "
                 "[a 232-fold kernel speedup found by an auto-research loop](/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup.md) "
                 "in August."},
        {"id": "2026-05-22-a-model-matches-superforecasters",
         "title": "A model matches superforecaster performance",
         "claim": "An LLM matched superforecaster performance on ForecastBench, closing a "
                  "gap that had been treated as a durable human advantage.",
         "domain": "benchmarks",
         "evidences": ["benchmark-saturation", "humans-need-not-apply"],
         "supersedes": [B + "developments/2026-05-17-a-simulator-beats-the-crowd"]},
        {"id": "2026-05-22-ai-kills-the-cheap-smartphone",
         "title": "AI memory demand kills the cheap smartphone",
         "claim": "Entry-level smartphone shipments fell 13% as AI-driven memory demand "
                  "pushed component costs past what the low end could absorb.",
         "domain": "economics", "score": "-13%",
         "evidences": ["infrastructure-crowding-out", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-05-08-motherboard-sales-collapse"]},
        {"id": "2026-05-22-a-ten-thousand-unit-humanoid-line",
         "title": "A humanoid maker opens a 10,000-unit line",
         "claim": "EngineAI opened a production line rated for 10,000 humanoid units a year, "
                  "moving humanoids from demonstration builds to volume manufacturing.",
         "domain": "robotics", "actor": ["engineai"], "score": "10,000 units/yr",
         "evidences": ["physical-recursion", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-05-12-a-production-ready-mecha"]},
        {"id": "2026-05-22-a-robot-barber-for-under-a-dollar",
         "title": "Robot barbers cut hair for under a dollar",
         "claim": "Robotic barbers began offering haircuts for under a dollar, pricing a "
                  "manual service below what human labor can match.",
         "domain": "robotics", "score": "<$1",
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-05-09-two-robots-make-a-bed-in-two-minutes"]},
        {"id": "2026-05-22-cutting-staff-while-paying-for-orchestrators",
         "title": "A company cuts 22% while opening $1M bands for agent orchestrators",
         "claim": "ClickUp cut 22% of its workforce while introducing compensation bands up to "
                  "$1 million for engineers who orchestrate agents, a single company pricing "
                  "both sides of the substitution at once.",
         "domain": "economics", "actor": ["clickup"], "score": "-22% / $1M bands",
         "evidences": ["work-displaced", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-05-20-replacing-lower-value-human-capital"]},
    ],
}
