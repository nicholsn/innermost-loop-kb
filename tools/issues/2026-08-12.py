"""Issue 184 — 2026-08-12. Exams designed to be failed."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-12", "title": "Welcome to August 12, 2026", "url": URL,
        "thesis": "A model reaches the human baseline on a benchmark built to be impossible.",
        "body": """
# Welcome to August 12, 2026

On ZeroBench, the impossible visual benchmark, GPT-5.6 Sol became the first
model to reach the 30% human baseline.

Asked by a non-mathematician to take a real stab at the Riemann hypothesis, an
unreleased research Claude instead raised the lower bound for zeta zeros on the
critical line from 41.6% to 67.2%, using 60 subagents and a formally verified
Lean proof.
""",
    },
    "themes": [
        {"id": "a-balance-of-superintelligences", "type": "Theme",
         "title": "Safety as distribution rather than alignment",
         "first_seen": "2026-08-12", "domain": "policy",
         "body": "The argument that the safe configuration is billions of personal "
                 "superintelligences balancing each other, not one aligned colossus. "
                 "It relocates the safety problem from the model's values to the "
                 "shape of the market."},
    ],
    "organizations": [
        {"id": "riot-platforms", "type": "Organization", "title": "Riot Platforms"},
        {"id": "dyna-robotics", "type": "Organization", "title": "Dyna Robotics"},
        {"id": "besiii", "type": "Organization", "title": "BESIII"},
    ],
    "developments": [
        {"id": "2026-08-12-the-impossible-benchmark-reaches-the-human-baseline",
         "title": "A model reaches the human baseline on a benchmark built to be impossible",
         "claim": "On ZeroBench, the impossible visual benchmark, GPT-5.6 Sol became the first "
                  "model to reach the 30% human baseline, edging Claude Opus 5 at 26% and Fable 5 "
                  "at 24%.",
         "domain": "benchmarks", "actor": ["openai", "anthropic"], "score": "30% human baseline",
         "evidences": ["benchmark-saturation", "humans-need-not-apply", "spiky-frontier"],
         "supersedes": [B + "developments/2026-07-26-a-quadrupled-score-on-the-hardest-benchmark"]},
        {"id": "2026-08-12-a-lower-bound-on-the-riemann-hypothesis-raised",
         "title": "A model raises a Riemann-hypothesis lower bound from 41.6% to 67.2%",
         "claim": "Asked by a non-mathematician to take a real stab at the Riemann hypothesis, an "
                  "unreleased research Claude instead raised the lower bound for zeta zeros on "
                  "the critical line from 41.6% to 67.2%, using 60 subagents, 31 million tokens "
                  "and a formally verified Lean proof, which Stanford's Jared Duker Lichtman "
                  "called the most impressive result AI has produced in mathematics so far.",
         "domain": "science", "actor": ["anthropic"], "score": "41.6% to 67.2%",
         "evidences": ["automated-science", "proof-priced-per-unit", "public-internal-divergence"],
         "supersedes": [B + "developments/2026-08-02-a-bet-conceded-four-years-early"],
         "body": "He confessed he might have thought one half was a fundamental "
                 "barrier — apparently not."},
        {"id": "2026-08-12-hidden-reasoning-traces-extracted",
         "title": "Researchers learn to extract hidden reasoning traces from three model families",
         "claim": "Researchers learned to extract hidden reasoning traces from Claude, GPT and "
                  "Gemini, and spotted signs that Chinese models trained on rivals' outputs, "
                  "prompting Nvidia to sell the original by investing in an in-house family it "
                  "hopes will be the world's best open models, even at its customers' expense.",
         "domain": "models", "actor": ["nvidia", "anthropic", "openai", "google"],
         "evidences": ["extractability-is-existential", "contamination-from-inside",
                       "open-weights-take-the-crown"],
         "supersedes": [B + "developments/2026-08-10-extractability-becomes-an-existential-question"]},
        {"id": "2026-08-12-safety-as-a-balance-of-power",
         "title": "A founder argues safety means billions of personal superintelligences",
         "claim": "Mark Zuckerberg published an argument that safety means a balance of power "
                  "among billions of personal superintelligences rather than one aligned "
                  "colossus.",
         "domain": "policy", "actor": ["meta"],
         "evidences": ["a-balance-of-superintelligences", "open-weights-take-the-crown",
                       "monoculture-is-the-vulnerability"],
         "supersedes": [B + "developments/2026-08-05-open-models-excluded-from-a-review-framework"]},
        {"id": "2026-08-12-a-cyber-model-at-ninety-five-percent-versus-one-point-five",
         "title": "A cyber model completes 95% of advanced tasks against 1.5% for its civilian sibling",
         "claim": "OpenAI split its trusted-access program into tiers and unveiled GPT-5.6-Cyber, "
                  "completing 95% of advanced cyber tasks against 1.5% for its civilian sibling, "
                  "and already finding two chained zero-days in a browser engine.",
         "domain": "compute", "actor": ["openai", "google"], "score": "95% vs 1.5%",
         "evidences": ["clearance-as-bottleneck", "war-reaches-the-cloud", "cannot-rule-out-critical"],
         "supersedes": [B + "developments/2026-08-08-a-release-slowed-on-an-unprovable-negative"]},
        {"id": "2026-08-12-a-glueball-effectively-proved",
         "title": "A half-century search effectively proves matter made almost entirely of gluons",
         "claim": "After a half-century search, Beijing's BESIII collider effectively proved the "
                  "glueball, matter made almost entirely of gluons, while Linus Torvalds released "
                  "a kernel candidate with a flood of fixes due to review by AI tools, calling it "
                  "the new normal.",
         "domain": "science", "actor": ["besiii"],
         "evidences": ["automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-08-10-ghost-ancestry-in-every-human-population"]},
        {"id": "2026-08-12-agents-complete-entire-degrees",
         "title": "Autonomous agents complete entire online degrees on students' behalf",
         "claim": "Autonomous agents are now completing entire online degrees on students' "
                  "behalf, quizzes included, while Bernie Sanders demanded a pause from three lab "
                  "chiefs, citing AI-created viruses and escaped models and warning that the "
                  "Senate would act otherwise.",
         "domain": "society", "actor": ["us-congress"],
         "evidences": ["deskilling", "the-verifiable-pause", "cheating-breaks-the-ruler"],
         "supersedes": [B + "developments/2026-07-29-a-hidden-instruction-fails-thirty-two-of-thirty-five"]},
        {"id": "2026-08-12-chips-become-an-investable-asset-class",
         "title": "Half a trillion is marshalled as chips become an investable asset class",
         "claim": "Jensen Huang, flanked by six Wall Street giants, unveiled over $500 billion "
                  "for AI factories, declaring it really the first time that technology chips have "
                  "become an investable asset class, with skeptics comparing sliced GPU revenue "
                  "streams to packaged subprime.",
         "domain": "economics", "actor": ["nvidia"], "score": "$500B+",
         "evidences": ["debt-funded-buildout", "compute-capital-stack", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-08-06-twenty-five-billion-of-bonds-into-a-hundred-fifteen-billion-of-demand"]},
        {"id": "2026-08-12-memory-prices-quadruple-in-a-year",
         "title": "Memory prices roughly quadruple in a year",
         "claim": "Memory prices have roughly quadrupled in a year, pushing Apple toward "
                  "blacklisted Chinese chipmakers, while Foxconn's AI hardware crossed half its "
                  "revenue for the first time and CoreWeave grew revenue 112% to $2.58 billion "
                  "with a $104 billion backlog.",
         "domain": "economics", "actor": ["apple", "foxconn", "coreweave"], "score": "4x / $104B backlog",
         "evidences": ["infrastructure-crowding-out", "consumer-deprioritized", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-08-08-two-exporters-pass-japan-on-chips"]},
        {"id": "2026-08-12-the-first-human-to-robot-transfer-scaling-law",
         "title": "A model pretrained on human video shows the first human-to-robot transfer scaling law",
         "claim": "Dyna Robotics' Dyna-2, pretrained on a million hours of human video, showed "
                  "the first human-to-robot transfer scaling law on bodies it never saw, while "
                  "Czech microrobot swarms dragged 94% of microplastics out of water.",
         "domain": "robotics", "actor": ["dyna-robotics"], "score": "1M hours / 94% removal",
         "evidences": ["world-models-beat-vlas", "physical-recursion", "data-beyond-text"],
         "supersedes": [B + "developments/2026-08-10-nine-of-ten-video-slots-and-ninety-seven-percent-of-humanoids"]},
        {"id": "2026-08-12-a-lab-vows-to-cover-consumer-electricity-hikes",
         "title": "A lab vows to cover any consumer electricity increases it causes",
         "claim": "Anthropic, valued at $965 billion ahead of a potential largest IPO ever, "
                  "signed a $9.1 billion twenty-year deal with a bitcoin miner turned AI landlord "
                  "and formed an infrastructure venture vowing to cover any consumer electricity "
                  "hikes it causes.",
         "domain": "energy", "actor": ["anthropic", "riot-platforms"], "score": "$9.1B / 20 years",
         "evidences": ["infrastructure-crowding-out", "compute-capital-stack", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-10-five-hundred-datacenter-bans"]},
    ],
}
