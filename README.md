# The Innermost Loop — a knowledge graph

A [LOKF](https://github.com/nicholsn/lokf) knowledge base modelling
[The Innermost Loop](https://theinnermostloop.substack.com/), Dr. Alex
Wissner-Gross's newsletter of daily developments in machine intelligence.

Every markdown file under `knowledge/` is one concept with YAML frontmatter, and
the whole directory projects losslessly to RDF. The goal is to turn 236 newsletter
issues into something you can query as one trajectory.

## The model

LOKF supplies the concept model, provenance and trust machinery.
`schema/innermost.yaml` adds only what this corpus needs, via
`imports: [lokf]`:

| Type | What it is |
|---|---|
| **Issue** | One dated edition. The provenance anchor for everything it reports. |
| **Development** | The atomic unit — one dated, attributed claim ("Oracle's backlog rose 438% to $523B"). |
| **Theme** | A thread the newsletter returns to. What makes the corpus a trajectory. |
| **AISystem** | A named model, agent or embodied system. |
| **Benchmark** | A named evaluation. Kept separate from scores, which are Developments. |
| **Facility** | Physical or orbital infrastructure with an operator and a location. |

Two separations do the real work:

- **Reporter vs. actor.** `author` is always Wissner-Gross — he reported it.
  `actor` is whoever *did* the thing. Conflating them would make the graph
  useless for asking who is actually building what.
- **Benchmark vs. score.** A benchmark persists; a score is a dated, sourced
  Development. That is what lets "2% per month on SWE-bench" be a trend rather
  than a fact with no time index.

## Working on it

Issues are declared as data in `tools/issues/<date>.py` and rendered to concept
files by `tools/emit.py`. Hand-writing thirty frontmatter blocks per issue is
where mistakes live; entity files are written once and reused, so later issues
only add developments.

```bash
uv venv && uv pip install 'lokf[build]==0.8.0'

python tools/emit.py tools/issues/2025-12-11.py   # render an issue
cd schema && lokf validate ../knowledge --schema innermost.yaml --check-refs
```

`--check-refs` is the check that matters as this grows: a development pointing
at an organization that was never written is a perfectly valid string to JSON
Schema, and a hole in the graph. CI runs it on every PR, and also re-runs the
emitter to confirm `knowledge/` still matches its specs.

> **Gotcha:** `imports: [lokf]` resolves against the *working directory*, not
> the schema file, so validation has to run from `schema/`. `schema/lokf.yaml`
> is a pinned copy of the LOKF schema the corpus was built against.

Entity files are owned by the issue that first wrote them: re-running that
issue's spec rewrites the entity, every other issue leaves it alone. So an
entity is enriched in the spec where it was first declared, and the emitter
carries the change through.

### Enriched regions

The lean profile above (claim, actor, themes, trajectory edge) covers the whole
corpus. Regions of the graph are then enriched with the rest of what LOKF and
the domain schema can say — the first is the
[recursive-self-improvement](knowledge/themes/recursive-self-improvement.md)
cluster, the newsletter's namesake thread. An enriched development carries:

| slot | what it holds |
|---|---|
| `description` | one sentence of significance — the author's framing, not a restatement of the claim |
| `score`, `occurred_on` | the headline figure verbatim with its unit; the event date when it differs from the issue date and is evidenced |
| `about`, `relatedTo`, `references`, `relations[]` | the systems and benchmarks it concerns; lateral links; labelled edges (using a valid predicate plus `relation_label` for interpretations such as `extends`) |
| `tags` | a small controlled vocabulary for slicing (`rsi`, `speedrun`, `kernels`, `chip-design`, `forecast`, …) |
| `sources[]` | the issue first, with a `supporting_text` excerpt of at most fifteen words that anchors the claim; then the primary sources the newsletter links |
| `verified[]` | a machine-confirmed check of the claim against the issue text, with the model version as the actor (`claude-fable-5-1/2026-09-17`) |

Enriched entities gain `description`, `resource`, `tags`, a Wikidata `sameAs`
where one was verified, and type-specific slots (`developed_by`, `evaluated_on`,
`published_by`, `measures_capability`). A `roles/` collection reifies the
positions the newsletter states for people (LOKF `Role`: `roleName`, `memberOf`,
`holder`). Themes in an enriched region carry a `genre: explanation` essay of
the trajectory with dated links into it.

## Provenance

Every concept carries a `sources[]` entry pointing at the Substack permalink it
came from. Claims are written as original one-sentence summaries rather than
quotations; the source link is the thing to check them against. Where a
`supporting_text` excerpt is present it is a short anchor for that check, never
a reproduction of the prose.

Licensed CC BY 4.0. Not affiliated with or endorsed by Dr. Alex Wissner-Gross;
this is a reader's index of a public newsletter.

### Browsing and search

The graph opens on the newest issue. Article and topic selectors load individual
static files from `graph-data/`; no full-graph download or layout is needed.
Large topics and entity neighborhoods are paginated in groups of 60 connections,
with at most 180 nodes in a view. A context-limit message explains omitted
neighbors. Select a node and choose **Explore connections** to continue, or use
`?focus=<concept-id>&page=2` to share a view. Browser Back restores earlier views.
The complete graph remains available as a separate export.

The home-page search lazily loads a generated, weighted full-text index covering
titles, tags, descriptions, claims, theses, and markdown bodies. Multiple words
narrow results; the final word supports prefix matching. Results can be filtered
by concept type and are shown in batches of 20. Query URLs preserve `q` and `type`.

Run `npm test` for graph-boundary and search regression checks, and `npm run build`
to generate the scoped graph files, search index, and site. CI runs both checks.

The graph’s **Layout** button offers fast spectral/force placement (fCoSE),
Markov community clusters with labeled boundaries, concept-type groups, classic
CoSE force placement, and radial connection hubs. Community detection uses the
visible substantive relationships, excluding article-membership links; inferred
groups describe the current scope, not a permanent taxonomy. Type colors remain
consistent between layouts. Layouts recompute when filters change, can be rerun
with **Rearrange**, and work in full screen. The selection is saved locally and
can be shared with `&layout=communities` (or `fcose`, `types`, `cose`, `radial`).
Relationship labels are optional to reduce clutter.
