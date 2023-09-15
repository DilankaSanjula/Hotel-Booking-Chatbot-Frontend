import streamlit as st
import requests
import time


class Metrics:
    """
    Handles response time metric
    """
    def __init__(self):
        self.total_queries = 0
        self.total_response_time = 0

    def metrics_avg_response_time(self, query_start_time):
        query_end_time = time.time()
        query_response_time = query_end_time - query_start_time
      
        return query_response_time 

metrics = Metrics()

api_url = "http://44.208.57.126:5005/webhooks/rest/webhook"

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

    query_start_time = time.time()

    # User message added to the list of messages in session state
    with st.chat_message("user"):
        st.markdown(prompt)
  
    st.session_state.messages.append({"role": "user", "content": prompt})
    payload = {
        "message": prompt
    }
    
    #post request to rasa enable api. Chatbot connection
    response = requests.post(api_url, json=payload)
    chatbot_response = response.json()
    print(chatbot_response)
    
    #Handling multiple bot responses
    for responses in chatbot_response:
        bot = responses['text']
        response = f"ABC: {bot}"

        with st.chat_message("assistant"):
            st.markdown(response)
            
    # Side bar to display response time of each query
    response_time = metrics.metrics_avg_response_time(query_start_time)
    st.sidebar.subheader("Response Time")
    st.sidebar.write(f"{response_time:.2f} seconds")
        
    # Assistant message added to the list of messages
    st.session_state.messages.append({"role": "assistant", "content": response})
    