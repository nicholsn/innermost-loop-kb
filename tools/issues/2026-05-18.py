"""Issue 119 — 2026-05-18. The last time a human will ever win."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-18-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-18", "title": "Welcome to May 18, 2026", "url": URL,
        "thesis": "The human wins the race and breaks his arm doing it.",
        "body": """
# Welcome to May 18, 2026

Figure's human package sorter beat the android by a slim margin, with his left
forearm basically broken. The company's chief executive: "This is the last time
a human will ever win."

Meanwhile bug bounty submissions quadrupled in three weeks, and Linus Torvalds
called the kernel's security mailing list almost entirely unmanageable under
duplicate machine-written reports.
""",
    },
    "organizations": [
        {"id": "bugcrowd", "type": "Organization", "title": "Bugcrowd",
         "resource": "https://www.bugcrowd.com/"},
        {"id": "fsb", "type": "Organization", "title": "Financial Stability Board",
         "resource": "https://www.fsb.org/"},
        {"id": "nextera", "type": "Organization", "title": "NextEra Energy",
         "resource": "https://www.nexteraenergy.com/"},
        {"id": "kuaishou", "type": "Organization", "title": "Kuaishou",
         "body": "Chinese video generation lab trained on short-form libraries."},
    ],
    "developments": [
        {"id": "2026-05-18-the-last-time-a-human-will-ever-win",
         "title": "A human beats the android and breaks his forearm doing it",
         "claim": "Figure's human package sorter won by a slim margin with his left forearm "
                  "basically broken, and the company's chief executive predicted this is the "
                  "last time a human will ever win.",
         "domain": "robotics", "actor": ["figure"],
         "evidences": ["work-displaced", "physical-recursion"],
         "supersedes": [B + "developments/2026-05-17-four-days-of-humanoids-until-failure"]},
        {"id": "2026-05-18-one-line-of-code-against-delusions",
         "title": "Masking an agent's own past actions stops it mistaking hallucination for memory",
         "claim": "Microsoft's Nando de Freitas reported that one line of code is all it takes "
                  "to prevent agent delusions, by masking an agent's past actions from its "
                  "history so it stops mistaking hallucinations for memory.",
         "domain": "agents", "actor": ["microsoft"],
         "evidences": ["architecture-of-mind", "deception-measured"],
         "supersedes": [B + "developments/2026-05-16-memory-grafted-onto-a-frozen-backbone"]},
        {"id": "2026-05-18-bug-bounties-drown-in-machine-reports",
         "title": "Bug bounty submissions quadruple in three weeks",
         "claim": "Bug bounty programs are drowning in AI-generated vulnerability reports, with "
                  "one platform seeing submissions quadruple in three weeks, while Linus "
                  "Torvalds called the Linux kernel's security mailing list almost entirely "
                  "unmanageable under duplicate reports.",
         "domain": "policy", "actor": ["bugcrowd"], "score": "4x in 3 weeks",
         "evidences": ["coordination-tax", "war-reaches-the-cloud"],
         "supersedes": [B + "developments/2026-04-07-bug-bounty-pauses-submissions"]},
        {"id": "2026-05-18-briefing-central-banks-on-what-a-model-found",
         "title": "A lab will brief central banks on flaws its model found in the financial system",
         "claim": "Anthropic will brief the Financial Stability Board and central banks on real "
                  "vulnerabilities its Mythos Preview model found in the global financial "
                  "system.",
         "domain": "policy", "actor": ["anthropic", "fsb"],
         "evidences": ["war-reaches-the-cloud", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-05-17-a-model-finds-an-apple-silicon-exploit-before-release"]},
        {"id": "2026-05-18-china-overtakes-the-us-in-video-generation",
         "title": "Chinese labs overtake the US in video generation",
         "claim": "Chinese groups including ByteDance and Kuaishou have apparently overtaken the "
                  "US in video generation, training on the short-form libraries that "
                  "advertising, ecommerce and entertainment consume, while SpaceX's AI division "
                  "launched an early-beta coding agent.",
         "domain": "models", "actor": ["bytedance", "kuaishou", "spacex"],
         "evidences": ["silicon-curtain", "open-weight-latency"],
         "supersedes": [B + "developments/2026-05-16-a-minute-of-video-from-one-image"]},
        {"id": "2026-05-18-half-of-cs-majors-would-rather-cheat",
         "title": "Half of surveyed CS majors say they would rather cheat than fail",
         "claim": "Stanford seniors report cheating is omnipresent, with 49% of surveyed "
                  "computer science majors saying they would rather cheat than fail, as a campus "
                  "that banned proctored exams for a century rebuilds assessment around what AI "
                  "cannot fake.",
         "domain": "society", "actor": ["stanford"], "score": "49%",
         "evidences": ["deskilling", "coordination-tax"],
         "supersedes": [B + "developments/2026-05-13-princeton-ends-a-133-year-old-honor-code"]},
        {"id": "2026-05-18-a-bigger-stake-in-intel",
         "title": "The President says the government should have asked for more of Intel",
         "claim": "The President said the White House should have asked for a bigger stake in "
                  "Intel beyond its 10% holding after landmark deals lifted the stock over 300%, "
                  "while Apple built a booming budget-device line from slightly flawed chips "
                  "rivals discard.",
         "domain": "policy", "actor": ["white-house", "intel", "apple"], "score": "+300%",
         "evidences": ["science-as-industrial-policy", "vertical-silicon"],
         "supersedes": [B + "developments/2026-05-15-ten-chinese-firms-cleared-for-h200s"]},
        {"id": "2026-05-18-iran-would-charge-for-subsea-cables",
         "title": "Iran wants to charge tech giants for the subsea cables crossing its waters",
         "claim": "Emboldened by its blockade of the Strait of Hormuz, Iran wants to charge tech "
                  "giants for the subsea cables carrying internet and financial traffic, with "
                  "state media hinting they could be cut if firms refuse.",
         "domain": "policy", "actor": ["iran"],
         "evidences": ["war-reaches-the-cloud", "politics-as-infrastructure"],
         "supersedes": [B + "developments/2026-05-11-fiber-strung-beside-crude-oil-pipelines"]},
        {"id": "2026-05-18-the-biggest-power-deal-ever",
         "title": "A $67B utility merger forms a colossus across the datacenter belt",
         "claim": "NextEra Energy agreed to buy Dominion for $67 billion, the biggest power deal "
                  "ever, forming a colossus across Virginia's datacenter belt, while Tesla "
                  "dropped its solar roof tiles for plain panels.",
         "domain": "energy", "actor": ["nextera", "tesla"], "score": "$67B",
         "evidences": ["capital-takes-the-plant", "burning-molecules-for-tokens"],
         "supersedes": [B + "developments/2026-05-17-power-cut-to-49000-residents"]},
        {"id": "2026-05-18-a-two-point-four-trillion-perpetual",
         "title": "A pre-listing valuation of $2.4 trillion trades on perpetual futures",
         "claim": "SpaceX opened for trading on perpetual futures at a $2.4 trillion valuation "
                  "ahead of what would be the largest listing in history, with Musk saying "
                  "Starship is built to lift over a megaton to orbit yearly.",
         "domain": "economics", "actor": ["spacex"], "score": "$2.4T / 1 megaton",
         "evidences": ["compute-capital-stack", "orbit-as-compute"],
         "supersedes": [B + "developments/2026-05-17-an-index-rewritten-for-one-listing"]},
        {"id": "2026-05-18-two-labs-take-89-percent-of-revenue",
         "title": "Two labs take 89% of revenue across the most mature AI startups",
         "claim": "Anthropic and OpenAI together take 89% of annualized revenue across 34 of the "
                  "most mature AI startups, while a jury ruled against Elon Musk in his suit "
                  "claiming Sam Altman broke a promise to keep OpenAI a nonprofit.",
         "domain": "economics", "actor": ["anthropic", "openai", "xai"], "score": "89%",
         "evidences": ["ai-as-the-economy", "compute-capital-stack"],
         "supersedes": [B + "developments/2026-05-17-a-hedge-fund-founder-goes-home-depressed"]},
        {"id": "2026-05-18-birth-rates-tied-to-smartphones",
         "title": "Population records tie the birth-rate plunge to smartphone adoption",
         "claim": "Population records and search data tie the global birth-rate plunge to the "
                  "spread of smartphones.",
         "domain": "society",
         "evidences": ["intimate-interface", "cognitive-load-inverted"],
         "supersedes": [B + "developments/2026-02-26-japan-tenth-year-of-record-low-births"]},
    ],
}
