from __future__ import annotations

import shutil
import tomllib
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from src.charts import landscape_chart, timeline_chart, uk_map

ROOT = Path(__file__).parent
DIST = ROOT / "dist"


def load_profile() -> dict:
    with (ROOT / "data" / "profile.toml").open("rb") as profile_file:
        return tomllib.load(profile_file)


def copy_tree(source: Path, destination: Path) -> None:
    if source.exists():
        shutil.copytree(source, destination, dirs_exist_ok=True)


def main() -> None:
    profile = load_profile()
    charts = {
        "timeline": timeline_chart(profile["timeline"]),
        "landscape": landscape_chart(profile["landscape"]),
        "map": uk_map(profile["map_points"]),
    }

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html", "xml"]),
    )
    for page in ("index.html", "services.html"):
        template = env.get_template(page)
        context = dict(profile=profile, charts=charts, year=date.today().year, page_path=page)
        if page == "services.html":
            context["page_title"] = f"Services | {profile['identity']['display_name']}"
        html = template.render(**context)
        (DIST / page).write_text(html, encoding="utf-8")

    copy_tree(ROOT / "static", DIST / "static")
    copy_tree(ROOT / "assets", DIST / "assets")


if __name__ == "__main__":
    main()
