from openai import OpenAI

# Crea il client
client = OpenAI(
    api_key='545454545',
    base_url='http://localhost:8000/v1'
)

# Chat completion
response = client.chat.completions.create(
    
    # definisco il modello da utilizzare
    model='models/mistral-7b-instruct-v0.1.Q4_K_M.gguf',   
#    model='models/zefiro-7b-beta-ITA-v0.1-q4_0.gguf',

    # definisco il prompt
     messages=[{
        'role':'user',
#        'content':'what is ROI in reference to finance?'
#        'content':'Cosa si intende per  ROI in ambito finanziario?'
#        'content':'Consigliami se iscrivermi all''università a 50 anni'
        'content':'How many parameter has CHAT-GPT4'
    }],
    # Aggiungiamo lo streaming della risposta
    stream=True
)

#Stampa la risposta
# print(response.choices[0].message.content)
for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, flush=True, end="")
   