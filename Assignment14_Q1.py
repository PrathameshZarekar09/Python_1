# Write a lamda function which accepts one number and return square of that number
def main():
    square = lambda x: x * x

    number = int(input("Enter number: "))

    result = square(number)

    print("Square:", result)


if __name__ == "__main__":
    main()