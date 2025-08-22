import google.generativeai as genai

genai.configure(api_key="AIzaSyCXjHgc6o4-COKQsPULlK37dk8RJG4rZFk")

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Which agent handles questions about programming concepts?")
print(response.text.strip())
# API_KEY = "AIzaSyCW8RPqqP4utfo0r4T5kKmBY810QrsY_bk"