def main():

    file = input("Enter file name")

    string = input("Enter string")

    fobj = open(file,"r")

    Data = fobj.read()

    count = Data.count(string)

    print("count is : ",count)

    

if __name__ == "__main__":
    main()