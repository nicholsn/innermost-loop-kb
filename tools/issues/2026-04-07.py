"""Issue 092 — 2026-04-07. Seventy-two hours of unsupervised research."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-7-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-07", "title": "Welcome to April 7, 2026", "url": URL,
        "thesis": "Left alone for three days, a system invents something better than anything humans designed.",
        "body": """
# Welcome to April 7, 2026

UNC researchers let an AI run unsupervised for 72 hours. It executed 50
experiments and invented a long-context memory system that beats every
human-designed baseline.

Meanwhile a city councilor in Indianapolis says his home was shot at thirteen
times over a proposed neighborhood data center, with a note reading NO DATA
CENTERS. The cloud casts a local shadow.
""",
    },
    "organizations": [
        {"id": "unc", "type": "Organization", "title": "University of North Carolina at Chapel Hill",
         "description": "Public research university whose Chapel Hill researchers ran the corpus's "
                        "72-hour unattended research loop that invented the Omni-SimpleMem agent "
                        "memory system.",
         "resource": "https://www.unc.edu/",
         "sameAs": ["http://www.wikidata.org/entity/Q192334"],
         "tags": ["university"],
         "body": "The University of North Carolina at Chapel Hill is the flagship campus of the "
                 "state's public university system. It enters this corpus once, as the home of "
                 "the team whose autonomous research pipeline ran "
                 "[roughly fifty experiments over three unsupervised days](/developments/2026-04-07-seventy-two-hours-fifty-experiments.md) "
                 "and produced a long-context agent memory system that beat every hand-designed "
                 "baseline, an early academic instance of the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) loop the "
                 "newsletter tracks."},
        {"id": "frontier-model-forum", "type": "Organization", "title": "Frontier Model Forum",
         "body": "Industry body through which labs share distillation-attack intelligence."},
        {"id": "henry-intelligent", "type": "Organization", "title": "Henry Intelligent Machines",
         "body": "Agent layer operating fleets of microbusinesses for a single owner."},
        {"id": "meti", "type": "Organization", "title": "METI",
         "body": "Japan's trade ministry; targeting 30% of the global physical AI market."},
        {"id": "aei", "type": "Organization", "title": "American Enterprise Institute",
         "resource": "https://www.aei.org/"},
    ],
    "developments": [
        {"id": "2026-04-07-seventy-two-hours-fifty-experiments",
         "title": "Three unsupervised days produce a memory system beating every baseline",
         "claim": "UNC researchers let an AI run autonomously for 72 hours, during which it ran "
                  "fifty experiments and invented a long-context memory system that beats every "
                  "human-designed baseline.",
         "description": "The author's 'scientist is now a subroutine' moment: an unattended loop "
                        "is credited with inventing an architecture rather than tuning one, and "
                        "its largest gains came from bug fixes and structural changes beyond the "
                        "reach of AutoML.",
         "domain": "agents", "actor": ["unc"], "score": "72 hours / 50 experiments",
         "evidences": ["recursive-self-improvement", "automated-science"],
         "supersedes": [B + "developments/2026-04-05-self-distillation-without-a-teacher",
                        B + "developments/2026-03-09-autoresearch-650-experiments"],
         "relatedTo": [B + "developments/2026-02-12-alma-agents-design-their-own-memory",
                       B + "developments/2026-03-31-bilevel-autoresearch"],
         "tags": ["autonomous-research", "rsi", "ai-r-and-d"],
         "supporting_text": "let an AI loose for 72 hours of autonomous research",
         "sources": [{"id": "omni-simplemem-arxiv",
                      "resource": "https://arxiv.org/abs/2604.01007",
                      "title": "Omni-SimpleMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory",
                      "author": "org:unc"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The paper behind the item is *Omni-SimpleMem* "
                 "([arXiv 2604.01007](https://arxiv.org/abs/2604.01007)), from a UNC-led team: an "
                 "autonomous research pipeline started from a naive agent-memory baseline and, with "
                 "no human in the inner loop, executed roughly 50 experiments across two benchmarks "
                 "over what the newsletter reports as 72 unattended hours, lifting F1 on LoCoMo from "
                 "0.117 to 0.598 (+411%) and on Mem-Gallery from 0.254 to 0.797 (+214%) to reach "
                 "state of the art on both. The authors stress that the biggest gains were bug "
                 "fixes, architectural changes and prompt rewrites rather than hyperparameter "
                 "tuning, which is what separates the run from AutoML. In the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it "
                 "sits between Karpathy's "
                 "[650-experiment autoresearch run](/developments/2026-03-09-autoresearch-650-experiments.md) "
                 "and Anthropic's report the next day that Mythos "
                 "[sped internal research up to 400x](/developments/2026-04-08-research-sped-up-400x.md); "
                 "the target it optimized, agent memory, is the same one "
                 "[ALMA](/developments/2026-02-12-alma-agents-design-their-own-memory.md) had agents "
                 "meta-learn in February."},
        {"id": "2026-04-07-labs-share-distillation-intelligence",
         "title": "Rival labs begin sharing intelligence on distillation attacks",
         "claim": "OpenAI, Anthropic and Google are sharing intelligence through the Frontier "
                  "Model Forum to detect Chinese distillation attacks.",
         "domain": "policy", "actor": ["openai", "anthropic", "google", "frontier-model-forum"],
         "evidences": ["silicon-curtain", "coordination-tax"],
         "supersedes": [B + "developments/2026-04-01-claude-code-leaks-with-decoy-tools"],
         "body": "The decoy tools were one lab's defence. This is a shared one."},
        {"id": "2026-04-07-one-person-conglomerates",
         "title": "An agent layer operates fleets of microbusinesses for one owner",
         "claim": "Henry Intelligent Machines unveiled the first one-person AI conglomerates, "
                  "an agent layer that spins up and operates fleets of microbusinesses for a "
                  "single human owner, while Meta ran an internal leaderboard where employees "
                  "competed by burning tokens.",
         "domain": "economics", "actor": ["henry-intelligent", "meta"],
         "evidences": ["one-person-company", "compute-as-compensation", "agent-economy"],
         "supersedes": [B + "developments/2026-04-05-unicorn-founders-get-younger"]},
        {"id": "2026-04-07-bug-bounty-pauses-submissions",
         "title": "A bug bounty pauses submissions because discovery got too cheap",
         "claim": "The Internet Bug Bounty program paused new submissions because AI-assisted "
                  "vulnerability discovery became too cheap to price.",
         "domain": "economics",
         "evidences": ["reasoning-price-deflation", "coordination-tax"],
         "supersedes": [B + "developments/2026-04-03-cyber-autonomy-doubles-every-57-months"]},
        {"id": "2026-04-07-samsung-profit-up-eightfold",
         "title": "Samsung's quarterly profit rises more than eightfold",
         "claim": "Samsung reported a record quarterly operating profit of roughly $38 billion, "
                  "up more than eightfold year over year, as AI chip demand pushed memory "
                  "prices higher.",
         "domain": "economics", "actor": ["samsung"], "score": "~$38B, 8x",
         "evidences": ["compute-capital-stack", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-04-02-chinese-gpus-take-41-percent-at-home"]},
        {"id": "2026-04-07-anthropic-run-rate-triples-in-a-quarter",
         "title": "One lab's run rate goes from $9B to over $30B in a quarter",
         "claim": "Anthropic inked a multi-gigawatt TPU deal with Google and Broadcom while "
                  "disclosing run-rate revenue leapt from roughly $9 billion at the end of 2025 "
                  "to over $30 billion, as OpenAI reportedly planned to spend $121 billion on "
                  "compute in 2028 alone.",
         "domain": "economics", "actor": ["anthropic", "google", "broadcom", "openai"],
         "score": "$9B → $30B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-04-03-experts-forecast-growth-and-fewer-jobs"]},
        {"id": "2026-04-07-a-councilors-home-is-shot-over-a-datacenter",
         "title": "A councilor's home is shot thirteen times over a datacenter proposal",
         "claim": "An Indianapolis city councilor says his home was shot at thirteen times over "
                  "a proposed neighborhood data center, with a note reading no data centers.",
         "domain": "society", "score": "13 shots",
         "evidences": ["infrastructure-crowding-out", "regulatory-exit"],
         "supersedes": [B + "developments/2026-04-05-half-of-us-datacenters-may-slip"],
         "body": "The first act of violence in the corpus directed at the buildout itself."},
        {"id": "2026-04-07-companion-dolls-for-the-elderly",
         "title": "South Korea deploys thousands of chatbot companion dolls to its elderly",
         "claim": "South Korea is deploying thousands of chatbot-enabled companion dolls to its "
                  "elderly, now roughly a fifth of the population, while Japan's trade ministry "
                  "targets 30% of the global physical AI market by 2040.",
         "domain": "society", "actor": ["meti"], "score": "20% of population",
         "evidences": ["intimate-interface", "machine-affect"],
         "supersedes": [B + "developments/2026-04-03-harvard-replaces-freshman-advisers"]},
        {"id": "2026-04-07-first-megawatt-hydrogen-turboprop",
         "title": "The first megawatt-class hydrogen turboprop flies",
         "claim": "China flew the world's first megawatt-class hydrogen turboprop for sixteen "
                  "minutes.",
         "domain": "energy", "actor": ["china"], "score": "16 minutes",
         "evidences": ["burning-molecules-for-tokens"]},
        {"id": "2026-04-07-artemis-breaks-apollo-13s-distance-record",
         "title": "Artemis II breaks Apollo 13's distance record and sees the full far side",
         "claim": "Artemis II broke Apollo 13's record for the farthest humans from Earth and "
                  "its crew became the first to see the Moon's entire far side, while Anduril's "
                  "telescopes captured Orion separating from its upper stage 30,000 miles up "
                  "and MoonRF released open-source hardware for bouncing signals off the Moon.",
         "domain": "space", "actor": ["nasa", "anduril"], "score": "30,000 miles",
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-04-05-artemis-crosses-the-halfway-point"]},
        {"id": "2026-04-07-one-plant-five-psychedelics",
         "title": "One tobacco plant is engineered to make five psychedelics at once",
         "claim": "Scientists engineered a single tobacco plant to produce five different "
                  "psychedelics simultaneously by importing genes from plants, toads and "
                  "mushrooms, while Finnish researchers found sauna bathing triggers powerful "
                  "immune cell responses.",
         "domain": "biotech",
         "evidences": ["hardware-grade-biology", "compiling-matter"],
         "supersedes": [B + "developments/2026-04-05-an-appetite-suppressant-from-python-blood"]},
        {"id": "2026-04-07-openai-proposes-a-new-social-contract",
         "title": "OpenAI proposes automated-labor taxes and a public wealth fund",
         "claim": "OpenAI proposed an industrial policy for the intelligence age featuring "
                  "automated-labor taxes, a public wealth fund and four-day workweek pilots, "
                  "with Sam Altman calling for a new social contract on the scale of the New "
                  "Deal.",
         "domain": "policy", "actor": ["openai", "people/sam-altman"],
         "evidences": ["legislating-the-shift", "work-displaced"],
         "supersedes": [B + "developments/2026-03-31-institutions-as-workarounds"]},
        {"id": "2026-04-07-robot-umpires-draw-applause",
         "title": "Robot umpires are applauded for overturning human calls",
         "claim": "Major League Baseball's robot umpires are drawing applause for overturning "
                  "human calls, while an AI singer held eleven slots in the iTunes top 100 and "
                  "AI-assisted stories drove nearly 20% of one magazine's traffic.",
         "domain": "society",
         "evidences": ["work-displaced", "agent-exclusion"]},
        {"id": "2026-04-07-tech-openings-double-since-2023",
         "title": "Tech job openings double from their 2023 low",
         "claim": "Tech job openings have doubled since mid-2023 to a three-year high and the "
                  "American Enterprise Institute finds 31% of Americans are now upper middle "
                  "class, up from 10% in 1979.",
         "domain": "economics", "actor": ["aei"], "score": "31% vs 10%",
         "evidences": ["growth-without-hiring", "work-displaced"],
         "body": "A counter-signal to the displacement series that the corpus should keep "
                 "alongside the layoffs."},
    ],
}
