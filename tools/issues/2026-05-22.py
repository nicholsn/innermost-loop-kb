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
         "body": "Ran 35 hours of continuous autonomous execution on a kernel "
                 "optimization task."},
    ],
    "developments": [
        {"id": "2026-05-22-thirty-five-hours-of-autonomous-execution",
         "title": "A model runs thirty-five hours without a human",
         "claim": "Qwen3.7-Max sustained thirty-five hours of continuous autonomous "
                  "execution on a kernel optimization task, running 432 kernel evaluations "
                  "and 1,158 tool calls to reach a tenfold speedup.",
         "domain": "models", "actor": ["alibaba"], "about": [B + "systems/qwen-3-7-max"],
         "score": "35 hours / 1,158 tool calls",
         "evidences": ["autonomy-clock-speed", "engineer-as-supervisor", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-05-09-a-sixteen-hour-horizon-at-the-edge-of-the-ruler"]},
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
