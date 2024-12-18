from transformers import pipeline

class QASystem:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering")

    def answer_question(self, question):
        # Placeholder context, this would ideally be dynamic or pulled from a database.
        context = "EduGPT uses large language models to provide educational answers to various queries."
        result = self.qa_pipeline(question=question, context=context)
        return result['answer']
