mult = lambda a, b: a * b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = mult(x, y)

    print("Multiplication:", result)


if __name__ == "__main__":
    main()