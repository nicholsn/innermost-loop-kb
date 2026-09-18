# Search baseline — September 18, 2026

Before adding date/domain metadata, the deployed index transferred 1,151,251 bytes compressed in a single desktop curl observation (0.319s). Local JSON parsing took 21ms. A Node 22 desktop run of 100 searches across flatbed, openai, compute, AI, and governance measured 1.98ms p95 for the search function. This is not a mobile, cold-browser, or input-to-paint benchmark.

The index remains lazy-loaded and cached for the page lifetime. No external search service is introduced. Follow-up device profiling should measure cold network/parse time and input-to-result latency on an agreed mobile device; proposed warm-search target is 200ms p95. Workers or split payloads should be justified by that measurement, while preserving complete-corpus search.
