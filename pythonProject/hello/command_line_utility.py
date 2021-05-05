# i am infinite
# hello guys today we are going to create a command line utility
# this is also going to be a faulty calculator
# 56 +1 = 58,54-1 = 52,67*2 = 144,56/2 = 26
import argparse
import sys
def cal(args):
    if args.o=='add':
        if args.x == 56 and args.y == 1:
            return 58
        else:
            return args.x + args.y
    elif args.o == 'sub':
        if args.x == 54 and args.y == 1:
            return 52
        else:
            return args.x - arga.y
    elif args.o == 'mul':
        if args.x== 67 and args.y==2:
            return 144
        else:
            return args.x *args.y
    elif args.o=='div':
        if args.x==56 and args.y==2:
            return 26
        else:
            return args.x / args.y

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type=float
                        ,default=2.0,help="for more help call to our center add lines")
    parser.add_argument('--y',type=float
                        ,default=12.0,help="you can call to our mobile center for more help")
    parser.add_argument('--o',type=str,default='add'
                        ,help="enter operand for more information you can call to us")
    arga = parser.parse_args()
    sys.stdout.write(str(cal(arga)))
