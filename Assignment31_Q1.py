import schedule
import time
def Display(message):
    print(message)

def main():
    message = input("Enter Message to be Displayed: ")
    interval = int(input("Enter interval in seconds: "))

    if interval >0 :

        schedule.every(interval).seconds.do(Display,message)
    else:
        print("Interval should be greater than 0")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()