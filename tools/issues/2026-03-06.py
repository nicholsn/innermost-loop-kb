"""Issue 070 — 2026-03-06. Matching professionals 83% of the time."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-march-6-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-03-06", "title": "Welcome to March 6, 2026", "url": URL,
        "thesis": "A model matches or beats human professionals at knowledge work 83% of the time.",
        "body": """
# Welcome to March 6, 2026

GPT-5.4 scores 83.0% on GDPval — matching or exceeding human professionals at
knowledge work in more than four cases out of five.

The mathematician whose FrontierMath Tier 4 problem was first solved by a model
called it his personal "move 37," said the solution felt almost human, and
declared his own Singularity had arrived. And Iranian state media confirmed the
Bahrain datacenter strike was deliberate.
""",
    },
    "organizations": [
        {"id": "interpositive", "type": "Organization", "title": "InterPositive",
         "body": "AI filmmaking startup trained on production dailies; acquired by Netflix."},
        {"id": "cloverleaf", "type": "Organization", "title": "Cloverleaf Infrastructure",
         "body": "Sells powered land for datacenters."},
        {"id": "vast", "type": "Organization", "title": "Vast",
         "body": "Building space stations from low orbit to Mars."},
        {"id": "new-york-city", "type": "Organization", "title": "State of New York"},
        {"id": "indiana", "type": "Organization", "title": "State of Indiana"},
    ],
    "systems": [
        {"id": "gpt-5-4-pro", "type": "AISystem", "title": "GPT-5.4 Pro",
         "developed_by": [B + "organizations/openai"], "modality": "text",
         "body": "83.0% on GDPval; million-token context and native computer use."},
    ],
    "developments": [
        {"id": "2026-03-06-gdpval-83-percent",
         "title": "A model matches human professionals 83% of the time",
         "claim": "OpenAI's GPT-5.4 Thinking and Pro arrived with native computer use, a "
                  "million-token context and an 83.0% GDPval score, matching or exceeding human "
                  "professionals at knowledge work 83% of the time, alongside 57.7% on "
                  "SWE-Bench Pro and 67.3% on WebArena-Verified.",
         "domain": "benchmarks", "actor": ["openai"], "about": [B + "systems/gpt-5-4-pro"],
         "score": "83.0% GDPval",
         "evidences": ["work-displaced", "benchmark-saturation"],
         "supersedes": [B + "developments/2026-03-05-speculative-speculative-decoding"]},
        {"id": "2026-03-06-minecraft-clone-in-24-minutes",
         "title": "A model builds a working Minecraft clone in 24 minutes",
         "claim": "GPT-5.4 built a basically perfect Minecraft clone in 24 minutes, apparently "
                  "the first model to manage it.",
         "domain": "agents", "actor": ["openai"], "score": "24 minutes",
         "evidences": ["software-margin-collapse", "engineer-as-supervisor"]},
        {"id": "2026-03-06-naskrecki-move-37",
         "title": "A mathematician calls the solution his personal move 37",
         "claim": "GPT-5.4 Pro posted a new record of 38.0% on FrontierMath Tier 4, and "
                  "Bartosz Naskręcki, whose Tier 4 problem was first solved by AI, called it his "
                  "personal move 37, said the solution was clean and felt almost human, and "
                  "declared his own Singularity had arrived.",
         "domain": "science", "actor": ["openai"], "about": [B + "benchmarks/frontiermath"],
         "score": "38.0%",
         "evidences": ["automated-science", "takeoff-declared"],
         "supersedes": [B + "developments/2026-03-05-knuth-conjecture-cracked"]},
        {"id": "2026-03-06-novel-observations-on-open-problems",
         "title": "A model begins making novel observations where none had scored",
         "claim": "Epoch AI reported GPT-5.4 has begun making novel observations on "
                  "FrontierMath's Open Problems benchmark, where no model had previously scored.",
         "domain": "benchmarks", "actor": ["epoch-ai", "openai"],
         "evidences": ["automated-science", "discovery-as-process"]},
        {"id": "2026-03-06-netflix-buys-an-ai-film-studio",
         "title": "One industry absorbs the machine, the other demands a name tag",
         "claim": "Netflix acquired InterPositive, an AI filmmaking startup training on "
                  "production dailies to handle mixing, coloring, relighting and effects, while "
                  "Apple Music launched Transparency Tags requiring labels on whether a track's "
                  "artwork, composition or video involved AI generation.",
         "domain": "society", "actor": ["netflix", "interpositive", "apple"],
         "evidences": ["work-displaced", "agent-exclusion"],
         "supersedes": [B + "developments/2026-02-23-amc-kills-ai-film-screenings"]},
        {"id": "2026-03-06-apple-pulls-512gb-mac-studio",
         "title": "Apple withdraws a configuration as the memory shortage reaches Cupertino",
         "claim": "Apple quietly pulled the 512-GB Mac Studio configuration as the DRAM shortage "
                  "reached even Cupertino, while Washington drafted regulations requiring US "
                  "approval for AI chip shipments anywhere on Earth.",
         "domain": "compute", "actor": ["apple", "white-house"],
         "evidences": ["consumer-deprioritized", "silicon-curtain"],
         "supersedes": [B + "developments/2026-02-27-smartphone-shipments-decade-low"]},
        {"id": "2026-03-06-powered-land-becomes-an-asset-class",
         "title": "A startup raises $300M selling powered land",
         "claim": "Cloverleaf Infrastructure, which sells powered land for data centers, raised "
                  "$300 million, while Oracle cut thousands of jobs to fund datacenter "
                  "expansion, targeting roles it expects AI to replace.",
         "domain": "economics", "actor": ["cloverleaf", "oracle"], "score": "$300M",
         "evidences": ["capital-takes-the-plant", "work-displaced"],
         "supersedes": [B + "developments/2026-02-23-farmland-at-120000-an-acre"]},
        {"id": "2026-03-06-first-advanced-reactor-permit",
         "title": "The NRC issues its first commercial advanced reactor permit",
         "claim": "TerraPower received the first ever NRC construction permit for a "
                  "commercial-scale advanced nuclear plant, a 345-MW sodium-cooled fast reactor "
                  "in Wyoming with molten salt storage.",
         "domain": "energy", "actor": ["terrapower"], "score": "345 MW",
         "evidences": ["burning-molecules-for-tokens", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-04-watts-not-weights"]},
        {"id": "2026-03-06-bahrain-datacenter-hit-deliberately",
         "title": "A datacenter strike is confirmed as deliberate",
         "claim": "Iranian state media revealed that Amazon's Bahrain data center was "
                  "deliberately targeted by the IRGC for the company's US military support, one "
                  "of the first known cases of a data center intentionally struck as an act of "
                  "war.",
         "domain": "policy", "actor": ["amazon", "iran"],
         "evidences": ["war-reaches-the-cloud", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-03-three-datacenters-hit-lasers-answer"],
         "body": "Collateral damage on the 2nd; confirmed intent on the 6th."},
        {"id": "2026-03-06-productivity-visible-in-macro-data",
         "title": "AI productivity effects become visible in aggregate data",
         "claim": "A University of Chicago economist found AI's impact on productivity now "
                  "visible in macro aggregate data, while Citadel Securities published a chart "
                  "showing software engineer job postings surging in a textbook Jevons paradox.",
         "domain": "economics",
         "evidences": ["growth-without-hiring", "work-displaced"],
         "supersedes": [B + "developments/2026-02-26-growth-without-jobs-unprecedented"],
         "body": "The first counter-signal to the displacement series: efficiency breeding "
                 "more demand, not less."},
        {"id": "2026-03-06-observed-exposure-early-warning",
         "title": "Anthropic ships an early-warning system for its own displacement effects",
         "claim": "Anthropic launched observed exposure, an early-warning system for AI-driven "
                  "white-collar displacement weighting automated over augmentative uses, "
                  "suggesting limited evidence of job loss so far.",
         "domain": "economics", "actor": ["anthropic"],
         "evidences": ["work-displaced", "values-negotiated-with-the-model"]},
        {"id": "2026-03-06-new-york-would-ban-chatbot-legal-advice",
         "title": "New York weighs banning chatbots from legal and medical advice",
         "claim": "New York is considering a bill to ban chatbots from giving legal and medical "
                  "advice with a private right of action, while Indiana required cryptocurrency "
                  "options in retirement plans by July 2027.",
         "domain": "policy", "actor": ["new-york-city", "indiana"],
         "evidences": ["agent-exclusion", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-03-03-no-copyright-for-ai-artwork"]},
        {"id": "2026-03-06-pentagon-formalizes-the-designation",
         "title": "The supply-chain-risk designation is formalized",
         "claim": "The Pentagon formally designated Anthropic a supply-chain risk, a "
                  "classification likely to force military contractors to sever ties, while "
                  "Dario Amodei said the company has been having productive conversations with "
                  "the Department and apologized for a leaked memo.",
         "domain": "policy", "actor": ["war-department", "anthropic", "people/dario-amodei"],
         "evidences": ["refusal-as-differentiator", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-03-04-anthropic-nears-20b-run-rate"]},
        {"id": "2026-03-06-roman-telescope-and-vast-500m",
         "title": "A telescope with a hundred times Hubble's field of view prepares to launch",
         "claim": "NASA's Nancy Grace Roman Space Telescope, with a field of view a hundred "
                  "times larger than Hubble's, is set to launch this autumn, while Vast raised "
                  "$500 million to build space stations from low orbit to the Moon and Mars.",
         "domain": "space", "actor": ["nasa", "vast"], "score": "100x Hubble",
         "evidences": ["inhabitable-worlds", "automated-science"],
         "supersedes": [B + "developments/2026-03-04-microbes-survive-impact-pressures"]},
    ],
}
