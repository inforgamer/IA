# Voz.py
import edge_tts as tts
import asyncio  as aio

from IA import ia

async def falar(texto):
    comunicador = tts.Communicate(texto, "pt-BR-FranciscaNeural")
    await comunicador.save("voz.mp3")
    print("Salvou")

aio.run(falar(ia("teste")))