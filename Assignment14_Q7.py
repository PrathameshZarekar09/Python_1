divisible = lambda x: x % 5 == 0

def main():
    number = int(input("Enter number: "))

    if divisible(number):
        print("divisible by 5")
    else:
        print("not divisible")


if __name__ == "__main__":
    main()