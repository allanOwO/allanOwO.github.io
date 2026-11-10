# Allan Blyth | Portfolio

Static site, no dependencies. Open `index.html` or host on GitHub Pages / Netlify.

- Edit `PROJECTS` list in `build.py`, then run `python build.py` to regenerate every page.
- cv saved as `Allan_Blyth_CV.pdf`
- To add a gameplay clip to a project, set its `video` field to an mp4 path (e.g. `clips/kyomen-boss.mp4`).
- Playable builds: Unity WebGL builds live in `play/<id>/Build/` and are loaded by `play/player.html?g=<id>`. Set a project's `play` field in `build.py` to that id to show the "Play in browser" panel. Builds must use Gzip compression with Decompression Fallback on, and "Name Files As Hashes" off.
