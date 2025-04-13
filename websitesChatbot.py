
# Import packages

from langchain_text_splitters import TextSplitter
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter








# App Configuration

st.set_page_config(page_title="websites chatbot" , page_icon="✨")

st.title("Intelligent Conversations with Websites")




# response generator 
def respond(user_text):
    return "this is your responses"



# get text from website in document form
def get_vectorstore_from_url(url):
    loader = WebBaseLoader(url)
    document = loader.load()
    # split the doc into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    return document_chunks



# chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    




# add a sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

# the url must be given
if website_url is None or website_url == "" :
    st.info("Please enter a website URL")

else : 
   
   # extracting the all HTML text from the page
   document_chunks = get_vectorstore_from_url(website_url)
   with st.sidebar:
       st.write(document_chunks)

   # add a prompt textarea
   user_text = st.chat_input("Enter your text here")

   with st.chat_message("⚡ AI assistant"):
     st.write("Hello! How can i help you ?")



   # messages interaction
   if user_text is not None and user_text != "" :

      # add the user query to chat history
      st.session_state.chat_history.append(HumanMessage(content=user_text))

      # add AI response to the chat history
      response = respond(user_text)
      st.session_state.chat_history.append(AIMessage(content=response))

    

   

   # conversation
   for message in st.session_state.chat_history:
      if isinstance(message,AIMessage):
          with st.chat_message("⚡ AI assistant"):
              st.write(message.content)
      elif isinstance(message,HumanMessage):
          with st.chat_message("👁️ You"):
              st.write(message.content)        



    






    



# 23.01