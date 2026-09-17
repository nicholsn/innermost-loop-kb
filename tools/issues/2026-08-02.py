"""Issue 179 — 2026-08-02. The dark night of mathematics."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-2-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-02", "title": "Welcome to August 2, 2026", "url": URL,
        "thesis": "A discipline grieves as its central act is automated.",
        "body": """
# Welcome to August 2, 2026

A number theorist conceded a bet four years early: AI can produce
Annals-quality number theory for under $100k per paper. Prediction markets price
an AI-solved Millennium Prize Problem by 2028 at 52%.

The response from practitioners is not competitive but elegiac. One described a
dark night of mathematics, arguing discovery was how humans touched the
ineffable, and asking whether foreclosing it for future mathematicians is itself
a kind of evil.
""",
    },
    "themes": [
        {"id": "a-discipline-grieves", "type": "Theme",
         "title": "The field mourns rather than competes",
         "first_seen": "2026-08-02", "domain": "science",
         "body": "When automation reaches the act a profession considered sacred, the "
                 "reaction stops being about jobs. The loss described is access to "
                 "something ineffable, and the argument becomes whether foreclosing "
                 "that for the next generation is a harm in itself."},
    ],
    "organizations": [
        {"id": "manifold", "type": "Organization", "title": "Manifold Markets"},
        {"id": "capuchinai", "type": "Organization", "title": "CapuchinAI"},
    ],
    "systems": [
        {"id": "seedance-2-5", "type": "AISystem", "title": "Seedance 2.5",
         # tags waived: no controlled entity tag (ENRICH_RULES) describes a proprietary video model; the linked Seed blog says it ships via Jimeng AI, Doubao Pro and a BytePlus ModelArk API, not as open weights.
         "description": "ByteDance Seed's audio-video generation model, which produces 30-second clips in a single pass with multi-minute extensions and timestamp-level edits.",
         "developed_by": [B + "organizations/bytedance"], "modality": "video",
         "resource": "https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5",
         "sameAs": ["http://www.wikidata.org/entity/Q141136321"],
         "body": "Seedance 2.5 is ByteDance's audio-video generation model, announced with one-pass 30-second "
                 "clips, multi-minute extensions and timestamp-level editing. The corpus records it once, "
                 "alongside the [75.4-second speedrun record](/developments/2026-08-02-a-speedrun-record-falls-to-a-faster-kernel.md); "
                 "an earlier Seedance appears in February, when it "
                 "[cloned voices from photos](/developments/2026-02-11-seedance-cloned-voices-from-photos.md)."},
    ],
    "developments": [
        {"id": "2026-08-02-a-bet-conceded-four-years-early",
         "title": "A number theorist concedes his AI bet four years early",
         "claim": "After ten long-standing open problems were settled, number theorist Daniel "
                  "Litt conceded four years early his bet that AI could not produce "
                  "Annals-quality number theory under $100,000 per paper, calling it a big deal, "
                  "as prediction markets priced an AI-solved Millennium Prize Problem at 31% by "
                  "2027 and 52% by 2028.",
         "domain": "science", "actor": ["manifold", "openai"], "score": "52% by 2028",
         "evidences": ["proof-priced-per-unit", "automated-science", "takeoff-declared"],
         "supersedes": [B + "developments/2026-08-01-ten-decade-old-problems-for-under-two-thousand-dollars"]},
        {"id": "2026-08-02-the-dark-night-of-mathematics",
         "title": "Mathematicians describe grief rather than competition",
         "claim": "One mathematician called the results the last straw for academic mathematics, "
                  "since specialists spend months per conjecture in silos and now an amateur can "
                  "one-shot a life's work, while another described a dark night of mathematics, "
                  "arguing discovery was how humans touched the ineffable and asking whether "
                  "foreclosing it for future mathematicians is itself a kind of evil.",
         "domain": "science",
         "evidences": ["a-discipline-grieves", "disciplines-declare-themselves", "humans-need-not-apply"],
         "supersedes": [B + "developments/2026-08-02-a-bet-conceded-four-years-early"],
         "body": "A cosmologist agreed that mathematics functions as a religious "
                 "order, and that watching it fall must be like watching heaven "
                 "being plundered."},
        {"id": "2026-08-02-proofs-that-bury-the-crux-under-boilerplate",
         "title": "Reviewers complain machine proofs bury the technical crux under boilerplate",
         "claim": "Columbia's Henry Yuen complained that the writeups bury the technical crux "
                  "under boilerplate, introduced as if this were the obvious thing to do, with "
                  "another observer noting frontier models excel at cross-field translation into "
                  "verifiable constructions and warning to brace for the coming deluge.",
         "domain": "science",
         "evidences": ["understanding-as-the-scarce-good", "a-discipline-grieves"],
         "supersedes": [B + "developments/2026-08-02-the-dark-night-of-mathematics"]},
        {"id": "2026-08-02-a-fields-worthy-result-could-go-trivial-before-the-medal",
         "title": "A researcher notes a Fields-worthy result could turn trivial before the award",
         "claim": "A DeepMind researcher noted that a Fields-worthy human result could turn "
                  "AI-trivial before the medal is awarded, while a lab's own model estimated any "
                  "single one of the ten results would plausibly anchor a medal case.",
         "domain": "science", "actor": ["google-deepmind", "anthropic"],
         "evidences": ["a-discipline-grieves", "proof-priced-per-unit", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-08-02-proofs-that-bury-the-crux-under-boilerplate"]},
        {"id": "2026-08-02-labs-will-compete-with-their-own-customers",
         "title": "A researcher says maximum performance requires tying harness to model",
         "claim": "Anthropic's Jess Yan argued that maximum performance is impossible without "
                  "tying harness and model together, which one investor decoded as notice that "
                  "model labs will compete with their own customers.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["harness-as-generalizer", "orchestration-not-construction",
                       "software-margin-collapse"],
         "supersedes": [B + "developments/2026-08-01-agents-write-almost-all-output-tokens"]},
        {"id": "2026-08-02-a-speedrun-record-falls-to-a-faster-kernel",
         "title": "A training speedrun record falls to 75.4 seconds",
         "claim": "The NanoGPT speedrun record fell to 75.4 seconds on a faster Triton kernel, "
                  "while ByteDance's Seedance 2.5 began generating 30-second audio-video in one "
                  "pass with multi-minute extensions and timestamp-level edits.",
         "description": "The corpus's steadiest gauge of algorithmic progress ticks down again, "
                        "this time at the kernel layer rather than the architecture, with the "
                        "newsletter filing it under the machinery tightening beneath lab strategy.",
         "domain": "models", "actor": ["bytedance", "recursive-superintelligence"], "score": "75.4 seconds",
         "about": [B + "benchmarks/nanogpt-speedrun", B + "systems/seedance-2-5"],
         "evidences": ["optimizing-its-own-invoice", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-07-31-a-model-rewrites-its-own-harness-for-eleven-points",
                        B + "developments/2026-03-08-nanogpt-86s"],
         "relatedTo": [B + "developments/2026-05-15-agents-beat-the-human-speedrun-baseline",
                       B + "developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price",
                       B + "developments/2026-01-12-nanogpt-106s",
                       B + "developments/2026-05-14-recursive-superintelligence-raises-650m"],
         "tags": ["speedrun", "kernels", "rsi"],
         "supporting_text": "fell to 75.4 seconds",
         "sources": [{"id": "classiclarryd-nanogpt-75-4s-post",
                      "resource": "https://x.com/classiclarryd/status/2083739041338630372",
                      "title": "New NanoGPT Speedrun WR at 75.4s (-0.6s) from @cong_ml and Recursive, with a faster ReLU^2 MLP Triton kernel",
                      "author": "human:classiclarryd", "last_modified": "2026-08-02"},
                     {"id": "modded-nanogpt-record-table",
                      "resource": "https://github.com/KellerJordan/modded-nanogpt",
                      "title": "Modded-NanoGPT: World record history", "author": "human:kellerjordan0"},
                     {"id": "bytedance-seed-seedance-2-5-blog",
                      "resource": "https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5",
                      "title": "One-take Creation, Flexible Referencing: Introducing Seedance 2.5",
                      "author": "org:bytedance", "last_modified": "2026-07-31"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The [NanoGPT speedrun](/benchmarks/nanogpt-speedrun.md) record fell to 75.4 seconds on a "
                 "faster ReLU^2 MLP Triton kernel ([post on X](https://x.com/classiclarryd/status/2083739041338630372)), "
                 "down from [86.8 s](/developments/2026-03-08-nanogpt-86s.md) in March and "
                 "[127.7 s](/developments/2025-12-21-nanogpt-speedrun-127s.md) when the corpus began tracking it "
                 "in December. The X post and the speedrun's own "
                 "[record table](https://github.com/KellerJordan/modded-nanogpt) credit the record to @cong_ml and an AI system "
                 "called Recursive from [Recursive Superintelligence](/organizations/recursive-superintelligence.md), "
                 "the lab that [raised $650M in May](/developments/2026-05-14-recursive-superintelligence-raises-650m.md) "
                 "to have AI experiment on improving itself, so the record carries an AI-system co-author. The gain "
                 "comes from the kernel layer, where [compiler kernel hacking](/developments/2026-01-12-nanogpt-106s.md) "
                 "had already set a record in January and where [a model rewrote the production kernels](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md) "
                 "behind OpenAI's price cut three days earlier, and it lands after "
                 "[agents given idle compute beat the human baseline](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) "
                 "on the speedrun's optimizer track. In the same item ByteDance's [Seedance 2.5](/systems/seedance-2-5.md) "
                 "began generating 30-second audio-video in one pass with multi-minute extensions and "
                 "timestamp-level edits ([ByteDance Seed](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5))."},
        {"id": "2026-08-02-a-company-caps-vulnerability-reports-over-ai-slop",
         "title": "A company caps vulnerability reports after AI submissions buckle its reviewers",
         "claim": "Apple capped vulnerability reports after AI submissions mixing real flaws with "
                  "slop buckled its human reviewers, stranding one startup's six-figure exploit "
                  "chain even as AI-assisted updates carried five times the usual fixes.",
         "domain": "compute", "actor": ["apple"], "score": "5x the usual fixes",
         "evidences": ["botsitting", "risk-becomes-uninsurable", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-07-31-more-security-bugs-fixed-than-in-the-prior-two-years"]},
        {"id": "2026-08-02-twenty-million-chips-doubling-every-nine-months",
         "title": "The installed AI chip base doubles every nine months",
         "claim": "Epoch AI estimates 20 million AI chips are doubling every nine months toward "
                  "200 million H100 equivalents by 2028, with data center power quadrupling by "
                  "2030 and $1 trillion invested by 2029.",
         "domain": "compute", "actor": ["epoch-ai"], "score": "20M chips, doubling every 9 months",
         "evidences": ["compute-capital-stack", "infrastructure-crowding-out", "takeoff-declared"],
         "supersedes": [B + "developments/2026-07-31-the-largest-single-day-value-gain-ever"]},
        {"id": "2026-08-02-used-evs-appreciate-on-war-priced-gasoline",
         "title": "Used electric vehicles appreciate as war-priced gasoline bites",
         "claim": "Used electric vehicles are appreciating, up 7% this year on $4.10 war-priced "
                  "gasoline, as the energy squeeze reprices the driveway.",
         "domain": "energy", "score": "+7% / $4.10 gas",
         "evidences": ["burning-molecules-for-tokens", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-07-30-the-longest-commercial-flight-ever"]},
        {"id": "2026-08-02-wild-monkeys-recognized-and-paid-in-banana",
         "title": "A system recognizes wild monkeys and pays correct answers in dried banana",
         "claim": "In Costa Rica, CapuchinAI recognizes wild monkeys with 97% accuracy and pays "
                  "correct answers in dried banana, a first for wild primate science, while "
                  "Curiosity found a field of honeycomb polygons wrapping an entire Martian "
                  "valley.",
         "domain": "science", "actor": ["capuchinai", "nasa"], "score": "97% accuracy",
         "evidences": ["automated-science", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-08-01-almost-all-compute-in-space"]},
        {"id": "2026-08-02-a-bundle-raises-twenty-thousand-for-laid-off-developers",
         "title": "A game bundle raises $20,000 in a day for developers laid off to automation",
         "claim": "A pay-what-you-want bundle of more than a hundred games raised over $20,000 in "
                  "a day for developers laid off in the era when code writes itself.",
         "domain": "society", "score": "$20,000 in a day",
         "evidences": ["work-displaced", "a-discipline-grieves"],
         "supersedes": [B + "developments/2026-07-30-solo-founders-run-million-dollar-companies"]},
    ],
}
