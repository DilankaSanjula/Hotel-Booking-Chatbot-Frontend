import streamlit as st
import requests
import time


class Metrics:
    """
    Handles metrics
    """

    def __init__(self):
        self.total_queries = 0
        self.total_response_time = 0

    def metrics_avg_response_time(self, query_start_time):
        query_end_time = time.time()
        query_response_time = query_end_time - query_start_time
        self.total_queries += 1
        self.total_response_time += query_response_time
        return self.total_response_time, self.total_queries 


metrics = Metrics()

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

    query_start_time = time.time()

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
            
    total_response_time, total_queries  = metrics.metrics_avg_response_time(query_start_time)
    if total_queries > 0:
        average_response_time = total_response_time / total_queries
        st.sidebar.subheader("Total Number of Queries Handled")
        st.sidebar.write(f"{str(total_queries)}")
        st.sidebar.subheader("Average Response Time")
        st.sidebar.write(f"{average_response_time:.2f} seconds")
        
    else:
        st.sidebar.write("No queries yet.")
        
    # Assistant message added to the list of messages
    st.session_state.messages.append({"role": "assistant", "content": response})
    