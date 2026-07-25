import os
import schedule
import datetime
import time

def CountFiles(DirectoryName):

    if not os.path.exists(DirectoryName):
        print("Directory does not exist.")
        return

    FileCount = 0

    Data = os.listdir(DirectoryName)

    for Name in Data:
        Path = os.path.join(DirectoryName, Name)

        if os.path.isfile(Path):
            FileCount += 1

    Current = datetime.datetime.now()

    fobj = open("DirectoryCountLog.txt", "a")

    fobj.write(f"Directory Path : {DirectoryName}\n")
    fobj.write(f"Number of Files : {FileCount}\n")
    fobj.write(f"Date and Time : {Current.strftime('%d-%m-%Y %I:%M:%S %p')}\n")
    fobj.write("-" * 40 + "\n")

    fobj.close()

    print("Directory scanned successfully.")


def main():

    DirectoryName = input("Enter Directory Path : ")

    schedule.every(5).minutes.do(CountFiles, DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()