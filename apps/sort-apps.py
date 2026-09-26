#!/usr/bin/env python3
"""Turn a folder of downloaded Canvas HTML files into apps/<slug>/index.html folders.
Run from the folder that holds the .html files. Rename each file to the app name first."""
import os, re, shutil
out = "apps"
for f in sorted(os.listdir(".")):
    if not f.lower().endswith(".html") or f == "index.html":
        continue
    slug = re.sub(r"[^a-z0-9]+", "-", os.path.splitext(f)[0].lower()).strip("-")
    os.makedirs(os.path.join(out, slug), exist_ok=True)
    shutil.copy(f, os.path.join(out, slug, "index.html"))
    print(f"{f}  ->  {out}/{slug}/index.html")
print("Done. Now fill in apps/index.html and upload the apps folder.")
