from transformers import pipeline

class QA_Agent:
    def __init__(self, paragraph):

        self.paragraph = paragraph
        # Load question-answering pipeline model
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def answer_question(self, question):

        system_prompt = "Answer the following question based solely on the provided information about financial services. Use only facts from the text, and answer in full sentences."
        full_prompt = f"{system_prompt} {question}"

        # Use the pipeline to answer the question based on the provided paragraph
        response = self.qa_pipeline(question=question, context=self.paragraph)
        return response["answer"]
