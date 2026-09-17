"""Issue 194 — 2026-08-29. The corporate divorce arc."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-29-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-29", "title": "Welcome to August 29, 2026", "url": URL,
        "thesis": "A supplier cuts off a rival's subsidiary and neutral infrastructure ends.",
        "body": """
# Welcome to August 29, 2026

OpenAI notified SpaceX it will wind down Cursor's model access, citing Musk
companies' record of breaking contracts. Cursor's response names what broke: it
had trusted that platform to be neutral infrastructure for its business.

Anthropic answered within hours, pledging more compute. One reading: compute in
space is now the whole game.
""",
    },
    "themes": [
        {"id": "no-neutral-infrastructure", "type": "Theme",
         "title": "The platform picks sides",
         "first_seen": "2026-08-29", "domain": "economics",
         "body": "Model access was assumed to be a utility: metered, neutral, "
                 "available. A supplier cutting off a customer over its parent's "
                 "conduct ends that assumption, and every company building on someone "
                 "else's weights recalculates."},
    ],
    "organizations": [
        {"id": "architect-labs", "type": "Organization", "title": "Architect Labs"},
        {"id": "earth-species", "type": "Organization", "title": "Earth Species Project"},
        {"id": "mach33-inc", "type": "Organization", "title": "Mach33"},
    ],
    "developments": [
        {"id": "2026-08-29-neutral-infrastructure-ends",
         "title": "A model supplier cuts off a rival's newly acquired subsidiary",
         "claim": "OpenAI notified SpaceX it will wind down Cursor's model access by November 12, "
                  "citing Musk companies' record of breaking contracts, with Cursor's chief "
                  "executive responding that OpenAI serves about 5% of its traffic and that it "
                  "had trusted that platform to be neutral infrastructure for its business, while "
                  "Anthropic answered within hours pledging more compute.",
         "domain": "economics", "actor": ["openai", "spacex", "anysphere", "anthropic"],
         "evidences": ["no-neutral-infrastructure", "coordination-tax", "own-your-own-weights"],
         "supersedes": [B + "developments/2026-08-27-a-crm-placed-inside-a-model"]},
        {"id": "2026-08-29-agi-may-arrive-this-year",
         "title": "A chief executive says AGI may arrive this year as the next model previews",
         "claim": "After two weeks inside OpenAI, a reporter recounted Sam Altman saying AGI may "
                  "arrive this year as the lab previewed its next model, with Codex becoming a "
                  "persistent agent that runs until put to sleep.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["takeoff-declared", "the-persistent-colleague", "r-and-d-evals-saturated"],
         "supersedes": [B + "developments/2026-08-19-what-is-paused-is-the-export-not-the-engine"]},
        {"id": "2026-08-29-weights-released-under-a-screening-license",
         "title": "Open weights ship under a license that security-screens large hosts",
         "claim": "Z.ai released GLM-5.3's weights after a two-week safety hold, trading MIT terms "
                  "for a license that security-screens $10 billion hosts, apt after it topped "
                  "CyberGym with 2,436 vulnerabilities found.",
         "domain": "models", "actor": ["zai"], "score": "2,436 vulnerabilities",
         "evidences": ["open-weights-take-the-crown", "speed-of-containment", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-08-27-a-stealth-model-unmasked-on-chinese-chips"]},
        {"id": "2026-08-29-fifty-four-of-fifty-seven-models-in-one-quadrant",
         "title": "A political compass lands 54 of 57 models in the same quadrant",
         "claim": "A new AI Political Compass tested 57 models, landed 54 in the left-libertarian "
                  "quadrant with the Grok family excepted, and found answers built on "
                  "near-universal premises sit there 19 times in 20.",
         "domain": "models", "actor": ["xai"], "score": "54 of 57",
         "evidences": ["values-negotiated-with-the-model", "monoculture-is-the-vulnerability"],
         "supersedes": [B + "developments/2026-08-16-prompts-that-read-as-female-get-worse-answers"]},
        {"id": "2026-08-29-a-co-scientist-invents-an-architecture-beating-six-models",
         "title": "A co-scientist designs a reactor route and invents a winning architecture",
         "claim": "Google's Co-Scientist designed a safe precursor route for MXene nanomaterials "
                  "on a real deposition reactor, predicted bacterial swarming matching unpublished "
                  "wet-lab data, and invented an architecture beating six frontier models.",
         "domain": "science", "actor": ["google"],
         "evidences": ["automated-science", "research-taste-trained", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-08-23-research-taste-trained-by-reinforcement-learning"]},
        {"id": "2026-08-29-a-standard-that-lets-agents-drive-instruments",
         "title": "A hardware standard lets agents drive microscopes and robot arms",
         "claim": "Anthropic previewed the Model Hardware Standard, letting agents drive "
                  "microscopes and robot arms with integrations falling from weeks to hours.",
         "domain": "agents", "actor": ["anthropic"], "score": "weeks to hours",
         "evidences": ["physical-recursion", "automated-science", "agent-society"],
         "supersedes": [B + "developments/2026-08-29-a-co-scientist-invents-an-architecture-beating-six-models"]},
        {"id": "2026-08-29-national-security-is-not-a-blank-check",
         "title": "A judge blocks a defense blacklisting as retaliation against a critic",
         "claim": "A judge blocked the Pentagon's blacklisting of Anthropic, ruling that national "
                  "security is not a blank check to punish and retaliate against government "
                  "critics, while Texas paused funding for license-plate cameras ahead of a $30 "
                  "million surveillance exposé.",
         "domain": "policy", "actor": ["pentagon", "anthropic", "flock-os"],
         "evidences": ["models-as-munitions", "legislating-the-shift", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-08-23-a-lab-asks-for-its-own-leash"]},
        {"id": "2026-08-29-the-first-chip-designed-end-to-end-by-ai",
         "title": "A company announces the first AI chip designed end to end by AI",
         "claim": "Architect Labs announced the first AI chip designed end-to-end by AI, just as "
                  "Washington weighed new semiconductor tariffs and a rule curbing China's remote "
                  "chip access.",
         "domain": "compute", "actor": ["architect-labs", "white-house", "china"],
         "evidences": ["silicon-designs-itself", "recursive-self-improvement", "the-cuda-moat-is-dead"],
         "supersedes": [B + "developments/2026-08-27-an-inference-chip-beats-every-incumbent-tested"]},
        {"id": "2026-08-29-fifteen-gigawatts-that-cannot-be-switched-on",
         "title": "A founder warns 15 gigawatts of 2027 compute cannot be switched on in 2027",
         "claim": "Musk warned roughly 15 gigawatts of 2027 compute cannot be switched on in 2027 "
                  "because power is scarcer than logic, so SpaceX is building its own "
                  "turbine-blade factory, while Germany vowed to quadruple compute by 2030 and "
                  "unions defended data centers to defend jobs.",
         "domain": "energy", "actor": ["spacex", "european-union"], "score": "~15 GW shortfall",
         "evidences": ["thread-lines", "infrastructure-crowding-out", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-08-25-batteries-stuck-in-queues-for-want-of-transformers"]},
        {"id": "2026-08-29-a-national-emergency-over-foreign-grid-gear",
         "title": "A national emergency bars risky foreign grid equipment",
         "claim": "Washington declared a national emergency barring risky foreign grid gear "
                  "against AI-magnified sabotage risk and signed what it called the biggest oil "
                  "deal in world history, while a social platform exposed a 200,000-account bot "
                  "farm claiming data centers inflate household power bills.",
         "domain": "policy", "actor": ["white-house"], "score": "200,000 accounts",
         "evidences": ["war-reaches-the-cloud", "politics-as-infrastructure", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-08-25-thread-lines-ration-intelligence"]},
        {"id": "2026-08-29-a-nuclear-powered-mars-ship-for-2028",
         "title": "A president announces a nuclear-powered Mars ship and a space academy",
         "claim": "The President announced a nuclear-powered Mars ship for 2028, promising a "
                  "massive American star fleet, and chartered a United States Space Academy to "
                  "crew it, while a consultancy's propellant math behind a $100 billion coastal "
                  "campus earned a mostly correct from Musk.",
         "domain": "space", "actor": ["white-house", "spacex", "mach33-inc"],
         "evidences": ["orbit-as-compute", "science-as-industrial-policy", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-08-27-a-hundred-billion-dollar-second-spaceport"]},
        {"id": "2026-08-29-a-jurassic-soundscape-reconstructed",
         "title": "A Jurassic soundscape is reconstructed from 165-million-year-old wings",
         "claim": "Researchers reconstructed a Jurassic soundscape from 165-million-year-old "
                  "insect wings, recovering ultrasonic calls from eons before bats, while a "
                  "project decoded vocalizations across 9,000 bird species.",
         "domain": "science", "actor": ["earth-species"], "score": "9,000 species",
         "evidences": ["resurrection-and-time", "biosphere-uplift", "automated-science"],
         "supersedes": [B + "developments/2026-08-25-warp-visitors-arrive-quietly-or-not-at-all"]},
    ],
}
