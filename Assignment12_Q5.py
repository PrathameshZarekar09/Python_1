# Write a program which accepts one number and prints that many numbers in reverse order

def main():
    number = int(input("Enter number: "))
    for i in range(number,0,-1):
        print(i)


if __name__ == "__main__":
    main()