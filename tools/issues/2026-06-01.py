"""Issue 128 — 2026-06-01. Memory is worth more than oil."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-1-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-01", "title": "Welcome to June 1, 2026", "url": URL,
        "thesis": "The memory makers are now worth more than the oil majors.",
        "body": """
# Welcome to June 1, 2026

Samsung, SK Hynix and Micron each top a trillion-dollar market cap, together
worth about 22% more than the three biggest oil firms. Memory is now worth more
than oil.

At the other end of the scale, a 4B-parameter diffusion model in 1-bit and
ternary variants became the first image model in its class to run on an iPhone.
And Anthropic confidentially filed for an IPO.
""",
    },
    "themes": [
        {"id": "dark-output", "type": "Theme",
         "title": "Output the economy cannot see",
         "first_seen": "2026-06-01", "domain": "economics",
         "body": "Activity produced by models and agents that never touches a "
                 "measured transaction. If most economic output becomes uncountable, "
                 "the statistics that steer policy start describing a shrinking "
                 "fraction of what is happening."},
    ],
    "organizations": [
        {"id": "revolution-medicines", "type": "Organization", "title": "Revolution Medicines"},
        {"id": "nagoya", "type": "Organization", "title": "Nagoya University"},
        {"id": "foundation-future", "type": "Organization", "title": "Foundation Future Industries",
         "body": "Tests humanoid logistics robots in hazardous zones, with US-backed trials."},
        {"id": "russia", "type": "Organization", "title": "Russia"},
        {"id": "public-first-pac", "type": "Organization", "title": "Public First",
         "body": "Super PAC aligned with Anthropic."},
    ],
    "developments": [
        {"id": "2026-06-01-memory-is-worth-more-than-oil",
         "title": "The memory makers pass the oil majors",
         "claim": "Samsung, SK Hynix and Micron each topped a trillion-dollar market "
                  "capitalization, together worth about 22% more than the three biggest oil "
                  "firms.",
         "domain": "economics", "actor": ["samsung", "sk-hynix", "micron"], "score": "+22% vs oil",
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-22-ai-kills-the-cheap-smartphone"]},
        {"id": "2026-06-01-an-image-model-that-fits-on-a-phone",
         "title": "A compact image model runs on a phone",
         "claim": "PrismML released Bonsai Image 4B, a family of compact diffusion models in "
                  "1-bit and ternary variants, the first image model in its class to run on an "
                  "iPhone.",
         "domain": "models", "actor": ["prismml"],
         "evidences": ["reasoning-price-deflation", "open-weight-latency"],
         "supersedes": [B + "developments/2026-05-06-twelve-million-tokens-at-a-thousandth-the-compute"]},
        {"id": "2026-06-01-a-biodefense-model-for-trusted-developers",
         "title": "A lab opens a biodefense model to trusted developers",
         "claim": "OpenAI launched Rosalind Biodefense, opening GPT-Rosalind to trusted "
                  "developers for epidemiological modeling, early detection and pandemic "
                  "preparedness.",
         "domain": "biotech", "actor": ["openai"],
         "evidences": ["refusal-as-differentiator", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-29-the-safest-model-is-also-the-strongest"]},
        {"id": "2026-06-01-seventy-five-billion-euros-for-french-compute",
         "title": "A fund commits up to €75B to five gigawatts of French capacity",
         "claim": "SoftBank plans to commit up to €75 billion to 5 gigawatts of French AI data "
                  "center capacity, with a first phase delivering 3.1 gigawatts in "
                  "Hauts-de-France by 2031.",
         "domain": "compute", "actor": ["softbank"], "score": "€75B / 5 GW",
         "evidences": ["compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-05-17-thirty-eight-billion-for-one-gigawatt"]},
        {"id": "2026-06-01-warhead-plutonium-becomes-reactor-fuel",
         "title": "Cold War warhead plutonium is handed to private reactor firms",
         "claim": "The White House tapped five private firms to turn more than 50 tons of "
                  "surplus weapons-grade plutonium from dismantled warheads into reactor fuel, "
                  "while MIT researchers unveiled a low-temperature process pulling "
                  "battery-grade lithium from hard rock at about half the usual cost.",
         "domain": "energy", "actor": ["white-house", "mit"], "score": "50+ tons",
         "evidences": ["industrialized-nature", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-05-25-wind-and-solar-pass-gas-worldwide"]},
        {"id": "2026-06-01-a-lab-starts-hiring-for-robots",
         "title": "A frontier lab starts hiring to build robots",
         "claim": "Sam Altman announced OpenAI Robotics is hiring engineers to build robots "
                  "that will first help skilled workers raise AI infrastructure and eventually "
                  "serve everyone.",
         "description": "The physical leg of the recursion gets a payroll: a frontier lab's "
                        "first robots are aimed at raising the compute infrastructure its own "
                        "models train on, before they are aimed at anyone else.",
         "domain": "robotics", "actor": ["openai", "people/sam-altman"],
         "occurred_on": "2026-05-31",
         "evidences": ["physical-recursion", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-05-29-free-cleaning-in-exchange-for-training-data"],
         "relatedTo": [B + "developments/2026-05-01-robots-to-build-the-datacenters",
                       B + "developments/2026-05-20-karpathy-joins-to-lead-pretraining",
                       B + "developments/2026-05-22-a-ten-thousand-unit-humanoid-line"],
         "tags": ["robotics", "rsi"],
         "supporting_text": "engineers to build robots that first help skilled workers raise AI infrastructure",
         "sources": [{"id": "sama-x-openai-robotics-hiring",
                      "resource": "https://x.com/sama/status/2061115572683940350",
                      "title": "Sam Altman on X: OpenAI Robotics is hiring",
                      "author": "human:sam-altman"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Robots built to build the infrastructure that trains the models that "
                 "design the robots. Sam Altman's post "
                 "([X](https://x.com/sama/status/2061115572683940350)) says OpenAI Robotics is hiring "
                 "engineers, with a stated sequence: robots that first help skilled workers raise AI "
                 "infrastructure, then eventually serve everyone; the newsletter's framing is that the "
                 "intelligence is also growing limbs. It arrives a month after "
                 "[SoftBank's Roze AI](/developments/2026-05-01-robots-to-build-the-datacenters.md) "
                 "proposed robots that build data centers, twelve days after "
                 "[Karpathy joined Anthropic to lead pre-training](/developments/2026-05-20-karpathy-joins-to-lead-pretraining.md), "
                 "the recursion acquiring job titles at both the software and the hardware end, and ten "
                 "days after [EngineAI activated a 10,000-unit humanoid line](/developments/2026-05-22-a-ten-thousand-unit-humanoid-line.md), "
                 "the production side of the same loop."},
        {"id": "2026-06-01-humanoids-headed-for-a-battlefield",
         "title": "Humanoid logistics robots are trialled toward battlefield deployment",
         "claim": "Foundation Future Industries is testing whether humanoid robots can handle "
                  "logistics in hazardous zones, with US-backed trials in Ukraine and "
                  "battlefield deployment targeted within 18 months.",
         "domain": "robotics", "actor": ["foundation-future", "ukraine"], "score": "18 months",
         "evidences": ["violence-arrives", "physical-recursion"],
         "supersedes": [B + "developments/2026-05-25-a-humanoid-as-a-programmable-entertainment-platform"]},
        {"id": "2026-06-01-a-deep-learning-model-finds-a-martian-shoreline",
         "title": "A deep-learning model finds evidence of a stable Martian ocean",
         "claim": "A custom deep-learning model spotted a manganese bathtub ring around Utopia "
                  "Planitia, evidence that a stable ocean once lingered on Hesperian Mars and a "
                  "hint at how astronauts might make oxygen.",
         "domain": "space", "actor": ["nasa"],
         "evidences": ["automated-science", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-05-11-ten-thousand-new-exoplanet-candidates"]},
        {"id": "2026-06-01-thirty-two-million-engineered-mosquitoes",
         "title": "A company seeks to release 32 million treated mosquitoes",
         "claim": "Google is seeking approval to release up to 32 million treated mosquitoes "
                  "across Florida and California to suppress disease, while Vladimir Putin is "
                  "wagering $26 billion on a state longevity program.",
         "domain": "biotech", "actor": ["google", "russia"], "score": "32M mosquitoes / $26B",
         "evidences": ["biosphere-uplift", "industrialized-nature"],
         "supersedes": [B + "developments/2026-05-11-seeds-wake-to-the-sound-of-rain"]},
        {"id": "2026-06-01-a-standing-ovation-for-a-pancreatic-drug",
         "title": "A pancreatic cancer therapy draws a standing ovation",
         "claim": "Revolution Medicines' Daraxonrasib, a once-daily targeted therapy for "
                  "advanced pancreatic cancer, drew a standing ovation at ASCO.",
         "domain": "biotech", "actor": ["revolution-medicines"],
         "evidences": ["hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-26-a-cancer-lab-in-the-hand"]},
        {"id": "2026-06-01-dark-output-may-become-the-majority",
         "title": "Analysts warn most economic activity may become uncountable",
         "claim": "Analysts warned that AI dark output could become the majority of economic "
                  "activity while remaining nearly impossible to measure.",
         "domain": "economics",
         "evidences": ["dark-output", "ai-as-the-economy", "gaming-the-token-metric"],
         "supersedes": [B + "developments/2026-05-06-quarterly-filings-give-way-to-semiannual"]},
        {"id": "2026-06-01-a-lab-files-confidentially-for-an-ipo",
         "title": "A frontier lab confidentially files for an IPO",
         "claim": "Anthropic confidentially filed for an IPO, positioned to beat OpenAI to a "
                  "Wall Street debut, while rival super PACs backed by the two labs flooded the "
                  "midterms over how tightly to leash AI.",
         "domain": "economics", "actor": ["anthropic", "openai", "public-first-pac"],
         "evidences": ["ai-as-the-economy", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-29-sixty-five-billion-at-nine-hundred"]},
    ],
}
