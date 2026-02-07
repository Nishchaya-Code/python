import speech_recognition as sr
import pyttsx3

def speak(text, language="en"):
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    voices=engine.getProperty('voices')

    if language=='en':
        engine.setProperty('voice',voices[0].id)
    else:
        engine.setProperty('voice',voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer=sr.Recognizer
    with sr.Microphone() as source:
        print('please speak in english now')
        audio=recognizer.listen(source)
    try:
        print('Recognizing Speech')
        text=rcognizer.recognize_google(audio, language="en-UK")
        print(f'You said:{text}')
        return text
    except sr.UnkownValueError:
        print('could not understand the audio')
    except sr.RequestError as e:
        print(f' API Error; as {e}')
    return " "


def translate_text (text,target_languages="es"):
    translator=Translator()
    translation=translator.translate(text, dest=target_language)
    print(f'Translated text:
          {translation.text}')
          return translation.text
        
def display_language_options():
    print('available options:')
    print('1. Spanish(Esp)')
    print('2.Chinese(Ch)')
    print('3.Nepali(Np)')
    print('4.Dutch(Dt)')

    choice=input('please select the target language number(1-4)')
    language_dict={
        '1':'Esp'
        '2':'Ch'
        '3':'Np'
        '4':'Dt'
      }

      return language_