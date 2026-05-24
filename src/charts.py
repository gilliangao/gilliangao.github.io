from __future__ import annotations

from datetime import date

import plotly.graph_objects as go

PLOT_CONFIG = {
    "displayModeBar": False,
    "responsive": True,
}

COLORS = {
    "teal": "#0f766e",
    "forest": "#14532d",
    "sage": "#6b8f71",
    "ink": "#111827",
    "muted": "#64748b",
    "surface": "#f4f7f5",
    "line": "#d8e3dc",
}


def _fragment(fig: go.Figure) -> str:
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={
            "family": "Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
            "color": COLORS["ink"],
        },
        margin={"l": 16, "r": 16, "t": 28, "b": 24},
    )
    return fig.to_html(full_html=False, include_plotlyjs=True, config=PLOT_CONFIG)


def timeline_chart(items: list[dict]) -> str:
    rows = []
    for item in items:
        rows.append(
            {
                "Role": item["name"],
                "Start": item["start"],
                "Finish": item["end"],
                "Type": item["kind"],
                "Dates": item["date_label"],
                "Detail": item["detail"],
            }
        )

    fig = go.Figure()
    for role_type, color in (("Experience", COLORS["teal"]), ("Education", COLORS["sage"])):
        type_rows = [row for row in rows if row["Type"] == role_type]
        fig.add_trace(
            go.Bar(
                name=role_type,
                y=[row["Role"] for row in type_rows],
                x=[
                    (date.fromisoformat(row["Finish"]) - date.fromisoformat(row["Start"])).days
                    for row in type_rows
                ],
                base=[row["Start"] for row in type_rows],
                orientation="h",
                marker={"color": color, "line": {"color": "white", "width": 1.5}},
                customdata=[[row["Dates"], row["Detail"]] for row in type_rows],
                hovertemplate="<b>%{y}</b><br>%{customdata[0]}<br>%{customdata[1]}<extra></extra>",
            )
        )
    fig.update_yaxes(autorange="reversed", title="", tickfont={"size": 12})
    fig.update_xaxes(title="", gridcolor=COLORS["line"])
    fig.update_traces(marker_line_color="white", marker_line_width=1.5, opacity=0.92)
    fig.update_layout(height=560, legend_title_text="", bargap=0.35)
    return _fragment(fig)


def landscape_chart(items: list[dict]) -> str:
    fig = go.Figure(
        data=[
            go.Bar(
                x=[item["weight"] for item in items],
                y=[item["theme"] for item in items],
                orientation="h",
                marker={
                    "color": ["#0f766e", "#14532d", "#256d85", "#6b8f71", "#b7791f"],
                    "line": {"color": "white", "width": 1},
                },
                hovertemplate="<b>%{y}</b><br>Relative emphasis: %{x}<extra></extra>",
            )
        ]
    )
    fig.update_yaxes(autorange="reversed", title="")
    fig.update_xaxes(title="Relative emphasis", gridcolor=COLORS["line"], range=[0, 34])
    fig.update_layout(height=390, showlegend=False)
    return _fragment(fig)


def uk_map(points: list[dict]) -> str:
    fig = go.Figure(
        data=[
            go.Scattergeo(
                lon=[point["lon"] for point in points],
                lat=[point["lat"] for point in points],
                text=[f"{point['name']}<br>{point['description']}" for point in points],
                mode="markers+text",
                textposition="top center",
                marker={"size": 12, "color": COLORS["teal"], "line": {"width": 2, "color": "white"}},
                hovertemplate="<b>%{text}</b><extra></extra>",
            )
        ]
    )
    fig.update_geos(
        scope="europe",
        projection_type="mercator",
        center={"lat": 53.2, "lon": -1.4},
        lataxis_range=[50, 56],
        lonaxis_range=[-6, 2],
        showland=True,
        landcolor="#edf4ef",
        showocean=True,
        oceancolor="#f7faf9",
        showcountries=True,
        countrycolor="#cad8d0",
        coastlinecolor="#9eb2a7",
    )
    fig.update_layout(height=420, showlegend=False)
    return _fragment(fig)
