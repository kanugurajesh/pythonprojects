# hello guys today we are going to create a pickle program
# what does pickle generally mean?
# pickle generally means to store data in a security form it gives you some type of security let's deal with pickle
import pickle
shivansh = ["rudra","mahakaal"]
with open("shivam.txt",'wb') as f:
    pickle.dump(shivansh,f)
    f.close()
with open("shivam.txt") as r:
    print(r.read())
with open("shivam.txt","rb") as r:
    # print(r.read())
    # the below function only functions when we leave the above code commented
    x = pickle.load(r)
    print(x)
# generally there are many exceptions in using pickle because when we change ide version the pickling process get wrong
# sir we need to learn about many modules and we need to have an clear idea about them

with open("done.txt","w") as r:
    r.write("r")
    r.close()
with open("done.txt") as f:
    print(f.readline())
    print(f.read())
# have a look at this file later you need to good racap over this one to understand better
# now we are going to prepare a program

