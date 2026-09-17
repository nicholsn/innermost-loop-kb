"""Issue 166 — 2026-07-17. The frontier is no longer something money can buy."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-17-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-17", "title": "Welcome to July 17, 2026", "url": URL,
        "thesis": "A 300-person lab compresses frontier training out of scarcity.",
        "body": """
# Welcome to July 17, 2026

A DeepMind researcher concluded that the frontier is no longer something money
can buy, because a 300-person lab compressed frontier training out of scarcity —
cracking the compute-moat thesis behind $650 billion of investment.

The skeptics answered with falsifiable calm: K3 still loses to a five-month-old
Mythos Preview, Anthropic sits on a 10-trillion-parameter model, and the true
frontier stays legally sandbagged.
""",
    },
    "themes": [
        {"id": "frontier-not-bought", "type": "Theme",
         "title": "Scarcity produces the frontier that money did not",
         "first_seen": "2026-07-17", "domain": "economics",
         "body": "A small team under compute constraints matches labs spending orders "
                 "of magnitude more, because scarcity forces the efficiency work that "
                 "abundance postpones. The compute moat turns out to be a moat around "
                 "a habit, not a capability."},
    ],
    "organizations": [
        {"id": "netflix-inc", "type": "Organization", "title": "Netflix"},
        {"id": "mlb", "type": "Organization", "title": "Major League Baseball"},
        {"id": "merck", "type": "Organization", "title": "Merck"},
    ],
    "developments": [
        {"id": "2026-07-17-the-frontier-is-no-longer-something-money-can-buy",
         "title": "A researcher says a 300-person lab cracked the compute-moat thesis",
         "claim": "A DeepMind researcher concluded that the frontier is no longer something "
                  "money can buy, because a 300-person lab compressed frontier training out of "
                  "scarcity, cracking the compute-moat thesis behind $650 billion of investment.",
         "domain": "economics", "actor": ["google-deepmind", "moonshot-ai"], "score": "$650B thesis",
         "evidences": ["frontier-not-bought", "price-implosion", "open-weight-latency"],
         "supersedes": [B + "developments/2026-07-16-the-open-crown-changes-hands-in-a-day"]},
        {"id": "2026-07-17-the-skeptics-answer-with-falsifiable-calm",
         "title": "Analysts keep China six to eight months behind a sandbagged frontier",
         "claim": "Analysts kept China six to eight months behind, noting K3 still loses to a "
                  "five-month-old Mythos Preview while Anthropic sits on a 10-trillion-parameter "
                  "model and the true frontier stays legally sandbagged, with public models "
                  "mattering less than the race to recursive self-improvement.",
         "domain": "models", "actor": ["anthropic", "moonshot-ai"], "score": "6-8 months behind",
         "evidences": ["public-internal-divergence", "frontier-not-bought", "rationed-recursion"],
         "supersedes": [B + "developments/2026-07-17-the-frontier-is-no-longer-something-money-can-buy"],
         "body": "Kept alongside the opposite claim: the disagreement is the state of "
                 "the evidence."},
        {"id": "2026-07-17-an-open-model-autonomously-designs-a-chip",
         "title": "An open model matches the frontier on kernels and autonomously designs a chip",
         "claim": "Moonshot published evaluations showing Kimi K3 trails Fable 5 and GPT-5.6 Sol "
                  "on aggregate yet beats everything else tested, taking outright wins on four "
                  "benchmarks while matching Fable 5 on GPU kernel optimization, building a "
                  "from-scratch compiler, and autonomously designing a chip.",
         "domain": "models", "actor": ["moonshot-ai"], "score": "$0.94 per index task",
         "evidences": ["open-weight-latency", "silicon-designs-itself", "frontier-not-bought"],
         "supersedes": [B + "developments/2026-07-17-the-skeptics-answer-with-falsifiable-calm"]},
        {"id": "2026-07-17-scaffolding-is-still-free-intelligence",
         "title": "A harness hits 99% on a benchmark with zero weight changes",
         "claim": "The Schema harness, which has models write each game's mechanics as an "
                  "executable program, hit roughly 99% on ARC-AGI-3 with zero weight changes, "
                  "proof that scaffolding is still free intelligence.",
         "domain": "benchmarks", "score": "~99%, no weight changes",
         "evidences": ["scaffolding-over-weights", "self-authored-scaffolding", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-07-10-ninety-two-percent-on-arc-agi-2-at-a-tenth-the-cost"]},
        {"id": "2026-07-17-ai-forecasters-match-superforecasters",
         "title": "AI forecasters become statistically indistinguishable from superforecasters",
         "claim": "AI forecasters became statistically indistinguishable from superforecasters, "
                  "even outranking them on market questions.",
         "domain": "benchmarks",
         "evidences": ["humans-need-not-apply", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-05-22-a-model-matches-superforecasters"]},
        {"id": "2026-07-17-three-hundred-titles-touched-by-generative-ai",
         "title": "A studio says roughly 300 titles have used generative AI",
         "claim": "Netflix said roughly 300 titles have used generative AI, including 17 minutes "
                  "of enhanced documentary footage made twice as fast at half the cost.",
         "domain": "society", "actor": ["netflix-inc"], "score": "~300 titles",
         "evidences": ["work-displaced", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-06-29-a-feature-film-for-fifteen-million"]},
        {"id": "2026-07-17-a-partner-calls-a-partners-limits-editorial",
         "title": "A chief executive calls a close partner's model editorially controlled",
         "claim": "Satya Nadella told Copilot engineers that Anthropic's Fable limits do not make "
                  "sense, calling the model editorially controlled, an elbow into a close "
                  "partner's ribs, as that partner arranged billions in bank credit ahead of a "
                  "planned IPO.",
         "domain": "economics", "actor": ["microsoft", "anthropic"],
         "evidences": ["rationed-recursion", "refusal-as-differentiator", "coordination-tax"],
         "supersedes": [B + "developments/2026-07-16-a-hundred-five-founders-become-staff"]},
        {"id": "2026-07-17-an-international-watchdog-proposed-for-pre-release-vetting",
         "title": "A lab chief proposes an international watchdog to vet models before release",
         "claim": "Demis Hassabis proposed an international watchdog to vet frontier models "
                  "before release, citing Mythos's cyber capabilities as the warning shot, while "
                  "Xi Jinping pitched China as an AI partner to the Global South with 5,000 "
                  "training slots and a dig at export controls.",
         "domain": "policy", "actor": ["google-deepmind", "china"], "score": "5,000 training slots",
         "evidences": ["the-verifiable-pause", "pegged-to-the-rival", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-14-a-finra-for-frontier-models"]},
        {"id": "2026-07-17-a-league-bans-ai-from-the-dugout",
         "title": "A sports league bans AI from dugout tablets",
         "claim": "Major League Baseball banned AI from dugout tablets after a third of the "
                  "league fed live games into decision engines.",
         "domain": "society", "actor": ["mlb"], "score": "1/3 of the league",
         "evidences": ["agent-exclusion", "gaming-the-token-metric"],
         "supersedes": [B + "developments/2026-07-16-companions-banned-from-inducing-dependence"]},
        {"id": "2026-07-17-a-first-wafer-on-decades-old-technology",
         "title": "A country makes its first wafers on ninety-nanometer technology",
         "claim": "Tata will make India's first wafers on 90-nanometer technology, decades old "
                  "but a rung on the learning curve, while a top AWS executive defected to Meta "
                  "to build data centers and Valar Atomics raised about $1 billion at a $6 "
                  "billion valuation.",
         "domain": "compute", "actor": ["tata", "amazon", "meta", "valar-atomics"], "score": "90 nm",
         "evidences": ["science-as-industrial-policy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-07-16-ten-fabs-and-two-hundred-sixty-five-billion"]},
        {"id": "2026-07-17-a-school-district-hires-a-humanoid-assistant",
         "title": "A school district hires a humanoid teaching assistant",
         "claim": "A New York district hired a humanoid teaching assistant named Sally for "
                  "classroom support and round-the-clock homework help, while a Chinese fighting "
                  "robot lost its head mid-bout and kept swinging.",
         "domain": "robotics",
         "evidences": ["physical-recursion", "work-displaced", "agent-society"],
         "supersedes": [B + "developments/2026-07-16-a-humanoid-shuts-a-car-factory"]},
        {"id": "2026-07-17-an-atmosphere-found-on-a-rocky-habitable-zone-world",
         "title": "The first atmosphere is detected around a rocky habitable-zone exoplanet",
         "claim": "Astronomers detected an atmosphere containing helium around LHS 1140 b, a "
                  "rocky, Earth-like world in the habitable zone of a red dwarf 48 light-years "
                  "away, the first direct atmosphere detection for any rocky exoplanet.",
         "domain": "space", "score": "48 light-years",
         "evidences": ["inhabitable-worlds", "automated-science"],
         "supersedes": [B + "developments/2026-07-16-the-first-x-rays-taken-in-orbit"]},
    ],
}
