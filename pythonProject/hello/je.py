# i am infinite
# hello guys today we are going to import
# this is one of the things you can use in your life it is web browser
import webbrowser
webbrowser.open("https://stackoverflow.com/questions/45105135/redirecting-to-a-website-in-python")
# the above code is used to web search
usr = "https://financialmodelingprep.com/developer/docs/"
import requests
sp = requests.get(usr)
print(sp.text)
# using this you can print the content of the code
# we have used many functions
datat = {"hello":2,"man":5}
spr = requests.post(url=usr,data=datat)
print(spr.text)
# you can't post the above values now because they're not yet ready
# generally this is used to to the server
# the above code is used for posting data to a server
