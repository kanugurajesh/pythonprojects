# i am infinite
# hello guys today we ar going to create a program to list all our files to captalize
import os
# so let's create a program
#
import json
import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=c61863b01bf24e1aaafee2902b247db5')
response = requests.get(url)
print(response.json())

import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=c61863b01bf24e1aaafee2902b247db5')
response = requests.get(url)
print(response.json())
import requests

url = ('http://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2021-02-09&'
       'sortBy=popularity&'
       'apiKey=c61863b01bf24e1aaafee2902b247db5')

response = requests.get(url)

print(response.json)
# you can go to get api and get some codes and use it in your applications
import requests

url = ('http://newsapi.org/v2/everything?''q=tesla&''from=2021-01-09&''sortBy=publishedAt&''apiKey=c61863b01bf24e1aaafee2902b247db5')

response = requests.get(url)
json.dumps(response)

print(response.json)
# news api is like a search engine for news
# see we are done with code so let's go with programming
# we are going to learn about articles
