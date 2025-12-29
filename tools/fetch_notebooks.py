#!/usr/bin/env python3
"""
Fetch the canonical notebooks from GitHub into ./notebooks.

Usage:
  python tools/fetch_notebooks.py
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path
from urllib.request import urlopen, Request

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest" / "notebooks.json"
OUTDIR = ROOT / "notebooks"

def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    notebooks = data.get("notebooks", [])
    if not notebooks:
        print("No notebooks listed in manifest.")
        return 2

    for nb in notebooks:
        name = nb["name"]
        raw = nb["raw_url"]
        out = OUTDIR / name
        print(f"Downloading {name} ...")
        req = Request(raw, headers={"User-Agent":"Mozilla/5.0"})
        with urlopen(req) as r:
            out.write_bytes(r.read())
        print(f"Saved: {out}")

    print("Done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
