import pyttsx3
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from langdetect import detect
from translate import Translator

'''m=pyttsx3.init()
# Configurações de gravação
fs = 44100  # Taxa de amostragem em Hz
seconds = 5  # Duração da gravação em segundos

# Grava áudio do microfone
recording = sd.rec(int(fs * seconds), samplerate=fs, channels=2, dtype='int16')
print("Gravando...")

# Aguarde até que a gravação seja concluída
sd.wait()
print("Gravação concluída.")

# Salve o áudio gravado em um arquivo WAV
sf.write("audio.wav", recording, fs)
print("Áudio salvo como audio.wav.")

# Reproduza o áudio gravado
print("Reproduzindo...")
sd.play(recording, fs)
sd.wait()
print("Reprodução concluída.")

# Inicializa o reconhecedor de fala
r = sr.Recognizer()

# Realize o reconhecimento de fala no áudio gravado
with sr.AudioFile("audio.wav") as source:
    audio = r.record(source)
    try:
        recognized_text = r.recognize_google(audio,language='pt-BR')
        print("Texto reconhecido: " + recognized_text)
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala.")
    except sr.RequestError as e:
        print("Ocorreu um erro na solicitação: " + str(e))

#detecta o idioma 
detectar = detect(recognized_text)
# Informar ao usuário o idioma detectadose
print(f'Idioma Detectado: {detectar}')
# Traduzir para o português
traduz = Translator(from_lang=detectar, to_lang='en')
traducao = traduz.translate(recognized_text)
print('Tadução do audio: '+traducao)


#Audio traduzido
print('Reproduzindo tradução...')
m.say(traducao)
m.runAndWait()'''


def main():
    m = pyttsx3.init()

    while True:
        
        # Configurações de gravação
        fs = 44100  # Taxa de amostragem em Hz
        seconds = float(input('Qual a duração do audio em segundos? ') )# Duração da gravação em segundos

        # Grava áudio do microfone
        recording = sd.rec(int(fs * seconds), samplerate=fs, channels=2, dtype='float32')
        print("Gravando...")

        # Aguarde até que a gravação seja concluída
        sd.wait()
        print("Gravação concluída.")

        # Salve o áudio gravado em um arquivo WAV
        sf.write("audio.wav", recording, fs)
        print("Áudio salvo como audio.wav.")

        # Reproduza o áudio gravado
        print("Reproduzindo...")
        sd.play(recording, fs)
        sd.wait()
        print("Reprodução concluída.")

        # Inicializa o reconhecedor de fala
        r = sr.Recognizer()

        # Realize o reconhecimento de fala no áudio gravado
        with sr.AudioFile("audio.wav") as source:
            audio = r.record(source)
            try:
                recognized_text = r.recognize_google(audio, language='pt-BR')
                print("Texto reconhecido: " + recognized_text)
            except sr.UnknownValueError:
                print("Não foi possível reconhecer a fala.")
                
                
            except sr.RequestError as e:
                print("Ocorreu um erro na solicitação: " + str(e))

        # Detecta o idioma
        detectar = detect(recognized_text)
        # Informa ao usuário o idioma detectado
        print(f'Idioma Detectado: {detectar}')
        
       
        # Traduz para o idioma de destino
        traduz = Translator(from_lang=detectar, to_lang='pt-BR')
        traducao = traduz.translate(recognized_text)
        print('Tradução do áudio: ' + traducao)

        # Reproduz o áudio da tradução
        print('Reproduzindo tradução...')
        m.say(traducao)
        m.runAndWait()
        res=input('Voce que continuar a traduçao? s ou n? ').lower()
        
        if res == 'n':
            print('Até a próxima!')
            break  # Sai do loop se a fala não pôde ser reconhecida
if __name__ == "__main__":
    main()
