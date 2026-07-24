# Write a script that schedules the following tasks:
# print lunch time! everyday at 1:00 pm 
# print Wrap up work everyday at 6:00 pm

import schedule
import time

def Lunch():
    print("Lunch Time!")

def Wrap():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(Lunch)

    schedule.every().day.at("18:00").do(Wrap)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()