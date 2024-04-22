# Andiamo ad utilizzare un response model 

from openai import OpenAI
import streamlit as st

# Importo la funzione custom da richiamare
#from stock_data import get_stock_prices

# Crea il client
client = OpenAI(
    api_key='545454545',
    base_url='http://localhost:8000/v1'
)

st.title('OpenAI ChatGPT TAROCCO111')
image_url = st.text_input('Put your image URL qui')

prompt = st.chat_input('Inserisci qui il tuo prompt')


# All'invio sottometto il prompt
if prompt:
    st.chat_message('user').markdown(prompt)

    #Chat completion
    response = client.chat.completions.create(
        max_tokens=-1,
        # definisco il modello da utilizzare
        model='models/llava-v1.5-7b-Q4_K.gguf',   

        # definisco il prompt
        messages=[{
                'role':'user',
                'content': [
                    {
                        'type' : 'image_url',
                        'image_url' : image_url
                    },
                    {
                        'type' : 'text',
                        'text' : prompt
                    }                    
                ]
            }],
        stream=True,
    )

    st.chat_message("ai").markdown(response)

 
    with st.chat_message('ai'):
        completed_message = ''
        message = st.empty()

        #Stampa la risposta se non è none
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                # print(chunk.choices[0].delta.content, flush=True, end="")
                completed_message += chunk.choices[0].delta.content
                message.markdown(completed_message)



    