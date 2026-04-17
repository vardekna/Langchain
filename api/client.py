import requests
import streamlit as st

def post_and_parse(url, payload):
    response = requests.post(url, json=payload)
    response.raise_for_status()

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        raise ValueError(f"Server returned non-JSON response: {response.text}")

def extract_output(data):
    output = data.get("output")

    if isinstance(output, dict):
        return output.get("content", output)

    return output

#Function to get response from Ollama API
def get_ollama_response(input_text):
    data = post_and_parse(
        "http://localhost:8000/essay/invoke",
        {'input': {'topic': input_text}},
    )

    return extract_output(data)

#Function to get response from Ollama API
def get_ollama_response2(input_text):
    data = post_and_parse(
        "http://localhost:8000/poem/invoke",
        {'input': {'topic': input_text}},
    )

    return extract_output(data)

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    try:
        st.write(get_ollama_response(input_text))
    except Exception as exc:
        st.error(str(exc))

if input_text1:
    try:
        st.write(get_ollama_response2(input_text1))
    except Exception as exc:
        st.error(str(exc))
