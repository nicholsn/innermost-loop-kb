"""Issue 081 — 2026-03-23. Recursive self-improvement goes global."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-23-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-23", "title": "Welcome to March 23, 2026", "url": URL,
        "thesis": "A second country's lab says its model participates in its own evolution.",
        "body": """
# Welcome to March 23, 2026

MiniMax announced that M2.7 is its "first model deeply participating in its own
evolution." A week after Anthropic's alignment lead called recursive
self-improvement a present phenomenon, a Chinese lab says the same thing about
its own system.

Snowflake laid off its entire technical writing team — around 70 people —
replacing them with AI.
""",
    },
    "organizations": [
        {"id": "mantic", "type": "Organization", "title": "Mantic",
         "body": "Applied reinforcement learning to world-event forecasting."},
        {"id": "yuanjie", "type": "Organization", "title": "Yuanjie Semiconductor",
         "body": "Chinese optics supplier; shares up roughly 780% on AI demand."},
        {"id": "mediatek", "type": "Organization", "title": "MediaTek",
         "resource": "https://www.mediatek.com/"},
    ],
    "systems": [
        {"id": "minimax-m2-7", "type": "AISystem", "title": "MiniMax M2.7",
         "description": "MiniMax's M2-series coding and agent model, presented by its lab as the "
                        "first of its models to take part in its own evolution by building and "
                        "refining its own training harness.",
         "developed_by": [B + "organizations/minimax"], "modality": "text",
         "resource": "https://www.minimax.io/news/minimax-m27-en",
         "sameAs": ["http://www.wikidata.org/entity/Q140570527"],
         "tags": ["open-weight-model", "coding-agent"],
         "body": "M2.7 is a mixture-of-experts model tuned for software engineering, agent "
                 "harnesses and long-horizon office work; MiniMax reports a GDPval-AA Elo of "
                 "1495, which it calls the highest among open-source models "
                 "([announcement](https://www.minimax.io/news/minimax-m27-en)). Its place in "
                 "this corpus is the lab's claim that it is the "
                 "[first model deeply participating in its own evolution](/developments/2026-03-23-minimax-model-participates-in-its-own-evolution.md): "
                 "M2.7 wrote and repaired the harness used in its own reinforcement-learning "
                 "experiments, then improved the learning process from the results. It succeeds "
                 "[M2.1](/systems/minimax-m2-1.md) in the M2 line."},
    ],
    "developments": [
        {"id": "2026-03-23-minimax-model-participates-in-its-own-evolution",
         "title": "A Chinese lab says its model participates in its own evolution",
         "claim": "MiniMax announced that M2.7 is its first model deeply participating in its "
                  "own evolution, confirming recursive self-improvement has gone global.",
         "description": "The loop stops being a single-lab or single-country phenomenon: a "
                        "Chinese lab's release note adopts the same self-evolution language as "
                        "the American frontier, making recursion the shared idiom of the field.",
         "domain": "models", "actor": ["minimax"], "about": [B + "systems/minimax-m2-7"],
         "occurred_on": "2026-03-18",
         "evidences": ["recursive-self-improvement", "silicon-curtain", "takeoff-declared"],
         "supersedes": [B + "developments/2026-03-22-openai-targets-a-research-intern-by-september"],
         "relatedTo": [B + "developments/2026-06-25-an-agent-rewrites-its-own-harness",
                       B + "developments/2026-03-24-hyperagents-edit-their-own-mechanism",
                       B + "systems/minimax-m2-1"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-03-16-rsi-is-a-present-phenomenon",
                        "relation_label": "corroborates"}],
         "tags": ["rsi", "self-modification", "open-weights"],
         "supporting_text": "first model deeply participating in its own evolution",
         "sources": [{"id": "minimax-m2-7-announcement",
                      "resource": "https://www.minimax.io/news/minimax-m27-en",
                      "title": "MiniMax M2.7: Early Echoes of Self-Evolution",
                      "author": "org:minimax", "last_modified": "2026-03-18"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "A week after one lab called it a present phenomenon, a lab on the other side "
                 "of the Pacific says the same of its own system. MiniMax's release note, titled "
                 "\"Early Echoes of Self-Evolution\", describes [M2.7](/systems/minimax-m2-7.md) "
                 "building and repairing the agent harness used in its own reinforcement-learning "
                 "experiments and then improving its learning process from the results; in a "
                 "separate run MiniMax had M2.7 iterate on an internal coding scaffold for over "
                 "100 analyse-modify-evaluate rounds, which it says produced a 30% improvement on "
                 "internal evaluation sets "
                 "([MiniMax](https://www.minimax.io/news/minimax-m27-en)). It corroborates "
                 "[Hubinger's statement](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) "
                 "from outside the American labs, and the harness-editing mechanism anticipates "
                 "June's [agent that rewrites its own scaffolding](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md); "
                 "the next day Meta's [hyperagents](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md) "
                 "gave the same pattern a formal treatment."},
        {"id": "2026-03-23-deleted-post-about-a-robotics-breakthrough",
         "title": "A posted-then-deleted claim hints at an unannounced robotics result",
         "claim": "Google's Logan Kilpatrick posted and then hastily deleted a claim that all "
                  "the industries thought safe from AI are about to be disrupted, in an "
                  "apparent reference to an unannounced DeepMind robotics breakthrough.",
         "domain": "robotics", "actor": ["google", "google-deepmind"],
         "evidences": ["physical-recursion", "takeoff-declared"]},
        {"id": "2026-03-23-rl-improves-world-event-forecasting",
         "title": "Reinforcement learning improves forecasting of world events",
         "claim": "Mantic and Thinking Machines demonstrated significant gains in world-event "
                  "forecasting by applying reinforcement learning, training models to predict "
                  "the future with the rigor they use to parse the past.",
         "domain": "models", "actor": ["mantic", "thinking-machines-lab"],
         "evidences": ["discovery-as-process", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-13-prediction-arena-real-money"]},
        {"id": "2026-03-23-zuckerberg-builds-an-agent-to-be-ceo",
         "title": "A chief executive builds an agent to help him be chief executive",
         "claim": "Mark Zuckerberg is building an AI agent to help him be chief executive and "
                  "wants everyone inside and outside Meta to eventually have their own, while "
                  "developers trade tips on attracting talented AI bots to their open-source "
                  "projects.",
         "domain": "economics", "actor": ["meta"],
         "evidences": ["agents-on-the-org-chart", "humans-need-not-apply"],
         "supersedes": [B + "developments/2026-03-20-g42-posts-a-job-for-agents-only"]},
        {"id": "2026-03-23-snowflake-replaces-its-writers",
         "title": "A company replaces its entire technical writing team",
         "claim": "Snowflake laid off its entire technical writing team of around seventy people "
                  "and replaced them with AI, while young people are pivoting to blue-collar "
                  "careers as firefighters and electricians to AI-proof themselves.",
         "domain": "economics", "actor": ["snowflake"], "score": "~70 people",
         "evidences": ["work-displaced", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-03-16-meta-plans-20-percent-layoffs"]},
        {"id": "2026-03-23-terafab-one-billion-chips-a-year",
         "title": "Terafab targets a billion chips a year at a kilowatt each",
         "claim": "Elon Musk confirmed Terafab will produce roughly a billion chips per year at "
                  "one kilowatt each, powering 20 million cybercabs, 100 million Optimus units "
                  "and 800 million datacenter chips annually, with the full-scale facility "
                  "needing thousands of acres and over 10 GW.",
         "domain": "compute", "actor": ["tesla", "spacex"], "about": [B + "facilities/terafab"],
         "score": "1B chips/yr / 10+ GW",
         "evidences": ["silicon-designs-itself", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-22-terafab-announced"]},
        {"id": "2026-03-23-tsmc-2nm-booked-through-2028",
         "title": "Leading-edge capacity is booked out through 2028",
         "claim": "TSMC's 2-nm capacity is fully booked through 2028 with its 1.6-nm process "
                  "also under heavy demand, and Nvidia is reportedly redesigning its next "
                  "generation because that capacity will not suffice, shifting less critical "
                  "dies to an older process.",
         "domain": "compute", "actor": ["tsmc", "nvidia", "mediatek"],
         "evidences": ["infrastructure-crowding-out", "vertical-silicon"],
         "supersedes": [B + "developments/2026-03-16-helium-offline-after-drone-strikes"]},
        {"id": "2026-03-23-optics-supplier-up-780-percent",
         "title": "A photonics supplier rises 780% in a year",
         "claim": "Surging AI optics demand lifted China's Yuanjie Semiconductor shares roughly "
                  "780% over the past year, while BYD's chargers can take a 600-mile-range "
                  "vehicle from 10 to 70% in five minutes.",
         "domain": "economics", "actor": ["yuanjie", "byd-auto"], "score": "+780% / 5 minutes",
         "evidences": ["compute-capital-stack", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-03-17-light-based-network-claims-millionfold-speedup"]},
        {"id": "2026-03-23-blue-origin-asks-for-51600-satellites",
         "title": "Blue Origin asks to launch 51,600 satellites for orbital compute",
         "claim": "Blue Origin asked the US government for permission to launch 51,600 "
                  "satellites to handle AI computing from space, while SpaceX and Starcloud "
                  "converged on a common orbital datacenter design and the SpaceX IPO is now "
                  "projected above $2 trillion.",
         "domain": "space", "actor": ["blue-origin", "spacex", "starcloud"],
         "score": "51,600 satellites / $2T",
         "evidences": ["orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-20-theres-a-lot-of-space-in-space"]},
        {"id": "2026-03-23-openai-tempers-datacenter-ambitions",
         "title": "OpenAI tempers its datacenter plans ahead of a listing",
         "claim": "OpenAI has reportedly tempered its data center ambitions ahead of a "
                  "potential listing, realizing public markets do not reward spending as "
                  "enthusiastically as social media does.",
         "domain": "economics", "actor": ["openai"],
         "evidences": ["debt-funded-buildout", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-03-22-softbank-500b-on-an-enrichment-site"]},
        {"id": "2026-03-23-humanoids-for-rent-in-china",
         "title": "Humanoids are rented out for shops and events",
         "claim": "People in China are renting humanoid robots built on Unitree bodies for shops "
                  "and events where they blink, talk and dance, while OpenClaw co-hosted a "
                  "Shenzhen hackathon with 25 real robots and the Tesla Semi proved popular "
                  "with truckers.",
         "domain": "robotics", "actor": ["china", "unitree", "tesla"], "score": "25 robots",
         "evidences": ["physical-recursion", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-03-20-waymo-170-million-miles"]},
        {"id": "2026-03-23-robotaxi-attacked-with-a-passenger-inside",
         "title": "A robotaxi is attacked with its passenger inside",
         "claim": "A Waymo in San Francisco was attacked while carrying passenger Doug Fulop by "
                  "a man who punched the windows, tried to lift the vehicle and shouted that he "
                  "wanted to kill Fulop for giving money to a robot.",
         "domain": "society", "actor": ["waymo"],
         "evidences": ["agent-exclusion", "autonomous-commerce"],
         "body": "The newsletter frames this as a machine protecting a human; readers noted the "
                 "underlying report describes a disabled vehicle rather than a deliberate act."},
        {"id": "2026-03-23-car-t-cells-made-inside-the-body",
         "title": "CAR T cells are generated inside the body for the first time",
         "claim": "Researchers performed the first successful in vivo generation of CAR T cells "
                  "with CRISPR-Cas9, offering a path to more efficient and accessible cancer "
                  "therapies, while Michael Levin's group demonstrated the first xenobots with "
                  "self-assembled nervous systems.",
         "domain": "biotech",
         "evidences": ["hardware-grade-biology", "compiling-matter"],
         "supersedes": [B + "developments/2026-03-22-bioreason-pro-annotates-the-unannotated"],
         "body": "Synthetic life bootstrapping its own wiring."},
    ],
}
