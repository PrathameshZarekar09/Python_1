# Write a program which accepts one number and print count of digits in that number

def count(value):
    count = 0

    if value == 0:
        return 1

    while value > 0:
        value = value // 10
        count = count + 1
    return count

def main():
    number = int(input("Enter Number: "))
    ret = count(number)
    print("Count of digits:", ret)


if __name__ == "__main__":
    main()