# Write a program which accepts one number and prints addition, suntraction, multiplication, and division

def calculation(value1, value2):
    add = value1 + value2
    sub = value1 - value2
    mul = value1 * value2
    div = value1 / value2

    print("Addition      :", add)
    print("Subtraction   :", sub)
    print("Multiplication:", mul)
    print("Division      :", div)


def main():
    number1 = int(input("Enter First Number: "))
    number2 = int(input("Enter Second Number: "))

    calculation(number1, number2)


if __name__ == "__main__":
    main()