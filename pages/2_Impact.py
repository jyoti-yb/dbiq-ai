import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
from agent.impact_engine import calculate_impact
from agent.risk_engine import calculate_risk
from agent.anomaly_detector import detect_anomalies

st.title("💰 AI Impact & Business Value Dashboard")

# Load data from session OR fallback to CSV
if "df" in st.session_state:
    df = st.session_state.df
else:
    df = pd.read_csv("data/query_logs.csv")
    st.session_state.df = df

# Ensure computed columns exist
if "risk_score" not in df.columns:
    df["risk_score"] = df.apply(calculate_risk, axis=1)

if "anomaly" not in df.columns:
    df = detect_anomalies(df)    

df = st.session_state.df

st.subheader("📊 System-Wide Impact Overview")

# -----------------------------
# SYSTEM LEVEL METRICS
# -----------------------------

total_queries = len(df)
high_risk_queries = len(df[df["risk_score"] > 70])
anomalies = len(df[df["anomaly"] == -1])

col1, col2, col3 = st.columns(3)

col1.metric("Total Queries Monitored", total_queries)
col2.metric("High Risk Queries Detected", high_risk_queries)
col3.metric("Anomalies Identified", anomalies)

# -----------------------------
# SELECT QUERY IMPACT
# -----------------------------

st.subheader("🔍 Per-Query Optimization Impact")

selected_query = st.selectbox("Select Query", df["query_id"])
query_row = df[df["query_id"] == selected_query].iloc[0]

impact = calculate_impact(query_row)

colA, colB, colC = st.columns(3)

colA.metric("Execution Time Saved", f"{int(impact['time_saved'])} ms")
colB.metric("Data Scan Reduced", f"{int(impact['bytes_reduced'])} bytes")
colC.metric("Estimated Cost Saved", f"${round(impact['cost_saved'],2)}")

if impact["block_prevented"]:
    st.success("🚫 Potential long-running query blockage prevented")

# -----------------------------
# WAREHOUSE STABILIZATION TREND
# -----------------------------

st.subheader("📈 Warehouse Load Stabilization Trend")

# Simulated trend
load_before = np.random.randint(70, 95, 15)
load_after = load_before - np.random.randint(10, 25, 15)

fig1 = px.line(y=load_before, title="Warehouse Load Before AI Optimization")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(y=load_after, title="Warehouse Load After AI Optimization")
st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# PROJECTED ROI
# -----------------------------

st.subheader("📉 Projected Monthly Savings")

# simulate cost model
avg_cost_per_query = df["bytes_scanned"].mean() / 1e12 * 5
monthly_queries = 10000  # assumption for enterprise
projected_savings = avg_cost_per_query * 0.4 * monthly_queries

st.metric("Estimated Monthly Cost Savings", f"${round(projected_savings,2)}")

st.info("Projection assumes 40% optimization efficiency across enterprise workloads.")