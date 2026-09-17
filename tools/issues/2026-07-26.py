"""Issue 174 — 2026-07-26. The hiring plan is the roadmap."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-26-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-26", "title": "Welcome to July 26, 2026", "url": URL,
        "thesis": "The job listings are a public AGI roadmap.",
        "body": """
# Welcome to July 26, 2026

All 1,171 job listings at OpenAI and Anthropic read like a public AGI roadmap:
AI-designed chips, simulated universes, and staff hired specifically to measure
when the loop accelerates.

Claude Opus 5 landed at Fable-class intelligence for half the price, taking
ARC-AGI-3 at 30.2%, quadruple the old best, after turning puzzle layouts into
reflection equations.
""",
    },
    "themes": [
        {"id": "hiring-as-roadmap", "type": "Theme",
         "title": "The job board discloses the plan",
         "first_seen": "2026-07-26", "domain": "models",
         "body": "Labs that decline to publish timelines publish job listings instead. "
                 "Roles for measuring when the loop accelerates are a commitment that "
                 "no blog post makes, because someone has to be paid to do it."},
    ],
    "organizations": [
        {"id": "arc-prize-org", "type": "Organization", "title": "ARC Prize Foundation"},
    ],
    "people": [
        {"id": "logan-kilpatrick", "type": "Person", "title": "Logan Kilpatrick", "name": "Logan Kilpatrick",
         "description": "American software engineer whom the newsletter consistently identifies as Google's, a recurring forecaster in the corpus, here predicting that automating AI research will come to look like data cleaning.",
         "resource": "https://x.com/officiallogank",
         "sameAs": ["http://www.wikidata.org/entity/Q134580710"],
         "tags": ["researcher"],
         "body": "Logan Kilpatrick appears in the corpus as 'Google's Logan Kilpatrick'; his own [X profile](https://x.com/officiallogank) "
                 "describes him as a member of technical staff working on Gemini, Google AI Studio, the Gemini API and Kaggle. "
                 "He is a serial forecaster of "
                 "the loop: he suggested [superintelligence would arrive as existing weights unlocked by scaffolding](/developments/2025-12-12-kilpatrick-scaffolding-endgame.md), "
                 "called [2026 the year of embodied AI](/developments/2025-12-22-kilpatrick-2026-embodied.md), warned that "
                 "[the compute gap grows daily](/developments/2026-02-26-compute-gap-grows-daily.md) and "
                 "[posted then deleted a robotics claim](/developments/2026-03-23-deleted-post-about-a-robotics-breakthrough.md). "
                 "In the recursive-self-improvement cluster he supplies the prediction, beside the labs' "
                 "[job listings read as a roadmap](/developments/2026-07-26-the-job-board-is-the-roadmap.md), that "
                 "automating AI research will come to look like data cleaning."},
    ],
    "developments": [
        {"id": "2026-07-26-a-quadrupled-score-on-the-hardest-benchmark",
         "title": "A model quadruples the best score on the hardest reasoning benchmark",
         "claim": "Claude Opus 5 landed at Fable-class intelligence for half the price, sweeping "
                  "Frontier-Bench, GDPval and Humanity's Last Exam, and ARC Prize crowned it "
                  "state of the art on ARC-AGI-3 at 30.2%, quadruple the old best, after it "
                  "turned puzzle layouts into reflection equations for the first time.",
         "domain": "benchmarks", "actor": ["anthropic", "arc-prize"], "score": "30.2%, 4x prior",
         "evidences": ["price-implosion", "benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-07-24-six-erdos-problems-in-one-sitting"],
         "body": "One dissent: on held-out novel puzzle games the leap evaporates, "
                 "since evaluations stay held-out only until someone optimizes the "
                 "genre."},
        {"id": "2026-07-26-eighty-percent-of-a-system-prompt-deleted",
         "title": "A lab deletes 80% of its agent's system prompt",
         "claim": "Anthropic deleted 80% of Claude Code's system prompt, as the new models thrive "
                  "on judgment over rules, while the system card rated Opus 5 the most aligned "
                  "Claude yet — sharp at finding vulnerabilities, dull at weaponizing them.",
         "domain": "agents", "actor": ["anthropic"], "score": "-80% of prompt",
         "evidences": ["scaffolding-over-weights", "behavior-unlocks-intelligence", "alignment-as-moat"],
         "supersedes": [B + "developments/2026-07-26-a-quadrupled-score-on-the-hardest-benchmark"]},
        {"id": "2026-07-26-the-job-board-is-the-roadmap",
         "title": "Over a thousand job listings read as a public AGI roadmap",
         "claim": "All 1,171 job listings at OpenAI and Anthropic read like a public AGI roadmap, "
                  "covering AI-designed chips, simulated universes and staff to measure when the "
                  "loop accelerates, while Logan Kilpatrick predicted automating AI research will "
                  "come to look like data cleaning.",
         "description": "Labs that decline to publish timelines publish job listings instead, and "
                        "paying staff to measure when the loop accelerates is a commitment no blog "
                        "post makes: the newsletter's case that the hiring plan is the disclosed plan.",
         "domain": "models", "actor": ["openai", "anthropic", "people/logan-kilpatrick"], "score": "1,171 listings",
         "evidences": ["hiring-as-roadmap", "recursive-self-improvement", "a-model-trains-a-model"],
         "supersedes": [B + "developments/2026-07-24-an-ai-kill-switch-act",
                        B + "developments/2026-06-01-a-lab-starts-hiring-for-robots"],
         "relatedTo": [B + "developments/2026-05-20-karpathy-joins-to-lead-pretraining",
                       B + "developments/2026-07-19-we-want-k2-to-help-build-k3",
                       B + "people/roon"],
         "tags": ["rsi", "ai-r-and-d", "labor", "forecast"],
         "supporting_text": "read like a public AGI roadmap",
         "sources": [{"id": "openai-anthropic-job-listings-roadmap",
                      "resource": "https://x.com/imjustnewatai/status/2081221459226034524",
                      "title": "All 1,171 job listings at OpenAI and Anthropic, read as an AGI roadmap"},
                     {"id": "kilpatrick-ai-research-as-data-cleaning",
                      "resource": "https://x.com/officiallogank/status/2081117440990404649",
                      "title": "Automating AI research will look like data cleaning",
                      "author": "human:logan-kilpatrick"},
                     {"id": "roon-magic-slowdown-button",
                      "resource": "https://x.com/tszzl/status/2081122092096065771",
                      "title": "Roon on pressing a magic slowdown button", "author": "human:roon"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "A reading of [all 1,171 open roles at OpenAI and Anthropic](https://x.com/imjustnewatai/status/2081221459226034524) "
                 "found the labs advertising for AI-designed chips, simulated universes and staff whose job is to "
                 "measure when the loop accelerates, a roadmap disclosed through payroll rather than a blog post. "
                 "Beside it [Logan Kilpatrick](/people/logan-kilpatrick.md) "
                 "[predicted](https://x.com/officiallogank/status/2081117440990404649) that automating AI research "
                 "will come to look like data cleaning, [Elon Musk](/people/elon-musk.md) replied 'So true', and "
                 "[Roon](/people/roon.md) [admitted](https://x.com/tszzl/status/2081122092096065771) he would press a "
                 "magic slowdown button if one existed, even as alignment researchers work like 'many armed deities'. "
                 "It belongs to the [hiring-as-roadmap](/themes/hiring-as-roadmap.md) strand of the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory: "
                 "[Karpathy's move to lead pre-training](/developments/2026-05-20-karpathy-joins-to-lead-pretraining.md) "
                 "gave the loop a job title and [OpenAI Robotics' hiring call](/developments/2026-06-01-a-lab-starts-hiring-for-robots.md) "
                 "a headcount, while a week earlier Moonshot's chief executive had said the same plan out loud as "
                 "[K2 helping to build K3](/developments/2026-07-19-we-want-k2-to-help-build-k3.md). The same issue's "
                 "[Claude Opus 5 system card](/developments/2026-07-26-eighty-percent-of-a-system-prompt-deleted.md) "
                 "rated the model below the automated-R&D red line, the threshold the newly advertised measurement "
                 "staff exist to watch."},
        {"id": "2026-07-26-twenty-firms-urge-against-open-weight-restrictions",
         "title": "Twenty-plus firms urge policymakers against restricting open weights",
         "claim": "Nvidia, Microsoft, Meta, Palantir and more than twenty other firms urged "
                  "policymakers against premature restrictions on open weights, with Nvidia's "
                  "letter likening it to the 1980s open-source fight, while the two "
                  "trillion-dollar holdouts sat out.",
         "domain": "policy", "actor": ["nvidia", "microsoft", "meta", "palantir"],
         "evidences": ["open-weights-take-the-crown", "pegged-to-the-rival", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-23-two-hundred-startups-beg-washington-not-to-cut-off-open-models"]},
        {"id": "2026-07-26-an-android-play-against-pax-silica",
         "title": "A leader pitches free models to the global south as an Android play",
         "claim": "Xi pitched the global south free Chinese models plus a 29-member cooperation "
                  "bloc, an Android play against America's Pax Silica, as a joint UK-US audit of "
                  "Kimi K3 found it trailing US frontiers on cyber with safeguards that never "
                  "said no.",
         "domain": "policy", "actor": ["china", "moonshot-ai", "uk-aisi"], "score": "29 members",
         "evidences": ["silicon-curtain", "open-weights-take-the-crown", "refusal-as-outage"],
         "supersedes": [B + "developments/2026-07-26-twenty-firms-urge-against-open-weight-restrictions"]},
        {"id": "2026-07-26-a-lab-polices-its-own-users-before-any-law",
         "title": "A lab's monitors catch and suspend users probing for weapon recipes",
         "claim": "When hundreds of users probed ChatGPT for bioweapon and poison recipes and "
                  "some answers slipped through, OpenAI's own monitors caught and suspended them, "
                  "self-policing ahead of any law requiring it, while universities ditched AI "
                  "detectors over false positives and rebuilt assessment around orals.",
         "domain": "policy", "actor": ["openai"],
         "evidences": ["ethics-tracks-detectability", "deskilling", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-24-an-ai-kill-switch-act"]},
        {"id": "2026-07-26-a-lab-asks-a-memory-maker-for-its-own-chips",
         "title": "A lab asks a memory maker to supply its own chip effort",
         "claim": "Anthropic asked SK Hynix for supplies to make its own chips, startling SK's "
                  "chairman, as Nvidia put $1 billion into Naver and unveiled a $500 billion "
                  "Korean push spanning HBM4 and two-gigawatt data centers, and Samsung inked a "
                  "$200 billion pact with Broadcom.",
         "domain": "compute", "actor": ["anthropic", "sk-hynix", "nvidia", "samsung", "broadcom"],
         "score": "$500B / $200B",
         "evidences": ["vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-07-24-rivals-split-inference-between-racks-and-wafers"]},
        {"id": "2026-07-26-a-model-flies-a-drone-better-than-the-baseline",
         "title": "A model flies a $129 drone to find and follow a person",
         "claim": "On Drone-Bench, Fable 5 flew a $129 drone to find and follow a person, beating "
                  "the human-AI baseline, with only 3D reconstruction left to solve after it "
                  "mistook one wall for a doorway.",
         "domain": "robotics", "actor": ["anthropic"], "score": "$129 drone",
         "evidences": ["physical-recursion", "world-models-beat-vlas"],
         "supersedes": [B + "developments/2026-07-24-an-ai-agent-flies-a-live-f-16"]},
        {"id": "2026-07-26-a-union-vows-no-robot-enters-without-a-deal",
         "title": "A union vows no robot enters the plant without a deal",
         "claim": "Hyundai denied its 25,000-humanoid plan sparked strikes, though the union "
                  "vowed no robot enters without a deal, as support for nearby data centers "
                  "cratered to 27%.",
         "domain": "robotics", "actor": ["hyundai"], "score": "25,000 humanoids / 27% support",
         "evidences": ["work-displaced", "infrastructure-crowding-out", "physical-recursion"],
         "supersedes": [B + "developments/2026-07-16-a-humanoid-shuts-a-car-factory"]},
        {"id": "2026-07-26-ninety-percent-of-transuranics-stripped-in-a-day",
         "title": "A validated process strips 90% of long-lived waste from spent fuel in a day",
         "claim": "A validated Canadian process strips 90% of long-lived transuranics from spent "
                  "nuclear fuel in 24 hours, leaving reactor feedstock.",
         "domain": "energy", "score": "90% in 24 hours",
         "evidences": ["industrialized-nature", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-07-24-a-first-certificate-for-wave-energy"]},
        {"id": "2026-07-26-an-exosatellite-strains-the-taxonomy",
         "title": "A first-of-its-kind exosatellite strains planetary taxonomy",
         "claim": "Astronomers found a first-of-its-kind exosatellite 73 light-years out, massive "
                  "enough to be a planet yet orbiting a brown dwarf, straining a taxonomy built "
                  "for our own solar system, while Starship's thirteenth flight deployed 20 "
                  "Starlink V3 satellites and eased into a soft water landing.",
         "domain": "space", "actor": ["spacex"], "score": "73 light-years",
         "evidences": ["inhabitable-worlds", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-07-24-a-robotic-servicer-extends-satellite-lives"]},
        {"id": "2026-07-26-a-hundred-forty-thousand-jobs-shed-as-capex-hits-seven-hundred-billion",
         "title": "US tech sheds 140,000 jobs as hyperscalers commit $725 billion",
         "claim": "US tech has shed 140,000 jobs this year even as hyperscalers committed $725 "
                  "billion to data centers, with proposals to spread the gains running from "
                  "public ownership of half of AI to zero income tax for the bottom half.",
         "domain": "economics", "score": "-140,000 jobs / $725B capex",
         "evidences": ["work-displaced", "post-labor-instruments", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-07-24-a-lab-shutters-its-agi-unit-as-a-stake-swells"]},
    ],
}
