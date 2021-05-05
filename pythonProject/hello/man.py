# i am infinite
# hello guys today we are going to create some programs
# hello guys we have wrote a program which is very good
import time
input()
f = open("myfile.txt","r+")
for line in f:
    out = line.title()
    print(out)
time.sleep(5)
w = open("myfile.txt","w")
for line in f:
    outa = line.title()
    outaa = line.title()
    w.write(outa)
    time.sleep(1)
    c = open("myfile.txt","a")
    for line in c:
        w.write(outaa)