from translate import Translator
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import soundfile as sf


'''texto = input('Texto: ') #texto para ser traduzido

detectar = detect(texto) #detecter o idioma do texto

traduz = Translator(from_lang=detectar, to_lang='pt-br') # traduçao do texto

traducao = traduz.translate(texto) #texto traduzido

print( texto)
print(detectar)
print(traducao)'''

'''try:
    texto = input('Texto: ')

    # Detectar automaticamente o idioma
    detectar = detect(texto)

    # Informar ao usuário o idioma detectadose
    print(f'Idioma Detectado: {detectar}')


    # Traduzir para o português
    traduz = Translator(from_lang=detectar, to_lang='pt-br')
    traducao = traduz.translate(texto)
    print(traduz)
    print('Texto original:', texto)
    print('Texto Traduzido:', traducao)
except LangDetectException as e:
    print('Não foi possível detectar o idioma:', e)
except Exception as e:
    print('Ocorreu um erro inesperado:', e)
'''



# Inicializa o reconhecedor de fala
r = sr.Recognizer()


# Função para traduzir a fala
def traduzir_audio():
    with sr.Microphone(1) as source:
        print("Diga algo...")
        audio = r.listen(source)

        # Reconhecimento de fala (converter áudio em texto)
        try:
            texto = r.recognize_google(audio)
            print(f"Texto reconhecido: {texto}")

            # Detectar idioma do texto
            detectar = detect(texto)

            # Permitir que o usuário escolha o idioma de destino
            idioma_destino = input("Escolha o idioma de destino (por exemplo, pt-br para português brasileiro): ")

            # Traduzir para o idioma de destino
            traduz = Translator(from_lang=detectar, to_lang=idioma_destino)
            traducao = traduz.translate(texto)

            print(f"Texto Traduzido para {idioma_destino}: {traducao}")

        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala.")
        except sr.RequestError as e:
            print(f"Ocorreu um erro na solicitação: {e}")

if __name__ == "__main__":
    traduzir_audio()


