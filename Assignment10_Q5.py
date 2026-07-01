#Write a program which accepts one number and print all odd number till that number

number = int(input("Enter number:  "))
print("Odd numbers till ",number," are :")
for i in range(1,number+1,2):
    print(i)
    