"""Feature — 2026-05-19. The first major-exchange compute futures."""
URL = "https://theinnermostloop.substack.com/p/the-first-major-exchange-compute"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-05-19", "slug": "feature-major-exchange-compute-futures",
        "title": "The First Major-Exchange Compute Futures", "url": URL,
        "thesis": "The index was the foundation. The exchange is the keystone.",
        "body": """
# The First Major-Exchange Compute Futures

Credentialing is not clearing. To finish the arc oil walked in the 1980s and gas
in the 1990s, compute had to find a home at a major regulated derivatives
exchange.

Oil took over a century, from Drake's well in 1859 to futures in 1983. Gas took
longer still. Compute took only years, because oil and gas had already built the
machinery.
""",
    },
    "organizations": [
        {"id": "ice-exchange", "type": "Organization", "title": "Intercontinental Exchange"},
    ],
    "developments": [
        {"id": "2026-05-19-compute-futures-reach-a-regulated-exchange",
         "title": "Compute futures are planned for a major regulated derivatives exchange",
         "claim": "Ornn plans to launch exchange-listed futures on GPU compute through the "
                  "Intercontinental Exchange, US dollar denominated and cash-settled against "
                  "index series covering H100, H200, B200 and additional GPU types, pending "
                  "regulatory approval — extending the plumbing that runs crude, gas, carbon and "
                  "the benchmark soft commodities to compute.",
         "domain": "economics", "actor": ["ornn", "ice-exchange"],
         "evidences": ["compute-becomes-a-commodity", "ai-as-the-economy", "compute-capital-stack"]},
        {"id": "2026-05-19-the-arch-can-now-bear-weight",
         "title": "Clearing lets regulated capital pools finance the buildout",
         "claim": "Once index-referenced futures clear at a major exchange, lenders financing GPU "
                  "buildouts can hedge on the same infrastructure that clears oil and gas, "
                  "insurers can underwrite residual value against a regulated curve, treasury "
                  "desks can lock forward compute costs the way airlines have locked jet fuel "
                  "since the 1980s, and sovereign and pension capital that cannot touch "
                  "unregulated venues at scale can finally participate.",
         "domain": "economics", "actor": ["ornn", "ice-exchange"], "score": "$7T buildout",
         "evidences": ["compute-becomes-a-commodity", "debt-funded-buildout",
                       "bottlenecks-arbitraged-instantly"],
         "supersedes": [B + "developments/2026-05-19-compute-futures-reach-a-regulated-exchange"]},
        {"id": "2026-05-19-oil-took-a-century-compute-took-years",
         "title": "Compute compresses a century of market formation into a few years",
         "claim": "Every commodity that powered a phase of civilization eventually traded next to "
                  "the others on the same plumbing — oil taking over a century from the first "
                  "well to futures, gas longer still — while compute took only years because the "
                  "machinery already existed.",
         "domain": "economics", "actor": ["ornn"],
         "evidences": ["compute-becomes-a-commodity", "price-implosion", "ai-as-the-economy"],
         "supersedes": [B + "developments/2026-05-19-the-arch-can-now-bear-weight"]},
    ],
}
