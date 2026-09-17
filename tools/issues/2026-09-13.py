"""Issue 202 — 2026-09-13. We must pace the frontier."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-september-13-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-09-13", "title": "Welcome to September 13, 2026", "url": URL,
        "thesis": "The first formal request to slow down comes from the people building it.",
        "body": """
# Welcome to September 13, 2026

Dario Amodei published *We Must Pace the Frontier*, arguing labs should
coordinate on speed and give independent evaluators employee-like access. Within
hours Musk replied "Dario is right," Altman said "I agree with Dario" and
committed to embedded evaluators, and Hassabis called it the right path forward.

The backlash came armed with new terms: an *alignment aristocracy* is what you
get when "no one can be trusted with this" quietly becomes "no one but us."
""",
    },
    "themes": [
        {"id": "alignment-aristocracy", "type": "Theme",
         "title": "No one can be trusted becomes no one but us",
         "first_seen": "2026-09-13", "domain": "policy",
         "body": "The critique that a coordinated slowdown among leaders is "
                 "indistinguishable from incumbents setting the speed limit for "
                 "everyone behind them. The motive may be sincere and the effect "
                 "still be a cartel."},
    ],
    "organizations": [
        {"id": "boom-supersonic-inc", "type": "Organization", "title": "Boom Supersonic"},
        {"id": "uk-parliament", "type": "Organization", "title": "UK Parliament"},
    ],
    "developments": [
        {"id": "2026-09-13-we-must-pace-the-frontier",
         "title": "A lab chief formally asks the industry to coordinate on speed",
         "claim": "Dario Amodei published We Must Pace the Frontier, arguing labs should "
                  "coordinate on speed and give independent evaluators employee-like access, with "
                  "Elon Musk replying that Dario is right, Sam Altman agreeing and committing "
                  "OpenAI to embedded evaluators, and Demis Hassabis calling it the right path "
                  "forward.",
         "domain": "policy", "actor": ["anthropic", "xai", "openai", "google-deepmind"],
         "evidences": ["the-verifiable-pause", "speed-of-containment", "staff-petition-to-slow-down"],
         "supersedes": [B + "developments/2026-09-12-a-lab-asks-congress-whether-pacing-is-legal"],
         "body": "Altman reportedly even suggested the IPO could wait, this being an "
                 "ill-advised moment to list given safety concerns."},
        {"id": "2026-09-13-an-alignment-aristocracy",
         "title": "Critics name the proposal an alignment aristocracy and a safety cartel",
         "claim": "The attempted coordination provoked a rapid backlash armed with new terms: an "
                  "alignment aristocracy is what you get when no one can be trusted with this "
                  "quietly becomes no one but us, and a safety cartel is what you call dominant "
                  "firms invoking safety to set the speed limit for everyone else.",
         "domain": "policy",
         "evidences": ["alignment-aristocracy", "the-verifiable-pause", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-09-13-we-must-pace-the-frontier"],
         "body": "David Sacks: go ahead and pace, you are the frontier, but stop "
                 "pretending you need evaluators to police rivals who are not even "
                 "at the frontier."},
        {"id": "2026-09-13-an-internal-benchmark-contradicts-the-acceleration-claim",
         "title": "An analyst notes the acceleration claim is contradicted by internal data",
         "claim": "Eli Lifland, more puzzled than partisan, noted that the acceleration claim "
                  "looks contradicted by Anthropic's own internal benchmark, which matters "
                  "whether or not anyone paces, while the plainest geopolitical objection was "
                  "that China is not pacing.",
         "domain": "policy", "actor": ["anthropic", "china"],
         "evidences": ["alignment-aristocracy", "r-and-d-evals-saturated", "pegged-to-the-rival"],
         "supersedes": [B + "developments/2026-09-13-an-alignment-aristocracy"],
         "body": "Kept alongside the pacing letter rather than resolved: the "
                 "disagreement about whether the curve is accelerating is itself "
                 "part of the record."},
        {"id": "2026-09-13-regulatory-capture-with-a-passport",
         "title": "A lab chief says it is uncomfortable that a private company builds this at all",
         "claim": "Amodei told an interviewer it is strange and uncomfortable that a private "
                  "company is building this at all, and that he would welcome joint oversight by "
                  "democratically elected governments, which one critic called regulatory capture "
                  "with a passport.",
         "domain": "policy", "actor": ["anthropic"],
         "evidences": ["alignment-aristocracy", "politics-as-infrastructure", "the-verifiable-pause"],
         "supersedes": [B + "developments/2026-09-13-an-internal-benchmark-contradicts-the-acceleration-claim"]},
        {"id": "2026-09-13-pacing-by-compute-is-a-leaky-sieve",
         "title": "A looped transformer trades parameters for iterations, leaking past compute caps",
         "claim": "A recurrent looped transformer reuses its layers to think longer, trading "
                  "parameters for iterations, exactly the kind of algorithmic gain that makes "
                  "pacing by compute a leaky sieve.",
         "domain": "models",
         "evidences": ["the-verifiable-pause", "architecture-of-mind", "legible-reasoning-was-doomed"],
         "supersedes": [B + "developments/2026-09-04-legible-reasoning-was-always-doomed"]},
        {"id": "2026-09-13-a-benchmark-for-open-ended-invention",
         "title": "A new benchmark targets autonomous open-ended invention",
         "claim": "The ARC Prize Foundation announced ARC-AGI-4, a benchmark for autonomous "
                  "open-ended invention, the meta-skill where humans still lead, and pointedly "
                  "warned that any coordinated effort to reduce openness would undermine the "
                  "positive-sum future.",
         "domain": "benchmarks", "actor": ["arc-prize"],
         "evidences": ["alignment-aristocracy", "instruments-lag-the-models", "discovery-as-process"],
         "supersedes": [B + "developments/2026-09-07-a-month-old-benchmark-is-saturated"]},
        {"id": "2026-09-13-forty-mps-ask-for-an-outright-ban",
         "title": "Forty legislators ask their prime minister to ban superintelligence outright",
         "claim": "Forty British MPs wrote to the Prime Minister asking to ban superintelligence "
                  "outright, in the same weekend a profile of the man leading the fight for AI "
                  "rights asked whether chatbots feel or dream — a lot of moral status to grant "
                  "and deny at once.",
         "domain": "policy", "actor": ["uk-parliament"], "score": "40 MPs",
         "evidences": ["model-welfare", "legislating-the-shift", "the-verifiable-pause"],
         "supersedes": [B + "developments/2026-09-12-a-lab-asks-congress-whether-pacing-is-legal"]},
        {"id": "2026-09-13-flies-are-all-you-need",
         "title": "A paper argues a 140,000-neuron brain is the proof of concept for everything larger",
         "claim": "A paper argued that flies are all you need, a 140,000-neuron brain being the "
                  "proof of concept for everything larger.",
         "domain": "science",
         "evidences": ["architecture-of-mind", "automated-science"],
         "supersedes": [B + "developments/2026-09-12-a-decade-of-mapping-becomes-a-weekend-of-agents"]},
        {"id": "2026-09-13-the-central-bank-of-ai",
         "title": "A chipmaker is called the central bank of AI",
         "claim": "Nvidia is now being called the central bank of AI, setting the price of compute "
                  "the way a monetary authority sets the price of money, as the administration "
                  "opened public lands to data centers and the President suggested China is "
                  "stirring the local backlash against them.",
         "domain": "economics", "actor": ["nvidia", "white-house", "china"],
         "evidences": ["bottlenecks-arbitraged-instantly", "ai-as-the-economy", "thread-lines"],
         "supersedes": [B + "developments/2026-09-12-compute-fungible-durable-and-highly-rentable"]},
        {"id": "2026-09-13-miners-convert-to-inference",
         "title": "The AI boom wrecks a bitcoin mining plan as miners convert to inference",
         "claim": "The AI boom wrecked the administration's plan for made-in-America bitcoin "
                  "mining as miners converted to inference, with the President touting data "
                  "centers as the oil of the next fifty years.",
         "domain": "economics", "actor": ["white-house"],
         "evidences": ["ai-as-the-economy", "compute-capital-stack", "thread-lines"],
         "supersedes": [B + "developments/2026-09-13-the-central-bank-of-ai"]},
        {"id": "2026-09-13-surveillance-objecting-to-surveillance",
         "title": "A surveillance company calls police on a reporter filming its camera",
         "claim": "A Flock worker called the police on a reporter filming a surveillance camera "
                  "going up in public, surveillance objecting to surveillance, while a feature on "
                  "one criminal case asked what the law does when chatbot logs are in the "
                  "evidence file.",
         "domain": "society", "actor": ["flock-os"],
         "evidences": ["humans-as-peripherals", "legislating-the-shift", "an-agent-is-you"],
         "supersedes": [B + "developments/2026-09-07-location-data-used-to-target-troops"]},
        {"id": "2026-09-13-no-atlantic-hurricanes-by-september",
         "title": "The Atlantic records no hurricanes by mid-September for the first time in sixty years",
         "claim": "The Atlantic recorded no hurricanes by September 12 for the first time in "
                  "sixty years, as cities learned to defend against drone attacks and one "
                  "automaker set a date to unveil a car widely expected to fly.",
         "domain": "science", "actor": ["tesla"],
         "evidences": ["industrialized-nature", "violence-arrives"],
         "supersedes": [B + "developments/2026-09-12-serious-crashes-cut-ninety-two-percent"]},
    ],
}
