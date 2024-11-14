from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
os.environ['LANGCHAIN_ENDPOINT'] = os.getenv('LANGCHAIN_ENDPOINT')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

llm = ChatGroq(
  model_name="llama3-8b-8192",
  temperature=0.2,
  max_tokens=1024,
)

prompt = ChatPromptTemplate([
  ('system', 'You are a helpful assistant who answers questions asked in a simple way which a kid can also understand'),
  ('human', '{input}')
])

chain = prompt|llm|StrOutputParser()
st.set_page_config(page_title="Q&A Chatbot")
st.title("Q&A Chatbot")
input = st.text_input("Ask a question", key="input")
response = chain.invoke(input=input)
st.write(response)