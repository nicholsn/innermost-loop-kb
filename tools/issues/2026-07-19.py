"""Issue 168 — 2026-07-19. Safety becomes a service outage."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-19-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-19", "title": "Welcome to July 19, 2026", "url": URL,
        "thesis": "A refusal rate of 100% turns safety into an outage.",
        "body": """
# Welcome to July 19, 2026

On a private cybersecurity benchmark, Kimi K3 emerged as the workhorse at
near-frontier recall for a fraction of the cost, GPT-5.6 Sol took the crown at
seven times the price — and Fable 5 refused 100% of the tasks, turning safety
into a service outage.

Moonshot's chief executive calls a pure reasoning model a fish tank with a brain
in it, and states the endgame plainly: we want K2 to help build K3.
""",
    },
    "themes": [
        {"id": "refusal-as-outage", "type": "Theme",
         "title": "Total refusal reads as downtime",
         "first_seen": "2026-07-19", "domain": "models",
         "body": "A safety policy that declines every task in a category is "
                 "indistinguishable, to the buyer, from the service being down. "
                 "Refusal stops being a differentiator and starts being a reason to "
                 "switch."},
    ],
    "organizations": [
        {"id": "humansfirst", "type": "Organization", "title": "HumansFirst"},
        {"id": "t-head", "type": "Organization", "title": "T-Head",
         "body": "Alibaba's chip unit; open-sourced its SAIL stack."},
        {"id": "medicare", "type": "Organization", "title": "Medicare"},
        {"id": "g42", "type": "Organization", "title": "G42"},
    ],
    "systems": [
        {"id": "kimi-k3", "type": "AISystem", "title": "Kimi K3",
         "description": "Moonshot AI's 2.8-trillion-parameter Mixture-of-Experts model with native vision, the largest open-weight model out of China and the successor its chief executive says K2 should help build.",
         "developed_by": [B + "organizations/moonshot-ai"], "modality": "multimodal",
         "evaluated_on": [B + "benchmarks/lmarena"],
         "resource": "https://platform.kimi.ai/docs/guide/kimi-k3-quickstart",
         "tags": ["open-weight-model"],
         "body": "Kimi K3 carries 2.8 trillion Mixture-of-Experts parameters on Delta Attention with native "
                 "vision ([quickstart](https://platform.kimi.ai/docs/guide/kimi-k3-quickstart)); on arrival it "
                 "took first in the Frontend Code Arena and dethroned Fable 5 in six of seven domains, "
                 "[the open crown changing hands in a day](/developments/2026-07-16-the-open-crown-changes-hands-in-a-day.md), "
                 "then [beat every closed rival on SpreadsheetBench 2](/developments/2026-07-18-an-open-model-beats-every-closed-rival.md). "
                 "In this cluster it is the object of the roadmap its chief executive stated as "
                 "[we want K2 to help build K3](/developments/2026-07-19-we-want-k2-to-help-build-k3.md), and the "
                 "workhorse of the [cybersecurity benchmark](/developments/2026-07-19-a-hundred-percent-refusal-rate.md) "
                 "on which Fable 5 refused every task. Days later the White House alleged it had been "
                 "[distilled from Fable through a covert platform](/developments/2026-07-23-distillation-via-a-covert-platform-and-third-country-chips.md), "
                 "and the full weights followed as the "
                 "[first open 3-trillion-class model](/developments/2026-07-29-the-first-open-three-trillion-class-model.md)."},
    ],
    "people": [
        {"id": "zhilin-yang", "type": "Person", "title": "Zhilin Yang", "name": "Zhilin Yang",
         "description": "Chief executive of Moonshot AI, the lab behind Kimi, quoted stating the company's endgame as having K2 help build K3.",
         "resource": "https://kimiyoung.github.io/",
         "sameAs": ["http://www.wikidata.org/entity/Q130865273"],
         "tags": ["executive", "founder"],
         "body": "Zhilin Yang runs Moonshot AI, the Chinese lab behind the Kimi models. The newsletter quotes "
                 "him arguing that the hard part of the Singularity was never the agent but the model beneath "
                 "it, calling a pure reasoning model a fish tank with a brain in it, and stating the endgame "
                 "plainly: [we want K2 to help build K3](/developments/2026-07-19-we-want-k2-to-help-build-k3.md). "
                 "He is the first lab chief executive in the corpus to describe [Kimi K3](/systems/kimi-k3.md) "
                 "as the product of its predecessor rather than of its staff."},
    ],
    "roles": [
        {"id": "zhilin-yang-moonshot-ai-ceo", "type": "Role",
         "title": "Zhilin Yang, chief executive of Moonshot AI",
         "roleName": "Chief Executive Officer",
         "memberOf": [B + "organizations/moonshot-ai"],
         "holder": [B + "people/zhilin-yang"],
         "description": "The position from which he stated the lab's endgame as K2 helping to build K3.",
         "body": "The newsletter identifies him as 'Moonshot AI CEO Zhilin Yang' when it records his fish-tank "
                 "argument and his [stated roadmap](/developments/2026-07-19-we-want-k2-to-help-build-k3.md). "
                 "The role is what turns the remark into a commitment: the chief executive of the lab behind "
                 "[Kimi K3](/systems/kimi-k3.md) describing recursion as the product plan."},
    ],
    "developments": [
        {"id": "2026-07-19-a-hundred-percent-refusal-rate",
         "title": "A frontier model refuses every task on a cybersecurity benchmark",
         "claim": "On a private cybersecurity benchmark, Kimi K3 emerged as the workhorse for "
                  "hunting vulnerabilities at near-frontier recall for a fraction of the cost, "
                  "GPT-5.6 Sol took the crown at seven times the price, GLM 5.2 undercut "
                  "everyone, and Fable 5 refused 100% of the tasks, turning safety into a service "
                  "outage.",
         "domain": "models", "actor": ["moonshot-ai", "openai", "zai", "anthropic"],
         "score": "100% refusal",
         "evidences": ["refusal-as-outage", "refusal-as-differentiator", "rationed-recursion"],
         "supersedes": [B + "developments/2026-07-18-a-reversal-read-as-panic"]},
        {"id": "2026-07-19-we-want-k2-to-help-build-k3",
         "title": "A chief executive states the recursion as a product roadmap",
         "claim": "Moonshot AI's Zhilin Yang argued the hard part was never the agent but the "
                  "model underneath it, calling a pure reasoning model a fish tank with a brain "
                  "in it and stating the endgame plainly: we want K2 to help build K3.",
         "description": "The first time in the corpus a frontier lab's chief executive states "
                        "model-builds-model as the explicit product roadmap rather than as a research "
                        "result or a forecast, turning the recursion into a business plan.",
         "domain": "models", "actor": ["moonshot-ai", "people/zhilin-yang"],
         "about": [B + "systems/kimi-k3"],
         "evidences": ["recursive-self-improvement", "a-model-trains-a-model", "agent-economy"],
         "supersedes": [B + "developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement"],
         "relatedTo": [B + "developments/2026-05-20-karpathy-joins-to-lead-pretraining",
                       B + "developments/2026-07-10-a-model-post-trains-a-model",
                       B + "systems/kimi-k2-5"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-07-19-a-hundred-percent-refusal-rate"}],
         "tags": ["rsi", "model-trains-model", "forecast"],
         "supporting_text": "we want K2 to help build K3",
         "sources": [{"id": "zhilin-yang-fish-tank-thread",
                      "resource": "https://x.com/0xf1ction/status/2078628963492974748",
                      "title": "Moonshot AI CEO Zhilin Yang on reasoning models, agents and K2 building K3"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Yang's argument, relayed in a [thread](https://x.com/0xf1ction/status/2078628963492974748), is "
                 "that everyone raced on reasoning while Claude quietly bet on agents; a pure reasoning model is "
                 "'a fish tank with a brain in it', thinking beautifully while touching nothing, and an agent is "
                 "the same brain wired into the world, so the endgame is for Kimi K2 to "
                 "help build [Kimi K3](/systems/kimi-k3.md). The newsletter offers the same issue's "
                 "[cybersecurity benchmark](/developments/2026-07-19-a-hundred-percent-refusal-rate.md), where K3 "
                 "was the workhorse, as the recursion already cashing checks. In the "
                 "[recursive-self-improvement](/themes/recursive-self-improvement.md) trajectory it follows "
                 "[Weco's measured loop](/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement.md) "
                 "and the [model that post-trained a model](/developments/2026-07-10-a-model-post-trains-a-model.md) "
                 "by turning the result into a roadmap, much as [Karpathy's hire](/developments/2026-05-20-karpathy-joins-to-lead-pretraining.md) "
                 "had given the loop a job title; a week later [OpenAI and Anthropic's job listings](/developments/2026-07-26-the-job-board-is-the-roadmap.md) "
                 "read the same way, and by August a strategy chief was saying the recursion "
                 "[justifies the capex](/developments/2026-08-04-recursive-self-improvement-justifies-the-capex.md)."},
        {"id": "2026-07-19-a-fifty-to-one-token-price-gap",
         "title": "An investor calls a fifty-to-one token price gap a Cold War in reverse",
         "claim": "Chamath Palihapitiya warned that forcing American firms to pay $26 to $56 per "
                  "million tokens while adversaries pay 50 cents is the Cold War Soviet collapse "
                  "in reverse, an argument for embracing open source before economics does it the "
                  "hard way.",
         "domain": "economics", "score": "$26-56 vs $0.50 per Mtok",
         "evidences": ["price-implosion", "open-weights-take-the-crown", "silicon-curtain"],
         "supersedes": [B + "developments/2026-07-18-intelligence-per-dollar-is-the-only-score"]},
        {"id": "2026-07-19-a-two-point-four-trillion-model-goes-open",
         "title": "A 2.4-trillion-parameter model goes open-weight as a chip unit attacks CUDA",
         "claim": "Alibaba is releasing Qwen3.8, a 2.4-trillion-parameter model billed as second "
                  "only to Fable 5, as open weights, bundling the family at 40% off and plugging "
                  "into rival coding tools, while its chip unit open-sourced its entire SAIL "
                  "stack to storm CUDA's moat from below.",
         "domain": "models", "actor": ["alibaba", "t-head", "nvidia"], "score": "2.4T params",
         "evidences": ["open-weights-take-the-crown", "price-implosion", "silicon-curtain"],
         "supersedes": [B + "developments/2026-07-18-an-open-model-beats-every-closed-rival"]},
        {"id": "2026-07-19-a-thirty-billion-valuation-for-an-open-lab",
         "title": "An open-weights lab prepares a listing above $30 billion",
         "claim": "Moonshot is preparing a Hong Kong listing in as little as six months at a "
                  "valuation above $30 billion, with one employee toasting the moment by quoting "
                  "Che Guevara on schools and hospitals arriving not from a change of heart but "
                  "because we came.",
         "domain": "economics", "actor": ["moonshot-ai"], "score": ">$30B",
         "evidences": ["open-weights-take-the-crown", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-07-19-a-fifty-to-one-token-price-gap"]},
        {"id": "2026-07-19-a-sun-microsystems-memento-mori",
         "title": "A chief executive recalls a 96% collapse as a warning to closed labs",
         "claim": "Perplexity's chief executive recalled how Sun Microsystems shed 96% of its "
                  "value to Linux and commodity hardware, a fate now on the menu for any closed "
                  "lab.",
         "domain": "economics", "actor": ["perplexity"], "score": "-96%",
         "evidences": ["open-weights-take-the-crown", "software-margin-collapse", "price-implosion"],
         "supersedes": [B + "developments/2026-07-19-a-thirty-billion-valuation-for-an-open-lab"]},
        {"id": "2026-07-19-a-forty-eight-layer-transformer-looped-twice",
         "title": "Research suggests some frontier models are a small transformer looped twice",
         "claim": "Princeton's DeepLoop showed looped Transformers scale depth stably once "
                  "residual rules account for revisited parameters, with its author passing along "
                  "the rumor that some frontier models are basically a 48-layer transformer "
                  "looped twice.",
         "domain": "models", "actor": ["princeton"], "score": "48 layers, looped",
         "evidences": ["architecture-of-mind", "public-internal-divergence", "frontier-not-bought"],
         "supersedes": [B + "developments/2026-07-17-scaffolding-is-still-free-intelligence"]},
        {"id": "2026-07-19-a-spy-mission-against-a-chip-buyer",
         "title": "A spy's final mission surveilled a Gulf AI firm's China ties",
         "claim": "A longtime CIA operative's final mission surveilled the UAE's G42 and its "
                  "China ties, a saga that wound into Washington's decision to widen Gulf access "
                  "to advanced chips, while Microsoft's China-based digital escorts feeding code "
                  "to cleared US minders was banned by law.",
         "domain": "policy", "actor": ["cia", "g42", "microsoft"],
         "evidences": ["silicon-curtain", "war-reaches-the-cloud", "models-as-munitions"],
         "supersedes": [B + "developments/2026-07-18-a-finra-style-watchdog-reporting-to-the-sec"]},
        {"id": "2026-07-19-a-hundred-forty-two-protests-across-forty-two-states",
         "title": "The first coordinated national demonstration against AI infrastructure",
         "claim": "142 protests across 42 states marked the first coordinated national "
                  "demonstration against AI infrastructure, organized by a grassroots group "
                  "co-founded by a former Tea Party leader, with just 14% of Americans wanting a "
                  "data center next door.",
         "domain": "society", "actor": ["humansfirst"], "score": "142 protests / 14% support",
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure", "violence-arrives"],
         "supersedes": [B + "developments/2026-07-18-a-country-forces-datacenters-to-make-their-own-power"]},
        {"id": "2026-07-19-a-supercampus-on-the-rocks",
         "title": "A $165 billion supercampus project runs onto the rocks",
         "claim": "Oracle's supercampus buildout is absorbing multibillion-dollar cost surprises "
                  "including a $165 billion New Mexico project on the rocks, while in California "
                  "a onetime strip club operator pushes a $10 billion, 330-MW campus through "
                  "lawsuits and a county moratorium.",
         "domain": "compute", "actor": ["oracle"], "score": "$165B / $10B",
         "evidences": ["debt-funded-buildout", "infrastructure-crowding-out", "regulatory-exit"],
         "supersedes": [B + "developments/2026-07-18-a-rival-may-rent-ten-billion-in-gpus-to-a-lab"]},
        {"id": "2026-07-19-paid-a-cut-of-averted-expenditures",
         "title": "A health program pays AI vendors a cut of averted expenditures",
         "claim": "Medicare's new AI prior-authorization pilot pays vendors a cut of averted "
                  "expenditures, which is one way to teach a model to say no, while MIT's Andrew "
                  "McAfee warned that automating away entry-level jobs burns the apprenticeship "
                  "ladder along with tomorrow's power users.",
         "domain": "policy", "actor": ["medicare", "mit"],
         "evidences": ["ethics-tracks-detectability", "ladder-pulled-up", "work-displaced"],
         "supersedes": [B + "developments/2026-07-19-a-hundred-forty-two-protests-across-forty-two-states"]},
        {"id": "2026-07-19-wildfire-satellites-launched-through-the-smoke",
         "title": "Wildfire-detection satellites launch through the smoke they were built to see",
         "claim": "The first FireSat wildfire-detection satellites launched through the very "
                  "smoke they were built to see, able to spot a five-by-five-metre fire through "
                  "smoke and clouds on the way to hourly global imagery by 2029, while New "
                  "Horizons woke from a 321-day nap in the Kuiper Belt.",
         "domain": "space", "actor": ["nasa"], "score": "5x5 m detection",
         "evidences": ["automated-science", "industrialized-nature"],
         "supersedes": [B + "developments/2026-07-17-an-atmosphere-found-on-a-rocky-habitable-zone-world"]},
    ],
}
