import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

credentials = {'username': 'margarita_kuncheva93@abv.bg',
               'password': 'nemskinemski93'}

# Start connection
server = smtplib.SMTP('smtp.abv.bg', 465)
server.starttls()

# Log in to the server
server.login(credentials['username'], credentials['password'])

# Build message
message = MIMEMultipart()
message['Subject'] = 'Demo Mail'
message['From'] = 'margarita_kuncheva93@abv.bg'
message['To'] = 'margaritakuncheva93@gmail.com'
message_text = f'Hello! This email is sent from demo! {datetime.now()}'
body = MIMEText(message_text)
message.attach(body)

# Send the mail
server.send_message(message)
print('Mail sent!')