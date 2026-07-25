import schedule
import datetime
import time

def CreateFile():
    Current = datetime.datetime.now()

    FileName = "File_" + Current.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName, "w")
    fobj.write(f"Filename : {FileName}\n")
    fobj.write(f"Creation Date : {Current.strftime('%d-%m-%Y')}\n")
    fobj.write(f"Creation Time : {Current.strftime('%I:%M:%S %p')}\n")

    print("File Created :", FileName)

    fobj.close()


def main():
    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()