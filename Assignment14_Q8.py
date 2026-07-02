add = lambda a, b: a + b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = add(x, y)

    print("Addition:", result)


if __name__ == "__main__":
    main()