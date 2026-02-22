import requests

def call_local_llm(prompt):

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        return response.json()["response"]

    except Exception as e:
        return f"Local LLM error: {str(e)}"