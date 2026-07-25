import os
import shutil
import schedule
import time
import datetime

def CopyFiles(Source, Destination):

    try:
        if not os.path.exists(Source):
            print("Source directory does not exist.")
            return

        if not os.path.exists(Destination):
            print("Destination directory does not exist.")
            return

        Data = os.listdir(Source)

        for FileName in Data:

            SourcePath = os.path.join(Source, FileName)

            if os.path.isfile(SourcePath) and FileName.endswith(".txt"):

                try:
                    DestinationPath = os.path.join(Destination, FileName)

                    shutil.copy(SourcePath, DestinationPath)

                    with open("CopyLog.txt", "a") as fobj:
                        fobj.write(f"File Copied : {FileName}\n")
                        fobj.write(
                            f"Time : {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n"
                        )
                        fobj.write("-" * 40 + "\n")

                    print("Copied :", FileName)

                except Exception as e:
                    print("Unable to copy", FileName)
                    print("Error :", e)

    except Exception as e:
        print("Error while processing directory :", e)


def main():

    Source = input("Enter Source Directory : ")
    Destination = input("Enter Destination Directory : ")

    schedule.every(10).minutes.do(CopyFiles, Source, Destination)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()