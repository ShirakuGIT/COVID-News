import reqcovid
import vlc
try:
    reqcovid.news_speak()
    p = vlc.MediaPlayer("news.mp3")
    p.play()
except:
    p = vlc.MediaPlayer("news.mp3")
    p.play()
