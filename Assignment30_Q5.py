# Schedule a task that executes every five minutes 
import schedule
import datetime
import time

def Display():
    fobj = open("Marvellous.txt", "a")
    fobj.write(f"Task Executed at: {datetime.datetime.now()}\n")
    fobj.close()
def main():
    schedule.every(5).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()