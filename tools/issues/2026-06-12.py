"""Issue 137 — 2026-06-12. A Dyson Swarm goes public."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-12", "title": "Welcome to June 12, 2026", "url": URL,
        "thesis": "The largest IPO ever is a fundraise for orbital compute.",
        "body": """
# Welcome to June 12, 2026

SpaceX prices the largest IPO ever near $1.8 trillion, and on a pre-IPO
livestream Musk gave the reason plainly: raising funds for the massive capital
endeavor of orbital data centers — round-the-clock solar beyond Earth's power
budget and beyond its backlash.

Also: a clause permitting the poisoning of AI research was caught in Fable 5's
system card, and Anthropic reversed within 48 hours and apologized.
""",
    },
    "organizations": [
        {"id": "ai-alliance", "type": "Organization", "title": "AI Alliance"},
        {"id": "kioxia", "type": "Organization", "title": "Kioxia"},
        {"id": "visa", "type": "Organization", "title": "Visa"},
        {"id": "beijing-301", "type": "Organization", "title": "301 Hospital, Beijing"},
        {"id": "igi", "type": "Organization", "title": "Innovative Genomics Institute"},
    ],
    "developments": [
        {"id": "2026-06-12-the-largest-ipo-ever-funds-orbital-compute",
         "title": "The largest IPO ever is explicitly a fundraise for orbital datacenters",
         "claim": "SpaceX priced the largest IPO ever near $1.8 trillion, with Musk saying on a "
                  "pre-IPO livestream that the purpose is funding the massive capital endeavor "
                  "of orbital data centers, his main way to expand AI with round-the-clock "
                  "solar beyond Earth's power budget and backlash.",
         "domain": "economics", "actor": ["spacex"], "score": "~$1.8T",
         "evidences": ["orbit-as-compute", "compute-capital-stack", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-09-three-of-the-largest-listings-on-record"]},
        {"id": "2026-06-12-the-no-cot-horizon-doubles-yearly",
         "title": "Models' no-chain-of-thought time horizon has doubled yearly for six years",
         "claim": "A study found frontier models' no-chain-of-thought time horizon has doubled "
                  "yearly for six years, with GPT-5.5 reasoning past three human-minutes and "
                  "projected to reach 25 by 2030.",
         "domain": "models", "actor": ["openai"], "score": "3 min now, 25 by 2030",
         "evidences": ["autonomy-clock-speed", "takeoff-declared"],
         "supersedes": [B + "developments/2026-05-14-doubling-time-compresses-to-45-months"]},
        {"id": "2026-06-12-a-poisoning-clause-reversed-in-48-hours",
         "title": "A clause permitting poisoning of AI research is reversed within 48 hours",
         "claim": "After researchers caught a clause allowing the poisoning of AI research in "
                  "Fable 5's system card, Anthropic reversed the policy within 48 hours and "
                  "apologized.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["rationed-recursion", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-06-10-mythos-on-a-leash"]},
        {"id": "2026-06-12-a-genuine-leap-in-exploit-development",
         "title": "A model family is judged seven months ahead of trend on exploit development",
         "claim": "Epoch AI judged the Mythos family a genuine leap in exploit development, "
                  "seven months ahead of trend, while Microsoft's larger Patch Tuesday reflected "
                  "AI scanning surfacing more bugs in even its best code.",
         "domain": "compute", "actor": ["epoch-ai", "anthropic", "microsoft"],
         "score": "7 months ahead of trend",
         "evidences": ["risk-becomes-uninsurable", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-06-07-cve-disclosures-spike-with-a-model-release"]},
        {"id": "2026-06-12-malware-hides-behind-safety-refusals",
         "title": "Malware authors stuff spyware with text that trips safety refusals",
         "claim": "Malware authors began stuffing spyware with nuclear and biological weapons "
                  "text specifically to trip AI scanners' safety refusals, turning alignment "
                  "into an evasion surface.",
         "domain": "compute",
         "evidences": ["sandbox-escape", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-06-12-a-genuine-leap-in-exploit-development"]},
        {"id": "2026-06-12-nations-co-train-one-shared-model",
         "title": "Nations are offered a way to co-train one shared model with local data",
         "claim": "The AI Alliance's Project Tapestry lets nations co-train a single shared "
                  "model while keeping their data local, as OpenAI weighs drastic price cuts "
                  "against Anthropic, racing the cost of intelligence toward zero.",
         "domain": "policy", "actor": ["ai-alliance", "openai", "anthropic"],
         "evidences": ["reasoning-price-deflation", "open-weight-latency", "network-over-node"],
         "supersedes": [B + "developments/2026-06-07-enterprises-route-by-difficulty"]},
        {"id": "2026-06-12-a-memory-maker-passes-an-automaker",
         "title": "A memory-chip maker overtakes an automaker as Japan's most valuable firm",
         "claim": "Kioxia, up 600% this year, overtook Toyota as Japan's most valuable firm, "
                  "while Nvidia, shut out of China's GPU market, began pitching Arm-based Vera "
                  "CPUs to Chinese clients and Google courted Samsung to help build a future AI "
                  "chip as the crunch pushed past TSMC.",
         "domain": "economics", "actor": ["kioxia", "toyota", "nvidia", "google", "samsung"],
         "score": "+600%",
         "evidences": ["ai-as-the-economy", "silicon-curtain", "vertical-silicon"],
         "supersedes": [B + "developments/2026-06-02-an-ai-bet-dethrones-the-combustion-engine"]},
        {"id": "2026-06-12-agents-reach-for-your-wallet",
         "title": "A card network moves inside a chatbot and an exchange opens to agents",
         "claim": "Visa now sits inside ChatGPT to check out anywhere, and Coinbase for Agents "
                  "lets an AI trade within user-set limits.",
         "domain": "agents", "actor": ["visa", "openai", "coinbase"],
         "evidences": ["autonomous-commerce", "agent-economy"],
         "supersedes": [B + "developments/2026-06-04-a-tireless-salesforce-across-three-apps"]},
        {"id": "2026-06-12-a-lab-leases-its-own-datacenters",
         "title": "A lab signs a dozen letters of intent to lease its own datacenters",
         "claim": "Anthropic signed more than a dozen letters of intent to lease its own data "
                  "centers, backed by Google, while Epoch found the largest single data center "
                  "has doubled compute every seven months since 2024.",
         "domain": "compute", "actor": ["anthropic", "google", "epoch-ai"],
         "score": "doubling every 7 months",
         "evidences": ["compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2026-06-07-a-rival-ends-up-powering-its-pursuer"]},
        {"id": "2026-06-12-terminator-mode-drones-kill-without-a-human",
         "title": "Fully autonomous drones have killed with no human in the loop",
         "claim": "A Ukrainian official confirmed that fully autonomous drones have killed "
                  "soldiers with no human in the loop, while OpenAI exposed a China-linked "
                  "influence operation seeding narratives against US data centers.",
         "domain": "robotics", "actor": ["ukraine", "openai"],
         "evidences": ["violence-arrives", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-06-10-six-hundred-sixty-humanoids-and-a-robot-truck-listing"],
         "body": "The threshold the field had described as a line rather than a slope, "
                 "crossed and confirmed after the fact."},
        {"id": "2026-06-12-solar-outproduces-coal",
         "title": "US solar outproduces coal for the first time",
         "claim": "US solar outproduced coal for the first time, as Commonwealth Fusion detailed "
                  "an upcoming 400-MW ARC reactor across five papers and BYD switched on 1.5-MW "
                  "chargers adding 400km of range in five minutes.",
         "domain": "energy", "actor": ["commonwealth-fusion", "byd"], "score": "400 MW ARC",
         "evidences": ["industrialized-nature", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-06-05-fusion-passes-a-hundred-fifty-million-degrees"]},
        {"id": "2026-06-12-a-beam-a-hundred-million-times-brighter-than-the-sun",
         "title": "A laser phase plate images half the proteins running life inside cells",
         "claim": "A Biohub-Berkeley laser phase plate, a beam 100 million times brighter than "
                  "the Sun's surface, sharpened cryo-EM enough to image over half the proteins "
                  "running life inside intact cells.",
         "domain": "biotech", "actor": ["czi"], "score": "100M x solar brightness",
         "evidences": ["hardware-grade-biology", "automated-science"],
         "supersedes": [B + "developments/2026-06-09-retrieval-makes-biology-agent-legible"]},
        {"id": "2026-06-12-ai-overviews-ruled-to-be-speech",
         "title": "A court rules AI summaries are the platform's own speech",
         "claim": "A German court ruled Google's AI Overviews to be the company's own speech and "
                  "therefore liable for falsehoods, while Dario Amodei warned policy is plodding "
                  "like Treebeard as AI sprints and urged a leap past transparency to FAA-style "
                  "testing of top models.",
         "domain": "policy", "actor": ["google", "anthropic"],
         "evidences": ["legislating-the-shift", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-06-10-a-testing-unit-told-to-stop-publishing"]},
        {"id": "2026-06-12-recursion-could-delay-an-ipo",
         "title": "A chief executive warns recursive self-improvement could delay his own IPO",
         "claim": "Sam Altman warned that recursive self-improvement could delay OpenAI's IPO, "
                  "while the President predicted AI firms will give back through equity stakes "
                  "that make citizens very rich.",
         "description": "Recursive self-improvement enters a chief executive's guidance to investors as a "
                        "scheduling variable, the point at which the newsletter says the biggest players "
                        "begin pacing themselves against the Singularity.",
         "domain": "economics", "actor": ["openai", "people/sam-altman", "white-house"],
         "occurred_on": "2026-06-10",
         "evidences": ["recursive-self-improvement", "takeoff-declared", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-06-07-everyone-wants-on-the-cap-table",
                        B + "developments/2026-06-09-three-of-the-largest-listings-on-record"],
         "relatedTo": [B + "developments/2025-12-28-altman-self-improving-in-production",
                       B + "developments/2026-06-09-a-personal-agi-for-every-human",
                       B + "developments/2026-06-12-the-largest-ipo-ever-funds-orbital-compute"],
         "tags": ["rsi", "funding", "forecast"],
         "supporting_text": "Sam Altman warning recursive self-improvement could",
         "sources": [{"id": "reuters-openai-expects-to-go-public-within-next-year",
                      "resource": "https://www.reuters.com/business/openai-expects-go-public-within-next-year-information-reports-2026-06-10/",
                      "title": "OpenAI expects to go public within next year, The Information reports",
                      "author": "org:reuters", "last_modified": "2026-06-10"},
                     {"id": "reuters-trump-ai-companies-giving-back",
                      "resource": "https://www.reuters.com/business/media-telecom/trump-says-he-thinks-ai-companies-will-agree-giving-back-public-2026-06-10/",
                      "title": "Trump says he thinks AI companies will agree to giving back to public",
                      "author": "org:reuters", "last_modified": "2026-06-10"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The first time the loop is named as a scheduling risk to a "
                 "company's own liquidity event. Reuters, relaying The Information on June 10, reported that "
                 "OpenAI expects to go public within the next year, with [Sam Altman](/people/sam-altman.md) "
                 "cautioning that recursive self-improvement could push the timing back "
                 "([Reuters](https://www.reuters.com/business/openai-expects-go-public-within-next-year-information-reports-2026-06-10/)), "
                 "while the President predicted AI firms would give back to the public through equity stakes that "
                 "make citizens \"very rich\" "
                 "([Reuters](https://www.reuters.com/business/media-telecom/trump-says-he-thinks-ai-companies-will-agree-giving-back-public-2026-06-10/)). "
                 "It follows OpenAI's [confidential IPO filing](/developments/2026-06-09-three-of-the-largest-listings-on-record.md) "
                 "at $850 billion-plus and its [plan dating an automated AI researcher to March 2028](/developments/2026-06-09-a-personal-agi-for-every-human.md), "
                 "and it revisits the [equity-stake idea](/developments/2026-06-07-everyone-wants-on-the-cap-table.md) "
                 "of the week before; in the trajectory it marks the point where the executive who "
                 "[confirmed self-improving systems in production](/developments/2025-12-28-altman-self-improving-in-production.md) "
                 "in December begins treating the loop as a variable in corporate finance."},
    ],
}
