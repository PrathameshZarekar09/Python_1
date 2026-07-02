even = lambda x: x % 2 == 0

def main():
    number = int(input("Enter number: "))

    if even(number):
        print("True (Even Number)")
    else:
        print("False (Odd Number)")


if __name__ == "__main__":
    main()