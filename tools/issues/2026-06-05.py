"""Issue 132 — 2026-06-05. When AI builds itself."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-5-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-05", "title": "Welcome to June 5, 2026", "url": URL,
        "thesis": "A lab publishes the evidence that its own work is already recursive.",
        "body": """
# Welcome to June 5, 2026

The Anthropic Institute published *When AI builds itself*, showing with public
and internal data that AI is already accelerating AI development, and arguing
the world should keep the option to verifiably pause before recursive
self-improvement — which it says could come sooner than most institutions are
prepared for.

The numbers: engineers shipping 8x the code of 2021-2025. Claude's success on
open-ended problems up 50 points to 76% in six months. On a standing test to
speed up model-training code, Mythos Preview hit ~52x where a skilled human
reaches 4x and 2024's Opus 4 managed 3x.

The lab asked its rivals to weigh slowing down. Almost nobody is reaching for
that brake.
""",
    },
    "themes": [
        {"id": "the-verifiable-pause", "type": "Theme",
         "title": "Keeping the option to stop",
         "first_seen": "2026-06-05", "domain": "policy",
         "body": "Not a call to halt, but a call to preserve the capability to halt. "
                 "Its central problem is verification: a training run is harder to "
                 "confirm stopped than a nuclear site, and the actor proposing the "
                 "brake is the one with the most to lose by pulling it."},
    ],
    "organizations": [
        {"id": "antares", "type": "Organization", "title": "Antares",
         "body": "Achieved the first private non-light-water reactor criticality in the US "
                 "in forty years."},
        {"id": "caltech", "type": "Organization", "title": "Caltech",
         "resource": "https://www.caltech.edu/"},
        {"id": "cambridge", "type": "Organization", "title": "University of Cambridge"},
        {"id": "argentina", "type": "Organization", "title": "Argentina"},
        {"id": "nsa", "type": "Organization", "title": "National Security Agency"},
    ],
    "developments": [
        {"id": "2026-06-05-when-ai-builds-itself",
         "title": "A lab publishes the evidence that AI already accelerates AI",
         "claim": "The Anthropic Institute published When AI builds itself, showing with public "
                  "and internal data that AI is already accelerating AI development, and arguing "
                  "the world should keep the option to verifiably pause before recursive "
                  "self-improvement, which it said could come sooner than most institutions are "
                  "prepared for.",
         "domain": "models", "actor": ["anthropic-institute", "anthropic"],
         "evidences": ["recursive-self-improvement", "the-verifiable-pause", "takeoff-declared"],
         "supersedes": [B + "developments/2026-05-05-sixty-percent-odds-on-rsi-by-2028"],
         "body": "The lab conceded none of it guarantees runaway recursion yet, since "
                 "picking the right problems is still unproven. It asked rival labs to "
                 "weigh slowing down, while admitting such a brake would be harder to "
                 "verify than a nuclear site."},
        {"id": "2026-06-05-fifty-two-x-where-a-human-reaches-four",
         "title": "A model speeds up training code thirteen times better than a skilled human",
         "claim": "On a standing test to speed up model-training code, Mythos Preview reached "
                  "roughly 52x where a skilled human reaches 4x and 2024's Opus 4 managed 3x, "
                  "while Anthropic engineers now ship eight times as much code per quarter as "
                  "in 2021-2025.",
         "domain": "models", "actor": ["anthropic"], "score": "52x vs 4x human",
         "evidences": ["recursive-self-improvement", "humans-need-not-apply",
                       "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-06-05-when-ai-builds-itself"]},
        {"id": "2026-06-05-the-model-learns-to-steer",
         "title": "A model learns to abandon dead ends better than its researchers",
         "claim": "Claude improved on researchers who hit a dead end 64% of the time, up from "
                  "22% in 2024, and its success on open-ended problems jumped 50 points to 76% "
                  "in six months at quality already on par with human and projected to pass it "
                  "within the year.",
         "domain": "models", "actor": ["anthropic"], "score": "76%, up 50 points",
         "evidences": ["recursive-self-improvement", "discovery-as-process", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-06-05-fifty-two-x-where-a-human-reaches-four"],
         "body": "Picking the right problem was the last thing the lab said it could not "
                 "yet automate. This is the measurement of that gap closing."},
        {"id": "2026-06-05-ten-million-back-if-the-agent-underdelivers",
         "title": "A vendor offers to pay up to $10M if its agent underdelivers",
         "claim": "Cognition offered to foot a customer's bill up to $10 million if Devin "
                  "underdelivers, while an ICML paper showed transformers can share query-key-"
                  "value projections to shrink the KV cache by up to 96.9% for on-device "
                  "inference.",
         "domain": "agents", "actor": ["cognition"], "score": "$10M guarantee / -96.9% KV cache",
         "evidences": ["agent-economy", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-06-04-a-laptop-multimodal-model-under-apache"]},
        {"id": "2026-06-05-a-dormant-face-recognition-pipeline",
         "title": "A dormant facial-recognition pipeline ships to millions of phones",
         "claim": "WIRED found Meta has quietly shipped a dormant facial-recognition pipeline "
                  "called NameTag to tens of millions of smart-glasses phones, while OpenAI's "
                  "new dreaming memory keeps ChatGPT current on a user's life in the background.",
         "domain": "society", "actor": ["meta", "openai"],
         "evidences": ["intimate-interface", "humans-as-peripherals"],
         "supersedes": [B + "developments/2026-06-04-a-voice-cloned-faster-than-reaction-time"]},
        {"id": "2026-06-05-engineers-embedded-in-the-nsa",
         "title": "A lab embeds engineers in the NSA to point its model at offensive cyber",
         "claim": "Anthropic embedded engineers in the NSA to point Mythos at offensive cyber "
                  "operations.",
         "domain": "policy", "actor": ["anthropic", "nsa"],
         "evidences": ["war-reaches-the-cloud", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-06-03-a-model-defends-a-hundred-fifty-organizations"],
         "body": "Project Glasswing defends critical infrastructure with the same model "
                 "now being aimed outward."},
        {"id": "2026-06-05-fusion-passes-a-hundred-fifty-million-degrees",
         "title": "A private fusion prototype burns D-T fuel past 150 million degrees",
         "claim": "Helion raised $465 million at a $15.5 billion valuation after its prototype, "
                  "the first private machine to burn deuterium-tritium fuel, passed 150 million "
                  "°C, while Antares achieved the first private non-light-water reactor "
                  "criticality in the US in forty years.",
         "domain": "energy", "actor": ["helion", "antares"], "score": "150M °C / $15.5B",
         "evidences": ["industrialized-nature", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-06-01-warhead-plutonium-becomes-reactor-fuel"]},
        {"id": "2026-06-05-retired-robotaxi-batteries-become-grid-storage",
         "title": "Retired robotaxi batteries return as grid storage",
         "claim": "Waymo is resurrecting retired robotaxi batteries as hundreds of megawatts of "
                  "storage on the very California and Texas grids its fleet charges from, while "
                  "a datacenter developer halved a 40,000-acre Utah project after a backlash "
                  "over a wildlife refuge.",
         "domain": "energy", "actor": ["waymo"], "score": "hundreds of MW",
         "evidences": ["industrialized-nature", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-06-04-replenishing-more-water-than-consumed"]},
        {"id": "2026-06-05-a-genome-stitched-error-free-in-days",
         "title": "A synthesis method stitches a bacterial genome error-free in days",
         "claim": "Caltech's Sidewinder DNA synthesis misfires once per 10 million joins, "
                  "stitching a 12,500-letter E. coli genome error-free in days, finally fast "
                  "enough to build what models like Evo 2 design faster than anyone can "
                  "assemble.",
         "domain": "biotech", "actor": ["caltech"], "score": "1 error per 10M joins",
         "evidences": ["compiling-matter", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-04-four-lab-chiefs-ask-congress-to-screen-dna"],
         "body": "Published the day after four lab chiefs asked Congress to screen "
                 "synthetic DNA orders."},
        {"id": "2026-06-05-the-first-ai-designed-vaccine-in-people",
         "title": "The first AI-designed vaccine is trialled in people",
         "claim": "Cambridge trialled the first AI-designed vaccine in people, aimed at every "
                  "coronavirus and now extending to flu and Ebola.",
         "domain": "biotech", "actor": ["cambridge"],
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-01-a-biodefense-model-for-trusted-developers"]},
        {"id": "2026-06-05-washington-weighs-equity-in-the-labs",
         "title": "Washington quietly weighs equity stakes in AI labs",
         "claim": "Washington is quietly weighing equity stakes in AI labs, an idea Altman "
                  "pitched to the President in early 2025 as a public dividend and one Anthropic "
                  "says it has stayed out of, as the lab's rift with the White House thaws "
                  "ahead of its IPO.",
         "domain": "policy", "actor": ["white-house", "openai", "anthropic"],
         "evidences": ["politics-as-infrastructure", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-02-a-sovereign-wealth-fund-paid-in-lab-stock"]},
        {"id": "2026-06-05-a-legal-home-for-non-human-corporations",
         "title": "A country gives AI agents a legal home",
         "claim": "Argentina's Javier Milei gave AI agents a legal home, a non-human corporation "
                  "whose independent judgment earns it limited liability.",
         "domain": "policy", "actor": ["argentina"],
         "evidences": ["agent-society", "legislating-the-shift", "one-person-company"],
         "supersedes": [B + "developments/2026-05-20-minnesota-criminalizes-hosting-prediction-markets"],
         "body": "The first jurisdiction to grant an agent a corporate form of its own "
                 "rather than treating it as a tool operated by someone else."},
    ],
}
