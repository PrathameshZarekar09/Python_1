# Display File Line by Line
def main():
    file = input("Enter File: ")

    fobj = open(file,"r")

    data = fobj.read()

    print("Data of file",file, "\n")
    print(data)

if __name__ == "__main__":
    main()