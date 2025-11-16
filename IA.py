import requests
import json

def pensar(texto_usuario):
    if not texto_usuario.strip():
        return ""

    # prompt da VTuber
    prompt_personalidade = (
        ""
    )

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "model",
        "prompt": prompt_personalidade + texto_usuario,
        "stream": True
    }

    resposta_texto = ""
    try:
        with requests.post(url, json=payload, stream=True) as resp:
            for linha in resp.iter_lines():
                if not linha:
                    continue
                try:
                    data = json.loads(linha.decode("utf-8"))
                except:
                    continue
                parte = data.get("response", "")
                resposta_texto += parte
    except Exception as e:
        print("Erro IA:", e)

    return resposta_texto
