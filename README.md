# AI Hackathon Microsite — Deployment Guide

Static site. No build step, no dependencies, no server. Everything here is what
gets served.

```
index.html          the entire site — HTML, CSS, and JavaScript in one file
media/              video and poster images
  hero.mp4 / hero-m.mp4 / hero.jpg          hero background (desktop / mobile / still)
  band.mp4 / band-m.mp4 / band.jpg          Los Angeles aerial band
  journey.mp4 / journey-m.mp4 / journey.jpg Seattle → Long Beach flyover
404.html            branded not-found page, redirects home after 3s
robots.txt          lets search engines index the site
.nojekyll           stops GitHub trying to process this as a Jekyll blog
CNAME.example       rename to CNAME once you own the domain
```

## Why it's one file

CSS and JavaScript are inline rather than split into `styles.css` and
`script.js`. That's deliberate for a site this size: one HTTP request instead of
three, nothing to get out of sync, and no chance of a stale cached stylesheet
against fresh HTML. At roughly 85KB it is well under the point where splitting
would help. If the site grows into multiple pages, that's the moment to split.

---

## Step 1 — Create the repository

1. Go to github.com → **New repository**
2. Name it something durable, not event-specific: `ai-hackathon` rather than
   `hackathon-sept-2026`. You'll reuse it next year.
3. Set it to **Public** (required for GitHub Pages on a free account)
4. Don't add a README — this file is your README
5. **Create repository**

## Step 2 — Upload the files

Easiest route, no command line:

1. On the empty repo page, click **uploading an existing file**
2. Drag in `index.html`, `404.html`, `robots.txt`, and the whole `media` folder
3. Commit message: `Initial site`
4. **Commit changes**

The `.nojekyll` file may not appear in the drag-and-drop (browsers hide
dotfiles). If it doesn't, create it manually: **Add file → Create new file**,
name it `.nojekyll`, leave it empty, commit. Without it GitHub may ignore
files and folders in ways that break media paths.

If you prefer the command line:

```bash
git init
git add .
git commit -m "Initial site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-hackathon.git
git push -u origin main
```

## Step 3 — Turn on GitHub Pages

1. Repo → **Settings** → **Pages** (left sidebar)
2. Source: **Deploy from a branch**
3. Branch: **main**, folder: **/ (root)** → **Save**
4. Wait about a minute, then visit
   `https://YOUR-USERNAME.github.io/ai-hackathon/`

**Test it here before buying a domain.** Check that video plays, the countdown
shows a real number, and the Eventbrite links work. If media doesn't load, it's
almost always a missing `.nojekyll` or a capitalisation mismatch in a filename
— GitHub's servers are case-sensitive even though your laptop isn't.

## Step 4 — Buy the domain (Namecheap)

See the naming strategy in the chat. Whatever you choose:

- Turn on **auto-renew** immediately
- Turn on **WHOIS privacy** (free with Namecheap) — it hides your home address
- Register it to an address more than one person can reach

## Step 5 — Point the domain at GitHub

In Namecheap: **Domain List → Manage → Advanced DNS**. Delete any default
parking records, then add:

| Type  | Host | Value                     | TTL       |
|-------|------|---------------------------|-----------|
| A     | @    | 185.199.108.153           | Automatic |
| A     | @    | 185.199.109.153           | Automatic |
| A     | @    | 185.199.110.153           | Automatic |
| A     | @    | 185.199.111.153           | Automatic |
| CNAME | www  | YOUR-USERNAME.github.io.  | Automatic |

All four A records are needed — they're GitHub's redundant servers, not
alternatives. The trailing dot on the CNAME value matters.

## Step 6 — Connect the domain in GitHub

1. Repo → **Settings** → **Pages** → **Custom domain**
2. Enter your domain (e.g. `longbeachaihackathon.org`) → **Save**
   This creates a `CNAME` file in your repo automatically. That's why
   `CNAME.example` here is only a template — don't rename it unless GitHub
   fails to create one.
3. Wait for the DNS check to pass (usually minutes, occasionally an hour)
4. Tick **Enforce HTTPS** once the certificate is issued — it will be greyed
   out until then. Do not skip this. A site collecting nothing still looks
   broken to a browser without it, and some school networks block plain HTTP.

## Step 7 — Fix the social preview

Open `index.html`, find `og:image`, and change it to your full domain:

```html
<meta property="og:image" content="https://longbeachaihackathon.org/media/hero.jpg">
```

Open Graph requires an absolute URL. Until you do this, links shared to Slack,
iMessage, or Instagram will render without artwork. Commit the change.

Also update the `Sitemap:` line in `robots.txt` if you add a sitemap later.

## Step 8 — Verify on a real phone

- Hero video plays; scroll to the LA band and the flyover and confirm both play
- Tap the Eventbrite buttons, the PS2 parking pin, and the campus pin
- Text yourself the link and confirm the preview card shows the hero image
- Turn on Reduced Motion (iOS: Settings → Accessibility → Motion) and reload:
  video should become stills and animation should stop, with nothing broken

---

## Making changes later

Edit `index.html` on github.com directly (pencil icon) and commit. The site
updates in about a minute. Common edits are marked with comments in the file:

| What | Search `index.html` for |
|------|------------------------|
| Waiver PDF link | `WAIVER` |
| Family track (confirm or delete) | `FOR FAMILIES` |
| Video files | `const MEDIA` |
| Event date/time for the countdown | `EVENT_START` |
| Challenge briefs | `const BRIEFS` |
| Ambient music (swap for an mp3) | `AUDIO_FILE` |
| Eventbrite links | `eventbrite.com` |

**If the page ever goes blank below the hero**, you've introduced a JavaScript
syntax error. Sections start hidden and are revealed by script, so one bad
character hides everything. Undo the last commit (repo → commit history → revert)
and the site comes straight back.

## Next year

Don't create a new repo. Branch this one, update dates, swap the media, and
merge. The URL keeps its search history and every printed flyer and QR code
from prior years still resolves.
