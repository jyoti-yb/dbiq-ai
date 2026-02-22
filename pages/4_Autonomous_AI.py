import streamlit as st
import pandas as pd
import time
import plotly.express as px

from agent.risk_engine import calculate_risk
from agent.anomaly_detector import detect_anomalies
from agent.optimizer import optimize_query
from agent.impact_engine import calculate_impact

st.set_page_config(layout="wide", page_title="Autonomous AI")

st.title("🤖 Autonomous AI – Self-Healing Snowflake")

# -----------------------------------
# LOAD DATA
# -----------------------------------
if "df" in st.session_state:
    df = st.session_state.df
else:
    df = pd.read_csv("data/query_logs.csv")
    st.session_state.df = df

# Ensure computed fields exist
if "risk_score" not in df.columns:
    df["risk_score"] = df.apply(calculate_risk, axis=1)

if "anomaly" not in df.columns:
    df = detect_anomalies(df)

# -----------------------------------
# AUTONOMOUS MODE TOGGLE
# -----------------------------------
autonomous_mode = st.toggle("🧠 Enable Autonomous Optimization")

if "ai_logs" not in st.session_state:
    st.session_state.ai_logs = []

if "total_auto_saved" not in st.session_state:
    st.session_state.total_auto_saved = 0

# -----------------------------------
# DETECT HIGH RISK
# -----------------------------------
high_risk_df = df[df["risk_score"] > 70]

st.subheader("🚨 High Risk Queries")

st.dataframe(high_risk_df, use_container_width=True)

# -----------------------------------
# AUTONOMOUS EXECUTION
# -----------------------------------
if autonomous_mode and not high_risk_df.empty:

    st.subheader("⚡ AI Auto-Optimization in Progress")

    for _, row in high_risk_df.iterrows():

        st.session_state.ai_logs.append(
            f"Detected high-risk query {row['query_id']} (Risk: {row['risk_score']})"
        )

        # Simulate optimization
        result = optimize_query(row["query_text"])

        impact = calculate_impact(row)

        st.session_state.total_auto_saved += impact["cost_saved"]

        st.session_state.ai_logs.append(
            f"Optimized query {row['query_id']} | Cost Saved: ${round(impact['cost_saved'],2)}"
        )

        time.sleep(0.5)

    st.success("✅ Autonomous AI completed optimization cycle.")

# -----------------------------------
# DECISION LOG
# -----------------------------------
st.subheader("🧠 AI Decision Log")

st.code("\n".join(st.session_state.ai_logs[-10:]))

# -----------------------------------
# CUMULATIVE SAVINGS
# -----------------------------------
st.subheader("💰 Autonomous Savings")

st.metric(
    "Total Cost Saved (Autonomous Mode)",
    f"${round(st.session_state.total_auto_saved,2)}"
)

# -----------------------------------
# SELF-HEALING SIMULATION
# -----------------------------------
st.subheader("📉 Warehouse Load After AI Intervention")

import numpy as np

before = np.random.randint(75, 95, 20)
after = before - np.random.randint(15, 30, 20)

fig1 = px.line(y=before, title="Before AI Intervention")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(y=after, title="After AI Self-Healing")
st.plotly_chart(fig2, use_container_width=True)