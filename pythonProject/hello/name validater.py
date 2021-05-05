# i am infinite
# hello guys we are going to create a program which finds whether the name which is input in the program is valid or not
import re
name_of_the_person = "dhruva vijay"
if re.search("\w{2,20}\s\w{2,6}",name_of_the_person):
    print("the name "+ name_of_the_person +" is valid")
# program which is used to find names of multiple things
names_of_the_person = """ori  dhruva
rudra  veena"""
x = re.findall("\w{2,20}\s\s\w{2,10}",names_of_the_person)
# number of spaces also varies we need to have a clear vision on them
for i in x:
    print("the name "+i+" is valid")
# hello guys we have finally found a program which finds whether the name of the person inputed in the program is valid
# hello guys we are going to write a program which finds whether the email which is given as input in the program
email_of_the_person = "hello@gmail.com"
xr = re.findall("[\w.%+-]{1,20}@[\w.-]{1,20}.[A-Za-z]{2,3}",email_of_the_person)
py = "".join(xr)
# you can generally use join method to join the list and convert list to string
print("magic "+str(py))
# really regulations and expressions is a vast topic
# there is also way to use urllib.request you can just learn about it in another session