# Write a program which accepts one number and returns reverse of that number

def reverse(value):
    reverse = 0

    while value > 0:
        digit = value % 10
        reverse = reverse * 10 + digit
        value = value // 10

    return reverse


def main():
    number = int(input("Enter Number: "))

    ret = reverse(number)

    print("Reverse Number:", ret)


if __name__ == "__main__":
    main()