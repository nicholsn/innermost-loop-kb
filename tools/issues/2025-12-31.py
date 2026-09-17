"""Issue — 2025-12-31. The timeline gets new dates."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-new-years-eve-2025"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2025-12-31", "title": "Welcome to New Year's Eve 2025", "url": URL,
        "thesis": "The forecasts get revised and the decentralized curve is steeper.",
        "body": """
# Welcome to New Year's Eve 2025

The AI Futures model puts a 2x gap between ASI and peak human capability at July
2034. More interesting is the second number: decentralized training compute
growing 20x a year against 5x for frontier runs, converging around mid-2031.

GPT-5.2 Pro takes 29.2% on FrontierMath Tier 4 and a mathematician concludes
2026 will be a hell of a year. Tao concedes the definition of a mathematician
will have to broaden.
""",
    },
    "organizations": [
        {"id": "ftai-aviation", "type": "Organization", "title": "FTAI Aviation",
         "body": "Jet engine shop converting aircraft turbines into datacenter power."},
        {"id": "ymtc", "type": "Organization", "title": "YMTC",
         "body": "Chinese memory maker developing high-bandwidth flash."},
        {"id": "eth-zurich", "type": "Organization", "title": "ETH Zurich",
         "resource": "https://ethz.ch/"},
        {"id": "hyphen", "type": "Organization", "title": "Hyphen",
         "body": "Automated makelines producing a bowl every ten seconds."},
        {"id": "ai21", "type": "Organization", "title": "AI21 Labs",
         "resource": "https://www.ai21.com/"},
    ],
    "developments": [
        {"id": "2025-12-31-asi-gap-july-2034",
         "title": "The forecast puts a 2x superhuman gap at July 2034",
         "claim": "The updated AI Futures Model now forecasts a twofold gap between artificial "
                  "superintelligence and peak human capability by July 2034.",
         "description": "The AI 2027 authors' scenario becomes a dated quantitative model, and the "
                        "newsletter reads its mid-2030s convergence with decentralized and orbital "
                        "compute as a single vector pointing at a Dyson swarm.",
         "domain": "models", "actor": ["ai-futures-project"], "score": "2x gap by July 2034",
         "evidences": ["takeoff-declared", "recursive-self-improvement"],
         "supersedes": [B + "developments/2025-12-15-ai-2027-forecast-accuracy"],
         "relatedTo": [B + "developments/2025-12-31-decentralized-training-20x",
                       B + "developments/2026-04-03-forecasts-move-eighteen-months-in-three",
                       B + "developments/2026-08-17-automated-coders-around-late-2027"],
         "tags": ["forecast", "rsi"],
         "supporting_text": "2x gap between ASI and peak human capability by July 2034",
         "sources": [{"id": "ai-futures-model-site", "resource": "https://www.aifuturesmodel.com/",
                      "title": "AI Futures Model", "author": "org:ai-futures-project"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The AI Futures Model is the [AI Futures Project](/organizations/ai-futures-project.md)'s "
                 "interactive timelines-and-takeoff model, published by the authors of the AI 2027 "
                 "scenario; its updated run places the point at which artificial superintelligence is twice "
                 "peak human capability in July 2034 ([model](https://www.aifuturesmodel.com/)). It lands two "
                 "weeks after [91% of AI 2027's verifiable predictions were found to hold](/developments/2025-12-15-ai-2027-forecast-accuracy.md), "
                 "turning a scenario into a dated forecast, and the same issue pairs it with "
                 "[decentralized training compute growing 20x a year](/developments/2025-12-31-decentralized-training-20x.md) "
                 "to converge on centralized labs around mid-2031. Later entries move the date: a "
                 "[hyperbolic regression puts the singularity on 18 July 2034](/developments/2026-02-11-singularity-dated-july-18-2034.md), "
                 "[forecasters pull their timelines forward eighteen months in three](/developments/2026-04-03-forecasts-move-eighteen-months-in-three.md), "
                 "and [three methods converge on automated coders around late 2027](/developments/2026-08-17-automated-coders-around-late-2027.md)."},
        {"id": "2025-12-31-decentralized-training-20x",
         "title": "Decentralized training compute grows four times faster than frontier runs",
         "claim": "Epoch AI found decentralized training compute growing 20x annually against "
                  "5x for frontier training, on track to catch centralized labs by mid-2031.",
         "domain": "compute", "actor": ["epoch-ai"], "score": "20x vs 5x",
         "evidences": ["network-over-node", "open-weight-latency"]},
        {"id": "2025-12-31-frontiermath-tier-4-29pct",
         "title": "GPT-5.2 Pro takes 29.2% on FrontierMath Tier 4",
         "claim": "GPT-5.2 Pro scored 29.2% on FrontierMath Tier 4, prompting mathematician "
                  "Bartosz Naskrecki to say 2026 will be a hell of a year and to start using AI "
                  "toward the Langlands Program.",
         "domain": "benchmarks", "actor": ["openai"], "about": [B + "benchmarks/frontiermath"],
         "score": "29.2%", "evidences": ["automated-science", "benchmark-saturation"]},
        {"id": "2025-12-31-tao-definition-will-broaden",
         "title": "Tao says the definition of a mathematician will broaden",
         "claim": "Terry Tao conceded the definition of a mathematician will broaden as proofs "
                  "become a joint human-machine output.",
         "domain": "science", "actor": ["people/terry-tao"],
         "evidences": ["automated-science", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2025-12-17-tao-magic-dissipates"]},
        {"id": "2025-12-31-transformers-implement-bayes",
         "title": "Transformers are verified to implement Bayesian inference geometrically",
         "claim": "Researchers verified for the first time that transformers implement Bayesian "
                  "inference geometrically, with the residual stream as belief substrate, "
                  "feed-forward layers performing posterior updates and attention providing "
                  "content-addressable routing.",
         "domain": "models", "evidences": ["architecture-of-mind", "machine-introspection"]},
        {"id": "2025-12-31-stanford-cs-degrees-stop-guaranteeing-work",
         "title": "A Stanford CS degree stops guaranteeing employment",
         "claim": "Stanford computer science graduates are finding their degrees no longer "
                  "guarantee employment as firms replace ten juniors with two seniors and an AI.",
         "domain": "economics", "actor": ["stanford"], "score": "10 juniors → 2 seniors + AI",
         "evidences": ["work-displaced"]},
        {"id": "2025-12-31-claude-builds-a-bird-feeder-camera",
         "title": "A model builds a $30 bird feeder camera with custom firmware",
         "claim": "Claude Code autonomously built a $30 bird feeder camera with custom "
                  "firmware, while Shaquille O'Neal completed seven vibe-coding projects.",
         "domain": "agents", "actor": ["anthropic"], "evidences": ["compiling-matter", "engineer-as-supervisor"]},
        {"id": "2025-12-31-xai-third-site-tennessee",
         "title": "xAI takes a third site to reach a million chips",
         "claim": "xAI acquired a third site in Tennessee toward its million-chip goal, while "
                  "SoftBank fully funded its $40 billion OpenAI investment and Nvidia opened "
                  "talks to acquire AI21 Labs for $3 billion.",
         "domain": "compute", "actor": ["xai", "softbank", "nvidia", "ai21"], "score": "$40B / $3B",
         "evidences": ["compute-capital-stack", "capital-takes-the-plant"]},
        {"id": "2025-12-31-turbines-become-datacenter-power",
         "title": "Aircraft turbines are converted into datacenter power",
         "claim": "FTAI Aviation launched a division converting aircraft turbines into data "
                  "center power sources, as Caterpillar's power segment became its "
                  "fastest-growing business.",
         "domain": "energy", "actor": ["ftai-aviation", "caterpillar"],
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2025-12-28-jet-engines-for-datacenters"]},
        {"id": "2025-12-31-high-bandwidth-flash",
         "title": "China fuses flash storage directly to GPUs",
         "claim": "YMTC is developing high-bandwidth flash to fuse storage to GPUs in three "
                  "dimensions, while China mandated 50% domestic equipment for chipmakers and "
                  "Intel confirmed 14A will debut High-NA EUV.",
         "domain": "compute", "actor": ["ymtc", "china", "intel"],
         "evidences": ["silicon-curtain", "vertical-silicon"],
         "supersedes": [B + "developments/2025-12-27-ssd-next-gpu-storage"]},
        {"id": "2025-12-31-wifi-becomes-a-motion-sensor",
         "title": "Wi-Fi becomes a native motion sensor",
         "claim": "The IEEE 802.11bf standard turns Wi-Fi into a native motion detector, making "
                  "ambient radio a sensing layer.",
         "domain": "compute", "evidences": ["data-beyond-text", "politics-as-infrastructure"]},
        {"id": "2025-12-31-a-bowl-every-ten-seconds",
         "title": "Automated makelines produce a bowl every ten seconds",
         "claim": "Cava and Chipotle are deploying Hyphen's automated makelines producing a bowl "
                  "every ten seconds, while humanoids direct traffic in China and at least 36 "
                  "humanoid vendors prepare for CES 2026.",
         "domain": "robotics", "actor": ["hyphen", "china"], "score": "1 bowl / 10 s",
         "evidences": ["work-displaced", "physical-recursion"]},
        {"id": "2025-12-31-ml-finds-proton-conducting-membranes",
         "title": "ML-guided simulation finds new 2D membrane materials",
         "claim": "Machine-learning-guided simulations identified new two-dimensional materials "
                  "for proton-conducting membranes, while ETH Zurich developed electrolysis to "
                  "neutralize DDT.",
         "domain": "science", "actor": ["eth-zurich"],
         "evidences": ["automated-science", "biosphere-uplift"]},
        {"id": "2025-12-31-adhd-linked-to-circadian-dysfunction",
         "title": "ADHD is linked to circadian rhythm dysfunction",
         "claim": "Researchers linked ADHD to circadian rhythm dysfunction, suggesting "
                  "scheduling as a therapeutic vector, as Baltimore recorded its lowest "
                  "homicide rate in 48 years.",
         "domain": "biotech", "evidences": ["hardware-grade-biology"]},
    ],
}
