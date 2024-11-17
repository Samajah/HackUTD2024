
# PoyoBot - Financial Advisor Chatbot

PoyoBot is an intelligent financial advisor chatbot designed to help users with various financial topics, including investment strategies, retirement planning, budgeting, and more. Built using Streamlit and FastAPI, PoyoBot answers questions using a pre-trained language model and a custom knowledge base.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

PoyoBot provides users with personalized financial insights by answering questions based on a knowledge base. The bot is designed to handle diverse financial inquiries and assist users in making informed financial decisions. 

## Features

- Answers predefined financial questions and dynamically responds to custom queries using FastAPI.
- Provides users with insights into investment strategies, credit management, retirement planning, and more.
- Interactive chat interface built with Streamlit.

## Installation

To set up and run PoyoBot locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/PoyoBot.git
   cd PoyoBot
   ```

2. **Install dependencies**:
   Make sure you have Python 3.11.7 installed, then install the required libraries.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the knowledge base**:
   Ensure you have a `knowledge_base.txt` file with relevant financial information.

4. **Run FastAPI Server**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Run Streamlit App**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Start a new chat in the Streamlit app interface and type your questions.
2. The bot will respond based on either predefined answers or by calling the FastAPI server to generate an answer.
3. View and manage previous chat histories in the sidebar.

## Project Structure

```plaintext
PoyoBot/
├── app.py               # Front-end Streamlit app
├── main.py              # FastAPI backend for question answering
├── knowledge_base.txt   # Knowledge base for answering questions
├── requirements.txt     # Required libraries and dependencies
├── mascot.png       # Mascot image used in the chat interface
└── README.md            # Project documentation
```

## Dependencies

This project requires the following libraries:

- **Python**: 3.11.7
- **Streamlit**: for the chat interface
- **FastAPI**: for the backend server
- **Transformers**: for the question-answering model
- **Requests**: to fetch responses from the FastAPI server

Install the required libraries with the command:
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```plaintext
streamlit==1.10.0
fastapi==0.95.2
transformers==4.32.0
requests==2.31.0
uvicorn==0.20.0
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add a new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.


