# testing! 

# imports
from datetime import datetime
import threading

# function to call when timer happens 
def print_message(i):
    print("hello there! counter= " + i)


# time testing function
def do_time_testing():
    current_time = datetime.now()

    # cut the time down to a less precise string for comparsion
    current_time = current_time.strftime("%H:%M")

    print(current_time)

    # in 24 hour format!!!
    test_time1 = "12:00"
    test_time2 = "15:12"

    # test
    if current_time == test_time1:
        print(True)
    else:
        print(False)

    # test
    if current_time == test_time2:
        print(True)
    else:
        print(False)


# init and start the timer 
t = threading.Timer(3, print_message())     # delay, function call
t.start()

# run a loop 
i = 0
while True:
    # just like do a thing
    i += 1

    if i is 5:
        do_time_testing()

