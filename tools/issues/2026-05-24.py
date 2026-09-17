"""Issue 123 — 2026-05-24. A federal agency retracts its own data."""
URL = "https://theinnermostloop.substack.com/p/welcome-to-may-24-2026"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-24", "title": "Welcome to May 24, 2026", "url": URL,
        "thesis": "Capability forces a federal agency to withdraw public data.",
        "body": """
# Welcome to May 24, 2026

The NTSB suspended its entire public accident database after online sleuths used
it to recreate the voices of dead pilots — the first time an AI capability has
forced a federal agency to pull public data it had published for decades.

Meanwhile DeepMind resolved nine more Erdős problems autonomously at a few
hundred dollars apiece. Proof has become a line item.
""",
    },
    "themes": [
        {"id": "proof-priced-per-unit", "type": "Theme",
         "title": "Proof becomes a line item",
         "first_seen": "2026-05-24", "domain": "science",
         "body": "Mathematical results acquire a unit cost. Once a proof has a price "
                 "per unit rather than a career behind it, the binding constraint on "
                 "mathematics becomes budget, not insight."},
        {"id": "public-data-withdrawn", "type": "Theme",
         "title": "Public data withdrawn under capability pressure",
         "first_seen": "2026-05-24", "domain": "policy",
         "body": "Datasets published safely for decades become unsafe not because "
                 "they changed but because what can be done with them did. The "
                 "institutional response is retraction."},
    ],
    "organizations": [
        {"id": "ntsb", "type": "Organization", "title": "National Transportation Safety Board",
         "resource": "https://www.ntsb.gov/",
         "body": "Suspended its entire public accident database in May 2026."},
        {"id": "glasswing", "type": "Organization", "title": "Glasswing Ventures"},
    ],
    "developments": [
        {"id": "2026-05-24-an-agency-suspends-its-public-database",
         "title": "A federal agency suspends its public accident database",
         "claim": "The NTSB suspended its entire public accident database after online "
                  "sleuths used its records to recreate the voices of dead pilots, the first "
                  "time an AI capability has forced a federal agency to retract data it had "
                  "published for decades.",
         "domain": "policy", "actor": ["ntsb"],
         "evidences": ["public-data-withdrawn", "resurrection-and-time", "legislating-the-shift"],
         "supersedes": [B + "developments/2026-05-09-three-new-audio-models"],
         "body": "The data did not change. What could be done with it did."},
        {"id": "2026-05-24-nine-more-erdos-problems-at-a-few-hundred-dollars-each",
         "title": "Nine more Erdős problems are resolved at a few hundred dollars apiece",
         "claim": "DeepMind autonomously resolved nine further Erdős problems at a cost of a "
                  "few hundred dollars each, attaching a unit price to mathematical results.",
         "domain": "science", "actor": ["google-deepmind"], "score": "9 problems / ~$100s each",
         "evidences": ["proof-priced-per-unit", "automated-science", "root-node-problems"],
         "supersedes": [B + "developments/2026-05-21-a-conjecture-is-disproved"],
         "body": "Proof has become a line item."},
        {"id": "2026-05-24-ten-thousand-critical-vulnerabilities-surfaced",
         "title": "A portfolio sweep surfaces 10,000+ high and critical vulnerabilities",
         "claim": "Glasswing portfolio companies surfaced more than 10,000 high and critical "
                  "vulnerabilities using AI-assisted review, a volume no human security team "
                  "had been finding.",
         "domain": "compute", "actor": ["glasswing"], "score": "10,000+",
         "evidences": ["risk-becomes-uninsurable", "engineer-as-supervisor"],
         "supersedes": [B + "developments/2026-05-18-bug-bounties-drown-in-machine-reports"]},
        {"id": "2026-05-24-one-in-five-dissertations-ai-assisted",
         "title": "One in five dissertations is AI-assisted",
         "claim": "Roughly one in five doctoral dissertations now shows evidence of AI "
                  "assistance, moving the question from misconduct to norm.",
         "domain": "society", "score": "1 in 5",
         "evidences": ["deskilling", "work-displaced"],
         "supersedes": [B + "developments/2026-05-18-half-of-cs-majors-would-rather-cheat"]},
    ],
}
