# i am infinite
# hello guys today we are going to create a file in python
import os
# os.chdir("C:\New folder.\hello.py")
# with open(r"C:\New folder.\hello.py") as f:
#     print(f.read())
# with open("sample.txt","x") as r:
#     print(r.read())
# the above code doesn't work as file already exists we need to work on it more to develop our skills
# with open("hi.txt","x") as p:
#     print(p.write("hello man"))
# the below mode is used to read and write
# hello guys now we are going to learn about encode which is used to encode values so let's begin our encoding
# strint = "python is greatt"
# print(strint.encode("utf-8","ignore"))
# print(strint.encode("utf-8","replace"))
# # both of the above codes have a lot of difference we need to have a good understanding of them so let's begin our tut
# # ignore statement ignores the unencodable string value
# # while replace replaces the unencodable string value with ?
# # and there are also many things you can use in mode like things
#
# with open("sample.txt","r+b") as f:
#     print(f.read())
# # this file gives encoded value in binary form
# # hello guys now we are going to use a split function in python
# with open("helloman.txt.txt") as r:
#     for line in r:
#         print(line.split())
# # split is used to split the line of a program in to a list
# f = open("helloman.txt.txt", mode = "r", encoding = 'utf-8')
# print(f.read())
# generally encoding type is utf-8 so it is recommended to use this type
# hello guys generally sys module is
import sys
# def print_value(*a):
#     print(*a,file=sys.stderr)
# print_value("hello man this is rajesh")
# so generally this is all about this function let's have a closer look on it
# this is a error this is passed to it
# hello guys now we are going to deal with command line arguments
import sys
print("initializing...")
num = len(sys.argv)
print("hello guys the number of inputs is equal to ",num-1)
sum = 0
sums = 1
pixel = int(sys.argv[1])
missile = int(sys.argv[1])
print("the name of the file you opened is",sys.argv[0])
print("the arguments you have gave has input into the computer is",end=" ")
for i in range(1,num):
    print(sys.argv[i],end="  ")
for i in range(1,num-1):
    sum+=int(sys.argv[i])
    sums*=int(sys.argv[i])
for i in range(2,num-1):
    pixel/=int(sys.argv[i])
    missile%=int(sys.argv[i])
print("\n sir the result is...")
if sys.argv[num-1]=="add" or sys.argv[num-1]=="+":
    print("the sum of the value of the given input is ",sum)
elif sys.argv[num-1]=="mul"or sys.argv[num-1]=="*":
    print("the multiplication of the value of the given input is ",sums)
elif sys.argv[num-1]=="div" or sys.argv[num-1]=="/":
    print("the division of the value of the given input is ",pixel)
elif sys.argv[num-1]=="%":
    print("the modulus of the value of the given input is ",missile)
else:
    for i in range(1,num):
        sum+=int(sys.argv[i])
    # finally we are dealt with the values
    print("the sum of the results is ", sum)
    print("sir we cannot provide you / and % service now")
    print("sir we cannot provide you this service")
    print("good bye sir")
# see finally we have build thec module and we need to have a full information reagarding it