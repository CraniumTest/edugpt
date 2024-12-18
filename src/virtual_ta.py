from transformers import pipeline

class VirtualTeachingAssistant:
    def __init__(self):
        self.explain_pipeline = pipeline("text-generation")

    def explain_topic(self, topic):
        # Placeholder prompt for explanation. Ideally, more context or curriculum guidelines should be integrated.
        prompt = f"Explain the topic: {topic} in a simple manner."
        result = self.explain_pipeline(prompt, max_length=100)
        return result[0]['generated_text']
