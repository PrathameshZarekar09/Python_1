# Write a lamda function which accepts one number and return cube of that number
def main():
    cube = lambda x: x * x * x

    number = int(input("Enter number: "))

    result = cube(number)

    print("cube:", result)


if __name__ == "__main__":
    main()