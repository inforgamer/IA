import asyncio
import edge_tts
import tempfile
import os
import pygame

async def _falar_async(texto, voz="pt-BR-FranciscaNeural"):
    if not texto.strip():
        return

    # Cria arquivo temporário
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_filename = tmp_file.name

    # Gera o áudio
    communicate = edge_tts.Communicate(texto, voice=voz)
    await communicate.save(tmp_filename)

    # Inicializa o mixer
    pygame.mixer.init()
    pygame.mixer.music.load(tmp_filename)
    pygame.mixer.music.play()

    # Espera terminar
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    # Finaliza mixer antes de remover arquivo
    pygame.mixer.quit()

    # Remove o arquivo temporário
    os.remove(tmp_filename)

def falar(texto, voz="pt-BR-FranciscaNeural"):
    asyncio.run(_falar_async(texto, voz))
