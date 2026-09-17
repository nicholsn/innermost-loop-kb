"""Issue 102 — 2026-04-27. A model lives 49 days."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-27-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-27", "title": "Welcome to April 27, 2026", "url": URL,
        "thesis": "Frontier models start living shorter lives than the problems they solve.",
        "body": """
# Welcome to April 27, 2026

GPT-4o ran for 21 months. GPT-5.4 lasted 49 days. A mayfly schedule for
synthetic minds — and the corpus has been recording retirement interviews for
models deprecated on this cadence.

Also here: a 23-year-old with no advanced mathematical training cracked an Erdős
problem with a single prompt, prompting Tao to note that humans hit a mental
block from a slight wrong turn at move one.
""",
    },
    "themes": [
        {"id": "risk-becomes-uninsurable", "type": "Theme",
         "title": "Insurers withdraw from what the technology now does",
         "first_seen": "2026-04-27", "domain": "economics",
         "body": "When carriers exclude AI-related damages from corporate policies, the losses "
                 "stop being priced and start being absorbed. Uninsurability is the market's "
                 "way of saying the tail is unknown."},
    ],
    "organizations": [
        {"id": "x-energy", "type": "Organization", "title": "X-energy",
         "body": "Nuclear startup that raised $1B in an IPO."},
        {"id": "berkshire", "type": "Organization", "title": "Berkshire Hathaway",
         "resource": "https://www.berkshirehathaway.com/"},
        {"id": "varda", "type": "Organization", "title": "Varda",
         "resource": "https://www.varda.com/"},
        {"id": "state-grid", "type": "Organization", "title": "State Grid Corporation of China",
         "body": "Deploying 500 humanoid robots for high-voltage operations."},
    ],
    "developments": [
        {"id": "2026-04-27-a-model-lives-forty-nine-days",
         "title": "A frontier model's service life falls from 21 months to 49 days",
         "claim": "GPT-4o ran for 21 months while GPT-5.4 lasted only 49 days, a mayfly "
                  "schedule for frontier models.",
         "domain": "models", "actor": ["openai"], "score": "21 months → 49 days",
         "evidences": ["model-welfare", "spiky-frontier"],
         "supersedes": [B + "developments/2026-04-26-gpt-55-sweeps-four-domains"],
         "body": "The corpus has recorded a retirement interview for a deprecated model. This "
                 "is the cadence those retirements now run on."},
        {"id": "2026-04-27-a-23-year-old-cracks-an-erdos-problem-in-one-prompt",
         "title": "A 23-year-old with no advanced training solves an Erdős problem in one prompt",
         "claim": "Liam Price, a 23-year-old with no advanced mathematical training, used a "
                  "single GPT-5.4 Pro prompt to crack an Erdős problem that had eluded "
                  "prominent minds, prompting Terry Tao to observe that humans hit a mental "
                  "block from making a slight wrong turn at move one.",
         "domain": "science", "actor": ["openai", "people/terry-tao"],
         "evidences": ["automated-science", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-04-16-a-proof-from-the-book"]},
        {"id": "2026-04-27-bostrom-on-the-long-human-level-era",
         "title": "Bostrom says the surprise is how long the human-level era has lasted",
         "claim": "Nick Bostrom said what surprised him most is this extended era of roughly "
                  "human-level AI, which has already stretched three to five years and may "
                  "stretch further, while Demis Hassabis moved from saying AGI needed one or "
                  "two more breakthroughs to calling it a coin flip whether any are needed.",
         "domain": "society", "actor": ["people/demis-hassabis"],
         "evidences": ["takeoff-declared"],
         "supersedes": [B + "developments/2026-04-20-agi-becomes-a-version-number"]},
        {"id": "2026-04-27-the-prize-is-the-kitchen-not-the-recipe",
         "title": "Weights matter less than the inference compute to run them",
         "claim": "OpenAI's Noam Brown noted that model weights now matter relatively less than "
                  "securing inference compute, while Sam Altman mocked the gap between "
                  "predictions that nobody would work after AGI and users adopting polyphasic "
                  "sleep to ship more code.",
         "domain": "economics", "actor": ["openai"],
         "evidences": ["compute-capital-stack", "cognitive-load-inverted"],
         "supersedes": [B + "developments/2026-04-23-two-labs-reach-a-tenth-of-a-percent-of-gdp"]},
        {"id": "2026-04-27-openai-designs-phone-silicon",
         "title": "A model lab starts designing smartphone processors",
         "claim": "OpenAI is reportedly working with MediaTek and Qualcomm on AI smartphone "
                  "processors with mass production targeted for 2028, while Apple has six "
                  "product categories in the pipeline including camera-bearing wearables, "
                  "displays and tabletop robots.",
         "domain": "compute", "actor": ["openai", "mediatek", "qualcomm", "apple"],
         "evidences": ["silicon-designs-itself", "intimate-interface"],
         "supersedes": [B + "developments/2026-04-20-intel-erases-the-dot-com-crash"]},
        {"id": "2026-04-27-we-have-never-retired-old-a100s",
         "title": "Demand is so high that no generation of chips has been retired",
         "claim": "The AWS chief executive said demand is so excessive that the company has "
                  "never retired old A100s, marking a post-obsolescence era for silicon, while "
                  "a planned Utah data center would generate its own power, clean its own water "
                  "and consume more electricity than the entire state.",
         "domain": "compute", "actor": ["amazon"],
         "evidences": ["infrastructure-crowding-out", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-26-google-holds-a-quarter-of-global-compute"]},
        {"id": "2026-04-27-five-hundred-humanoids-on-high-voltage-work",
         "title": "China's grid deploys 500 humanoids to high-voltage work",
         "claim": "China's State Grid is deploying 500 humanoid robots for high-voltage "
                  "operations, where the optimal failure mode becomes a melted servo rather than "
                  "a melted operator, while fifteen chemical-spraying drones were stolen in New "
                  "Jersey with the FBI investigating.",
         "domain": "robotics", "actor": ["state-grid"], "score": "500 robots / 15 drones",
         "evidences": ["physical-recursion", "violence-arrives"],
         "supersedes": [B + "developments/2026-04-26-a-bus-with-no-safety-driver"],
         "body": "Deployment surface and attack surface expanding at the same rate."},
        {"id": "2026-04-27-space-solar-beamed-to-datacenters",
         "title": "Meta signs for a gigawatt of power beamed from orbit",
         "claim": "Meta signed for up to a gigawatt of space solar beamed from satellites to "
                  "data centers below, while nuclear startup X-energy raised $1 billion in a "
                  "listing that popped 25% and a geothermal startup filed at roughly $3 billion.",
         "domain": "energy", "actor": ["meta", "overview-energy", "x-energy", "fervo-energy"],
         "score": "1 GW",
         "evidences": ["orbit-as-compute", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-04-26-forty-nations-reconsider-nuclear"]},
        {"id": "2026-04-27-a-hundred-terawatts-of-compute-from-space",
         "title": "A pay package is tied to delivering 100 terawatts of compute from space",
         "claim": "SpaceX approved a plan granting Elon Musk sixty million additional shares if "
                  "its market capitalization climbs from $1.1 to $6.6 trillion while delivering "
                  "a hundred terawatts of compute per year from space data centers, orders of "
                  "magnitude beyond peak US power consumption.",
         "domain": "space", "actor": ["spacex"], "score": "100 TW/yr",
         "evidences": ["orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-26-a-laser-coherent-from-here-to-uranus"]},
        {"id": "2026-04-27-first-phase-3-success-for-in-vivo-crispr",
         "title": "In vivo CRISPR posts its first Phase 3 success",
         "claim": "Intellia Therapeutics announced the first Phase 3 success for an in vivo "
                  "CRISPR treatment that edits a disease-causing gene, while runners broke the "
                  "sub-two-hour marathon barrier in London in next-generation shoes.",
         "domain": "biotech", "score": "Phase 3",
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-04-26-a-gene-therapy-approved-in-61-days"]},
        {"id": "2026-04-27-glp1s-outearn-the-frontier-labs",
         "title": "Two weight-loss drugs outearn the two leading AI labs combined",
         "claim": "Ozempic and Mounjaro outearned OpenAI and Anthropic combined in 2025, making "
                  "longevity a heavyweight rival to AI itself.",
         "domain": "economics",
         "evidences": ["hardware-grade-biology", "compute-capital-stack"]},
        {"id": "2026-04-27-insurers-drop-ai-damages",
         "title": "Major insurers win approval to exclude AI damages from corporate policies",
         "claim": "Major insurers including Berkshire Hathaway, Chubb and Travelers won "
                  "approval to drop AI-related damages from corporate policies, excluding claims "
                  "such as agents misusing copyrighted material in marketing.",
         "domain": "economics", "actor": ["berkshire"],
         "evidences": ["risk-becomes-uninsurable", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-04-05-eight-hundred-sanctions-for-hallucinated-briefs"],
         "body": "The market declining to price a tail it cannot estimate."},
        {"id": "2026-04-27-an-ai-in-the-sp500-in-five-years",
         "title": "A founder predicts an AI-led public company within five years",
         "claim": "Varda's Andrew McCalip predicted an AI-led S&P 500 company within five years "
                  "and an AI elected official within twenty, while the Supreme Court prepared to "
                  "decide whether geofence warrants violate the Fourth Amendment and US "
                  "bookstores grew 70% in six years.",
         "domain": "society", "actor": ["varda", "supreme-court"],
         "evidences": ["agent-economy", "legislating-the-shift"]},
    ],
}
