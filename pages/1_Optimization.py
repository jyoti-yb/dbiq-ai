import streamlit as st
import pandas as pd
import time

from agent.risk_engine import calculate_risk
from agent.anomaly_detector import detect_anomalies
from agent.optimizer import optimize_query
from agent.impact_engine import calculate_impact

st.set_page_config(layout="wide", page_title="AI Optimization")

st.title("🧠 AI Query Optimization Engine")

# -----------------------------------
# LOAD DATA
# -----------------------------------
if "df" in st.session_state:
    df = st.session_state.df
else:
    df = pd.read_csv("data/query_logs.csv")
    st.session_state.df = df

# ensure computed fields
if "risk_score" not in df.columns:
    df["risk_score"] = df.apply(calculate_risk, axis=1)

if "anomaly" not in df.columns:
    df = detect_anomalies(df)

# -----------------------------------
# SELECT QUERY
# -----------------------------------
st.subheader("🔍 Select Query for Optimization")

selected_query = st.selectbox("Query ID", df["query_id"])
query_row = df[df["query_id"] == selected_query].iloc[0]

st.write("### Query Details")
st.write(f"Risk Score: {query_row['risk_score']}")
st.write(f"Execution Time: {query_row['execution_time']}")
st.write(f"Bytes Scanned: {query_row['bytes_scanned']}")

# -----------------------------------
# ORIGINAL SQL
# -----------------------------------
st.subheader("📜 Original Query")
st.code(query_row["query_text"], language="sql")

# -----------------------------------
# OPTIMIZE BUTTON
# -----------------------------------
if st.button("⚡ Optimize Query with AI"):

    with st.spinner("AI analyzing query..."):
        time.sleep(1)
        optimized_sql = optimize_query(query_row["query_text"])

    # -----------------------------------
    # SHOW OPTIMIZED SQL
    # -----------------------------------
    st.subheader("🤖 Optimized Query Suggestion")
    st.code(optimized_sql, language="sql")

    # -----------------------------------
    # IMPACT CALCULATION
    # -----------------------------------
    impact = calculate_impact(query_row)

    st.subheader("📊 Optimization Impact")

    col1, col2, col3 = st.columns(3)

    col1.metric("Execution Time Saved", f"{int(impact['time_saved'])} ms")
    col2.metric("Data Scan Reduced", f"{int(impact['bytes_reduced'])} bytes")
    col3.metric("Estimated Cost Saved", f"${round(impact['cost_saved'],2)}")

    if impact["block_prevented"]:
        st.success("🚫 Potential query blockage prevented")

    # -----------------------------------
    # AUTO RESOLUTION SIMULATION
    # -----------------------------------
    st.subheader("⚡ Warehouse Stabilization")

    progress = st.progress(100)

    for i in range(100, 30, -10):
        time.sleep(0.1)
        progress.progress(i)

    st.success("Warehouse stabilized after AI optimization.")