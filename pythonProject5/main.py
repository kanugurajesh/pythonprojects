# i am infinite
# i can do anything
# always pay heed to minute things
# infinity is my habit
numbers = int(input("please enter the value : "))
def function1(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
# vey minute  things are very necessary
# indentation are very necessary in the process
# print(function1(numbers))
def function2(n):
    """ this function is about recursions"""
    if n==1:
        return 1
    else:
        return n*function2(n-1)
# print(function2(numbers))
def function3(n):
    """ this function is about inputing the index and gaining the number of fibonacci """
    # always pay heed to minute things
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return function3(n-1)+function3(n-2)
print(function3(numbers))
 # 0,1,1,2,3,5,8,13 this is fibonacci sequence
    #  from here 1 => index is 1 and continues on later
    # fibonacci series is one of the best series