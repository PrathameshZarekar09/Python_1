import os
import schedule
import time
import datetime

def DeleteEmptyFiles(DirectoryName):

    if not os.path.exists(DirectoryName):
        print("Directory does not exist.")
        return

    for FolderName, SubFolders, FileNames in os.walk(DirectoryName):

        for FileName in FileNames:

            FilePath = os.path.join(FolderName, FileName)

            try:
                if os.path.getsize(FilePath) == 0:

                    os.remove(FilePath)

                    with open("DeletedFilesLog.txt", "a") as fobj:
                        fobj.write(f"Deleted File : {FilePath}\n")
                        fobj.write(
                            f"Deleted Time : {datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}\n"
                        )
                        fobj.write("-" * 40 + "\n")

                    print("Deleted :", FilePath)

            except PermissionError:
                print("Permission denied :", FilePath)

            except Exception as e:
                print("Unable to delete :", FilePath)
                print("Error :", e)


def main():

    DirectoryName = input("Enter Directory Path : ")

    schedule.every(1).hours.do(DeleteEmptyFiles, DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()