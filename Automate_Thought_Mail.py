import threading
import Sending_an_image_through_mail
def startAutomatingMail():
    print("Starting..... Automating thought of the Mail")
    Sending_an_image_through_mail.automateThought()
    threading.Timer(60.0*60.0,startAutomatingMail).start()
    

startAutomatingMail()
