import os 

def main():
    File = str(input("Enter File name to be searched: "))
    ret = os.path.exists(File)

    if (ret == True):
        print("File is there")
    else:
        print("File is not there")

if __name__ == "__main__":
    main()