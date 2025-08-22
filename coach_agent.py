import google.generativeai as genai

class CoachAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-1.5-flash")



    def explain_course(self, topic, student_info):
        prompt = f"Explain the topic '{topic}' in a way suitable for the student: {student_info}"
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error: {e}"
