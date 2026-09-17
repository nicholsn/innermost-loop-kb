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
        {"id": "architect-labs", "type": "Organization", "title": "Architect Labs",
         "description": "Startup building AI systems that design and provably verify silicon, which "
                        "announced the first AI chip designed end-to-end by AI.",
         "resource": "https://architectlabs.com/",
         "tags": ["startup", "chipmaker"],
         "body": "Architect Labs builds AI systems that design and formally verify chips for modern "
                 "workloads, with the human contribution ending at a high-level specification. In "
                 "this corpus it is the company behind the [Redwood](/hardware/redwood.md) accelerator recorded as "
                 "[a first of authorship rather than assistance](/developments/2026-08-27-a-first-of-authorship-not-assistance.md), "
                 "whose resident model then [found optimizations for its own operations](/developments/2026-08-27-the-loop-reaches-silicon.md), "
                 "and the daily issue's report of "
                 "[the first AI chip designed end-to-end by AI](/developments/2026-08-29-the-first-chip-designed-end-to-end-by-ai.md)."},
        {"id": "earth-species", "type": "Organization", "title": "Earth Species Project"},
        {"id": "mach33-inc", "type": "Organization", "title": "Mach33"},
    ],
    "systems": [
        {"id": "ai-co-scientist", "type": "AISystem", "title": "AI Co-Scientist",
         "description": "Google's Gemini-based multi-agent research system that generates and tests "
                        "scientific hypotheses, and in this corpus designed a reactor route, predicted "
                        "bacterial swarming and invented a model architecture.",
         "developed_by": [B + "organizations/google"],
         "modality": "research agent",
         "resource": "https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/",
         "tags": ["research-agent"],
         "body": "Google's AI co-scientist is a multi-agent system built on Gemini that generates, "
                 "debates and ranks scientific hypotheses and proposes the experiments to test them "
                 "([Google Research](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)). "
                 "The corpus first records it in May, when Google "
                 "[tied it into a single science stack](/developments/2026-05-20-gemini-for-science.md) "
                 "with evolutionary search and notebooks; in August it "
                 "[designed a reactor route, predicted bacterial swarming and invented an architecture beating six frontier models](/developments/2026-08-29-a-co-scientist-invents-an-architecture-beating-six-models.md), "
                 "in the same issue in which Anthropic's "
                 "[Model Hardware Standard](/developments/2026-08-29-a-standard-that-lets-agents-drive-instruments.md) "
                 "gave such agents control of laboratory instruments."},
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
         "description": "Science becomes an agentic loop in the author's framing: one research agent "
                        "spans materials, microbiology and machine-learning design, and the last of "
                        "the three feeds back into the models that run it.",
         "domain": "science", "actor": ["google"],
         "about": [B + "systems/ai-co-scientist"],
         "score": "beats six frontier models",
         "occurred_on": "2026-08-27",
         "evidences": ["automated-science", "research-taste-trained", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-08-23-research-taste-trained-by-reinforcement-learning",
                        B + "developments/2026-05-20-gemini-for-science"],
         "relatedTo": [B + "developments/2026-08-16-an-ai-scientist-beats-far-larger-models",
                       B + "developments/2026-02-08-alphaevolve-finds-new-activations",
                       B + "developments/2026-08-05-a-company-founded-to-automate-the-scientific-method"],
         "tags": ["autonomous-research", "ai-r-and-d", "rsi"],
         "supporting_text": "invented an architecture beating six frontier models",
         "sources": [{"id": "google-co-scientist-real-world-arxiv",
                      "resource": "https://arxiv.org/abs/2608.26701",
                      "title": "Accelerating Scientific Research with Gemini in the Real-World",
                      "author": "org:google", "last_modified": "2026-08-27"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Google's paper *Accelerating Scientific Research with Gemini in the Real-World* "
                 "([arXiv:2608.26701](https://arxiv.org/abs/2608.26701), submitted 27 August 2026) "
                 "reports the [AI Co-Scientist](/systems/ai-co-scientist.md) working across three "
                 "domains: it designed a safe precursor route for MXene nanomaterials that was run "
                 "on a real deposition reactor, predicted E. coli swarming that matched wet-lab data "
                 "not yet published, and proposed a machine-learning architecture that outperformed "
                 "six frontier models. The third result is the one that closes the loop, since a "
                 "research agent inventing a better architecture is "
                 "[recursive self-improvement](/themes/recursive-self-improvement.md) applied to "
                 "the field that builds it. It follows the May report that Google "
                 "[tied the co-scientist into one science stack](/developments/2026-05-20-gemini-for-science.md) "
                 "and Inherent's Faraday, "
                 "[trained for research taste](/developments/2026-08-23-research-taste-trained-by-reinforcement-learning.md); "
                 "the same issue records Anthropic's "
                 "[Model Hardware Standard](/developments/2026-08-29-a-standard-that-lets-agents-drive-instruments.md) "
                 "giving such agents hands on microscopes and robot arms."},
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
         "description": "Silicon enters the loop as the state tightens its grip on it: the author "
                        "pairs a startup's autonomously designed chip with Washington's tariffs and "
                        "remote-access rule as the two forces now shaping compute.",
         "domain": "compute", "actor": ["architect-labs", "white-house", "china"],
         "about": [B + "hardware/redwood"],
         "evidences": ["silicon-designs-itself", "recursive-self-improvement", "the-cuda-moat-is-dead"],
         "supersedes": [B + "developments/2026-08-27-an-inference-chip-beats-every-incumbent-tested",
                        B + "developments/2026-08-27-a-first-of-authorship-not-assistance"],
         "relatedTo": [B + "developments/2026-08-27-the-loop-reaches-silicon",
                       B + "developments/2026-03-20-cpu-designed-in-twelve-hours",
                       B + "developments/2026-07-17-an-open-model-autonomously-designs-a-chip"],
         "tags": ["chip-design", "rsi", "policy"],
         "supporting_text": "the first AI chip designed end-to-end by AI",
         "sources": [{"id": "wissner-gross-architect-labs-chip-x",
                      "resource": "https://x.com/alexwg/status/2093039869887119567",
                      "title": "Alex Wissner-Gross on X: Architect Labs announces the first AI chip "
                               "designed end-to-end by AI",
                      "author": "human:alex-wissner-gross"},
                     {"id": "cnbc-trump-semiconductor-tariffs",
                      "resource": "https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html",
                      "title": "CNBC: Trump weighs new semiconductor and tech tariffs",
                      "author": "org:cnbc", "last_modified": "2026-08-27"},
                     {"id": "information-china-remote-chip-access-rule",
                      "resource": "https://www.theinformation.com/articles/trump-administration-working-ai-rule-curb-chinas-remote-access-chips",
                      "title": "The Information: Trump administration working on AI rule to curb "
                               "China's remote access to chips",
                      "author": "org:the-information"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The announcement, relayed by the newsletter's author on X "
                 "([post](https://x.com/alexwg/status/2093039869887119567)), is the public version "
                 "of the [Redwood](/hardware/redwood.md) accelerator that the corpus's feature recorded two days earlier as "
                 "[a first of authorship rather than assistance](/developments/2026-08-27-a-first-of-authorship-not-assistance.md): "
                 "designed, verified and deployed by an AI system from a human-written "
                 "specification, after which the model running on it "
                 "[found optimizations for its own operations](/developments/2026-08-27-the-loop-reaches-silicon.md). "
                 "[Architect Labs](/organizations/architect-labs.md) describes itself as building "
                 "AI systems that design and provably verify silicon. The issue sets the milestone "
                 "against Washington's "
                 "[proposed semiconductor tariffs](https://www.cnbc.com/2026/08/27/trump-semiconductor-tech-tariffs.html) "
                 "and a [rule curbing China's remote access to chips](https://www.theinformation.com/articles/trump-administration-working-ai-rule-curb-chinas-remote-access-chips), "
                 "the state tightening its hold on compute as its design leaves human hands. In the "
                 "[silicon-designs-itself](/themes/silicon-designs-itself.md) storyline it follows "
                 "Verkor's [twelve-hour CPU](/developments/2026-03-20-cpu-designed-in-twelve-hours.md), "
                 "Kimi K3's [autonomous chip design](/developments/2026-07-17-an-open-model-autonomously-designs-a-chip.md) "
                 "and OpenAI's [Jalapeño inference chip](/developments/2026-08-27-an-inference-chip-beats-every-incumbent-tested.md)."},
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
