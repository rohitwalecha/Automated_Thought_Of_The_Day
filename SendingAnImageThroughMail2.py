import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import Downloading_image_from_web


def automateThought(urlOfQuoteOftheDay):
    print("Intializing thought of the day")

    #All the Details at first fromAddress(sender email id), to Address(reciever's email id) and subject of the mail
    fromAddress="rohitwalecha8@gmail.com"
    print("Preparing Addresses to send!!")
    #dLs=["abhisek.nag@sdgc.com","Vishal.Singh@sdgc.com","Deepika.Khanna@sdgc.com","Mohammad.Azaz@sdgc.com","mohammed.ajaz@sdgc.com","rohit@sdgc.com","rohitwalecha8@gmail.com","amansinghvns26@gmail.com","aman.singh@sdgc.com","deepikasawhney19@gmail.com","vivekkumarwalecha@gmail.com","walechai019@gmail.com","lalitsinghjmi@gmail.com","ruchikasharma05670@gmail.com"]
    dLs=["rohitwalecha8@gmail.com"]
    #toAddress="rohitwalecha8@gmail.com"
    subject="It's test mail please ignore this"


    #Downloading image from the web using our own custom module "Downloading_image_from_web"
    print("Trying To Fetch Image from the web!!")
    Downloading_image_from_web.downloadImageFromWeb(urlOfQuoteOftheDay)
    print("Image Fecthed Successfully")


    

    #Creating a mime multipart message
    server=smtplib.SMTP("smtp.gmail.com","587")
    print("Contacting Server")
    server.starttls()
    server.login("rohitwalecha8@gmail.com","rohitwalecha")
    print("Loging In")
    for toAddress in dLs :

        '''
    
        msg = MIMEMultipart('alternative')
        msg["To"] = toAddress
        msg["From"] = fromAddress
        msg["Subject"] = subject

    
        #Text to be sent in mail
        #body="Hi This is an automated tought of the day using web scraping!! "

        #Downloading image from the web using our own custom module "Downloading_image_from_web"
        print("Trying To Fetch Image from the web!!")
        Downloading_image_from_web.downloadImageFromWeb(urlOfQuoteOftheDay)
        print("Image Fecthed Successfully")

        #Opening the thought of the day image here
        imageName="Thought of the day.jpg"
        attachment=open(imageName,'rb')

        msgImage=MIMEImage(fp.read())
        msgImage.add_header('Content-ID','<image1>')
        msg.Root.attach(msgImage)
        #adding data in the image as a part using MIMBase(don't really know whats happening here)
        #part=MIMEBase('application','octet-stream')
        #part.set_payload(attachment.read())
        #encoders.encode_base64(part)
        #part.add_header('Content-Disposition',"attachement; filename = "+imageName)

        #Attaching Image in the email msg
        #msg.attach(part)
        print("Attaching Image with msg")

        #Attaching body
        #msg.attach(MIMEText(body,'plain'))
        
        print("Attaching message content")

        #Changing msg content into text
        
        contentText=msg.as_string()
        '''
        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'Automated test mail | Thought of the day'
        msgRoot['From'] = fromAddress
        msgRoot['To'] = toAddress
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText('<b><i></i></b><br><img src="cid:image1"><br>', 'html')
        msgAlternative.attach(msgText)

        # This example assumes the image is in the current directory
        fp = open('Thought of the day.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        #Contacting gmail server and logging In
        '''
        server=smtplib.SMTP("smtp.gmail.com","587")
        print("Contacting Server")
        server.starttls()
        server.login("rohitwalecha8@gmail.com","rohitwalecha")
        print("Loging In")
        '''
        server.sendmail(fromAddress,toAddress,msgRoot.as_string())
        print("Thought of the Day Sent Successfully to :",toAddress)
        
    server.quit()
    #https: // www.imagesbazaar.com / Html2015 / homecat / images / festival.jpg?v1.1