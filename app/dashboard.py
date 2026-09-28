"""
Indonesia Economic Intelligence — Interactive Dashboard (Streamlit)
===================================================================
Dashboard interaktif atas 17 indikator ekonomi Indonesia (World Bank, 1960–2025).

Jalankan: streamlit run app/dashboard.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import analysis as A      # noqa: E402
import forecast as F      # noqa: E402

PROC = ROOT / "data" / "processed"

C = {
    "primary": "#C0392B", "accent": "#E4A11B", "dark": "#1B2A33",
    "grey": "#8B9AA6", "green": "#1F5C3D", "blue": "#2E6F95",
}
SERIES = [C["primary"], C["blue"], C["green"], C["accent"], "#6A4C93", "#2A9D8F"]

st.set_page_config(page_title="Indonesia Economy Intelligence",
                   page_icon=":material/public:", layout="wide",
                   initial_sidebar_state="expanded")

# label ramah-manusia
LABELS = {
    "gdp_usd": "GDP (US$)", "gdp_growth_pct": "GDP growth (%)",
    "gdp_per_capita_usd": "GDP per capita (US$)", "population": "Population",
    "urban_pct": "Urban population (%)", "life_expectancy": "Life expectancy",
    "inflation_pct": "Inflation (%)", "unemployment_pct": "Unemployment (%)",
    "lf_participation_pct": "Labour participation (%)",
    "internet_pct": "Internet users (%)", "fdi_pct_gdp": "FDI (% GDP)",
    "exports_pct_gdp": "Exports (% GDP)", "education_pct_gdp": "Education (% GDP)",
    "health_pct_gdp": "Health (% GDP)", "gini": "Gini index",
    "co2_mt": "CO2 emissions (Mt)", "land_area_km2": "Land area (km²)",
}


@st.cache_data(show_spinner="Memuat data World Bank...")
def load_data():
    wide = pd.read_csv(PROC / "indicators_wide.csv", index_col="year")
    return wide


def style_fig(fig, h=430):
    fig.update_layout(
        height=h, margin=dict(l=10, r=10, t=54, b=10),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#D5DBE1"), title=dict(font=dict(size=16, color="#fff")),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
    )
    fig.update_xaxes(gridcolor="#2A3038", zeroline=False)
    fig.update_yaxes(gridcolor="#2A3038", zeroline=False)
    return fig


def kpi(col, label, value, sub, color):
    col.markdown(
        f"""<div style="background:#1A1F2B;border-left:4px solid {color};
        padding:14px 16px;border-radius:10px;height:112px;">
        <div style="color:#9AA7B4;font-size:.76rem;text-transform:uppercase;
        letter-spacing:.06em;">{label}</div>
        <div style="color:{color};font-size:1.7rem;font-weight:700;
        margin-top:6px;">{value}</div>
        <div style="color:#6B7885;font-size:.75rem;">{sub}</div></div>""",
        unsafe_allow_html=True)


wide = load_data()
ins = A.key_insights(wide)

# ----- sidebar -----
st.sidebar.markdown("### 🎛️ Controls")
cats = sorted(set(A.__dict__.get("ERAS", [])))  # noqa
available = [c for c in wide.columns if wide[c].notna().sum() >= 15]
pick = st.sidebar.multiselect("Indicators to compare",
                              available, default=[c for c in
                              ["gdp_per_capita_usd", "life_expectancy",
                               "urban_pct", "internet_pct"] if c in available])
yr0, yr1 = int(wide.index.min()), int(wide.index.max())
rng = st.sidebar.slider("Year range", yr0, yr1, (1960, yr1))
st.sidebar.markdown("---")
st.sidebar.caption("Source: World Bank Open Data · 17 indicators · "
                   f"{yr0}–{yr1}\n\nData may include World Bank projections "
                   "for recent years.")

# ----- header -----
st.markdown(
    f"""<div style="background:linear-gradient(100deg,{C['primary']},{C['blue']});
    padding:22px 26px;border-radius:14px;margin-bottom:18px;">
    <div style="font-size:1.7rem;font-weight:800;color:white;">
    Indonesia Economic Intelligence 🇮🇩</div>
    <div style="color:#F4D9D6;font-size:.9rem;margin-top:4px;">
    60+ years of national indicators · World Bank Open Data ·
    by <b>Sandi Ridwan</b></div></div>""",
    unsafe_allow_html=True)

# ----- KPI band -----
k1, k2, k3, k4, k5 = st.columns(5)
kpi(k1, "GDP per capita", f"${ins.get('gdp_pc_latest', 0):,.0f}",
    f"from ${ins.get('gdp_pc_1967', 0):,.0f} (1967)", C["primary"])
kpi(k2, "Population", f"{ins.get('pop_latest', 0)/1e6:,.1f}M",
    f"from {ins.get('pop_1960', 0)/1e6:,.1f}M (1960)", C["blue"])
kpi(k3, "Inflation", f"{ins.get('inflation_latest', 0):.1f}%",
    f"peak {ins.get('inflation_max', 0):,.0f}% ({ins.get('inflation_max_year')})",
    C["accent"])
kpi(k4, "Urban", f"{ins.get('urban_latest', 0):.1f}%",
    f"from {ins.get('urban_1960', 0):.1f}% (1960)", C["green"])
kpi(k5, "Internet", f"{ins.get('internet_latest', 0):.1f}%",
    f"from {ins.get('internet_2000', 0):.1f}% (2000)", C["dark"])
st.write("")

tab1, tab2, tab3, tab4 = st.tabs(["📈 Trends", "🧩 Comparison",
                                  "🔮 Forecast", "⚠️ Crisis"])

# ============================ TRENDS ============================
with tab1:
    c1, c2 = st.columns(2)
    with c1:
        s = wide["gdp_per_capita_usd"].dropna()
        s = s[(s.index >= rng[0]) & (s.index <= rng[1])]
        fig = px.area(x=s.index, y=s.values,
                      labels={"x": "Year", "y": "US$"})
        fig.update_traces(line_color=C["primary"], fillcolor="rgba(192,57,43,.15)")
        for y0, y1, col, lbl in [(1998, 1999, "rgba(192,57,43,.18)", "Asian Crisis"),
                                 (2020, 2021, "rgba(31,92,61,.18)", "COVID-19")]:
            if y0 >= rng[0]:
                fig.add_vrect(x0=y0, x1=y1, fillcolor=col, line_width=0,
                              annotation_text=lbl, annotation_font_size=9)
        style_fig(fig).update_layout(title="GDP per Capita (US$)")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        s = wide["gdp_growth_pct"].dropna()
        s = s[(s.index >= rng[0]) & (s.index <= rng[1])]
        colors = [C["primary"] if v < 0 else C["green"] for v in s.values]
        fig = go.Figure(go.Bar(x=s.index, y=s.values, marker_color=colors))
        style_fig(fig).update_layout(title="GDP Growth (%)", yaxis_title="%")
        st.plotly_chart(fig, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        pop = (wide["population"].dropna() / 1e6)
        pop = pop[(pop.index >= rng[0]) & (pop.index <= rng[1])]
        fig = px.line(x=pop.index, y=pop.values, labels={"x": "Year", "y": "Million"})
        fig.update_traces(line_color=C["blue"], line_width=2.5)
        style_fig(fig).update_layout(title="Population (millions)")
        st.plotly_chart(fig, use_container_width=True)
    with c4:
        inf = wide["inflation_pct"].dropna()
        inf = inf[(inf.index >= rng[0]) & (inf.index <= rng[1]) & (inf > 0)]
        fig = px.line(x=inf.index, y=inf.values, labels={"x": "Year", "y": "%"})
        fig.update_traces(line_color=C["accent"], line_width=2.5)
        fig.update_yaxes(type="log")
        style_fig(fig).update_layout(title="Inflation (%, log scale)")
        st.plotly_chart(fig, use_container_width=True)

# ============================ COMPARISON ============================
with tab2:
    if pick:
        sub = wide[pick].loc[(wide.index >= rng[0]) & (wide.index <= rng[1])]
        # normalisasi untuk perbandingan bentuk
        norm = sub.copy()
        for cc in norm.columns:
            base = norm[cc].dropna()
            if len(base):
                norm[cc] = norm[cc] / base.iloc[0] * 100
        fig = go.Figure()
        for i, cc in enumerate(norm.columns):
            fig.add_trace(go.Scatter(x=norm.index, y=norm[cc], mode="lines",
                                     name=LABELS.get(cc, cc),
                                     line=dict(color=SERIES[i % len(SERIES)], width=2.2)))
        style_fig(fig, 480).update_layout(
            title="Indicators (indexed to first year = 100)",
            yaxis_title="Index (base=100)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Pilih minimal satu indikator di sidebar.")

    st.markdown("#### Correlation matrix (Pearson)")
    corr = A.correlation_matrix(wide, "pearson")
    keys = [k for k in ["gdp_per_capita_usd", "gdp_growth_pct", "inflation_pct",
                        "population", "urban_pct", "life_expectancy",
                        "internet_pct", "unemployment_pct", "exports_pct_gdp",
                        "co2_mt"] if k in corr.columns]
    cs = corr.loc[keys, keys]
    fig = px.imshow(cs.values, x=[LABELS.get(k, k) for k in keys],
                    y=[LABELS.get(k, k) for k in keys],
                    color_continuous_scale="RdBu_r", zmin=-1, zmax=1, text_auto=".2f")
    fig.update_traces(textfont_size=8)
    style_fig(fig, 600).update_layout(title="Correlation Heatmap")
    st.plotly_chart(fig, use_container_width=True)

# ============================ FORECAST ============================
with tab3:
    fc = F.forecast_all(wide, horizon=5)
    ft = F.summary_table(fc, 5)
    st.markdown("#### Forecast summary (5-year horizon)")
    show = ft.copy()
    show["indicator"] = show["indicator"].map(lambda x: LABELS.get(x, x))
    st.dataframe(show, use_container_width=True, hide_index=True)

    sel = st.selectbox("Detail forecast",
                       [k for k in fc.keys()],
                       format_func=lambda k: LABELS.get(k, k))
    r = fc[sel]
    h, f = r["history"], r["forecast"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=h.index, y=h.values, mode="lines",
                             name="Actual", line=dict(color=C["dark"], width=2.4)))
    fig.add_trace(go.Scatter(x=[h.index[-1]] + list(f.index),
                             y=[h.iloc[-1]] + list(f.values), mode="lines+markers",
                             name="Forecast",
                             line=dict(color=C["primary"], width=2.4, dash="dash")))
    fv = np.asarray(f.values, dtype=float)
    fig.add_trace(go.Scatter(x=list(f.index) + list(f.index)[::-1],
                             y=list(fv * 1.05) + list(fv * 0.95)[::-1],
                             fill="toself", fillcolor="rgba(192,57,43,.15)",
                             line=dict(width=0), name="±5% band"))
    style_fig(fig, 460).update_layout(
        title=f"{LABELS.get(sel, sel)} — R²={r['r2']}, backtest MAPE={r['mape_pct']}%")
    st.plotly_chart(fig, use_container_width=True)
    st.caption("⚠️ Forecast uses recent-regime trend. Inflation is volatile — "
               "treat its forecast cautiously (high backtest error).")

# ============================ CRISIS ============================
with tab4:
    st.markdown("#### Impact of the two major crises")
    t = A.crisis_impact(wide)
    t2 = t.copy()
    t2["indicator"] = t2["indicator"].map(lambda x: LABELS.get(x, x))
    st.dataframe(t2, use_container_width=True, hide_index=True)

    fig = go.Figure()
    ind = "gdp_growth_pct"
    s = wide[ind].dropna()
    s = s[s.index >= 1990]
    colors = [C["primary"] if v < 0 else C["grey"] for v in s.values]
    fig.add_trace(go.Bar(x=s.index, y=s.values, marker_color=colors,
                         name="GDP growth"))
    fig.add_vrect(x0=1998, x1=1999, fillcolor="rgba(192,57,43,.2)",
                  line_width=0, annotation_text="1998", annotation_font_size=9)
    fig.add_vrect(x0=2020, x1=2021, fillcolor="rgba(31,92,61,.2)",
                  line_width=0, annotation_text="2020", annotation_font_size=9)
    style_fig(fig, 430).update_layout(title="GDP Growth: 1998 vs 2020 recessions")
    st.plotly_chart(fig, use_container_width=True)

st.markdown(
    f"""<hr style="border-color:#2A3038;">
    <div style="color:{C['grey']};font-size:.8rem;text-align:center;">
    Indonesia Economic Intelligence 🇮🇩 · World Bank Open Data · built with
    Streamlit + Plotly · by <b>Sandi Ridwan</b><br>
    Recent years may include World Bank projections.</div>""",
    unsafe_allow_html=True)
