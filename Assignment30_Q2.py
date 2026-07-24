# Program that displays current date and time after evey one minute
import schedule
import time
import datetime

def Display():
    print("Current Date and time: ",datetime.datetime.now())

def main():
    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()