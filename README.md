# Gillian Gao Portfolio

Static, data-driven portfolio website for Dr Xingran "Gillian" Gao. The site is built with Python, Jinja2 and Plotly, then published as plain HTML/CSS/JS in `dist/`.

## Build

Install dependencies and build the site:

```bash
uv sync
uv run python build.py
```

Preview locally:

```bash
uv run python -m http.server -d dist 8000
```

Then open `http://localhost:8000`.

## Edit Content

All editable site copy and data lives in `data/profile.toml`. Update that file, rebuild with `uv run python build.py`, then review `dist/index.html`.

The CV button points to `/assets/cv/Gillian-Gao-CV.pdf`. Add the PDF at `assets/cv/Gillian-Gao-CV.pdf` when ready.

## Deploy

Create a public GitHub repository named exactly `gilliangao.github.io`, then run:

```bash
git remote add origin https://github.com/gilliangao/gilliangao.github.io.git
git branch -M main
git push -u origin main
```

After the first push, open the repository on GitHub and go to Settings -> Pages -> Source: GitHub Actions. The site will publish at `https://gilliangao.github.io`.

## Notes

- Chartered Engineer is intentionally shown as an application in progress, not as an awarded credential.
- LinkedIn and GitHub links come from `data/profile.toml`; confirm them before going live.
- The generated `dist/` directory is ignored by git because GitHub Actions builds it during deployment.
