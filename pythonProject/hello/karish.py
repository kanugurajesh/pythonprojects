# i am infinite
# hello this is about printing a star pattern
# this is all about programming
# hello this is programming
# you could print many programs
def hellish():
    sp = input("hello please enter the input of the pattern you want to print")
    rp = input("no of lines you want to print the input ")
    fifty = input("sir please enter the value whether you want to print the value in same or inverse order ( s for same /and int for inverse order: ) ")
    if fifty == "s":
        for i in range(0,int(rp)):
            i= i + 1
            print(i * sp, end=" \n")
    elif fifty == "int":
        for i in range(int(rp), 0, -1):
            print(i * sp, end=" \n")
            continue
    else:
        print("sir your value is not appropriate")
hellish()
exit_time=False
while exit_time is False:
    hello = input("thank you sir if you want to run this program again input ag or if you want to exit the program enter va")
    if hello == "ag":
        hellish()
    elif hello == "va":
        print("thank you sir you are welcomed again")
        exit_time=True
    else:
        print("sir your value is not appropriate")