import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib.request
#import Automate_Thought_Mail
import threading
import SendingAnImageThroughMail2

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def scrapeTheWeb() :
    print("Web Scrapper : Intializing....")
    opener = AppURLopener()
    response = opener.open('https://www.brainyquote.com/quotes_of_the_day.html')
    print("Web Scrapper : Going to www.brainyquote.com to fetch qoute of the day")    
    #Reading the object of response and printing the html of above url of web page
    print("Web Scrapper : Reading the response object")
    page_html=response.read()
    #print(page_html)
    #Now using BeautifulSoup to read data systematically
    page_soup=soup(page_html,"html.parser")
    print("Web Scrapper : bs4 parsing the HTML Page")
    #print(page_soup.prettify())
    #print(page_soup.find_all("a"))
    links=page_soup.find_all("img")
    print("Web Scrapper : bs4 fetched all the img tags")
    print("https://www.brainyquote.com"+links[2].get("src"))
    print("Web Scrapper : Image Scrapped Successfully")
    SendingAnImageThroughMail2.automateThought("https://www.brainyquote.com" + links[2].get("src"))
    threading.Timer(60*60.0,scrapeTheWeb).start()
    #https://www.brainyquote.com/photos_tr/en/s/sophocles/101515/sophocles1-2x.jpg


scrapeTheWeb()
