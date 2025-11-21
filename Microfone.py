#Microfone.py
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 4000

def ouvir_microfone():
    with sr.Microphone() as source:
        print("Diga algo:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        texto = r.recognize_google(audio, language = "pt-BR", show_all = False)
       
        return texto

if __name__ == "__main__":
   retorno =ouvir_microfone()

   print("Você disse: " + retorno)
