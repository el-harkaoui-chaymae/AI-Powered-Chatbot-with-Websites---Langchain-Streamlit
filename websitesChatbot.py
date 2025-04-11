
# Import packages

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

# App Configuration

st.set_page_config(page_title="websites chatbot" , page_icon="✨")

st.title("Intelligent Conversations with Websites")

# response generator 
def respond(user_text):
    return "this is your responses"

# add a sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

# add a prompt textarea
user_text = st.chat_input("Enter your text here")

with st.chat_message("⚡ AI assistant"):
    st.write("Hello! How can i help you ?")



# chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    



# messages interaction
if user_text is not None and user_text != "" :

    # add the user query to chat history
    st.session_state.chat_history.append(HumanMessage(content=user_text))

    response = respond(user_text)

    # add AI response to the chat history
    st.session_state.chat_history.append(AIMessage(content=response))

    with st.chat_message("👁️"):
        st.write(user_text)

    with st.chat_message("⚡ AI assistant"):
        st.write(response)
                             

with st.sidebar:
    st.write(st.session_state.chat_history)

    



# 23.01