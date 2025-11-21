# Voz.py
import edge_tts as tts
import asyncio  as aio
import pydub as pa
from pydub import AudioSegment
from pydub.playback import play



async def falar(resposta):
    comunicador = tts.Communicate(resposta, "pt-BR-FranciscaNeural")
    await comunicador.save("resposta.mp3")
    
    audio = AudioSegment.from_mp3("resposta.mp3")
    play(audio)
    print("Salvou")
    
