even = lambda x: x % 2 == 1

def main():
    number = int(input("Enter number: "))

    if even(number):
        print("True (odd Number)")
    else:
        print("False (even Number)")


if __name__ == "__main__":
    main()