# display message to user according to current system time
from datetime import datetime, timedelta
import pytz
name = input("Enter your name\n")
time = datetime.now()
if(time.hour < 12):
    print("Good morning ", end="")
elif (time.hour > 17 and time.hour < 20):
    print("Good evening",end="")
elif (time.hour>12):
    print("Have a good day ",end="")
print(name)
