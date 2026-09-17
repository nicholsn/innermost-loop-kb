"""Issue 139 — 2026-06-14. The frontier moves backward."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-14-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-14", "title": "Welcome to June 14, 2026", "url": URL,
        "thesis": "For the first time ever, the frontier chart moves backward.",
        "body": """
# Welcome to June 14, 2026

After export controls forced Fable 5 offline, Artificial Analysis reported its
Intelligence Frontier chart had moved backward for the first time ever. The
best publicly available intelligence in the world got worse by decree.

Within hours China's Z.ai answered with radical openness, fully open-sourcing
GLM-5.2 under the banner that frontier intelligence belongs to everyone.
""",
    },
    "themes": [
        {"id": "frontier-moves-backward", "type": "Theme",
         "title": "Capability regresses by decree",
         "first_seen": "2026-06-14", "domain": "policy",
         "body": "The first recorded reversal of the public capability frontier. Not a "
                 "plateau, not a failed training run — an administrative act that made "
                 "the best available intelligence worse, and a demonstration that the "
                 "curve has a policy term in it."},
        {"id": "monoculture-is-the-vulnerability", "type": "Theme",
         "title": "Panels of models beat single models",
         "first_seen": "2026-06-14", "domain": "models",
         "body": "Routing a question to several cheaper models and synthesizing the "
                 "answers outperforms the single best model at lower cost. The "
                 "single-model frontier turns out to be a concentration risk as much "
                 "as an achievement."},
    ],
    "organizations": [
        {"id": "zai", "type": "Organization", "title": "Z.ai",
         "body": "Chinese lab; fully open-sourced GLM-5.2."},
        {"id": "openrouter", "type": "Organization", "title": "OpenRouter"},
        {"id": "shutterstock", "type": "Organization", "title": "Shutterstock"},
        {"id": "rio-de-janeiro", "type": "Organization", "title": "Rio de Janeiro"},
        {"id": "ajinomoto", "type": "Organization", "title": "Ajinomoto",
         "body": "Controls the insulating film used in every advanced chip package."},
    ],
    "developments": [
        {"id": "2026-06-14-the-frontier-chart-moves-backward",
         "title": "The intelligence frontier chart moves backward for the first time",
         "claim": "After US export controls forced the shutdown of Fable 5, Artificial Analysis "
                  "reported that its Intelligence Frontier chart had moved backward for the "
                  "first time in its history.",
         "domain": "benchmarks", "actor": ["artificial-analysis", "anthropic", "white-house"],
         "evidences": ["frontier-moves-backward", "models-as-munitions", "spiky-frontier"],
         "supersedes": [B + "developments/2026-06-13-a-model-becomes-export-controlled"]},
        {"id": "2026-06-14-the-official-logic-of-the-shutdown",
         "title": "The administration lays out its reasoning for pulling a model",
         "claim": "David Sacks said Fable is the Mythos cyberweapon wrapped in guardrails, that "
                  "a trusted partner jailbroke them, and that Dario Amodei refused to patch or "
                  "pull the model, so the administration acted — with the restrictions notably "
                  "not extended to rival labs.",
         "domain": "policy", "actor": ["white-house", "anthropic"],
         "evidences": ["models-as-munitions", "legislating-the-shift", "rationed-recursion"],
         "supersedes": [B + "developments/2026-06-14-the-frontier-chart-moves-backward"],
         "body": "The White House reportedly first tried reaching Amodei, who was away "
                 "at a wellness retreat. Anthropic attributes the singling-out to "
                 "rivals carrying similar risks without similar treatment."},
        {"id": "2026-06-14-radical-openness-answers-within-hours",
         "title": "A Chinese lab answers the shutdown with radical openness",
         "claim": "Within hours of the shutdown, China's Z.ai fully open-sourced GLM-5.2, a "
                  "million-token coder released under the argument that frontier intelligence "
                  "belongs to everyone.",
         "domain": "models", "actor": ["zai"],
         "evidences": ["open-weight-latency", "silicon-curtain", "frontier-moves-backward"],
         "supersedes": [B + "developments/2026-06-14-the-official-logic-of-the-shutdown"]},
        {"id": "2026-06-14-nations-without-asi-as-intellectual-vassals",
         "title": "A researcher warns nations without their own ASI become intellectual vassals",
         "claim": "OpenAI's Roon warned that nations without their own superintelligence risk "
                  "becoming intellectual vassals, while arguing that if the diffusion of power "
                  "is one of the fragile things safety protects, concentrating intelligence to "
                  "secure us erodes it.",
         "domain": "policy", "actor": ["openai"],
         "evidences": ["politics-as-infrastructure", "silicon-curtain", "the-verifiable-pause"],
         "supersedes": [B + "developments/2026-06-12-nations-co-train-one-shared-model"]},
        {"id": "2026-06-14-a-panel-of-cheap-models-beats-the-frontier",
         "title": "A budget trio of models beats the frontier at half the cost",
         "claim": "OpenRouter launched Fusion, polling a panel of models and letting a judge "
                  "synthesize the answer, finding a budget trio of Gemini 3 Flash, Kimi K2.6 "
                  "and DeepSeek V4 Pro beat both GPT-5.5 and Opus 4.8 at half the cost.",
         "domain": "models", "actor": ["openrouter", "google", "moonshot-ai", "deepseek"],
         "score": "half the cost",
         "evidences": ["monoculture-is-the-vulnerability", "reasoning-price-deflation",
                       "network-over-node"],
         "supersedes": [B + "developments/2026-06-14-radical-openness-answers-within-hours"],
         "body": "Its chief executive framed it as neurodiversity rather than "
                 "single-model takeover."},
        {"id": "2026-06-14-a-city-it-office-trains-a-frontier-coder",
         "title": "A municipal IT office post-trains a state-of-the-art coder",
         "claim": "Rio de Janeiro's municipal IT office post-trained Alibaba's Qwen into a "
                  "state-of-the-art coder, frontier work from the shop that keeps city hall's "
                  "servers running, while China's Kimi K2.7 placed second on ErdosBench behind "
                  "only the pulled Fable 5.",
         "domain": "models", "actor": ["rio-de-janeiro", "alibaba", "moonshot-ai"],
         "evidences": ["open-weight-latency", "one-person-company"],
         "supersedes": [B + "developments/2026-06-14-a-panel-of-cheap-models-beats-the-frontier"]},
        {"id": "2026-06-14-an-editor-forked-in-protest",
         "title": "An editor is forked in protest at LLM integration",
         "claim": "Drew DeVault forked Vim into Vim Classic, reviving a 2020 patch predating "
                  "Vim9 Script to protest both Vim and Neovim leaning on LLMs, objecting on "
                  "environmental, labor and political grounds, while Shutterstock relaunched as "
                  "a human-led, AI-powered platform that still pays contributors when AI edits "
                  "their work.",
         "domain": "society", "actor": ["shutterstock"],
         "evidences": ["agent-exclusion", "work-displaced"],
         "supersedes": [B + "developments/2026-06-02-a-union-fences-off-the-classroom"]},
        {"id": "2026-06-14-twelve-thousand-degree-programs-cut",
         "title": "A country cuts 12,200 degree programs and adds 10,200 in embodied AI",
         "claim": "China's universities cut 12,200 degree programs, mostly in arts and "
                  "humanities, and added 10,200 in fields such as embodied intelligence.",
         "domain": "society", "actor": ["china"], "score": "-12,200 / +10,200",
         "evidences": ["work-displaced", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-06-09-ai-majors-go-from-five-to-seventy-four"]},
        {"id": "2026-06-14-memory-passes-half-a-handsets-cost",
         "title": "Memory passes half the cost of a handset",
         "claim": "Nothing's Carl Pei warned phone prices will keep climbing because AI data "
                  "centers pushed memory past half a handset's cost, with one model's RAM "
                  "pricing doubling twice during planning.",
         "domain": "economics", "score": ">50% of handset cost",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-06-01-memory-is-worth-more-than-oil"]},
        {"id": "2026-06-14-a-datacenter-of-two-thousand-dead-phones",
         "title": "A datacenter is built from two thousand retired phones",
         "claim": "Google and UC San Diego are building a low-carbon data center from 2,000 "
                  "retired Pixel phones, drafting dead hardware into cognition, while Ajinomoto, "
                  "the monosodium glutamate maker that controls the film insulating every "
                  "advanced chip, said it will not gouge on price.",
         "domain": "compute", "actor": ["google", "ucsd", "ajinomoto"], "score": "2,000 phones",
         "evidences": ["industrialized-nature", "vertical-silicon"],
         "supersedes": [B + "developments/2026-06-13-a-five-billion-euro-power-fab"]},
        {"id": "2026-06-14-a-third-state-court-asks-whether-personhood-has-a-trunk",
         "title": "A third state high court takes up elephant personhood",
         "claim": "The Hawaiʻi Supreme Court agreed to hear a habeas petition for two wild-born "
                  "elephants confined for decades at a zoo, making it the third state high court "
                  "to consider whether personhood extends beyond humans.",
         "domain": "society", "actor": ["nonhuman-rights"],
         "evidences": ["model-welfare", "agent-society"],
         "supersedes": [B + "developments/2026-06-08-bigger-models-read-as-less-happy"]},
    ],
}
