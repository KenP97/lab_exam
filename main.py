import sys
from Addition import Addition
from Subtract import Subtract
from Multiplication import Multiplication



print("Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")


i = sys.argv[1] #input("Enter your option between 1-3 : ")

if(i=="1"):
    op = Addition()
elif(i=="2"):
    op = Subtraction()
elif(i=="3"):
    op = Multiplication()
else:
    print("Wrong input given")
    sys.exit(0)

    
a = int(sys.argv[2])  #int(input("value for A :"))
b = int(sys.argv[3])  #int(input("value for B :"))
print(op.operation(a,b))
