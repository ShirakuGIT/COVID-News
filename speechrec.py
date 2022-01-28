import speech_recognition as sr 
import time
from reqcovid import *
import gtts

r = sr.Recognizer()

mic = sr.Microphone(device_index=6)

introduction = """
         HEY WELCOME TO THE COVID NEWS READER PROGRAM
         WE HAVE SELECTED THE TOP HEADLINES FROM 
         MAJOR NEWS SOURCES. 
         
         IF YOU WANT TO HEAR THE NEWS,
         JUST REPEAT THE FOLLOWING PHRASES LISTED BELOW FOR
         THEIR CORRESPONDING NEWS SITES AND HEADLINES.

         THE MICROPHONE WILL HEAR WHAT YOU ARE TRYING TO SAY,
         SO PLEASE BE CLEAR, AND WAIT FOR A FEW SECONDS 
         BEFORE SPEAKING OUT \n \n

         HERE ARE THE PHRASES

         1) TIMES OF INDIA
         2) CNBC
         3) HINDU
         """

myobj = gTTS(text=introduction, lang='en', slow=False)
myobj.save("intro.mp3")
p = vlc.MediaPlayer("intro.mp3")
p.play()

print(introduction)


time.sleep(35)

goahead = """
         OKAY, THE MICROPHONE IS LISTENING, GO AHEAD 
         AND SPEAK AFTER 5 SECONDS PASS.


"""



myobj = gTTS(text=goahead, lang='en', slow=False)
myobj.save("goahead.mp3")
p = vlc.MediaPlayer("goahead.mp3")
p.play()

print(goahead)

time.sleep(5)


with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

user_speech = r.recognize_google(audio)

if user_speech == "Times of India":
    news_spk_toi()
elif user_speech == "CNBC":
    news_spk_cnbc()
elif user_speech == "Hindu":
    news_spk_hindu()
else:
    pass
