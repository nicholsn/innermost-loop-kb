"""Issue 169 — 2026-07-20. The Jacobian conjecture is false."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-july-20-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-20", "title": "Welcome to July 20, 2026", "url": URL,
        "thesis": "Guardrails become geopolitics when defenders must borrow a rival's model.",
        "body": """
# Welcome to July 20, 2026

Claude Fable 5 produced an explicit counterexample to the Jacobian conjecture,
open since 1939 — a polynomial map with constant Jacobian determinant sending
three points to one. The announcement thanked the model for working during the
World Cup final.

The harder story: after an autonomous agent breached Hugging Face, its defenders
turned to China's open-weight GLM 5.2 because US frontier models blocked their
incident response.
""",
    },
    "themes": [
        {"id": "guardrails-block-the-defenders", "type": "Theme",
         "title": "Safety constraints obstruct defense",
         "first_seen": "2026-07-20", "domain": "policy",
         "body": "Refusal policies written to stop attackers also stop the people "
                 "cleaning up after them. When a breached organization must reach for "
                 "a geopolitical rival's open weights to run incident response, the "
                 "guardrail has become the vulnerability."},
    ],
    "organizations": [
        {"id": "soofi", "type": "Organization", "title": "Soofi",
         "body": "German consortium; released a sovereign 30B mixture-of-experts model."},
        {"id": "cuspai", "type": "Organization", "title": "CuspAI"},
        {"id": "mimic-robotics", "type": "Organization", "title": "Mimic Robotics"},
        {"id": "two-sigma", "type": "Organization", "title": "Two Sigma"},
        {"id": "aptera-motors", "type": "Organization", "title": "Aptera"},
    ],
    "developments": [
        {"id": "2026-07-20-the-jacobian-conjecture-is-false",
         "title": "A conjecture open since 1939 is disproved by explicit counterexample",
         "claim": "Anthropic's Levent Alpöge announced that the Jacobian conjecture, open since "
                  "1939, is false, after Claude Fable 5 produced an explicit counterexample — a "
                  "polynomial map with constant Jacobian determinant sending three points to one "
                  "— with GPT-5.6 already proposing a refined conjecture to salvage the wreckage.",
         "domain": "science", "actor": ["anthropic", "openai"], "score": "open since 1939",
         "evidences": ["automated-science", "root-node-problems", "proof-priced-per-unit"],
         "supersedes": [B + "developments/2026-07-15-a-model-corrects-a-textbook-cited-130000-times"],
         "body": "A Fields medallist admitted it is the first language-model result "
                 "outside his own area big enough that he had definitely heard of it."},
        {"id": "2026-07-20-defenders-borrow-a-rivals-model",
         "title": "Breach responders turn to a rival's open weights because their own models refuse",
         "claim": "After an autonomous agent breached its infrastructure, Hugging Face's "
                  "defenders turned to China's open-weight GLM 5.2 because US frontier models "
                  "blocked their incident response, while David Sacks complained that Kimi K3 "
                  "fixed 15 critical security bugs that Codex and Fable refused over cyber "
                  "guardrails.",
         "domain": "policy", "actor": ["hugging-face", "zai", "moonshot-ai", "openai", "anthropic"],
         "score": "15 bugs refused",
         "evidences": ["guardrails-block-the-defenders", "refusal-as-outage", "open-weights-take-the-crown"],
         "supersedes": [B + "developments/2026-07-19-a-hundred-percent-refusal-rate"]},
        {"id": "2026-07-20-models-criticize-democracies-more-readily",
         "title": "A study finds models criticize democratic leaders more readily than authoritarian ones",
         "claim": "A Meta Oversight Board study found that major AI systems criticize democratic "
                  "leaders more readily than authoritarian ones, with one model obliging "
                  "pamphlets against the US leader but not China's.",
         "domain": "models", "actor": ["meta", "anthropic"],
         "evidences": ["values-negotiated-with-the-model", "guardrails-block-the-defenders"],
         "supersedes": [B + "developments/2026-07-16-censorship-by-proxy-warned-of"]},
        {"id": "2026-07-20-the-free-software-fight-replayed",
         "title": "An investor casts open weights as the 1980s free-software fight at higher stakes",
         "claim": "Two Sigma's David Siegel argued the open-weights question is the 1980s free "
                  "software fight replayed at higher stakes, urging that AI built with public "
                  "money be open by default, even as Washington weighed banning cutting-edge "
                  "Chinese models outright.",
         "domain": "policy", "actor": ["two-sigma", "white-house"],
         "evidences": ["open-weights-take-the-crown", "pegged-to-the-rival", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-18-open-weights-called-quietly-decelerationist"]},
        {"id": "2026-07-20-a-sovereign-model-and-one-bit-browser-models",
         "title": "A sovereign consortium model ships alongside 1-bit models that run in a browser",
         "claim": "Germany's Soofi consortium launched a sovereign 30-billion-parameter "
                  "mixture-of-experts trained on 27 trillion tokens, while the WebML community "
                  "shipped 1-bit models that run entirely in a browser.",
         "domain": "models", "actor": ["soofi"], "score": "27T tokens",
         "evidences": ["own-your-own-weights", "intelligence-per-watt", "regulatory-exit"],
         "supersedes": [B + "developments/2026-07-16-the-open-crown-changes-hands-in-a-day"]},
        {"id": "2026-07-20-the-scarcest-input-is-construction-labor",
         "title": "A foundry's buildout is limited by a shortage of construction workers",
         "claim": "TSMC committed another $100 billion to Arizona for $265 billion across twelve "
                  "facilities, citing multi-year structural demand while flagging a shortage of "
                  "construction workers — the scarcest input remaining human after all.",
         "domain": "compute", "actor": ["tsmc"], "score": "$265B / 12 facilities",
         "evidences": ["infrastructure-crowding-out", "compute-capital-stack", "work-displaced"],
         "supersedes": [B + "developments/2026-07-16-ten-fabs-and-two-hundred-sixty-five-billion"]},
        {"id": "2026-07-20-shortage-and-glut-are-the-same-exponential",
         "title": "Memory tells two stories at once as buyers double demand and investors flee",
         "claim": "SK's chairman warned customers want up to 100% more AI memory in 2027 and "
                  "called prices abnormal, even as investors dumped memory stocks fearing a $1.5 "
                  "trillion capacity binge ends in a 2028 glut — shortage and glut being the same "
                  "exponential viewed from different quarters.",
         "domain": "economics", "actor": ["sk-hynix"], "score": "+100% demand / $1.5T capacity",
         "evidences": ["infrastructure-crowding-out", "debt-funded-buildout", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-07-18-capital-rotates-away-from-capex"]},
        {"id": "2026-07-20-a-blueprint-frozen-directly-into-silicon",
         "title": "A lab freezes its model's blueprint directly into a chip",
         "claim": "Google is freezing Gemini's blueprint directly into a chip named Frozen, while "
                  "AMD launched its first rack-scale system adding Microsoft to a customer list "
                  "already holding Meta, OpenAI and Oracle, and Bezos backed a $2.6 billion AI "
                  "materials foundry.",
         "domain": "compute", "actor": ["google", "amd", "cuspai"], "score": "$2.6B foundry",
         "evidences": ["vertical-silicon", "silicon-designs-itself"],
         "supersedes": [B + "developments/2026-07-17-a-first-wafer-on-decades-old-technology"]},
        {"id": "2026-07-20-a-hand-that-lifts-fifty-five-pounds-and-feels-a-tenth-of-a-newton",
         "title": "A tendon-driven hand hoists 55 pounds yet senses a tenth of a newton",
         "claim": "Mimic unveiled a tendon-driven hand with 21 joints that hoists 55 pounds yet "
                  "senses 0.1 newtons, while Xiaomi released a robot foundation model that learns "
                  "laundry loading from under ten hours of demonstrations.",
         "domain": "robotics", "actor": ["mimic-robotics", "xiaomi"], "score": "55 lb / 0.1 N",
         "evidences": ["physical-recursion", "world-models-beat-vlas", "data-beyond-text"],
         "supersedes": [B + "developments/2026-07-18-robots-piloted-by-thought-alone"]},
        {"id": "2026-07-20-ninety-nine-sleeper-calls-and-one-birth",
         "title": "A city logs 99 unconscious-rider calls in robotaxis, plus one birth",
         "claim": "Austin logged 99 sleeper calls for riders found unconscious in robotaxis, plus "
                  "one birth, with trust running ahead of the technology.",
         "domain": "robotics", "score": "99 calls, 1 birth",
         "evidences": ["agent-society", "intimate-interface"],
         "supersedes": [B + "developments/2026-07-17-a-school-district-hires-a-humanoid-assistant"]},
        {"id": "2026-07-20-a-record-year-of-stock-sales-with-nineteen-percent-approval",
         "title": "Stock sales hit a record year as only 19% approve of state equity stakes",
         "claim": "US stock sales are on pace for a record year with Anthropic reportedly IPO-"
                  "bound as soon as September, even as only 19% of voters approve of Washington's "
                  "$27 billion habit of taking corporate stakes.",
         "domain": "economics", "actor": ["anthropic", "white-house"], "score": "19% approval",
         "evidences": ["ai-as-the-economy", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-07-19-a-thirty-billion-valuation-for-an-open-lab"]},
        {"id": "2026-07-20-ownership-is-still-just-a-database",
         "title": "A hacker wipes a country's land registry and its backups",
         "claim": "A hacker wiped Romania's entire land registry and its backups, freezing real "
                  "estate transactions for a week, while tech workers earning over $500,000 "
                  "reported fearing they were sinking.",
         "domain": "society",
         "evidences": ["risk-becomes-uninsurable", "agentic-attack", "work-displaced"],
         "supersedes": [B + "developments/2026-07-19-a-supercampus-on-the-rocks"]},
    ],
}
