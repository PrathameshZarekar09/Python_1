import os
import schedule
import datetime
import time

def MonitorFile(FileName):

    if not os.path.exists(FileName):
        print("File does not exist.")

        fobj = open("FileSizeLog.txt", "a")
        fobj.write(f"File Path : {FileName}\n")
        fobj.write("Status : File does not exist.\n")
        fobj.write(f"Date and Time : {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n")
        fobj.close()

        return

    Size = os.path.getsize(FileName)

    Current = datetime.datetime.now()

    fobj = open("FileSizeLog.txt", "a")
    fobj.write(f"File Path : {FileName}\n")
    fobj.write(f"File Size : {Size} bytes\n")
    fobj.write(f"Date and Time : {Current.strftime('%d-%m-%Y %I:%M:%S %p')}\n")
    fobj.close()


def main():

    FileName = input("Enter File Path : ")

    schedule.every(30).seconds.do(MonitorFile, FileName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()