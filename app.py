import streamlit as st
import pandas as pd
import time
import plotly.express as px
from styles.theme import apply_theme
from agent.impact_engine import calculate_impact
from agent.risk_engine import calculate_risk
from agent.anomaly_detector import detect_anomalies
from agent.optimizer import optimize_query
from agent.voice_alert import speak
from agent.stream_simulator import stream_queries

st.set_page_config(layout="wide")
theme_choice = st.sidebar.selectbox(
    "🎨 Select UI Theme",
    ["Neon Cyber", "Corporate", "Light", "Hacker"]
)

apply_theme(theme_choice)

st.title("🧠 DBIQ AI – Autonomous Snowflake Guardian")

# -------------------------------
# LOAD DATA (session based)
# -------------------------------
if "df" not in st.session_state:
    st.session_state.df = pd.read_csv("data/query_logs.csv")

df = st.session_state.df

# -------------------------------
# INITIALIZE LOG STATE
# -------------------------------
if "logs" not in st.session_state:
    st.session_state.logs = [
        "AI agent initialized...",
        "Monitoring Snowflake workload..."
    ]

# -------------------------------
# STREAMING CONTROL
# -------------------------------
colA, colB = st.columns(2)

if colA.button("📡 Start Live Workload Simulation"):
    st.session_state.streaming = True
    st.session_state.last_update = 0

if colB.button("⛔ Stop Simulation"):
    st.session_state.streaming = False

# Streaming engine
if "streaming" in st.session_state and st.session_state.streaming:
    st.info("📡 Live workload streaming ACTIVE")

    current_time = time.time()

    if "last_update" not in st.session_state:
        st.session_state.last_update = 0

    if current_time - st.session_state.last_update >= 2:
        df = stream_queries(df)
        st.session_state.df = df
        st.session_state.last_update = current_time

        # push AI thinking logs
        st.session_state.logs.append("New workload detected.")
        st.session_state.logs.append("Analyzing query pattern...")

        st.rerun()

# -------------------------------
# RISK + ANOMALY ENGINE
# -------------------------------
df["risk_score"] = df.apply(calculate_risk, axis=1)
df = detect_anomalies(df)

# -------------------------------
# DASHBOARD METRICS
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Active Queries", len(df))
col2.metric("High Risk Queries", len(df[df["risk_score"] > 70]))
col3.metric("Anomalies Detected", len(df[df["anomaly"] == -1]))

# -------------------------------
# SYSTEM STATUS BANNER
# -------------------------------
if df["risk_score"].max() > 70:
    st.error("🚨 CRITICAL WORKLOAD DETECTED")
elif df["risk_score"].max() > 40:
    st.warning("⚠ Elevated workload detected")
else:
    st.success("🟢 System Stable")

# -------------------------------
# LIVE QUERY TABLE
# -------------------------------
st.subheader("🚨 Live Query Monitor")
st.dataframe(df, use_container_width=True)

# -------------------------------
# QUERY SELECTION
# -------------------------------
selected_query = st.selectbox("Select Query", df["query_id"])
query_row = df[df["query_id"] == selected_query].iloc[0]

st.subheader("🧠 AI Diagnosis")

st.write(f"Risk Score: {query_row['risk_score']}")
st.write(f"Execution Time: {query_row['execution_time']}")
st.write(f"Bytes Scanned: {query_row['bytes_scanned']}")

# -------------------------------
# AI THINKING CONSOLE (Contextual)
# -------------------------------
if st.session_state.get("streaming", False) or st.session_state.get("show_logs", False):
    st.markdown("### 🧠 AI Thinking Console")
    st.code("\n".join(st.session_state.logs[-6:]))

# -------------------------------
# VOICE ALERT
# -------------------------------
if query_row["risk_score"] > 70:
    speak("Critical workload anomaly detected. Optimization recommended.")

# -------------------------------
# OPTIMIZE QUERY BUTTON
# -------------------------------
if st.button("🔍 Optimize Query"):

    st.session_state.show_logs = True
    st.session_state.logs.append("Optimization requested by user.")
    st.session_state.logs.append("Generating AI recommendation...")

    with st.spinner("🧠 AI analyzing workload patterns..."):
        time.sleep(1)
        result = optimize_query(query_row["query_text"])

    st.subheader("🤖 AI Response")

    output_area = st.empty()
    typed_text = ""

    # typing animation
    for char in result:
        typed_text += char
        output_area.markdown(typed_text)
        time.sleep(0.01)
        
    impact = calculate_impact(query_row)

    st.subheader("📊 Measured Impact")

    colA, colB, colC = st.columns(3)

    colA.metric("Execution Time Reduced (ms)", f"{int(impact['time_saved'])}")
    colB.metric("Data Scan Reduced (bytes)", f"{int(impact['bytes_reduced'])}")
    colC.metric("Estimated Cost Saved ($)", f"{round(impact['cost_saved'],2)}")

    if impact["block_prevented"]:
        st.success("🚫 Long-running query blockage prevented.")    

    st.session_state.logs.append("Optimization completed.")
    st.session_state.logs.append("Warehouse stabilized.")

    # -------------------------------
    # AUTO RESOLUTION ANIMATION
    # -------------------------------
    st.subheader("⚡ Auto-Resolution Simulation")

    risk = int(query_row["risk_score"])
    progress_bar = st.progress(risk)

    for i in range(risk, 20, -5):
        time.sleep(0.1)
        progress_bar.progress(i)

    st.success("✅ Warehouse Stabilized. Risk Reduced.")

# -------------------------------
# COST IMPACT VISUALIZATION
# -------------------------------
st.subheader("💰 Cost Optimization Impact")

before = [query_row["execution_time"], query_row["bytes_scanned"]]
after = [query_row["execution_time"] * 0.6, query_row["bytes_scanned"] * 0.5]

fig = px.bar(
    x=["Execution Time", "Bytes Scanned"],
    y=before,
    title="Before Optimization"
)
st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(
    x=["Execution Time", "Bytes Scanned"],
    y=after,
    title="After Optimization"
)
st.plotly_chart(fig2, use_container_width=True)