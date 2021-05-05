# list1 = ["hello","bye"]
# print(list1)
# x = ",".join(list1)
# print(x)
# print("see we have done with the value")
# guys i am just reviewing some code please wait
# we are going to create some programs
# hello guys we are going to crate a program
# this is a program
import json
import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=c61863b01bf24e1aaafee2902b247db5')
response = requests.get(url)
from win32com.client import Dispatch
speakers = Dispatch("SAPI.SpVoice")
speakers.speak(json.dumps(response.text))
# let's see how json works
li = {"hello":"bye","json":"a type of module"}
# hello guys we are going to create a program
# you need to learn modules on your own
print(li["hello"])
li = '{"hello":"bye","json":"a type of module"}'
# using loads you can parse the above string
rp = json.loads(li)
print(li) # you can also print this way but you cannot parse the code in this way
print(li)
print(rp["hello"])
lis = {
    "fridge":("hello",540),
    "heroism":False
}
x = json.dumps(lis)
print(x)