import os
import schedule
import time
import datetime

def ScanDirectory(DiractoryName):
    FileCount = 0
    DirCount = 0

    if not os.path.exists(DiractoryName):
        print("Directory does not exist.")
        return

    Data = os.listdir(DiractoryName)

    for Name in Data:
        Path = os.path.join(DiractoryName, Name)

        if os.path.isfile(Path):
            FileCount = FileCount + 1
        elif os.path.isdir(Path):
            DirCount = DirCount + 1

    print("Directory Scanned :", DiractoryName)
    print("Total Files :", FileCount)
    print("Total Subdirectories :", DirCount)
    print("Scan Time :", datetime.datetime.now())


def main():
    DiractoryName = input("Enter Directory Path : ")

    schedule.every(1).minutes.do(ScanDirectory, DiractoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()