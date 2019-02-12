
#2 ==========

import requests

def content(site):

	return site.text



site = requests.get('https://en.wikipedia.org/robots.txt')

print(content(site))




#3 ===========



def title(data):

	if title in data:

		return title.content



site2 = requests.get('http://www.example.com/')

#print(site2.headers)

print(title(site2))



#4



import json



def quantity(response):

  a = response.json()

  return a ['data']



site3 = requests.get('https://analytics.usa.gov/data/live/realtime.json')

print(quantity(site3))

