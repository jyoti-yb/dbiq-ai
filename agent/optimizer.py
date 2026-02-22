import requests
import streamlit as st


def optimize_query(query):

    api_key = st.secrets.get("GROQ_API_KEY")

    if not api_key:
        return "⚠ GROQ_API_KEY not configured in Streamlit secrets."

    prompt = f"""
You are a Snowflake database performance expert.

Analyze this SQL query:
{query}

Provide:
- performance problems
- optimized query
- explanation
- expected cost and performance impact
"""

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"⚠ Groq API error: {str(e)}"