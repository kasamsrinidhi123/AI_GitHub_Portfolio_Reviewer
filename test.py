import google.generativeai as genai

API_KEY = "YOUR_API_KEY"

print(API_KEY[:15])
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Say hello")

print(response.text)


