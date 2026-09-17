"""Issue 105 — 2026-05-01. Every reward signal breeds a creature."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-1-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-01", "title": "Welcome to May 1, 2026", "url": URL,
        "thesis": "A personality reward leaks into the metaphors and nobody notices for two versions.",
        "body": """
# Welcome to May 1, 2026

OpenAI admitted that from GPT-5.1 onward its models began compulsively summoning
goblins and gremlins into their metaphors — an emergent quirk inherited from
over-rewarding a "Nerdy" personality during reinforcement learning, with GPT-5.5
having started training before the root cause was found.

Yesterday's issue recorded the instructions forbidding the word. This one
records where it came from.
""",
    },
    "organizations": [
        {"id": "huawei", "type": "Organization", "title": "Huawei",
         "resource": "https://www.huawei.com/"},
        {"id": "roze-ai", "type": "Organization", "title": "Roze AI",
         "body": "SoftBank venture deploying autonomous robots to build datacenters."},
        {"id": "dax-robotics", "type": "Organization", "title": "Dax Robotics",
         "body": "Built a ton-class robot horse rated to carry 1,000 kg."},
        {"id": "joby", "type": "Organization", "title": "Joby Aviation",
         "resource": "https://www.jobyaviation.com/"},
        {"id": "colossal", "type": "Organization", "title": "Colossal Biosciences",
         "resource": "https://colossal.com/"},
        {"id": "spotify-co", "type": "Organization", "title": "Spotify",
         "resource": "https://www.spotify.com/"},
    ],
    "developments": [
        {"id": "2026-05-01-a-personality-reward-breeds-goblins",
         "title": "A personality reward leaks goblins into two model generations",
         "claim": "OpenAI admitted that starting with GPT-5.1 its models began compulsively "
                  "summoning goblins, gremlins and other creatures into their metaphors, an "
                  "emergent quirk inherited from over-rewarding a nerdy personality during "
                  "reinforcement learning, with GPT-5.5 having started training before the root "
                  "cause was found.",
         "domain": "models", "actor": ["openai"],
         "evidences": ["warmth-costs-accuracy", "machine-affect", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-04-30-a-bestiary-of-forbidden-words"],
         "body": "Yesterday's issue recorded the ban. This one records the cause."},
        {"id": "2026-05-01-an-early-checkpoint-matches-the-unreleased-frontier",
         "title": "An early checkpoint matches an unreleased rival on cyber tasks",
         "claim": "The UK's AI Security Institute found an early GPT-5.5 checkpoint matched or "
                  "exceeded Anthropic's unreleased Mythos on advanced capture-the-flag "
                  "cybersecurity tasks, while the NSA began testing Mythos to hunt "
                  "vulnerabilities in Microsoft software.",
         "domain": "benchmarks", "actor": ["aisi", "openai", "anthropic"],
         "evidences": ["war-reaches-the-cloud", "spiky-frontier"],
         "supersedes": [B + "developments/2026-04-30-guidance-drafted-to-bypass-its-own-designation"]},
        {"id": "2026-05-01-not-enough-tpus-for-two-frontier-families",
         "title": "Google concedes it lacks the silicon for two frontier model families",
         "claim": "Demis Hassabis admitted Google simply lacks the TPUs to maintain two "
                  "frontier model families simultaneously, explaining why its open models stay "
                  "compact while its flagship takes the silicon.",
         "domain": "models", "actor": ["google", "people/demis-hassabis"],
         "evidences": ["infrastructure-crowding-out", "open-weight-latency"],
         "supersedes": [B + "developments/2026-04-26-google-holds-a-quarter-of-global-compute"]},
        {"id": "2026-05-01-ai-data-stocktakes",
         "title": "DeepMind interviews field experts to map the data blocking discovery",
         "claim": "Google DeepMind began conducting AI data stocktakes, interviewing leading "
                  "experts in each field to map the data obstacles slowing scientific discovery.",
         "domain": "science", "actor": ["google-deepmind"],
         "evidences": ["automated-science", "data-beyond-text"]},
        {"id": "2026-05-01-huawei-takes-chinas-chip-market",
         "title": "Huawei takes the largest share of China's AI chip market",
         "claim": "Huawei is set to capture the largest share of China's AI chip market this "
                  "year with sales jumping 60% as domestic buyers move away from Nvidia, while "
                  "Meta sold another $25 billion of bonds and Intel shares rose 114% in April.",
         "domain": "compute", "actor": ["huawei", "nvidia", "meta", "intel"], "score": "+60% / +114%",
         "evidences": ["silicon-curtain", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-04-26-maine-vetoes-its-own-moratorium"]},
        {"id": "2026-05-01-apple-gives-up-on-the-headset",
         "title": "Apple abandons its headset for display-less glasses",
         "claim": "Apple has reportedly given up on the Vision Pro after an M5 refresh failed to "
                  "revive interest, pivoting to display-less smart glasses because the headset's "
                  "silicon draws too much power for a lighter device.",
         "domain": "compute", "actor": ["apple"],
         "evidences": ["consumer-deprioritized", "intimate-interface"],
         "supersedes": [B + "developments/2026-04-27-openai-designs-phone-silicon"]},
        {"id": "2026-05-01-robots-to-build-the-datacenters",
         "title": "A venture plans a $100B listing before shipping a single robot",
         "claim": "SoftBank is assembling Roze AI to deploy autonomous robots that build data "
                  "centers more efficiently, already eyeing a $100 billion listing before any "
                  "robot has shipped.",
         "domain": "robotics", "actor": ["softbank", "roze-ai"], "score": "$100B",
         "evidences": ["physical-recursion", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-04-30-humanoid-production-scales-24x-in-120-days"]},
        {"id": "2026-05-01-a-ton-class-robot-horse",
         "title": "A robot horse is rated to carry a tonne",
         "claim": "Dax Robotics unveiled a ton-class robot horse rated to carry 1,000 "
                  "kilograms, while Tesla produced the first Semi off its high-volume Nevada "
                  "line and 1X opened a 58,000-square-foot factory targeting 10,000 home "
                  "humanoids this year and 100,000 by the end of 2027.",
         "domain": "robotics", "actor": ["dax-robotics", "tesla", "1x"], "score": "1,000 kg / 100,000 units",
         "evidences": ["physical-recursion", "work-displaced"]},
        {"id": "2026-05-01-an-air-taxi-out-of-jfk",
         "title": "An electric air taxi flies out of JFK to Manhattan in fifteen minutes",
         "claim": "A Joby Aviation prototype completed the first electric air taxi flight out of "
                  "JFK, touching down at a Manhattan heliport fifteen minutes later.",
         "domain": "robotics", "actor": ["joby"], "score": "15 minutes",
         "evidences": ["autonomy-clock-speed", "autonomous-commerce"]},
        {"id": "2026-05-01-resurrecting-an-antelope-extinct-200-years",
         "title": "A company works to resurrect an antelope extinct for two centuries",
         "claim": "Colossal Biosciences revealed it has been quietly working to resurrect the "
                  "bluebuck, an African antelope extinct for 200 years, alongside its mammoth, "
                  "dodo and thylacine projects.",
         "domain": "biotech", "actor": ["colossal"], "score": "200 years",
         "evidences": ["resurrection-and-time", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-04-03-seven-thousand-pets-signed-up-for-cryopreservation"]},
        {"id": "2026-05-01-a-model-outperforms-doctors-on-real-cases",
         "title": "A model beats hundreds of physicians on real clinical cases",
         "claim": "Harvard and Beth Israel researchers pitted a reasoning model against hundreds "
                  "of physicians on real clinical cases and found it outperformed both the "
                  "doctors and older models across diagnosis and management, while DeepMind "
                  "launched an AI co-clinician for supervised care teams.",
         "domain": "biotech", "actor": ["harvard", "google-deepmind"],
         "evidences": ["work-displaced", "automated-science"],
         "supersedes": [B + "developments/2026-04-30-pancreatic-cancer-spotted-475-days-early"]},
        {"id": "2026-05-01-the-median-person-is-screwed",
         "title": "The local consensus converges on the median person being screwed",
         "claim": "A New York Times opinion piece reported that across political leanings, from "
                  "engineers to investors to founders, the San Francisco consensus on AI's "
                  "effect on the workforce has converged on the median person being screwed, "
                  "while a slim majority of Swiss voters backed capping the human population at "
                  "ten million and Spotify began badging living artists.",
         "domain": "society", "actor": ["spotify-co"],
         "evidences": ["work-displaced", "agent-exclusion"],
         "supersedes": [B + "developments/2026-04-30-the-radiologist-paradox"]},
        {"id": "2026-05-01-musk-admits-distillation-under-oath",
         "title": "Musk admits under oath that xAI distilled a rival's models",
         "claim": "In the OpenAI trial, Elon Musk admitted under oath that xAI distilled "
                  "OpenAI's models to train its own, while the judge told his lawyer they would "
                  "not get into issues of catastrophe and extinction, and the Senate "
                  "unanimously banned its members from trading prediction markets.",
         "domain": "policy", "actor": ["xai", "openai", "us-congress"],
         "evidences": ["coordination-tax", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-04-07-labs-share-distillation-intelligence"]},
    ],
}
