# i am infinite
# hello guys today we are going to write a program
# hello guys today we are going to learn about anonymous functions and have to acquire a good skill
# ax = lambda n,n2,n3:n*n2*n3
# print("this is a lambda function",ax(5,6,7))
# # lambda function is also similar to a function but in this synario you do not have to you def
# a =[[1, 14], [5, 6], [8,23]]
# a.sort(key=lambda x:x[1])
# print(a)
# # here key says in which way to sort
# # hello guys this is one of the programs you can use
# # this function is somewhat crazy we need to have a good look at it
# print(a.sort())
# # the above code returns None value
# list2 = [2,3,4]
# list2.sort(key=lambda x:x**2,reverse=False)
# print(list2)
# # in this we understood that sort according to given things
# # sorting is one of the things you can do to make your code more good looking
# # HELLO GUYS THIS IS ALL ABOUT CODING
# # we are going to build code so let's begin our code
# # a = list(map(lambda x : x **2),list2)
# items = [1, 2, 3, 4, 5]
# # b = list(map(lambda x:x**2,items))
# # the above function squares the value
# bx = list(map(lambda z:z^4,items))
# print(bx)
# the above function is somewhat peculiar have a look at it later to increase your perceptability on it
# print(b)
# # a=list(map((lambda x: x **3), items))
# # print(a)
# # #Output: [1, 8, 27, 64, 125]
# umpteen = [1,5,6,7,8,9]
# c = list(map(lambda y:y*2,umpteen))
# print(c)
# map() is one of the function we can use to call function and use it in our list
# hello guys now we are going to define a filter function
list1 = [1,2,3,4,5]
list3 = [5,6,7,8,4]
list5 = []
for items in list1:
    for value in list3:
        if items==value:
            list5.append(value)
print(list5)
# finally sir we have dealt with all the values
# see finally we have done our value
# hello guys now we are going to set default values
# the above code can also be written as
za = list(filter(lambda x:x in list1,list3))
print(za)
# see man finally we are gone with the value
# SEE FINALLY WE ARE DONE WITH FILTER FUNCTION
from functools import reduce
b =  reduce(lambda x,y:x*y,list1)
print(b)
for items in str(b):
    print(b)
# now i have understood how this function works and have a full quality understanding on it
# see finally we are done with the value
# the main function of reduce is to reduce the value given as input into a single element
# hello guys now we are going to write a lamda function
list1 = [1,2,3,4,5]
list2 = []
def funct(items):
    return items*2
for items in list1:
    list2.append(items*2)
print(list2)
list56 = [5,6,7,8,9,0]
list6 = []
for items in list56:
    list6.append(funct(items))
print(list6)
# if you have completed the value let's finish it
# see you can also write the code in this way
# this codes are good
