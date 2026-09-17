#!/usr/bin/env python3
"""Emit LOKF concept files from a structured issue definition.

Each issue of The Innermost Loop names on the order of thirty distinct
developments. Hand-writing that many frontmatter blocks per issue is where
mistakes live, so issues are declared as data in ``tools/issues/`` and rendered
here. Entities (organizations, systems, benchmarks, facilities, themes) are
written only if they do not already exist, so later issues reuse them and only
their developments accumulate.

    uv run python tools/emit.py tools/issues/2025-12-11.py
"""
from __future__ import annotations

import pathlib
import runpy
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge"

BASE = "https://nicholsn.github.io/innermost-loop-kb/"
#: `author` has range Agent and is inlined, so it takes an object - not the
#: OKF actor string, which is only correct for `sources[].author`.
AUTHOR_AGENT = {"type": "Person", "id": BASE + "people/alex-wissner-gross",
                "name": "Dr. Alex Wissner-Gross"}


def iri(*parts: str) -> str:
    """A concept's absolute IRI.

    Frontmatter relations must carry full IRIs, as LOKF's own reference bundle
    does. A leading-slash shorthand ("/organizations/oracle.md") looks right and
    even resolves for `lokf validate --check-refs`, because Bundle.get() joins it
    to base_iri - but JSON-LD resolves a leading slash against the document's
    ORIGIN, so the projection silently emits edges pointing at
    https://host/organizations/oracle.md, which is not a concept in this graph.
    """
    return BASE + "/".join(parts)


def _round_trips_as_str(s: str) -> bool:
    """True when YAML reads ``s`` back as the same string, not an int/date/bool."""
    try:
        return yaml.safe_load("v: " + s)["v"] == s
    except Exception:
        return False


def _yaml_scalar(v: str, *, flow: bool = False) -> str:
    """Quote a scalar when YAML would otherwise mis-read it.

    ``flow=True`` is for values inside an inline ``{ a: 1, b: 2 }`` mapping,
    where a comma or a bracket terminates the value - an unquoted title like
    "Welcome to December 11, 2025" silently truncates at the comma.
    """
    s = str(v)
    risky = s and (s[0] in "!&*[]{}#|>%@`\"'" or ": " in s or s.endswith(":"))
    if flow and s and any(c in s for c in ",{}[]"):
        risky = True
    if not risky and s and not _round_trips_as_str(s):
        # YAML 1.1 reads "2:1" as sexagesimal 121 and "2034-07-18" as a date.
        risky = True
    if risky:
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


def _fm(data: dict) -> str:
    out = ["---"]
    for k, v in data.items():
        if v is None or v == [] or v == "":
            continue
        if isinstance(v, list):
            out.append(f"{k}:")
            for i in v:
                # `tags` is a list of strings, but an unquoted 2025-12-11 is a
                # YAML *date*. lokf validate tolerated it; Astro's content schema
                # rejected tags.1 as an object and broke the site build.
                if k == "tags":
                    out.append('  - "%s"' % str(i).replace('"', '\\"'))
                    continue
                if isinstance(i, dict):
                    # a list of mappings (sources[]) - inline, not str()-ed, which
                    # silently produced a list of quoted Python reprs
                    inner = ", ".join(f"{ik}: {_yaml_scalar(iv, flow=True)}" for ik, iv in i.items())
                    out.append(f"  - {{ {inner} }}")
                else:
                    out.append(f"  - {_yaml_scalar(i)}")
        elif isinstance(v, dict):
            inner = ", ".join(f"{ik}: {_yaml_scalar(iv, flow=True)}" for ik, iv in v.items())
            out.append(f"{k}: {{ {inner} }}")
        else:
            out.append(f"{k}: {_yaml_scalar(v)}")
    out.append("---")
    return "\n".join(out)


def write(rel: str, front: dict, body: str, *, overwrite: bool = False) -> bool:
    """Write one concept file. Returns True if it was created or updated."""
    path = KB / rel
    if path.exists() and not overwrite:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_fm(front) + "\n\n" + body.strip() + "\n", encoding="utf-8")
    return True


