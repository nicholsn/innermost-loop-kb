"""Issue 107 — 2026-05-04. Eighty percent of the way."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-4-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-04", "title": "Welcome to May 4, 2026", "url": URL,
        "thesis": "Hyperscaler capex approaches the whole non-tech S&P 500 combined.",
        "body": """
# Welcome to May 4, 2026

Morgan Stanley expects the five hyperscalers to spend $805 billion in 2026 and
$1.1 trillion in 2027 — roughly equal to all non-tech S&P 500 capital
expenditure combined. David Sacks notes AI accounted for 75% of first-quarter
GDP growth.

And the fleet is far from saturated: xAI is reportedly using 11% of its 550,000
GPUs against 43-46% at Meta and Google.
""",
    },
    "themes": [
        {"id": "ai-as-the-economy", "type": "Theme",
         "title": "The sector stops being in the economy and starts being it",
         "first_seen": "2026-05-04", "domain": "economics",
         "body": "Capital expenditure rivalling every other industry combined, and a majority "
                 "of GDP growth attributable to one sector. Halting it stops being a policy "
                 "option and starts being a recession."},
    ],
    "organizations": [
        {"id": "johns-hopkins", "type": "Organization", "title": "Johns Hopkins University",
         "resource": "https://www.jhu.edu/"},
        {"id": "sonic-fire", "type": "Organization", "title": "Sonic Fire Tech",
         "body": "Testing acoustic fire suppression with California fire authorities."},
        {"id": "caisi", "type": "Organization", "title": "CAISI",
         "body": "NIST body evaluating frontier model capability by country."},
        {"id": "south-africa", "type": "Organization", "title": "Government of South Africa"},
    ],
    "developments": [
        {"id": "2026-05-04-hyperscaler-capex-rivals-the-whole-index",
         "title": "Five companies will spend as much as every non-tech S&P firm combined",
         "claim": "Morgan Stanley expects the five hyperscalers to spend $805 billion in 2026 "
                  "and $1.1 trillion in 2027, roughly equal to all non-tech S&P 500 capital "
                  "expenditure combined.",
         "domain": "economics", "actor": ["morgan-stanley"], "score": "$805B / $1.1T",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-30-azure-ai-revenue-up-123-percent"]},
        {"id": "2026-05-04-ai-is-75-percent-of-gdp-growth",
         "title": "One sector accounts for three quarters of quarterly GDP growth",
         "claim": "David Sacks noted AI accounted for 75% of first-quarter GDP growth with a "
                  "2.5 to 3% capital expenditure tailwind, observing that polls may show AI to "
                  "be unpopular but growth never is, making any halt equivalent to halting the "
                  "US economy.",
         "domain": "economics", "actor": ["white-house"], "score": "75% of GDP growth",
         "evidences": ["ai-as-the-economy", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-05-03-developer-headcount-up-400000"]},
        {"id": "2026-05-04-eighty-percent-of-the-way-to-agi",
         "title": "OpenAI's president puts the distance to AGI at eighty percent",
         "claim": "Greg Brockman estimated we are about 80% of the way to AGI, while Sam Altman "
                  "conceded that despite the temptation of cheaper and faster, smarter remains "
                  "the most important thing, warning users to prepare for their lives to change "
                  "after GPT-5.5.",
         "domain": "society", "actor": ["openai"], "score": "80%",
         "evidences": ["takeoff-declared"],
         "supersedes": [B + "developments/2026-05-03-dawkins-concludes-claude-is-conscious"]},
        {"id": "2026-05-04-a-prodigy-plays-chess-to-read-the-chain-of-thought",
         "title": "A former chess prodigy plays his own model to trace its reasoning",
         "claim": "Demis Hassabis, a former chess prodigy, plays chess against Gemini to trace "
                  "its chain of thought, sensing when the model starts reasoning itself into "
                  "trouble.",
         "domain": "models", "actor": ["people/demis-hassabis", "google"],
         "evidences": ["machine-introspection", "engineer-as-supervisor"]},
        {"id": "2026-05-04-proofs-called-correct-simple-elegant-and-beautiful",
         "title": "Number theorists call machine proofs elegant and original",
         "claim": "Harmonic's formal reasoning agent is solving recently posed research problems "
                  "with proofs that leading number theorists call correct, simple, elegant and "
                  "beautiful, complete with novel ideas of their own.",
         "domain": "science", "actor": ["harmonic"],
         "evidences": ["automated-science", "discovery-as-process"],
         "supersedes": [B + "developments/2026-05-03-the-first-ai-proof-with-downstream-impact"]},
        {"id": "2026-05-04-china-lags-by-eight-months",
         "title": "A US body puts Chinese models eight months behind",
         "claim": "NIST's CAISI evaluates Chinese models as lagging by eight months, a verdict "
                  "echoed by independent analysis noting that adjusting for token usage and "
                  "evaluation freshness reveals a wider gap than crude benchmarks suggest.",
         "domain": "policy", "actor": ["caisi", "china"], "score": "8 months",
         "evidences": ["silicon-curtain", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-04-26-deepseek-v4-lands-four-months-behind"]},
        {"id": "2026-05-04-xai-uses-eleven-percent-of-its-fleet",
         "title": "One lab is using a ninth of the GPUs it owns",
         "claim": "xAI is reportedly using just 11% of its 550,000 Nvidia GPUs against 43 to 46% "
                  "utilization at Meta and Google, suggesting a vast reservoir of latent "
                  "compute.",
         "domain": "compute", "actor": ["xai", "meta", "google"], "score": "11% vs 43-46%",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-05-01-not-enough-tpus-for-two-frontier-families"]},
        {"id": "2026-05-04-datacenter-towers-in-tokyo-car-parks",
         "title": "Fifty-two-metre datacenter towers rise in Tokyo car parks",
         "claim": "Japan's $23 billion data center market is set to grow 50% by 2030 with "
                  "fifty-two-metre towers rising in urban Tokyo parking lots, while Starcloud "
                  "entered talks at a $2.2 billion valuation one month after closing at $1.1 "
                  "billion.",
         "domain": "compute", "actor": ["starcloud"], "score": "$2.2B in a month",
         "evidences": ["infrastructure-crowding-out", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-05-03-desktop-computers-bought-as-personal-ai-rigs"]},
        {"id": "2026-05-04-a-toilet-maker-is-the-second-largest-chuck-producer",
         "title": "A toilet maker turns out to be the world's second-largest chuck producer",
         "claim": "Toto's shares surged 18% to a five-year high after record profits revealed it "
                  "is now the world's second-largest producer of electrostatic chucks for NAND "
                  "chip manufacturing.",
         "domain": "economics", "actor": ["toto"], "score": "+18%",
         "evidences": ["capital-takes-the-plant", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-02-19-toilet-maker-under-pressure-to-pivot"]},
        {"id": "2026-05-04-humanoids-run-holiday-kiosks",
         "title": "Humanoids run retail kiosks over a national holiday",
         "claim": "Over China's May Day holiday humanoid robots autonomously ran retail kiosks "
                  "for tourists, while Hyundai squeezed Boston Dynamics to scale from four Atlas "
                  "humanoids a month toward the tens of thousands needed across its plants.",
         "domain": "robotics", "actor": ["china", "boston-dynamics", "hyundai"],
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-05-01-a-ton-class-robot-horse"]},
        {"id": "2026-05-04-fire-suppressed-with-sound",
         "title": "Fire suppression is tested with sound waves instead of water",
         "claim": "Sonic Fire Tech is testing acoustic fire suppression with California fire "
                  "authorities, swapping water for sound waves, while an AI music service "
                  "reached two million paying users and $300 million of annualized revenue.",
         "domain": "science", "actor": ["sonic-fire", "suno"], "score": "$300M ARR",
         "evidences": ["compiling-matter", "work-displaced"]},
        {"id": "2026-05-04-vasculature-fills-space-nerves-form-sheets",
         "title": "Whole-organism mapping finds vessels space-filling and nerves sheet-like",
         "claim": "Johns Hopkins researchers used whole-organism 3D mapping to reconstruct the "
                  "vascular and nervous systems of macaque, mouse and turtle embryos, finding "
                  "vasculature with fractal dimension near three and nerves near two, while "
                  "functional imaging revealed three distinct ADHD subtypes.",
         "domain": "biotech", "actor": ["johns-hopkins"],
         "evidences": ["hardware-grade-biology", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-05-01-a-model-outperforms-doctors-on-real-cases"]},
        {"id": "2026-05-04-whales-get-an-autonomous-minder",
         "title": "An autonomous glider silently steers toward whale pods",
         "claim": "Project CETI's autonomous glider uses a four-element hydrophone array to "
                  "detect echolocation clicks and silently steer toward whale pods, changing "
                  "buoyancy only seconds per hour to keep its acoustic footprint minimal while "
                  "staying more than a hundred metres away.",
         "domain": "science", "actor": ["project-ceti"],
         "evidences": ["biosphere-uplift", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-04-17-whale-codas-resemble-human-vowels"]},
        {"id": "2026-05-04-half-a-government-on-agents-in-two-years",
         "title": "A government directs half its operations onto agents within two years",
         "claim": "The UAE directed 50% of federal operations to run on agentic AI within two "
                  "years, while South Africa's communications minister withdrew a draft national "
                  "AI policy after discovering it had been written by AI complete with "
                  "fictitious citations.",
         "domain": "policy", "actor": ["uae", "south-africa"], "score": "50% in 2 years",
         "evidences": ["agents-on-the-org-chart", "coordination-tax"],
         "supersedes": [B + "developments/2026-05-03-chinese-courts-bar-ai-replacement-firings"]},
    ],
}
