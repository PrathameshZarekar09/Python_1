import schedule
import datetime
import time

def CreateLog():
    Current = datetime.datetime.now()

    FileName = "Marvellous_Log_" + Current.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj =  open(FileName, "w")
    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time: ")
    fobj.write(Current.strftime("%d-%m-%Y %I:%M:%S %p"))
    fobj.close()

    print("Log File Created :", FileName)


def main():
    schedule.every(10).minutes.do(CreateLog)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()