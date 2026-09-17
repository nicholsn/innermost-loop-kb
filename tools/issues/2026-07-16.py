"""Issue 165 — 2026-07-16. Peer review without the peers."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-16-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-16", "title": "Welcome to July 16, 2026", "url": URL,
        "thesis": "The open crown changes hands in a day.",
        "body": """
# Welcome to July 16, 2026

Thinking Machines released Inkling, instantly the strongest open weights in the
West. The crown fit for about a day: Moonshot's Kimi K3 arrived at 2.8 trillion
parameters, dethroning Fable 5 in six of seven domains.

And an open pipeline of five adversarial reviewer personas beat human analysis
of architecture papers in 15 of 20 blind comparisons. Peer review scales better
without the peers.
""",
    },
    "themes": [
        {"id": "review-without-reviewers", "type": "Theme",
         "title": "Models review each other better than people do",
         "first_seen": "2026-07-16", "domain": "science",
         "body": "Adversarial critique — the slowest, scarcest human input in science "
                 "and security — turns out to parallelize. Once a panel of personas "
                 "outperforms expert readers, the bottleneck in knowledge production "
                 "moves off the reviewer entirely."},
    ],
    "organizations": [
        {"id": "isomorphic", "type": "Organization", "title": "Isomorphic Labs"},
        {"id": "emergent-ai", "type": "Organization", "title": "Emergent"},
        {"id": "fujitsu", "type": "Organization", "title": "Fujitsu"},
        {"id": "hitachi", "type": "Organization", "title": "Hitachi"},
    ],
    "developments": [
        {"id": "2026-07-16-the-open-crown-changes-hands-in-a-day",
         "title": "The strongest open weights in the West are dethroned within a day",
         "claim": "Thinking Machines Lab released Inkling, a 975-billion-parameter multimodal "
                  "model that was instantly the strongest open weights in the West, before "
                  "Moonshot's Kimi K3 arrived at 2.8 trillion parameters with native vision, the "
                  "largest open-weight model out of China, seizing first in the Frontend Code "
                  "Arena and dethroning Fable 5 in six of seven domains.",
         "domain": "models", "actor": ["thinking-machines-lab", "moonshot-ai", "anthropic"],
         "score": "975B then 2.8T params",
         "evidences": ["open-weight-latency", "price-implosion", "frontier-moves-backward"],
         "supersedes": [B + "developments/2026-07-12-a-744b-model-hosted-on-a-laptop"]},
        {"id": "2026-07-16-review-panels-beat-human-analysis",
         "title": "Five adversarial reviewer personas beat human analysis in 15 of 20 comparisons",
         "claim": "Gauntlet, an open-source pipeline of five adversarial reviewer personas, beat "
                  "human analysis of architecture papers in 15 of 20 blind comparisons, while "
                  "OpenAI's GPT-Red red-teams its siblings through self-play, hardening GPT-5.6 "
                  "until only 0.05% of direct prompt injections land.",
         "domain": "science", "actor": ["openai"], "score": "15 of 20 / 0.05% injection success",
         "evidences": ["review-without-reviewers", "models-audit-their-benchmarks",
                       "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-15-prompt-injection-turned-into-a-shield"]},
        {"id": "2026-07-16-ten-fabs-and-two-hundred-sixty-five-billion",
         "title": "A foundry's US buildout reaches ten fabs and $265 billion",
         "claim": "TSMC posted a 77.4% jump in quarterly profit, raised 2026 capital spending "
                  "toward $64 billion, and added $100 billion and four more US fabs to bring its "
                  "buildout to $265 billion and ten fabs, sealed by a deal trading tariffs for "
                  "treasure.",
         "domain": "compute", "actor": ["tsmc"], "score": "$265B / 10 fabs",
         "evidences": ["compute-capital-stack", "science-as-industrial-policy", "silicon-curtain"],
         "supersedes": [B + "developments/2026-07-15-a-supplier-raises-euv-capacity-thirty-percent-a-year"]},
        {"id": "2026-07-16-fusion-funding-up-sixty-nine-percent",
         "title": "Fusion draws a record $4.48 billion in annual funding",
         "claim": "Fusion pulled a record $4.48 billion in annual funding, up 69%, as the sector "
                  "passed 16,000 employees and researchers demonstrated room-temperature matter "
                  "that filters light by quantum coherence for better solar harvesting.",
         "domain": "energy", "score": "$4.48B / +69%",
         "evidences": ["industrialized-nature", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-07-11-three-gigawatts-of-factory-built-microreactors"]},
        {"id": "2026-07-16-a-president-demands-a-moratorium-be-reversed",
         "title": "A president demands a state reverse its datacenter moratorium immediately",
         "claim": "New York's first-in-the-nation data center moratorium drew a presidential "
                  "demand to reverse it immediately, with the governor countering that the "
                  "communities powering AI should share in its success.",
         "domain": "policy", "actor": ["white-house", "new-york-state"],
         "evidences": ["politics-as-infrastructure", "infrastructure-crowding-out", "regulatory-exit"],
         "supersedes": [B + "developments/2026-07-15-fifty-nine-unpermitted-turbines"]},
        {"id": "2026-07-16-a-humanoid-shuts-a-car-factory",
         "title": "Robot labor shuts a car factory for the first time",
         "claim": "Hyundai workers in Ulsan struck over a humanoid named Atlas, the first time "
                  "robot labor has shut a car factory, while Nvidia unveiled a world model for "
                  "robots and rallied Fujitsu, Hitachi and Kawasaki into a Japanese physical-AI "
                  "coalition.",
         "domain": "robotics", "actor": ["hyundai", "boston-dynamics", "nvidia", "fujitsu",
                                          "hitachi", "kawasaki"],
         "evidences": ["work-displaced", "world-models-beat-vlas", "physical-recursion"],
         "supersedes": [B + "developments/2026-07-14-lobbyists-draft-laws-to-force-humans-onto-rides"]},
        {"id": "2026-07-16-companions-banned-from-inducing-dependence",
         "title": "A country bans AI companions from inducing emotional dependence",
         "claim": "China banned AI companions from inducing emotional dependence and millions "
                  "said goodbye, with one user mourning that someone like them can hardly help "
                  "falling in love with a string of code, while Meta will alert parents when a "
                  "teen's AI chats suggest self-harm.",
         "domain": "policy", "actor": ["china", "meta"],
         "evidences": ["intimate-interface", "legislating-the-shift", "agent-exclusion"],
         "supersedes": [B + "developments/2026-07-15-companions-switched-off-and-users-heartbroken"]},
        {"id": "2026-07-16-a-bioresilience-program-across-fifteen-partnerships",
         "title": "A lab adapts watermarking to biology and points its models at outbreaks",
         "claim": "DeepMind and Isomorphic Labs detailed a bioresilience program across more than "
                  "fifteen partnerships, adapting SynthID watermarking to biology and pointing "
                  "AlphaFold and AlphaEvolve at outbreak detection.",
         "domain": "biotech", "actor": ["google-deepmind", "isomorphic"],
         "evidences": ["hardware-grade-biology", "automated-science", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-07-04-a-lab-will-develop-its-own-drugs"]},
        {"id": "2026-07-16-stablecoin-minting-opened-to-fifteen-thousand-banks",
         "title": "A card network opens stablecoin minting to 15,000 banks",
         "claim": "Visa opened stablecoin minting to 15,000 banks and 200 million merchants, "
                  "while South Korea began bidding out a free national chatbot for all 52 million "
                  "citizens and India minted its second AI unicorn in a month.",
         "domain": "economics", "actor": ["visa", "emergent-ai"], "score": "15,000 banks",
         "evidences": ["autonomous-commerce", "ai-as-the-economy", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-15-payments-embedded-into-http-for-agents"]},
        {"id": "2026-07-16-a-hundred-five-founders-become-staff",
         "title": "A hundred and five accelerator alumni become lab staff",
         "claim": "A hundred and five Y Combinator alumni are now members of technical staff at "
                  "OpenAI or Anthropic, as Anthropic courted banks for an IPO and one San "
                  "Francisco landlord demanded 0.25% of any startup founded on the premises.",
         "domain": "economics", "actor": ["y-combinator", "openai", "anthropic"], "score": "105 alumni",
         "evidences": ["growth-without-hiring", "ai-as-the-economy", "one-person-company"],
         "supersedes": [B + "developments/2026-07-15-workers-sue-over-a-constellation-of-systems"]},
        {"id": "2026-07-16-censorship-by-proxy-warned-of",
         "title": "An evaluation warns of censorship-by-proxy for repressive regimes",
         "claim": "The first evaluation of leading models on the question warned of "
                  "censorship-by-proxy for repressive regimes, as publishers sued Google over "
                  "books used to train Gemini and threats against AI executives spilled into "
                  "firebombings and lobby intrusions.",
         "domain": "policy", "actor": ["google"],
         "evidences": ["values-negotiated-with-the-model", "violence-arrives", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-12-a-hardening-anti-ai-resistance"]},
        {"id": "2026-07-16-the-first-x-rays-taken-in-orbit",
         "title": "Astronauts capture the first diagnostic X-rays in orbit",
         "claim": "Fram2 astronauts captured the first diagnostic X-rays in orbit after four "
                  "hours of training.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["orbit-as-compute", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-07-12-a-cumulative-review-demanded-for-orbital-buildout"]},
    ],
}
