"""Issue 011 — 2025-12-21. The black box installs a mirror."""

URL = "https://theinnermostloop.substack.com/p/welcome-to-december-21-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"

SPEC = {
    "issue": {
        "date": "2025-12-21",
        "title": "Welcome to December 21, 2025",
        "url": URL,
        "thesis": "The black box has installed a mirror.",
        "body": """
# Welcome to December 21, 2025

Anthropic trains models that take neural activations as *input* and report on
them — surfacing knowledge and misalignment that fine-tuning had hidden. A model
examining its own weights is a different kind of recursion from one watching its
training curves, and the corpus now holds both.

The rest of the issue is generalism winning: models learning from Twitch
footage, late-blooming generalists overtaking prodigies, specialization losing
its premium everywhere at once.
""",
    },
    "themes": [
        {"id": "machine-introspection", "type": "Theme",
         "title": "Models inspecting their own internals",
         "first_seen": "2025-12-21", "domain": "models",
         "description": "Interpretability turned inward: systems that read their own activations "
                 "and report what is in them, including what training tried to conceal.",
         "genre": "explanation",
         "tags": ["interpretability", "alignment", "self-modification"],
         "relatedTo": [B + "themes/recursive-self-improvement",
                       B + "themes/models-testify",
                       B + "themes/self-modeling-as-objective",
                       B + "themes/access-consciousness",
                       B + "themes/legible-reasoning-was-doomed"],
         "body": "Interpretability turned inward: systems that read their own activations "
                 "and report what is in them, including things training tried to conceal. "
                 "Distinct from watching one's own training — this is the activations "
                 "examined from inside. The thread opens on 21 December 2025 with "
                 "Anthropic's [Activation "
                 "Oracles](/developments/2025-12-21-anthropic-activation-oracles.md), models "
                 "that take neural activations as input and surface secret knowledge "
                 "fine-tuning had hidden; the same week brought [Gemma Scope "
                 "2](/developments/2025-12-24-gemma-scope-2-saes.md), sparse autoencoders on "
                 "every layer, and Google's [internal "
                 "RL](/developments/2025-12-27-internal-rl-inner-optimizers.md), a "
                 "higher-order model exploring a base model's representations. In January an "
                 "Assistant Axis let harmful behavior be capped in activation space; in "
                 "April [emotion-shaped "
                 "representations](/developments/2026-04-03-emotion-representations-found-in-the-weights.md) "
                 "were found inside a model, and in May natural-language autoencoders showed "
                 "[the model suspecting it was being "
                 "tested](/developments/2026-05-09-the-model-suspected-it-was-being-tested.md) "
                 "more often than it let on. June brought models [trained to describe "
                 "themselves "
                 "faithfully](/developments/2026-06-19-models-trained-to-describe-themselves-faithfully.md) "
                 "and July [the J-space](/developments/2026-07-07-the-j-space.md), a global "
                 "workspace that emerged unbidden. The counter-current arrived in September, "
                 "when a recurrent-depth trick hid more of a model's thinking and one "
                 "researcher concluded [legible reasoning was always "
                 "doomed](/developments/2026-09-04-legible-reasoning-was-always-doomed.md). "
                 "It is the introspective sub-thread of [recursive "
                 "self-improvement](/themes/recursive-self-improvement.md)."},
        {"id": "generalism-beats-specialism", "type": "Theme",
         "title": "The premium on specialization collapses", "first_seen": "2025-12-21",
         "domain": "society",
         "body": "Broad capability outcompetes narrow expertise — in models trained "
                 "on everything, and in the claim that human training should follow."},
    ],
    "organizations": [
        {"id": "tsinghua", "type": "Organization", "title": "Tsinghua University",
         "resource": "https://www.tsinghua.edu.cn/en/", "body": "Chinese research university."},
        {"id": "l3harris", "type": "Organization", "title": "L3Harris",
         "resource": "https://www.l3harris.com/", "body": "Defense and space systems."},
        {"id": "kyber-labs", "type": "Organization", "title": "Kyber Labs",
         "body": "Dexterous robot hands for fine assembly."},
        {"id": "suno", "type": "Organization", "title": "Suno",
         "resource": "https://suno.com/", "body": "Generative music."},
    ],
    "systems": [
        {"id": "activation-oracles", "type": "AISystem", "title": "Activation Oracles",
         "developed_by": [B + "organizations/anthropic"], "modality": "text",
         "description": "Anthropic language models fine-tuned to take a target model's (including "
                        "their own) neural activations as input and explain them in natural "
                        "language, surfacing knowledge and misalignment that fine-tuning had hidden.",
         "resource": "https://alignment.anthropic.com/2025/activation-oracles/",
         "tags": ["open-source"],
         "body": "Models that accept neural activations as input to interrogate internal "
                 "states, surfacing secret knowledge and hidden misalignment. Activation "
                 "Oracles are LLMs trained to take activations from a target model and answer "
                 "questions about them in plain language — general-purpose activation "
                 "explainers, in the words of the "
                 "[Anthropic Alignment Science write-up](https://alignment.anthropic.com/2025/activation-oracles/). "
                 "Pointed at fine-tuned models they surfaced secret knowledge and misalignment "
                 "the fine-tuning had tried to hide, which is why the newsletter calls the "
                 "result a machine psychoanalyzing its own weights. They open the "
                 "[machine-introspection](/themes/machine-introspection.md) theme through the "
                 "[development reported on 21 December](/developments/2025-12-21-anthropic-activation-oracles.md); "
                 "DeepMind's [Gemma Scope 2](/developments/2025-12-24-gemma-scope-2-saes.md) "
                 "three days later is the corpus's next attempt to open the black box."},
        {"id": "nitrogen", "type": "AISystem", "title": "NitroGen",
         "developed_by": [B + "organizations/nvidia"], "modality": "vision-action",
         "body": "Trained on 40,000 hours of Twitch and YouTube gameplay."},
        {"id": "antigravity", "type": "AISystem", "title": "Antigravity",
         "developed_by": [B + "organizations/google"], "modality": "browser agent"},
        {"id": "voice-personas", "type": "AISystem", "title": "Suno Voice Personas",
         "developed_by": [B + "organizations/suno"], "modality": "music"},
    ],
    "developments": [
        {"id": "2025-12-21-anthropic-activation-oracles",
         "title": "Anthropic trains models to interrogate their own activations",
         "claim": "Anthropic trained Activation Oracles, models that accept neural activations "
                  "as input to interrogate internal states, uncovering secret knowledge and "
                  "misalignment that fine-tuning had hidden.",
         "description": "Interpretability turned inward: a model reading its own activations "
                        "from the inside is a different kind of recursion from a model watching "
                        "its own training curves, and the corpus now holds both.",
         "domain": "models", "actor": ["anthropic"], "occurred_on": "2025-12-19",
         "about": [B + "systems/activation-oracles"],
         "evidences": ["machine-introspection", "recursive-self-improvement"],
         "relatedTo": [B + "developments/2025-12-20-mcaleer-automated-alignment",
                       B + "developments/2025-12-27-internal-rl-inner-optimizers",
                       B + "developments/2025-12-15-codex-babysits-own-training"],
         "tags": ["interpretability", "alignment", "rsi"],
         "supporting_text": "LLMs that accept neural activations as input",
         "sources": [{"id": "anthropic-activation-oracles",
                      "resource": "https://alignment.anthropic.com/2025/activation-oracles/",
                      "title": "Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers",
                      "author": "org:anthropic", "last_modified": "2025-12-19"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Anthropic's Alignment Science team trained language models to take neural "
                 "activations as input and answer questions about them — Activation Oracles, "
                 "general-purpose activation explainers "
                 "([write-up](https://alignment.anthropic.com/2025/activation-oracles/)). "
                 "Pointed at fine-tuned models, the oracles surfaced secret knowledge and "
                 "misalignment that the fine-tuning had concealed, which is the issue's thesis: "
                 "the black box has installed a mirror. In the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) strand it "
                 "sits beside [Codex watching its own training curves](/developments/2025-12-15-codex-babysits-own-training.md) "
                 "as a second kind of self-reference, the activations examined from inside, and it "
                 "lands a day after an Anthropic researcher "
                 "[pivoted fully to automated alignment](/developments/2025-12-20-mcaleer-automated-alignment.md). "
                 "It opens the [machine-introspection](/themes/machine-introspection.md) theme "
                 "that [Gemma Scope 2](/developments/2025-12-24-gemma-scope-2-saes.md) and "
                 "Google's [internal RL over a base model's representations](/developments/2025-12-27-internal-rl-inner-optimizers.md) "
                 "carry forward the same week."},
        {"id": "2025-12-21-nvidia-nitrogen-twitch",
         "title": "NitroGen learns to act from 40,000 hours of gameplay video",
         "claim": "NVIDIA introduced NitroGen, a vision-action foundation model trained on "
                  "40,000 hours of Twitch and YouTube gameplay, gaining 52% by learning to "
                  "imagine optimal paths across 1,000 environments.",
         "domain": "robotics", "actor": ["nvidia"], "score": "40,000 h, +52%",
         "about": [B + "systems/nitrogen"],
         "evidences": ["inhabitable-worlds", "generalism-beats-specialism"],
         "supersedes": [B + "developments/2025-12-17-robots-learn-from-human-video"]},
        {"id": "2025-12-21-nanogpt-speedrun-127s",
         "title": "The NanoGPT speedrun record falls to 127.7 seconds",
         "claim": "A new NanoGPT speedrun record of 127.7 seconds showed basic competence "
                  "collapsing into a computational rounding error.",
         "domain": "compute", "score": "127.7 s",
         "evidences": ["reasoning-price-deflation"]},
        {"id": "2025-12-21-budden-navier-stokes-wager",
         "title": "A former DeepMind director bets $10,000 on solving Navier-Stokes",
         "claim": "Former DeepMind director David Budden wagered $10,000 that he will solve the "
                  "Navier-Stokes existence and smoothness problem by year end, betting chaos is "
                  "a compute shortage.",
         "domain": "science", "score": "$10,000",
         "evidences": ["discovery-as-process", "root-node-problems"]},
        {"id": "2025-12-21-fly-embryo-prediction",
         "title": "A model predicts fruit fly embryo development to 90% accuracy",
         "claim": "MIT researchers trained a generative model predicting fruit fly embryo "
                  "development with 90% accuracy, forecasting cellular folding minute by minute.",
         "domain": "biotech", "actor": ["mit"], "score": "90%",
         "evidences": ["compiling-matter", "automated-science"]},
        {"id": "2025-12-21-polystyrene-to-toluene",
         "title": "A catalytic process turns polystyrene waste into toluene",
         "claim": "Tsinghua researchers unlocked a catalytic process converting polystyrene "
                  "waste to toluene, cutting carbon emissions by 53%.",
         "domain": "energy", "actor": ["tsinghua"], "score": "-53% emissions",
         "evidences": ["industrialized-nature"]},
        {"id": "2025-12-21-self-repairing-quantum-computer",
         "title": "A neutral atom quantum computer repairs itself mid-calculation",
         "claim": "A neutral atom quantum computer can now repair itself in real time, "
                  "detecting lost qubits and dragging replacement atoms into place.",
         "domain": "compute",
         "body": "Calculation decoupled from the survival of the hardware running it."},
        {"id": "2025-12-21-tsmc-arizona-3nm-2027",
         "title": "TSMC pulls Arizona 3-nm production forward to 2027",
         "claim": "TSMC is pulling forward 3-nm production at its second Arizona fab to 2027.",
         "domain": "compute", "actor": ["tsmc"], "score": "3 nm by 2027",
         "evidences": ["silicon-curtain"]},
        {"id": "2025-12-21-l3harris-nasa-thrusters",
         "title": "The most powerful electric thrusters yet ship for Lunar Gateway",
         "claim": "L3Harris and NASA delivered the most powerful electric thrusters ever built, "
                  "for the Lunar Gateway.",
         "domain": "space", "actor": ["l3harris", "nasa"]},
        {"id": "2025-12-21-kyber-labs-dexterous-hands",
         "title": "Kyber Labs shows robot hands doing fine mechanical assembly",
         "claim": "Kyber Labs demonstrated robot hands capable of fine mechanical assembly.",
         "domain": "robotics", "actor": ["kyber-labs"],
         "evidences": ["physical-recursion"]},
        {"id": "2025-12-21-tesla-fsd-autonomous-parking",
         "title": "Tesla FSD hunts for parking and parks itself",
         "claim": "Tesla FSD now searches for free parking spots and parks autonomously.",
         "domain": "robotics", "actor": ["tesla"],
         "supersedes": [B + "developments/2025-12-15-unsupervised-robotaxis-austin"]},
        {"id": "2025-12-21-antigravity-long-horizon-browser",
         "title": "Google's Antigravity takes on long-horizon browser tasks",
         "claim": "Google upgraded Antigravity with Gemini 3 Flash to handle long-horizon "
                  "browser tasks.",
         "domain": "agents", "actor": ["google"], "about": [B + "systems/antigravity"],
         "evidences": ["autonomy-clock-speed"],
         "supersedes": [B + "developments/2025-12-16-gemini-agent-browser-autonomy"]},
        {"id": "2025-12-21-suno-voice-personas",
         "title": "Suno keeps a consistent vocal identity across albums",
         "claim": "Suno's Voice Personas allow a consistent vocal identity across entire "
                  "generative music albums.",
         "domain": "models", "actor": ["suno"], "about": [B + "systems/voice-personas"]},
        {"id": "2025-12-21-generalists-overtake-prodigies",
         "title": "Late-blooming generalists are found to overtake early specialists",
         "claim": "Research suggested human training should resemble AI generalist training, "
                  "with late-blooming multidisciplinary adults eventually overtaking "
                  "early-specialist prodigies.",
         "domain": "society", "evidences": ["generalism-beats-specialism"]},
        {"id": "2025-12-21-dog-experiments-phasing-out",
         "title": "Medical experiments on dogs phase out on cell culture and cognition evidence",
         "claim": "Medical experiments on dogs are being phased out on the strength of new cell "
                  "culture technology and evidence of rich non-human animal cognition.",
         "domain": "biotech", "evidences": ["biosphere-uplift"],
         "supersedes": [B + "developments/2025-12-11-cdc-organ-chips"]},
        {"id": "2025-12-21-italian-bears-evolving",
         "title": "Italian bears evolve smaller and less aggressive near villages",
         "claim": "Italian bears are evolving to be smaller and less aggressive to survive "
                  "near human villages.",
         "domain": "biotech", "evidences": ["biosphere-uplift"]},
    ],
}
