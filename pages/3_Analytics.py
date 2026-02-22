import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

from agent.risk_engine import calculate_risk
from agent.anomaly_detector import detect_anomalies

st.set_page_config(layout="wide", page_title="DBIQ Analytics")

st.title("📊 AI Observability & Performance Analytics")

# -----------------------------------
# LOAD DATA
# -----------------------------------
if "df" in st.session_state:
    df = st.session_state.df
else:
    df = pd.read_csv("data/query_logs.csv")
    st.session_state.df = df

# ensure computed columns exist
if "risk_score" not in df.columns:
    df["risk_score"] = df.apply(calculate_risk, axis=1)

if "anomaly" not in df.columns:
    df = detect_anomalies(df)

# -----------------------------------
# SYSTEM HEALTH SCORE
# -----------------------------------
st.subheader("🧠 System Health Score")

health_score = 100 - int(df["risk_score"].mean())

st.metric("Overall Warehouse Health", f"{health_score}/100")

# -----------------------------------
# RISK DISTRIBUTION
# -----------------------------------
st.subheader("⚠ Risk Distribution")

fig = px.histogram(
    df,
    x="risk_score",
    nbins=20,
    title="Risk Score Distribution Across Queries"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------
# EXECUTION TIME ANALYSIS
# -----------------------------------
st.subheader("⏱ Execution Time Analysis")

fig2 = px.box(
    df,
    y="execution_time",
    title="Execution Time Spread"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------------
# SPILL ANALYSIS
# -----------------------------------
st.subheader("💾 Spill to Disk Frequency")

spill_counts = df["spill_to_disk"].value_counts()

fig3 = px.pie(
    values=spill_counts.values,
    names=["No Spill", "Spill"],
    title="Disk Spill Occurrence"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------------
# ANOMALY TREND
# -----------------------------------
st.subheader("🚨 Anomaly Detection Trend")

# simulated trend
trend = np.random.randint(0, 5, 15)

fig4 = px.line(
    y=trend,
    title="Anomalies Detected Over Time"
)

st.plotly_chart(fig4, use_container_width=True)

# -----------------------------------
# QUERY LOAD TREND
# -----------------------------------
st.subheader("📈 Query Load Trend")

load = np.random.randint(50, 100, 20)

fig5 = px.area(
    y=load,
    title="Warehouse Load Over Time"
)

st.plotly_chart(fig5, use_container_width=True)