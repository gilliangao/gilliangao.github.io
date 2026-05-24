# Codex Build Brief — Personal Portfolio Website

This file is a ready-to-use prompt for **OpenAI Codex**. Open Codex in an empty
folder where you want the project to live, then paste **everything below the
line** as your first message. The appendix already contains your real content,
so Codex should not invent or guess anything.

> Before you paste: see "What you need to do yourself" at the very bottom of this
> file — three small manual steps (GitHub repo, CV PDF, link checks).

---

## PROMPT FOR CODEX — copy from here ↓

You are building a personal portfolio website for **Dr Xingran "Gillian" Gao**,
a University of Cambridge environmental scientist and climate-risk analyst. The
site's purpose is to support her UK job search in climate/ESG risk, climate data
science, and sustainability consulting. It must look credible to hiring managers
at large firms (banks, insurers, energy companies, consultancies).

Work in the current directory. Build the whole project, run it, and verify the
output before telling me you are done. Ask me only if something is genuinely
blocking; otherwise make sensible decisions and keep going.

### 1. Tech stack (required — do not substitute)

- **Python 3.12**, with the project and its environment managed by **`uv`**.
- **`git`** initialised from the first commit, with a sensible `.gitignore`.
- **Static-site approach**: Jinja2 templates rendered by a Python build script.
  There is no server — the output is plain HTML/CSS/JS.
- **Plotly** to generate the interactive data visualisations at build time.
- Output is written to a `dist/` directory (vanilla HTML/CSS/JS, no runtime
  dependencies, works opened directly in a browser).
- **Hosting: GitHub Pages**, deployed automatically by a **GitHub Actions**
  workflow that runs the Python build on every push to `main`.

Keep it lightweight: no Node, no React, no CSS framework. Hand-written CSS in one
stylesheet. Any browser JS should be small and vanilla. Plotly figures are
generated in Python and embedded as self-contained HTML/JS.

### 2. Project structure

Create roughly this layout:

```
.
├── pyproject.toml            # uv-managed; deps: jinja2, plotly
├── uv.lock
├── .gitignore
├── README.md                 # how to build, edit, and deploy
├── build.py                  # renders templates + charts -> dist/
├── data/
│   └── profile.toml          # ALL site content lives here (see Appendix A)
├── templates/
│   ├── base.html             # head, meta/OG tags, header, footer
│   └── index.html            # the single page, section by section
├── src/
│   └── charts.py             # Plotly figures -> HTML fragments
├── static/
│   ├── style.css
│   ├── main.js               # animated stat counters, smooth scroll
│   └── favicon.svg           # simple "GG" monogram, climate-toned
├── assets/
│   └── cv/                   # Gillian drops her CV PDF here
└── .github/
    └── workflows/
        └── deploy.yml        # build with uv + deploy to GitHub Pages
```

All written copy must come from `data/profile.toml` so Gillian can edit text
without touching code. Templates and `build.py` read from it.

### 3. Build script behaviour

`build.py` should: load `data/profile.toml`; generate the Plotly figures via
`src/charts.py`; render the Jinja2 templates; copy `static/` and `assets/` into
`dist/`; write `dist/index.html`. Running `uv run python build.py` must produce a
complete, working `dist/` with zero manual steps. Add a short note in the README
on how to preview locally (e.g. `uv run python -m http.server -d dist`).

### 4. The website — sections (single page, anchored nav)

Build a **one-page site** with a sticky top nav that smooth-scrolls to anchors.
Sections, in order:

1. **Hero** — full name with post-nominals (`Dr Xingran "Gillian" Gao · CSci ·
   CEnv · MIMMM`), the positioning one-liner, location (Cambridge, UK), and
   primary links: email, LinkedIn, GitHub, and a "Download CV" button. State
   clearly that she has UK Indefinite Leave to Remain (no visa sponsorship
   needed) — recruiters look for this.
2. **About** — two or three short paragraphs from the summary content.
3. **Impact in numbers** — a strip of ~5 animated stat counters (numbers count
   up on scroll into view) drawn from the metrics in Appendix A.
4. **Selected projects** — responsive cards, one per flagship project: title,
   one-line context, her role, the tools/methods used (as small tags), and the
   quantified result. Six projects in Appendix A.
5. **Career & education timeline** — an **interactive Plotly timeline** of roles
   and degrees (horizontal, hover shows detail). This is the centrepiece data
   visual — make it clean and readable.
6. **Project landscape** — a second **interactive Plotly chart** showing the
   spread of her work across themes (Climate & ESG risk, Nature & biodiversity,
   Water & flood, Data science & modelling, Applied AI). A grouped bar or
   treemap is fine; pick whichever reads most clearly.
