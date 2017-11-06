from random import random, randint
from turtledemo.forest import randomfd

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
    response = opener.open('https://www.brainyquote.com/topics/inspirational')
    print("Web Scrapper : Going to www.brainyquote.com to fetch a random qoute of the day")
    #Reading the object of response and printing the html of above url of web page
    print("Web Scrapper : Reading the response object")
    page_html=response.read()
    #print(page_html)
    #Now using BeautifulSoup to read data systematically
    page_soup=soup(page_html,"html.parser")
    #print(page_soup.img.get("src"))
    print("Web Scrapper : bs4 parsing the HTML Page")
    #print(page_soup.prettify())
    #print(page_soup.find_all("a"))
    links=page_soup.find_all("img")
    for link in links :
        print(link.get("src"),":",link.get("alt"))
    print("Web Scrapper : bs4 fetched all the img tags")
    #print("https://www.brainyquote.com"+links[2].get("src"))
    print("Web Scrapper : Image Scrapped Successfully")
    print("https://www.brainyquote.com"+links[randint(2,10)].get("src"))
    SendingAnImageThroughMail2.automateThought("https://www.brainyquote.com" + links[randint(2,10)].get("src"))
    threading.Timer(60*60.0,scrapeTheWeb).start()
    #https://www.brainyquote.com/photos_tr/en/s/sophocles/101515/sophocles1-2x.jpg


scrapeTheWeb()