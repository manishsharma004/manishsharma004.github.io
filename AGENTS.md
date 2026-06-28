# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is
This is a **fully static website** (a GitHub Pages / Vercel style deploy). It contains a
pre-built Next.js static export (`index.html`, `_next/`, `404.html`) plus several
self-contained static mini-apps served from subfolders:

- `json/` – JSON viewer
- `mobile-preview/` – mobile preview tool
- `dsalgo/questions.html` – LeetCode/DS-Algo question browser (uses CodeMirror)
- `understanding-deep-learning-jdprince/` – reading notes page
- `chessclock/` – interactive chess clock

There is **no source/build step in the repo** — the built HTML/CSS/JS is committed
directly. Do not try to run a Next.js dev/build; there is no root `package.json`.

### Running the site (dev)
Serve the repository root over static HTTP and open it in a browser:

```
python3 -m http.server 8000   # run from the repo root (/workspace)
```

Then visit `http://localhost:8000/index.html`. Sub-apps are reachable at e.g.
`http://localhost:8000/chessclock/index.html` and
`http://localhost:8000/dsalgo/questions.html`. Serve from the **root** because
`index.html` references `_next/` assets via absolute paths (`/_next/...`).

### Dependencies
The only npm dependency is `codemirror`, used by `dsalgo/questions.html` via a relative
path (`dsalgo/node_modules/codemirror/...`). It is already committed under
`dsalgo/node_modules`, so the site works with no install. The startup update script runs
`npm install` in `dsalgo/` to keep it fresh; this is the only dependency step.

### Lint / test / build
- **Build:** none — the static export is already committed.
- **Tests:** none. `dsalgo/package.json` has a placeholder `test` script that just
  errors (`npm test` exits 1 by design).
- **Lint:** `.eslintrc` extends `next` configs, but no ESLint/Next toolchain is installed
  at the repo root, so there is no runnable lint command.

### Gotcha
The committed root `index.html` is a static Next.js export whose nav list relies on
client-side hydration; some links may not render fully on the bare page. Navigate to
sub-apps directly by URL if a homepage link is missing.
