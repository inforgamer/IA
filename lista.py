import speech_recognition as sr

rec = sr.Recognizer()

def listar():
    for i, mic in enumerate(sr.Microphone.list_microphone_names()):
        print(i, mic)

listar()
