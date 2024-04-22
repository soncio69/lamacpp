from openai import OpenAI

# Uso streamlit come app framework
import streamlit as st


# Crea il client
client = OpenAI(
    api_key='545454545',
    base_url='http://localhost:8000/v1'
)

# Titolo dell'app   
st.title('OpenAI ChatGPT TAROCCO')
prompt = st.chat_input('Inserisci qui il tuo prompt')

# All'invio sottometto il prompt
if prompt:
    st.chat_message('user').markdown(prompt)

    #Chat completion
    response = client.chat.completions.create(
        # definisco il modello da utilizzare
        model='models/mistral-7b-instruct-v0.1.Q4_K_M.gguf',   

        # definisco il prompt
        messages=[{
            'role':'user',
    #        'content':'what is ROI in reference to finance?'
            'content': prompt
        }],
        # Aggiungiamo lo streaming della risposta
        stream=True
    )

    with st.chat_message('ai'):
        completed_message = ''
        message = st.empty()

        #Stampa la risposta se non è none
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                # print(chunk.choices[0].delta.content, flush=True, end="")
                completed_message += chunk.choices[0].delta.content
                message.markdown(completed_message)

