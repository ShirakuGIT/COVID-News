import gtts
from gtts import gTTS
import os
import requests 
from bs4 import BeautifulSoup
import vlc
import time

def news_speak():
            #Just storing the info from website on result var
    result = requests.get("https://timesofindia.indiatimes.com/india/coronavirus-omicron-variant-india-live-updates-january-26/liveblog/89125067.cms")


            #This just checks if the stuff I am saying actually works
            #Code 200 is good. Anything else bad.
            #Nothing, just prints out a shit ton of HTML stuff
            #This var stores the content in the page
    contentpage = result.content

            #Extracts only certain information
    soup = BeautifulSoup(contentpage, 'lxml')     

            #This finds all the <b> tags in the HTML and finally stores them
    latestNews = soup.find_all('p')
            
        #This takes the list from the var, loops through it and finally converts them into pure text
    language = 'en'

    temp = ""

    for news in latestNews:
        latestNews = news.get_text()
        temp += latestNews + "\n"
        print(temp)

    try:
        myobj = gTTS(text=temp, lang=language, slow=False)
        myobj.save("news.mp3")
    except:
        p = vlc.MediaPlayer("news.mp3")
        p.play()
        time.sleep(240)

news_speak()




