import sys

def main():
    File1 = str(sys.argv[1])
    File2 = str(sys.argv[2])

    fobj1 = open(File1,"r")
    fobj2 = open(File2, "r")

    if (fobj1.read() == fobj2.read()):
        print("Success")
    else:
        print("Failure")


if __name__ == "__main__":
    main()