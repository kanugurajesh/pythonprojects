# i am infinite
# hello guys today we are going to learn about dictionary some examples so let us look at it
# always concentrate to learn
import re
dict1  = {}
hello = "muster"
dict1[hello] = "r"
print(dict1)
# this is also one of the things you need to know about dictionary but no problem at least you have learn't it now
# so guys let's write a code that we gonna use now
dict2 = {}
spr = "Hello value is 200 and Justice value is 500 and Minister value is 100 and Pm value is 100"
histam = re.findall(r'\d{1,3}',spr)
mahesh = re.findall(r'[A-Z][a-z]*',spr)
vis = 0
for everthing in mahesh:
    dict2[everthing] = histam[vis]
    vis+=1
# the above for loops generate values for a dictionary we need to have a clear view on it
print(dict2)
# see guys this is one of the things you can learn to make use of your
dict3 = {"json":"man"}
print(dict3["json"])
dict3["minister"] = "hello"
# the above code can be used to assign value to the dictionary we need to have close look at it
print(dict3)
# hello guys in this code let's build a thing which gives information if we type the password so let's view it
r = input("please ")
if re.search(r"inform",r):
    print("hello sir you know the password")
# this is like simple lock for the program you can use to clear your concepts
r = re.findall(r"machine",r"hello guys machines can be used to complete tasks and they are used by humans machines and humans work together")
for s in r:
    print(s)
# the above things print the code
# rp = re.search(r"sp",r" this is good sp is sp")
# for s in rp:
#     print(rp)
# search object is not iterable
# findall method is used to generate lists
# hello guys let's generate an iterator using finditer method
sp = re.finditer("sper","hello sper , sper , sper,")
for r in sp:
    print(r)
# finditer gives you an complete information about the value you need if it is present in the string
# hello guys let's look at another example
strp = "Sat,Hat,Mat,Kat"
sprp = re.finditer(r"[SHMK]at",strp)
for s in sprp:
    print(s)

# using the above iterator you can print many value
# now let's write another program
# we need to be sure about the program we are going to use to

# the input in the bracket should be only be of capital and from accending order
p = "Minist,Arrest,Linguist,Jewel"
q = re.finditer(r"[A-J][a-z]*st",p)
# every single mistake has a huge impact in programming you need to be cautious and very good at it to function it
for i in q:
    print(i)
# regular expression is all about finding a pattern and executing it using manu inbuilt functions in re modules
# so let's go onto another
qp = "sat mat food cat dog"
pr = re.compile(r"[f]ood")
regex = pr.sub(r"rat",qp)
if pr.search("food"):
    print("hello man")
# the extension of above code is regex = re.compile(r"[f]ood").sub(r"rat","sat mat food cat dog")
print(regex)
# see we have finally completed our work now let
print(pr)
# now guys let's look at another type of operation we need to have a clear vision on it
hello_python = "json is a \\done"
print(hello_python)
# the above code gives value json is a \done
# so to solve it we need to use
print(re.search(r"\\done",hello_python))
# now the above code gives the below value
# <re.Match object; span=(10, 15), match='\\done'>
# print(re.search("\\done",hello_python))
# when we will not use r before"" the output is none for the above code
# its because it thinks\\done here it highlights \\d as a function so to solve this we use r""
# super computers are one of the craziest things you can never have
# so let's begin our work
finda = """shiva is great
rudra is miraculous
mahadev is benevolent
"""
print(finda)
x =re.compile(r"\n")
xr = x.sub(r"  ",finda)
print(xr)
# hello guys we are going to create a new variable let's learn about it
list2 = "12345"
print("matches:",len(re.findall("\d",list2)))
# finally we have completed the above one
print("matches:",len(re.findall("\d{5}",list2)))
print("matches:",len(re.findall("\d{2}",list2)))
list3 = "34567890"
print("matchboxes",len(re.findall("\D",list3)))
# in the above code the \D returns everything except digits
list4 = "123 1234 12345 123455 12345689"
print("money:",len(re.findall("\d{5,7}",list4)))
# the above code specifies the range of the digits which need to be present
print("hello:",len(re.findall("\d{5}",list4)))
# the above code has worked
# really regular expressions are very good

