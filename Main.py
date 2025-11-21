#Main.py
import asyncio as aio

from Microfone import ouvir_microfone
from IA import ia
from Voz import falar


if __name__ == "__main__":
    pergunta = ouvir_microfone()
    resposta = ia(pergunta)
    aio.run(falar(resposta))