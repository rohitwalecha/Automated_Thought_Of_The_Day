import threading
import Sending_an_image_through_mail


def startAutomatingMail(urlOfQuoteOfTheDay):
    print("Starting..... Automating thought of the day Mail")
    Sending_an_image_through_mail.automateThought(urlOfQuoteOfTheDay)
    threading.Timer(20*60.0,startAutomatingMail).start()




    

