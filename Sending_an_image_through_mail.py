import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  # Added
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import Downloading_image_from_web

print("Intializing thought of the day")

#All the Details at first fromAddress(sender email id), to Address(reciever's email id) and subject of the mail
fromAddress="rohitwalecha8@gmail.com"
toAddress="rohitwalecha8@gmail.com"
subject="Automated mail using web scraping | Thought of the day!! "

print("Preparing Addresses to send!!")

#Creating a mime multipart message
msg = MIMEMultipart()
msg["To"] = toAddress
msg["From"] = fromAddress
msg["Subject"] = subject

#Text to be sent in mail
body="Hi This is an automated tought of the day using web scraping!! "

#Downloading image from the web using our own custom module "Downloading_image_from_web"
print("Trying To Fetch Image from the web!!")
Downloading_image_from_web.downloadImageFromWeb('https://www.brainyquote.com/photos_tr/en/c/charlesrswindoll/388332/charlesrswindoll1.jpg')
print("Image Fecthed Successfully")

#Opening the thought of the day image here
imageName="Thought of the day.jpg"
attachment=open(imageName,'rb')

#adding data in the image as a part using MIMBase(don't really know whats happening here)
part=MIMEBase('application','octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachement; filename = "+imageName)

#Attaching Image in the email msg
msg.attach(part)
print("Attaching Image with")

#Attaching body
msg.attach(MIMEText(body,'plain'))
print("Attaching message content")

#Changing msg content into text
contentText=msg.as_string()

#Contacting gmail server and logging In
server=smtplib.SMTP("smtp.gmail.com","587")
print("Contacting Server")
server.starttls()
server.login("rohitwalecha8@gmail.com","rohitwalecha")
print("Loging In")
server.sendmail(fromAddress,toAddress,contentText)

print("Thought of the Day Sent Successfully")
server.quit() 
