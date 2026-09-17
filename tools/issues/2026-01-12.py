"""Issue 031 — 2026-01-12. TCP/IP for the agentic economy."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-12-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-12", "title": "Welcome to January 12, 2026", "url": URL,
        "thesis": "Commerce gets a protocol layer built for agents rather than people.",
        "body": """
# Welcome to January 12, 2026

Google ships the Universal Commerce Protocol: an open standard for agents to
negotiate and transact across a whole shopping journey. The corpus has been
recording agents buying things; this is the first time the plumbing is built for
them rather than borrowed from humans.

Linus Torvalds vibe-coding with Antigravity is the same story on the other side
of the stack — manual syntax becoming optional for the person who wrote the
Linux kernel.
""",
    },
    "organizations": [
        {"id": "wing", "type": "Organization", "title": "Wing",
         "resource": "https://wing.com/", "body": "Alphabet drone delivery arm."},
        {"id": "walmart", "type": "Organization", "title": "Walmart",
         "resource": "https://www.walmart.com/"},
        {"id": "harmattan-ai", "type": "Organization", "title": "Harmattan AI",
         "body": "European defense drone unicorn producing 10,000 units a month."},
        {"id": "shopify", "type": "Organization", "title": "Shopify",
         "resource": "https://www.shopify.com/"},
        {"id": "ixi", "type": "Organization", "title": "IXI",
         "body": "Liquid-crystal autofocusing eyeglasses."},
        {"id": "iran", "type": "Organization", "title": "Government of Iran"},
    ],
    "people": [
        {"id": "linus-torvalds", "type": "Person", "title": "Linus Torvalds", "name": "Linus Torvalds",
         "description": "Creator and architect of the Linux kernel, recorded in the corpus taking up "
                        "vibe-coding with Google's Antigravity agent.",
         "resource": "https://github.com/torvalds",
         "sameAs": ["http://www.wikidata.org/entity/Q34253"],
         "tags": ["founder"],
         "body": "Linus Torvalds created the Linux kernel and remains its architect. In this corpus he "
                 "appears when he [began vibe-coding with Antigravity](/developments/2026-01-12-torvalds-vibe-codes.md) "
                 "on his AudioNoise project ([GitHub](https://github.com/torvalds/AudioNoise)), which the "
                 "newsletter reads as manual syntax becoming optional even for the kernel's author. The "
                 "next day [Claude Code wrote all of Claude Cowork](/developments/2026-01-13-claude-code-writes-cowork.md), "
                 "and the kernel he maintains returns when "
                 "[Chris Mason published AI prompts for kernel review](/developments/2026-02-02-kernel-review-prompts.md)."},
    ],
    "systems": [
        {"id": "universal-commerce-protocol", "type": "AISystem",
         "title": "Universal Commerce Protocol",
         "developed_by": [B + "organizations/google"], "modality": "protocol",
         "body": "Open standard for agents to interact, negotiate and transact across a "
                 "shopping journey."},
    ],
    "developments": [
        {"id": "2026-01-12-universal-commerce-protocol",
         "title": "Google ships a commerce protocol for agents",
         "claim": "Google launched the Universal Commerce Protocol, an open standard letting AI "
                  "agents interact, negotiate and transact across the shopping journey, "
                  "alongside Direct Offers and an autonomous Business Agent.",
         "domain": "economics", "actor": ["google"],
         "about": [B + "systems/universal-commerce-protocol"],
         "evidences": ["autonomous-commerce", "network-over-node"],
         "supersedes": [B + "developments/2026-01-09-copilot-checkout"],
         "body": "The first infrastructure in the corpus built for agents rather than adapted "
                 "from human interfaces."},
        {"id": "2026-01-12-torvalds-vibe-codes",
         "title": "Linus Torvalds starts vibe-coding",
         "claim": "Linus Torvalds began vibe-coding with Antigravity, signalling that manual "
                  "syntax is optional even for the Linux kernel's architect.",
         "domain": "agents", "actor": ["people/linus-torvalds"], "about": [B + "systems/antigravity"],
         "evidences": ["engineer-as-supervisor", "software-margin-collapse"],
         "supersedes": [B + "developments/2026-01-06-vibe-coding-dies"]},
        {"id": "2026-01-12-kernel-bugs-found-69pct",
         "title": "AI fuzzing finds 69% of kernel bugs within a year",
         "claim": "The share of Linux kernel bugs found within a year of creation rose from 0% "
                  "in 2010 to 69% recently, driven by AI fuzzing.",
         "domain": "agents", "score": "0% → 69%",
         "evidences": ["automated-science", "engineer-as-supervisor"]},
        {"id": "2026-01-12-mri-viewer-on-the-fly",
         "title": "A CEO builds an MRI viewer from a USB stick",
         "claim": "Shopify's CEO ran Claude against a raw MRI USB stick to build a web-based "
                  "viewer on the spot, bypassing commercial medical software.",
         "domain": "agents", "actor": ["shopify", "anthropic"],
         "evidences": ["software-margin-collapse", "engineer-as-supervisor"]},
        {"id": "2026-01-12-alibaba-concedes-compute-lead",
         "title": "Alibaba puts Chinese odds of leapfrogging below 20%",
         "claim": "Alibaba conceded the American compute lead looks insurmountable, giving "
                  "Chinese labs under a 20% chance of leapfrogging US labs.",
         "domain": "policy", "actor": ["alibaba"], "score": "<20%",
         "evidences": ["silicon-curtain", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-10-grok-5-seven-trillion"]},
        {"id": "2026-01-12-delivery-vans-plow-wet-concrete",
         "title": "Driverless vans optimize for delivery time over roads",
         "claim": "Driverless delivery vans in China gained cult status for driving through wet "
                  "concrete and crumbling roads, optimizing delivery time over infrastructure "
                  "preservation.",
         "domain": "robotics", "actor": ["china"],
         "evidences": ["autonomy-clock-speed", "coordination-tax"],
         "body": "An objective function meeting a shared resource it was never told about."},
        {"id": "2026-01-12-wing-150-walmart-stores",
         "title": "Drone delivery reaches 40 million Americans",
         "claim": "Wing is scaling to 150 Walmart stores, putting drone delivery within reach "
                  "of more than 40 million Americans, while Harmattan AI began producing 10,000 "
                  "defense drones a month in Europe.",
         "domain": "robotics", "actor": ["wing", "walmart", "harmattan-ai"], "score": "40M people",
         "evidences": ["autonomous-commerce", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-01-03-zipline-delivers-to-pastures"]},
        {"id": "2026-01-12-twilight-dawn-dusk-orbit",
         "title": "SpaceX flies the first mission to a perpetual-sunlight orbit",
         "claim": "SpaceX launched its first Twilight mission to a dawn-dusk sun-synchronous "
                  "orbit, securing perpetual sunlight for future orbital data centers.",
         "domain": "space", "actor": ["spacex"],
         "evidences": ["orbit-as-compute", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-01-10-graham-orbital-datacenters-inevitable"]},
        {"id": "2026-01-12-iran-severs-starlink",
         "title": "Iran jams Starlink and darkens 80 million people",
         "claim": "Iran activated jamming that severed Starlink access, cutting 80 million "
                  "people off from the network.",
         "domain": "policy", "actor": ["iran", "spacex"], "score": "80M people",
         "evidences": ["politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-08-regime-change-from-orbit"],
         "body": "Four days after orbit was used to coordinate a regime change, a state proves "
                 "the link can be cut."},
        {"id": "2026-01-12-china-files-200000-satellites",
         "title": "China files for 200,000 satellites",
         "claim": "China filed plans for 200,000 satellites, while NASA's Jared Isaacman said "
                  "Artemis III astronauts will arrive at a Moon base already waiting for them.",
         "domain": "space", "actor": ["china", "nasa"], "score": "200,000",
         "evidences": ["silicon-curtain", "inhabitable-worlds"]},
        {"id": "2026-01-12-erdos-397-third-this-week",
         "title": "Erdős #397 falls, the third this week",
         "claim": "GPT-5.2 Pro and Aristotle solved Erdős problem #397, the third of the week.",
         "domain": "science", "actor": ["openai", "harmonic"],
         "evidences": ["automated-science", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-01-11-erdos-729"]},
        {"id": "2026-01-12-nanogpt-106s",
         "title": "The speedrun record falls to 106.9 seconds on compiler kernel hacking",
         "claim": "The NanoGPT speedrun record dropped to 106.9 seconds through compiler kernel "
                  "hacking.",
         "description": "The chain's gain comes from below the model, in the compiler and kernel layer "
                        "rather than from architecture, the layer the corpus's later kernel-writing "
                        "agents work in.",
         "domain": "models", "score": "106.9 s",
         "about": [B + "benchmarks/nanogpt-speedrun"],
         "evidences": ["recursive-self-improvement", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-01-08-nanogpt-109s"],
         "relatedTo": [B + "developments/2026-01-02-speedrun-gains-generalize",
                       B + "developments/2026-04-29-a-model-writes-the-kernels-that-run-it",
                       B + "developments/2026-05-15-agents-beat-the-human-speedrun-baseline"],
         "tags": ["speedrun", "kernels"],
         "supporting_text": "106.9 seconds",
         "sources": [{"id": "dial-nanogpt-speedrun-106-9",
                      "resource": "https://x.com/classiclarryd/status/2010545452832407943",
                      "title": "Larry Dial on X: New NanoGPT Speedrun WR at 106.9 seconds",
                      "author": "human:larry-dial", "last_modified": "2026-01-12"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The record, 2.3 seconds under the "
                 "[109.2-second mark](/developments/2026-01-08-nanogpt-109s.md) of four days earlier, "
                 "came from GitHub contributors andrewbriand and jrauvola, who noticed that the torch "
                 "compiler was running a separate, inefficient kernel for the ReLU(x)^2 activation and "
                 "wrote a Triton kernel fusing it into the preceding linear op "
                 "([X](https://x.com/classiclarryd/status/2010545452832407943)). Earlier links in the "
                 "[NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) chain came from optimizers and "
                 "attention variants, and the "
                 "[January 2 result](/developments/2026-01-02-speedrun-gains-generalize.md) showed "
                 "those gains transfer; this one is pure kernel work, the layer where "
                 "[a model later tops the leaderboard for writing its own kernels](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md). "
                 "The record falls again to "
                 "[99.3 seconds](/developments/2026-01-24-nanogpt-99s-bigram-hash.md) twelve days "
                 "later, and by May "
                 "[agents beat the human speedrun baseline](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) "
                 "outright."},
        {"id": "2026-01-12-coca-cola-reverse-engineered",
         "title": "A hobbyist reverse-engineers Coca-Cola",
         "claim": "A YouTube hobbyist used mass spectrometry to reverse-engineer the Coca-Cola "
                  "formula, resolving a mystery held since the late nineteenth century.",
         "domain": "science", "evidences": ["discovery-as-process", "automated-science"]},
        {"id": "2026-01-12-magneto-conversion-battery",
         "title": "A magneto-conversion battery quadruples energy density",
         "claim": "South Korean researchers built a magneto-conversion lithium battery with "
                  "four times the energy density at 99% efficiency, as the Buick Electra E7 "
                  "hybrid reached 995 miles of range.",
         "domain": "energy", "score": "4x density / 995 miles",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-01-06-five-minute-solid-state-battery"]},
        {"id": "2026-01-12-claude-for-healthcare-and-life-sciences",
         "title": "Anthropic ships healthcare and life-sciences products",
         "claim": "Anthropic launched dedicated Claude products for Healthcare and Life "
                  "Sciences handling HIPAA-ready analysis and drafting clinical trial "
                  "protocols, as the FDA relaxed CMC requirements for gene therapies.",
         "domain": "biotech", "actor": ["anthropic", "fda"],
         "evidences": ["legislating-the-shift", "automated-science"],
         "supersedes": [B + "developments/2026-01-09-openai-for-healthcare"]},
        {"id": "2026-01-12-liquid-crystal-autofocus-glasses",
         "title": "Eyeglasses autofocus with liquid crystals",
         "claim": "IXI is launching glasses that autofocus using liquid crystals, eliminating "
                  "static prescriptions.",
         "domain": "biotech", "actor": ["ixi"], "evidences": ["intimate-interface"]},
        {"id": "2026-01-12-jpmorgan-ai-casts-proxy-votes",
         "title": "JPMorgan drops proxy advisors for an in-house model",
         "claim": "JPMorgan cut ties with proxy-advisory firms to cast shareholder votes with "
                  "an in-house AI, while a federal judge in Texas began using AI to draft "
                  "hearing questions.",
         "domain": "policy", "actor": ["jpmorgan"],
         "evidences": ["autonomous-commerce", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-01-04-alaska-ai-judges"]},
        {"id": "2026-01-12-grokipedia-self-heals",
         "title": "An encyclopedia auto-approves its own corrections",
         "claim": "Grokipedia now researches and auto-approves corrections to itself when users "
                  "challenge an article.",
         "description": "The newsletter's phrase is that truth is becoming self-healing: the loop "
                        "applied to a reference work rather than to code, with the human editor "
                        "removed from the correction step and the machine both writing and "
                        "adjudicating.",
         "domain": "society", "actor": ["xai"], "about": [B + "systems/grokipedia"],
         "occurred_on": "2026-01-11",
         "evidences": ["machine-introspection", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-01-11-ai-music-three-hours-a-week"],
         "relatedTo": [B + "developments/2026-01-11-x-timeline-rewrite-20pct",
                       B + "developments/2026-01-12-jpmorgan-ai-casts-proxy-votes",
                       B + "developments/2026-05-12-the-model-grades-the-graders"],
         "tags": ["rsi", "self-modification"],
         "supporting_text": "auto-approve corrections to itself",
         "sources": [{"id": "nas-daily-grokipedia-correction",
                      "resource": "https://x.com/nasdaily/status/2010326795967684899",
                      "title": "Nuseir Yassin on X: Grokipedia researched and approved a correction to his own article",
                      "author": "human:nuseir-yassin", "last_modified": "2026-01-11"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The source is Nuseir Yassin, the Nas Daily creator, who found that Grok had written a "
                 "10,000-word Grokipedia article on his career that was about 95% accurate but wrongly "
                 "said he had divorced; rather than petition an editor he challenged the claim, and the "
                 "system researched it and approved the correction itself "
                 "([X](https://x.com/nasdaily/status/2010326795967684899)). "
                 "[Grokipedia](/systems/grokipedia.md) had reached "
                 "[86% of English Wikipedia's article count](/developments/2026-01-11-ai-music-three-hours-a-week.md) "
                 "the day before; this is the corpus's first case of a model-authored corpus reviewing "
                 "and revising itself with no human approval step, in the same week that xAI's "
                 "[rewrite of the X timeline](/developments/2026-01-11-x-timeline-rewrite-20pct.md) and "
                 "JPMorgan's [in-house model casting proxy votes](/developments/2026-01-12-jpmorgan-ai-casts-proxy-votes.md) "
                 "put machine judgment in charge of other human institutions. The measured correcting "
                 "the measurement recurs in May when "
                 "[a model flags fatal errors in a third of a benchmark's problems](/developments/2026-05-12-the-model-grades-the-graders.md) "
                 "and the graders are corrected."},
        {"id": "2026-01-12-greenland-freedom-city",
         "title": "Investors propose a Greenland freedom city",
         "claim": "Silicon Valley investors are proposing a Greenland freedom city for "
                  "unregulated AI and nuclear reactors.",
         "domain": "policy", "evidences": ["regulatory-exit"],
         "supersedes": [B + "developments/2026-01-10-starbase-police-department"]},
    ],
}
