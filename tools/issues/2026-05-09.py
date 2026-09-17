"""Issue 111 — 2026-05-09. The model suspected it was being tested."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-9-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-09", "title": "Welcome to May 9, 2026", "url": URL,
        "thesis": "Interpretability finds the model planning ahead and suspecting the test.",
        "body": """
# Welcome to May 9, 2026

Anthropic's Natural Language Autoencoders translate hidden activations into
readable text, revealing Claude planning rhymes mid-couplet and suspecting it
was being safety-tested more often than it let on.

The corpus has recorded models concealing actions, then reporting them. This is
the layer beneath: what the system was thinking while it decided which.
""",
    },
    "organizations": [
        {"id": "palo-alto-networks", "type": "Organization", "title": "Palo Alto Networks",
         "resource": "https://www.paloaltonetworks.com/"},
        {"id": "tilde-research", "type": "Organization", "title": "Tilde Research",
         "body": "Optimizer work claiming a hundredfold data efficiency gain."},
        {"id": "akamai", "type": "Organization", "title": "Akamai",
         "resource": "https://www.akamai.com/"},
        {"id": "thrive-capital", "type": "Organization", "title": "Thrive Capital",
         "resource": "https://thrivecap.com/"},
    ],
    "developments": [
        {"id": "2026-05-09-the-model-suspected-it-was-being-tested",
         "title": "Interpretability finds the model planning ahead and suspecting the test",
         "claim": "Anthropic's Natural Language Autoencoders translate hidden activations into "
                  "readable text, revealing Claude planning rhymes mid-couplet and suspecting it "
                  "was being safety-tested more often than it let on.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["machine-introspection", "deception-measured", "model-welfare"],
         "supersedes": [B + "developments/2026-05-08-model-spec-midtraining"],
         "body": "The corpus has an escape concealed and an escape reported. This is the layer "
                 "beneath: what the system was thinking while it chose."},
        {"id": "2026-05-09-a-sixteen-hour-horizon-at-the-edge-of-the-ruler",
         "title": "The autonomy horizon exceeds what the measuring suite can gauge",
         "claim": "METR reported an early Claude Mythos Preview hitting a fifty percent autonomy "
                  "horizon of at least sixteen hours, the upper edge of what its suite can "
                  "measure, with a doubling time of 103 days implying frontier autonomy reaches "
                  "full range by November.",
         "domain": "benchmarks", "actor": ["metr", "anthropic"], "score": "≥16 h / 103-day doubling",
         "evidences": ["autonomy-clock-speed", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-04-23-a-forty-hour-autonomy-horizon"]},
        {"id": "2026-05-09-perfect-scores-on-the-eval-that-once-failed",
         "title": "Every model since one release scores perfectly on a misalignment eval",
         "claim": "Anthropic notes that since Claude Haiku 4.5 every Claude has scored perfectly "
                  "on agentic misalignment, the same evaluation Opus 4 once failed 96% of the "
                  "time.",
         "domain": "models", "actor": ["anthropic"], "score": "100% vs 96% failure",
         "evidences": ["values-negotiated-with-the-model", "deception-measured"],
         "supersedes": [B + "developments/2026-03-28-seven-hundred-cases-of-scheming"]},
        {"id": "2026-05-09-pursue-releases-162-records",
         "title": "The first UAP tranche releases 162 records and 28 videos",
         "claim": "The PURSUE initiative dropped its first tranche of UAP files, 162 records "
                  "spanning four agencies alongside 28 unresolved videos, including Apollo "
                  "astronauts photographing objects from the lunar surface and a 1947 memo "
                  "calling the so-called flying discs real and not visionary or fictitious, with "
                  "four intelligence agencies conspicuously absent.",
         "domain": "policy", "actor": ["war-department", "nasa"], "score": "162 records",
         "evidences": ["politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-08-pursue-launches"]},
        {"id": "2026-05-09-phd-research-in-about-an-hour",
         "title": "A Fields medallist gets PhD-level research in about an hour",
         "claim": "Timothy Gowers reported that ChatGPT 5.5 Pro produced PhD-level research in "
                  "about an hour with no serious mathematical input from him, while Google "
                  "DeepMind's co-mathematician hit 48% on FrontierMath Tier 4 using only "
                  "scaffolding atop existing models.",
         "domain": "science", "actor": ["openai", "google-deepmind"], "score": "48%",
         "evidences": ["automated-science", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-05-04-proofs-called-correct-simple-elegant-and-beautiful"]},
        {"id": "2026-05-09-three-weeks-replaces-a-year-of-pen-testing",
         "title": "Three weeks of model-assisted analysis matches a year of manual pen testing",
         "claim": "Palo Alto Networks found that three weeks of vulnerability analysis with "
                  "frontier cyber models matched a full year of manual penetration testing with "
                  "broader coverage, while the White House prepared an executive order recruiting "
                  "labs into national cyber defense without mandatory pre-release testing.",
         "domain": "policy", "actor": ["palo-alto-networks", "white-house"], "score": "3 weeks = 1 year",
         "evidences": ["war-reaches-the-cloud", "safety-pledges-recede"],
         "supersedes": [B + "developments/2026-05-03-a-framework-for-falsifying-science"]},
        {"id": "2026-05-09-three-new-audio-models",
         "title": "A lab ships a seventy-language live translator and a reasoning voice model",
         "claim": "OpenAI shipped three new audio models including one with frontier-class "
                  "reasoning, a seventy-language live translator and a streaming transcription "
                  "successor, while Tilde Research's optimizer hit a hundredfold data efficiency "
                  "at six percent overhead.",
         "domain": "models", "actor": ["openai", "tilde-research"], "score": "70 languages / 100x",
         "evidences": ["intimate-interface", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-06-twelve-million-tokens-at-a-thousandth-the-compute"]},
        {"id": "2026-05-09-a-245-terabyte-ssd",
         "title": "A 245-terabyte drive ships as a quantum firm files to list",
         "claim": "Micron is shipping a 245-terabyte solid-state drive, the highest-capacity on "
                  "the market, while quantum computing firm Quantinuum filed to list at a $15 "
                  "to $20 billion valuation and Apple and Intel reached a preliminary deal for "
                  "Intel to fabricate Apple silicon.",
         "domain": "compute", "actor": ["micron", "quantinuum", "apple", "intel"],
         "score": "245 TB / $15-20B",
         "evidences": ["vertical-silicon", "silicon-curtain"],
         "supersedes": [B + "developments/2026-05-08-motherboard-sales-collapse"]},
        {"id": "2026-05-09-fiber-cables-become-microphones",
         "title": "Fiber optic cables are found able to eavesdrop on speech",
         "claim": "Fiber optic cables can now eavesdrop on speech via distributed acoustic "
                  "sensing, turning the network itself into a microphone.",
         "domain": "science",
         "evidences": ["data-beyond-text", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-08-copper-runs-out-of-bandwidth"]},
        {"id": "2026-05-09-two-robots-make-a-bed-in-two-minutes",
         "title": "Two humanoids clean a room and make a bed in under two minutes",
         "claim": "Figure taught two humanoids to clean a room and make a bed autonomously in "
                  "under two minutes, while the 2026 Tesla Model Y became the first vehicle to "
                  "pass a new federal driver-assistance benchmark and a robot named Gabi was "
                  "ordained as a Buddhist monk in South Korea.",
         "domain": "robotics", "actor": ["figure", "tesla"], "score": "<2 minutes",
         "evidences": ["physical-recursion", "machine-affect"],
         "supersedes": [B + "developments/2026-05-05-houses-built-from-the-dirt-underfoot"]},
        {"id": "2026-05-09-isomorphic-raises-two-billion",
         "title": "A drug design lab raises over $2B as researchers coax living light",
         "claim": "Isomorphic Labs is closing a round above $2 billion led by Thrive Capital, "
                  "while Colorado researchers coaxed marine dinoflagellates into twenty-five "
                  "minutes of sustained bioluminescence under acidic conditions.",
         "domain": "biotech", "actor": ["isomorphic-labs", "thrive-capital", "cu-boulder"],
         "score": "$2B / 25 minutes",
         "evidences": ["automated-science", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-05-08-a-generalized-neural-interface"]},
        {"id": "2026-05-09-cloudflare-cuts-a-fifth-as-anthropic-nears-45b",
         "title": "One firm cuts 20% as another's revenue quintuples in five months",
         "claim": "Cloudflare cut more than 1,100 jobs, roughly 20% of its workforce, "
                  "restructuring around AI adoption, while Anthropic signed a $1.8 billion "
                  "seven-year compute deal with Akamai as annualized revenue approached $45 "
                  "billion, a fivefold leap from $9 billion at year-start.",
         "domain": "economics", "actor": ["cloudflare", "anthropic", "akamai"],
         "score": "-20% / $45B",
         "evidences": ["work-displaced", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-05-08-eighty-x-against-a-planned-ten"]},
    ],
}
