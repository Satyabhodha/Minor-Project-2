import google.generativeai as genai

genai.configure(api_key="AIzaSyCW8RPqqP4utfo0r4T5kKmBY810QrsY_bk")

models = genai.list_models()

for m in models:
    print(f"Model name: {m.name} | Support generate_content: {'generateContent' in m.supported_generation_methods}")
# API_KEY = "AIzaSyCW8RPqqP4utfo0r4T5kKmBY810QrsY_bk"