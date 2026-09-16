#!/usr/bin/env python3
"""Generate this KB's JSON-LD context from the domain schema.

`gen-jsonld-context` alone is not enough. LOKF's own context is that generator's
output *plus* a post-processing step (see ``lokf.build.generate``), and without
it the authoring form stops being valid JSON-LD: `type:` and `id:` in
frontmatter are OKF keys, not JSON-LD keywords, so they must be aliased to
`@type` and `@id` or nothing in the bundle gets a type at all.

    python tools/gen_context.py        # writes ./lokf.context.jsonld

The output is named `lokf.context.jsonld` at the repo root because that is the
filename `lokf.schema.load_context()` looks for when walking up from the working
directory. It is *this* KB's context - LOKF's terms plus the domain's - not a
copy of LOKF's.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schema" / "innermost.yaml"
OUT = ROOT / "lokf.context.jsonld"


def main() -> int:
    if not SCHEMA.exists():
        sys.exit(f"no schema at {SCHEMA}")
    # imports resolve against the working directory, not the schema file
    proc = subprocess.run(
        ["gen-jsonld-context", SCHEMA.name],
        cwd=SCHEMA.parent, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        sys.exit(f"gen-jsonld-context failed:\n{proc.stderr[-2000:]}")

    doc = json.loads(proc.stdout)
    ctx = doc["@context"]

    # The two aliases that make unmodified OKF frontmatter valid JSON-LD.
    ctx["type"] = "@type"
    ctx["id"] = "@id"

    # `author` must not be @id-coerced: OKF actor strings ("human:awg") are
    # literals, and coercion would mint IRIs in an unregistered scheme.
    if isinstance(ctx.get("author"), dict):
        ctx["author"].pop("@type", None)

    doc.setdefault("comments", {})["note"] = (
        "Context for the Innermost Loop KB: LOKF's terms plus this corpus's own "
        "(Issue, Development, Theme, AISystem, Benchmark, Facility). Generated "
        "by tools/gen_context.py from schema/innermost.yaml - do not hand-edit."
    )
    doc["comments"].pop("generation_date", None)  # churn, not information

    OUT.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    types = [k for k in ("Issue", "Development", "Theme", "AISystem", "Benchmark",
                         "Facility") if k in ctx]
    print(f"  wrote {OUT.relative_to(ROOT)} ({len(ctx)} terms, domain types: {', '.join(types)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
