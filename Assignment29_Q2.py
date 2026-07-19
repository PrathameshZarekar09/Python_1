def main():
    File = str(input("Enter File name to be displayed: "))

    fobj = open(File,"r")
    Data = fobj.read()
    print(Data)
    fobj.close

if __name__ == "__main__":
    main()