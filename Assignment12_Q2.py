# Write a program which accepts one number and prints its factor


def factors(value):
    print("Factors are:")

    for i in range(1, value + 1):
        if value % i == 0:
            print(i)


def main():
    number = int(input("Enter Number: "))

    factors(number)


if __name__ == "__main__":
    main()