import sys

def main():
    File = str(sys.argv[1])

    fobj = open(File,"r")
    fobj1 = open("Demo.txt","w")

    Data = fobj.read()
    fobj1.write(Data)

    fobj.close()
    fobj1.close()




if __name__ == "__main__":
    main()