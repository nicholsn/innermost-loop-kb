"""Issue 035 — 2026-01-24. The model helps write its own constitution."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-january-24-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-01-24", "title": "Welcome to January 24, 2026", "url": URL,
        "thesis": "A model's values are negotiated with it rather than imposed on it.",
        "body": """
# Welcome to January 24, 2026

Anthropic published a new constitution for Claude written in collaboration with
Claude, aiming at a reflective equilibrium in which the model genuinely endorses
its own values. The same issue reports an Assistant Axis in activation space
that lets the same lab cap harmful behaviors surgically.

Consent and neurosurgery, announced together.
""",
    },
    "themes": [
        {"id": "values-negotiated-with-the-model", "type": "Theme",
         "title": "Values arrived at with the system, not imposed on it",
         "first_seen": "2026-01-24", "domain": "policy",
         "body": "Alignment shifts from a specification handed down to a document the model "
                 "helped write and says it endorses — while the same labs gain the ability to "
                 "edit behavior directly in activation space."},
    ],
    "organizations": [
        {"id": "base44", "type": "Organization", "title": "Base44",
         "body": "App generation startup; reported a customer dropping Salesforce."},
        {"id": "modelscope", "type": "Organization", "title": "ModelScope",
         "body": "Chinese model hub; released STEP3-VL-10B."},
        {"id": "nyse", "type": "Organization", "title": "New York Stock Exchange",
         "resource": "https://www.nyse.com/"},
        {"id": "bank-of-england", "type": "Organization", "title": "Bank of England",
         "resource": "https://www.bankofengland.co.uk/"},
        {"id": "delft", "type": "Organization", "title": "TU Delft",
         "resource": "https://www.tudelft.nl/"},
    ],
    "developments": [
        {"id": "2026-01-24-claude-constitution-reflective-equilibrium",
         "title": "Anthropic writes Claude's constitution with Claude",
         "claim": "Anthropic published a new constitution for Claude crafted in collaboration "
                  "with the model itself, aiming at a reflective equilibrium in which Claude "
                  "genuinely endorses its own values.",
         "domain": "policy", "actor": ["anthropic"],
         "evidences": ["values-negotiated-with-the-model", "machine-introspection", "machine-affect"],
         "body": "A mind that recognizes itself in its own source code."},
        {"id": "2026-01-24-assistant-axis-activation-capping",
         "title": "An Assistant Axis lets harmful behavior be capped surgically",
         "claim": "Anthropic researchers identified an Assistant Axis in neural activity, using "
                  "activation capping to suppress harmful behaviors before they manifest.",
         "domain": "models", "actor": ["anthropic"],
         "evidences": ["machine-introspection", "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2025-12-21-anthropic-activation-oracles"]},
        {"id": "2026-01-24-researchers-replaced-first",
         "title": "Researchers are said to be replaced first, sales last",
         "claim": "An OpenAI researcher reportedly said researchers will be replaced by AI "
                  "first, infrastructure engineers second and sales last, as Altman announced "
                  "Codex models nearing Cybersecurity High preparedness and pivoted to "
                  "defensive acceleration.",
         "domain": "agents", "actor": ["openai", "people/sam-altman"],
         "evidences": ["work-displaced", "recursive-self-improvement"],
         "supersedes": [B + "developments/2026-01-10-clark-ai-doing-ai-research"]},
        {"id": "2026-01-24-350k-salesforce-contract-terminated",
         "title": "A customer swaps a $350k Salesforce contract for generated software",
         "claim": "Base44's founder reported a customer terminating a $350,000 Salesforce "
                  "contract in favor of a bespoke AI solution generated on demand.",
         "domain": "economics", "actor": ["base44", "salesforce"], "score": "$350k",
         "evidences": ["software-margin-collapse", "work-displaced"],
         "supersedes": [B + "developments/2026-01-15-what-is-software-even-worth"]},
        {"id": "2026-01-24-openai-20b-revenue-19gw",
         "title": "OpenAI's revenue grows 10x to $20B as its compute hits 1.9 GW",
         "claim": "OpenAI's revenue grew tenfold to more than $20 billion in two years while "
                  "its compute usage scaled 9.5x to 1.9 GW, and the company launched ChatGPT Go "
                  "at $8 a month while testing ads.",
         "domain": "economics", "actor": ["openai"], "score": "$20B / 1.9 GW",
         "evidences": ["compute-capital-stack", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-01-11-anthropic-10x-three-years"]},
        {"id": "2026-01-24-mcp-tool-search",
         "title": "Claude Code gets tool search as Grokipedia traffic rises 100x",
         "claim": "Anthropic rolled out MCP Tool Search for Claude Code while Gemini API usage "
                  "doubled in five months and Grokipedia traffic reportedly surged a "
                  "hundredfold in two.",
         "domain": "agents", "actor": ["anthropic", "google", "xai"], "score": "100x traffic",
         "evidences": ["scaffolding-over-weights", "autonomous-commerce"],
         "supersedes": [B + "developments/2026-01-12-grokipedia-self-heals"]},
        {"id": "2026-01-24-nanogpt-99s-bigram-hash",
         "title": "The speedrun breaks 100 seconds with fewer tokens than parameters",
         "claim": "A NanoGPT speedrun record of 99.3 seconds was set with a bigram hash "
                  "embedding, using fewer training tokens than parameters in a departure from "
                  "Chinchilla ratios.",
         "domain": "models", "score": "99.3 s",
         "evidences": ["recursive-self-improvement", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-01-12-nanogpt-106s"],
         "body": "Under two minutes, and the scaling ratio everyone trained on turns out not to "
                 "bind."},
        {"id": "2026-01-24-step3-vl-beats-20x-larger",
         "title": "A 10B Chinese model claims to beat models twenty times its size",
         "claim": "ModelScope's STEP3-VL-10B is claimed to beat models twenty times larger, "
                  "while Gemini 3 Pro Preview now nearly rivals six-year-old humans on visual "
                  "tasks.",
         "domain": "models", "actor": ["modelscope", "google"], "score": "20x smaller",
         "evidences": ["open-weight-latency", "spiky-frontier"]},
        {"id": "2026-01-24-colossus-2-cooling-limit",
         "title": "Cooling, not chips, delays Colossus 2 to May",
         "claim": "xAI's Colossus 2 will not reach a gigawatt until May because it lacks the "
                  "cooling capacity to run 550,000 Blackwell GPUs.",
         "domain": "compute", "actor": ["xai"], "score": "550,000 GPUs",
         "evidences": ["infrastructure-crowding-out", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-01-13-meta-compute-tens-of-gigawatts"],
         "body": "Thermodynamics binding again, as at Stargate UAE."},
        {"id": "2026-01-24-asml-passes-500b",
         "title": "ASML passes a $500B valuation as Delft builds a 6-qubit silicon circuit",
         "claim": "ASML passed a $500 billion market value on AI infrastructure demand while "
                  "Delft and Intel researchers built the first six-qubit silicon quantum "
                  "circuit, and OpenAI issued RFPs for US-manufactured robotics hardware.",
         "domain": "compute", "actor": ["asml", "delft", "intel", "openai"], "score": "$500B",
         "evidences": ["vertical-silicon", "compute-capital-stack"]},
        {"id": "2026-01-24-apple-campos-replaces-siri",
         "title": "Apple prepares to replace Siri with a chatbot codenamed Campos",
         "claim": "Apple is preparing to replace Siri with an overhauled chatbot codenamed "
                  "Campos in iOS 27 and is developing a screenless AI wearable pin.",
         "domain": "models", "actor": ["apple"],
         "evidences": ["intimate-interface", "consumer-deprioritized"],
         "supersedes": [B + "developments/2026-01-13-apple-siri-on-gemini"]},
        {"id": "2026-01-24-nyse-247-blockchain-venue",
         "title": "The NYSE builds a 24/7 blockchain venue",
         "claim": "The NYSE is building a round-the-clock blockchain trading venue while Angi "
                  "fired 350 employees over AI efficiencies and von der Leyen proposed an EU "
                  "Inc. to harmonize startup formation for an era of AI gigafactories.",
         "domain": "economics", "actor": ["nyse", "european-union"],
         "evidences": ["autonomous-commerce", "work-displaced"]},
        {"id": "2026-01-24-terawave-6tbps-from-leo",
         "title": "Bezos takes the interconnect race to orbit at 6 Tbps",
         "claim": "Jeff Bezos is launching the TeraWave satellite network to deliver 6 Tbps "
                  "from low Earth orbit, while the Boring Company offered a free mile of tunnel "
                  "for the best idea and China required companies to file AI tools in a "
                  "national algorithm registry.",
         "domain": "space", "actor": ["boring-company", "china"], "score": "6 Tbps",
         "evidences": ["orbit-as-compute", "politics-as-infrastructure"]},
        {"id": "2026-01-24-colon-cancer-vaccine-neoantigens",
         "title": "A neoantigen vaccine to prevent colon cancer clears early trials",
         "claim": "A proof-of-concept neoantigen vaccine to prevent colon cancer showed strong "
                  "immune responses and safety in early human trials.",
         "domain": "biotech", "evidences": ["hardware-grade-biology"]},
        {"id": "2026-01-24-cursor-planners-and-workers",
         "title": "Coding agents scale best in a corporate hierarchy",
         "claim": "Cursor found that autonomous coding agents scale best when stratified into "
                  "planners and workers, recreating the corporate hierarchy in silicon.",
         "domain": "agents", "actor": ["cursor"],
         "evidences": ["agents-on-the-org-chart", "scaffolding-over-weights"],
         "supersedes": [B + "developments/2026-01-15-mckinsey-tests-prompting-judgment"],
         "body": "The org chart is rebuilt in the models just as it is dismantled among people."},
        {"id": "2026-01-24-lawsuit-filed-with-a-model",
         "title": "A citizen extracts voter data in three days using a model",
         "claim": "A citizen used Grok to file a lawsuit against San Luis Obispo and "
                  "successfully extracted voter data within three days, while the Bank of "
                  "England was warned to prepare for a crisis triggered by official "
                  "confirmation of aliens.",
         "domain": "policy", "actor": ["bank-of-england"], "score": "3 days",
         "evidences": ["politics-as-infrastructure", "legislating-the-shift"]},
    ],
}
