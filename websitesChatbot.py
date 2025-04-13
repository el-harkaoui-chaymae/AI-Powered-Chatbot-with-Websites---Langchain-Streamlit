
# Import packages

from langchain_text_splitters import TextSplitter
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings





# App Configuration

st.set_page_config(page_title="websites chatbot" , page_icon="✨")

st.title("Intelligent Conversations with Websites")




# response generator 
def respond(user_text):
    return "this is your responses"



# Storing
def get_vectorstore_from_url(url):
    
    # get text from website in document form
    loader = WebBaseLoader(url)
    document = loader.load()
    
    # split the doc into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # use the chunks to create a vectorstore
    # vector_store = Chroma.from_documents(document_chunks,OpenAIEmbeddings())

    # Use Hugging Face embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = Chroma.from_documents(document_chunks, embeddings, persist_directory=None)

    return vector_store



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
   
   # vector store
   vector_store = get_vectorstore_from_url(website_url)
 

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