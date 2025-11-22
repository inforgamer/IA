#Main.py
import asyncio as aio

from Microfone import ouvir_microfone
from IA import ia
from Voz import falar

x = 0
while x == 0:
    if __name__ == "__main__":
        pergunta = ouvir_microfone()
        print(pergunta)
        resposta = ia(pergunta)
        aio.run(falar(resposta))
        print(resposta)