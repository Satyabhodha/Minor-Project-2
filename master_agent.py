class MasterAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def process_query(self, query):
        query_lower = query.lower()

        if "quiz" in query_lower:
            if "supervised" in query_lower:
                return "LearningTrackingAgent:supervised learning"
            elif "ai" in query_lower:
                return "LearningTrackingAgent:artificial intelligence"
            else:
                return "LearningTrackingAgent:Python basics"

        if "track" in query_lower or "progress" in query_lower:
            return "LearningTrackingAgent"

        if "roadmap" in query_lower or "what to study" in query_lower:
            return "RoadmapAgent"

        if "coach" in query_lower or "motivate" in query_lower:
            return "CoachAgent"

        if "tutor" in query_lower or "explain" in query_lower:
            return "TutorAgent"

        return "Unknown"
