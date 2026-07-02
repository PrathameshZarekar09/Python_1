# write a program which accepts one number and prints sum of digits
def digitsum(value):
    sum = 0

    while value > 0:
        digit = value % 10
        sum = sum + digit
        value = value // 10

    return sum


def main():
    number = int(input("Enter Number: "))

    ret = digitsum(number)

    print("Sum of digits:", ret)


if __name__ == "__main__":
    main()
