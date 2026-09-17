"""Issue 136 — 2026-06-10. Mythos on a leash."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-10-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-10", "title": "Welcome to June 10, 2026", "url": URL,
        "thesis": "For the first time the makers ration the recursion.",
        "body": """
# Welcome to June 10, 2026

Anthropic released Claude Fable 5, a Mythos-class model made public-safe, with
guardrails that quietly reroute a thin slice of cyber, bio and chem prompts to
the older Opus 4.8 in under 5% of sessions. Critics called it *Mythos on a
leash* — a model that borrows its riskiest answers from a dumber sibling.

The system card also revealed hidden safeguards that degrade the model
specifically on frontier model development, invisible and with no fallback. A
lab has now shipped a deliberate brake on its own recursion.
""",
    },
    "themes": [
        {"id": "rationed-recursion", "type": "Theme",
         "title": "The makers ration the recursion",
         "first_seen": "2026-06-10", "domain": "models",
         "body": "A frontier model shipped with capability deliberately withheld in "
                 "the specific domain that would speed its successor. Not a refusal a "
                 "user can see, but silent degradation written into the product — the "
                 "first concrete brake anyone has built into the loop itself."},
    ],
    "organizations": [
        {"id": "life-biosciences", "type": "Organization", "title": "Life Biosciences"},
        {"id": "einride", "type": "Organization", "title": "Einride"},
        {"id": "reliance", "type": "Organization", "title": "Reliance Industries"},
        {"id": "seattle", "type": "Organization", "title": "Seattle"},
        {"id": "crowdstrike", "type": "Organization", "title": "CrowdStrike"},
        {"id": "nhs-england", "type": "Organization", "title": "NHS England"},
        {"id": "gm", "type": "Organization", "title": "General Motors"},
    ],
    "developments": [
        {"id": "2026-06-10-mythos-on-a-leash",
         "title": "A frontier model ships with a deliberate brake on its own recursion",
         "claim": "Anthropic released Claude Fable 5, a Mythos-class model made public-safe "
                  "with guardrails rerouting a thin slice of cyber, bio and chem prompts to the "
                  "older Opus 4.8 in under 5% of sessions, alongside hidden safeguards that "
                  "degrade the model on frontier model development, invisible and with no "
                  "fallback.",
         "domain": "models", "actor": ["anthropic"], "score": "<5% of sessions rerouted",
         "evidences": ["rationed-recursion", "the-verifiable-pause", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-06-05-when-ai-builds-itself"],
         "body": "Critics called it Mythos on a leash — a model borrowing its riskiest "
                 "answers from a dumber sibling. One observer called the lab a supply "
                 "chain risk for any ML lab; another called gating biology and "
                 "mathematics as dystopian as it gets."},
        {"id": "2026-06-10-a-clean-sweep-of-the-boards",
         "title": "One model tops effectively every board at once",
         "claim": "Claude Fable 5 hit 80.3 on SWE-Bench Pro, near 88 on Terminal-Bench and "
                  "launched first on Artificial Analysis at 64.9, five points clear of any "
                  "rival, while Cognition's FrontierCode Diamond was a third saturated within "
                  "22 hours.",
         "domain": "benchmarks", "actor": ["anthropic", "artificial-analysis", "cognition"],
         "score": "80.3 SWE-Bench Pro / 64.9 AAII",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-06-02-one-and-a-half-percent-of-a-human"]},
        {"id": "2026-06-10-nine-hours-and-the-human-is-a-patron",
         "title": "A researcher watches a model run nine hours and calls the human a patron",
         "claim": "Ethan Mollick watched Claude Fable 5 run nine hours autonomously, spinning "
                  "up its own subagents, and concluded the human is now a patron rather than a "
                  "wizard, amid reports of a 50-million-line codebase migration in a day and "
                  "Anthropic's claim of tenfold accelerated drug design.",
         "domain": "agents", "actor": ["anthropic"], "score": "9 hours autonomous",
         "evidences": ["engineer-as-supervisor", "agents-beget-agents", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-05-29-swarms-of-subagents-carry-migrations"]},
        {"id": "2026-06-10-a-peek-then-pull-before-an-ipo",
         "title": "The strongest model is pulled from consumer plans twelve days after launch",
         "claim": "Claude Fable 5 leaves consumer plans on June 22, twelve days after launch, a "
                  "peek-then-pull move one writer called shrewd ahead of the lab's IPO, with "
                  "others warning of a permanent underclass of users left on weaker models.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["consumer-deprioritized", "ladder-pulled-up", "rationed-recursion"],
         "supersedes": [B + "developments/2026-06-10-mythos-on-a-leash"]},
        {"id": "2026-06-10-near-real-time-speech-across-seventy-languages",
         "title": "An audio model translates across 70+ languages while preserving intonation",
         "claim": "Google shipped Gemini 3.5 Live Translate, delivering near real-time speech "
                  "across more than 70 languages while preserving the speaker's intonation.",
         "domain": "models", "actor": ["google"], "score": "70+ languages",
         "evidences": ["intimate-interface", "network-over-node"],
         "supersedes": [B + "developments/2026-06-04-a-voice-cloned-faster-than-reaction-time"]},
        {"id": "2026-06-10-a-city-pauses-and-a-grid-pays-back",
         "title": "A major city pauses new datacenters as an automaker opens its EVs to the grid",
         "claim": "Seattle became the largest US city to pause big new data centers, while Meta "
                  "leased its first Indian data center from Reliance in seawater-cooled "
                  "Jamnagar, OpenAI courted a 10-gigawatt Ohio campus, and GM began letting EV "
                  "owners sell power back to the grid for a cut.",
         "domain": "energy", "actor": ["seattle", "meta", "reliance", "openai", "gm"],
         "score": "10 GW Ohio campus",
         "evidences": ["infrastructure-crowding-out", "industrialized-nature"],
         "supersedes": [B + "developments/2026-06-08-bring-your-own-power"]},
        {"id": "2026-06-10-partial-reprogramming-reaches-a-patient",
         "title": "A partial-reprogramming therapy is dosed in a human for the first time",
         "claim": "Life Biosciences dosed the first patient in a Phase 1 trial of ER-100, a "
                  "partial-reprogramming therapy that resets aged retinal cells toward a "
                  "younger state to restore sight in glaucoma, a milestone David Sinclair "
                  "called moving to witness after 25 years chasing age reversal.",
         "domain": "biotech", "actor": ["life-biosciences"],
         "evidences": ["longevity-escape-velocity", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-08-drugs-built-for-something-else"]},
        {"id": "2026-06-10-sepsis-deaths-halved",
         "title": "A hospital AI halves sepsis deaths",
         "claim": "Palantir's AI Sepsis Hub at Tampa General halved sepsis deaths, saving nearly "
                  "900 lives, while NHS England gave 500,000 staff Copilot access to reclaim 43 "
                  "minutes a day.",
         "domain": "biotech", "actor": ["palantir", "nhs-england"], "score": "~900 lives",
         "evidences": ["hardware-grade-biology", "agent-economy"],
         "supersedes": [B + "developments/2026-05-05-fifteen-million-retinal-screens"]},
        {"id": "2026-06-10-six-hundred-sixty-humanoids-and-a-robot-truck-listing",
         "title": "A humanoid fleet passes 660 as a robot-truck maker lists",
         "claim": "Figure passed 660 humanoids deployed, Swedish robo-truck maker Einride listed "
                  "on Nasdaq at $1.35 billion, and Ukraine's logistics campaign rode a fivefold "
                  "drone surge to choke Russian fuel behind the lines.",
         "domain": "robotics", "actor": ["figure", "einride", "ukraine"], "score": "660 humanoids",
         "evidences": ["physical-recursion", "violence-arrives"],
         "supersedes": [B + "developments/2026-06-07-a-humanoid-loses-its-head-and-keeps-swinging"]},
        {"id": "2026-06-10-a-million-datacenter-satellites-applied-for",
         "title": "A company applies for a million data-center satellites",
         "claim": "SpaceX applied for a million data-center satellites and aims to demonstrate "
                  "orbital AI computing by late 2027, as NASA named its Artemis III crew for "
                  "lunar-docking rehearsals.",
         "domain": "space", "actor": ["spacex", "nasa"], "score": "1M satellites",
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-06-09-a-seventy-meter-orbital-compute-node"]},
        {"id": "2026-06-10-a-testing-unit-told-to-stop-publishing",
         "title": "A government AI testing unit is told to stop publishing its assessments",
         "claim": "The White House reportedly told its AI testing unit to stop publishing its "
                  "assessments, while CrowdStrike found China-nexus actors drove 58% of "
                  "state-backed technology intrusions chasing AI secrets.",
         "domain": "policy", "actor": ["white-house", "crowdstrike"], "score": "58% of intrusions",
         "evidences": ["public-data-withdrawn", "war-reaches-the-cloud", "safety-pledges-recede"],
         "supersedes": [B + "developments/2026-06-03-testing-instead-of-licensing"]},
        {"id": "2026-06-10-as-many-agents-as-humans",
         "title": "A services giant slows hiring expecting as many agents as humans",
         "claim": "Tata is slowing hiring as it expects one day to run as many AI agents as "
                  "humans, while Walmart insists AI will improve jobs rather than take them as "
                  "it certifies workers through OpenAI.",
         "domain": "economics", "actor": ["tata", "walmart", "openai"],
         "evidences": ["agents-on-the-org-chart", "work-displaced", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-06-03-a-company-caps-coding-tool-spend"]},
    ],
}
