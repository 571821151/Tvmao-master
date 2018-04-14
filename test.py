import urllib
import time
def download_img(url):
    path = str(time.time()) + ".gif"
    data = urllib.urlopen(url).read()
    f = open('d:/gif/' + path, "wb")
    f.write(data)
    f.close()
download_img('https://pppp.642p.com/91/2018/04/TVRr6rus.gif')
