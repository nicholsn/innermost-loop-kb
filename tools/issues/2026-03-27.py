"""Issue 084 — 2026-03-27. Machines outwrite us."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-27-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-27", "title": "Welcome to March 27, 2026", "url": URL,
        "thesis": "Machine-written output passes human-written output, and a benchmark restores the gap.",
        "body": """
# Welcome to March 27, 2026

ARK projects that AI-written output exceeded human-written output in 2025 for
the first time. Wikipedia responded by banning editors from writing or rewriting
articles with AI.

And ARC-AGI-3 launched with 135 environments trivial for humans and humbling for
machines: Gemini 3.1 Pro at 0.37%, GPT-5.4 at 0.26%, Grok at 0%. Then a
scaffolding SDK claimed 36% on day one for $1,005, where Opus spent $8,900 to
reach a quarter of a percent.
""",
    },
    "organizations": [
        {"id": "wikipedia", "type": "Organization", "title": "Wikipedia",
         "resource": "https://www.wikipedia.org/"},
        {"id": "symbolica", "type": "Organization", "title": "Symbolica",
         "body": "Agentica SDK claimed 36% on ARC-AGI-3 at a fraction of frontier cost."},
        {"id": "mirendil", "type": "Organization", "title": "Mirendil",
         "body": "Former Anthropic researchers building self-accelerating AI R&D."},
        {"id": "fannie-mae", "type": "Organization", "title": "Fannie Mae",
         "resource": "https://www.fanniemae.com/"},
        {"id": "canada-immigration", "type": "Organization", "title": "Immigration, Refugees and Citizenship Canada",
         "body": "Using generative AI to review permanent residence applications."},
    ],
    "developments": [
        {"id": "2026-03-27-machines-outwrite-humans",
         "title": "AI written output passes human written output",
         "claim": "ARK Invest projects that AI-written output exceeded human-written output in "
                  "2025 for the first time in history, and Wikipedia responded by banning "
                  "editors from writing or rewriting articles using AI.",
         "domain": "society", "actor": ["ark-invest", "wikipedia"],
         "evidences": ["work-displaced", "agent-exclusion"],
         "supersedes": [B + "developments/2026-03-22-search-replaces-headlines-with-generated-text"]},
        {"id": "2026-03-27-arc-agi-3-humbles-the-frontier",
         "title": "A new benchmark returns frontier models to near zero",
         "claim": "ARC-AGI-3 launched with 135 novel game environments designed to be trivial "
                  "for humans and humbling for machines, with Gemini 3.1 Pro scoring 0.37%, "
                  "GPT-5.4 0.26%, Opus 4.6 0.25% and Grok 4.2 zero.",
         "domain": "benchmarks", "actor": ["arc-prize"], "about": [B + "benchmarks/arc-agi-3"],
         "score": "0.37% best",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-03-24-first-frontiermath-open-problem-solved"],
         "body": "The first benchmark in months to open a gap rather than close one."},
        {"id": "2026-03-27-scaffolding-beats-weights-at-a-ninth-the-cost",
         "title": "A scaffolding SDK claims 36% where a frontier model reached 0.25%",
         "claim": "Symbolica's Agentica SDK claimed an unverified 36.08% on ARC-AGI-3 on day "
                  "one, passing 113 of 182 levels for $1,005, while Opus 4.6 spent $8,900 to "
                  "reach 0.25%.",
         "domain": "benchmarks", "actor": ["symbolica"], "score": "36.08% for $1,005",
         "evidences": ["scaffolding-over-weights", "reasoning-price-deflation"],
         "body": "The next leap may come from rethinking the harness rather than scaling the "
                 "weights."},
        {"id": "2026-03-27-claude-mythos-leaked",
         "title": "A tier above Opus leaks and is deleted",
         "claim": "Anthropic leaked and then deleted an announcement of Claude Mythos, a tier "
                  "above Opus with substantially higher scores in coding, reasoning and "
                  "cybersecurity, while Mirendil launched to build self-accelerating AI R&D.",
         "domain": "models", "actor": ["anthropic", "mirendil"],
         "evidences": ["recursive-self-improvement", "spiky-frontier"]},
        {"id": "2026-03-27-apple-opens-siri-to-rivals",
         "title": "Apple negotiates model weights and opens Siri to outside assistants",
         "claim": "Apple reportedly negotiated complete access to Gemini's weights in its own "
                  "data centers with distillation rights for on-device models, and plans to "
                  "open Siri to outside AI assistants in iOS 27, letting users route queries to "
                  "Google, Anthropic or anyone from the App Store.",
         "domain": "models", "actor": ["apple", "google", "anthropic"],
         "evidences": ["network-over-node", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-01-24-apple-campos-replaces-siri"]},
        {"id": "2026-03-27-openai-ad-revenue-passes-100m",
         "title": "Ad revenue passes $100M six weeks in, and adult mode is shelved",
         "claim": "OpenAI surpassed $100 million in annualized advertising revenue six weeks "
                  "after its pilot launched, but shelved its adult mode indefinitely after "
                  "staff and investor pushback.",
         "domain": "economics", "actor": ["openai"], "score": "$100M annualized",
         "evidences": ["autonomous-commerce", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-03-17-adult-mode-and-real-world-relationships"]},
        {"id": "2026-03-27-datacenter-moratorium-act",
         "title": "A federal datacenter moratorium bill is introduced",
         "claim": "Senator Sanders and Representative Ocasio-Cortez introduced the AI Data "
                  "Center Moratorium Act proposing a federal pause on new data centers until "
                  "safety guardrails exist, while a White House adviser suggested Congress could "
                  "pass bipartisan AI standards within months.",
         "domain": "policy", "actor": ["us-congress", "white-house"],
         "evidences": ["legislating-the-shift", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-03-18-rural-ohio-would-ban-large-datacenters"]},
        {"id": "2026-03-27-anthropic-wins-an-injunction",
         "title": "A court keeps the blacklisted lab's contracts alive",
         "claim": "Anthropic won a preliminary injunction in its lawsuit to reverse the "
                  "Department of War's blacklisting, keeping its government contracts alive by "
                  "court order, while Canada's immigration department began using generative AI "
                  "to review permanent residence applications.",
         "domain": "policy", "actor": ["anthropic", "war-department", "canada-immigration"],
         "evidences": ["refusal-as-differentiator", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-10-anthropic-sues-the-pentagon"]},
        {"id": "2026-03-27-hypersonic-missiles-at-99000-dollars",
         "title": "Hypersonic missiles are mass-produced at $99,000 each",
         "claim": "A Chinese private company is mass-producing hypersonic missiles at $99,000 "
                  "apiece, launched from containers disguisable as shipping crates, collapsing "
                  "the cost of precision strike by orders of magnitude.",
         "domain": "policy", "actor": ["china"], "score": "$99,000",
         "evidences": ["autonomy-clock-speed", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-03-24-cloud-workloads-migrate-because-of-strikes"]},
        {"id": "2026-03-27-tradable-compute-price-index",
         "title": "Compute gets a tradable price index",
         "claim": "Ornn announced the first tradable AI compute price index, financializing "
                  "GPU-hours into a commodity as legible as crude oil, while Anthropic "
                  "executives discussed a listing as soon as the fourth quarter expecting to "
                  "raise more than $60 billion.",
         "domain": "economics", "actor": ["ornn", "anthropic"], "score": "$60B",
         "evidences": ["compute-capital-stack", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-03-03-765kv-lines-return"]},
        {"id": "2026-03-27-crypto-backed-mortgages",
         "title": "A mortgage giant will accept crypto as collateral",
         "claim": "Fannie Mae will soon accept crypto-backed mortgages for the first time, "
                  "letting buyers pledge digital holdings instead of selling them.",
         "domain": "economics", "actor": ["fannie-mae"],
         "evidences": ["autonomous-commerce"]},
        {"id": "2026-03-27-a-humanoid-visits-the-white-house",
         "title": "A humanoid robot walks into the White House",
         "claim": "Figure's F.03 became the first humanoid robot to visit the White House, "
                  "walking alongside the First Lady into an educational summit of international "
                  "first spouses as a military orchestra played.",
         "domain": "robotics", "actor": ["figure", "white-house"],
         "evidences": ["physical-recursion", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-25-amazon-acquires-a-humanoid-startup"]},
        {"id": "2026-03-27-tribe-v2-predicts-brain-responses",
         "title": "A model trained on 1,000 hours of fMRI predicts brain responses",
         "claim": "Meta released TRIBE v2, a tri-modal foundation model trained on over a "
                  "thousand hours of fMRI across 720 subjects, predicting high-resolution brain "
                  "responses to novel stimuli and recovering decades of empirical neuroscience "
                  "in a single training run.",
         "domain": "science", "actor": ["meta"], "score": "1,000 hours / 720 subjects",
         "evidences": ["architecture-of-mind", "automated-science"],
         "supersedes": [B + "developments/2026-03-25-agents-run-physics-analysis-pipelines"]},
        {"id": "2026-03-27-gateway-scrapped-for-a-lunar-base",
         "title": "NASA scraps the lunar gateway for a south pole base",
         "claim": "NASA scrapped the Lunar Gateway in favor of a three-phase lunar base "
                  "programme targeting permanent south pole infrastructure for $20 billion over "
                  "seven years, while SpaceX's president said her long-term goal is to meet "
                  "another sentient species.",
         "domain": "space", "actor": ["nasa", "spacex"], "score": "$20B / 7 years",
         "evidences": ["inhabitable-worlds"],
         "supersedes": [B + "developments/2026-03-25-lunar-mass-drivers-double-as-weapons"]},
    ],
}
