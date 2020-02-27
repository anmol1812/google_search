import pyaudio
import wave
from gtts import gTTS
import playsound
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
from googlesearch import search
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

file_audio = sr.AudioFile('output.wav')
with file_audio as source:
   audio_text = r.record(source)

print(type(audio_text))
audio_to_txt = r.recognize_google(audio_text)
print(audio_to_txt)
