
#3

import requests

def title(data):
		text_from_site = data.text
		file_with_site_content = open('text_for_work.txt', 'w')
		file_with_site_content.write(data.text)
		file_with_site_content.close()
		file_with_site_content = open('text_for_work.txt', 'r')
		for line in file_with_site_content:
			if '<title>' in line:
				return line




		text = file_with_site_content.readlines()
		if '<title>' in file_with_site_content:
			return line
		

site2 = requests.get('http://www.example.com/')
#print(site2.headers)
print(title(site2))