7. **Skills** — grouped by category (see Appendix A), shown as clean tag groups.
8. **Credentials & education** — chartered status, memberships, degrees.
9. **Recognition** — awards, patents, the hackathon result.
10. **Contact** — email, LinkedIn, GitHub, and a polite line inviting roles in
    her target areas. Footer with a build year.

**Stretch (do it if it works cleanly, skip if not):** a small UK map locating
her project work — Plotly `scatter_geo` scoped to the UK. Approximate
coordinates are in Appendix B. If it looks rough, leave it out rather than ship
something messy.

### 5. Design direction — "data-forward, professional"

- Clean, confident, and credible — a working climate-risk professional, not a
  flashy startup. Generous white space, strong typographic hierarchy.
- Restrained palette: a deep teal/forest green as the accent, near-black text on
  off-white, one cool neutral for surfaces. No gradients-as-decoration.
- The interactive charts are the visual identity — give them room and style
  their colours to match the palette (don't ship default Plotly blue).
- Fully responsive and mobile-first; must look right at 375px wide.
- Accessible: semantic HTML5 landmarks, alt text, labelled links, visible focus
  states, colour contrast meeting WCAG AA. Charts need a short text caption so
  the information isn't lost if a figure fails to load.
- Fast: no web fonts heavier than one family (a clean system or Google font is
  fine), no large images.
- In `<head>`: title, meta description, favicon, and Open Graph + Twitter card
  tags so a shared link renders well on LinkedIn.

### 6. Deployment — GitHub Pages via GitHub Actions

- Write `.github/workflows/deploy.yml` that, on push to `main`: checks out the
  repo, installs `uv` (use the `astral-sh/setup-uv` action), runs
  `uv run python build.py`, uploads `dist/` with `actions/upload-pages-artifact`,
  and deploys with `actions/deploy-pages`. Include the correct `permissions`
  (`pages: write`, `id-token: write`) and a `github-pages` environment.
- Assume the GitHub repo will be named **`gilliangao.github.io`** so the live
  URL is `https://gilliangao.github.io` with no base-path issues. If you use any
  asset paths, keep them root-relative so this works.
- In the README, give the exact click-path to enable Pages
  (Settings → Pages → Source: GitHub Actions) and the `git remote add` / push
  commands.

### 7. Accuracy rules — important

- **Chartered Engineer (CEng) is IN PROGRESS, not awarded.** Never list it as a
  post-nominal and never imply it is complete. If mentioned at all, say the
  application is in progress. CSci and CEnv *are* awarded (2026).
- Use only the content in the appendices. Do not invent metrics, employers,
  dates, or claims. If a field is blank, leave it blank rather than guessing.
- Keep the tone factual and quantified — no marketing superlatives.

### 8. When you finish

Run the build, confirm `dist/index.html` opens cleanly, and print: a summary of
what you created, how to edit content (`data/profile.toml`), how to preview
locally, and the exact steps to create the GitHub repo and go live.

---

## APPENDIX A — site content (put this into `data/profile.toml`)

### Identity

- **Name:** Dr Xingran Gao (goes by Gillian)
- **Post-nominals:** Dr · CSci · CEnv · MIMMM  *(do NOT add CEng)*
- **Location:** Cambridge, UK
- **Work eligibility:** UK — Indefinite Leave to Remain; no visa sponsorship required
- **Email:** gxr.gao@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/gillian-gao-056b23107/  *(Gillian: confirm this URL)*
- **GitHub:** https://github.com/gilliangao
- **Positioning one-liner:** Environmental scientist and risk analyst (Cambridge
  PhD, Chartered Scientist) specialising in climate, nature, ESG and water risk —
  combining quantitative modelling and data science with regulatory,
  decision-focused consulting.

### About (summary paragraphs)

1. I am an environmental scientist and risk analyst based in Cambridge. I hold a
   PhD in Environmental Science from the University of Cambridge, where I combined
   machine learning with atmospheric physics to study urban climate, processing
   more than 30 TB of spatiotemporal data across high-performance and cloud
   computing.
2. I now work at Risilience as a Risk Analyst, building quantitative models of
   climate, nature and water risk for clients across multiple sectors — from
   composite environmental indicators to global water-stress datasets and
   supply-chain scenario analysis, aligned to TCFD and TNFD. Alongside this I
   lead a part-time Cambridge research project building a 3D geospatial "digital
   twin" of Fenland peatland for the Environment Agency and Defra.
3. My background bridges technical modelling and decision-focused consulting: a
   year at Arup delivering regulatory water and flood-risk work, a Chartered
   Scientist and Chartered Environmentalist, and a consistent focus on turning
   complex environmental data into evidence people can act on.

### Impact in numbers (stat counters — pick 5)

- **30+ TB** — climate & environmental data processed across HPC and cloud
- **31:1** — benefit-cost ratio on a £1M flood scheme protecting 579 homes
- **16** — member WRF climate-model ensemble designed and run for PhD research
- **3** — Chinese invention patents in wastewater treatment (first inventor)
- **2nd** — place, Cambridge Multi-Agent Systems for Scientific Research Hackathon

### Selected projects (6 cards)

**1. Fens Peatland Digital Twin — University of Cambridge**
- Context: climate adaptation and sustainable land management in the Fens.
- Role: project lead (Research Associate).
- Tools/methods: Tygron 3D geospatial platform, hydrological modelling,
  sensitivity analysis, stakeholder engagement.
- Result: built a peatland digital twin linking water-table depth to CO2/CH4
  emissions and land stability under climate scenarios; presented decision-ready
  outputs to the Environment Agency and Defra, feeding into expansion and funding
  discussions.

**2. Global Water-Stress & Nature-Risk Models — Risilience**
- Context: clients need consistent, transparent measures of climate and nature
  risk across sectors.
- Role: risk analyst / model owner.
- Tools/methods: Google Earth Engine, BigQuery, Python, geospatial pipelines,
  composite indicators.
- Result: built and managed large-scale global water-stress datasets and
  developed an Ecosystem Integrity Index converting complex datasets into
  consistent, decision-ready risk layers, aligned to TCFD and TNFD.

**3. Welsh Water — SOAF Water-Quality Tool — Arup**
- Context: Welsh Water needed auditable evidence on combined sewer-overflow
  impacts for regulatory investment planning.
- Role: consultant, water & environmental modelling.
- Tools/methods: Python, time-series analysis, probabilistic river scenarios,
  pollutant decay/mixing models (DO, ammonia, BOD).
- Result: delivered a Python water-quality tool aligned with SOAF and UPM,
  implementing 99th-percentile and Fundamental Intermittent Standards logic for
  regulator-ready decision support.

**4. Northumbrian Water — AMMA Regulatory Review (PR24) — Arup**
- Context: Northumbrian Water needed to demonstrate asset-management maturity
  for its PR24 submission to Ofwat.
- Role: co-author, independent review.
- Tools/methods: scoring matrix, benchmarking against Ofwat framework and
  ISO 55001 / SAMP.
- Result: identified maturity gaps and delivered evidence-based investment
  recommendations supporting the regulatory submission.

**5. Flood-Risk Investment Case (FCERM) — Arup**
- Context: an Internal Drainage Board pumping-station scheme needed an Outline
  Business Case to justify multi-million-pound investment.
- Role: appraisal contributor.
- Tools/methods: FCERM cost-benefit analysis, option appraisal, risk assessment.
- Result: demonstrated a £1M investment protecting 579 homes and 1,888 ha of
  land at a 31:1 benefit-cost ratio, supporting the funding decision.

**6. Multi-Agent AI System for Urban Applications — Cambridge Hackathon**
- Context: a one-day hackathon (Accelerate Programme for Scientific Discovery ×
  Infosys Cambridge AI Centre) on multi-agent AI for scientific research.
- Role: team member.
- Tools/methods: LangGraph, AG2, multi-agent orchestration.
- Result: built a working multi-agent AI system for urban applications; placed
  2nd of all competing teams. Repo: github.com/gilliangao/multi-agent_urban

### Career & education timeline (for the Plotly timeline)

Experience:
- **Risilience — Risk Analyst (Climate & Nature Risk)** · Jun 2024 – Present ·
  Quantitative climate, nature and water risk modelling for multi-sector clients.
- **University of Cambridge — Research Associate (part-time)** · Jan 2026 –
  Present · Leads a Tygron 3D geospatial peatland digital-twin project.
- **Arup — Consultant, Water & Environmental Modelling** · Jun 2023 – Jun 2024 ·
  Regulatory water modelling, flood-risk appraisal, asset-management review.
- **Cambridge Consulting Network — Engagement Manager** · Oct 2020 – Jun 2021 ·
  Led client consulting projects and structured research.

Education:
- **PhD, Environmental Science — University of Cambridge** · Oct 2018 – May 2023 ·
  Machine learning + atmospheric physics; urban climate (LoHCool programme).
- **MSc, Environmental Engineering — Imperial College London** · 2017 – 2018 ·
  GPA 3.6/4.0; water demand analysis, wastewater & landfill design.
- **BSc (Hons), Environmental Science — University of Manchester** · 2015 – 2017 ·
  First Class Honours, GPA 3.8/4.0.
- **BSc (Hons), Atmospheric Science — Nanjing University of Information Science
  and Technology** · 2012 – 2015 · First Class Honours.

### Project landscape (theme breakdown — for the second chart)

Approximate share of her recent work by theme — use these as the data points:
- Climate & ESG risk — high
- Nature & biodiversity risk — high
- Water & flood modelling — high
- Data science & geospatial modelling — high
- Applied AI / multi-agent systems — emerging

(If a numeric chart is needed, a reasonable weighting is: Climate & ESG risk 30,
Nature & biodiversity 20, Water & flood 25, Data science & geospatial 20,
Applied AI 5 — these represent emphasis, not exact figures, so label the axis
"relative emphasis".)

### Skills (grouped tag sets)

- **Programming & data:** Python (pandas, numpy), MATLAB, SQL-style querying,
  Google Earth Engine, BigQuery, Power BI, Excel, API integration, reproducible
  HPC & cloud (AWS / GCP) workflows.
- **Modelling & analysis:** Quantitative environmental risk modelling, geospatial
  analysis (QGIS, Tygron), hydrological & water-quality modelling (SOAF, UPM),
  climate modelling (WRF ensembles), machine learning, statistical analysis,
  scenario & sensitivity analysis, cost-benefit analysis.
- **AI & emerging tools:** Multi-agent systems (LangGraph, AG2), LLM-based agent
  orchestration, agent tracing & observability concepts.
- **Domain expertise:** Climate risk (physical & transition), nature &
  biodiversity risk, ESG, water quality & flood risk, asset management, natural
  capital, decarbonisation pathways, environmental impact assessment.
- **Frameworks & regulation:** TCFD, TNFD, CSRD, Ofwat / PR24, AMMA,
  ISO 55001 / SAMP, SOAF, UPM, WFD, FCERM, CRREM, EU Taxonomy, Environment
  Agency guidance.
- **Professional:** Project management & delivery (scope, budget, QA),
  stakeholder & regulatory engagement, multidisciplinary coordination, technical
  reporting, presenting to senior stakeholders, mentoring.

### Credentials & education

- **Chartered Scientist (CSci)** — awarded 2026 (IOM3 / Science Council).
- **Chartered Environmentalist (CEnv)** — awarded 2026 (IOM3 / Society for the
  Environment).
- **Chartered Engineer (CEng)** — application in progress (IOM3 Technical Report
  Route). *Show as in progress; never as awarded.*
- **MIMMM** — Member of the Institute of Materials, Minerals and Mining (IOM3).
- Memberships: CIWEM, CIWM.
- Degrees as listed in the timeline above.

### Recognition

- 2nd place — Multi-Agent Systems for Scientific Research Hackathon, University
  of Cambridge, 11 May 2026.
- Chartered Scientist and Chartered Environmentalist, 2026.
- Three Chinese invention patents, first inventor (wastewater treatment):
  CN113149210A, CN114856454A, CN114956352A.
- First Class Honours — BSc Environmental Science (Manchester) and BSc
  Atmospheric Science (Nanjing).
- First Class Scholarship 2015–2017; Excellent Graduate Thesis 2017 (Manchester).
- Two-week specialist training at the European Centre for Medium-Range Weather
  Forecasts (ECMWF).

### Publications & research

Research projects: Low Carbon Climate-Responsive Heating and Cooling of Cities
(LoHCool); Making Safer Emergency Hospitals; Examining the Influence of Aerosols
from Air Pollution on Current and Projected Temperatures in the Urban Area.

---

## APPENDIX B — approximate UK coordinates (only for the optional map)

Use these only if you build the stretch UK project map; otherwise ignore.

- Cambridge (Risilience / University of Cambridge) — 52.20 N, 0.12 E
- The Fens / Ely (peatland digital twin) — 52.40 N, 0.26 E
- Wales (Welsh Water — SOAF tool) — 52.13 N, -3.78 E
- North East England (Northumbrian Water — AMMA) — 54.97 N, -1.61 E
- River Severn / Lower Severn (flood-risk OBC) — 51.99 N, -2.16 E

## PROMPT FOR CODEX — copy to here ↑

---

## What you need to do yourself

These three steps are outside Codex's control:

1. **Create the GitHub repo.** Make a new repository named exactly
   `gilliangao.github.io` (public). Codex will give you the `git remote add` and
   `git push` commands. After the first push, go to **Settings → Pages** and set
   **Source** to **GitHub Actions**. The site goes live at
   `https://gilliangao.github.io` within a minute or two.
2. **Add your CV PDF.** Export your CV as a PDF and drop it into `assets/cv/`
   (e.g. `assets/cv/Gillian-Gao-CV.pdf`), then push. The "Download CV" button
   will then work. Until then the button can point to a placeholder.
3. **Check your links.** Confirm the LinkedIn URL is correct (your records show
   two slightly different versions) and that the GitHub username is `gilliangao`.

Optional polish for later: buy a custom domain (e.g. `gilliangao.com`, ~£10/yr)
and point it at GitHub Pages — Codex can add the `CNAME` file when you're ready.
