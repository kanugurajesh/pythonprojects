# i am infinite
# hello guys today we are going to create a command line utility
# this is also going to be a faulty calculator
# 56 +1 = 58,54-1 = 52,67*2 = 144,56/2 = 26
import argparse
import sys
def cla(arga):
    if args.o=="add"or args.o =="+":
        return args.x + args.y
    elif args.o=="sub" or args.o=="+":
        return args.x - args.y
    elif args.o=="div" or args.o=="/":
        return args.x / args.y
    elif args.o=="mul" or args.o=="*":
        return args.x * args.y
    else:
        print("i think something went wrong")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=20,help="sir please input the numbers")
    parser.add_argument('--y', type=float, default=20, help="sir please input the numbers")
    parser.add_argument('--o', type=str, default="add", help="sir please input the numbers")
    args = parser.parse_args()
    sys.stdout.write(str(cla(args)))
# the above values are only responding when -- this is added before variables in this code and executed using
# this same type it is not executed if we use x variable in this code and call it using same variable
# see we have completed the program in this lines now we have to execute it to test whether it runs or not
# concentration is the best thing to learn anything
# HELLO GUYS TODAY WE ARE GOING TO WRITE A PROGRAM NOW WE WILL BE WRITING IN A AMAZING WAY SO BE READY
