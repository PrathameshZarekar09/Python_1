# Write a program which accepts a one number and checkes ehether it is perfect number or not

def perfect(n):
    if n <= 1:
        return False

    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum = sum + i

    return sum == n


def main():
    number = int(input("Enter number: "))

    if perfect(number):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")


if __name__ == "__main__":
    main()