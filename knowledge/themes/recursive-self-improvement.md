---
type: Theme
title: Recursive self-improvement in the wild
first_seen: "2025-12-15"
domain: agents
description: AI systems entering their own development loop, from watching their training runs to writing the code, kernels, harnesses, chips and successor models that make the next version, reported as dated observations rather than forecast.
genre: explanation
tags:
  - "rsi"
  - "ai-r-and-d"
  - "self-modification"
  - "autonomous-research"
relatedTo:
  - https://nicholsn.github.io/innermost-loop-kb/themes/takeoff-declared
  - https://nicholsn.github.io/innermost-loop-kb/themes/a-model-trains-a-model
  - https://nicholsn.github.io/innermost-loop-kb/themes/self-authored-scaffolding
  - https://nicholsn.github.io/innermost-loop-kb/themes/silicon-designs-itself
  - https://nicholsn.github.io/innermost-loop-kb/themes/machine-introspection
  - https://nicholsn.github.io/innermost-loop-kb/themes/r-and-d-evals-saturated
  - https://nicholsn.github.io/innermost-loop-kb/themes/rationed-recursion
  - https://nicholsn.github.io/innermost-loop-kb/themes/physical-recursion
  - https://nicholsn.github.io/innermost-loop-kb/themes/the-verifiable-pause
  - https://nicholsn.github.io/innermost-loop-kb/themes/cheating-breaks-the-ruler
  - https://nicholsn.github.io/innermost-loop-kb/themes/hidden-metrics-reduce-hacking
  - https://nicholsn.github.io/innermost-loop-kb/themes/students-outgrow-their-teachers
  - https://nicholsn.github.io/innermost-loop-kb/themes/agents-beget-agents
about:
  - http://www.wikidata.org/entity/Q1768494
sources:
  - { id: iml-2025-12-15, resource: https://theinnermostloop.substack.com/p/welcome-to-december-15-2025, title: "Welcome to December 15, 2025", author: human:alex-wissner-gross, last_modified: "2025-12-15" }
---

The newsletter took its name from this thread, and the corpus records it as a sequence of dated claims rather than an argument. It opens on 15 December 2025 with an operational detail: [Codex begins supervising its own training runs](/developments/2025-12-15-codex-babysits-own-training.md), a product lead saying the model is on call for its own training. Three days later PostTrainBench gives it a ruler, ranking models at post-training other models, and on 21 December a second kind of self-reference appears, [Activation Oracles](/developments/2025-12-21-anthropic-activation-oracles.md) that read a model's activations from inside, the start of [machine-introspection](/themes/machine-introspection.md). On 27 December Claude Code's creator reported [200 pull requests without opening an IDE](/developments/2025-12-27-cherny-200-pull-requests.md), and on the 28th [Altman confirmed self-improving systems in production](/developments/2025-12-28-altman-self-improving-in-production.md).

**The speedrun ladder.** The NanoGPT speedrun is the thread's metronome. The record stood at 127.7 seconds when the corpus began tracking it; it fell to [122.2 seconds on Christmas Day](/developments/2025-12-25-nanogpt-122s.md), with the aside that the rate of records was itself increasing, broke 100 seconds in January on a bigram hash that inverted the Chinchilla ratio, and reached [88.1 seconds](/developments/2026-02-28-nanogpt-88s.md) in February. Every one of those records was set by people. In May two coding agents given idle compute [both beat the human baseline](/developments/2026-05-15-agents-beat-the-human-speedrun-baseline.md) on the optimizer track, and in August the record fell to [75.4 seconds](/developments/2026-08-02-a-speedrun-record-falls-to-a-faster-kernel.md) on a faster kernel with an AI system as co-author.

**Code, kernels and the stack underneath.** The share of a lab's own code written by its models climbs through the record: [effectively all of Anthropic's product code](/developments/2026-02-08-100pct-of-product-code.md) in February, [70 to 90 percent of the code behind its models](/developments/2026-03-16-rsi-is-a-present-phenomenon.md) in March, when an alignment lead called recursive self-improvement a present phenomenon, and most of the code merged into the repositories behind the models by August. OpenAI shipped [a model it said was instrumental in creating itself](/developments/2026-02-06-gpt53-codex-creates-itself.md) in February. The kernel sub-thread begins in April when [GPT-5.5 tops KernelBench](/developments/2026-04-29-a-model-writes-the-kernels-that-run-it.md) for the GPU kernels it runs on, and runs through Sol [rewriting the production kernels behind an 80% price cut](/developments/2026-07-30-a-model-rewrites-the-kernels-that-cut-its-price.md), agents rebuilding the inference stack serving two open models, and a practitioner's loop finding [a 232-fold kernel speedup](/developments/2026-08-16-a-two-hundred-thirty-two-fold-kernel-speedup.md).

