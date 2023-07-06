import speech_recognition as sr
import pyttsx3
import datetime

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            audio.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if "olavo" in comando:
                comando = comando.replace('olavo', '')
                maquina.say(comando)
                maquina.runAndWait()

    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
    except sr.RequestError:
        print("Não foi possível acessar o serviço de reconhecimento de fala.")

    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()

comando_voz_usuario()
