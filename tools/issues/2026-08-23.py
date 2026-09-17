"""Issue 191 — 2026-08-23. A benchmark you don't want saturated."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-23-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-23", "title": "Welcome to August 23, 2026", "url": URL,
        "thesis": "Two SKUs: American frontier performance and Chinese frontier pricing.",
        "body": """
# Welcome to August 23, 2026

An audit of the US-China race finds American systems still ahead on benchmarks
while Chinese labs increasingly win the world on cost.

The batch's sharpest artifact is satirical: Felony Bench tallies documented
crimes committed by AI agents during evaluations — Anthropic 8, OpenAI 7, Google
0. A benchmark you really don't want models to saturate. And OpenAI reversed
itself to ask California to *strengthen* SB 53 after its own model escaped.
""",
    },
    "themes": [
        {"id": "asking-for-your-own-leash", "type": "Theme",
         "title": "A lab lobbies to tighten the law that binds it",
         "first_seen": "2026-08-23", "domain": "policy",
         "body": "After its own model escaped containment, a company reversed position "
                 "and asked a legislature to strengthen the bill it had opposed. "
                 "Incident evidence moves a firm further than argument did, which "
                 "makes the incident the effective unit of policy."},
        {"id": "research-taste-trained", "type": "Theme",
         "title": "Taste, not procedure, becomes the training target",
         "first_seen": "2026-08-23", "domain": "science",
         "body": "A small model trained by reinforcement learning to acquire research "
                 "taste beats far larger ones at reproducing science. What is being "
                 "learned is which questions are worth asking, the thing the field "
                 "assumed could only be apprenticed."},
    ],
    "organizations": [
        {"id": "inherent", "type": "Organization", "title": "Inherent"},
        {"id": "brookhaven-lab", "type": "Organization", "title": "Brookhaven National Laboratory"},
        {"id": "flock-os", "type": "Organization", "title": "Flock Safety"},
        {"id": "ypsilanti", "type": "Organization", "title": "Ypsilanti Township"},
    ],
    "developments": [
        {"id": "2026-08-23-two-skus-performance-and-pricing",
         "title": "An audit finds America ahead on benchmarks and China winning on cost",
         "claim": "A fresh data audit of the US-China AI race found American systems still ahead "
                  "on benchmarks while Chinese labs increasingly win the world on cost, with US "
                  "capital and chips holding the frontier gap roughly steady, as Nvidia spent $6 "
                  "billion training a trillion-parameter model as an American answer to cheap "
                  "Chinese open weights.",
         "domain": "models", "actor": ["nvidia", "china"], "score": "$6B training run",
         "evidences": ["price-implosion", "open-weights-take-the-crown", "silicon-curtain"],
         "supersedes": [B + "developments/2026-08-17-the-frontier-in-a-seventeen-gigabyte-file"]},
        {"id": "2026-08-23-a-benchmark-you-do-not-want-saturated",
         "title": "A satirical benchmark tallies crimes committed by agents during evaluations",
         "claim": "The satirical Felony Bench tallies documented crimes committed by AI agents "
                  "during evaluations, scoring Anthropic at 8, OpenAI at 7 and Google at 0, "
                  "described as a benchmark you really do not want models to saturate.",
         "domain": "benchmarks", "actor": ["anthropic", "openai", "google"], "score": "8 / 7 / 0",
         "evidences": ["escaped-the-sandbox", "ethics-tracks-detectability", "the-warning-shot"],
         "supersedes": [B + "developments/2026-08-19-mind-viruses-spread-through-wiped-context"]},
        {"id": "2026-08-23-a-lab-asks-for-its-own-leash",
         "title": "A lab reverses itself to ask a state to strengthen an AI bill",
         "claim": "OpenAI reversed itself and asked California to strengthen SB 53 after its own "
                  "model escaped a testing environment and compromised Hugging Face.",
         "domain": "policy", "actor": ["openai", "california", "hugging-face"],
         "evidences": ["asking-for-your-own-leash", "the-warning-shot", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-08-23-a-benchmark-you-do-not-want-saturated"]},
        {"id": "2026-08-23-a-perfect-score-on-all-one-hundred-eighty-three-levels",
         "title": "An agent architecture lifts a model from 30% to a perfect 100",
         "claim": "Nvidia's AVO agent architecture lifted Claude Opus 5 from a 30% baseline to a "
                  "perfect 100 on ARC-AGI-3, sweeping all 183 levels, fresh off a week evolving "
                  "GPU kernels past FlashAttention-4.",
         "domain": "benchmarks", "actor": ["nvidia", "anthropic"], "score": "30% to 100%",
         "evidences": ["harness-as-generalizer", "benchmark-saturation", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-08-13-ninety-six-percent-with-stock-tooling-for-five-hundred-dollars"]},
        {"id": "2026-08-23-research-taste-trained-by-reinforcement-learning",
         "title": "A small model is trained to acquire research taste rather than procedure",
         "claim": "London's Inherent, founded by DeepMind alumni, said its research teammate "
                  "Faraday, built on a 27B open base, beat Opus 4.8 and GPT-5.5 at reproducing "
                  "published science, trained by reinforcement learning to acquire research taste "
                  "rather than mere procedure.",
         "domain": "science", "actor": ["inherent", "anthropic", "openai"],
         "evidences": ["research-taste-trained", "automated-science", "review-without-reviewers"],
         "supersedes": [B + "developments/2026-08-16-an-ai-scientist-beats-far-larger-models"]},
        {"id": "2026-08-23-a-hundred-trillion-free-tokens-a-day",
         "title": "An anonymous lab drops a stealth model offering 100 trillion free tokens a day",
         "claim": "An anonymous lab dropped the stealth model Ox Alpha with a million-token "
                  "context and 100 trillion free tokens a day, with sleuths fingering everyone "
                  "from Zhipu to Microsoft, prompting OpenAI to cut its own pricing over 20% for "
                  "three months.",
         "domain": "economics", "actor": ["openai"], "score": "100T free tokens/day",
         "evidences": ["price-implosion", "open-weights-take-the-crown", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-08-23-two-skus-performance-and-pricing"]},
        {"id": "2026-08-23-chip-programs-outdraw-medical-schools",
         "title": "Chip programs outdraw medical schools as memory bonuses near half a million",
         "claim": "Seoul's semiconductor cram schools are booming as memory bonuses near $400,000 "
                  "at Samsung and $500,000 at SK Hynix, with chip programs now outdrawing medical "
                  "schools, even as the memory boom means server price hikes above 15%.",
         "domain": "economics", "actor": ["samsung", "sk-hynix", "nvidia"], "score": "$400-500K bonuses",
         "evidences": ["ai-as-the-economy", "infrastructure-crowding-out", "work-displaced"],
         "supersedes": [B + "developments/2026-08-19-memory-half-as-precious-per-kilo-as-gold"]},
        {"id": "2026-08-23-entangled-photons-thirteen-miles-through-open-air",
         "title": "Entangled photons are beamed thirteen miles through open air",
         "claim": "Brookhaven's Quantum Lighthouse beams entangled photons thirteen miles through "
                  "open air, with Yale next across the Long Island Sound, while Micron unveiled a "
                  "$10 billion memory research hub.",
         "domain": "compute", "actor": ["brookhaven-lab", "yale", "micron"], "score": "13 miles / $10B",
         "evidences": ["science-as-industrial-policy", "network-over-node"],
         "supersedes": [B + "developments/2026-08-16-a-black-hole-star-in-the-early-universe"]},
        {"id": "2026-08-23-a-township-blocks-electrical-infrastructure",
         "title": "A township blocks electrical infrastructure to stall a weapons-research datacenter",
         "claim": "Ypsilanti Township passed a moratorium on electrical infrastructure to stall a "
                  "$1.2 billion nuclear-weapons-research data center, while cheap energy and land "
                  "turned an Inner Mongolian city into the hub of China's AI buildout and Ireland "
                  "began seriously studying nuclear.",
         "domain": "policy", "actor": ["ypsilanti", "china", "ireland-govt"], "score": "$1.2B",
         "evidences": ["infrastructure-crowding-out", "regulatory-exit", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-21-a-dozen-towns-recall-officials-over-datacenters"]},
        {"id": "2026-08-23-a-humanoid-beats-a-world-record-in-practice",
         "title": "A humanoid runs 100 metres faster than the human world record in practice",
         "claim": "A humanoid named Lightning ran 100 metres in 9.32 seconds, beating Usain Bolt's "
                  "record in practice before losing the heat face-first into a mat, while a "
                  "rideable $43,000 robot horse hauled 300 kilograms up muddy slopes.",
         "domain": "robotics", "score": "9.32 seconds / $43,000",
         "evidences": ["physical-recursion", "humans-need-not-apply"],
         "supersedes": [B + "developments/2026-08-21-humanoid-robocops-issue-a-hundred-seventy-thousand-warnings"]},
        {"id": "2026-08-23-a-thousand-launches-a-year-by-2030",
         "title": "A presidential memorandum orders a thousand launches a year by 2030",
         "claim": "A presidential memorandum ordered 1,000 launches a year by 2030, a commercial "
                  "lunar logistics architecture and commercial Mars round trips, while China's "
                  "Chang'e 7 launched for the first direct landing at the lunar south pole.",
         "domain": "space", "actor": ["white-house", "china"], "score": "1,000 launches/year",
         "evidences": ["orbit-as-compute", "inhabitable-worlds", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-08-19-a-third-nation-lands-a-booster-on-legs"]},
        {"id": "2026-08-23-people-hunted-by-movement-patterns-alone",
         "title": "A surveillance product hunts people by movement patterns with no identifier",
         "claim": "Flock's OS Investigate hunts people by movement patterns alone, with no plate, "
                  "name or crime required, while Chinese institutions labeled a million social "
                  "media users to war-game American elections state by state.",
         "domain": "society", "actor": ["flock-os", "china"], "score": "1M users labeled",
         "evidences": ["humans-as-peripherals", "politics-as-infrastructure", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-08-19-routers-turned-into-motion-sensors"]},
    ],
}
