#Write a program which accepts one number and print all even number till that number

number = int(input("Enter number:  "))
print("Even numbers till ",number," are :")
for i in range(2,number+1,2):
    print(i)
    