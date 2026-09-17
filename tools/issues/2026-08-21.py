"""Issue 190 — 2026-08-21. Tokens become the central currency."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-august-21-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-08-21", "title": "Welcome to August 21, 2026", "url": URL,
        "thesis": "A payments giant buys the mint of the intelligence economy.",
        "body": """
# Welcome to August 21, 2026

Stripe's $7 billion purchase of OpenRouter — a 90-person gateway routing across
400+ models from 80+ providers — is its largest acquisition ever and a wager
that no single model wins. Patrick Collison calls tokens the central currency
for companies building with AI.

And prompting escapes the keyboard: a model learns a new physical task from a
three-to-twelve-second demonstration, scoring 59% with zero gradient updates.
""",
    },
    "themes": [
        {"id": "physical-prompting", "type": "Theme",
         "title": "A demonstration becomes the prompt",
         "first_seen": "2026-08-21", "domain": "robotics",
         "body": "A few seconds of video dropped into a context window teaches a new "
                 "manipulation task with no gradient updates. In-context learning "
                 "crosses into the physical world, and improvised tool use emerges "
                 "from pretraining rather than instruction."},
    ],
    "organizations": [
        {"id": "generalist-ai", "type": "Organization", "title": "Generalist"},
        {"id": "supcon", "type": "Organization", "title": "SUPCON"},
        {"id": "nevada", "type": "Organization", "title": "Nevada"},
        {"id": "groq-inc", "type": "Organization", "title": "Groq"},
        {"id": "independence-mo", "type": "Organization", "title": "Independence, Missouri"},
    ],
    "systems": [
        {"id": "slack-code", "type": "AISystem", "title": "Slack Code",
         "description": "Salesforce's agentic-coding surface inside Slack, giving third-party coding agents dedicated channels to write, review and ship code in the open.",
         "developed_by": [B + "organizations/salesforce"], "modality": "code",
         "resource": "https://www.salesforce.com/introducing-slack-code/",
         "tags": ["coding-agent"],
         "body": "Slack Code, introduced by Salesforce in August 2026, turns a Slack channel into the "
                 "workplace for coding agents: [Claude Code](/systems/claude-code.md), "
                 "[Devin](/systems/devin.md), [Copilot](/systems/copilot.md), [ChatGPT](/systems/chatgpt.md) "
                 "and Vercel agents each get a dedicated channel to write, review and ship code where the "
                 "team can watch, and the channel archives itself when the job is done. In this corpus it "
                 "appears once, in the [trillions-of-tokens item](/developments/2026-08-21-trillions-of-tokens-a-week-to-write-its-own-software.md), "
                 "as the moment agent spending moves into the group chat."},
        {"id": "devin", "type": "AISystem", "title": "Devin",
         "description": "Cognition's autonomous software-engineering agent, one of the coding agents given a dedicated channel by Slack Code.",
         "developed_by": [B + "organizations/cognition"], "modality": "code",
         "resource": "https://devin.ai/",
         "sameAs": ["http://www.wikidata.org/entity/Q124874381"],
         "tags": ["coding-agent"],
         "body": "Devin is the autonomous software engineer built by [Cognition](/organizations/cognition.md). "
                 "In this corpus Cognition [offered to foot a customer's bill up to $10 million](/developments/2026-06-05-ten-million-back-if-the-agent-underdelivers.md) "
                 "if Devin underdelivered, Devin [cracked a batch of decades-old graph conjectures in a day](/developments/2026-07-23-conjectures-become-a-line-item-and-a-meme.md), "
                 "and it is one of the agents that [Slack Code](/systems/slack-code.md) gives its own channel in the "
                 "[trillions-of-tokens item](/developments/2026-08-21-trillions-of-tokens-a-week-to-write-its-own-software.md)."},
    ],
    "developments": [
        {"id": "2026-08-21-a-payments-giant-buys-the-mint",
         "title": "A payments giant makes its largest acquisition ever to buy a model gateway",
         "claim": "Stripe's more than $7 billion purchase of OpenRouter, the 90-person gateway "
                  "routing requests across more than 400 models from over 80 providers, is the "
                  "payments giant's largest acquisition ever and a wager that no single model "
                  "wins, with Patrick Collison calling tokens the central currency for companies "
                  "building with AI.",
         "domain": "economics", "actor": ["stripe", "openrouter"], "score": "$7B+",
         "evidences": ["routing-around-the-ban", "monoculture-is-the-vulnerability", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-08-17-a-run-rate-past-sixty-five-billion"]},
        {"id": "2026-08-21-an-s-1-that-could-beat-the-record",
         "title": "A lab's IPO could match or beat the record share sale",
         "claim": "Anthropic reportedly expects its mega-IPO, which could file publicly by month's "
                  "end, to match or beat SpaceX's record $75 billion share sale, backed by a $65 "
                  "billion revenue run rate and quarterly revenue above $11.5 billion, up from "
                  "$787 million a year earlier.",
         "domain": "economics", "actor": ["anthropic", "spacex"], "score": "$787M to $11.5B in a year",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-08-19-founders-take-supervoting-shares-before-the-float"]},
        {"id": "2026-08-21-silicon-financed-like-sovereign-debt",
         "title": "A chipmaker seeks up to $100 billion for custom AI silicon",
         "claim": "Broadcom is in talks to raise more than $60 billion, potentially $100 billion "
                  "with the junior tranche, for custom AI chips benefiting Anthropic and others, "
                  "financing silicon like sovereign debt.",
         "domain": "economics", "actor": ["broadcom", "anthropic"], "score": "$60-100B",
         "evidences": ["debt-funded-buildout", "vertical-silicon", "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-08-21-an-s-1-that-could-beat-the-record"]},
        {"id": "2026-08-21-trillions-of-tokens-a-week-to-write-its-own-software",
         "title": "A social network burns trillions of tokens a week writing its own software",
         "claim": "Meta has quietly become one of Microsoft's largest AI customers, burning "
                  "trillions of tokens a week through Azure largely to write its own software, "
                  "while Slack Code gave five different agent products dedicated channels to "
                  "write, review and ship code in the open.",
         "description": "The token currency gets its first astronomical denomination: a company with "
                        "its own frontier models buys another's by the trillion to write its software, "
                        "and the coding agents get channels in the group chat like colleagues.",
         "domain": "agents",
         "actor": ["meta", "microsoft", "salesforce", "anthropic", "openai", "cognition", "vercel"],
         "score": "trillions of tokens a week", "occurred_on": "2026-08-20",
         "about": [B + "systems/slack-code", B + "systems/claude-code", B + "systems/devin",
                   B + "systems/copilot", B + "systems/chatgpt"],
         "evidences": ["the-persistent-colleague", "agents-on-the-org-chart", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-08-13-if-this-was-opt-in-nobody-would-opt-in"],
         "relatedTo": [B + "developments/2026-02-08-100pct-of-product-code",
                       B + "developments/2026-08-01-agents-write-almost-all-output-tokens",
                       B + "developments/2026-02-27-claude-gets-a-work-calendar"],
         "relations": [{"predicate": "relatedTo",
                        "target": B + "developments/2026-08-21-a-payments-giant-buys-the-mint",
                        "relation_label": "extends"}],
         "tags": ["ai-r-and-d", "compute-scaling", "labor"],
         "supporting_text": "burning trillions of tokens a week through Azure, largely to write its own software",
         "sources": [{"id": "bloomberg-meta-microsoft-largest-ai-customer",
                      "resource": "https://www.bloomberg.com/news/articles/2026-08-20/meta-has-quietly-become-one-of-microsoft-s-largest-ai-customers",
                      "title": "Meta Has Quietly Become One of Microsoft's Largest AI Customers",
                      "author": "org:bloomberg", "last_modified": "2026-08-20"},
                     {"id": "salesforce-introducing-slack-code",
                      "resource": "https://www.salesforce.com/introducing-slack-code/",
                      "title": "Introducing Slack Code: Agentic Coding for Teams", "author": "org:salesforce",
                      "last_modified": "2026-08-20"}],
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "Bloomberg reported on August 20 that Meta has quietly become one of Microsoft's "
                 "largest AI customers, burning trillions of tokens a week through Azure largely to "
                 "write its own software "
                 "([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-20/meta-has-quietly-become-one-of-microsoft-s-largest-ai-customers)). "
                 "Alongside it Salesforce introduced [Slack Code](/systems/slack-code.md), which gives "
                 "[Claude Code](/systems/claude-code.md), [Devin](/systems/devin.md), "
                 "[Copilot](/systems/copilot.md), [ChatGPT](/systems/chatgpt.md) and Vercel agents "
                 "dedicated channels to write, review and ship code in the open, self-archiving when "
                 "the job is done ([Salesforce](https://www.salesforce.com/introducing-slack-code/)). "
                 "The newsletter reads both as denominations of the token currency that the same "
                 "issue's [Stripe–OpenRouter deal](/developments/2026-08-21-a-payments-giant-buys-the-mint.md) "
                 "mints. In the trajectory the Meta figure carries the "
                 "[effectively all product code](/developments/2026-02-08-100pct-of-product-code.md) and "
                 "[99.8% of output tokens](/developments/2026-08-01-agents-write-almost-all-output-tokens.md) "
                 "claims from a lab's own agent to a customer's token bill, and Slack Code moves the "
                 "[agent as colleague](/developments/2026-02-27-claude-gets-a-work-calendar.md) from a "
                 "calendar to a channel."},
        {"id": "2026-08-21-a-billion-downloads-and-a-hundred-thousand-variants",
         "title": "An open family crosses a billion downloads and 100,000 community variants",
         "claim": "Google's Gemma crossed one billion downloads and 100,000 community variants, "
                  "running everywhere from orbiting satellites to a health app with 100 million "
                  "downloads in India.",
         "domain": "models", "actor": ["google"], "score": "1B downloads / 100,000 variants",
         "evidences": ["open-weights-take-the-crown", "most-people-never-see-the-frontier"],
         "supersedes": [B + "developments/2026-08-16-three-billion-downloads-and-a-hundred-fifty-thousand-derivatives"]},
        {"id": "2026-08-21-a-physical-prompt-teaches-a-new-task",
         "title": "A three-second demonstration teaches a new physical task with no training",
         "claim": "Generalist's GEN-1.5 learns a new physical task from a physical prompt, a "
                  "three-to-twelve-second demonstration dropped into its context window, scoring "
                  "59% with zero gradient updates and 83% after five minutes of data, with "
                  "improvised tool use emerging unprompted from pretraining.",
         "domain": "robotics", "actor": ["generalist-ai"], "score": "59% zero-shot / 83% after 5 min",
         "evidences": ["physical-prompting", "world-models-beat-vlas", "physical-recursion"],
         "supersedes": [B + "developments/2026-08-12-the-first-human-to-robot-transfer-scaling-law"]},
        {"id": "2026-08-21-seven-thousand-robotaxis-approved-for-one-city",
         "title": "A state approves up to 7,000 robotaxis for one city",
         "claim": "Nevada approved up to 7,000 robotaxis for Las Vegas from Tesla, Waymo and "
                  "Uber's partners, and Waymo arrives with its own custom chip, a 1,000-TOPS part "
                  "on a 5-nanometer process that sharpens reflexes while loosening its Nvidia "
                  "dependence.",
         "domain": "robotics", "actor": ["nevada", "waymo", "tesla", "uber", "tsmc"],
         "score": "7,000 robotaxis / 1,000 TOPS",
         "evidences": ["physical-recursion", "vertical-silicon", "agent-society"],
         "supersedes": [B + "developments/2026-08-15-driverless-rides-across-eighteen-counties"]},
        {"id": "2026-08-21-humanoid-robocops-issue-a-hundred-seventy-thousand-warnings",
         "title": "Humanoid traffic officers issue 170,000 warnings in one city",
         "claim": "SUPCON's humanoid robocops have issued 170,000 polite traffic warnings in "
                  "Hangzhou, while humanoid makers sell robots to state training centers that "
                  "sell teleoperation data back, a circular economy behind Unitree's $50 billion "
                  "debut.",
         "domain": "robotics", "actor": ["supcon", "unitree"], "score": "170,000 warnings / $50B",
         "evidences": ["physical-recursion", "agent-society", "data-beyond-text"],
         "supersedes": [B + "developments/2026-08-21-seven-thousand-robotaxis-approved-for-one-city"]},
        {"id": "2026-08-21-a-licensed-inference-chip-for-a-restricted-market",
         "title": "A chipmaker reportedly plans a licensed inference part for a restricted market",
         "claim": "Nvidia reportedly plans a Groq-licensed inference processor variant for China "
                  "by year-end to fight Huawei amid an inference chip famine, though it denies any "
                  "such roadmap.",
         "domain": "compute", "actor": ["nvidia", "groq-inc", "huawei"],
         "evidences": ["silicon-curtain", "infrastructure-crowding-out", "pegged-to-the-rival"],
         "supersedes": [B + "developments/2026-08-17-an-antifragile-hundred-billion-dollar-bet"]},
        {"id": "2026-08-21-a-dozen-towns-recall-officials-over-datacenters",
         "title": "Residents of a dozen towns move to recall officials over datacenter deals",
         "claim": "Residents of a dozen towns are recalling officials over data center deals, with "
                  "the scrutiny going fully bipartisan, complete with a party committee memo "
                  "calling it a sleeper issue.",
         "domain": "policy", "actor": ["independence-mo"],
         "evidences": ["infrastructure-crowding-out", "politics-as-infrastructure", "over-automation-is-rational"],
         "supersedes": [B + "developments/2026-08-17-ai-becomes-a-major-election-issue"]},
        {"id": "2026-08-21-a-third-of-submissions-fully-synthetic",
         "title": "A third of music submissions are fully synthetic while AI draws under 0.5% of listening",
         "claim": "Apple Music will label songs Made With AI, fitting since a third of submissions "
                  "are now fully synthetic while AI music draws under 0.5% of listening, as Japan "
                  "approved a comply-or-explain code urging AI firms to disclose models and "
                  "training data.",
         "domain": "society", "actor": ["apple", "japan-govt"], "score": "33% of submissions / <0.5% listening",
         "evidences": ["agent-exclusion", "legislating-the-shift", "bots-outnumber-us"],
         "supersedes": [B + "developments/2026-08-17-a-watermark-called-a-perversion-of-writing"]},
        {"id": "2026-08-21-more-screen-time-predicted-better-cognition",
         "title": "An eight-year study finds more childhood screen time predicted better cognition",
         "claim": "An eight-year Finnish study found more childhood screen time predicted better "
                  "teenage cognition, while the Treasury limited children's savings accounts to "
                  "broad, low-fee equity funds.",
         "domain": "society", "actor": ["us-treasury-dept"],
         "evidences": ["deskilling", "most-people-never-see-the-frontier"],
         "supersedes": [B + "developments/2026-08-13-top-adopters-burn-eight-times-the-median"],
         "body": "A counterweight to the year's dominant story about screens and "
                 "cognition, kept for that reason."},
    ],
}
