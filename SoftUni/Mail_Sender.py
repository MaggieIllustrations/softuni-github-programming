import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

credentials = {'username': '',
               'password': ''}


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()


server.login(credentials['username'], credentials['password'])

message = MIMEMultipart()
message['Subject'] = 'Demo Mail'
message['From'] = 'margaritakuncheva93@gmail.com'
message['To'] = 'margarita_kuncheva93@abv.bg'
message_text = f'Hello! This email is sent from demo! {datetime.now()}'
body = MIMEText(message_text)
message.attach(body)

server.send_message(message)
print('Mail sent!')



