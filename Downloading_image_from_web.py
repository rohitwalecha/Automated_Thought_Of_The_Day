import requests

def downloadImageFromWeb(url):
    f = open('Thought of the day.jpg','wb')  #create file locally   
    f.write(requests.get(url).content)  #write image content to this file 
    f.close()

#downloadImageFromWeb('https://www.brainyquote.com/photos_tr/en/a/alphonsekarr/104193/alphonsekarr1.jpg')
