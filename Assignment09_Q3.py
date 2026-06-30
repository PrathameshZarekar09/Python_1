# Write a program which accepts one number and prints square of that number 

# Scripting
'''number = int(input("Enter Number: "))
square = number*number
print("Square of ",number," is : ",square)'''

#Procedural
def Square(value):
    return value*value

def main():
    number1 = int(input("Enter number: "))
    Ret = Square(number1)

    print("pSquare of ",number1," is: ",Ret)

main()