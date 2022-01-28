import gtts
from gtts import gTTS
import os
import requests 
from bs4 import BeautifulSoup
import vlc
import time
from pathlib import Path



def news_spk_toi():
    #Just storing the info from website on result var
    result = requests.get("https://timesofindia.indiatimes.com/india/coronavirus-omicron-variant-india-live-updates-january-26/liveblog/89125067.cms")


    #This just checks if the stuff I am saying actually works
    #Code 200 is good. Anything else bad.
    #Nothing, just prints out a shit ton of HTML stuff
    #This var stores the content in the page
    contentpage = result.content




    #Extracts only certain information
    soup = BeautifulSoup(contentpage, 'lxml')     




    #This finds all the <p> tags in the HTML and finally stores them
    latestNews = soup.find_all('p')
    



    #The following code-bit prints out all the textual information retrieved from the Website
    temp = ""

    for news in latestNews:
        latestNews = news.get_text()
        temp += latestNews + "\n"
    temp.replace("Stay with TOI for live updates:Read Less", "")

    print(temp)
    
    print("\nPlease wait, the news will be read to you momentarily...")
    
    


    #Selects the language for the news reader
    language = 'en'




    #To check whether news.mp3 exists or not
    path_to_file = Path('news.mp3')
    file_exists = path_to_file.is_file()



    '''
    The following code bit essentially does two things:
        
        1) It checks whether a pre-existing .mp3 file exists
        2) If so, it removes that file and creates a new .mp3 file with the news
           Else, it just creates a new .mp3 file and reads that news

    The try/except statements exists in case there are any 
    annoying exceptions getting in the way of reading the
    news

    '''



    if file_exists == "True":
        os.remove('news.mp3')
        try:
            myobj = gTTS(text=temp, lang=language, slow=False)
            myobj.save("news.mp3")
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
        except:
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
    else:
        try:
            myobj = gTTS(text=temp, lang=language, slow=False)
            myobj.save("news.mp3")
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
        except:
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)


def news_spk_cnbc():
    #Just storing the info from website on result var
    result = requests.get("https://www.cnbctv18.com/healthcare/omicron-news-live-updates-12274752.htm")


    #This just checks if the stuff I am saying actually works
    #Code 200 is good. Anything else bad.
    #Nothing, just prints out a shit ton of HTML stuff
    #This var stores the content in the page
    contentpage = result.content




    #Extracts only certain information
    soup = BeautifulSoup(contentpage, 'lxml')     



    #This finds all the <strong> tags in the HTML and finally stores them
    latestNews = soup.find_all('strong')
    



    #The following code-bit prints out all the textual information retrieved from the Website
    temp = ""

    for news in latestNews:
        latestNews = news.get_text()
        temp += latestNews + "\n" + "\n"
    temp.replace("Stay with TOI for live updates:Read Less", "")

    print(temp)
    
    print("\nPlease wait, the news will be read to you momentarily...")
    
    


    #Selects the language for the news reader
    language = 'en'



    #To check whether news.mp3 exists or not
    path_to_file = Path('news.mp3')
    file_exists = path_to_file.is_file()



    '''
    The following code bit essentially does two things:
        
        1) It checks whether a pre-existing .mp3 file exists
        2) If so, it removes that file and creates a new .mp3 file with the news
           Else, it just creates a new .mp3 file and reads that news

    The try/except statements exists in case there are any 
    annoying exceptions getting in the way of reading the
    news

    '''


    if file_exists == "True":
        os.remove('news.mp3')
        try:
            myobj = gTTS(text=temp, lang=language, slow=False)
            myobj.save("news.mp3")
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
        except:
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
    else:
        try:
            myobj = gTTS(text=temp, lang=language, slow=False)
            myobj.save("news.mp3")
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
        except:
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)



def news_spk_hindu():
    #Just storing the info from website on result var
    result = requests.get("https://www.thehindu.com/news/national/coronavirus-live-updates-article38183192.ece")



    #This just checks if the stuff I am saying actually works
    #Code 200 is good. Anything else bad.
    #Nothing, just prints out a shit ton of HTML stuff
    #This var stores the content in the page
    contentpage = result.content



    #Extracts only certain information
    soup = BeautifulSoup(contentpage, 'lxml')     



    #This finds all the <strong> tags in the HTML and finally stores them
    latestNews = soup.find_all('h2')
    


    #The following code-bit prints out all the textual information retrieved from the Website
    list1 = []

    for news in latestNews:
        latestNews = news.get_text()
        latestNews = latestNews.split("\n")
        list1 += latestNews



    '''
    Okay, the following code bit exists because of this annoying thing
    that Hindu implemented, they essentially repeated the same news title
    three times within the same page.

    So it'd read like
    "UN implemented new laws"
    "UN implemented new laws"
    "UN implemented new laws"
    "Relations between India and Japan improve"
    "....."

    Because of this, I had to slice the first 7 indices of the text from
    the string, but for that I had to first convert it into a list as I 
    could slice whole sentences instead of just slicing characters, which
    would be a hassle because we don't know what title they could use next.

    Anyways, sorry for boring you with the information, this part was tricky
    but I had to implement it anyway because without it, you'd just hear
    the same news repeated three times, which is pretty stupid.
    '''


    # List slicing to remove repeated news headings
    del list1[0:6]

    temp = ""

    for i in list1:
        temp += i + "\n\n"

    print(temp)

    
    print("\nPlease wait, the news will be read to you momentarily...")
    
    


    #Selects the language for the news reader
    language = 'en'



    #To check whether news.mp3 exists or not
    path_to_file = Path('news.mp3')
    file_exists = path_to_file.is_file()

    '''
    The following code bit essentially does two things:
        
        1) It checks whether a pre-existing .mp3 file exists
        2) If so, it removes that file and creates a new .mp3 file with the news
           Else, it just creates a new .mp3 file and reads that news

    The try/except statements exists in case there are any 
    annoying exceptions getting in the way of reading the
    news

    '''



    if file_exists == "True":
        os.remove('news.mp3')
        try:
            myobj = gTTS(text=temp, lang=language, slow=False)
            myobj.save("news.mp3")
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
        except:
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
    else:
        try:
            myobj = gTTS(text=temp, lang=language, slow=False)
            myobj.save("news.mp3")
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)
        except:
            p = vlc.MediaPlayer("news.mp3")
            p.play()
            time.sleep(240)





