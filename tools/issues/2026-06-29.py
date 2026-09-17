"""Issue 151 — 2026-06-29. The open-source Claude moment."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-29-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-29", "title": "Welcome to June 29, 2026", "url": URL,
        "thesis": "Owning your own weights becomes the thing worth owning.",
        "body": """
# Welcome to June 29, 2026

GLM-5.2 is being hailed as the open-source Claude moment, with demand so fierce
that companies rush to post-train and own their own weights. Ethan Mollick's
consulting benchmark shows only a three-month lag between American and Chinese
open models.

Meanwhile renting is now cheaper than owning in every big metro, and even
millionaires rent — in an age when the asset everyone races to own is a set of
model weights.
""",
    },
    "themes": [
        {"id": "own-your-own-weights", "type": "Theme",
         "title": "Weights become the asset worth owning",
         "first_seen": "2026-06-29", "domain": "economics",
         "body": "Once open models are close enough to the frontier, the strategic "
                 "move stops being buying access and becomes post-training your own "
                 "copy. Ownership migrates from real estate and equipment to a file "
                 "of parameters nobody can revoke."},
    ],
    "organizations": [
        {"id": "firmus", "type": "Organization", "title": "Firmus"},
        {"id": "deloitte", "type": "Organization", "title": "Deloitte"},
        {"id": "tidal", "type": "Organization", "title": "Tidal"},
        {"id": "iridium", "type": "Organization", "title": "Iridium Communications"},
        {"id": "austria", "type": "Organization", "title": "Austria"},
    ],
    "developments": [
        {"id": "2026-06-29-the-open-source-claude-moment",
         "title": "Companies rush to post-train and own their own weights",
         "claim": "GLM-5.2 is being hailed as the open-source Claude moment, with demand so "
                  "fierce that companies rush to post-train and own their own weights, while "
                  "Ethan Mollick's consulting-style benchmark showed only a three-month lag "
                  "between American and Chinese open models.",
         "domain": "models", "actor": ["zai"], "score": "3-month lag",
         "evidences": ["own-your-own-weights", "open-weight-latency", "frontier-moves-backward"],
         "supersedes": [B + "developments/2026-06-28-a-trillion-six-parameter-open-model"]},
        {"id": "2026-06-29-a-company-caps-rival-tools-to-protect-its-training-data",
         "title": "A company caps rival AI tools to keep their output out of its training data",
         "claim": "Meta, fearing Claude Code and Codex output could seep into its own training "
                  "data and trigger escalations, is reportedly capping engineers' use of both as "
                  "it builds MetaCode.",
         "domain": "models", "actor": ["meta", "anthropic", "openai"],
         "evidences": ["dark-forest-research", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-06-25-the-largest-known-distillation-attack"]},
        {"id": "2026-06-29-open-models-behind-the-airlock",
         "title": "Open models are packaged to run in air-gapped classified environments",
         "claim": "Palantir and NVIDIA are shipping an engine to run Nemotron open models in "
                  "air-gapped, classified environments so agencies can adapt them behind the "
                  "airlock while keeping data, intellectual property and weights in-house.",
         "domain": "policy", "actor": ["palantir", "nvidia"],
         "evidences": ["own-your-own-weights", "clearance-as-bottleneck", "regulatory-exit"],
         "supersedes": [B + "developments/2026-06-29-the-open-source-claude-moment"]},
        {"id": "2026-06-29-a-country-lobbies-to-host-a-lab-physically",
         "title": "A country lobbies the EU to physically host a foreign lab inside the bloc",
         "claim": "Austria is lobbying the EU to physically host Anthropic inside the bloc after "
                  "a US directive cut foreigners off from its best models, even as California's "
                  "governor handed every state agency Claude at a 50% discount plus free "
                  "workforce training.",
         "domain": "policy", "actor": ["austria", "european-union", "anthropic", "california"],
         "evidences": ["clearance-as-bottleneck", "regulatory-exit", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-27-a-tiered-planet-of-model-access"]},
        {"id": "2026-06-29-a-duty-of-loyalty-for-agents",
         "title": "A draft bill would impose a duty of loyalty on agent services",
         "claim": "Senator Mark Warner's draft bill would impose a duty of loyalty on agent "
                  "services and stop platforms from throttling their rivals.",
         "domain": "policy", "actor": ["us-congress"],
         "evidences": ["legislating-the-shift", "agent-society", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-06-25-labs-hire-philosophers-to-write-constitutions"]},
        {"id": "2026-06-29-a-five-hundred-eighty-five-billion-semiconductor-complex",
         "title": "A country answers the memory crunch with a $585B semiconductor megacomplex",
         "claim": "South Korea is building a $585 billion semiconductor megacomplex as Ming-Chi "
                  "Kuo said the memory gap will widen through 2027 while data centers devour "
                  "consumer supply, the reason Apple is lobbying to keep China's CXMT off the "
                  "Entity List.",
         "domain": "compute", "actor": ["apple"], "score": "$585B",
         "evidences": ["consumer-deprioritized", "science-as-industrial-policy", "silicon-curtain"],
         "supersedes": [B + "developments/2026-06-26-a-third-wave-of-inflation-reaches-the-checkout"]},
        {"id": "2026-06-29-five-labs-still-under-half-the-worlds-compute",
         "title": "The five biggest labs still used under half the world's AI compute",
         "claim": "Epoch's Josh You noted the five biggest labs still used under half the world's "
                  "AI compute at the end of 2025, yet Anthropic and OpenAI could swallow that "
                  "headroom within a few years, while Firmus and DayOne poured a 360-MW Nvidia "
                  "campus into Indonesia under a deal worth up to $30 billion.",
         "domain": "compute", "actor": ["epoch-ai", "firmus", "nvidia"], "score": "<50% / 360 MW",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-06-28-a-hyperscaler-throttles-another-hyperscaler"]},
        {"id": "2026-06-29-five-archetypes-replace-job-titles",
         "title": "Engineering, product and design melt into five archetypes",
         "claim": "Claude Code creator Boris Cherny sees engineering, product and design melting "
                  "into five archetypes — prototyper, builder, sweeper, grower and maintainer — "
                  "none tied to a job title, as a Deloitte town hall reportedly projected human "
                  "consultant billing shrinking to a sliver by 2035.",
         "domain": "economics", "actor": ["anthropic", "deloitte"],
         "evidences": ["agents-on-the-org-chart", "work-displaced", "the-persistent-colleague"],
         "supersedes": [B + "developments/2026-06-27-a-half-billion-dollar-retraining-push"]},
        {"id": "2026-06-29-a-thirteen-percent-hit-that-is-not-going-away",
         "title": "A dashboard tracking 4.6 million workers says the entry-level hit persists",
         "claim": "Erik Brynjolfsson's Canaries Dashboard, tracking 4.6 million workers, extended "
                  "his earlier finding that AI's roughly 13% hit to entry-level employment for "
                  "22-to-25-year-olds is not going away.",
         "domain": "economics", "actor": ["stanford"], "score": "-13% entry-level",
         "evidences": ["ladder-pulled-up", "work-displaced", "oral-tradition-dissolves"],
         "supersedes": [B + "developments/2026-06-13-junior-postings-up-as-hiring-collapses"]},
        {"id": "2026-06-29-a-feature-film-for-fifteen-million",
         "title": "A studio plans a feature with 40 animators for $15M instead of $100-200M",
         "claim": "One studio is planning an animated feature using 40 animators for about $15 "
                  "million instead of $100 to $200 million, even as a filmmaker quit an Amazon AI "
                  "project in protest and GPT-5.6 Pro one-shotted a legally distinct game clone "
                  "in 31 minutes.",
         "domain": "society", "score": "$15M vs $100-200M",
         "evidences": ["work-displaced", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-06-22-a-search-giant-buys-into-a-film-studio"]},
        {"id": "2026-06-29-an-average-of-96-craters-to-48",
         "title": "A take-home average of 96 craters to 48 once the exam goes in-person",
         "claim": "A Brown professor caught at least 50 students whose take-home average of 96 "
                  "cratered to 48 once the final went in-person, while East Asian students were "
                  "found reading exam answers off AI smart glasses.",
         "domain": "society", "actor": ["brown-university"], "score": "96 to 48",
         "evidences": ["deskilling", "cheating-breaks-the-ruler", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-06-21-humanizers-add-fake-typos-in-real-time"]},
        {"id": "2026-06-29-royalties-cut-for-fully-machine-made-songs",
         "title": "A streaming service cuts royalties for fully machine-made songs",
         "claim": "Tidal began tagging fully AI-generated songs from mid-July and cutting "
                  "royalties to anything it deems wholly machine-made.",
         "domain": "society", "actor": ["tidal"],
         "evidences": ["agent-exclusion", "work-displaced"],
         "supersedes": [B + "developments/2026-06-20-a-prize-defended-by-citing-the-model"]},
        {"id": "2026-06-29-renting-beats-owning-everywhere",
         "title": "Renting beats owning in every big metro as weights become the asset",
         "claim": "Renting is now cheaper than owning in every big US metro, with even "
                  "millionaires renting and asking whether owning anything matters, while Rocket "
                  "Lab bought Iridium for about $8 billion to own the entire space stack and the "
                  "Magnificent 7's price-to-earnings premium sank to a decade low.",
         "domain": "economics", "actor": ["rocket-lab", "iridium"], "score": "$8B",
         "evidences": ["own-your-own-weights", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-29-five-archetypes-replace-job-titles"]},
    ],
}
