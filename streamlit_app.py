import streamlit as st

#Title
st.title("ABC Hotel Chatbot")

# Check for existing messages in the session state and initialize if not found
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Display existing chat messages
if prompt := st.chat_input():
    # Add the user's message to the list of messages in session state
    with st.chat_message("user"):
        st.markdown(prompt)
  
    st.session_state.messages.append({"role": "user", "content": prompt})

# Generate a response (currently a template) and display it in the chat interface
    response = f"ABC: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)
        
    # Add the assistant's response to the list of messages in session state
    st.session_state.messages.append({"role": "assistant", "content": response})