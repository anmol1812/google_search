'''
from googlesearch import search
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
def get_data(page_no):
    a = Request(page_no, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(a).read()
    soup = BeautifulSoup(webpage, "html.parser")
    for tag in soup.find_all("article") :
        id = tag.get('id')
        print(id)
    title = soup.find("meta",  property="og:description")
    print(title["content"] if title else "No meta description given")
query = "gamezop"
my_results_list = []
for i in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 1,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = None,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):   
    my_results_list.append(i)
    get_data(i)
    break




from googlesearch import search
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
def get_description(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    title = soup.find("meta",  property="og:description")
    return(title["content"] if title else "No meta description given")
query = "games"
for url in search(query, stop=1):
    description = get_description(url)
    print(description)
'''
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



#filename = 'C:/Users/Anmol/Anmol/output.wav'
#winsound.PlaySound(filename, winsound.SND_FILENAME)
#fs, data = wavfile.read('C:/Users/Anmol/Anmol/output.wav')
#song = AudioSegment.from_wav(filename)
#play(song)