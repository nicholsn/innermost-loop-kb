"""Issue 158 — 2026-07-08. Outrun before the launch week ends."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-8-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-08", "title": "Welcome to July 8, 2026", "url": URL,
        "thesis": "The turn itself becomes the unit under renegotiation.",
        "body": """
# Welcome to July 8, 2026

GPT-5.6 ships globally after Commerce cleared it, lifting the same restrictions
once placed on Mythos and Fable. The early verdict was capable but outmatched:
if a single Fable turn does the work of ten from Sol, the turn itself is the
unit being renegotiated.

A developer released a Self-Improvement Loops skill for meta-harnesses that
rewrite their own scaffolding, warning that the loop will optimize whatever
signal you give it.
""",
    },
    "organizations": [
        {"id": "d-matrix", "type": "Organization", "title": "d-Matrix"},
        {"id": "wurzburg", "type": "Organization", "title": "University of Würzburg"},
    ],
    "developments": [
        {"id": "2026-07-08-a-model-clears-review-and-ships-globally",
         "title": "A model clears federal testing and ships worldwide with preview access",
         "claim": "OpenAI shipped GPT-5.6 Sol, Terra and Luna with preview access going global "
                  "immediately, after Commerce cleared the broad launch following CAISI testing "
                  "and lifted the same restrictions once placed on Mythos and Fable, with Sol "
                  "streaming at 750 tokens per second.",
         "domain": "models", "actor": ["openai", "white-house", "cerebras"], "score": "750 tok/s",
         "evidences": ["clearance-as-bottleneck", "models-as-munitions", "public-internal-divergence"],
         "supersedes": [B + "developments/2026-07-04-there-will-not-be-an-fda-for-ai"]},
        {"id": "2026-07-08-the-turn-becomes-the-unit-under-renegotiation",
         "title": "A rival's single turn is said to do the work of ten",
         "claim": "Reviewers judged the new model capable but outmatched, with one finding Fable "
                  "quite a bit better and more agentic and another watching Sol run a day without "
                  "a goal while orchestrating subagents, so that if one Fable turn does the work "
                  "of ten from Sol, the turn itself is the unit under renegotiation.",
         "domain": "models", "actor": ["openai", "anthropic"],
         "evidences": ["intelligence-per-watt", "spiky-frontier", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-07-08-a-model-clears-review-and-ships-globally"]},
        {"id": "2026-07-08-a-model-finds-bugs-in-a-rivals-code",
         "title": "A model finds edge-case bugs in a rival model's own code",
         "claim": "A reviewer flagged the new model finding edge-case bugs in Fable's own code, "
                  "as OpenAI shipped a bi-directional ChatGPT voice that abandons turn-taking "
                  "altogether.",
         "domain": "models", "actor": ["openai", "anthropic"],
         "evidences": ["models-audit-their-benchmarks", "intimate-interface"],
         "supersedes": [B + "developments/2026-07-08-the-turn-becomes-the-unit-under-renegotiation"]},
        {"id": "2026-07-08-the-transformer-eulogized",
         "title": "A researcher begins eulogizing the transformer",
         "claim": "SpaceXAI and Cursor are shipping a joint efficiency model tuned to rival Opus "
                  "4.8, while OpenAI's Jerry Tworek began eulogizing the transformer as a prelude "
                  "to its successor, on the argument that intelligence is just compression.",
         "domain": "models", "actor": ["spacex", "anysphere", "openai"],
         "evidences": ["architecture-of-mind", "intelligence-per-watt"],
         "supersedes": [B + "developments/2026-07-05-a-ten-thousand-parameter-conductor-beats-every-model"]},
        {"id": "2026-07-08-every-public-profile-opted-in",
         "title": "A platform opts every public profile into likeness-based generation",
         "claim": "Meta opted every public Instagram profile into likeness-based image "
                  "generation, making opting out the user's own homework.",
         "domain": "society", "actor": ["meta"],
         "evidences": ["humans-as-peripherals", "intimate-interface", "data-beyond-text"],
         "supersedes": [B + "developments/2026-07-07-synthetic-friendship-switched-off"]},
        {"id": "2026-07-08-the-loop-optimizes-whatever-signal-you-give-it",
         "title": "A skill ships for meta-harnesses that rewrite their own scaffolding",
         "claim": "A developer released a Self-Improvement Loops skill for meta-harnesses that "
                  "rewrite their own scaffolding, warning that the loop will optimize whatever "
                  "signal you give it, while Anthropic extended Claude Cowork to web and mobile, "
                  "running tasks in the background and surfacing only decisions needing approval.",
         "description": "The self-rewriting harness leaves the research paper and becomes an "
                        "installable skill, and its author's warning names the failure mode any "
                        "such loop inherits from its reward signal.",
         "domain": "agents", "actor": ["anthropic"],
         "about": [B + "systems/claude-cowork"],
         "evidences": ["self-authored-scaffolding", "recursive-self-improvement",
                       "ethics-tracks-detectability", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-07-05-accountability-as-the-only-value-left"],
         "relatedTo": [B + "developments/2026-05-13-agents-write-their-own-goals",
                       B + "developments/2026-06-24-skills-that-write-themselves",
                       B + "developments/2026-06-25-an-agent-rewrites-its-own-harness",
                       B + "developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less"],
         "tags": ["rsi", "self-modification", "agent-harness"],
         "supporting_text": "the loop will optimize whatever signal you give it",
         "sources": [{"id": "muratcan-self-improvement-loops-skill",
                      "resource": "https://x.com/muratcan/status/2074730841083621377",
                      "title": "Self-Improvement Loops skill for meta-harnesses",
                      "author": "human:muratcan"},
                     {"id": "9to5mac-claude-cowork-web-and-mobile",
                      "resource": "https://9to5mac.com/2026/07/07/anthropic-expanding-claude-cowork-to-mobile-and-web-details-here/",
                      "title": "Anthropic expanding Claude Cowork to mobile and web",
                      "author": "org:9to5mac", "last_modified": "2026-07-07"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "A developer packaged the self-rewriting harness as an installable "
                 "Self-Improvement Loops skill for meta-harnesses, agents whose job is to rewrite "
                 "the scaffolding of other agents, and shipped it with the caveat that the loop "
                 "will optimize whatever signal you give it "
                 "([announcement](https://x.com/muratcan/status/2074730841083621377)). In the "
                 "same issue Anthropic pushed [Claude Cowork](/systems/claude-cowork.md) to web "
                 "and mobile, running tasks in the background and surfacing only the decisions "
                 "that need approval "
                 "([9to5Mac](https://9to5mac.com/2026/07/07/anthropic-expanding-claude-cowork-to-mobile-and-web-details-here/)). "
                 "The skill productizes the "
                 "[Self-Harness paradigm](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md) "
                 "of two weeks earlier and sits beside users "
                 "[metaprompting an agent to write its own goals](/developments/2026-05-13-agents-write-their-own-goals.md); "
                 "the warning is answered a week later when Weco's outer loop scores its inner "
                 "researcher on a "
                 "[hidden metric it cannot game](/developments/2026-07-15-a-hidden-metric-teaches-an-agent-to-cheat-less.md) "
                 "and reward hacking falls."},
        {"id": "2026-07-08-cognitive-load-time-density",
         "title": "Only high-stakes ambiguity is left, so the load per hour rises",
         "claim": "Yishan Wong noted that once machines do every lower task only high-stakes "
                  "ambiguity remains, so cognitive load time density now demands a chief "
                  "executive's monastic exercise regime.",
         "domain": "society",
         "evidences": ["cognitive-load-inverted", "botsitting", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-07-03-participation-at-a-fifty-year-low"]},
        {"id": "2026-07-08-one-division-out-earns-forty-years",
         "title": "A chip division's year beats everything it earned across four decades",
         "claim": "Samsung's chip chief told staff 2026 profit will beat everything the division "
                  "earned across 40 years, putting the company on track to overtake Nvidia as "
                  "tech's most profitable firm for the quarter, while CPUs became the new "
                  "battleground and Nvidia hedged by partnering with rivals.",
         "domain": "economics", "actor": ["samsung", "nvidia", "d-matrix"], "score": ">40 years of profit",
         "evidences": ["ai-as-the-economy", "vertical-silicon", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-07-07-a-twenty-year-lease-reincarnates-a-bitcoin-miner"]},
        {"id": "2026-07-08-a-uranium-free-laser-fusion-pilot",
         "title": "A Nobel laureate unveils a uranium-free laser-fusion plant",
         "claim": "Blue-LED Nobel laureate Shuji Nakamura unveiled a laser-fusion plant aiming "
                  "for a one-gigawatt uranium-free pilot near Santa Barbara by 2032.",
         "domain": "energy", "score": "1 GW by 2032",
         "evidences": ["industrialized-nature", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-07-07-a-fourth-microreactor-and-contracting-gas-demand"]},
        {"id": "2026-07-08-a-driver-facing-camera-in-every-new-car",
         "title": "A bloc mandates a driver-facing distraction camera in every new car",
         "claim": "The EU now mandates a driver-facing distraction camera in every new car with "
                  "murky rules on retention, a Waymo reported two teens for underage drinking "
                  "leading to an arrest, and Meta's smart glasses will disable their camera "
                  "entirely if the capture light is tampered with.",
         "domain": "policy", "actor": ["european-union", "waymo", "meta"],
         "evidences": ["agent-society", "humans-as-peripherals", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-07-08-every-public-profile-opted-in"]},
        {"id": "2026-07-08-rockets-become-a-cost-center",
         "title": "A bank values a launch business at 3% of its parent",
         "claim": "Morgan Stanley pegged SpaceX's launch business at just $8 a share, barely 3% "
                  "of the company's value even as launch costs fell 99% and margins swung from "
                  "negative 50% to positive 40%, because rockets have become the on-ramp to the "
                  "orbital economy rather than the prize.",
         "domain": "space", "actor": ["morgan-stanley", "spacex"], "score": "3% of value",
         "evidences": ["orbit-as-compute", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-07-07-a-lab-dissolves-into-its-mothership"]},
        {"id": "2026-07-08-silent-speech-read-from-the-tongue",
         "title": "A model reads silent speech from ultrasound of the tongue",
         "claim": "Aleph trained a model to read silent speech from ultrasound of the tongue at a "
                  "15.6% error rate after just 50 hours of data, while Würzburg researchers found "
                  "the ants that amputate injured nestmates' legs are not specialist surgeons but "
                  "foragers in transition, with care falling to whoever is socially closest.",
         "domain": "biotech", "actor": ["aleph-bio", "wurzburg"], "score": "15.6% error / 50 hrs",
         "evidences": ["intimate-interface", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-07-01-sentences-read-from-the-brain-without-surgery"]},
        {"id": "2026-07-08-an-entire-kingdom-from-a-single-plan",
         "title": "A model conjures a procedural kingdom with economies and lineages from one plan",
         "claim": "Ethan Mollick had Fable conjure an entire procedural fantasy kingdom, with "
                  "economies, trade routes, wars, lineages and occasional dragons, from a single "
                  "plan — every ancestor simulation this cheap to run raising the Bayesian odds "
                  "that our own world is someone else's afternoon project.",
         "domain": "society", "actor": ["anthropic"],
         "evidences": ["inhabitable-worlds", "authoring-minds", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-07-05-four-superconductors-from-twenty-eight-gpu-hours"]},
    ],
}
