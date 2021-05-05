from win32com.client import Dispatch
speaker = Dispatch("SAPI.SpVoice")
speaker.speak("hello i am ori")
speaker.speak("rule on my command")
exit = False
while not exit:
    s= input("hello please enter your input")
    speaker.speak(s)
    if s=="bye":
        exit=True
import json
import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=c61863b01bf24e1aaafee2902b247db5')
response = requests.get(url)
print(response.json())




# To stop the program press
# CTRL + Z

