import google.genai as genai

client = genai.Client(api_key="AIzaSyDzEzJykLiDgy3yRafDJ_qc8ZSi5boM5p8")

response = client.models.generate_content(
    model="gemini-1.0-pro",
    contents="Say hello"
)

print(response.text)