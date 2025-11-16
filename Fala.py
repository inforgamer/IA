import speech_recognition as sr

rec = sr.Recognizer()

def ouvir():
    with sr.Microphone(device_index=13) as mic:  # <<< ESTE
        print("🎧 Ouvindo (Mic + PC)...")
        audio = rec.listen(mic)

    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print("🗣️ Você/PC disse:", texto)
        return texto
    except Exception as e:
        print("Erro:", e)
        return ""
