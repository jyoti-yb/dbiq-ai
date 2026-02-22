#  Snowflake Performance AI Agent

AI-powered system to monitor, diagnose, optimize, and autonomously improve Snowflake query performance in real time.
Deployed : https://dbiq-ai-y7qbuxzhendv4rekwjezy5.streamlit.app/

---

## 🚀 What is DBIQ AI?

DBIQ AI is an intelligent assistant that:

- monitors Snowflake workloads  
- detects inefficient queries  
- predicts performance risks  
- optimizes queries using AI  
- measures cost & performance impact  
- simulates autonomous warehouse stabilization  

It transforms Snowflake operations from **manual DBA-driven monitoring → AI-driven optimization.**

---

## 🎯 Problem We Solve

Organizations using Snowflake face:

- slow queries  
- disk spills  
- warehouse blocking  
- rising compute costs  
- heavy DBA dependency  

There is no automation layer to detect and fix issues proactively.

DBIQ AI fills that gap.

---

## 🧩 Key Features

### 🧭 Real-Time Monitoring
### 🧠 AI Query Optimization
### 💰 Business Impact Dashboard  
### 📊 Analytics & Observability
### 🤖 Autonomous AI Mode
---

## 🏗 Architecture Overview


Components:

- **Risk Engine** → scores queries based on performance signals  
- **Anomaly Detector** → identifies abnormal workloads  
- **AI Optimizer** → suggests optimized SQL  
- **Impact Engine** → calculates savings & improvements  
- **Analytics Layer** → observability + trends  

---

## 🖥 Application Pages

### 1️⃣ Monitoring
Real-time workload, risk detection, anomalies.

### 2️⃣ Optimization
AI-powered query improvement and auto-resolution simulation.

### 3️⃣ Impact
Business ROI: cost savings, compute reduction, performance gains.

### 4️⃣ Analytics
Observability dashboards, trends, and system health.

### 5️⃣ Autonomous AI
Self-healing simulation and auto-optimization logic.

---

## 🛠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Plotly  
- **AI Engine:** LLM API (Groq / Llama models)  
- **Architecture:** Modular agent-based system  

---

## 📦 Project Structure
dbiq-ai/
│
├── app.py
├── pages/
│ ├── Optimization.py
│ ├── Impact.py
│ ├── Analytics.py
│ ├── Autonomous_AI.py
│
├── agent/
│ ├── risk_engine.py
│ ├── anomaly_detector.py
│ ├── optimizer.py
│ ├── impact_engine.py
│
├── data/
│ └── query_logs.csv
│
├── styles/
├── requirements.txt
└── README.md


---

## ⚙️ Setup & Run Locally

### 1. Clone repo

### 2. Install dependencies

### 3. Run app


---

## 🔐 Environment Setup (LLM API)

Add Groq API key in Streamlit secrets:


