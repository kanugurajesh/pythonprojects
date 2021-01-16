# hello guys now i am going to write a faulty calculaor program
# 56/2 = 24,36/2= 19,32*2 = 60,4+4 = 9
# lets begin our faulty calculator program
print("hello welcome to the  calculator lets begin our journey with the following words")
print("hello please enter the first value")
firstvalue = int(input())

print("please enter the the operator")
operator = input()

print("hello please enter the second number")
secondnumber = int(input())

print("here is your calculation")


if firstvalue == 56 | secondnumber == 2  | operator == "/":print(24)
elif firstvalue == 36 | secondnumber == 2 | operator == "/":print(19)
elif firstvalue == 32 | secondnumber == 2 | operator == "*":print(60)
elif firstvalue == 4 | secondnumber == 4 | operator == "+" :print(9)
elif operator == "+":
    addition = int(firstvalue+secondnumber)
elif operator == "-":
    subtractin = int(firstvalue-secondnumber)
elif operator == "*":
    multuplication = int(firstvalue*secondnumber)
elif operator == "/":
    division = int(firstvalue/secondnumber)

if firstvalue != 56 | secondnumber != 2   | operator != "/" : print(addition)
if firstvalue != 32 | secondnumber == (2) | operator == "*" : print(subtractin)
if firstvalue != 4  | secondnumber == (4) | operator == "+" : print(multuplication)
if firstvalue != 4  | secondnumber != 4   | operator != "+" : print(division)
