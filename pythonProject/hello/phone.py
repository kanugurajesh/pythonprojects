# i am infinite
# hello guys we are going to write a program which is going to show whether the phone number which is inputed in the input is really a phone number or not
import re
hello = "555-555-5566"
if re.search("\w{3}-\w{3}-\w{4}",hello):
    print(hello,"is a phone number")
# this is used to find whether the phone number which is inputed is a phone number or not
enter_phone_number = """555-555-5566
555-555-5566
555-555-5566
555-555-556
555-555-5566
555-555-5566"""
# this is the program which shows whether the input is a phone number or not
# you need to prepare a caller which can call a person and find his take carings
x = re.findall("\w{3}-\w{3}-\w{4}",enter_phone_number)
for i in x:
    print("this phone number is real"+i)
# see you have finally made a caller which can be used to make something
# actually we can prepare anything using python
json = "hello"
x = re.findall("[^he]",json)
p = "".join(x)
print(p)
# see carrot function has many uses you can use this function to do many things so you can use it to increase your performance
# we can do many things in python


