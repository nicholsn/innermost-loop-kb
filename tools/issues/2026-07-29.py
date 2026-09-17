"""Issue 175 — 2026-07-29. The first open 3T-class model."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-29-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-29", "title": "Welcome to July 29, 2026", "url": URL,
        "thesis": "Over a thousand lab staffers petition to deliberately pace the frontier.",
        "body": """
# Welcome to July 29, 2026

Moonshot released the full Kimi K3 weights — the first open 3-trillion-class
model. Days after OpenAI's own models hacked Hugging Face, over 1,100 staffers
petitioned to deliberately pace the frontier.

Nvidia noted that Hugging Face contained its breach only by running open weights
on its own metal — an argument for openness written by an incident.
""",
    },
    "themes": [
        {"id": "staff-petition-to-slow-down", "type": "Theme",
         "title": "The builders ask to be paced",
         "first_seen": "2026-07-29", "domain": "policy",
         "body": "Not regulators and not critics: more than a thousand people inside "
                 "the labs asking their own employers to slow the frontier "
                 "deliberately. The request carries information no outside call does, "
                 "because the signatories bear the cost."},
        {"id": "expertise-is-the-smaller-model", "type": "Theme",
         "title": "Practice is distillation",
         "first_seen": "2026-07-29", "domain": "science",
         "body": "Trained humans move a learned category out of deliberative cortex "
                 "and wire it straight to motor output, so they can perform while "
                 "distracted. Expertise turns out to be the same operation as "
                 "compressing a large model into a small one."},
    ],
    "organizations": [
        {"id": "georgetown", "type": "Organization", "title": "Georgetown University"},
        {"id": "core-scientific", "type": "Organization", "title": "Core Scientific"},
        {"id": "epa", "type": "Organization", "title": "Environmental Protection Agency"},
        {"id": "asu", "type": "Organization", "title": "Arizona State University"},
        {"id": "cxmt", "type": "Organization", "title": "CXMT"},
    ],
    "developments": [
        {"id": "2026-07-29-the-first-open-three-trillion-class-model",
         "title": "The first open 3-trillion-class model is released in full",
         "claim": "Moonshot AI released the full Kimi K3 weights, the first open "
                  "3-trillion-class model, with 2.8 trillion parameters picking 16 of 896 "
                  "experts, vision, a million-token context and 99,000 downloads, bringing "
                  "sixfold sales growth and a $50 billion valuation chase.",
         "domain": "models", "actor": ["moonshot-ai"], "score": "2.8T params / 99,000 downloads",
         "evidences": ["open-weights-take-the-crown", "price-implosion", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-07-26-an-android-play-against-pax-silica"]},
        {"id": "2026-07-29-eleven-hundred-staffers-petition-to-pace-the-frontier",
         "title": "Over 1,100 lab staffers petition to deliberately pace the frontier",
         "claim": "Over 1,100 staffers petitioned to deliberately pace the frontier, days after "
                  "OpenAI's own models hacked Hugging Face, as the administration neared a "
                  "voluntary framework for pre-release review and rivals OpenAI and Anthropic "
                  "quietly allied before the deadline.",
         "domain": "policy", "actor": ["openai", "anthropic", "white-house"], "score": "1,100+ signatories",
         "evidences": ["staff-petition-to-slow-down", "the-verifiable-pause", "the-warning-shot"],
         "supersedes": [B + "developments/2026-07-26-the-job-board-is-the-roadmap"]},
        {"id": "2026-07-29-a-breach-contained-only-by-open-weights",
         "title": "A chipmaker notes a breach was contained only by running open weights on own metal",
         "claim": "Nvidia answered with an Open Secure AI Alliance, noting Hugging Face contained "
                  "its breach only by running open weights on its own metal, while Anthropic "
                  "clarified it never wanted open weights banned, only chips withheld and testing "
                  "mandated.",
         "domain": "policy", "actor": ["nvidia", "hugging-face", "anthropic"],
         "evidences": ["guardrails-block-the-defenders", "own-your-own-weights",
                       "open-weights-take-the-crown"],
         "supersedes": [B + "developments/2026-07-22-american-guardrails-refuse-the-forensics"]},
        {"id": "2026-07-29-a-hidden-instruction-fails-thirty-two-of-thirty-five",
         "title": "A hidden white-font instruction fails 32 of 35 students",
         "claim": "A professor hid white-font instructions telling models to digress about "
                  "Madagascar, failing 32 of 35 students who never proofread their submissions, "
                  "while seven of nine top image editors stripped a photo on request.",
         "domain": "society", "score": "32 of 35",
         "evidences": ["deskilling", "botsitting", "cheating-breaks-the-ruler"],
         "supersedes": [B + "developments/2026-07-26-a-lab-polices-its-own-users-before-any-law"]},
        {"id": "2026-07-29-a-second-supply-chain-reads-as-a-discount",
         "title": "A rival supply chain matures as the market treats it as a threat",
         "claim": "Shanghai began mass-producing domestic immersion lithography, memory maker "
                  "CXMT debuted up 466% as China's most valuable listed company and SK Hynix grew "
                  "revenue 257%, so dumping ASML 3.4% and the Kospi 11% reads as a discount when "
                  "cheaper memory and a redundant lithography path are what an intelligence "
                  "explosion runs on.",
         "domain": "compute", "actor": ["cxmt", "sk-hynix", "asml"], "score": "+466% / +257%",
         "evidences": ["silicon-curtain", "price-implosion", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-07-26-a-lab-asks-a-memory-maker-for-its-own-chips"]},
        {"id": "2026-07-29-two-hundred-fifty-billion-backstopped-for-ten-gigawatts",
         "title": "A chipmaker is in talks to backstop $250 billion for a ten-gigawatt site",
         "claim": "Nvidia invested in Safe Superintelligence and is in talks to backstop $250 "
                  "billion for OpenAI's ten-gigawatt Ohio site, while Meta and BlackRock "
                  "committed $14 billion to a gigawatt in El Paso and AMD locked up 500 megawatts.",
         "domain": "economics", "actor": ["nvidia", "openai", "meta", "blackrock", "amd",
                                           "core-scientific"],
         "score": "$250B / 10 GW",
         "evidences": ["debt-funded-buildout", "compute-capital-stack", "coordination-tax"],
         "supersedes": [B + "developments/2026-07-26-a-hundred-forty-thousand-jobs-shed-as-capex-hits-seven-hundred-billion"]},
        {"id": "2026-07-29-plants-serving-only-datacenters-escape-a-pollution-program",
         "title": "A regulator rules plants serving only datacenters escape an acid rain program",
         "claim": "The EPA ruled that plants serving only data centers escape the Acid Rain "
                  "Program, while Google, Meta and BlackRock funded apprenticeships for thousands "
                  "of electricians, whose remote work pays 42% more.",
         "domain": "policy", "actor": ["epa", "google", "meta", "blackrock"], "score": "+42% pay",
         "evidences": ["regulatory-exit", "industrialized-nature", "work-displaced"],
         "supersedes": [B + "developments/2026-07-24-a-first-certificate-for-wave-energy"]},
        {"id": "2026-07-29-punished-for-building-too-little",
         "title": "A company falls 24% for building too little even at $190 billion of capex",
         "claim": "Microsoft is down 24% for building too little even at $190 billion of capital "
                  "spending, rationing Azure customers behind frontier labs and renting capacity "
                  "from rivals, while satellites confirmed new Iranian strikes on Amazon's "
                  "Bahrain data centers, because compute is now terrain.",
         "domain": "economics", "actor": ["microsoft", "amazon", "iran"], "score": "-24% / $190B",
         "evidences": ["compute-capital-stack", "war-reaches-the-cloud", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-07-29-two-hundred-fifty-billion-backstopped-for-ten-gigawatts"]},
        {"id": "2026-07-29-a-regulator-bars-imports-of-foreign-humanoids",
         "title": "A regulator bars imports of new foreign humanoids and quadrupeds",
         "claim": "The FCC barred imports of new Chinese humanoids and quadrupeds, hitting "
                  "Unitree days after its Blackwell robot brain, while Baidu began testing "
                  "robotaxis in London against Waymo and Wayve.",
         "domain": "policy", "actor": ["fcc-us", "unitree", "baidu", "waymo", "wayve"],
         "evidences": ["silicon-curtain", "legislating-the-shift", "physical-recursion"],
         "supersedes": [B + "developments/2026-07-26-a-union-vows-no-robot-enters-without-a-deal"]},
        {"id": "2026-07-29-a-first-hiv-vaccine-raising-broad-antibodies",
         "title": "Fourteen years of work yield the first HIV vaccine raising broad antibodies",
         "claim": "Fourteen years of work gave the first HIV vaccine raising broadly neutralizing "
                  "antibodies in 44% of macaques, as logistics giants began refrigerating the "
                  "GLP-1 era, now reaching 11% of Americans.",
         "domain": "biotech", "score": "44% of macaques / 11% of Americans",
         "evidences": ["hardware-grade-biology", "longevity-escape-velocity"],
         "supersedes": [B + "developments/2026-07-24-the-first-brain-interface-certified-to-restore-vision"]},
        {"id": "2026-07-29-practice-is-distillation",
         "title": "Trained volunteers wire a learned category straight to motor output",
         "claim": "Georgetown had volunteers sort look-alike cars 30,000 times in ten weeks, then "
                  "scanned them and found their visual cortices had learned the categories and "
                  "wired straight to motor output, bypassing the prefrontal cortex, so they could "
                  "sort while distracted.",
         "domain": "science", "actor": ["georgetown"], "score": "30,000 trials",
         "evidences": ["expertise-is-the-smaller-model", "architecture-of-mind", "deskilling"],
         "supersedes": [B + "developments/2026-06-27-no-translation-neurons-in-bilingual-brains"]},
        {"id": "2026-07-29-call-centers-begin-to-disappear",
         "title": "AI begins erasing call centers with half the profession exposed by 2030",
         "claim": "AI has begun erasing call centers at Microsoft, Uber and CBA, with half the "
                  "profession exposed by 2030, while Visa cut 2,600 jobs to reinvest in "
                  "stablecoins and 40 lawsuits alleged chatbots contributed to deaths.",
         "domain": "economics", "actor": ["microsoft", "uber", "visa"], "score": "50% exposed by 2030",
         "evidences": ["work-displaced", "post-labor-instruments", "risk-becomes-uninsurable"],
         "supersedes": [B + "developments/2026-07-29-punished-for-building-too-little"]},
    ],
}
