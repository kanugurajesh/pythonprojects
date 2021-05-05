import pyttsx3
import requests
import json
import time

url = ('https://newsapi.org/v2/top-headlines?'
	'country = in&'
	'apiKey =')

url +='c61863b01bf24e1aaafee2902b247db5'

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)
print(type(rate))
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.60)
print(type(volume))
sound = engine.getProperty ('voices');
engine.setProperty('voice', 'sound[1].id')


try:
	response = requests.get(url)
except:
	engine.say("can, t access link, plz check you internet ")

news = json.loads(response.text)
# news =response.json()
# the above line is written by me have a look at it
for new in news['articles']:
	print("##############################################################\n")
	print(str(new['title']), "\n\n")
	engine.say(str(new['title']))
	print('______________________________________________________\n')

	engine.runAndWait()

	print(str(new['description']), "\n\n")
	engine.say(str(new['description']))
	engine.runAndWait()
	print("..............................................................")
	time.sleep(2)
