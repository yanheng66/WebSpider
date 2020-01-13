import smtplib

sender_email = "houhouhahaheihei@gmail.com"
rec_email = "yanhengjiang123@gmail.com"
password = "1234qwerxxxx"
message = "we have a seat for ya"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
print ("1111111111")


server.login(sender_email, password)
print ("login success")

server.sendmail(sender_email, rec_email, message)
print ("Email sent to", rec_email)