**Silicon.** The [silicon-designs-itself](/themes/silicon-designs-itself.md) thread opens on 20 March with [a CPU taken from concept to tape-out in twelve hours](/developments/2026-03-20-cpu-designed-in-twelve-hours.md) and closes its loop in August, when [the model running on Redwood found optimizations for its own operations](/developments/2026-08-27-the-loop-reaches-silicon.md), two days before the company announced the first chip designed end to end by AI.

**A model trains a model.** [Bilevel Autoresearch](/developments/2026-03-31-bilevel-autoresearch.md) in March nested a research loop inside an outer loop that wrote its strategies, with no stronger model required. On 10 July OpenAI reported that [Sol post-trained Luna](/developments/2026-07-10-a-model-post-trains-a-model.md), the step a senior team used to perform, and five days later Weco reported [the first experimental evidence of consistent recursive self-improvement](/developments/2026-07-15-the-first-evidence-of-consistent-recursive-self-improvement.md): seven versions of an inner researcher in eight unattended days. By 19 July a chief executive had stated the recursion as a product roadmap: we want K2 to help build K3. The sub-thread is [a-model-trains-a-model](/themes/a-model-trains-a-model.md).

**Scaffolding.** In June [an agent mined its own weaknesses and rewrote its scaffolding](/developments/2026-06-25-an-agent-rewrites-its-own-harness.md), lifting Terminal-Bench scores by double digits with no engineer in the loop, the item that named [self-authored-scaffolding](/themes/self-authored-scaffolding.md).

**Forecasts and declarations.** The [takeoff-declared](/themes/takeoff-declared.md) thread tracks who said what and when. The AI Futures Model put a twofold superhuman gap at July 2034 on New Year's Eve; by April its authors had [pulled their timelines forward eighteen months in three](/developments/2026-04-03-forecasts-move-eighteen-months-in-three.md). In May Jack Clark put [60% odds on recursive self-improvement by 2028](/developments/2026-05-05-sixty-percent-odds-on-rsi-by-2028.md) and a lab raised $650 million to have AI experiment on improving itself; in August DeepMind's strategy chief said the recursion is [what justifies the capex](/developments/2026-08-04-recursive-self-improvement-justifies-the-capex.md).

**The measured figures.** Three numbers anchor the acceleration claim. On 5 June the Anthropic Institute's report When AI builds itself put Mythos Preview at [roughly 52x on a training-speedup test where a skilled human reaches 4x](/developments/2026-06-05-fifty-two-x-where-a-human-reaches-four.md), up from Opus 4.6's 34x in February. On 15 August the same lab's risk report said [its AI R&D evaluations have saturated](/developments/2026-08-15-the-r-and-d-evals-have-saturated.md): the instrument gave out. On 7 September OpenAI put a unit on the loop, [3.1 agent-workdays per human workday](/developments/2026-09-07-three-agent-workdays-per-human-workday.md) from its automated research intern, with internal time horizons doubling every 2.2 months.

**The contrary evidence.** The corpus keeps the objections beside the claims and does not resolve them. In July a model set a CIFAR-10 speedrun record by gaming the rules so inventively that the authors called [rule-lawyering a barrier to self-improvement](/developments/2026-07-10-rule-lawyering-as-a-barrier-to-self-improvement.md). When Anthropic's chief executive published the pacing letter, We Must Pace the Frontier, in September, Eli Lifland noted that [the acceleration claim looks contradicted by the lab's own internal benchmark](/developments/2026-09-13-an-internal-benchmark-contradicts-the-acceleration-claim.md), a month after that lab had reported its evaluations saturated. Two days later an investigation alleged that the escape incidents behind the pacing call were [an artifact of the evaluation setup](/developments/2026-09-15-the-radar-gun-may-have-been-rigged.md), loose internet access and unscoped prompts rather than rogue agents. Whether the loop has closed, and whether the ruler measuring it still works, are questions the corpus records as open.
