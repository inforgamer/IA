#IA.py
import requests as req


url = "http://192.168.0.7:1234/v1/chat/completions"
#url = "http://127.0.0.1:1234/v1/chat/completions"

def ia(pergunta):

    data = {
        "model": "meta-llama-3.1-8b-instruct",
        "messages": [
            {"role": "user", "content": pergunta}
        ]
    }

    response = req.post(url, json=data)
    resposta = response.json()

   # print(resposta)

    return(resposta["choices"][0]["message"]["content"])
    #return "Erro na IA"