# Write a program which accepts one number and prints sum of first N natural numbers 

number = int(input("Enter number: "))
sum = 0
for i in range(1,number+1):
    sum = sum + i 

print("Sum: ",sum)
    