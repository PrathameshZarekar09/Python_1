# write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number

def ChkGreater():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if (num1 > num2):
        print("First number ",num1," is greater")

    else:
        print("Second number ",num2, " is greater")


if __name__ == "__main__":
    ChkGreater()