import requests 
from bs4 import BeautifulSoup
from gtts import gTTS
import os
from playsound import playsound



#Just storing the info from website on result var
result = requests.get("https://timesofindia.indiatimes.com/india/coronavirus-in-india-live-updates/liveblog/76251911.cms")
#This just checks if the stuff I am saying actually works
#Code 200 is good. Anything else bad.

#Nothing, just prints out a shit ton of HTML stuff

#This var stores the content in the page
contentpage = result.content

#Extracts only certain information
soup = BeautifulSoup(contentpage, 'lxml')


        

#This finds all the <b> tags in the HTML and finally stores them
latestNews = soup.find_all('b')


#This takes the list from the var, loops through it and finally converts them into pure text

for news in latestNews:
    latestNews = news.get_text()
    print(latestNews)


    
    

#This shows that the output is a string!



#This specifies the language i.e English


#This just activates the Text To Speech Engine!





#Saves it as an audio file
   ###news = str(news)
    #print(newsNow)
    #print(type(newsNow))
    #for news in latestNews:
        #latNewsTxt = open('latestnews.txt', 'w')
        #latNewsTxt = latNewsTxt.writelines()
#    newfile = open(r'some.txt', 'w')
    ###print(newsNow)