# Write a program which accepts a file name from the user and counts how many lines are present in the file 
try:

    file = str(input("Enter File name: "))

    fobj = open(file,"r")

    count = 0

    for i in fobj:
        count = count+1

    print("Total count : ",count)

    fobj.close()

except FileNotFoundError:
    print("Enter appropriate file name")

