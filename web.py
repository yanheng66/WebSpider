import requests
import re
from pick import pick
import smtplib
import time

SubjectCode = input(str("Enter the Subject Code (example: CPSC): "))
CourseNum = input(str("Enter the Course Number (example: 310): "))
SectionNum = input(str("Enter the Section Number (example: 201): "))

title = 'Please choose your required seat type: '
options = ['Generalseats', 'Restrictdedseats']
selected = pick(options, title, multi_select=False, min_selection_count=1)
SeatsType = selected[0]
Email = input(str("Enter your Email(dont need to include www): "))

before = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept="
url = before + SubjectCode + "&course=" + CourseNum + "&section=" + SectionNum

def geturl():
	global html
	html = requests.get(url)

def SearchforGen():
	pattern_Gen = r'(?<=General\sSeats\sRemaining:</td><td\salign=&#39;left&\S39;><strong>).*?(?=</strong></td></tr>)'
	global html
	global match_Gen
	match_Gen = re.search(pattern_Gen, html.text, re.M|re.I)
	Gen_Rr = match_Gen.group(0)
	return Gen_Rr

def SearchforRes():
	pattern_Res = r'(?<=Restricted\sSeats\sRemaining\S:</td><td\salign=&#39;left&\S39;><strong>).*?(?=</strong></td></tr>)'
	global html
	global match_Res
	match_Res = re.search(pattern_Res, html.text, re.M|re.I)
	Res_Rr = match_Res.group(0)
	return Res_Rr

def sendmail():
	global done
	sender_email = "houhouhahaheihei@gmail.com"
	rec_email = Email
	password = "1234qwerxxxx"
	message = "we have a seat for ya"

	if SeatsType == 'Generalseats':
		Gen_R = SearchforGen()
		if int(Gen_R)> 0 : 
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(sender_email, password)
			print ("login success")
			server.sendmail(sender_email, rec_email, message)
			print ("Email sent to", rec_email)
			done = True
		else:
			done = False
	else:
		Res_R = SearchforRes()
		if int(Res_R) > 0 : 
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(sender_email, password)
			print ("login success")
			server.sendmail(sender_email, rec_email, message)
			print ("Email sent to", rec_email)
			done = True
		else:
			done = False


done = False
number = 1
while done == False:
	geturl()
	sendmail()
	number = number +1
	print (number)
	time.sleep(3)
	










