# Allan Blyth | Portfolio

Static site, no dependencies. Open `index.html` or host on GitHub Pages / Netlify.

- Edit `PROJECTS` list in `build.py`, then run `python build.py` to regenerate every page.
- cv saved as `Allan_Blyth_CV.pdf`
- To add a gameplay clip to a project, set its `video` field to an mp4 path (e.g. `clips/kyomen-boss.mp4`).
- Playable builds: Unity WebGL builds live in `play/<id>/Build/` and are loaded by `play/player.html?g=<id>`. Set a project's `play` field in `build.py` to that id to show the "Play in browser" panel. Builds must use Gzip compression with Decompression Fallback on, and "Name Files As Hashes" off.
- Images live in `img/` as `<slug>-cover.<ext>` and `<slug>-1.<ext>`, `<slug>-2.<ext>`, and so on. The first screenshot is used as the page's main image; drop in a new numbered file and rebuild to add one.
- Headline stats and team sizes live in the `STATS` and `TEAM` tables in `build.py`, keyed by project slug.
- The "How it works" and "Code" sections come from the `DEEP` table in `build.py`. Code excerpts are plain files in `code/`. The Kyomen excerpts are parked in `stash/` (git-ignored, so not published); to bring them back, move them into `code/` and rename `code_stashed` to `code` in Kyomen's `DEEP` entry.
- `build.py` also writes `sitemap.xml`. Change `BASE` if the site moves to another domain.
- A project with no itch.io page leaves its itch id and label empty; the "Play it" section is then left out.
- `build.py` also writes `404.html`. The home page preview image for links is `img/social-card.jpg`.
- The home page "Engine work" block loops `clips/voxel-world-loop.mp4`, a small cut of the full clip.
