import streamlit as st

# with st.chat_message("user"):
#     st.write("Hello from ABC Hotels , How can I help you?")

# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "Hello from ABC Hotels , How can I help you?"}]

chat_history = []

# Create a Streamlit text input widget for user messages
user_message = st.text_input("User's Message", "")

# Function to simulate the bot's response
def bot_response(user_message):
    user_message = "test response from bot"
    return f"Bot: {user_message}"

# Handle user input and bot responses
if st.button("Send"):
    if user_message:
        chat_history.append(f"User: {user_message}")
        bot_reply = bot_response(user_message)
        chat_history.append(bot_reply)
        user_message = ""

# Display the chat history
st.title("ABC Hotel Chat UI")
for message in chat_history:
    st.write(message)