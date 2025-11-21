#IA.py
import requests as req


url = "http://127.0.0.1:1234/v1/chat/completions"

def ia(mensagem):

    data = {
        "model": "meta-llama-3.1-8b-instruct",
        "messages": [
            {"role": "user", "content": mensagem}
        ]
    }

    response = req.post(url, json=data)
    resposta = response.json()
    print(resposta["choices"][0]["message"]["content"])
