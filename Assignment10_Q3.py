# Write a program which accepts one number and prints factorial of that number

number = int(input("Enter number: "))
fact = 1
for i in range(1,number+1):
    fact = fact*i
    
print("Factorial: ",fact)