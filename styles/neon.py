def apply():
    import streamlit as st
    st.markdown("""
    <style>
    html, body { background:#0b0f1a; color:#e0e6ff; }
    h1 { color:#00f7ff; text-shadow:0 0 10px #00f7ff; }
    [data-testid="stMetric"] {
        background:#111827; border:1px solid #00f7ff;
        border-radius:10px; box-shadow:0 0 10px #00f7ff33;
    }
    </style>
    """, unsafe_allow_html=True)