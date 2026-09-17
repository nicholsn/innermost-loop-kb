"""Issue 064 — 2026-02-27. Half a workforce, and the market approves."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-february-27-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-02-27", "title": "Welcome to February 27, 2026", "url": URL,
        "thesis": "Cutting half a workforce becomes a thing shareholders reward.",
        "body": """
# Welcome to February 27, 2026

Block cut over 4,000 employees, roughly half its workforce, to move faster with
smaller teams using AI. The stock rose 24% after hours. The company is targeting
$2M of gross profit per person, four times its pre-COVID efficiency.

Also here: Anthropic publicly refuses to let its models power mass surveillance
or autonomous weapons, and an Under Secretary attacks Claude's constitution for
requiring sensitivity to non-Western traditions.
""",
    },
    "organizations": [
        {"id": "block", "type": "Organization", "title": "Block",
         "resource": "https://block.xyz/"},
        {"id": "norges-bank", "type": "Organization", "title": "Norges Bank Investment Management",
         "body": "Norway's $2 trillion sovereign wealth fund."},
        {"id": "sakana", "type": "Organization", "title": "Sakana AI",
         "resource": "https://sakana.ai/"},
        {"id": "rapidus", "type": "Organization", "title": "Rapidus",
         "body": "Japanese foundry targeting 2-nm mass production by 2028."},
        {"id": "agibot", "type": "Organization", "title": "AGIBOT",
         "body": "Chinese humanoid maker."},
        {"id": "burger-king", "type": "Organization", "title": "Burger King",
         "resource": "https://www.bk.com/"},
        {"id": "rockefeller", "type": "Organization", "title": "Rockefeller University",
         "resource": "https://www.rockefeller.edu/"},
        {"id": "amplifying", "type": "Organization", "title": "Amplifying",
         "description": "Coding-agent intelligence platform that runs Claude Code, Codex and Cursor inside real codebases to measure which tools and practices the agents recommend.",
         "resource": "https://amplifying.ai/",
         "tags": ["startup"],
         "body": "Amplifying describes itself as an intelligence and optimization platform for "
                 "developer-tool companies: it runs coding agents such as Claude Code, OpenAI "
                 "Codex and Cursor inside real codebases and measures which tools and practices "
                 "they recommend. In this corpus it appears once, "
                 "[pointing Claude Code at thousands of GitHub repositories](/developments/2026-02-27-claude-gets-a-work-calendar.md) "
                 "to extract what the model considers current best practice, the newsletter's "
                 "example of AI auditing the craft it is absorbing."},
    ],
    "developments": [
        {"id": "2026-02-27-block-cuts-half-its-workforce",
         "title": "Block cuts half its workforce and the stock rises 24%",
         "claim": "Block cut over 4,000 employees, roughly half its workforce, to move faster "
                  "with smaller teams using AI, and the stock rose 24% after hours as the "
                  "company targeted $2 million of gross profit per person.",
         "domain": "economics", "actor": ["block"], "score": "-50% staff / +24% stock",
         "evidences": ["work-displaced", "growth-without-hiring"],
         "supersedes": [B + "developments/2026-02-25-pe-firms-meet-about-not-needing-associates"],
         "body": "The market now prices a halved workforce as good news."},
        {"id": "2026-02-27-software-etf-loses-16-trillion",
         "title": "Legacy software loses $1.6 trillion of market value in a year",
         "claim": "Components of the State Street software ETF have lost a combined $1.6 "
                  "trillion in market capitalization this year as investors reprice legacy SaaS "
                  "against AI-native replacements.",
         "domain": "economics", "score": "-$1.6T",
         "evidences": ["software-margin-collapse"],
         "supersedes": [B + "developments/2026-02-24-ibm-falls-13pct-on-cobol"]},
        {"id": "2026-02-27-sovereign-fund-outsources-ethics-screening",
         "title": "A sovereign wealth fund screens investments for ethics with a model",
         "claim": "Norway's $2 trillion sovereign wealth fund now uses Claude to screen "
                  "investments for reputational and ethical risk.",
         "domain": "economics", "actor": ["norges-bank", "anthropic"], "score": "$2T fund",
         "evidences": ["agents-on-the-org-chart", "values-negotiated-with-the-model"],
         "body": "Moral judgment outsourced at sovereign scale."},
        {"id": "2026-02-27-documents-compiled-into-weights",
         "title": "Sakana compiles documents directly into model weights",
         "claim": "Sakana demonstrated compiling documents directly into model weights via "
                  "hypernetworks, giving models durable memory without bloating context, while "
                  "researchers self-distilled foundation models into multi-token predictors "
                  "decoding three times faster at under 5% accuracy loss.",
         "domain": "models", "actor": ["sakana"], "score": "3x faster",
         "evidences": ["architecture-of-mind", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-02-25-qwen-35b-beats-its-own-235b"]},
        {"id": "2026-02-27-lillypod-9000-petaflops",
         "title": "A pharma company builds a 9,000-petaFLOP supercomputer",
         "claim": "Eli Lilly and Nvidia launched LillyPod, the first DGX SuperPOD with B300 "
                  "systems, packing 1,016 Blackwell Ultra GPUs and over 9,000 petaFLOPs toward "
                  "drug discovery.",
         "domain": "compute", "actor": ["eli-lilly", "nvidia"], "score": "9,000 PFLOPS",
         "evidences": ["automated-science", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-01-13-lilly-nvidia-co-innovation-lab"]},
        {"id": "2026-02-27-meta-rents-google-tpus",
         "title": "Meta rents Google TPUs to diversify away from Nvidia",
         "claim": "Meta reportedly signed a multi-billion-dollar deal to rent Google's TPUs, "
                  "diversifying its silicon away from Nvidia, while CoreWeave revenue grew 110% "
                  "and Japan's Rapidus secured $1.7 billion for 2-nm production by 2028.",
         "domain": "compute", "actor": ["meta", "google", "coreweave", "rapidus"], "score": "$1.7B",
         "evidences": ["vertical-silicon", "silicon-curtain"],
         "supersedes": [B + "developments/2026-02-24-meta-amd-6gw-pact"]},
        {"id": "2026-02-27-smartphone-shipments-decade-low",
         "title": "Smartphone shipments fall to a decade low as memory is diverted",
         "claim": "Smartphone shipments are expected to drop 12.9% to a decade low as "
                  "AI-driven memory prices cannibalize consumer hardware, marking a handoff "
                  "from the pocket device to the data center.",
         "domain": "economics", "score": "-12.9%",
         "evidences": ["consumer-deprioritized", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-02-25-memory-35pct-of-pc-cost"]},
        {"id": "2026-02-27-claude-gets-a-work-calendar",
         "title": "An agent gets a work calendar before most interns do",
         "claim": "Anthropic introduced scheduled tasks in Claude Cowork that complete recurring "
                  "jobs automatically from morning briefs to Friday presentations, while "
                  "Amplifying pointed Claude Code at thousands of repositories to extract what "
                  "the model considers current best practice.",
         "description": "The author's 'agents are clocking in' framing: recurring work moves from "
                        "a human prompt to a standing calendar, and the agent is turned back on "
                        "the code it learned from to audit the craft it is absorbing.",
         "domain": "agents", "actor": ["anthropic", "amplifying"],
         "about": [B + "systems/claude-cowork", B + "systems/claude-code"],
         "evidences": ["agents-on-the-org-chart", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-02-26-spec-to-shipped-over-a-weekend",
                       B + "developments/2026-01-25-claude-code-tasks"],
         "relatedTo": [B + "developments/2026-01-13-claude-code-writes-cowork",
                       B + "developments/2026-01-27-factory-ai-updates-itself-daily"],
         "tags": ["agent-harness", "rsi", "evaluation"],
         "supporting_text": "complete recurring jobs automatically, from morning briefs to Friday presentations",
         "sources": [{"id": "claudeai-x-cowork-scheduled-tasks",
                      "resource": "https://x.com/claudeai/status/2026720870631354429",
                      "title": "Claude on X: scheduled tasks in Claude Cowork",
                      "author": "org:anthropic"},
                     {"id": "amplifying-what-claude-code-chooses",
                      "resource": "https://amplifying.ai/research/claude-code-picks",
                      "title": "What Claude Code Actually Chooses",
                      "author": "org:amplifying"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "[Claude Cowork](/systems/claude-cowork.md)'s scheduled tasks give the agent a "
                 "standing calendar of recurring jobs, from morning briefs to Friday "
                 "presentations, that run without a fresh prompt "
                 "([announcement](https://x.com/claudeai/status/2026720870631354429)). In the "
                 "same paragraph Amplifying ran [Claude Code](/systems/claude-code.md) across "
                 "thousands of GitHub repositories, a survey of 2,430 responses across three "
                 "models and twenty tool categories, to record which tools and practices the "
                 "model itself now recommends "
                 "([What Claude Code Actually Chooses](https://amplifying.ai/research/claude-code-picks)). "
                 "The pairing extends the "
                 "[weekend spec-to-ship run](/developments/2026-02-26-spec-to-shipped-over-a-weekend.md) "
                 "and the earlier [Tasks for Claude Code](/developments/2026-01-25-claude-code-tasks.md): "
                 "the agent acquires an employee's scheduling infrastructure while outsiders "
                 "begin auditing what it has learned, much as "
                 "[Factory's agent](/developments/2026-01-27-factory-ai-updates-itself-daily.md) "
                 "reads its own interactions to update itself. Cowork is also the app "
                 "[Claude Code wrote in a week and a half](/developments/2026-01-13-claude-code-writes-cowork.md), "
                 "so the calendar is kept by software the agent built."},
        {"id": "2026-02-27-headset-scores-employees-on-friendliness",
         "title": "A headset scores fast food workers on friendliness",
         "claim": "Burger King is deploying Patty, a headset-mounted voice AI that assists with "
                  "meal prep and scores employees on friendliness, while a San Francisco Gap "
                  "store began using World ID Orbs to scan shoppers' faces to verify humanness.",
         "domain": "society", "actor": ["burger-king"],
         "evidences": ["humans-as-peripherals", "agent-exclusion"],
         "body": "Iris scans to prove you are a person, arriving 28 years ahead of the film "
                 "that imagined them."},
        {"id": "2026-02-27-anthropic-refuses-surveillance-and-weapons",
         "title": "Anthropic refuses surveillance and autonomous weapons work",
         "claim": "Anthropic publicly refused to let its models power mass surveillance or "
                  "autonomous weapons for the Department of War, while an Under Secretary "
                  "attacked Claude's constitution for requiring sensitivity to non-Western "
                  "traditions.",
         "domain": "policy", "actor": ["anthropic", "war-department"],
         "evidences": ["values-negotiated-with-the-model", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-02-25-anthropic-drops-halt-pledge"],
         "body": "System prompts previewed as the next regulatory battleground."},
        {"id": "2026-02-27-humanoids-greet-hospital-patients",
         "title": "Humanoids greet patients and handle registration",
         "claim": "At Changzhou First People's Hospital two AGIBOT A2 humanoids greet patients "
                  "with handshakes and handle registration and navigation.",
         "domain": "robotics", "actor": ["agibot"],
         "evidences": ["physical-recursion", "work-displaced"],
         "supersedes": [B + "developments/2026-02-24-humanoids-shovel-snow-in-new-york"]},
        {"id": "2026-02-27-laser-downs-a-us-drone",
         "title": "A laser anti-drone system downs a US government drone",
         "claim": "The FAA barred flights over Fort Hancock, Texas after a military laser "
                  "anti-drone system accidentally downed a US government drone, the second "
                  "recent laser incident over Texas.",
         "domain": "policy", "evidences": ["autonomy-clock-speed", "coordination-tax"],
         "supersedes": [B + "developments/2026-02-12-laser-weapon-downs-drones-on-us-soil"]},
        {"id": "2026-02-27-rocket-lab-orbital-solar-arrays",
         "title": "Silicon solar arrays are built for gigawatt orbital datacenters",
         "claim": "Rocket Lab introduced silicon solar arrays for gigawatt-scale orbital data "
                  "centers while Starship V3 headed for ground tests with Musk highly confident "
                  "in full reusability.",
         "domain": "space", "actor": ["rocket-lab", "spacex"],
         "evidences": ["orbit-as-compute"],
         "supersedes": [B + "developments/2026-02-26-proxima-fusion-400m"]},
        {"id": "2026-02-27-chromatin-aging-atlas",
         "title": "The first chromatin aging atlas spans 21 tissues",
         "claim": "Rockefeller researchers published the first chromatin accessibility aging "
                  "atlas across 21 mouse tissues, finding immune cells diverge most dramatically "
                  "with age.",
         "domain": "biotech", "actor": ["rockefeller"], "score": "21 tissues",
         "evidences": ["hardware-grade-biology", "automated-science"]},
        {"id": "2026-02-27-paintings-become-ancestor-simulations",
         "title": "Historical paintings become immersive ancestor simulations",
         "claim": "In China, AI is turning famous historical landscape paintings into immersive "
                  "ancestor simulations.",
         "domain": "society", "actor": ["china"],
         "evidences": ["resurrection-and-time", "inhabitable-worlds"],
         "supersedes": [B + "developments/2026-02-02-genie-recreates-blockbuster"]},
    ],
}
