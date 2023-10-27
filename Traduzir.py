from translate import Translator
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import speech_recognition as sr



'''texto = input('Texto: ') #texto para ser traduzido

detectar = detect(texto) #detecter o idioma do texto

traduz = Translator(from_lang=detectar, to_lang='pt-br') # traduçao do texto

traducao = traduz.translate(texto) #texto traduzido

print( texto)
print(detectar)
print(traducao)'''

try:
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







