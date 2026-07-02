# Write a program which accepts one number and checks whether it is palidrom or not

def palindrome(value):
    original = value
    reverse = 0

    while value > 0:
        digit = value % 10
        reverse = reverse * 10 + digit
        value = value // 10

    return original == reverse


def main():
    number = int(input("Enter Number: "))

    if palindrome(number):
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")


if __name__ == "__main__":
    main()