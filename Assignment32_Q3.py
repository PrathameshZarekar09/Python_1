import os
import schedule
import time

def ReadFile(FileName):

    try:
        if not os.path.exists(FileName):
            print("File does not exist.")
            return

        fobj = open(FileName, "r") 

        Data = fobj.read()

        if len(Data) == 0:
            print("File is empty.")
        else:
            print("\nFile Contents:")
            print(Data)

    except PermissionError:
        print("Permission denied. Cannot access the file.")

    except FileNotFoundError:
        print("File not found.")

    except Exception as e:
        print("File cannot be opened.")
        print("Error :", e)


def main():

    FileName = input("Enter Text File Path : ")

    schedule.every(1).minutes.do(ReadFile, FileName)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()