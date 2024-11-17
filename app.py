from flask import Flask, request, jsonify, render_template
from agent import QA_Agent

# Read the paragraph from the text file
with open("financial_services.txt", "r") as file:
    paragraph = file.read()

# Initialize the Flask app and QA agent
app = Flask(__name__)
agent = QA_Agent(paragraph)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    if question:
        answer = agent.answer_question(question)
        return jsonify({"answer": answer})
    return jsonify({"error": "Please provide a question"}), 400

if __name__ == '__main__':
    app.run(debug=True)
