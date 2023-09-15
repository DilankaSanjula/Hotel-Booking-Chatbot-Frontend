import streamlit as st
import requests

api_url = "http://localhost:5005/webhooks/rest/webhook"

# Check for existing messages in the session state and initialize if not found
if "messages" not in st.session_state:
    print("no messages")
    x=st.session_state.messages = []
    print(x)

#Title
st.title("ABC Hotel Chatbot")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Display existing chat messages
if prompt := st.chat_input():
    # User message added to the list of messages in session state
    with st.chat_message("user"):
        st.markdown(prompt)
  
    st.session_state.messages.append({"role": "user", "content": prompt})
    payload = {
        "message": prompt
    }

    response = requests.post(api_url, json=payload)
    chatbot_response = response.json()
    print(chatbot_response)
    
    #Handling multiple bot responses
    for responses in chatbot_response:
        print(responses['text'])
        bot = responses['text']
        response = f"ABC: {bot}"

        with st.chat_message("assistant"):
            st.markdown(response)

        # Assistant message added to the list of messages
        st.session_state.messages.append({"role": "assistant", "content": response})