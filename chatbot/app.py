from langchain_openai import ChatOpenAI #LLM wrapper for openAI
from langchain_core.prompts import ChatPromptTemplate #Prompt template for chat models
from langchain_core.output_parsers import StrOutputParser #Output parser to convert the output to string
from openai import RateLimitError

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "default")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    try:
        st.write(chain.invoke({'question':input_text}))
    except RateLimitError:
        st.error("OpenAI quota reached. Check your OpenAI billing and API usage, or add credits to your account.")
