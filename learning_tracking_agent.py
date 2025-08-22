import google.generativeai as genai

class LearningTrackingAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-flash')  # or use another model from your list

    def generate_question(self, topic):
        # Normalize topic if input is generic
        if topic.lower() in ["quiz", "take a quiz", "give me a quiz"]:
            topic = "supervised learning in AI"

        prompt = f"""
Generate a multiple-choice question on the topic: {topic}

Format:
Question: <question>
A) <option 1>
B) <option 2>
C) <option 3>
D) <option 4>
Answer: <correct option letter>
"""
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating question: {e}"

    def evaluate_answer(self, question, answer):
        prompt = f"Evaluate this answer to the question '{question}': {answer}"
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error evaluating answer: {e}"

    def create_summary(self, topic, performance):
        prompt = f"Create a learning summary for {topic} based on this performance: {performance}"
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error creating summary: {e}"
