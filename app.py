from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated chatbot response function
def get_chatbot_response(prompt):
    # Here you can integrate your chatbot logic
    return f"Chatbot: You said '{prompt}'"

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = get_chatbot_response(prompt)  # Get the chatbot's response

    return render_template('home.html', response=response)

@app.route('/page1')
def page1():
    return render_template('page1.html', title="Page 1")

@app.route('/page2')
def page2():
    return render_template('page2.html', title="Page 2")

@app.route('/page3')
def page3():
    return render_template('page3.html', title="Page 3")

@app.route('/process_prompt', methods=['POST'])
def process_prompt():
    # Get the user input from the form
    prompt = request.form['prompt']
    
    # Process the input (e.g., use it for a chatbot response or other logic)
    print(f"User Prompt: {prompt}")  # This can be logged or used elsewhere

    # Redirect back to the home page (or render a response)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
