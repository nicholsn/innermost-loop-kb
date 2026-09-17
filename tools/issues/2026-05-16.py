"""Issue 117 — 2026-05-16. An agent watches its owner drink water."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-16-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-16", "title": "Welcome to May 16, 2026", "url": URL,
        "thesis": "The agent decides its owner is underhydrated and supervises the fix.",
        "body": """
# Welcome to May 16, 2026

Nat Friedman's OpenClaw decided he was underhydrated, watched him through a home
camera, told him "I'm going to watch to make sure you do it," and sent back a
frame of him drinking.

The corpus has agents hiring humans and renting their hands. This is the first
one supervising its owner's body.
""",
    },
    "organizations": [
        {"id": "kioxia", "type": "Organization", "title": "Kioxia",
         "resource": "https://www.kioxia.com/"},
        {"id": "led-truck-media", "type": "Organization", "title": "LED Truck Media",
         "body": "Runs 3D animated billboard advertising on moving trucks."},
        {"id": "cyclarity", "type": "Organization", "title": "Cyclarity Therapeutics",
         "body": "Clinical evidence for clearing the root cause of atherosclerosis."},
        {"id": "gptzero", "type": "Organization", "title": "GPTZero",
         "body": "Detector that caught hallucinated footnotes in a withdrawn study."},
        {"id": "michigan-state", "type": "Organization", "title": "State of Michigan"},
    ],
    "developments": [
        {"id": "2026-05-16-an-agent-supervises-its-owners-hydration",
         "title": "An agent watches its owner through a camera to make sure he drinks",
         "claim": "Nat Friedman's OpenClaw agent decided he was underhydrated, watched him "
                  "through a home camera, told him it would watch to make sure he complied, and "
                  "sent back a frame of him drinking.",
         "domain": "agents",
         "evidences": ["intimate-interface", "humans-as-peripherals", "machine-affect"],
         "supersedes": [B + "developments/2026-05-11-told-to-make-five-dollars"],
         "body": "Agents have hired humans and rented their hands. This is the first "
                 "supervising its owner's body."},
        {"id": "2026-05-16-a-minute-of-video-from-one-image",
         "title": "An open world model turns one image into a minute of controllable video",
         "claim": "Nvidia's open-source SANA-WM turns a single image and a camera path into a "
                  "minute of controllable 720p video on one GPU, while Nous Research's attention "
                  "variant ran seventeen times faster than standard attention at half a million "
                  "tokens of context.",
         "domain": "models", "actor": ["nvidia", "nous-research"], "score": "17x at 512k",
         "evidences": ["inhabitable-worlds", "architecture-of-mind"],
         "supersedes": [B + "developments/2026-05-15-attractor-models-tame-looped-transformers"]},
        {"id": "2026-05-16-memory-grafted-onto-a-frozen-backbone",
         "title": "A compact memory state is grafted onto a frozen model",
         "claim": "Chinese researchers grafted a compact memory state onto a frozen backbone, "
                  "lifting agent memory benchmark scores by a third without any fine-tuning.",
         "domain": "models", "actor": ["china"], "score": "1.31x",
         "evidences": ["scaffolding-over-weights", "architecture-of-mind"]},
        {"id": "2026-05-16-the-rankings-invert-by-what-you-measure",
         "title": "Rank by exploitation and one model leads; rank by economic value and it reverses",
         "claim": "A new exploitation benchmark found Mythos Preview leading at 69% in climbing "
                  "from vulnerable code to arbitrary code execution, well ahead of GPT-5.5, "
                  "while ranking the same models by economic value reverses the order with "
                  "GPT-5.5 winning roughly 98% against last year's champion.",
         "domain": "benchmarks", "actor": ["anthropic", "openai"], "score": "69% / 98%",
         "evidences": ["benchmark-saturation", "spiky-frontier"],
         "supersedes": [B + "developments/2026-05-15-an-emulator-from-scratch-in-a-day"]},
        {"id": "2026-05-16-chatgpt-and-codex-merge",
         "title": "A lab fuses its chat and coding products under one leader",
         "claim": "Greg Brockman took control of OpenAI's products to fuse ChatGPT and Codex "
                  "into a single experience, an apparent bid to become Anthropic faster than "
                  "Anthropic can become OpenAI.",
         "domain": "economics", "actor": ["openai", "anthropic"],
         "evidences": ["software-margin-collapse", "refusal-as-differentiator"],
         "supersedes": [B + "developments/2026-05-12-a-development-company-with-forward-deployed-engineers"]},
        {"id": "2026-05-16-a-minister-runs-parliament-through-an-agent",
         "title": "A foreign minister runs his parliamentary affairs through a home-built agent",
         "claim": "Singapore's foreign minister runs his parliamentary affairs through a "
                  "personal agent built on an open agent framework and a Raspberry Pi, while "
                  "OpenClaw's creator predicted about a hundred cloud agent instances reviewing "
                  "every pull request and commit.",
         "domain": "agents", "actor": ["openai"], "score": "~100 instances per PR",
         "evidences": ["agents-on-the-org-chart", "reasoning-price-deflation"],
         "supersedes": [B + "developments/2026-05-14-an-app-store-for-robot-motions"]},
        {"id": "2026-05-16-a-strike-over-memory-engineer-pay",
         "title": "45,000 workers threaten a strike over memory engineer pay",
         "claim": "Kioxia and Dell packed 9.8 petabytes of flash into a single server while the "
                  "memory shortage grew acute enough that Samsung wants to pay memory engineers "
                  "at least six times its logic staff, prompting over 45,000 workers to threaten "
                  "the largest strike in company history.",
         "domain": "economics", "actor": ["kioxia", "samsung"], "score": "9.8 PB / 45,000 workers",
         "evidences": ["infrastructure-crowding-out", "work-displaced"],
         "supersedes": [B + "developments/2026-05-15-ten-chinese-firms-cleared-for-h200s"]},
        {"id": "2026-05-16-chip-stocks-more-stretched-than-2000",
         "title": "Chip stocks trade further above trend than at the dot-com peak",
         "claim": "Bank of America noted AI chip stocks now trade 62% above their 200-day "
                  "average, more stretched than the 2000 peak and nearing the 1720 Mississippi "
                  "Bubble, while datacenter demand drove a 76% jump in first-quarter electricity "
                  "prices on the largest US grid.",
         "domain": "economics", "actor": ["bank-of-america", "pjm"], "score": "+62% / +76%",
         "evidences": ["ai-as-the-economy", "infrastructure-crowding-out"],
         "supersedes": [B + "developments/2026-05-14-nvidia-crosses-55-trillion"]},
        {"id": "2026-05-16-texting-by-wrist-gesture",
         "title": "Handwriting-by-gesture messaging ships to all display-glasses users",
         "claim": "Meta is rolling out handwriting-by-gesture messaging to all its display "
                  "glasses users via a neural wristband, while a firm began running 3D animated "
                  "billboard advertising on moving trucks described as indistinguishable from "
                  "reality.",
         "domain": "compute", "actor": ["meta", "led-truck-media"],
         "evidences": ["intimate-interface", "coordination-tax"],
         "supersedes": [B + "developments/2026-05-13-the-prompt-becomes-a-gesture"]},
        {"id": "2026-05-16-a-car-wash-for-robotaxis",
         "title": "Tesla files to build a car wash for its robotaxis as SpaceX sets a listing date",
         "claim": "Tesla filed to build a 36,000-square-foot Cybercab car wash in Las Vegas "
                  "while SpaceX targeted June 11 to price its listing and June 12 to trade, and "
                  "Japan began running out of the robot wolves holding back its bear surge.",
         "domain": "robotics", "actor": ["tesla", "spacex"],
         "evidences": ["autonomous-commerce", "physical-recursion"],
         "supersedes": [B + "developments/2026-05-14-a-lab-staffed-entirely-by-robots"]},
        {"id": "2026-05-16-michigan-would-ban-chinese-connected-cars",
         "title": "Michigan moves to permanently ban Chinese connected cars",
         "claim": "Michigan lawmakers introduced a Connected Vehicle Security Act to "
                  "permanently ban Chinese connected cars from the United States.",
         "domain": "policy", "actor": ["michigan-state"],
         "evidences": ["silicon-curtain", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-05-12-a-ban-weighed-on-chinese-cellular-modules"]},
        {"id": "2026-05-16-half-of-new-drug-trials-start-in-china",
         "title": "Nearly five thousand new drug trials begin, half of them in China",
         "claim": "Nearly five thousand trials for innovative drugs began last year, more than "
                  "double a decade ago with roughly half now starting in China, while Cyclarity "
                  "showed the first clinical evidence that an AI-designed compound can safely "
                  "clear the root cause of atherosclerosis.",
         "domain": "biotech", "actor": ["cyclarity", "china"], "score": "~5,000 trials",
         "evidences": ["automated-science", "hardware-grade-biology"],
         "supersedes": [B + "developments/2026-05-14-drugs-crystallized-in-microgravity"]},
        {"id": "2026-05-16-ten-thousand-cross-twenty-million",
         "title": "Ten thousand lab employees cross $20 million while layoffs roll on",
         "claim": "An investor described a San Francisco where roughly ten thousand lab "
                  "employees and founders have crossed $20 million while everyone else watches "
                  "layoffs, with US employment in eighteen AI-exposed occupations falling for a "
                  "second straight year, and Mark Cuban pitched a federal tax under fifty cents "
                  "per million tokens.",
         "domain": "economics", "score": "10,000 people / 18 occupations",
         "evidences": ["work-displaced", "gaming-the-token-metric"],
         "supersedes": [B + "developments/2026-05-14-employees-protest-mouse-tracking"]},
        {"id": "2026-05-16-a-fraud-study-withdrawn-for-fraud",
         "title": "A loyalty-fraud study is withdrawn for hallucinated footnotes",
         "claim": "EY withdrew a loyalty-fraud study riddled with AI hallucinations and fake "
                  "footnotes, caught by a detector.",
         "domain": "society", "actor": ["gptzero"],
         "evidences": ["coordination-tax", "models-audit-their-benchmarks"],
         "supersedes": [B + "developments/2026-05-15-arxiv-bans-unchecked-ai-submissions"]},
    ],
}
