# The Innermost Loop — a knowledge graph

A [LOKF](https://github.com/nicholsn/lokf) knowledge base modelling
[The Innermost Loop](https://theinnermostloop.substack.com/), Dr. Alex
Wissner-Gross's newsletter of daily developments in machine intelligence.

Every markdown file under `knowledge/` is one concept with YAML frontmatter, and
the whole directory projects losslessly to RDF. The goal is to turn 233 daily
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

## Provenance

Every concept carries a `sources[]` entry pointing at the Substack permalink it
came from. Claims are written as original one-sentence summaries rather than
quotations; the source link is the thing to check them against.

Licensed CC BY 4.0. Not affiliated with or endorsed by Dr. Alex Wissner-Gross;
this is a reader's index of a public newsletter.
