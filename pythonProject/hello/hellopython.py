# i am infinite
# i am going to prepare a program related to comprehension
intx = input("sir please enter the value(enter int values(0-infinity))  :")
i = 0
list1 = []
while i<int(intx):
    ori = input("please enter the value")
    list1.append(ori)
    i+=1
inta = input("sir please enter the type of categorisation")
if inta=="set":
    print(set(list1))
elif inta == "list":
    print(list1)
elif inta == "tuple":
    print(tuple(list1))
else:
    print("sir please enter the input")
# hello guys finally we have wrote the program
