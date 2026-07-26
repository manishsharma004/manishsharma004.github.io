# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is
This is a **fully static website** (a GitHub Pages / Vercel style deploy). The portfolio
is a multi-page static site at the repo root (`index.html`, `about.html`, `experience.html`,
`skills.html`, `education.html`, `contact.html`, plus shared `css/site.css` and `js/site.js`).
Several self-contained static mini-apps are also served from subfolders:

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

Then visit `http://localhost:8000/index.html`. Portfolio pages are at e.g.
`http://localhost:8000/about.html` and `http://localhost:8000/experience.html`.
Sub-apps are reachable at e.g. `http://localhost:8000/chessclock/index.html` and
`http://localhost:8000/dsalgo/questions.html`.

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
`404.html` is still a legacy Next.js export and does not match the portfolio design.
The `_next/` folder is only used by that 404 page.
