# Write a program that performs a file backup every hour 
#incomplete
import os
import datetime
import time
import schedule
import shutil


def backup(Source_File,Destination):
    time = datetime.datetime.now()

    File = os.path.basename(Source)
    Name, Extension = os.path.splitext(File)

    backupname = f{datetime.datetime.now()}


def main():
    Source_File = input("Enter Source File Path: ")
    Destination = input("Enter the Destination: ")

    schedule.every(1).hours.do()



if __name__ == "__main__":
    main()