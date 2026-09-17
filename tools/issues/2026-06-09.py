"""Issue 135 — 2026-06-09. The doctrinal phase."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-june-9-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-06-09", "title": "Welcome to June 9, 2026", "url": URL,
        "thesis": "The labs preview their intentions before they ship their intelligence.",
        "body": """
# Welcome to June 9, 2026

OpenAI released a plan targeting an automated AI researcher by March 2028,
broadly shared economic acceleration, and a personal AGI for every human on
Earth — so that the post-AGI transition is collectively steered rather than
quietly hoarded.

Apple capitulated at WWDC26. Its rebuilt architecture was co-developed with
Google on Gemini technology, and its own frontier model runs on Nvidia GPUs
inside Google's cloud. Apple's remaining job is not to build the intelligence
but to orchestrate it.
""",
    },
    "themes": [
        {"id": "intentions-published-first", "type": "Theme",
         "title": "Labs publish doctrine before capability",
         "first_seen": "2026-06-09", "domain": "policy",
         "body": "Roadmaps, plans and charters arrive ahead of the models they "
                 "describe. Publishing the intention first is both a commitment "
                 "device and a claim on legitimacy — the argument about what should "
                 "happen is staked out before anyone can check the capability."},
        {"id": "orchestration-not-construction", "type": "Theme",
         "title": "Integrators stop building intelligence",
         "first_seen": "2026-06-09", "domain": "economics",
         "body": "The most vertically integrated companies in the world give up "
                 "making the model and keep only the routing, the context and the "
                 "surface. Owning the customer stops implying owning the capability."},
    ],
    "organizations": [
        {"id": "pentagon", "type": "Organization", "title": "US Department of Defense"},
        {"id": "redwire", "type": "Organization", "title": "Redwire"},
        {"id": "taiwan", "type": "Organization", "title": "Taiwan"},
    ],
    "developments": [
        {"id": "2026-06-09-a-personal-agi-for-every-human",
         "title": "A lab publishes a plan for a personal AGI for every human",
         "claim": "OpenAI released a plan to benefit everyone targeting an automated AI "
                  "researcher by March 2028, broadly shared economic acceleration and a "
                  "personal AGI for every human on Earth, so the post-AGI transition is "
                  "collectively steered rather than quietly hoarded.",
         "description": "The newsletter's doctrinal phase in its purest form: a lab dates its automated "
                        "researcher and stakes out the distribution of the post-AGI world before the "
                        "capability exists to check.",
         "domain": "policy", "actor": ["openai"], "score": "automated AI researcher by March 2028",
         "evidences": ["intentions-published-first", "takeoff-declared",
                       "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-03-22-openai-targets-a-research-intern-by-september"],
         "relatedTo": [B + "developments/2026-06-05-when-ai-builds-itself",
                       B + "developments/2026-01-09-openai-eight-months-to-intern-researchers",
                       B + "developments/2026-05-05-sixty-percent-odds-on-rsi-by-2028"],
         "tags": ["rsi", "ai-r-and-d", "forecast", "policy"],
         "supporting_text": "targets an automated AI researcher by March 2028",
         "sources": [{"id": "openai-built-to-benefit-everyone-plan",
                      "resource": "https://openai.com/index/built-to-benefit-everyone-our-plan/",
                      "title": "Built to benefit everyone: our plan", "author": "org:openai"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "OpenAI's plan ([Built to benefit everyone](https://openai.com/index/built-to-benefit-everyone-our-plan/)) "
                 "sets three commitments: an automated AI researcher by March 2028, broadly shared economic "
                 "acceleration, and a personal AGI for every human on Earth, framed so that the post-AGI "
                 "transition is steered collectively rather than hoarded. The March 2028 date firms up the "
                 "roadmap the corpus has tracked since the [eight-months-to-intern report](/developments/2026-01-09-openai-eight-months-to-intern-researchers.md) "
                 "in January and the [intern-by-September target](/developments/2026-03-22-openai-targets-a-research-intern-by-september.md) "
                 "in March, and it lands four days after Anthropic's institute published "
                 "[its own evidence that AI already accelerates AI](/developments/2026-06-05-when-ai-builds-itself.md), "
                 "so that within one week both leading labs had put their recursion doctrine in writing. The "
                 "newsletter's frame is [intentions published first](/themes/intentions-published-first.md): the "
                 "argument about who benefits is staked out ahead of the capability."},
        {"id": "2026-06-09-retrieval-makes-biology-agent-legible",
         "title": "A deterministic retrieval layer takes viral accuracy from 17% to over 90%",
         "claim": "Anthropic researchers showed that bolting a deterministic retrieval layer "
                  "onto their research agents raised viral-sequence accuracy from 17% to over "
                  "90% while nearly erasing run-to-run variance, evidence that making biology "
                  "agent-legible immediately turns it into automatable terrain.",
         "domain": "biotech", "actor": ["anthropic"], "score": "17% to 90%+",
         "evidences": ["scaffolding-over-weights", "automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-06-05-a-genome-stitched-error-free-in-days"]},
        {"id": "2026-06-09-apple-capitulates-to-orchestration",
         "title": "The last vertically integrated holdout stops building its own intelligence",
         "claim": "Apple capitulated at WWDC26 with an architecture co-developed with Google on "
                  "Gemini technology, its frontier AFM Cloud Pro now running on Nvidia GPUs "
                  "inside Google's cloud, leaving Apple to orchestrate intelligence rather than "
                  "build it.",
         "domain": "economics", "actor": ["apple", "google", "nvidia"],
         "evidences": ["orchestration-not-construction", "network-over-node",
                       "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-06-01-an-image-model-that-fits-on-a-phone"]},
        {"id": "2026-06-09-a-second-generation-siri-routed-query-by-query",
         "title": "An assistant is rebuilt to route each query between device and cloud",
         "claim": "Apple's new Siri pairs a second-generation on-device model with personal "
                  "context, on-screen awareness, a semantic index and systemwide app actions, "
                  "routed query by query between device and cloud, while Visual Intelligence "
                  "splits restaurant bills and reads nutrition from a photo.",
         "domain": "agents", "actor": ["apple"],
         "evidences": ["intimate-interface", "orchestration-not-construction"],
         "supersedes": [B + "developments/2026-05-29-a-law-firm-builds-rather-than-rents"]},
        {"id": "2026-06-09-a-two-hundred-ninety-five-billion-domestic-stack",
         "title": "China plans a $295B datacenter network on 80% domestic hardware",
         "claim": "China is reportedly planning a $295 billion nationwide data-center network "
                  "sourcing 80% domestic hardware from firms such as Huawei, effectively "
                  "evicting Nvidia and AMD, while Taiwan mulls stricter export controls on AI "
                  "chips bound for China.",
         "domain": "policy", "actor": ["china", "huawei", "taiwan"], "score": "$295B / 80% domestic",
         "evidences": ["silicon-curtain", "science-as-industrial-policy"],
         "supersedes": [B + "developments/2026-06-08-three-million-tpus-ordered-from-a-rival-foundry"]},
        {"id": "2026-06-09-all-three-chinese-champions-designated",
         "title": "All three of China's leading AI champions are designated at once",
         "claim": "The Pentagon added Alibaba, Baidu and EV maker BYD to its list of Chinese "
                  "military companies, leaving all three of China's leading AI champions "
                  "designated at once, with Alibaba vowing legal action.",
         "domain": "policy", "actor": ["pentagon", "alibaba", "baidu", "tencent", "byd"],
         "evidences": ["silicon-curtain", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-06-09-a-two-hundred-ninety-five-billion-domestic-stack"]},
        {"id": "2026-06-09-a-seventy-meter-orbital-compute-node",
         "title": "A 70-meter, 150-kW orbital compute satellite is unveiled",
         "claim": "SpaceX unveiled its AI1 satellite, a 70-meter, 150-kW orbital compute node "
                  "that Musk says is simpler to build than a Starlink, and broke ground on a "
                  "factory set to mass-produce AI satellites by the end of 2027.",
         "domain": "space", "actor": ["spacex"], "score": "70 m / 150 kW",
         "evidences": ["orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-04-datacenters-launched-off-a-strip-mined-moon"]},
        {"id": "2026-06-09-early-warning-satellites-could-jam-continents",
         "title": "Early-warning satellites are found able to jam navigation across continents",
         "claim": "A new study found Russia's EKS early-warning satellites emitting bursts that "
                  "could jam GPS and BeiDou across whole continents with a modest power "
                  "increase, while Varda and Redwire race to manufacture drugs in microgravity "
                  "as the ISS sunsets.",
         "domain": "space", "actor": ["russia", "varda-space", "redwire"],
         "evidences": ["war-reaches-the-cloud", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-06-02-undersea-drones-to-guard-the-cables"]},
        {"id": "2026-06-09-ai-majors-go-from-five-to-seventy-four",
         "title": "AI majors go from five schools to seventy-four",
         "claim": "AI majors exploded from five schools in 2021 to at least 74 majors and 89 "
                  "minors today, while Meta committed $115 million to a free workforce academy "
                  "guaranteeing graduates a job building its AI data centers.",
         "domain": "society", "actor": ["meta"], "score": "5 to 74 majors",
         "evidences": ["work-displaced", "ladder-pulled-up"],
         "supersedes": [B + "developments/2026-06-04-a-third-of-a-cs-class-fails"]},
        {"id": "2026-06-09-three-of-the-largest-listings-on-record",
         "title": "Three of the largest listings on record queue up at once",
         "claim": "OpenAI confidentially filed for an IPO at an $850 billion-plus valuation, "
                  "trailing Anthropic's $965 billion filing a week earlier and SpaceX's imminent "
                  "debut, in what could become three of the largest listings on record.",
         "domain": "economics", "actor": ["openai", "anthropic", "spacex"],
         "score": "$850B / $965B / $1.77T",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-06-07-three-point-four-trillion-by-2040"]},
    ],
}
