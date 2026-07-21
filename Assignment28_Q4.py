# Copy File Content into another

def main():

    file = input("Enter file :")

    file2 = input("Enter file name in which content to be copied: ")

    fobj = open(file,"r")
    fobj1 = open(file2,"w")

    Data = fobj.read()

    fobj1.write(Data)

    fobj.close()
    fobj1.close()


if __name__ == "__main__":
    main()