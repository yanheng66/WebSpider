import requests
import re


url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=CPSC&course=310&section=202'
html = requests.get(url)

pattern = re.compile(r'(?<=left&\S39;><strong>).*?(?=</strong></td></tr>)')
matches = pattern.finditer(html.text)

print (type(matches))

count = 1
for match in matches:
	if count == 3:
		print (match)
		count = count +1

	else: 
		count = count +1