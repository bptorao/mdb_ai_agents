import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import streamlit as st
import json
import ollama

MODEL_GPT = 'gpt-4o-mini'

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

# Haz que Llama 3.2 responda
#OLLAMA_SERVER = "http://localhost:11434"
OLLAMA_SERVER = "http://host.docker.internal:11434"
OLLAMA_API = f"{OLLAMA_SERVER}/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL_LLAMA = 'llama3.2'



system_prompt = "Eres un asistente de código que explica el código introducido por el usuario.\
Identifica el lenguaje, proporciona una descripcion del código y explica.\
Si es posible proporciona una version optimizada \
Responder en Markdown."

def check_url_status(url):
    status = None
    try:
        response = requests.get(url)
        if response.status_code == 200:
            status = f"Success: {url} is reachable."
        else:
            status = f"Failed: {url} responded with status code {response.status_code}."
    except requests.exceptions.RequestException as e:
        status = f"Error: Unable to reach {url}. Details: {e}"
    return status

def get_chat(question):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

def copilot_openai(question):
    stream = openai.chat.completions.create(
        model = MODEL_GPT,
        messages = get_chat(question),
        stream = False
    )
    #print(stream.choices[0].message.content)
    return stream.choices[0].message.content
    # response = ""
    # display_handle = display(Markdown(""), display_id=True)
    # for chunk in stream:
    #     response += chunk.choices[0].delta.content or ''
    #     response = response.replace("```","").replace("markdown", "")
    #     update_display(Markdown(response), display_id=display_handle.display_id)

def copilot_ollama(question):
    # content = f"{system_prompt} Pregunta: {question}"

    # messages = [
    # {"role": "user", "content": content}
    # ]

    # payload = {
    #     "model": MODEL_LLAMA,
    #     "messages": messages,
    #     "stream": True
    # }

    # response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    client = ollama.Client(
      host=OLLAMA_SERVER,
      headers={'x-some-header': 'some-value'}
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    response = client.chat(model=MODEL_LLAMA, messages=messages)
    return response['message']['content']


st.title("Copilot Chat")

# Session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []
# LLM selector
llm_model = st.selectbox("Select LLM model", ["gpt-4o-mini", "llama3.2"])
st.write(f"Selected model: {llm_model}")
if llm_model:
    st.divider()
    if llm_model == MODEL_LLAMA:
        status = check_url_status(OLLAMA_SERVER)
        print(status)
        st.write(check_url_status(OLLAMA_SERVER))
    else:
        st.write("Using OpenAI API")
# Chat input
st.divider()
user_input = st.text_input("Escribe un código", "")
send_clicked = st.button("Send")

if send_clicked and user_input:
    st.session_state.messages.append(("You", user_input))
    
    # Simulate AI response
    if llm_model == MODEL_LLAMA:
        response = copilot_ollama(user_input)
    else:
        response = copilot_openai(user_input)
    print("------------------")
    print(response)
    # # Simulate streaming response
    #st.session_state.messages.append(("AI", ""))
    # for char in response:
    #     st.session_state.messages[-1] = ("AI", st.session_state.messages[-1][1] + char)
    #     time.sleep(0.05)
    #     st.rerun()

    # # Display messages
    # for sender, msg in st.session_state.messages:
    #     st.markdown(f"**{sender}:** {msg}")

    #st.markdown(display(Markdown(response)))
    st.markdown(response)
    #st.markdown(Markdown(response['message']['content']))
