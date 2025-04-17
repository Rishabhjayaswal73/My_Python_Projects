import time
import winsound


def alarm_clock():
  print("Welcome to the simple alarm clock!")


alarm_time = input("Enter your alarm time in(HH:MM:SS):")

while True:
  current_time = time.strftime("%H:%M:%S")


  print(f"Current time :{current_time}",end = "\r")


  if alarm_time == current_time:
    print("\nTime to wake up!The alarm is getting off!")

    winsound.Beep(2000,4000)


    break


  time.sleep(1)

alarm_clock()
