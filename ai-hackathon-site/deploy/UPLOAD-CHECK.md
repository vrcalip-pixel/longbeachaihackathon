# If video isn't playing on the live site

## 1. Test whether the files are there
Open this in a browser (swap in your repo name):

    https://YOUR-USERNAME.github.io/YOUR-REPO/media/hero.jpg

- **404** → the files aren't in the repo. Go to step 2.
- **Image loads** → files are fine; it's a playback issue, not an upload issue.

## 2. Check the repo layout
Your repository root must look EXACTLY like this:

    index.html
    404.html
    robots.txt
    .nojekyll
    media/          <-- a folder, at the top level
      hero.mp4
      hero-m.mp4
      hero.jpg
      band.mp4
      band-m.mp4
      band.jpg
      journey.mp4
      journey-m.mp4
      journey.jpg

Common mistakes:
- Everything nested one level deep (`site/index.html`, `site/media/...`).
  Fix: move files to the root, or set GitHub Pages to serve from that folder.
- The `media` folder didn't upload at all — GitHub's drag-and-drop sometimes
  takes files but drops folders.
- Capitalisation: `Media/` or `Hero.mp4` will 404. GitHub is case-sensitive.

## 3. Re-upload just the media folder
1. Repo → **Add file** → **Upload files**
2. Drag the whole `media` FOLDER (not the nine files individually)
3. Commit. Wait a minute, retest the URL from step 1.

If dragging the folder fails, use **Add file → Create new file**, type
`media/hero.mp4` in the filename box — typing the slash creates the folder —
then cancel and use the upload option, which will now target that folder.

## 4. Still stuck? Use the command line
```bash
cd /path/to/the/unzipped/folder
git init
git add .
git commit -m "Site with media"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main --force
```
This uploads everything with the folder structure intact and is the most
reliable route.
