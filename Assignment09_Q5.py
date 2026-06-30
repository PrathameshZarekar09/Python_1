#Write a program which accepts one number and checks whether it is divisible by 3 and 5 


#Scripting

number  = int(input("Enter a number: "))
if (number % 3 == 0 and number % 5 == 0):
    print(number," is .divisible by 3 and 5")
else:
    print(number," is not divisible by 3 and 5")




#Procedural

'''def Divisible(no):
    return (no % 3 == 0 and no % 5 == 0)


def main():
    value = int(input("Enter the number: "))
    Ret = Divisible(value)

    if (Ret == True):
        print(value," is divisible by 3 and 5")
    else:
        print(value," is not divisible by 3 and 5")

main()'''
