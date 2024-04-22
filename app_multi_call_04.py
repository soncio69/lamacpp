# Andiamo ad utilizzare un response model 

from openai import OpenAI
import streamlit as st

import instructor

# Importa BaseModel class
from pydantic import BaseModel


# Importo la funzione custom da richiamare
#from stock_data import get_stock_prices

# Crea il client
client = OpenAI(
    api_key='545454545',
    base_url='http://localhost:8000/v1'
)

st.cache_data.clear()
st.cache_resource.clear()
# Creo un patched client. In pratica, in questo modo si abilita il 'response_model'
client = instructor.patch(client=client)

# DEfinisce la struttura dei dati che vogliamo che venga estratta dall'LLM
class ResponseModel(BaseModel):
    ticker:str
    days:int

#  class ResponseModel(BaseModel):
#     codfiscale:str
#     importo:int
#     date:str


st.title('OpenAI ChatGPT TAROCCO')
prompt = st.chat_input('Inserisci qui il tuo prompt')

# All'invio sottometto il prompt
if prompt:
    st.chat_message('user').markdown(prompt)

    #Chat completion
    response = client.chat.completions.create(
        max_tokens=-1,
        # definisco il modello da utilizzare
#        model='mistral-function-calling',   
        model='models/mistral-7b-instruct-v0.1.Q4_K_M.gguf',   

        # definisco il prompt
        messages=[{
            'role':'user',
            'content': prompt
        }],
        response_model=ResponseModel,
    )

    st.chat_message("ai").markdown(response)

    # try:
    #     prices = get_stock_prices(response.ticker, response.days)        
    #     st.chat_message("ai").markdown(prices)
        
    #     #Summary output prompt +prices
    #     fullresponse = client.chat.completions.create(
    #         # definisco il modello da utilizzare
    #         model='mixtral',   

    #         # definisco il prompt
    #         messages=[{
    #             'role':'user',
    #             'content': prompt +'\n' +str(prices)
    #         }],
    #         stream=True
    #      )
    #     with st.chat_message('ai'):
    #         completed_message = ''
    #         message = st.empty()

    #         #Stampa la risposta se non è none
    #         for chunk in fullresponse:
    #             if chunk.choices[0].delta.content is not None:
    #                 # print(chunk.choices[0].delta.content, flush=True, end="")
    #                 completed_message += chunk.choices[0].delta.content
    #                 message.markdown(completed_message)

    # except Exception as e:
    #     st.chat_message("ai").markdown("Qualcosa è andato storto!!!")


    