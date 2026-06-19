# 1. Write a program to display: Value,Type,Memory address for a variable using appropriate built-in function
age = 10
print("Age: ",age)
print(type(age))
print(id(age))


# 6. Write a program that accepts two numbers from user and prints their: add,sub,multi,div 
print("Enter 1st number: ")
num1 = int(input())

print("Enter 2nd number: ")
num2 = int(input())

add = num1 + num2
sub = num1 - num2
mult = num1 * num2 
div = num1 / num2 

print("Addition :",add)
print("Subtraction: ",sub)
print("mult: ",mult)
print("Division: ",div)


# 9. Write a program to take user's name and age and display
print("Enter your Name: ")
name = input()
print("Enter your Age: ")
age = int(input())
print("Hello ",name,"you will turn ", age+1, "next year")