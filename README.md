# Dr Xingran "Gillian" Gao | Portfolio

**Live website:** [https://gilliangao.github.io](https://gilliangao.github.io)

Environmental scientist and risk analyst based in Cambridge, UK, specialising in climate, nature, ESG and water risk. This portfolio is designed for recruiters and hiring managers reviewing Gillian for roles in climate/ESG risk, climate data science, and sustainability consulting.

![Dr Xingran Gao in a laboratory](assets/images/gillian-gao-lab.jpg)

## Profile Snapshot

- **Location:** Cambridge, UK
- **Work eligibility:** UK Indefinite Leave to Remain; no visa sponsorship required
- **Focus areas:** climate risk, nature and biodiversity risk, ESG, water and flood modelling, geospatial data science, applied AI
- **Credentials:** Chartered Scientist (CSci), Chartered Environmentalist (CEnv), MIMMM
- **Contact:** [gxr.gao@gmail.com](mailto:gxr.gao@gmail.com)
- **LinkedIn:** [linkedin.com/in/gillian-gao-056b23107](https://www.linkedin.com/in/gillian-gao-056b23107/)
- **GitHub:** [github.com/gilliangao](https://github.com/gilliangao)

## Portfolio Highlights

- Cambridge PhD in Environmental Science, combining machine learning with atmospheric physics for urban climate research.
- Risk Analyst at Risilience, building quantitative climate, nature and water-risk models for multi-sector clients.
- Research Associate at the University of Cambridge, leading a 3D geospatial Fenland peatland digital twin project.
- Former Arup consultant delivering regulatory water modelling, flood-risk appraisal and asset-management review.
- Built evidence-led tools and models using Python, Google Earth Engine, BigQuery, Plotly, Tygron, QGIS and cloud/HPC workflows.

## Website Features

- One-page professional portfolio with anchored navigation.
- Editable content stored in `data/profile.toml`.
- Interactive Plotly charts for career timeline, project landscape and UK project locations.
- GitHub Pages deployment through GitHub Actions.
- Plain static HTML/CSS/JS output in `dist/`, with no runtime server needed.

## For Recruiters

The best way to review the portfolio is the live site:

**[Open Gillian's portfolio website](https://gilliangao.github.io)**

The site includes selected projects, quantified impact, skills, credentials, recognition, contact details and CV download link.

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

To make the website public, create a public GitHub repository named exactly `gilliangao.github.io`, then run:

```bash
git remote add origin https://github.com/gilliangao/gilliangao.github.io.git
git branch -M main
git push -u origin main
```

After the first push, open the repository on GitHub and go to Settings -> Pages -> Source: GitHub Actions. The site will publish at `https://gilliangao.github.io`.

If the repository already has a remote, check it with:

```bash
git remote -v
```

Then push with:

```bash
git push -u origin main
```

## Before Sharing With Interviewers

1. Confirm the repository is public.
2. Confirm GitHub Pages is enabled: Settings -> Pages -> Source: GitHub Actions.
3. Wait for the GitHub Actions deployment to finish successfully.
4. Open [https://gilliangao.github.io](https://gilliangao.github.io) in a private/incognito browser window.
5. Add the live website link to your CV, LinkedIn profile and job applications.
6. Add your CV PDF at `assets/cv/Gillian-Gao-CV.pdf` so the website's Download CV button works.

## Notes

- Chartered Engineer is intentionally shown as an application in progress, not as an awarded credential.
- LinkedIn and GitHub links come from `data/profile.toml`; confirm them before going live.
- The generated `dist/` directory is ignored by git because GitHub Actions builds it during deployment.
