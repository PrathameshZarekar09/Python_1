maxnum = lambda a, b: a if a > b else b

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    result = maxnum(x, y)

    print("Maximum number:", result)


if __name__ == "__main__":
    main()