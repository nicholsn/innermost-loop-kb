---
type: Development
title: Giving an agent research papers improves its results
claim: A controlled experiment confirmed that giving an autoresearch agent access to computer science papers during hyperparameter search improved results by 3.2%.
domain: agents
reported_in:
  - https://nicholsn.github.io/innermost-loop-kb/issues/2026-03-31
about:
  - https://nicholsn.github.io/innermost-loop-kb/systems/claude-code
evidences:
  - https://nicholsn.github.io/innermost-loop-kb/themes/recursive-self-improvement
  - https://nicholsn.github.io/innermost-loop-kb/themes/automated-science
score: +3.2%
occurred_on: "2026-03-27"
supersedes:
  - https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-09-autoresearch-650-experiments
description: "The author reads it as the payoff of the optimizer-optimizing agents in the same paragraph: an autonomous researcher gets measurably better simply by being allowed to read the literature, so the agents are getting hungrier for input."
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/people/andrej-karpathy
relations:
  - { predicate: relatedTo, target: https://nicholsn.github.io/innermost-loop-kb/developments/2026-03-31-bilevel-autoresearch, relation_label: corroborates }
verified:
  - { by: claude-fable-5-1/2026-09-17, at: "2026-09-17T08:00:00Z" }
tags:
  - "development"
  - "2026-03-31"
  - "autonomous-research"
  - "ai-r-and-d"
  - "agent-harness"
generated: { by: process:iml-emit, at: "2026-03-31T00:00:00Z" }
sources:
  - { id: iml-2026-03-31, resource: https://theinnermostloop.substack.com/p/welcome-to-march-31-2026, title: "Welcome to March 31, 2026", author: human:alex-wissner-gross, last_modified: "2026-03-31", supporting_text: access to CS papers during hyperparameter search improved results by 3.2% }
  - { id: reddit-autoresearch-papers-experiment, resource: https://www.reddit.com/r/MachineLearning/comments/1s5jpgz/r_controlled_experiment_giving_an_llm_agent/, title: "[R] Controlled experiment: giving an LLM agent access to CS papers during automated hyperparameter search improves results by 3.2%", author: human:kalpitdixit, last_modified: "2026-03-27" }
  - { id: paper-lantern-autoresearch-writeup, resource: https://www.paperlantern.ai/blog/auto-research-case-study, title: Paper Lantern improves Autoresearch, author: org:paper-lantern, last_modified: "2026-03-26" }
---

The experiment, posted to r/MachineLearning on 27 March by u/kalpitdixit ([thread](https://www.reddit.com/r/MachineLearning/comments/1s5jpgz/r_controlled_experiment_giving_an_llm_agent/)), compared an autoresearch-style hyperparameter-search agent with and without access to computer-science papers and reported a 3.2% improvement for the arm that could read; the newsletter's framing is that the agents are getting hungrier for input. It is a small number attached to a large question, whether autonomous researchers benefit from the literature the way human ones do, and it sits between Karpathy's [650-experiment autoresearch run](/developments/2026-03-09-autoresearch-650-experiments.md) and the same issue's [Bilevel Autoresearch](/developments/2026-03-31-bilevel-autoresearch.md), which improves the loop by rewriting its search mechanism rather than feeding it papers. The setup was two identical runs of Karpathy's autoresearch framework, a [Claude Code](/systems/claude-code.md) agent optimizing a roughly 7M-parameter GPT-2 on TinyStories on an M4 Pro for 100 experiments per arm from the same seed configuration, with the only variable an MCP server (Paper Lantern) doing full-text search over more than two million CS papers; at the two-hour mark the arm without papers stood at a val_bpb of 0.4624 and the arm with papers at 0.4475, a 3.2% gap still widening, after considering 520 papers, citing 100 and trying 25 paper-sourced techniques including AdaGC, the sqrt batch-scaling rule, the REX schedule and WSD cooldown ([full writeup](https://www.paperlantern.ai/blog/auto-research-case-study)). The author's own limitation is a single run per condition on a tiny model, so the figure is suggestive rather than settled.
