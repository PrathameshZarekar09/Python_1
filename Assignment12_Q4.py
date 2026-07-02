# Write a program which accepts one number and prints that many numbers starting from 1
def main():
    number = int(input("Enter number: "))
    for i in range(1,number+1):
        print(i)


if __name__ == "__main__":
    main()