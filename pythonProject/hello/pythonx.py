# i am infinite
# hello guys we today we are going to prepare a library
# hello guys we are going to create a python program
# this is our program
# if you own logic you can build anything so let's get into the work
import os
list2 = []
exit = False
exi = False
def function(filelocation):
    sp = open(filelocation)
    os.chdir(filelocation)
    sr = os.listdir(filelocation)
    for files in sp:
        if files in sr == files in list2:
            pass
        else:
            x = os.rename(files,files.title())
            print(x)
while not exit:
    ina = input("sir please enter the words you want to secure from captalizing,sir you can enter exit to exit the loop: ")
    list2.append(ina)
    if ina == "exita":
        exit = True
while not exi:
    list1 = []
    inext = input("sir please enter the directory from beginning sir you can type exit to end the recursion: ")
    list1.append(inext)
    if inext=="end":
        try:
            x = ",".join(list1)
            function(x)
        except:
                exi = True

# C:\Users\Bunny\PycharmProject\pythonProject\hello
function("pythonProject")