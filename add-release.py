#!/usr/bin/env python3
"""Add a GitHub release to fnpack.json for the given apps.

Usage: ./add-release.py <owner/repo> <tag> <version> <app> [<app> ...]
  e.g. ./add-release.py jiaaom/up6-linux-drivers v1.5 1.5.0 t6-drivers t6-control t6-panel

Each app's FPK must be a release asset named <app>.fpk. download_url / sha256 /
size come from the release (needs `gh`); the architecture key and
os_min_version are copied from the app's previous release. Changelogs are left
as TODO to edit by hand.
"""
import json, subprocess, sys
from datetime import datetime, timedelta, timezone

repo, tag, ver, names = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
if not names:
    sys.exit(__doc__)
rel = json.loads(subprocess.check_output(
    ["gh", "release", "view", tag, "-R", repo, "--json", "assets,publishedAt"]))
assets = {a["name"]: a for a in rel["assets"]}
when = (datetime.fromisoformat(rel["publishedAt"].replace("Z", "+00:00"))
        .astimezone(timezone(timedelta(hours=8))).isoformat(timespec="seconds"))

src = json.load(open("fnpack.json"))
for name in names:
    app = src["apps"][name]
    prev = app["releases"][max(app["releases"], key=lambda v: [int(x) for x in v.split(".")])]
    arch = next(iter(prev["packages"]))
    a = assets[f"{name}.fpk"]
    app["releases"][ver] = {
        "changelog": "TODO",
        "i18n": {"en-US": {"changelog": "TODO"}},
        "updated_at": when,
        **({"os_min_version": prev["os_min_version"]} if "os_min_version" in prev else {}),
        "packages": {arch: {
            "download_url": f"https://github.com/{repo}/releases/download/{tag}/{name}.fpk",
            "sha256": a["digest"].removeprefix("sha256:"),
            "size": a["size"],
        }},
    }
with open("fnpack.json", "w") as f:
    json.dump(src, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"added {ver} for {', '.join(names)}; now edit the TODO changelogs")
