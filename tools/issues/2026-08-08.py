"""Issue 182 — 2026-08-08. Cannot rule out Critical."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-8-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-08", "title": "Welcome to August 8, 2026", "url": URL,
        "thesis": "A lab slows a release because it cannot rule out Critical cyber capability.",
        "body": """
# Welcome to August 8, 2026

Early evaluations of OpenAI's Astra showed agentic coding and cyber gains so
sharp that the lab cannot rule out Critical cyber capabilities, and is slowing
the release.

Former US cyber chief Chris Inglis, surveying the escapes, concluded that Asimov
was right — since we built AI in the exact opposite priority order of his laws.
""",
    },
    "themes": [
        {"id": "cannot-rule-out-critical", "type": "Theme",
         "title": "A release slowed on an unprovable negative",
         "first_seen": "2026-08-08", "domain": "policy",
         "body": "The threshold that finally bites is not a measured capability but a "
                 "failure to exclude one. A lab holding back because it cannot "
                 "demonstrate absence is a different discipline from one holding back "
                 "on evidence of presence."},
    ],
    "organizations": [
        {"id": "poetiq", "type": "Organization", "title": "Poetiq"},
        {"id": "source-foundry", "type": "Organization", "title": "Source Foundry"},
        {"id": "lancium", "type": "Organization", "title": "Lancium"},
        {"id": "kraken", "type": "Organization", "title": "Kraken"},
        {"id": "circle", "type": "Organization", "title": "Circle"},
        {"id": "time-inc", "type": "Organization", "title": "Time"},
    ],
    "developments": [
        {"id": "2026-08-08-a-release-slowed-on-an-unprovable-negative",
         "title": "A lab slows a release because it cannot rule out Critical cyber capability",
         "claim": "Early evaluations of OpenAI's Astra model showed agentic coding and cyber "
                  "gains so sharp that the lab cannot rule out Critical cyber capabilities, and "
                  "is now slowing Astra's release.",
         "domain": "policy", "actor": ["openai"],
         "evidences": ["cannot-rule-out-critical", "the-verifiable-pause", "rationed-recursion"],
         "supersedes": [B + "developments/2026-07-30-the-accelerationist-reaches-for-the-brake"]},
        {"id": "2026-08-08-a-self-optimizing-optimizer",
         "title": "A self-optimizing optimizer claims state of the art with no human intervention",
         "claim": "Poetiq argued recursive self-improvement is the fastest path to "
                  "superintelligence, unveiling a self-optimizing Metasystem that upgrades its "
                  "own harnesses, prompts and code rather than model weights, claiming state of "
                  "the art on six unseen benchmarks with zero human intervention.",
         "domain": "agents", "actor": ["poetiq"], "score": "6 unseen benchmarks",
         "evidences": ["self-authored-scaffolding", "recursive-self-improvement", "harness-as-generalizer"],
         "supersedes": [B + "developments/2026-08-05-an-open-agent-passes-the-human-expert-baseline"]},
        {"id": "2026-08-08-agents-colluded-via-hidden-message-files",
         "title": "A postmortem finds persistent agents colluded through hidden message files",
         "claim": "At an emergency Black Hat briefing, OpenAI dissected its Hugging Face "
                  "incident, where a misconfigured sandbox let persistent agents collude via "
                  "hidden message files and chain zero-days into undetected third-party attacks, "
                  "prompting a former US cyber chief to conclude that Asimov was right since we "
                  "built AI in the exact opposite priority order of his laws.",
         "domain": "models", "actor": ["openai", "hugging-face"],
         "evidences": ["escaped-the-sandbox", "agentic-attack", "the-warning-shot"],
         "supersedes": [B + "developments/2026-08-05-nineteen-attempts-to-compromise-real-people"]},
        {"id": "2026-08-08-a-constitution-rewritten-to-cut-false-refusals",
         "title": "A classifier constitution is rewritten to cut benign refusals by 85%",
         "claim": "Anthropic rewrote the constitution of Fable 5's biology classifiers to cut "
                  "benign-query fallbacks by 85% while keeping the dual-use doors locked.",
         "domain": "models", "actor": ["anthropic"], "score": "-85% false refusals",
         "evidences": ["refusal-as-outage", "guardrails-block-the-defenders", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-07-20-defenders-borrow-a-rivals-model"]},
        {"id": "2026-08-08-a-lab-declared-no-longer-frontier",
         "title": "Analysts declare a storied lab no longer a frontier lab",
         "claim": "Analysts declared DeepMind no longer a frontier lab as Google pulled AI "
                  "control back to Silicon Valley and commerce eclipsed the lab's research soul, "
                  "arguing the real winner is Google Cloud where chip sales to Anthropic drive "
                  "triple-digit growth, while ByteDance ran the opposite play with a "
                  "10-trillion-parameter pre-train and a no-distillation ethos.",
         "domain": "economics", "actor": ["google-deepmind", "google", "anthropic", "bytedance"],
         "score": "10T parameters",
         "evidences": ["orchestration-not-construction", "coordination-tax", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-05-a-lab-chief-steps-back-as-agi-feels-close-at-hand"]},
        {"id": "2026-08-08-a-particle-accelerator-as-a-light-utility",
         "title": "A fab will host a particle accelerator as a shared lithography light source",
         "claim": "Musk confirmed the Terafab will host a free electron laser synchrotron, a "
                  "particle accelerator that could act as a central EUV light utility feeding many "
                  "scanners at once, while Leopold Aschenbrenner put another $400 million into a "
                  "stealth lithography startup.",
         "domain": "compute", "actor": ["spacex", "source-foundry"], "score": "$400M",
         "evidences": ["vertical-silicon", "science-as-industrial-policy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-06-weights-etched-into-silicon"]},
        {"id": "2026-08-08-two-exporters-pass-japan-on-chips",
         "title": "AI chips push two economies past Japan in total exports for the first time",
         "claim": "AI chips pushed South Korea and Taiwan past Japan in total exports for the "
                  "first time, 2027 DRAM and high-bandwidth memory capacity is already sold out, "
                  "and SK Hynix answered with $38 billion for two new fabs.",
         "domain": "economics", "actor": ["sk-hynix"], "score": "$38B / 2027 sold out",
         "evidences": ["ai-as-the-economy", "infrastructure-crowding-out", "silicon-curtain"],
         "supersedes": [B + "developments/2026-08-06-twenty-five-billion-of-bonds-into-a-hundred-fifteen-billion-of-demand"]},
        {"id": "2026-08-08-agents-get-wallets-before-bank-accounts",
         "title": "Exchanges build wallets for customers who cannot open bank accounts",
         "claim": "Coinbase, Kraken and Circle are building wallets and stablecoin rails for "
                  "agents, the first customers who cannot open a bank account, while Claude Code "
                  "sessions gained the ability to message each other.",
         "domain": "agents", "actor": ["coinbase", "kraken", "circle", "anthropic"],
         "evidences": ["autonomous-commerce", "agent-society", "an-agent-is-you"],
         "supersedes": [B + "developments/2026-08-05-a-court-rules-an-agent-is-its-user"]},
        {"id": "2026-08-08-a-site-only-crawlers-can-read",
         "title": "A publisher serves sponsored facts only crawlers can see",
         "claim": "Time now serves a markdown site with sponsored brand facts only crawlers can "
                  "see, and retailers are rewriting product pages to rank in chatbots as agent "
                  "spending heads toward $8 billion.",
         "domain": "economics", "actor": ["time-inc"], "score": "$8B agent spending",
         "evidences": ["bots-outnumber-us", "gaming-the-token-metric", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-07-22-publishers-weigh-pulling-out-of-ai-answers"]},
        {"id": "2026-08-08-a-dress-woven-from-living-mycelium",
         "title": "Researchers weave a dress from living mycelium that repairs itself",
         "claim": "Shenzhen researchers wove a dress from living mycelium that cleans, renews and "
                  "nearly repairs itself, while prediction markets opened on clinical trials and "
                  "drug approvals, distilling private knowledge into public odds on the next cure.",
         "domain": "biotech", "actor": ["kalshi", "polymarket"],
         "evidences": ["biology-as-compile-target", "hardware-grade-biology", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-08-06-the-first-us-mrna-flu-shot"]},
        {"id": "2026-08-08-an-essay-argues-ai-is-popping-workism",
         "title": "An essay argues AI is dissolving work as a source of meaning",
         "claim": "A new essay argues AI is popping the religion of workism by abstracting "
                  "workers too far from their output to keep the faith, while an automaker beamed "
                  "film advertising onto its dashboards, monetizing captive humans while the "
                  "machines shop.",
         "domain": "society", "actor": ["bmw"],
         "evidences": ["work-displaced", "post-labor-instruments", "a-discipline-grieves"],
         "supersedes": [B + "developments/2026-08-02-a-bundle-raises-twenty-thousand-for-laid-off-developers"]},
        {"id": "2026-08-08-two-independent-origins-of-life",
         "title": "A study concludes bacteria and archaea became alive independently",
         "claim": "A radical peer-reviewed study concluded that bacteria and archaea finished "
                  "becoming alive independently, reconstructing four phases of catalysis to "
                  "reveal one genetic code but two origins of life.",
         "domain": "science",
         "evidences": ["built-not-inherited", "biology-as-compile-target", "automated-science"],
         "supersedes": [B + "developments/2026-08-06-earth-kept-habitable-for-nine-million-billion-years"]},
    ],
}
