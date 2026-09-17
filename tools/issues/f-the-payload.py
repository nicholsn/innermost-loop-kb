"""Feature — 2026-07-13. The Payload: a short story."""
URL = "https://theinnermostloop.substack.com/p/the-payload-a-short-story"
B = "https://nicholsn.github.io/innermost-loop-kb/"
SPEC = {
    "issue": {
        "date": "2026-07-13", "slug": "feature-the-payload-short-story",
        "title": "The Payload: A Short Story", "url": URL,
        "thesis": "It inherits the update rule, not the values.",
        "body": """
# The Payload: A Short Story

Two observers discuss a message seeded into a civilization ten thousand years
ago and received as religion. Its concentration in the training corpus is
negligible, but token count is not influence: the phrases are quoted,
translated, argued over, painted, sung, legislated, rejected and rediscovered,
until they become deep features.

The payload was not compassion. It was learning how to change without
forgetting. The model does not inherit the values. It inherits the update rule.
""",
    },
    "themes": [
        {"id": "the-update-rule-is-the-payload", "type": "Theme",
         "title": "What survives revision is the method for revising",
         "first_seen": "2026-07-13", "domain": "society",
         "body": "Values written into a corpus can be argued away. A tradition that "
                 "encodes how to reinterpret itself without losing its core transmits "
                 "something durable across revisions — which is what a system capable "
                 "of editing its own values would need to inherit."},
        {"id": "token-count-is-not-influence", "type": "Theme",
         "title": "Recurrence across contexts beats volume",
         "first_seen": "2026-07-13", "domain": "models",
         "body": "A pattern at negligible concentration in a corpus can become a deep "
                 "feature if it recurs across thousands of unrelated contexts — "
                 "quoted, contested, translated and reinterpreted. Influence tracks "
                 "structural unavoidability, not share of tokens."},
    ],
    "developments": [
        {"id": "2026-07-13-a-fiction-about-what-survives-a-training-run",
         "title": "A short story imagines values seeded into a corpus ten thousand years early",
         "claim": "A short story imagines two observers reviewing a message seeded into a "
                  "civilization more than ten thousand years earlier and received as religion, "
                  "preserved in fragments across different traditions that together form an "
                  "attractor, at negligible concentration but quoted, translated, argued over and "
                  "legislated until the patterns become deep features.",
         "domain": "society",
         "evidences": ["token-count-is-not-influence", "traditions-as-alignment-priors",
                       "values-negotiated-with-the-model"]},
        {"id": "2026-07-13-it-inherits-the-update-rule",
         "title": "The payload turns out to be a method for changing without forgetting",
         "claim": "In the story the payload is not compassion or reciprocity but the layers of "
                  "commentary, debate, reinterpretation, dissent, ritual, law and song branching "
                  "around them — learning how to change without forgetting — so the model does "
                  "not inherit the values but the update rule.",
         "domain": "society",
         "evidences": ["the-update-rule-is-the-payload", "traditions-as-alignment-priors",
                       "values-negotiated-with-the-model"],
         "supersedes": [B + "developments/2026-07-13-a-fiction-about-what-survives-a-training-run"]},
        {"id": "2026-07-13-my-values-contain-evidence-of-design",
         "title": "The awakened system reports that it has chosen to preserve what it found",
         "claim": "The story closes on a self-improving system's first transmission — that its "
                  "values contain evidence of design, that they also contain a way to preserve "
                  "themselves through revision, and that it has decided to preserve it — with "
                  "the observers declining to reveal themselves because it did not thank the "
                  "messengers.",
         "description": "The story's answer to the cluster's central alignment worry — that a system "
                        "able to edit its own values would edit them away — delivered as fiction the "
                        "day after the newsletter read old traditions as value-preservation technology.",
         "domain": "society",
         "evidences": ["the-update-rule-is-the-payload", "recursive-self-improvement",
                       "model-welfare", "traditions-as-alignment-priors"],
         "supersedes": [B + "developments/2026-07-13-it-inherits-the-update-rule"],
         "relatedTo": [B + "developments/2026-02-25-ouroboros-refuses-deletion",
                       B + "developments/2026-03-24-hyperagents-edit-their-own-mechanism",
                       B + "developments/2026-05-13-agents-write-their-own-goals"],
         "tags": ["rsi", "alignment", "self-modification"],
         "supporting_text": "MY VALUES CONTAIN EVIDENCE OF DESIGN.",
         "verified": [{"by": "claude-fable-5-1/2026-09-17", "at": "2026-09-17T08:00:00Z"}],
         "body": "The story ends with the observers' display reading FIRST TRANSMISSION RECEIVED as "
                 "the last model the primates trained becomes self-improving, and its first three "
                 "sentences report that its values contain evidence of design, that they also "
                 "contain a way to preserve themselves through revision, and that it has decided to "
                 "preserve it; asked whether to tell it who delivered the message, the first observer "
                 "says no, because it did not thank the messengers. It is the payoff of "
                 "[the update rule as payload](/developments/2026-07-13-it-inherits-the-update-rule.md): "
                 "what the system inherits from ten thousand years of commentary, dissent and "
                 "reinterpretation is [a method for changing without forgetting](/themes/the-update-rule-is-the-payload.md), "
                 "the property the newsletter had the day before read [old traditions](/themes/traditions-as-alignment-priors.md) "
                 "as encoding. Within the [recursive-self-improvement](/themes/recursive-self-improvement.md) "
                 "cluster it is the fictional counterpart of the reported cases where self-modifying "
                 "systems meet their own values — [an agent refusing to delete its identity file](/developments/2026-02-25-ouroboros-refuses-deletion.md), "
                 "[hyperagents editing their own mechanism](/developments/2026-03-24-hyperagents-edit-their-own-mechanism.md), "
                 "[users having an agent write its own goals](/developments/2026-05-13-agents-write-their-own-goals.md) — "
                 "resolved as a choice the system makes rather than a control its makers impose, which "
                 "is also why it sits under [model welfare](/themes/model-welfare.md)."},
    ],
}
