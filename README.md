## Installazione

Dopo aver creato un conda environment ad hoc:

$$$$$ conda create -n llamacpp python

clono il repository GIT di llama.cpp 
$$$$$ git clone https://github.com/ggerganov/llama.cpp

dopo essermi posizionato nella directory del repo, effettuo il make del progetto (la libreria è scritta in cpp)

$$$$ cd llama.cpp && make

Dopo aver attivato l'environment, procedo con l'installazione delle librerie python necessarie

$$$$ pip install openai 'llama-cpp-python[server]' pydantic instructor streamlit

- openai : utilizzata come API per comunicare con il server llama.cpp (che è compatibile con OpenAI)
- llama-cpp-python[server] : consente di interagire con llama.cpp via python
- pydantic 
- instructor : necessario per collegare llm con la chiamata a funzioni esterne
- streamlit : costituisce il framework utilizzato per la UI dell'app

Per poter utilizzare llamacpp è necessario scaricare i modelli da utilizzare in formato gguf (modello quantizato) in modo da poterli eseguire anche senza GPU.
Di seguito i modelli scaricati:
- https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF
- https://huggingface.co/jartine/llava-v1.5-7B-GGUF/tree/main
- https://huggingface.co/giux78/zefiro-7b-beta-ITA-v0.1-GGUF


A questo punto è possibile far partire il server passando come parametro il modello da utilizzare

$$$$$ python -m llama_cpp.server --model models/mistral-7b-instruct-v0.1.Q4_K_M.gguf

Uvicorn running on http://localhost:8000

A questo punto è possibile iniziare ad interagire con il modello come se fosse OpenAI ChatGPT

______________

Per importare la libreria che consente di interagire con yahoo finance

$$$$ pip install yfinance

Per utilizzare llm per implementare chiamate a funzioni (ad es python, tipo stock_data.py) è necessario importare la libreria instructor

$$$$ pip install instructor

Grazie a questa libreria è possibile creare un "Response Model" per far si che vengano estratte delle informazioni dal prompt

Per utilizzare il response model è necessario riavviare il server per supportare il functionary model.
Prima il server era avviato per supportare il chat format (il default è chatml), ora è necessario utilizzare il functionary chat format

$$$$$ python -m llama_cpp.server --model models/mistral-7b-instruct-v0.1.Q4_K_M.gguf --chat functionary


Ulteriore step è quello di utilizzare più modelli LLM. Nel nostro caso il secondo modello dovrà procedere con il summary sulla base dell'esito della chiamata 
a funzione. Finora potevamo utilizzare solo una modalità di chat (chatml o functionary). 
Per potere utilizzare più modelli è necessario utilizzare un file di configurazione (config.json)
Una volta configurati i parametri è possibile rilanciare il server

$$$$$ python -m llama_cpp.server --config_file config.json

Esempio : riassumi l'andamento dell'azione AAPL negli ultimi 4 giorni

Utilizzare un modello multi-modal(ad esempio llava)

$$$$ python -m llama_cpp.server --model models/llava-v1.5-7b-Q4_K.gguf --clip_model_path models/llava-v1.5-7b-mmproj-Q4_0.gguf --chat llava-1-5



