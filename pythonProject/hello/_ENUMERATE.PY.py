# i am infinite
# hello guys in this tutorial we are going to implement enumerate function which gonna be good
list1 = ["shiva","bholenath","kameshwar"]
i = 0
for item in list1:
    print(i,item)
    i+=1
# see we have printed the functions now we are going to be little advanced
# see enumerate function is lot more easier than running a for loop and making a mess out there
for index,value in enumerate(list1,start=1):
    print(index,value)
list2 = ["mahadev","shivshankar","vishwanath","maheshwar"]
i = 0
for item in list2:
    if i%2 is not 0:
        print(item)
    i+=1
# in this above code when ever for loop runs the i value is incremented to one
# you can also decrement the value
# playing with code is fun
# always have a good concentration level to unlock the universe
# if you own logic you can build anything you want logic is the main key to everything in programming
for index,value in enumerate(list2):
    if index%2 ==0:
        print(value)
list3 = ["ori","jarvis","not"]
for index,value in enumerate(list3,start=0):
    print(index,value)
for index,value in enumerate(list3,start=0):
    if index/2==1:
        print(value)
# there are many uses of enumerate functions we need to learn about them
