"""Issue 100 — 2026-04-23. A forty-hour autonomy horizon."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-april-23-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-04-23", "title": "Welcome to April 23, 2026", "url": URL,
        "thesis": "The autonomy horizon reaches a full human working week.",
        "body": """
# Welcome to April 23, 2026

Forecasters put Mythos Preview at a 40-hour autonomy horizon — a full human work
week — with Opus 4.7 at 19. In December the corpus recorded five hours.

And Mozilla used an early Mythos preview to comb Firefox, patching 271
vulnerabilities and declaring that the defects are finite and we are entering a
world where we can finally find them all.
""",
    },
    "organizations": [
        {"id": "mozilla", "type": "Organization", "title": "Mozilla",
         "resource": "https://www.mozilla.org/"},
        {"id": "sony-ai", "type": "Organization", "title": "Sony AI",
         "body": "Built an autonomous table tennis robot that beat top-level humans."},
        {"id": "observable-space", "type": "Organization", "title": "Observable Space",
         "body": "Planning terabit Earth-to-orbit laser links for in-orbit datacenters."},
        {"id": "kind-biotechnology", "type": "Organization", "title": "Kind Biotechnology",
         "body": "Growing integrated organ networks inside animal wombs for transplant."},
        {"id": "maryland", "type": "Organization", "title": "State of Maryland"},
    ],
    "developments": [
        {"id": "2026-04-23-a-forty-hour-autonomy-horizon",
         "title": "The measured autonomy horizon reaches a full working week",
         "claim": "Forecasters put Mythos Preview at a METR fifty percent time horizon of 40 "
                  "hours, a full human work week, with Opus 4.7 at 19 hours.",
         "domain": "benchmarks", "actor": ["metr", "anthropic"], "score": "40 hours",
         "evidences": ["autonomy-clock-speed", "work-displaced"],
         "supersedes": [B + "developments/2026-04-12-thirteen-hours-if-cheating-is-allowed"],
         "body": "December recorded five hours. April records a working week."},
        {"id": "2026-04-23-the-defects-are-finite",
         "title": "Mozilla patches 271 vulnerabilities and calls the defects finite",
         "claim": "Mozilla used an early Mythos preview to comb Firefox, patching 271 "
                  "vulnerabilities and declaring that the defects are finite and we are entering "
                  "a world where we can finally find them all.",
         "domain": "agents", "actor": ["mozilla", "anthropic"], "score": "271 patched",
         "evidences": ["automated-science", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-04-20-maintainers-conscripted-as-a-global-red-team"]},
        {"id": "2026-04-23-a-model-screenshots-itself",
         "title": "An image model generates photorealistic screenshots of its own chat",
         "claim": "OpenAI released its first image model with thinking capabilities, able to "
                  "search the web, generate multiple distinct images from one prompt and audit "
                  "its own outputs, and demonstrated it generating photorealistic screenshots of "
                  "ChatGPT conversations.",
         "domain": "models", "actor": ["openai"], "score": "+242 Elo lead",
         "evidences": ["machine-introspection", "data-beyond-text"],
         "supersedes": [B + "developments/2026-04-09-you-ship-the-org-chart-you-have"]},
        {"id": "2026-04-23-deepmind-engineers-threaten-to-quit-over-a-rivals-tool",
         "title": "Engineers threaten to quit when their employer floats removing a rival's tool",
         "claim": "Steve Yegge reported that DeepMind engineers use Claude daily and threatened "
                  "to quit when Google floated removing it, prompting the company to assemble a "
                  "strike team and unite its coding efforts, even as it noted 75% of its new "
                  "code is already AI-generated.",
         "domain": "economics", "actor": ["google-deepmind", "anthropic"], "score": "75% of code",
         "evidences": ["engineer-as-supervisor", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-04-16-uber-maxes-out-its-annual-ai-budget"]},
        {"id": "2026-04-23-agents-build-memories-from-screen-captures",
         "title": "Background agents build memories from screen captures",
         "claim": "OpenAI shipped background agents that build memories from screen captures "
                  "plus shared workspace agents teams can spawn, and open-weighted a small "
                  "model for masking personal information.",
         "domain": "agents", "actor": ["openai"],
         "evidences": ["agents-on-the-org-chart", "intimate-interface"],
         "supersedes": [B + "developments/2026-04-17-codex-operates-your-computer-alongside-you"]},
        {"id": "2026-04-23-sk-hynix-revenue-triples",
         "title": "A memory maker's revenue nearly triples in a year",
         "claim": "SK Hynix reported quarterly revenue up 198% year over year to about $35.55 "
                  "billion on surging memory prices, while Google unveiled its eighth-generation "
                  "TPUs and NIST built fingernail-sized photonic chips emitting any wavelength "
                  "from a single wafer.",
         "domain": "economics", "actor": ["sk-hynix", "google", "nist"], "score": "+198%",
         "evidences": ["compute-capital-stack", "vertical-silicon"],
         "supersedes": [B + "developments/2026-04-20-dram-meets-60-percent-of-demand"]},
        {"id": "2026-04-23-amazon-adds-25b-as-anthropic-commits-100b",
         "title": "A $25B investment meets a $100B commitment in the other direction",
         "claim": "Amazon is investing another $25 billion in Anthropic while Anthropic commits "
                  "more than $100 billion to AWS over the decade, and Microsoft pledged AU$25 "
                  "billion to expand in Australia.",
         "domain": "economics", "actor": ["amazon", "anthropic", "microsoft"], "score": "$25B / $100B",
         "evidences": ["compute-capital-stack", "debt-funded-buildout"],
         "supersedes": [B + "developments/2026-04-17-cerebras-files-at-35b-with-warrants"]},
        {"id": "2026-04-23-a-robot-beats-top-humans-at-a-physical-sport",
         "title": "A robot becomes the first machine to beat top humans at a physical sport",
         "claim": "Sony AI's autonomous table tennis robot became the first machine to beat "
                  "top-level humans in a physical sport, while Amazon's delivery drones were "
                  "reported dropping boxes from ten feet and bruising merchandise.",
         "domain": "robotics", "actor": ["sony-ai", "amazon"],
         "evidences": ["physical-recursion", "autonomy-clock-speed"],
         "supersedes": [B + "developments/2026-04-20-the-first-professional-robot-races"]},
        {"id": "2026-04-23-solars-largest-growth-ever-recorded",
         "title": "Solar posts the largest single-year growth ever recorded for any source",
         "claim": "The IEA confirmed 2025 as a turning point with solar's largest growth ever "
                  "recorded for any energy source and carbon-free power finally outpacing "
                  "demand, while CATL unveiled a 621-mile battery charging in under seven "
                  "minutes.",
         "domain": "energy", "actor": ["catl"], "score": "621 miles / <7 minutes",
         "evidences": ["burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-04-17-britain-asks-households-to-use-more-power"]},
        {"id": "2026-04-23-laser-comms-as-the-orbital-nervous-system",
         "title": "Artemis II validates laser links as the nervous system for orbital compute",
         "claim": "Artemis II validated laser communications as a nervous system for orbital "
                  "compute, with Observable Space planning terabit Earth-to-space links for "
                  "in-orbit data centers, while SpaceX agreed to optionally acquire Cursor for "
                  "$60 billion but is holding off to protect its listing.",
         "domain": "space", "actor": ["nasa", "observable-space", "spacex", "cursor"],
         "score": "$60B option",
         "evidences": ["orbit-as-compute", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-04-20-new-glenn-reuses-a-booster"]},
        {"id": "2026-04-23-organ-networks-grown-in-animal-wombs",
         "title": "Integrated organ networks are grown inside animal wombs",
         "claim": "Kind Biotechnology is growing integrated organ networks inside animal wombs "
                  "for transplant, Stanford found a bacterial enzyme that synthesizes long DNA "
                  "without a template, and airborne environmental DNA can now detect tigers at "
                  "two hundred metres.",
         "domain": "biotech", "actor": ["kind-biotechnology", "stanford"],
         "evidences": ["hardware-grade-biology", "biosphere-uplift"],
         "supersedes": [B + "developments/2026-04-20-pancreatic-vaccine-responders-alive-at-six-years"]},
        {"id": "2026-04-23-a-model-outperforms-physicians-on-a-clinical-benchmark",
         "title": "A model outperforms human physicians on a professional health benchmark",
         "claim": "OpenAI released a free clinician product and a professional health benchmark "
                  "on which GPT-5.4 outperforms all other models and human physicians, while "
                  "House Oversight began treating eleven dead or missing US scientists as a "
                  "national security matter.",
         "domain": "biotech", "actor": ["openai", "us-congress"], "score": "11 scientists",
         "evidences": ["work-displaced", "automated-science"],
         "supersedes": [B + "developments/2026-04-17-doomers-playing-with-fire"]},
        {"id": "2026-04-23-two-labs-reach-a-tenth-of-a-percent-of-gdp",
         "title": "Two labs each reach a tenth of a percent of US GDP",
         "claim": "Elad Gil noted OpenAI and Anthropic each already sit at 0.1% of US GDP with "
                  "one to two percent combined plausible within a year, while a new class of "
                  "startups brags about spending more on AI than on people.",
         "domain": "economics", "actor": ["openai", "anthropic"], "score": "0.1% of GDP each",
         "evidences": ["compute-capital-stack", "one-person-company"],
         "supersedes": [B + "developments/2026-04-17-capex-passes-apollo-and-the-marshall-plan"]},
        {"id": "2026-04-23-keystrokes-captured-and-surveillance-pricing-banned",
         "title": "A company captures employee keystrokes as a state bans surveillance pricing",
         "claim": "Meta began capturing employee keystrokes for a model capability programme, "
                  "Maryland became the first state to ban surveillance pricing, Microsoft paused "
                  "Copilot signups as token billing arrived with weekly costs doubling since "
                  "January, and Deezer reported 44% of daily uploads are AI-generated music.",
         "domain": "policy", "actor": ["meta", "maryland", "microsoft", "deezer"],
         "score": "44% of uploads",
         "evidences": ["compute-as-compensation", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-02-17-60000-ai-tracks-a-day"]},
    ],
}
