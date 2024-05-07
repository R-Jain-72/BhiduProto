'''
import speech_recognition as sr
import os
def say(text):
    os.system(f"say {text}")

if __name__ == "__main__":
    say("Hello")
'''
import speech_recognition as sr
import win32com.client
# Create a speech object
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def say(text):
  """Speaks the given text using Windows Speech Synthesis."""
  speaker.Speak(text)

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.pause_threshold = 1
    audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query
    except Exception as e:
       return say("Error phir seh bol lawde")

if __name__ == "__main__":
    say("Hello from Bhidu")
    while True:
        print("Listening ...")
        text = takeCommand()
        say(text)
