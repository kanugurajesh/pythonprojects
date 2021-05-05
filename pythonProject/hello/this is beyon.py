# i am infinite
import  requests
import time
# hello guys we are going to create a newsreader
url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c61863b01bf24e1aaafee2902b247db5'
us = requests.get(url).json()
hello = us["articles"]
results = []
description = []
conclusion = []
jsonmaster = []
sir_what_do_you_want_to_hear_before_title = "headline"
sir_what_do_you_want_to_hear_before_description = "description"
sir_what_do_you_want_to_hear_before_conclusion = "conclusion"
for ar in hello:
    results.append(sir_what_do_you_want_to_hear_before_title+ar["title"])
for r in hello:
    description.append(sir_what_do_you_want_to_hear_before_description+str(r["description"]))
for c in hello:
    conclusion.append(sir_what_do_you_want_to_hear_before_conclusion+str(c["content"]))
# only minute mistakes change the entire game
#you can append values in a string
print(description)
# for i,z in range(len(results)),range(len(description)):
# jsonmaster.append([results[i],description[z]])
# the above code doesn't work so let's begin our journey
for i in range(len(results)):
    jsonmaster.append([results[i],description[i],conclusion[i]])
with open("shiva.txt", "w")as fr:
    # this is the data
    fr.write(str(jsonmaster))
# see the logic here is that the number of title here is equal to number of description
print(jsonmaster)
print("## sir a quick note ## the above one is today's news we need to look at it--")
from win32com.client import Dispatch
speak = Dispatch("SAPI.Spvoice")
speak.Speak(jsonmaster)
speak.Speak("sir my task is completed you can update me do change my posture in reading the news")
time.sleep(1)
speak.Speak("sir have a good day")
# you can use ctrl+f2 to stop the program
# the above is a bunch of code used to pronounce some words we need to have a clear view on it to need it
# see how it works we are going to creating a news reader so let's reading a good news we are going
# sir we need to do more in news reading we need to learn more about we need to have a clear idea on it
