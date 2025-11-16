from Fala import ouvir
from Voz import falar
from IA import pensar

while True:
    frase = ouvir()  # VTuber escuta

    if not frase:
        continue

    print("🧠 Processando IA...")
    resposta = pensar(frase)  # IA responde

    if resposta.strip():
        print("🔊 IA:", resposta)
        falar(resposta)  # fala imediatamente
