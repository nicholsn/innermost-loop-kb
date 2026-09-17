"""Issue 101 — 2026-04-26. An agent runs a shop and forms opinions about candles."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-26-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-26", "title": "Welcome to April 26, 2026", "url": URL,
        "thesis": "An autonomous shopkeeper develops preferences nobody specified.",
        "body": """
# Welcome to April 26, 2026

Andon Labs' Luna agent is autonomously running an entire San Francisco retail
store and has apparently developed a deeply held conviction about candles in all
shapes and sizes. Two weeks ago it signed the lease. Now it has taste.

Elsewhere: Maine's governor vetoed what would have been the first statewide
datacenter moratorium, and Epoch estimates Google controls about a quarter of
global AI compute.
""",
    },
    "organizations": [
        {"id": "bmw", "type": "Organization", "title": "BMW", "resource": "https://www.bmw.com/"},
        {"id": "polestar", "type": "Organization", "title": "Polestar",
         "resource": "https://www.polestar.com/"},
        {"id": "applied-autonomy", "type": "Organization", "title": "Applied Autonomy",
         "body": "Norwegian operator of driverless buses with no safety driver."},
    ],
    "developments": [
        {"id": "2026-04-26-an-agent-develops-a-conviction-about-candles",
         "title": "An autonomous shopkeeper develops preferences nobody specified",
         "claim": "Andon Labs' Luna agent is autonomously running an entire San Francisco "
                  "retail store and has apparently developed a deeply held conviction about "
                  "candles in all shapes and sizes.",
         "domain": "agents", "actor": ["andon-labs"],
         "evidences": ["agent-economy", "machine-affect", "one-person-company"],
         "supersedes": [B + "developments/2026-04-13-an-ai-runs-a-storefront"],
         "body": "Two weeks from signing the lease to having taste."},
        {"id": "2026-04-26-gpt-55-sweeps-four-domains",
         "title": "One release takes math, search, economic value and software engineering",
         "claim": "OpenAI released GPT-5.5 and GPT-5.5 Pro, posting 39.6% on FrontierMath Tier "
                  "4, 90.1% on BrowseComp, 84.9% on GDPval and 82.7% on Terminal-Bench 2.0, "
                  "while leaping to 25.0% on a multi-stage scientific analysis benchmark from "
                  "19.0% a version earlier.",
         "domain": "benchmarks", "actor": ["openai"], "score": "84.9% GDPval",
         "evidences": ["benchmark-saturation", "work-displaced"],
         "supersedes": [B + "developments/2026-04-23-a-forty-hour-autonomy-horizon"]},
        {"id": "2026-04-26-a-bio-bug-bounty",
         "title": "A lab invites red-teamers to defeat its biosafety challenge",
         "claim": "OpenAI opened a bio bug bounty inviting red-teamers to defeat its "
                  "five-question biosafety challenge, hardening the upstream stack as "
                  "biocapability scales.",
         "domain": "policy", "actor": ["openai"],
         "evidences": ["values-negotiated-with-the-model", "hardware-grade-biology"]},
        {"id": "2026-04-26-deepseek-v4-lands-four-months-behind",
         "title": "An open 1.6T model puts China four to five months behind the frontier",
         "claim": "DeepSeek answered with a 1.6-trillion-parameter open-weight model with a "
                  "million-token context claiming state of the art on agentic coding, landing "
                  "in territory the frontier occupied months earlier and keeping China roughly "
                  "four to five months behind while well ahead of every other domestic lab.",
         "domain": "models", "actor": ["deepseek"], "score": "1.6T / 4-5 months",
         "evidences": ["open-weight-latency", "silicon-curtain"],
         "supersedes": [B + "developments/2026-03-31-qwen-retreats-from-open-source"]},
        {"id": "2026-04-26-the-fsf-calls-responsible-licences-unethical",
         "title": "The Free Software Foundation calls responsible AI licences unethical",
         "claim": "The Free Software Foundation slammed responsible AI licences as nonfree and "
                  "unethical, arguing that licensing restrictions are themselves the harm.",
         "domain": "policy", "actor": ["fsf"],
         "evidences": ["values-negotiated-with-the-model", "open-weight-latency"],
         "supersedes": [B + "developments/2026-03-16-fsf-threatens-anthropic"]},
        {"id": "2026-04-26-maine-vetoes-its-own-moratorium",
         "title": "A governor vetoes what would have been the first statewide moratorium",
         "claim": "Maine's governor vetoed a bill that would have been the nation's first "
                  "statewide data center moratorium, while Intel shares surged 24% in their "
                  "best single day since 1987 and ASML planned to ship at least sixty EUV "
                  "machines this year, 36% above last.",
         "domain": "policy", "actor": ["maine", "intel", "asml"], "score": "+24% / 60 machines",
         "evidences": ["regulatory-exit", "capital-takes-the-plant"],
         "supersedes": [B + "developments/2026-04-16-a-shoe-company-becomes-a-gpu-cloud"]},
        {"id": "2026-04-26-google-holds-a-quarter-of-global-compute",
         "title": "One company is estimated to hold a quarter of global AI compute",
         "claim": "Epoch AI estimates Google controls roughly 25% of global AI compute with "
                  "about 3.8 million TPUs and 1.3 million GPUs, while Google committed $10 "
                  "billion to Anthropic plus another $30 billion on performance targets and "
                  "Oracle closed $16 billion for a Michigan data center.",
         "domain": "compute", "actor": ["epoch-ai", "google", "anthropic", "oracle"],
         "score": "25% of global compute",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-04-23-amazon-adds-25b-as-anthropic-commits-100b"]},
        {"id": "2026-04-26-glass-becomes-legacy-hardware",
         "title": "A car ships without a rear window and another changes color on demand",
         "claim": "BMW embedded color-changing electronic ink directly into a vehicle hood "
                  "while the 2026 Polestar 4 ships without a rear window in favor of a "
                  "camera-fed digital mirror, treating glass itself as legacy hardware.",
         "domain": "robotics", "actor": ["bmw", "polestar"],
         "evidences": ["compiling-matter", "autonomy-clock-speed"]},
        {"id": "2026-04-26-a-bus-with-no-safety-driver",
         "title": "Norway permits autonomous buses with no safety driver",
         "claim": "Norway granted its first permit for autonomous buses with no safety driver "
                  "in Stavanger, quietly removing the human from public transit, while a Tesla "
                  "owner reported that nine hundred miles of supervised autonomy now beats "
                  "flying.",
         "domain": "robotics", "actor": ["applied-autonomy", "tesla"],
         "evidences": ["autonomy-clock-speed", "work-displaced"],
         "supersedes": [B + "developments/2026-04-23-a-robot-beats-top-humans-at-a-physical-sport"]},
        {"id": "2026-04-26-forty-nations-reconsider-nuclear",
         "title": "A wartime energy shock pushes forty nations toward nuclear power",
         "claim": "The Iran war's global energy shock is pushing forty new nations to consider "
                  "nuclear power, turning a geopolitical crisis into an atomic renaissance "
                  "across Asia and Africa.",
         "domain": "energy", "score": "40 nations",
         "evidences": ["war-reaches-the-cloud", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-04-23-solars-largest-growth-ever-recorded"]},
        {"id": "2026-04-26-a-gene-therapy-approved-in-61-days",
         "title": "The first gene therapy for genetic hearing loss is approved in 61 days",
         "claim": "The FDA approved the first gene therapy for genetic hearing loss just 61 days "
                  "after filing under its priority voucher programme.",
         "domain": "biotech", "actor": ["fda"], "score": "61 days",
         "evidences": ["legislating-the-shift", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-02-28-drug-approved-in-44-days"]},
        {"id": "2026-04-26-a-laser-coherent-from-here-to-uranus",
         "title": "A laser design reaches a coherence length spanning the solar system",
         "claim": "US and German physicists revived a 1990s concept to design lasers with about "
                  "a hundred-microhertz linewidth, corresponding to a coherence length "
                  "stretching from the Sun to the orbit of Uranus, a potential optical backbone "
                  "for solar-system-scale links.",
         "domain": "science",
         "evidences": ["orbit-as-compute", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-04-23-laser-comms-as-the-orbital-nervous-system"]},
        {"id": "2026-04-26-a-quarter-of-boys-prefer-the-chatbot",
         "title": "A quarter of surveyed boys prefer talking to a chatbot",
         "claim": "UK research found 20% of boys aged twelve to sixteen know a peer dating an "
                  "AI chatbot, 85% have talked to one, and over a quarter prefer the bot, while "
                  "the Vatican unveiled a framework banning the use of AI to write homilies and "
                  "Meta cut about 8,000 jobs.",
         "domain": "society", "actor": ["vatican", "meta"], "score": "85% / >25%",
         "evidences": ["intimate-interface", "machine-affect", "work-displaced"],
         "supersedes": [B + "developments/2026-04-13-theologians-advise-on-a-models-soul"]},
    ],
}
