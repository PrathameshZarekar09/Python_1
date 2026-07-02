# Write a program which accepts one number and checks whether it is prime or not 

def Prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def main():
    n = int(input("Enter number: "))

    if(Prime(n)): 
        print("Number is prime")
    else:
        print("Number is not prime")

if __name__ == "__main__":

    main()
 