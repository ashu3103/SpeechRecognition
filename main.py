!pip install PyAudio
!pip install SpeechRecognition

import speech_recognition as sr
import pyaudio
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
  print("[search Google : search Youtube]")
  print("Speak Now!!")
  audio = r3.listen(source)

if 'video' in r1.recognize_google(audio):
  r1 = sr.Recognizer()
  url = 'https://www.youtube.com/results?search_query='
  with sr.Microphone() as source:
    print("Search for video")
    audio = r1.listen(source)
  
    try:
      get = r1.recognize_google(audio)
      print(get)
      wb.get().open_new(url+get)
    except sr.UnknownValueError:
      print("Couldn't understand")
    except sr.RequestError as e:
      print("Failed to get results".format(e))
