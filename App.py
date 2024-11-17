import streamlit as st
import requests

st.markdown("""
    <style>
        .stApp {
            background-color: #54DDE8;
        }

        .fixed-title {
            position: fixed;
            top: 60px;  /* Adjust this value based on the height of the navbar */
            left: 0;
            width: 100%;
            background-color: #40B7BA;
            text-align: center;
            color:  #F7CE79;
            padding: 15px;
            font-size: 30px;
            font-weight: bold;
            z-index: 1000;
            display: flex;
            justify-content: center;  /* Center content horizontally */
            align-items: center;      /* Center content vertically */
        }

        .chat-container {
            display: flex;
            flex-direction: column;
            margin: 10px;
            margin-top: 80px;  /* Adjust to give space for fixed title */
        }
        .user-message {
            display: flex;
            justify-content: flex-end;
            margin-bottom: 10px;
        }
        .ai-message {
            display: flex;
            justify-content: flex-start;
            margin-bottom: 10px;
            align-items: center;
        }
        .message-bubble {
            max-width: 70%;
            padding: 10px;
            border-radius: 10px;
            word-wrap: break-word;
        }
        .user-bubble {
            background-color:#163950;
            color: white;
            border: none;
        }
        .ai-bubble {
            background-color: white;
            color: black;
            border: none;
            display: flex;
            align-items: center;
        }
        .ai-bubble img {
            margin-right: 10px;  /* Space between image and text */
            border-radius: 50%; /* Round image */
            width: 30px;
            height: 30px;
        }
        .sidebar-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='fixed-title'><h1>PoyoBot</h1></div>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; color: #163950;'>PoyoBot</h1>", unsafe_allow_html=True) 

# Define predefined questions and answers
predefined_qa = {
    "What are the main differences between a traditional savings account and a money market account?": 
        "A savings account is a basic, low-risk account that typically offers a lower interest rate. It’s ideal for emergency funds or short-term savings. You can make deposits and withdrawals, but there may be limits on the number of transactions. A money market account, on the other hand, usually offers a higher interest rate compared to a savings account. It may also provide limited check-writing capabilities and often requires a higher minimum balance to avoid fees. It’s a good option for those who want to earn more interest but still need liquidity for short-term goals.",
    
    "How can I reduce my tax burden while investing for retirement?": 
        "There are a few strategies to reduce your tax burden when saving for retirement: " +
            "Contribute to tax-deferred retirement accounts like a 401(k) or IRA. Contributions to these accounts are typically tax-deductible, lowering your taxable income for the year you contribute. Consider Roth IRAs: Although Roth contributions are made after-tax, qualified withdrawals during retirement are tax-free. Maximize employer contributions: If your employer offers a 401(k) match, try to contribute enough to take full advantage of the match—this is essentially free money. Tax-efficient investing: Use index funds or ETFs that generally incur fewer taxable events than actively managed funds.",
    
    "What’s the benefit of diversifying my investment portfolio?": 
        "Diversifying your portfolio means spreading investments across various asset classes (stocks, bonds, real estate, commodities, etc.) to reduce the overall risk. The primary benefit of diversification is that it helps protect your portfolio from significant losses in any single investment. For example, if the stock market declines, bonds or other assets may perform better, helping to offset those losses. It’s important for long-term investors because it can smooth out the returns and reduce the volatility of your portfolio.",
    
    "Should I consider investing in real estate as part of my portfolio?": 
        "Real estate can be a valuable component of a diversified portfolio, especially for long-term investors. "+
        "It offers potential for capital appreciation (property value increases) and income generation (rental income). "+
        "Real estate also tends to have a low correlation with stocks and bonds, which can help reduce overall portfolio volatility. "+
        "However, real estate also involves risks, such as market fluctuations and property maintenance costs. "+
        "If you're not ready to buy physical properties, you can consider investing in REITs (Real Estate Investment Trusts), "+
        "which provide exposure to real estate markets without owning physical property.",
    
    "How can I start investing if I have limited funds?": 
        "Even with limited funds, there are several ways to start investing: Start with low-cost index funds or ETFs: These funds offer broad market exposure with low fees, making them ideal for beginners with smaller amounts to invest. Use a robo-advisor: These automated platforms create and manage a diversified portfolio based on your risk tolerance and goals. Many robo-advisors have low minimum investment requirements. Contribute to retirement accounts: Even small, regular contributions to a 401(k) or IRA can compound over time, benefiting from tax advantages. Consider fractional shares: Some platforms allow you to buy fractional shares of stocks or ETFs, making it possible to invest in high-priced stocks without needing large amounts of capital. These questions and answers cover key concepts about savings, tax strategies, investment diversification, and ways to get started in investing, all of which a financial advisor would typically discuss with clients."
}

# Initialize chat history and chat names
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_names" not in st.session_state:
    st.session_state.chat_names = []
if "current_chat" not in st.session_state:
    st.session_state.current_chat = 0

# Function to delete chat history
def delete_chat(index):
    del st.session_state.messages[index]
    del st.session_state.chat_names[index]
    if len(st.session_state.messages) == 0:
        start_new_chat()
    else:
        st.session_state.current_chat = min(st.session_state.current_chat, len(st.session_state.messages) - 1)

# Function to start a new chat
def start_new_chat():
    st.session_state.current_chat = len(st.session_state.messages)
    st.session_state.messages.append([])
    st.session_state.chat_names.append("New Chat")

# Sidebar for chat management
with st.sidebar:
    st.header("Menu")
    if st.button("New Chat"):
        start_new_chat()

    st.write("Chat History")
    for i, chat_name in enumerate(st.session_state.chat_names):
        chat_container = st.columns([4, 1])
        with chat_container[0]:
            if st.button(chat_name, key=f"chat_{i}"):
                st.session_state.current_chat = i
        with chat_container[1]:
            if st.button("🗑️", key=f"delete_{i}", help="Delete Chat", on_click=delete_chat, args=(i,)):
                st.rerun()

# Ensure there is at least one chat
if len(st.session_state.messages) == 0:
    start_new_chat()

# Display chat messages from history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.messages[st.session_state.current_chat]:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="user-message">
            <div class="message-bubble user-bubble">
                {message["content"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="ai-message">
            <div class="message-bubble ai-bubble">
            <img src="https://ripple.hackutd.co/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmascot-moving.29641068.gif&w=3840&q=75" alt="Mascot" style="width: 150px; height: 100px; border-radius: 50%;" />
            {message["content"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input field for user question in chat format
if st.session_state.current_chat != -1 and (question := st.chat_input("Enter your question here:")):
    st.session_state.messages[st.session_state.current_chat].append({"role": "user", "content": question})
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="user-message">
        <div class="message-bubble user-bubble">
            {question}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Rename chat based on the first question
    if st.session_state.chat_names[st.session_state.current_chat] == "New Chat":
        st.session_state.chat_names[st.session_state.current_chat] = question[:30] + "..."

    # Check if the question matches a predefined one
    if question in predefined_qa:
        answer = predefined_qa[question]
    else:
        # Fallback to FastAPI if no match is found
        try:
            response = requests.get('http://localhost:8000/answer/', params={"question": question})
            response.raise_for_status()  # Raise an error for bad HTTP responses (e.g., 404 or 500)
            answer = response.json().get('answer', 'No answer received')
        except requests.exceptions.RequestException as e:
            answer = f"Error: {e}"

    st.session_state.messages[st.session_state.current_chat].append({"role": "assistant", "content": answer})
    st.markdown(f"""
    <div class="ai-message">
        <div class="message-bubble ai-bubble">
            <img src="https://ripple.hackutd.co/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmascot-moving.29641068.gif&w=3840&q=75" alt="Mascot" style="width: 150px; height: 100px; border-radius: 70%;" />
            {answer}
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
