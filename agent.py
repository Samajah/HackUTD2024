from transformers import pipeline

class QA_Agent:
    def __init__(self, paragraph):
        self.paragraph = paragraph
        self.qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

    def answer_question(self, question):
        # Use a system prompt to instruct the agent to answer in full sentences
        system_prompt = "Answer the following question based on the provided information about the internet's history and impact. Respond in full sentences, providing context when necessary. "
        full_prompt = f"{system_prompt} {question}"
        
        response = self.qa_pipeline(question=full_prompt, context=self.paragraph)
        
        # Format the answer in full sentences if needed
        answer = response["answer"]
        return answer