def emit(spec: dict) -> dict:
    """Render one issue spec. Returns per-kind counts of files written."""
    counts: dict[str, int] = {}

    def bump(kind: str, made: bool) -> None:
        if made:
            counts[kind] = counts.get(kind, 0) + 1

    issue = spec["issue"]
    date = issue["date"]
    # Feature essays share a publication date with that day's regular issue, so
    # the file is keyed by an explicit slug when one is given, and by the date
    # otherwise - which keeps every daily issue at issues/<date>.md as before.
    slug = issue.get("slug", date)
    src = {"id": f"iml-{slug}", "resource": issue["url"], "title": issue["title"],
           "author": "human:alex-wissner-gross", "last_modified": date}

    # -- entities: written once, reused by every later issue ----------------
    # (spec key, directory) - keyed explicitly rather than pluralizing, which
    # silently dropped "facilities" when it was derived as "facility" + "s".
    for key, rel_dir in (
        ("organizations", "organizations"),
        ("systems", "systems"),
        ("benchmarks", "benchmarks"),
        ("facilities", "facilities"),
        ("hardware", "hardware"),
        ("people", "people"),
        ("themes", "themes"),
    ):
        kind = rel_dir.rstrip("s")
        for e in spec.get(key, []):
            front = {"type": e["type"], "title": e["title"]}
            front.update({k: v for k, v in e.items() if k not in ("type", "title", "body", "id")})
            front = {k: v for k, v in front.items() if v is not None}
            front["sources"] = [src]
            bump(kind, write(f"{rel_dir}/{e['id']}.md", front, e.get("body", "")))

    # -- the issue itself ---------------------------------------------------
    dev_ids = [d["id"] for d in spec.get("developments", [])]
    bump("issue", write(
        f"issues/{slug}.md",
        {
            "type": "Issue", "title": issue["title"], "issue_date": date,
            "resource": issue["url"], "thesis": issue["thesis"],
            "author": [AUTHOR_AGENT],
            "covers": [iri("developments", i) for i in dev_ids],
            "tags": ["issue"],
            "generated": {"by": "process:iml-emit", "at": f"{date}T00:00:00Z"},
            "sources": [src],
        },
        issue["body"],
        overwrite=True,
    ))

    # -- developments -------------------------------------------------------
    for d in spec.get("developments", []):
        front = {
            "type": "Development", "title": d["title"],
            "claim": d["claim"], "domain": d["domain"],
            "reported_in": [iri("issues", slug)],
            # an actor is usually an organization id, but a development can be
            # attributed to a person ("people/terry-tao") - a bare id keeps the
            # common case short, a path selects any other collection.
            "actor": [iri(a) if "/" in a else iri("organizations", a)
                      for a in d.get("actor", [])],
            "about": d.get("about"),
            "evidences": [iri("themes", t) for t in d.get("evidences", [])],
            "score": d.get("score"),
            "occurred_on": d.get("occurred_on"),
            "supersedes": d.get("supersedes"),
            "tags": ["development", date],
            "generated": {"by": "process:iml-emit", "at": f"{date}T00:00:00Z"},
            "sources": [src],
        }
        front = {k: v for k, v in front.items() if v}
        bump("development", write(f"developments/{d['id']}.md", front, d.get("body", ""),
                                  overwrite=True))
    return counts


def reindex() -> None:
    """Regenerate knowledge/index.md from whatever is on disk.

    The bundle root is the site's front page and the graph's entry point, and it
    has to stay true across 233 issues - so it is derived, never hand-edited.
    """
    import yaml

    def load(rel: str) -> list[tuple[str, dict]]:
        out = []
        for f in sorted((KB / rel).glob("*.md")):
            fm = yaml.safe_load(f.read_text(encoding="utf-8").split("---", 2)[1])
            out.append((f.stem, fm))
        return out

    issues = load("issues")
    by_date = sorted(issues, key=lambda t: str(t[1]["issue_date"]))
    themes = load("themes")
    counts = {d.name: len(list(d.glob("*.md")))
              for d in sorted(KB.iterdir()) if d.is_dir()}

    lines = [
        "# The Innermost Loop — a knowledge graph",
        "",
        "Every markdown file under `knowledge/` is one concept; together they are a",
        "queryable graph of [The Innermost Loop](https://theinnermostloop.substack.com/),",
        "Dr. Alex Wissner-Gross's newsletter of daily developments in machine",
        "intelligence — and the source for every claim in it.",
        "",
        "The unit of the corpus is the **development**: one dated, attributed claim.",
        "An **issue** bundles the developments it reported; a **theme** is a thread",
        "running through them. That separation is what lets the corpus be read as a",
        "trajectory rather than a pile of days.",
        "",
        "## Coverage",
        "",
        f"**{len(issues)} of 233 issues** modelled"
        + (f", {by_date[0][1]['issue_date']} → {by_date[-1][1]['issue_date']}."
           if issues else "."),
        "",
        "| | count |",
        "|---|---|",
    ]
    for name, n in counts.items():
        lines.append(f"| {name} | {n} |")

    if themes:
        lines += ["", "## Themes", ""]
        for stem, fm in sorted(themes, key=lambda t: str(t[1].get("first_seen") or "")):
            lines.append(f"* [{fm['title']}](themes/{stem}.md) — first seen "
                         f"{fm.get('first_seen', '?')}")

    if issues:
        lines += ["", "## Issues", ""]
        for stem, fm in sorted(by_date, key=lambda t: str(t[1]["issue_date"]),
                               reverse=True)[:20]:
            lines.append(f"* [{fm['title']}](issues/{stem}.md) — {fm.get('thesis', '')}")
        if len(issues) > 20:
            lines.append(f"* … and {len(issues) - 20} earlier issues")

    front = (KB / "index.md").read_text(encoding="utf-8").split("---", 2)[1]
    (KB / "index.md").write_text("---" + front + "---\n\n" + "\n".join(lines) + "\n",
                                 encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        sys.exit("usage: emit.py <issue-spec.py> [more-specs.py ...]")
    total: dict[str, int] = {}
    for arg in argv[1:]:
        spec = runpy.run_path(arg)["SPEC"]
        for k, v in emit(spec).items():
            total[k] = total.get(k, 0) + v
    reindex()
    print("  wrote: " + ", ".join(f"{v} {k}(s)" for k, v in sorted(total.items())) if total
          else "  nothing new")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
