import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():

    try:
        with sr.Microphone() as source:
            print('Ouvindo')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if "Olavo" in comando:
                comando = comando.replace('Olavo', '')
                maquina.say(comando)
                maquina.runAndWait()


    except:
        print("Não foi possível acessar o serviço de reconhecimento de fala.")

    return comando

def comando_voz_usuario():