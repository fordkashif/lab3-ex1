import smtplib

fromname = 'Kashif Ford'
fromaddr = 'kashif.ford@gmail.com'
toname = 'Davis Shanay'
toaddr = 'shanaynesha@hotmail.com'
subject = 'Music'
msg = 'Check out my song'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'kashif.ford@gmail.com'
password = 'tequilla'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()